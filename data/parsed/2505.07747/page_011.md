<tbc>In details, to predict the multi-view latent output _z_<sub>_t_+1</sub>, we unproject the latent _z<sub>i,t</sub>_ of each view to texture space and P represents UV mapping function. Then, we obtain the synchronized texture \(T_{i,t}^{^\prime}\) by fusing multi-view _T<sub>i,t</sub>_ and weight different views in texture space with the cosine similarities between the ray direction and per-pixel normal map. Further, the synchronized latent \(z_{i,t}^{^\prime}\) is obtained by projecting the \(T_{i,t}^{^\prime}\) with UV rasterization function P. We formulate the whole procession of each denoise step as the following:

\(T_{i,t}=\mathcal{P}^{-1}(z_{i,t}),\) (6)

\(T_{i,t}^{^\prime}=\sum_{i=1}^Ncos(v_i,n_i)*T_{i,t},\) (7)

\(z_{i,t}^{^\prime}=\mathcal{P}(T_{i,t}^{^\prime}),\) (8)

\(z_{t+1}=D_{MV}(z_t^{^\prime},\mathcal{C}).\) (9)

### 4.4 Bake Texture

Following conventional texture baking workflows [90, 12, 94], we adopt standard texture processing operations on multi-view projections of the object and reuse the texture baker tools in Hunyuan3D 2.0 [94]. First, multi-view images were upsampled to achieve a \(2048\times 2048\) resolution and then are inversely projected onto the texture space. Due to occlusions and multi-view inconsistencies, this process inevitably introduces artifacts such as discontinuities and holes in the UV-mapped texture. To address this, we implement continuity-aware texture inpainting through iterative optimization, ensuring seamless texture synthesis across the entire surface. This post-processing stage effectively resolves topological ambiguities while preserving high-frequency texture details critical for photorealistic rendering.

## 5 Experiment

This section presents a comprehensive evaluation of the generation performance of Step1X-3D. First, we provide a detailed demonstration of Step1X-3D’s ability to generate geometry and texture conditioned on a single input image in Sec. 5.1. Next, we validate the model’s flexibility and controllability in Sec. 5.2. Finally, we conduct a thorough comparison between Step1X-3D and state-of-the-art (SOTA) methods, including both open-source (Trellis [85], Hunyuan3D 2.0 [71], and TripoSG [39]) and proprietary approaches (Meshy-4 <sup>3</sup>, Tripo-v2.5 <sup>4</sup>, and Rodin-v1.5 <sup>5</sup>), across three key dimensions: quantitative metrics, user studies, and visual quality in Sec. 5.3.

### 5.1 The Visual Quality Results of Step1X-3D Assets

To evaluate Step1X-3D, we present the generated 3D assets from both geometric and textural dimensions in Fig. 6 and Fig. 7, respectively. To better showcase geometric details, we render multi- view normal maps from the generated meshes for 3D geometry visualization. As shown in Fig. 6, the first and sixth columns display input images, while the remaining columns present multi-view representations of different objects. Our test objects cover a wide variety of styles (cartoon, sketch, and photorealistic), geometric complexity (flat surfaces, hollow structures, and detail-rich objects), and spatial configurations (single objects and multi-object compositions). Across this diverse input images, Step1X-3D geometry generation model not only maintains strong similarity between the 3D mesh and input image, but also reconstructs plausible spatial structures for occluded regions with reasonable geometric details. These results demonstrate the crucial role of our specifically designed 3D diffusion model and VAE architecture in Step1X-3D, along with the significant improvement in generalization capability enabled by large-scale high-quality training data. Fig. 7 further demonstrates Step1X- 3D’s texture generation capability through multi-view renders of textured 3D meshes. The texture generation model produces style-consistent textures across various input styles while maintaining high fidelity to the input image’s textural details. For occluded regions in the input image, by<tbc>

<sup>3</sup>The API was invoked from Meshy platform in May 2025. <sup>4</sup>The API was invoked from Tripo platform in May 2025. <sup>5</sup>The API was invoked from Rodin platform in May 2025.

