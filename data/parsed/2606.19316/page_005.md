<tbc>methods \[74, 87, 89\] which directly function on the global coordinate **x**, we instead forward the local geometry code \(\mathbf{l}_k^g\), local texture code \(\mathbf{l}_k^t\) along with the local indicator vector **h**_<sub>k</sub>_=(_p<sub>k</sub>,w<sub>k</sub>_) to the geometry decoder _F<sub>G</sub>_ and radiance decoder _F<sub>R</sub>_ respectively:

\(\sigma_k=F_G\left(\mathbf{l}_k^g,\mathbf{h}_k\right),\mathbf{c}_k=F_R\left(\mathbf{l}_k^t,\mathbf{h}_k,\mathbf{d},\mathbf{n}_k\right)+\mathbf{c}_k^m,\) (2)

where \(\sigma_k\), **c**_<sub>k</sub>_ are the density and color value contributed by the neighboring vertex _v<sub>k</sub>_, and **d** is the viewing direction. Here \(\mathbf{c}_k^m\) is a decoder-free, view-independent color attribute. This decoder-free color is easy to modify without network fine-tuning and invariant to the view direction. This design facilitates the fidelity of texture editing as shown in Sec. 3.4. Besides, the inclusion of **h**_<sub>k</sub>_ complements the spatial distinguishability of the network query along the direction perpendicular to the surface (i.e., inside or outside the mesh) while avoiding hurting the locality of the representation.

Given the geometry and texture contribution of each vertex to the point **x**, we employ a post-interpolation strategy, conducting spatial interpolation to fuse the density and color from neighboring vertices:

\(\sigma=\frac{\sum_{k=1}^Kw_k\sigma_k}{\sum_{k=1}^Kw_k},\mathbf{c}=\frac{\sum_{k=1}^Kw_k\mathbf{c}_k}{\sum_{k=1}^Kw_k},\) (3)

where \(\sigma\) and **c** are the final density and color at point **x**. This strategy contributes to creating a group of "local neural fields" conditioned by the latent code on the mesh vertices. The final density and color come from the blending of the output of these "local neural fields". The local neural field can fully learn the high-frequency scene content in the vicinity of the mesh vertex, leading to higher rendering quality. Compared to NeuMesh \[83\], which utilizes the interpolated signed distance and latent codes to parameterize the whole space, we leverage local indicator **h**_<sub>k</sub>_ as input of the neural field to achieve a smoother spatial parameterization and avoid the sub-optimal convergence without the guidance of a teacher model.

## 3.2 Learning Mesh-based Radiance Field

The proposed neural mesh-based radiance field is learned directly given the input images and poses, which is different from NeuMesh \[83\] that needs a teacher model. Our method is robust to convergence without distillation and reaches comparable or slightly better rendering quality than training with distillation (See Sec. 4.6 and Tab. 5). Therefore, we employ the photometric loss on the batched ray **_r_**:

\(\mathcal{L}_\mathrm{f}=\sum_{\mathbf{r}\in R}||\hat{C}(\mathbf{r})-C(\mathbf{r})||_2^2+0.01\cdot\sum_{\mathbf{r}\in R}||\hat{C}^m(\mathbf{r})-C(\mathbf{r})||_2^2,\) (4)

where _C_ is the color of ground-truth images. We also accumulate interpolated modification color **_c_**_<sup>m</sup>_ along ray **_r_** to get \(\hat{C}^m(\mathbf{r})\) through Eq. 1. An option for the scene with the empty background is achieved by the mask loss:

\(\mathcal{L}_\mathrm{m}=\sum_{\mathbf{r}\in R}\mathrm{BCE}(\hat{M}(\mathbf{r}),M(\mathbf{r})),\) (5)

where \(\hat{M}(r)=\sum_{i=1}^NT_i\alpha_i\), _M_ is the ground-truth mask value.

As introduced in Sec. 3.1, our neural codes are tightly bound to the mesh surface. To ensure a smooth convergence, we apply a total variation loss on the latent codes by penalizing the differences between two neighboring codes:

\(\mathcal{L}_\mathrm{t}=\sum_{i=1}^N\sum_{j\in\mathrm{NR}(i)}|l_i-l_j|,\) (6)

where NR(_i_) contains the indices of closest _K<sub>tv</sub>_ vertex to **v**_<sub>i</sub>_.

## 3.3 Mesh-guided Geometry Editing

Since the neural radiance field has been tightly aligned to the mesh surface, any manipulation on mesh vertices would directly take effect on the field and the volume rendering results. Therefore, to perform geometry editing with a mesh- bounded radiance field, users are only required to edit the corresponding mesh, which is easily accomplished by interactively moving a few vertices with out-of-box mesh deforming methods (e.g., as-rigid-as-possible, or ARAP \[63\]), or 3D modeling software like Blender. We show an example of the geometry editing in Fig. 3, where we first deform the microphone by bending its head and lifting the wire on the corresponding mesh. Without any fine-tuning, the microphone’s radiance field has been deformed in the meantime, and we render deformed views (see Fig. 3). Thanks to the mesh-based workflow, we can bring some advanced physical simulation algorithms to the neural radiance field (see Fig. 7 (c)).

## 3.4 Designatable Texture Editing

Until then, the texture editing on the neural radiance model is still an open problem. Existing methods tend to replace the entire materials by swapping the appearance branch \[64, 89, 95\], changing a uniformed color \[37\], or learning an editable UV mapping for simple and plump shapes \[79\]. However, in practical texturing steps of the 3D modeling process, artists are used to working with a mesh-based workflow, which allows them to select a partial region of an object and modify it with arbitrary colors and

Original Mesh
Original Object Rendering
Deformed Mesh
Deformed Object Rendering

Fig. 3: **Mesh-guided Geometry editing.** By simply deforming the corresponding mesh, the change will synchronously take effect on the implicit field, and the rendered object will also be deformed accordingly.

