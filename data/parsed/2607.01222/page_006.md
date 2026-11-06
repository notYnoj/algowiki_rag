<tbc>rate of 16 and a temporal downsampling rate of 4, to obtain compact spatiotemporal latent features. The resulting latent representations are denoted as \(\{\mathbf{F}_H^{RGB},\mathbf{F}_H^{Normal},\mathbf{F}_H^{Pos},\mathbf{F}_V^{RGB},\mathbf{F}_V^{Normal},\mathbf{F}_V^{Pos}\}\). In addition, since the video encoder<tbc>

Orbit Scan
Latents
Horizontal Scan
Vertical Scan
Horizontal Scan
Texture
Surface Normal
3D Asset
Texture Video
Texture Video
3DPos.
Re-Render
Video VAE Encoder
Vertical Scan
Surface-Normal Video
Surface-Normal Video
Texture
Surface Normal
3D-Position Video
3D-Position Video
3DPos.
Reference Image
(a) Data Pre-Processing and Latent Extraction
Denoise
:
:
:
:
Key
NxMain Block
-
Attention
Full Attention
Geometry-Aware Sparse Attention
Full Attention
Noise
Noise
Ref. Image Latent
(b) OrbitPainter Architecture

**Fig.2:** Overview of _OrbitPainter_. (a) Given a 3D asset, we first apply random lighting and render it from a randomly sampled viewpoint to obtain a reference image. We then perform horizontal and vertical orbit scans to render RGB videos, surface- normal videos, and 3D-position videos. All videos, together with the reference image, are encoded by a video VAE encoder into latent representations. (b) OrbitPainter is a conditional video generative model that synthesizes RGB orbit-scan videos conditioned on a 2D appearance prior (the reference image) and 3D geometry priors (surface-normal and 3D-position videos). A Geometry-Aware Sparse Attention module is introduced in parallel with full attention to better leverage the 3D geometry priors.

