_where_ \(\Gamma(\cdot)\) _is the gamma function._

_Since the development of FC, several definitions of non-integer order derivatives have been proposed, including the Riemann-Liouville, Caputo, and Grünwald-Letnikov formulations \[105, 110\]. These definitions are generally not equivalent on bounded domains, unless additional regularity or boundary conditions are imposed on the function u(z). In the present work, we first focus on the Riemann-Liouville fractional derivatives (R-LFD), which are introduced below._

**Definition 1.2** _\[105\] Let_ \(\xi\in(n-1,n)\), \(n\in\mathbb{N}^+\)_, and let_ \(u(z)\in AC([a,b])\) _be absolutely continuous. Then, the left- and right-sided R-LFD are defined as_

\(\mathcal{D}_{a+,z}^\xi u(z)=\frac{1}{\Gamma(n-\xi)}\frac{d^n}{dz^n}\int_a^z\frac{u(\sigma)}{(z-\sigma)^{\xi-n+1}}d\sigma,\)<br>
\(\mathcal{D}_{b-,z}^\xi u(z)=\frac{(-1)^n}{\Gamma(n-\xi)}\frac{d^n}{dz^n}\int_z^b\frac{u(\sigma)}{(\sigma-z)^{\xi-n+1}}d\sigma.\)

If \(\alpha\in\mathbb{N}\), the R-LFDs reduce to the classical integer order derivatives. We now introduce the Riesz fractional derivative, which is closely related to the Riemann- Liouville formulation.

**Definition 1.3** _\[110\] For_ \(\xi\in(n-1,n)\), \(n\in\mathbb{N}^+\)_, the Riesz fractional derivative is defined as_

\(\frac{\partial^\xi u(z)}{\partial|z|^\xi}=c(\xi)\left(\mathcal{D}_{a+,z}^\xi u(z)+\mathcal{D}_{b-,z}^\xi u(z)\right),\) (1.1)

_where_ \(c(\xi)=-\frac{1}{2\mathrm{cos}\left(\frac{\xi\pi}{2}\right)}>0\) _with_ \(\xi\neq 1\).

In the 1D case, the Riesz fractional derivative coincides with the fractional Laplacian, which can also be defined as follows.

**Definition 1.4** _Let u(z_) _be in the Schwartz space of rapidly decaying functions and_ \(\alpha\in(0,1)\)_. The fractional Laplacian operator_ \((-\Delta)^\xi\) _is defined as_

\((-\Delta)^\xi u(z)=C(\xi)P.V.\int_\mathbb{R}\frac{u(z_1)-u(z_2)}{|z_1-z_2|^{1+2\xi}}d(z_2),\) (1.2)

_where_ \(C(\xi)=\frac{\xi 2^{2\xi}\Gamma(\xi+\frac{1}{2})}{\sqrt{\pi}\Gamma(1-\xi)}\) _is a normalization constant._

A generalized class of fractional derivatives is obtained by introducing exponential tempering, leading to the so-called tempered fractional derivatives \[108\]. In the Riemann-Liouville framework, these operators are defined as follows.

**Definition 1.5** _\[4\] Let_ \(\xi\in(n-1,n)\), \(n\in\mathbb{N}^+\), \(\vartheta\ge 0\) _and let_ \(u(z)\in AC([a,b])\)_. Then, the left- and right-sided Riemann-Liouville tempered fractional derivatives are defined as_

\(\mathcal{D}_{a+,z}^{\xi,\vartheta} u(z)=\frac{\mathrm{e}^{-\vartheta z}}{\Gamma(n-\xi)}\frac{d^n}{dz^n}\int_a^z\frac{\mathrm{e}^{\vartheta\sigma} u(\sigma)}{(z-\sigma)^{\xi-n+1}}d\sigma,\) (1.3)

\(\mathcal{D}_{b-,z}^{\xi,\vartheta} u(z)=\frac{(-1)^n\mathrm{e}^{\vartheta z}}{\Gamma(n-\xi)}\frac{d^n}{dz^n}\int_z^b\frac{\mathrm{e}^{-\vartheta\sigma} u(\sigma)}{(\sigma-z)^{\xi-n+1}}d\sigma.\) (1.4)

