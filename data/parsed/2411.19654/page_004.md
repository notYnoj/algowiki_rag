## 3.2 . Octant-aligned 3D Gaussian Splitting

For a given mesh, we first sample _N_=100,000 3D points on its surface. The corresponding octree is then built by adaptively subdividing the voxels containing those points until the maximum depth is reached. As a result, all of the finest leaf nodes of octree lie along the boundary of the 3D object, which is consistent with the characteristic of the optimized 3D Gaussian. Therefore, we align a 3D Gaussian at the central position of each finest leaf node to effectively model the appearance without compromising the splatting quality. It is worth noting that we do not adjust the position of 3D Gaussians because they are already on the surface of 3D shape and adding additional offset relative to the octant center would not improve the rendering quality through our early experiments. To model PBR material that includes roughness and metallic information, we follow \[21, 44\] to append two additional channels at the end of 3D Gaussian parameters which are responsible for roughness and metallic map rendering, respectively.

For each 3D object in our dataset, we render multi-view images of albedo, roughness, and metallic maps for the training of 3D Gaussian. The multi-view rendering results of the albedo map are view-independent. So we just use three RGB channels to take the place of the original spherical harmonics. As noted, we exclude the position from 3D Gaussian parameters in our model. Thus, our 3D Gaussian parameters consist of 13 channels in total: one for opacity, three for scale, four for rotation, three for albedo, one for roughness, and one for metallic. To stabilize training, we choose to employ different activation functions compared to the original Gaussian Splatting \[22\]. Specifically, We multiply the softplus-activated scales **s**_<sub>i</sub>_ with 0.01, ensuring that the initial 3D Gaussians conform to the object’s counter of object at the beginning of training rather than expanding outward.

We pre-fitting the parameters of 3D Gaussians on the

constructed octree for each 3D object in our dataset via the original loss function in \[22\] on multi-view albedo images, roughness maps, and metallic maps:

\(L=(1-\lambda)L_1+\lambda L_{\text{D}-\text{SSIM}},\) (1)

where \(\lambda=0.2\).

## 3.3 . Octree-based 3D U-Net Training

To handle the encoding of our octant-aligned 3D Gaussian representation, we use the 3D U-Net built upon octree- based convolutional neural networks \[49\] to predict the Gaussian parameters. Inspired by LGM \[47\], the output feature of the 3D U-Net on each octant is treated as the 3D Gaussian parameters, which contain 13 channels, as discussed in the last subsection.

To effectively train our 3D U-Net, we adopt the regressive loss objective, which could further facilitate the generation process. The input to our octree-based 3D U-Net is the geometry feature on each octree’s finest leaf node, such as normal and local displacement. For text-conditioned PBR material synthesis, the text feature is extracted by pre- trained CLIP model \[39\] and is fed to U-Net via the octree- based multi-head cross attention mechanism similar to \[48\]. The predicted 3D Gaussians are rasterized from multiple views via Gaussian Splatting \[22\]. At each training step, we rasterize the albedo images, alpha images, roughness and metallic maps from randomly selected eight views. Following \[47\], we apply the mean square error (MSE) loss and the VGG-based LPIPS loss \[59\] to the albedo image, roughness map, and metallic map:

\(L_\text{albedo}=L_\text{MSE}(I_\text{albedo},I_\text{albedo}^\text{GT})+L_\text{LPIPS}(I_\text{albedo},I_\text{albedo}^\text{GT}),\) (2)

\(L_\text{R}=L_\text{MSE}(I_\text{R},I_\text{R}^\text{GT})+L_\text{LPIPS}(I_\text{R},I_\text{R}^\text{GT}),\) (3)

\(L_\text{M}=L_\text{MSE}(I_\text{M},I_\text{M}^\text{GT})+L_\text{LPIPS}(I_\text{M},I_\text{M}^\text{GT}),\) (4)

L2D
L2D
Multi-view Rendering
"a wooden and metal shield"
Albedo
Roughness
Gaussian Splatting
Multi-view images
Gaussian Fitting
Baking
Roughness
Albedo
Octree-based 3D U-Net
Octant-aligned 3D Gaussian
3D Octree
Rendered images
O
S
S
S
R
R
R
R
R
C
B
M
R
3D Object
3D Octree
Opacity Scale
Rotation
Albedo Material
(a) Octant-aligned 3D Gaussian Splatting
(b) Octree-based 3D U-Net Training
(c) Texture & Material Baking

Figure 2. An overview of our PBR material generation framework. (a) We propose octant-aligned 3D Gaussian Splatting, which positions a 3D Gaussian at the center of each finest leaf node of the constructed octree. Additional channels are added at the end of the Gaussian parameters to model PBR material. (b) We use the 3D U-Net built upon octree-based convolutional networks to predict the Gaussian parameters. Our octree-based 3D U-Net is trained by minimizing the difference on 2D raster images and 3D Gaussian parameters. (c) We bake the multi-view rendered images to the UV space of the input 3D model to realize physically based rendering under new illumination environments.

