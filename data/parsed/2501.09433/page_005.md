<tbc>**Advantages of Spatially Decoupled Attention.** The proposed mechanism allows each view’s spatial region to be processed independently within the same U-Net architecture, preserving view-specific details and ensuring consistency across perspectives. Therefore, it can utilize large pre-trained generative models like ControlNet or SDXL [32] without any architectural modifications or finetuning.

Intuitively, this approach _amplifies_ low-quality, geometry- unaligned multi-view guide images to high-quality, geometry-aligned multi-view images in a single diffusion process. Unlike conventional MVDiffusions, which require modified U-Net architecture and extensive retraining, the proposed method generates consistent, high-fidelity textures in a model-agnostic manner, bypassing traditional limitations.

### 3.2.2 Occlusion Inpainting

In the initial texture generation, we create four orthogonal images for 3D geometry, which are then back-projected to produce a coarse-textured mesh. However, due to the limited number of views, occlusions inevitably arise in regions not visible from these views. To address this issue, we propose a novel 3D-aware occlusion inpainting algorithm.

**3D-Aware Occlusion Mapping and Inpainting.** As discussed in Section 2.3, existing occlusion inpainting methods have challenges for speed or locality bias. To overcome these issues, we propose a more adaptive, geometry-aware occlusion inpainting approach.

This method identifies and isolates the untextured regions on the mesh surface, targeting only the areas affected by occlusion. To capture the occluded areas more accurately, we employ _k_-means clustering using the face normal orientations and spatial coordinates of untextured faces on the 3D mesh surface. This clustering process yields several repre<tbc>

<tbc>sentative cluster centroids, each corresponding to a distinct occluded region on the mesh. For each centroid, we define a viewpoint on the unit sphere that faces the untextured area, projecting the coarse-textured mesh from this viewpoint to capture a region-specific view of the occlusion.

We then aggregate these projections onto a single 2D plane, creating a _specialized UV map_ dedicated solely to inpainting occluded areas. Unlike traditional UV maps, this occlusion-specific UV map maintains a more accurate representation of locality on the mesh surface, thus preserving the spatial coherence required for 2D inpainting methods. By leveraging this UV map, we use the same 2D diffusion model for texture generation and inpainting. This approach yields a high-fidelity, 3D-aware texture that effectively fills occluded regions. Empirically, we found that _k_=6 covers most occluded areas, and further apply the extrapolation technique for other remaining regions. Figure 4 illustrates the 3D-aware occlusion inpainting scheme.

## 4 . Experiments

### 4.1 . Implementation Details

**Dataset.** We utilize the Objavese [8] dataset for ShapeVAE and 3D latent diffusion training. We preprocess this dataset by filtering out low-quality, non-manifold meshes, retaining 150K high-quality objects with high CLIP [34] scores.

**Geometry Generation.** We employ a perceiver-based [15] transformer architecture for ShapeVAE, as used in Michelangelo [63], modifying it with Fourier featuring and spherical harmonics encoding. For the multi-view guided 3D latent diffusion stage, we adopt a U-Net-based transformer. The entire training takes around 8 days on 32 NVIDIA A100 GPUs. Finally, we integrate a custom-trained MVDiffusion model,<tbc>

positive
11
12
9
9
Image Encoder
9
12
14
9
9
Low-Quality MV images
negative
Spatially Decoupled Attention
9
X
Decoupled Attention map
ht
[hf, hh]
ht = [hf, hy hh, hh]
Input Rendered view
High-Quality Mesh-Aligned Images
In Denoising U-Net

Occlusion-Aware Viewpoint Clustering
Specialized UV
2D Inpainting
Final Mesh
Occlusion Normal
Occlusion Point

Figure 3. **Spatially Decoupled Cross Attention.** To produce high- quality multi-view images for a given geometry, we design a model-agnostic Spatially Decoupled Cross Attention. During cross- attention in denoising U-Net, we replicate hidden feature channels so that each duplicated channels focuses solely on the designated view. Since the design is model-agnostic, we can utilize an external ControlNet to guide the textures aligned with the input mesh.

Figure 4. **3D-Aware Occlusion Inpainting.** First, we cluster the normal and spatial coordinates of the occluded face. Using clustered centers as viewpoints, we create specialized UV maps through projection mapping. This approach captures surface locality, allowing 2D diffusion-based inpainting to effectively fill occluded regions. Note that this UV map is utilized solely for occlusion.

