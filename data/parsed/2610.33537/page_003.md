In general, one Newton-multigrid step per alternating iteration is sufficient to provide an effective hydrodynamic correction, substantially reducing the need for parameter tuning required in \[23\]. The resulting framework also provides an alternative way to integrate coarse-level corrections in the velocity and spatial spaces through the hydrodynamic equations and the Newton-multigrid method, respectively. With these improvements, the FIM solver achieves enhanced efficiency and robustness, particularly at small Knudsen numbers.

The rest of this paper is arranged as follows. In section 2, we introduce the model equations, their spatial discretization with linear reconstruction, and the FIM framework with the time-integration-based hydrodynamic solver. The local Fourier analysis is presented in section 3, and in section 4 both the IMEX scheme for the moment system with the Shakhov model and the Newton-multigrid method for the hydrodynamic equations are presented. Numerical experiments are carried out in section 5 to demonstrate the performance of the proposed method. Finally, some concluding remarks are given in the last section.

## 2. Governing equations and FIM framework

In this section, we first give a brief review of the steady-state Boltzmann-Shakhov equation and the high-order moment models, then present a unified spatial discretization with linear reconstruction for the given models, and finally introduce the FIM framework for solving the resulting discrete system.

### 2.1. Boltzmann equation with Shakhov collision term

The Boltzmann equation with a BGK-type collision term provides a fundamental description of gas flows in the near-continuum regime. For the steady-state problems considered in this work, it takes the form

\(v\cdot\nabla_xf=\bar{v}(f^\mathrm{E}-f).\) (1)

Here, _f_(**_x_**_,**v**_) is the distribution function, in which \(x=(x_1,\dots,x_D)\in\Omega\subset\mathbb{R}^D\) (_D_=1,2 or 3) and \(v=(v_1,v_2,v_3)\in\mathbb{R}^3\) represent the spatial location and velocity of the gas molecules, respectively. The left-hand side of (1) describes the change of _f_ due to the free streaming, while the right-hand side models the interactions between gas molecules via a simplified relaxation process. The average collision frequency \(\bar{v}\) determines how fast the distribution function approaches equilibrium, assumed to be independent of **_v_** and inversely proportional to the Knudsen number, i.e., \(\bar{v}\propto 1/Kn\). In the BGK model, the function _f_<sup>E</sup> equals the local Maxwellian _f_<sup>M</sup> defined by

\(f^\mathcal{M}(x,v)=\frac{\rho(x)}{m_*(2\pi\theta(x))^{3/2}}\mathrm{exp}\left(-\frac{|v-u(x)|^2}{2\theta(x)}\right),\) (2)

where _m_<sub>∗</sub> is the mass of a single gas molecule. The macroscopic quantities in (2), including the mass density \(\rho(x)\), the mean velocity **_u_**(**_x_**)=(_u_<sub>1</sub>_,u_<sub>2</sub>_,u_<sub>3</sub>) and the temperature \(\theta(x)\), can be computed from the distribution function _f_ as

\(\rho(x)=m_*\int_{\mathbb{R}^3}f(x,v)\mathrm{d}v,\rho(x)u(x)=m_*\int_{\mathbb{R}^3}vf(x,v)\mathrm{d}v,\rho(x)|u(x)|^2+3\rho(x)\theta(x)=m_*\int_{\mathbb{R}^3}|v|^2f(x,v)\mathrm{d}v.\) (3)

It is well known that the BGK model does not produce the correct Prandtl number. A commonly used fix is the Shakhov model \[4\], in which the equilibrium distribution _f_<sup>E</sup> is given by<tbc>

\(f^\mathrm{E}(x,v)=\left[1+\frac{(1-\mathrm{Pr})(v-u(x))\cdot q(x)}{5\rho(x)[\theta(x)]^2}\left(\frac{|v-u(x)|^2}{\theta(x)}-5\right)\right]f^\mathcal{M}(x,v),\) (4)

<tbc>where the Prandtl number can be specified by the parameter Pr, and **_q_** denotes the heat flux of the gas to be defined later. When Pr=1, the Shakhov model reduces to the BGK model. The nonequilibrium moments, including the stress tensor \(\sigma_{ij}\), _i,j_=1,2,3, and the heat flux **_q_**, can be computed from the distribution function as

\(\sigma_{ij}(x)=m_*\int_{\mathbb{R}^3}(v_i-u_i(x))(v_j-u_j(x))f(x,v)\mathrm{d}v-\rho(x)\theta(x)\delta_{ij},i,j=1,2,3,q(x)=\frac{m_*}{2}\int_{\mathbb{R}^3}|v-u(x)|^2(v-u(x))f(x,v)\mathrm{d}v.\text{(5)}\)

Here \(\delta_{ij}\) is Kronecker’s delta symbol. Note that \(\sigma_{ij}\) is a trace-free tensor satisfying \(\sigma_{11}+\sigma_{22}+\sigma_{33}=0\).

