<tbc>ever, existing methods are either limited to object-level rigid transformation \[15, 85, 93\], not generalize to out-of- distribution categories \[7, 8, 10, 37, 45, 66, 66, 73, 76\], restricts its representation to simple shapes \[79\] or orthographic projection \[55\], or does not support fine-grained texture editing \[12, 33, 37, 44, 48, 64, 89, 92, 94, 95, 96\]. In contrast, we pick up the triangle mesh as a scaffold to encode the scene, since the mesh can be edited conveniently and intuitively in mature industry software, and the region of interest on the mesh can be precisely selected by vertices. Built upon this, our method delivers the capability of non-rigid geometry editing and fine-grained texture editing.

## 3 METHOD

We introduce NeuMesh++, a novel scene representation that encodes a neural radiance field at a mesh-based scaffold. As demonstrated in Fig. 2, instead of learning the entire scene as a whole in a coordinate-based network, we leverage 3D mesh structure by decomposing the scene into a set of local-vertex-bounded radiance fields (Sec. 3.1), where each vertex stores geometry, texture and semantic information of its neighboring local space. Motivated by previous works \[40, 54, 74\], we adopt the volume rendering technique to render pixels, and employ the photometric loss and other regularizations to encode the neural radiance field into the mesh surface (Sec. 3.2). In this way, the scene representation is locally aligned to the mesh, and the geometry and color are encoded in separated latent spaces, which naturally inherits the approaches of mesh-guided geometry deforming and designatable texture editing (Sec. 3.3, Sec. 3.4). To accomplish semantic-guided editing with a user-friendly click, we assign semantic code for each vertex and propose a semantic propagation algorithm for automatic area selection (Sec. 3.5). Besides, our method can achieve efficient rendering and editing and a graphical user interface is developed for interactive editing. (Sec. 3.6).

### 3.1 Neural Mesh-based Radiance Field

We use a mesh-based scaffold to model the neural radiance field, as depicted in Fig. 2. First, we acquire the mesh of the object using out-of-box Neuralangelo \[32\] and marching cubes \[38\]. To accomplish disentangled geometry and texture representation along with semantic-guided selection, we replace the NeRF-like MLP with several groups of latent codes on the mesh vertices and decoders to model the geometry, texture, and semantic attribute of the object independently. Specifically, we store a set of learnable parameters for each vertex **v** on the mesh, including a geometry code **_l_**_<sup>g</sup>_, a texture code **_l_**_<sup>t</sup>_, a modification color **_c_**_<sup>m</sup>_ and a semantic code **_l_**_<sup>s</sup>_ (**_l_**_<sup>s</sup>_ helps to identify the different semantic regions of objects and will be introduced in Sec. 3.5). The surface-bounded latent codes on mesh vertices can facilitate a greater degree of flexibility and fine-grained control when editing the neural field.

Following the volume rendering techniques, we cast the physical ray into the scene and use the occupancy grid \[31\] to guide the sampling along the rays. The novel view is synthesized by:

\(\hat{C}(r)=\sum_{i=1}^NT_i\alpha_i\mathbf{c}_i,T_i=\prod_{j=1}^{i-1}(1-\alpha_j),\) (1)

where \(\alpha_i=1-exp(-\sigma_i\delta_i)\), _T_ is accumulated transmittance, \(\alpha\) is the opacity, \(\delta\) is the distance between adjacent samples along the ray, \(\hat{C}(r)\) is the rendered color of the ray **_r_**. \(\sigma_i\) and **c**_<sub>i</sub>_ are the predicted density and color respectively.

In the volume rendering process, we sample a series of sampling points along each pixel ray. For each query point **x**, we first find _K_ nearest vertices {**v**_<sub>k</sub>|k_=1,2_,...,K_} from the mesh scaffold vertices within a fixed radius \[18\]. Then, we calculate the distance between the query point to each neighboring vertex, and project the point **x** to the normal of each neighboring vertex **v**_<sub>k</sub>_ to obtain the normalized inverse distance \(w_k=\frac{1}{||\mathbf{v}_k-\mathbf{x}||}/(\sum_{i=1}^K\frac{1}{||\mathbf{v}_i-\mathbf{x}||})\) and projec tion distance along the vertex normal \(p_k=(\mathbf{v}_k-\mathbf{x})\cdot\mathbf{n}_k\), where **n**_<sub>k</sub>_ is the normal of vertex **v**_<sub>k</sub>_. Different from previous

Geometry  lg
nk
g
o, c, s
Ray Casting
PK
g
o
o
Texture  lt
Post-Interp.
W
w
k
Semantic  ls
k
y()
Geometry Decoder
Ray Distance
Modification Color cm
concat
hk
Volume Rendering
Per-Vertex Storage
Local Indicator hk
cm
Project Distance pk
t
k
ck
c
Inverse Distance wk
d
sum
Post-Interp.
Query point X
Vk
Neighbor Projection
N
Radiance Decoder
Mesh-based Scaffold
W
Interp. ls
S
Nearest K Vertex Search
Spatial Interpolation
Semantic Decoder
RGB & Semantic Rendering
Mesh-based Scene Structure
Disentangled Decoder

Fig. 2: **Overview.** We encode the neural radiance field on a mesh-based scaffold, where each vertex maintains a geometry, texture, and semantic code **_l_**_<sup>g</sup>,**l**<sup>t</sup>,**l**<sup>s</sup>_and a modification color **_c_**_<sup>m</sup>_ for high-fidelity texture editing. For a query point **_x_** along a casted camera ray, we retrieve codes and local indicators from the nearby mesh vertices, and forward to the geometry/radiance decoder to obtain density value \(\sigma_k\) and color **c**_<sub>k</sub>_ contributed by each neighboring vertex. Then a post- interpolation is applied to fuse them and obtain the final density \(\sigma\) and color **c** of the query point. Semantic information is decoded by the semantic decoder with the interpolated semantic code.

