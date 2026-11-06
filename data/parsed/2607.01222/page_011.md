<tbc>**Textured Voxelization from Dense-View Images.** We first convert the dense-view image set O into a _textured voxel representation_ based on the white- mesh geometry G to satisfy the input requirements of Trellis-2.

Concretely, given a set of occupied surface voxels \(\mathcal{V}=\{\mathbf{v}_m\}_{m=1}^M\) containing _M_ voxels (obtained by voxelizing the white-mesh geometry G), and a dense- view image set \(\mathcal{O}=\{\mathbf{O}_k\in\mathbb{R}^{H\times W}\}_{k=1}^K\) consisting of _K_ multi-view images, each with spatial resolution (_H,W_), our goal is to establish a globally optimal correspondence between the _M_ voxels and the \(H\times W\times K\) image pixels. In other words, each voxel is assigned the color of one pixel selected from the dense-view image set. This correspondence should minimize texture seams while respecting geometric visibility constraints.

To this end, we formulate the problem as a _graph-matching_ task and optimize the following objective using a Markov Random Field (MRF) over the 6-connected voxel graph E:

\(min_{\{k_m\}_{m=1}^M}\sum_{m=1}^MD_m(k_m)+\lambda\sum_{(m,n)\in\mathcal{E}}w_{m,n}\mathbf{1}[k_m\neq k_n],\) (8)

where \(k_m\in\{1,\dots,K\}\) is the assigned view index for voxel **_v_**_<sub>m</sub>_. By determining _k<sub>m</sub>_, voxel **_v_**_<sub>m</sub>_ is explicitly assigned the pixel value **_O_**_<sub>k<sub>m</sub></sub>(i<sub>m</sub>,j<sub>m</sub>_), where (_i<sub>m</sub>,j<sub>m</sub>_) represents the 2D projected coordinates of the voxel in the _k<sub>m</sub>_-th view. The data term (the first term) _D<sub>m</sub>(k<sub>m</sub>_) evaluates the geometric visibility and projection reliability of this specific pixel, which is measured based on the angle between the voxel’s surface normal and the camera’s viewing direction. The smoothness term (the second term) utilizes color-gradient-adaptive weights _w<sub>m,n</sub>_ to penalize texture seams, which occur when adjacent voxels draw colors from different views (_i.e._, \(k_m\neq k_n\)). Finally, we optimize Eq. (8) via alpha-expansion \[5\] and fill any unobserved voxels via breadth-first color diffusion. After optimization, we obtain a textured voxel representation of the geometry, denoted as \(\mathcal{V}'\).

**Prior-Guided Denoising.** The original Trellis-2 model takes untextured voxels corrupted with randomly sampled Gaussian noise as input and gradually denoises them to produce textured geometry. As the denoising process progresses, the intermediate representations gradually accumulate texture information.

In our setting, however, we already obtain textured voxels \(\mathcal{V}'\) that contain substantial texture information. This observation motivates us to leverage Trellis-2 to perform a _prior-guided denoising_ process. Specifically, as illustrated in Figure 3(b). we first use the Trellis-2 3D VAE encoder to extract latent representations from \(\mathcal{V}'\). We then perturb the latents with _mild_ Gaussian noise and feed the resulting mildly noisy latents into Trellis-2. Since the initialization is only mildly corrupted, the model performs only a few denoising steps (corresponding to the later stages of the original denoising trajectory) to generate the final textured geometry.

### 4 Experiment

**Implementation Details.** _OrbitPainter_ is trained on a subset of the Objaverse \[16\] and sketchfab \[45\] dataset, consisting of 60K samples with albedo

