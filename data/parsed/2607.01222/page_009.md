Surface-Normal Video
Surface-Normal Video
White-Mesh Geometry
White-Mesh Geometry
3D-Position Video
3D-Position Video
Horizontal Orbit Scan
Vertical Orbit Scan
Geometry Generation Model
Video VAE Encoder
OrbitPainter
Texture Optimizer
Video VAE Decoder
Texture Video (Horizontal Orbit Scan)
Texture Video (Vertical Orbit Scan)
Textured 3D Asset
Reference Image
(a) Inference Pipeline of Ink3D
Textured Voxelization from Dense-View Images
Prior-Guided Denoising
Voxelized White-Mesh Geometry
Trellis-2 3D Encoder
Graph Matching
+Mild Noise
Textured Voxels
Trellis-2
Denoise
Textured 3D Asset
Dense-View Images
(b)
TextureOptimizer

**Fig.3:** (a) **Inference pipeline of Ink3D.** Given a reference image, we first estimate the corresponding white-mesh geometry using an off-the-shelf geometry generation model. The trained OrbitPainter then generates orbit-scan videos of the object, whose frames are collected to form a dense-view image set. Finally, TextureOptimizer bakes these dense views onto the white-mesh geometry to produce the final textured 3D asset. (b) **TextureOptimizer.** We first convert the dense-view images into textured voxels based on the white-mesh geometry by formulating voxel-pixel correspondence as a graph-matching problem. The resulting textured voxels are then refined via prior- guided denoising: mild noise is added and Trellis-2 performs a few denoising steps to produce the final textured 3D asset.

