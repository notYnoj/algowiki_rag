# Neural Harmonic Textures for High-Quality Primitive Based Neural Reconstruction

**Abstract.** Primitive-based methods such as 3D Gaussian Splatting have recently become the state-of-the-art for novel-view synthesis and related reconstruction tasks. Compared to neural fields, these representations are more flexible, adaptive, and scale better to large scenes. However, the limited expressivity of individual primitives makes modeling high- frequency detail challenging. We introduce _Neural Harmonic Textures_, a neural representation approach that anchors latent feature vectors on a virtual scaffold surrounding each primitive. These features are interpolated within the primitive at ray intersection points. Inspired by Fourier



Jorge Condor<sup>1,2</sup><sup>\*</sup>, Nicolas Moënne-Loccoz<sup>1</sup><sup>\*</sup>, Merlin Nimier-David<sup>1</sup><sup>\*</sup>, Piotr<br> Didyk<sup>2</sup><sup>\*</sup>, Zan Gojcic<sup>1</sup><sup>\*</sup>, and Qi Wu<sup>1</sup><sup>\*</sup>

<sup>1</sup> NVIDIA

`{nicolasm,mnimierdavid,zgojcic,qiwu}@nvidia.com`

<sup>2</sup> Università della Svizzera italiana, Lugano, Switzerland `{jorge.condor,piotr.didyk}@usi.ch`

**Fig. 1: Neural Harmonic Textures for novel view synthesis.** We attach learnable feature vectors (right) to the virtual vertices of bounding tetrahedra encapsulating each primitive (center). After harmonic encoding and accumulation along the ray, a small neural network decodes the resulting signal into RGB color in a deferred manner (left). Source code and further results are available at `https://research.nvidia.com/labs/ sil/projects/neural-harmonic-textures/`.

