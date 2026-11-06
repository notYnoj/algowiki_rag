<tbc>significant strides. TEXTure \[61\] and Text2Tex \[7\] leverage pre-trained depth-to-image diffusion models \[93\], iteratively generating multi-view images from given camera trajectories and depth maps for texture baking. However, independently generated views suffer from severe consistency issues. Paint-3D \[90\] adopts a coarse-to-fine approach, introducing UV inpainting and UVHD diffusion models to refine incomplete regions and remove illumination artifacts in UV space. SyncMVD \[48\] enhances multi-view consistency by incorporating a texture synchronization module in latent space, while MVPaint \[12\] argues that latent space resolution (\(32\times 32\)) is insufficient for fine texture details and instead performs texture synchronization in image space with resolution (\(128\times 128\)), combined with 3D point cloud inpainting. This technique report follows the 3D diffusion generation paradigm to generate high-fidelity 3D shapes and textures compared to other state-of-the-art (SOTA) methods, and further involve controllable modules to improve the flexibility of the generation process.

## 3 Step1X-3D Geometry Generation

Step1X-3D is a flow-based diffusion model designed to generate high-fidelity 3D shapes from images, with support for multi-modal conditioning including text and semantic labels. The proposed geometry generation model builds upon prior latent set diffusion models such as Shape2VecSet \[91\], CLAY \[92\], Michelangelo \[95\], and Craftsman3D \[38\], utilizing a latent set diffusion framework with rectified flow for 3D shape generation.

In this section, we first introduce the data curation methodology for preprocessing in Sec. 3.1. Next, we provide a detailed description of the architectural design for both the Shape VAE and diffusion model components in Sec. 3.2. Additionally, inspired by the approach in CLAY \[92\], we present an adaptation of the LoRA \[25\] ecosystem for 3D generation in Sec. 3.3. All training code and sampled data will be made publicly available to support research and community development.

### 3.1 Geometry Data Curation

Recent years have witnessed the emergence of several large-scale open-source 3D datasets, including Objaveverse \[18\], Objaveverse-XL \[17\], ABO \[14\], 3D-FUTURE \[21\], ShapeNet \[5\], etc., which together contain more than 10 million 3D assets. However, as most of this data is sourced from the web- particularly the extensive Objaveverse-XL collection-the quality varies considerably. To ensure the data is suitable for training, we implemented a comprehensive 3D data processing pipeline that performs thorough preprocessing to curate a high-quality, large-scale training dataset.

Our curation pipeline consists of three main stages. First, we filter out low-quality data by removing assets with poor textures, incorrect normals, transparent materials or single surface. Second, we convert non-watertight meshes into watertight representations to enable proper geometry supervision. Third, we uniformly sample points on the surface along with their normals to provide comprehensive coverage for the VAE and diffusion model training. Through our comprehensive data processing pipeline, we successfully curated roughly 2 million high-quality 3D assets from multiple sources: extracting 320k valid samples from the original Objaveverse dataset, obtaining an additional 480k from Objaveverse-XL, and combining these with carefully selected data from ABO, 3D-FUTURE, and some internal created data.

#### Data Filter

The complete data filter process is shown in Fig. 3 (a). _(1) Texture Quality Filtering_: We render 6 canonical-view albedo maps for each 3D model. These rendered images are then converted to HSV color space for analysis. For each view, we compute histograms of the Hue (H) and Value (V) channels. Based on these histograms, we filter out textures that are either too dark,<tbc>

Image
Image
"Caption..."
Text
Step1X-3D Geometry Generation
Position
Step1X-3D Texture Generation
B-Box
Normal
More Conditions...
Untextured Mesh
Camera
Textured Mesh
Optional Conditions
Mesh Rendering

Figure 2: **Overall pipeline of Step1X-3D**.

