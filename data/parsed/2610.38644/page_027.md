for some coefficient vector \(\alpha\in\mathbb{R}^N\). Substituting into the finite feature representation gives

\(u_M(\mathbf{z})=\varphi_M(\mathbf{z})^\top Z^\top\alpha\)<br>
\(=\sum_{j=1}^N\alpha_j\left[\frac{1}{M}\sum_{m=1}^M\phi_{\theta_m}(\mathbf{z})\ell_j[\phi_{\theta_m}]\right].\) (57)

Because \(\ell_j\) acts on the second argument, the term in brackets can be written as

\(\ell_j^{\mathbf{z}^\prime} k_M(\mathbf{z},\mathbf{z}'_j),\) (58)

where the empirical feature kernel is

\(k_M(\mathbf{z},\mathbf{z}')=\frac{1}{M}\sum_{m=1}^M\phi_{\theta_m}(\mathbf{z})\phi_{\theta_m}(\mathbf{z}').\) (59)

Hence

\(u_M(\mathbf{z})=\sum_{j=1}^N\alpha_j\ell_j^{\mathbf{z}^\prime} k_M(\mathbf{z},\mathbf{z}'_j).\) (60)

If the feature parameters are sampled from \(\rho(\theta)\), then as \(M\rightarrow\infty\),

\(k_M(\mathbf{z},\mathbf{z}')\longrightarrow k_\rho(\mathbf{z},\mathbf{z}')=\mathbb{E}_{\theta\sim\rho}\left[\phi_\theta(\mathbf{z})\phi_\theta(\mathbf{z}')\right].\) (61)

Under the regularity conditions used in this work, the linear functionals may be interchanged with the expectation, so that

\(\ell_j^{\mathbf{z}^\prime} k_M(\mathbf{z},\mathbf{z}'_j)\longrightarrow\ell_j^{\mathbf{z}^\prime} k_\rho(\mathbf{z},\mathbf{z}'_j).\) (62)

The continuum-limit representation is therefore

\(u_h(\mathbf{z})=\sum_{j=1}^N\alpha_j\ell_j^{\mathbf{z}^\prime} k_\rho(\mathbf{z},\mathbf{z}'_j),\) (63)

which is the CFKS representer form used in the main text.

This derivation also shows that the finite feature coefficients \(\beta\) disappear from the continuum formulation: their effect is transferred to the constraint-space coefficients \(\alpha\) through the empirical Gram structure, while the sampled kernel _k<sub>M</sub>_ is replaced by the analytically evaluated continuum-feature mean kernel \(k_\rho\).

## B Analytical Derivation of the Bounded Continuum-Feature Gaussian Kernel

This appendix derives the closed-form mean kernel associated with a continuum of Gaussian radial-basis-function features whose centers are uniformly distributed over a bounded interval. The full-line version of this construction is classical and yields a squared-exponential covariance; see, for example, Rasmussen and Williams \[8\]. Here we retain the finite center-support interval explicitly, which produces additional error-function terms.

### B.1 One-dimensional Gaussian feature model

Consider the Gaussian feature

\(\phi_c(x)=exp\left(-\frac{(x-c)^2}{2\sigma^2}\right),\sigma>0,\) (64)

where the center _c_ is distributed uniformly over

\(c\sim\mathcal{U}[a,b],a<b.\) (65)

The corresponding mean feature kernel is

\(k_{[a,b]}(x,y)=\mathbb{E}_c\left[\phi_c(x)\phi_c(y)\right]=\frac{1}{b-a}\int_a^b\phi_c(x)\phi_c(y)dc.\) (66)

Substituting eq. 64 gives

\(k_{[a,b]}(x,y)=\frac{1}{b-a}\int_a^bexp\left(-\frac{(x-c)^2+(y-c)^2}{2\sigma^2}\right)dc.\) (67)

The integral can be evaluated analytically by completing the square with respect to the center variable _c_.

