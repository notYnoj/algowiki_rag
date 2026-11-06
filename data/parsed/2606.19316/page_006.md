<tbc>material properties. We propose to mimic such pipelines by introducing a designatable texture editing, where the selection of mesh vertices is used to precisely guide the texture editing on the region of interest. The core step of our texture editing is that we update the texture code **_l_**_<sup>t</sup>_ and modification color **_c_**_<sup>m</sup>_ ("material properties") and the binding decoder _F<sub>R</sub>_ ("rendering palette") at the selected region. As shown in Fig. 4, we deliver three ways of texture editing as follows:

**1) Texture swapping** by exchanging textures between two objects through 3D geometry (e.g., swapping textures of two apples in Fig. 4). Users are first asked to mark out the source and target object on the mesh, which is accomplished by mature 3D model software, or point-based instance segmentation \[77\]. Then, given a putative point that matches with interactive annotation \[98\], we perform non- rigid 3D alignment using Umeyama \[71\] and ARAP \[63\] to align the target mesh’s edited region and the source mesh’s template region to be close in Euclidean space. Then, each vertex in the edited region searches for the closest 4 vertices inside the template region. The new texture code \(\mathbf{l}_k^{t^\prime}\) of each edited vertex is obtained by weighted-averaging of 4 searched template texture codes, where weights are the inverse distance between the edited vertex and the template vertex. We apply the same method to swap modification color \(\mathbf{c}_k^{m^\prime}\). Since the texture code \(\mathbf{l}_k^t\) of unedited regions and all geometry attributes (geometry codes and local indica<tbc>

<tbc>tors) are untouched in the target object, the modified color \(\mathbf{c}'_k\) becomes:

\(\mathbf{c}'_k=F_R\left(\mathbf{l}_k^{t^\prime},\mathbf{h}_k,\mathbf{d},\mathbf{n}_k\right)+\mathbf{c}_k^{m^\prime}.\) (7)

**2) Texture filling** by filling a target object area with repeated textures from a pre-captured model (e.g., assigning part<tbc>

Apple 1
Apple 1
Apple 2
Apple 2
Area selection (highlighted in red and yellow)
Area  Swapping (swap texture with fixed geometry)
Unwarp UV-map
Original Rendered Object
Interest Area Selection
Repeatedly Fill Texture on UV-map
Umeyama
Apple 1
ARAP
Apple 2
Non-rigid Alignment
Template Texture s & Decoders
Rendered Objects with Texture Swapped
Pre-captured Model
Object with Designated Texture Filling
(a) Texture Swapping
(b) Texture Filling
Spatial-Aware Fine-Tuning
TPAMI
TPAMI
TPAMI
TPAMI
TPAMI
Paint on a Single 2D view
Mask Rays for Supervision
Pre-compute Affected s (in red color)
Object with Transferred Painting
(c) Texture Painting

(a) Point Selection
(b) Propagated 3D Semantic Mask
(c) Texture Editing on Selected Region

Fig. 4: **Designatable texture editing.** By exchanging texture codes (and decoders), our representation delivers various texture editing pipelines on the neural implicit field.

Fig. 5: **Semantic-guided texture editing.** Users select a semantic region of the object by clicking from a single viewpoint and edit the texture of the selected 3D region.

