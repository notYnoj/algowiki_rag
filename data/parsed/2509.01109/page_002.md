vector quantization. Based on VQVAE, VQGAN \[11\] and MaskGiT \[3\] train autoregressive models and achieve improved image generation performance. Beyond 2D grid tokenization, TiTok \[38\] transforms images into compact 1D latent sequences, significantly reducing tokens. FlexTok \[1\] and One-D-Piece \[24\] dynamically adjust counts, enhancing efficiency by concentrating key information early in the sequence. MAETok \[5\] shows masked autoencoders yield discriminative latent spaces suitable for diffusion models.

Despite the significant progress achieved by existing image tokenization methods, the grid-based tokenization strategy used by them is inefficient and inflexible in representing the different regions with different contents in natural images. As illustrated in Figs. 1 (a) and (b), 2D-grid tokens represent local patches of fixed size and at fixed positions, no matter whether the patch has complex structures or details, while 1D-grid tokens encode globally contextualized information from the entire image, lacking spatially-adaptive representation ability.

In this paper, we propose **GPSToken**, a novel **G**Gaussian **P**Parameterized **S** Spatially-adaptive **Token**ization framework, to achieve non-uniform and flexible image tokenization. GPSToken parameterizes each token with a 2D Gaussian function, encoding both the positions and shapes of different regions in an image. Specifically, as shown in Fig. 1 (c), each GPS-token consists of two components: the first component stores the standard deviation and position of the Gaussian function, representing region shape and location, while the second component represents the textural features of the region. Inspired by Gaussian Splatting \[18\], our GPSToken can be rendered into 2D feature maps, facilitating seamless integration with conventional 2D decoders and enabling end-to-end training.

To achieve spatially-adaptive tokenization, we iteratively partition an image into regions of varying sizes and shapes. The partitioned regions, though having different shapes and positions, will have a similar amount of information in terms of entropy. The shape and position of each region are used to initialize the corresponding Gaussian parameters. Then, we utilize a transformer, for which each query corresponds to a token, to refine these parameters and extract textural features. The shape-texture decomposition of GPSToken provides distinct advantages for image generation. With GPSToken, we can first generate Gaussian parameters that encode spatial layout (region shape/position), then synthesize texture features conditioned on the Gaussian geometric priors. The Gaussian priors act as structural constraints, simplifying texture generation while ensuring spatial consistency. This shape-texture decomposition approach aligns with how humans conceptualize images (structure-first, details-later), accelerating the model training and improving the generation quality.

Our method achieves significant improvements over existing methods in both image reconstruction and generation tasks. For image reconstruction, GPSToken achieves "rec. FID", PSNR and SSIM scores of 0.65, 24.06 and 0.657 on the ImageNet 256\(\times\)256 reconstruction task using 128 tokens. For image generation, our model achieves a state-of-the-art FID of 1.50 on the ImageNet 256 generation task, surpassing recent methods such as Titok \[38\], FlexTok \[1\], One-D-Piece \[24\] and MAETok \[5\]. Our contributions are summarized as follows:

Gaussian parameters
Textual features
(a) 2D-grid tokens
(b) 1D-grid tokens
(c) Our GPS-tokens
Input
GPS-tokens
Reconstruction
Input
GPS-tokens
Reconstruction
(d) Visualization of GPSToken

Figure 1: Comparisons between (a) 2D-grid tokens, (b) 1D-grid tokens and (c) our GPS-tokens. (d) Two visualization examples of the representation and reconstruction results of GPSToken.

