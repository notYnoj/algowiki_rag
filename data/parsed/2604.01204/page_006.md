<tbc>is defined by the particle center \(\unknown\in\mathbb{R}^3\) and covariance matrix \(\unknown\in\mathbb{R}^{3\times 3}\). To ensure positive semi-definiteness during optimization, the covariance is parameterized as \(\unknown=\mathbf{RSS}^T\mathbf{R}^T\), where \(\mathbf{R}\in SO(3)\) represents rotation and \(\mathbf{S}\in\mathbb{R}^{3\times 3}\) encodes scaling. In practice, these parameters are stored as a quaternion \(\mathbf{q}\in\mathbb{R}^4\) and a scale vector \(\mathbf{s}\in\mathbb{R}^3\). Each primitive additionally carries an opacity parameter \(\sigma\in\mathbb{R}\) and a view-dependent radiance function \(\phi(\mathbf{d})\), commonly represented using spherical harmonics. Note that in this case, \(\phi(\mathbf{d})\) depends only on the ray direction and not on the spatial position of the intersection point.

#### Primitive-based Volume Rendering.

Given a camera ray \(\mathbf{r}(\tau)=\mathbf{o}+\tau\mathbf{d}\) with origin \(\mathbf{o}\in\mathbb{R}^3\) and direction \(\mathbf{d}\in\mathbb{R}^3\), the rendered ray color \(\mathbf{c}\in\mathbb{R}^3\) is obtained via volume rendering over the primitives _P<sub>c</sub>_ intersecting the ray:

\(\mathbf{c}(\mathbf{o},\mathbf{d})=\sum_{i\in P_c}\phi(\mathbf{d})\cdot T_i\cdot\alpha_i,T_i=\prod_{j=1}^{i-1}1-\alpha_j,\) (2)

where the opacity \(\alpha_i\) is defined as \(\alpha_i=\sigma_i\rho_i(\mathbf{o}+\tau\mathbf{d})\) and _T<sub>i</sub>_ is the transmittance.

#### Positional Encoding:

Neural networks exhibit a natural spectral bias that limits their ability to learn high-frequency functions in low-dimensional domains [62]. Positional encodings mitigate this limitation by mapping low-dimensional spatial and directional coordinates into higher-dimensional representations before feeding them into the network [62]. While early approaches relied on fixed _frequency encodings_ [20,50], modern methods often use _parametric encodings_ that store learnable feature vectors in auxiliary spatial data structures, such as grids or trees [49,60]. Query coordinates retrieve and interpolate these features, effectively shifting much of the representational burden from the neural network to the encoding itself. This design trades increased memory usage for reduced computation: only a small subset of encoding parameters is updated per sample, allowing the neural network to remain compact and efficient while significantly accelerating convergence and maintaining high reconstruction quality.

## 4 Method

We present the core components of our approach using 3D Gaussian primitives in the context of novel view synthesis, following the formulation of 3DGUT [70]. We begin by introducing our _primitive-bound feature embedding_ in Sec. 4.1. Next, Sec. 4.2 presents _harmonic texturing_, which increases per-primitive expressive power while preserving the locality and explicit form of the representation. Finally, Sec. 4.3 describes a _neural deferred decoding_ scheme that enables efficient signal reconstruction in a single image-space pass. Generalization to other primitive types and additional applications will be discussed in Sec. 5.2. Fig. 2 provides a schematic overview of our method.

<sup>3</sup> Gaussian particles are bounded by ellipsoids in world space, which become spheres after whitening. Our virtual bounding tetrahedra are defined in this canonical space.

