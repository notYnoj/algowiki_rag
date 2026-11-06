## 2.2. High-order hyperbolic moment system and hydrodynamic equations

To obtain moment models for the Boltzmann equation (1), the distribution function is first expanded into a series of Hermite functions as<tbc>

\(f(x,v)=\sum_{\alpha\in\mathbb{N}^3}f_\alpha(x)\mathcal{H}_\alpha^{[\varpi,\vartheta]}(v),\) (6)

<tbc>where \(f_\alpha(x)\) are the coefficients, and \(\mathcal{H}_\alpha^{[\varpi,\vartheta]}(\cdot)\) are the basis functions defined by<tbc>

\(\mathcal{H}_\alpha^{[\varpi,\vartheta]}(v)=\frac{1}{m_*(2\pi\vartheta)^{3/2}\vartheta^{|\alpha|/2}}\prod_{d=1}^3He_{\alpha_d}(\xi_d)\mathrm{exp}\left(-\frac{\xi_d^2}{2}\right),\xi=\frac{v-\varpi}{\sqrt{\vartheta}},\forall v\in\mathbb{R}^3.\)

<tbc>In the above expression, \(\alpha=(\alpha_1,\alpha_2,\alpha_3)\) is a multi-index with order \(|\alpha|=\alpha_1+\alpha_2+\alpha_3\), and \(He_n(\cdot)\) is the Hermite polynomial of degree _n_ given by<tbc>

\(He_n(x)=(-1)^n\mathrm{exp}\left(\frac{x^2}{2}\right)\frac{\mathrm{d}^n}{\mathrm{d}x^n}\mathrm{exp}\left(-\frac{x^2}{2}\right).\)

<tbc>The parameters \(\varpi\in\mathbb{R}^3\) and \(\vartheta\in\mathbb{R}^+\) in the basis function could be either constants as in the Hermite spectral method \[27\], or variables depending on **_x_**. In Grad’s moment method \[12\], \(\varpi\) and \(\vartheta\) are chosen adaptively as the local mean velocity **_u_** and the local temperature \(\theta\), which are determined from _f_ itself via (3). With this choice, the relationship between the moment coefficients \(f_\alpha\) and the macroscopic variables can be deduced from (3) and (5) as

\(f_0=\rho,f_{e_1}=f_{e_2}=f_{e_3}=0,\sum_{d=1}^3f_{2e_d}=0,\sigma_{ij}=(1+\delta_{ij})f_{e_i+e_j},q_i=2f_{3e_i}+\sum_{d=1}^3f_{2e_d+e_i},i,j=1,2,3,\text{(7)}\)

where _e_<sub>1</sub>, _e_<sub>2</sub>, _e_<sub>3</sub> represent the multi-indices (1,0,0), (0,1,0) and (0,0,1), respectively. Since the first term of series (6) already recovers the local Maxwellian, Grad’s method often provides an efficient approximation of the distribution function for flows close to thermodynamic equilibrium. Accordingly, we adopt Grad’s choice \(\varpi=u\) and \(\vartheta=\theta\) for the representation of the distribution function in the near-continuum flow regime considered in this paper.

Numerically, the distribution function is approximated by a truncated series of order _M_, that is,<tbc>

\(f(x,v)\approx\sum_{|\alpha|\le M}f_\alpha(x)\mathcal{H}_\alpha^{[u,\vartheta]}(v)\in\mathcal{F}_M^{[u,\theta]},\) (8)

<tbc>in which \(\mathcal{F}_M^{[u,\theta]}\) is the linear space spanned by the basis functions \(\mathcal{H}_\alpha^{[u,\vartheta]}(v)\) with \(|\alpha|\le M\). Substituting the expansion (8) into the Boltzmann equation (1) and following the procedures in \[13, 17, 28\], we obtain the globally hyperbolic moment system of order _M_. With \(\varrho\) denoting the vector of all independent variables **_u_**, \(\theta\), and \(f_\alpha\) with \(|\alpha|\le M\), the resulting system can be written in the quasi-linear form

\(\sum_{d=1}^D\mathbf{A}_d(\varrho)\frac{\partial\varrho}{\partial x_d}=\mathcal{Q}(\varrho),\) (9)

where the left-hand side is derived from the convection part of the Boltzmann equation, and the right-hand side corresponds to the collision term. The detailed expression of the above system can be found for the Boltzmann- Shakhov equation in Appendix A. For \(M\ge 2\), the factor 1_/Kn_ enters the right-hand side of (9) through the collision frequency \(\bar{v}\), making the system increasingly stiff as \(Kn\rightarrow 0\).

Moreover, the conservation laws of mass, momentum and energy form a natural subsystem of the moment system (9) for \(M\ge 2\). The corresponding hydrodynamic equations for the primary macroscopic quantities \(\rho\), **_u_** and \(\theta\) take the<tbc>

