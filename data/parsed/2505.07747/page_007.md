forming the final point set \(P=P_{uniform}\cup P_{salient}\) along with their corresponding normals, as input to the VAE. For geometry supervision, we sample three distinct sets of points with their SDF values: 200k points within the cube volume, 200k points near the mesh surface with a threshold 0.02, and 200k points directly on the surface. (2) Data for Diffusion: For training our single-image conditioned flow model, we render each 3D model from 20 randomly sampled viewpoints with camera elevation between -15\(^\circ\) and 30\(^\circ\), azimuth between -75\(^\circ\) and 75\(^\circ\), and focal lengths randomly selected from orthogonal projection or perspective projections (with focal length uniformly sampled from 35mm to 100mm). We adjust the camera position to ensure the content occupies approximately 90% of the image. Additionally, we apply common data augmentations such as random flipping (for both images and sampled meshes), color jitter, and random rotations between -10\(^\circ\) and 10\(^\circ\).

## 3.2 Step1X-3D Shape Generation

Similar to 2D image generation \[63, 33\], the Step1X-3D shape generation module consists of a shape autoencoder and a Rectified Flow Transformer. For the sampled point cloud _P_, we first compress it into a 1D tensor using a shape latent set autoencoder \[91\], then train the diffusion model with a 1D Rectified Flow Transformer inspired by Flux \[33\]. We also support additional components like LoRA for extended flexibility.

### 3D Shape Variational Autoencoder

The success of the Latent Diffusion Model (LDM) \[63\] proves that a compact, efficient, and expressive representation is essential for training a diffusion model. Therefore, we first encode 3D shapes into a latent space and then train a 3D latent diffusion model for 3D generation. Following the design of 3DShape2VecSet \[91\], we adopt a latent vector set representation to encode point clouds into latent space and decode them into geometric functions (e.g., signed distance fields or occupancies). To improve scalability, we adopt a transformer-based encoder-decoder architecture as in recent works \[29, 95\]. Additionally, we incorporate the Sharp Edge Sampling and Dual Cross Attention techniques proposed in Dora \[9\] to enhance geometric detail preservation. Specifically, we use the downsampled variant of 3DShape2VecSet. Instead of learnable queries, we initialize the latent queries \(S=\mathrm{FPS}(P_{uniform})\cup\mathrm{FPS}(P_{salient})\) directly with the point cloud itself using the Farthest Points Sampling (FPS). We first integrate the information of the concatenated Fourier positional encodings with their respective normals into the shape encoder, forming the actual input to the shape encoder: \(\hat{P}=\mathrm{Concat}(PE(P_c),P_n)\), where _P<sub>c</sub>_ is the points position and _P<sub>n</sub>_ is the normal. The encoder then processes this input using two cross-attention layers and _L<sub>e</sub>_ self-attention layers, encoding the points into the latent space via:

\(\mathrm{Enc}(P)=\mathrm{SelfAttn}^{(i)}(\mathrm{CrossAttn}(S,\hat{P}_{uniform}),\mathrm{CrossAttn}(S,\hat{P}_{salient})),\forall i=1,2,\dots,L_e.\text{(1)}\)

Similarly, we use a perceiver-based decoder that mirrors the architecture of the encoder, and has an extra linear layer \(\varphi_\mathcal{O}\) to learn to predict the Truncated Signed Distance Function (TSDF) value at _x_:<tbc>

\(\mathrm{Dec}(x|S)=\varphi_\mathcal{O}(\mathrm{CrossAttn}(PE(x),\mathrm{SelfAttn}^{(i)}(S))),\forall i=1,2,\dots,L_d,\text{(2)}\)

<tbc>where _L<sub>d</sub>_ is the number of self-attention layers in the shape decoder. Given a query point \(x\in\mathbb{R}^3\) in 3D space and a learned latent set _S_, the decoder can output its TSDF value. Then the training objective is as:

\(\mathcal{L}_{VAE}=\mathbb{E}_{x\in\mathbb{R}^3}\left[\mathrm{MSE}\left(\hat{\mathcal{O}}(x|S),\mathrm{Dec}(x)\right)\right]+\lambda_{kl}\mathcal{L}_{kl},\) (3)

where \(\hat{\mathcal{O}}(x)\) is the ground truth TSDF value of _x_ and the truncated scale is set to 2/256. The KL divergence loss L_<sub>kl</sub>_ is used to regularize the latent space distribution to a standard Gaussian distribution. Subsequently, we sample query points from a regular grid to obtain their corresponding TSDF values, which are then utilized to reconstruct the final surface using the Marching Cubes \[50\]. We also employ Hierarchical Volume Decoding \[34\] to accelerate the inference process. Please refer to the 3DShape2VecSet \[91\] and Dora \[9\] for more details.

### Step1X-3D Diffusion Backbone

Following the state-of-the-art text-to-image Diffusion model architectures FLUX \[33\], we use the same MMDiT structure, but modify it for 1D latent space<tbc>

