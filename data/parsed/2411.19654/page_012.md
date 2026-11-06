## A . Preliminary of 3D Gaussian Splatting

Gaussian splatting employs a collection of 3D Gaussians to represent 3D data. Specifically, each Gaussian is formally defined as:

\(G(x)=e^{-\frac{1}{2}(x-\mu)^T\Sigma^{-1}(x-\mu)},\) (8)

where \(\mu\in\mathbb{R}^3\) represents the spatial mean of 3D Gaussian and \(\Sigma\in\mathbb{R}^{3\times 3}\) denotes the covariance matrix. The covariance matrix \(\Sigma\) of a 3D Gaussian is analogous to describing the configuration of an ellipsoid. Thus, the covariance matrix \(\Sigma\) is decomposed into a scaling matrix **_S_** and a rotation matrix **_R_** as follows:

\(\Sigma=RSS^\top R^\top.\) (9)

To allow independent optimization of both factors, they are stored separately: a 3D vector **_s_** for scaling and a quaternion **_q_** to represent rotation. During the rendering process, the 3D Gaussians are projected onto a 2D plane. With the intrinsic matrix **_K_** and extrinsic matrix **_T_**, the 2D mean \(\mu'\) and covariance \(\Sigma'\) are defined as follows:

\(\mu'=K[\mu,1]^\top,\Sigma'=JT\Sigma T^\top J^\top.\) (10)

Here, **_J_** represents the Jacobian of the affine approximation of the projective transformation. Each 3D Gaussian is associated with an opacity value **_o_** and a view-dependent color **_c_**, determined by a set of spherical harmonics coefficients. In our model, the multi- view rendered images of albedo map do not depend on the selected viewpoints. As a result, we just use three-channels RGB on each 3D Gaussian to represent the view-independent colors instead of original spherical harmonics, and we exclude the positional parameter \(\mu\) because each 3D Gaussian is fixed at the center of each finest leaf node of the constructed octree. All the parameters can be collectively denoted by \(\Theta_0\) with:

\(\Theta_{0_i}=\{o_i,s_i,q_i,c_i\},\) (11)

representing the parameters for the _i_-th Gaussian.

Moreover, to encode the PBR material parameters, we append additional two parameters: roughness **_r_** and metallic **_m_** at the end of the original Gaussian parameters. To render multi-view images of these two attributes, we concatenate **_r_** and **_m_** with previous parameters to obtain:

\(\Theta_{1_i}=\{o_i,s_i,q_i,r_i\},\Theta_{2_i}=\{o_i,s_i,q_i,m_i\}.\) (12)

Then, all the 3D Gaussians are paired with these two new parameters \(\Theta_{1_i}\) and \(\Theta_{2_i}\), rendered from multiple viewpoints to get multi- view roughness map and metallic map for further training.

## B . Network Details

### Unconditional RGB Texture Generation

The network architecture of the octree-based 3D U-Net we used in unconditional RGB texture generation is shown in Fig. 9. The U-Net has five hierarchical levels, corresponding to octree depths of 8, 7, 6, 5 and 4, with resolutions of 256<sup>3</sup>,128<sup>3</sup>,64<sup>3</sup>,32<sup>3</sup>,16<sup>3</sup>. The feature dimensions are set to 32,64,128,256,256 respectively. The number of channels for input and output features is 4 and 11, respectively, due to the lack of material information.

### Text-conditioned PBR Material Generation

The network architecture of the octree-based 3D U-Net we used in text- conditioned PBR material generation is shown in Fig. 10. The U-Net has five hierarchical levels, corresponding to octree depths of 8, 7, 6, 5 and 4, with resolutions of 256<sup>3</sup>,128<sup>3</sup>,64<sup>3</sup>,32<sup>3</sup>,16<sup>3</sup>. The feature dimensions are set to 64,128,256,512,512 respectively. The number of channels for input and output features is 4 and 13, respectively, as described in the main manuscript. The text feature is fed to U-Net via the octree-based multi-head cross attention mechanism. The cross attention layers are only inserted at the least two down-sampling blocks, the middle block and the two first up-sampling blocks to save GPU memory.

## C . More Results

Our method is capable of generating diverse materials given different text prompts for a single mesh. Fig. 11 shows the PBR materials and the rendering results of the same mesh generated from different text prompts by our proposed TexGaussian. These results demonstrate that our method is able to generate diverse materials of different styles that align well with the text prompts and 3D objects with high fidelity.

We provide more generated results in Fig. 12.

Gaussian Parameters
Octree Upsample
Octree-based Convolution
Geometry Features
Octree Downsample

Gaussian Parameters
Octree Upsample
Octree-based Convolution
Text Feature
Geometry Features
Octree Downsample
Octree-based Cross Attention

Figure 9. The network architecture of the octree-based 3D U-Net we used to train our unconditional RGB texture generation model.

Figure 10. The network architecture of the octree-based 3D U- Net we used to train our text-conditioned PBR material generation model.

