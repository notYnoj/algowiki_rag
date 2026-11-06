Tab. 11 ablates the encoding function applied to the interpolated features before the decoding MLP. We compare no encoding (identity), a ReLU activation, a cosine encoding, and a paired cosine-and-sine encoding.

### 3 2D Image Reconstruction Details

We provide additional details on the high-resolution HDR image fitting experiment summarized in the main paper. We adapt Neural Harmonic Textures to this domain while preserving the core idea: learnable per-vertex features, interpolated per pixel and activated with periodic functions, and decoded by a shallow MLP. However, there are a number of differences to the 3D and semantic reconstruction tasks, which we detail below.

#### 3.1 Representation

#### Triangle mesh.

Unlike the volumetric disconnected primitives used in the scene reconstruction tasks, the 2D image fitting experiment employs a _connected Delaunay triangulation_ that tiles the image plane without overlap. Every pixel belongs to exactly one triangle; there is no alpha blending, no Gaussian kernel, and no depth ordering. Vertices can be freely learned and positioned, and carry individual learnable feature vectors. Given a query pixel, its containing triangle is found via a tile-accelerated rasterizer, and the features at the triangle’s three vertices are interpolated to produce a per-pixel feature vector.

#### Clough-Tocher C<sup>1</sup> interpolation.

Standard barycentric (linear) interpolation produces a _C_<sup>0</sup> feature field: while continuous, the feature gradient is discontinuous across triangle edges. This turns out to be problematic when meshes are fully opaque, as it creates high frequency artifacts. Despite being followed by a frequency encoding and a nonlinear MLP, these gradient discontinuities manifest as visible seam artifacts along every edge.

To eliminate this, we replace linear interpolation with _Clough-Tocher cubic interpolation_, which constructs a degree-3 Bézier patch on each triangle from vertex values and vertex gradients, guaranteeing _C_<sup>1</sup> continuity everywhere (and \(C^\infty\) within each triangle). The 10 Bézier control points are:

\(c_{300}=f_0,c_{030}=f_1,c_{003}=f_2,\)<br>
\(c_{210}=f_0+\frac{1}{3}\nabla f_0\cdot\mathbf{e}_{01},c_{120}=f_1-\frac{1}{3}\nabla f_1\cdot\mathbf{e}_{01},\)<br>
\(c_{021}=f_1+\frac{1}{3}\nabla f_1\cdot\mathbf{e}_{12},c_{012}=f_2-\frac{1}{3}\nabla f_2\cdot\mathbf{e}_{12},\)<br>
\(c_{102}=f_2+\frac{1}{3}\nabla f_2\cdot\mathbf{e}_{20},c_{201}=f_0-\frac{1}{3}\nabla f_0\cdot\mathbf{e}_{20},\)<br>
\(c_{111}=\frac{1}{6}\big(c_{210}+c_{120}+c_{021}+c_{012}+c_{102}+c_{201}\big)\)<br>
\(-\frac{1}{6}\big(c_{300}+c_{030}+c_{003}\big),\) (7)

where _f<sub>i</sub>_ and \(\nabla f_i\) are the feature value and gradient at vertex _i_, and **e**_<sub>ij</sub>_=**v**_<sub>j</sub>_-**v**_<sub>i</sub>_.

