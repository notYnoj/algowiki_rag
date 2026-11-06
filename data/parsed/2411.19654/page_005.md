<tbc>where ‘R’ and ‘M’ denote roughness and metallic, respectively. We further apply the MSE loss on the alpha image for faster convergence of the shape:

\(L_\alpha=L_\text{MSE}(I_\alpha,I_\alpha^\text{GT}).\) (5)

To accelerate the coverage process, we also apply the 3D MSE loss _L_<sub>3D</sub>, which calculates the difference between predicted parameters of 3D Gaussians and pre-fitting ones. Finally, the complete loss function of our model is defined as the sum of all the above losses:

\(L_\text{total}=L_\text{albedo}+L_\text{R}+L_\text{M}+L_\alpha+L_\text{3D}.\) (6)

### 3.4 . Texture and Material Baking

In the inference stage, we also first build the corresponding octree for the input 3D mesh. Then, we use our trained octree-based 3D U-Net to generate 3D Gaussian on every octant and rasterize them from multiple views. The ultimate output of our method should be a global texture map and material map. Thus, we rasterize the input mesh using the differentiable renderer \[24\] and optimize its albedo, roughness and metallic parameters via the MSE loss between the Nvdiffrast \[24\] rendering results and 3D Gaussian rendering results. With adequately optimized implementation, this process takes only about several seconds to bake the multi- view images to an untextured 3D model. After the optimization, our input mesh paired with its albedo and material map is capable of performing physically based rendering in new illumination environments.

## 4 . Experiments

### 4.1 . Implementation Details

#### Dataset

We train our TexGaussian model on two publicly-available datasets: ShapeNet \[7\] and Objaverse \[13\]. For 3D objects in the ShapeNet dataset, since they only contain albedo maps without PBR materials, our model is trained to generate RGB textures only. We train our model on four categories of ShapNet: `bench`, `car`, `chair` and `table` which is consistent with previous works \[26, 55\]. We curate a subset of Objaverse models encoded with PBR materials and convert those using the specular-glossiness workflow to the metallic-roughness workflow to achieve a consistent PBR representation. This process resulted in a total of 29,200 models. For each 3D object, we render its RGBA albedo image, roughness map, and metallic map from 64 views of 512<sup>2</sup> for training.

#### Network Architecture

Our 3D U-Net is built upon octree-based convolutional neural networks \[49\] which only operates on non-empty octree leaf nodes. The depth of our constructed octree is set to 8 (resolution 256<sup>2</sup>). Our 3D U- Net consists of 5 down-sampling and up-sampling blocks.

For the text-conditioned generation, cross-attention layers are only inserted at the last two down-sampling blocks, the middle block, and the first two up-sampling blocks. The input channel of our 3D U-Net is set to 4, where 3 for normal vector and 1 for local displacement while the output channel is set to 13 as mentioned above. The resolution of 3D Gaussian Splatting is set to 512<sup>2</sup>. The resolution of the baked albedo and material map is set to 1024<sup>2</sup>.

#### Training Details

We train our model in a single-category and unconditional manner on ShapeNet, i.e., there are 4 TexGaussian models without text conditions in total. This per-category model is trained on 4 NVIDIA A100 (40G) GPUs for about 2 days and is set up for a fair comparison with other existing methods trained on ShapeNet. For the Objaverse dataset, we train a text-conditioned TexGaussian model for PBR material generation on 24 NVIDIA A100 (40G) GPUs for two weeks. For each batch, we randomly sample 8 camera views to calculate loss functions. We adopt the AdamW \[27\] optimizer with a learning rate of \(4\times 10^{-4}\), a weight decay of 0.05, and betas of (0.9,0.95). The learning rate is cosine annealed to 0 during the training and we clip the gradient with a maximum norm of 1.0.

#### Evaluation metrics

To effectively assess the quality of our generative results, we adopt the metric proposed by \[61\]. Specifically, each mesh with the generated PBR material is rendered from 20 uniformly distributed views to get multi-view albedo maps, and PBR rendering results in a new illumination environment. These images are used to calculate the FID \[36\] and KID \[2\] scores against those from ground truth to evaluate the quality and diversity of generative PBR materials. For the ShapeNet dataset, we only use albedo maps. The final score is averaged across 20 views, and a lower FID and KID score indicates better generation quality and diversity.

### 4.2 . Unconditional RGB Texture Generation

We conduct unconditional RGB texture instead of PBR material generation on four categories of the ShapeNet dataset. We use the same train and test data split as in \[26, 55\]. Fig. 3 shows the unconditionally generated RGB texture by our single-category model with high quality, fidelity, and diversity. It can be seen that the texture map synthesized by our method is of great 3D global consistency with the corresponding input geometry.

#### Quantitative Comparison

We conduct quantitative analysis and comparison on our model and other state-of-the-art methods. Specifically, we compare our model with Point- UV Diffusion \[55\] and TexOct \[26\] which also train single- category models on ShapeNet. We also compare with some methods using pre-trained 2D diffusion prior for multi- view images synthesis such as TEXTure \[55\], Text2Tex \[8\]<tbc>

