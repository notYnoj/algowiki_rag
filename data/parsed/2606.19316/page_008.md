<tbc>mesh scaffold by gradually incorporating mesh vertices that exhibit proximity in both semantic attributes and spatial positions to the current cluster. A maximum cosine-similarity threshold is set to measure the similarity of semantic features and a searching radius is set to measure the spatial relation. This expansion process persists until there are no further vertices incorporated into the cluster. We show the examples of semantic selection in Fig. 5 and Fig. 6.

### 3.6 Efficient and Interactive Editing

In pursuit of efficient editing, two critical components must be addressed: the efficiency of rendering and the efficiency of the editing process. To enhance the rendering speed, we construct the neural architecture with compact latent codes and lightweight decoders, thereby minimizing time-consuming network queries. Additionally, we employ an occupancy grid to bypass unoccupied spaces, focusing sampling exclusively on the occupied grids. During the initial phase of training, the occupancy grid is initialized using the provided mesh scaffold, making the implicit field quickly concentrate near the mesh surface. NeuMesh++ can reach 15 fps on Nvidia GTX 4070 GPU when rendering \(800\times 800\) images. Regarding the efficiency of geometry editing, we should update the occupancy grid according to the deformed mesh which takes about 1 second. For texture swapping and texture filling, no extra fine-tuning is required. As soon as edited regions of original and reference objects are provided, we can immediately render the edited novel view. For texture painting, we only fine-tune the modification color (decoder-free) on the painted region which only takes about 1 second. For semantic-guided editing, it only takes about 2 seconds for the 3D semantic propagation from clicking on a single-perspective image.

Based on these efficient designs, we further develop a graphical user interface (GUI) to support the editing functionalities interactively. Please refer to the supplementary video for the interactive editing demo.

## 4 EXPERIMENTS

### 4.1 Datasets

We evaluate our method on the real captured DTU \[20\] dataset and NeRF \(360^\circ\) Synthetic dataset \[40\]. For the DTU dataset, we follow the setting of IDR \[89\] by using 15 scenes with images of \(1600\times 1200\) resolution and foreground masks for experiments. To facilitate the metric evaluation for novel view rendering, we randomly select 10% images as the test<tbc>

<tbc>split and use the remaining images for training. For NeRF \(360^\circ\) Synthetic dataset, we report testing metrics following official conventions.

### 4.2 Comparison of Rendering

As shown in Tab. 1, we compare our method with the SOTA editable neural rendering methods: NeuTex \[79\], NeuMainifold \[78\] , BakedSDF \[88\] and NeuMesh \[83\]. Besides, for reference, we also compare our method with the representative neural rendering method DVGO \[65\] and neural reconstruction method NeuS \[74\] , Neuralangelo \[32\] although these methods do not support geometry or texture editing. As the official code for BakedSDF \[88\] is not publicly available, we utilize its unofficial implementation \[90\] for this comparison. We denote it as BakedSDF\* in the s.

We first compare the rendering quality on NeRF \(360^\circ\) Synthetic dataset. Following previous works \[40, 74, 89\], we mainly use PSNR, SSIM and LPIPS to measure rendering qualities. As shown in Tab. 2, our method outperforms all editable neural rendering methods. For uneditable neural rendering methods, our method outperforms NeuS \[74\], and is comparable with DVGO \[65\], but slightly inferior to Neuralangelo \[32\]. Neuralangelo \[32\] adopts an implicit hash grid with volume rendering to pursue high-fidelity novel views but sacrifices real-time efficiency. On the contrary, NeuManifold deploys the mesh-based rasterization pipeline instead of the volume rendering to reach better efficiency but compromises the rendering quality due to the aliasing effect. Our approach strikes a balance between efficiency and quality by leveraging a compact mesh-based implicit representation, ensuring both efficient rendering and high-quality output. To achieve texture editing, NeuTex tries to memorize all textures in a single continuous UV- map by using a simplified Atlas-Net \[14\] (i.e., one atlas), which limits its representation of complex shapes. NeuS and NeuMesh model the scene using the SDF-based implicit field which produces smoother results but loses the detailed geometry and texture. In contrast, our method distributes the neural feature on a mesh scaffold and uses mesh-based volume rendering to aggregate the density and color values which preserves the high-frequency details and improves the visual quality.

To further validate our model, we exhibit foreground rendering metrics on the DTU dataset and compare with NeuS \[74\], DVGO \[65\], Neuralangelo \[32\], NeuTex \[79\], BakedSDF \[88\] and MeuMesh \[83\]. Since NeuManifold does not release the code or report the statistics on the DTU<tbc>

\begin{tabular}{ccccc}
Methods & Neural Architecture & Rendering Techniques & Geometry Editing & Texture Editing \\
DVGO \[65\] & Neural Radiance Field & Volume Rendering & & \\
NeuS \[74\] & Implicit SDF Field & Volume Rendering & & \\
Neuralangelo \[32\] & Implicit SDF Field & Volume Rendering & & \\
NeuTex \[79\] & Neural Radiance Field & Volume Rendering & & \(\unknown\) \\
NeuMainifold \[78\] & Mesh and Neural Texture & Mesh Rasterization & \(\unknown\) & \(\unknown\) \\
BakedSDF\* \[88\] & Mesh and Spherical Gaussians & Mesh Rasterization & \(\unknown\) & \(\unknown\) \\
NeuMesh \[83\] & Mesh-based Implicit SDF Field & Volume Rendering & \(\unknown\) & \(\unknown\) \\
Ours & Mesh-based Neural Radiance Field & Volume Rendering & \(\unknown\) & \(\unknown\) \\
\end{tabular}

TABLE 1: **Overview of comparison methods.** We compare our method with other methods on neural architecture, rendering techniques, and the ability of geometry and texture editing. The methods shaded in antique white represent neural implicit field approaches that lack editing capabilities, while the methods shaded in apricot correspond to neural rendering techniques with editing functionality.

