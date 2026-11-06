<tbc>also supports image encoding, we use the same encoder to map the reference image **_I_** into its latent representation **_F_**_<sub>I</sub>_.

**Architecture.** Figure 2(b) illustrates the architecture of OrbitPainter, a conditional video generative model. The model is conditioned on two types of priors:

1. A 2D appearance prior **_F_**_<sub>I</sub>_, extracted from the reference image.<tbc>

2. 3D geometric priors \(\{\mathbf{F}_H^{Normal},\mathbf{F}_H^{Pos},\mathbf{F}_V^{Normal},\mathbf{F}_V^{Pos}\}\), which encode surface orientation and spatial structure under horizontal and vertical scans.

Given these conditional inputs, the training objective is to generate the RGB latent videos \(\{\mathbf{F}_H^{RGB},\mathbf{F}_V^{RGB}\}\) using a Flow Matching objective. The generated latents represent multi-view appearance in video form while remaining consistent with the underlying 3D geometry.

### Flow Construction.

We first concatenate the target RGB latent videos along the temporal dimension:

\(\mathbf{F}^{RGB}=\mathrm{Concat}_T(\mathbf{F}_H^{RGB},\mathbf{F}_V^{RGB}),\) (1)

where \(\mathrm{Concat}_T(\cdot)\) denotes temporal concatenation. Following the Flow Matching formulation, we sample \(t\in[0,1]\) from a logit-normal distribution and initialize Gaussian noise **x**<sub>0</sub>∼N(**0**,**I**). The intermediate sample is obtained via linear interpolation:

\(\mathbf{x}_t=(1-t)\mathbf{x}_0+t\mathbf{F}^{RGB}.\) (2)

### Injecting Geometric Priors.

To guide the denoising process with geometry information, we first concatenate the horizontal and vertical geometric latents:

\(\mathbf{F}^{Normal}=\mathrm{Concat}_T(\mathbf{F}_H^{Normal},\mathbf{F}_V^{Normal}),\) (3)

\(\mathbf{F}^{Pos}=\mathrm{Concat}_T(\mathbf{F}_H^{Pos},\mathbf{F}_V^{Pos}).\) (4)

These geometric priors are then injected by channel-wise concatenation with the intermediate latent:

\(\mathbf{x}'_t=\mathrm{Concat}_C(\mathbf{x}_t,\mathbf{F}^{Pos},\mathbf{F}^{Normal}),\) (5)

where \(\mathrm{Concat}_C(\cdot)\) denotes channel-wise concatenation.

### Injecting Appearance Prior.

The 2D appearance prior is incorporated by temporally appending the reference image latent:

\(\mathbf{S}=\mathrm{Concat}_T(\mathbf{F}_I,\mathbf{x}'_t).\) (6)

The resulting sequence **_S_** therefore contains noise information together with both 2D appearance and 3D geometric priors.

