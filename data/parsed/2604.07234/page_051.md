<tbc>Combining all of these conditions on _b_ yields that the proof follows whenever<tbc>

\(b\ge\left[\frac{1920^{96}}{\alpha^{24}\beta(\alpha)^{96}(1-\alpha)^{12}}\right]=\kappa(\alpha).\)

<tbc>We take \(b=\kappa(\alpha)\). We now make the implicit constants in the proof of (3.34) explicit and then replace them by their minimum. Retrieving explicit expressions for (C.7) and (C.10), the guarantee of Proposition 3.8, whose corresponding constant is that of the initial \(\Omega(1)\) term of (3.34), can be explicitly written via<tbc>

\(\mathrm{exp}\left(-\frac{N\cdot\beta(\alpha)^3(1+o(1))}{5184(1+\beta(\alpha))\kappa(\alpha)}\right)\le\mathrm{exp}\left(-N\left[\frac{\beta(\alpha)^3}{8000\cdot\kappa(\alpha)}\right]\right)\)

<tbc>for all large _N_. We next consider the \(\Omega(N)\) term of (3.34). The guarantee of Proposition 3.9 here is<tbc>

\(\mathrm{exp}\left(-B\cdot\frac{\beta^\star(\alpha)^2}{8}\right)=\mathrm{exp}\left(-N\left[\frac{\beta(\alpha)^2}{12800\cdot\kappa(\alpha)}\right]\right),\)

<tbc>while the guarantee of Proposition 3.12 is<tbc>

\(\mathrm{exp}\left(-\frac{M}{b^{1/2+2\epsilon}}\cdot D_\mathrm{KL}\left(b^{-(4+8\epsilon)}\left\|2e^{-b^{1/2-6\epsilon}/2}\right)\right)\le^\text{(D.9)}\mathrm{exp}\left(-N\left[\frac{1}{\kappa(\alpha)^5}\right]\right).\)

<tbc>Altogether, we have that<tbc>

(D.10) \(f_\mathrm{pl}(\alpha)-f_\mathrm{null}^\mathrm{ann}(\alpha)\ge\frac{1}{4}\cdot\frac{\beta(\alpha)^3}{12800\cdot\kappa(\alpha)^5}\Longrightarrow^\text{(3.40)}C_\mathrm{unif}(1-\alpha)\ge\frac{\beta(\alpha)^3}{51200\cdot\kappa(\alpha)^5}.\)

<tbc>Finally, we fix \(p\in(0,1)\). Setting \(\alpha=1-p\), we conclude that

\(C_\mathrm{unif}(p)=C_\mathrm{unif}\left(1-\alpha\right)\ge^\text{(D.10)}\frac{\left(\beta(1-p)\right)^3}{51200\cdot\left(\kappa(1-p)\right)^5}>0,\)

yielding the desired result. □

## Appendix E. Addendum to the Proof of Lemma 4.9

We list some results on exponential families here that we invoke later.

**Theorem E.1** ([WJ08, Equation (3.28)])**.** _In an exponential family with discrete state space_ X _and sufficient statistic_ \(\phi(X)\)_, the mean parameter space_ M _admits the representation_

\(\mathcal{M}=\mathrm{conv}\left(\{\phi(x):x\in\mathcal{X}\}\right),\)

_where_ conv _denotes the convex hull operation._

**Theorem E.2** ([WJ08, Theorem 3.3])**.** _In a minimal exponential family with parameter space_ \(\Omega\)_, sufficient statistic_ \(\phi(X)\)_, and log-partition function A, the gradient map_ \(\nabla_\theta A\) _is onto_ \(\mathcal{M}^\circ\)_, the interior of the mean parameter space. Consequently, for each_ \(\mu\in\mathcal{M}^\circ\)_, there exists some_ \(\theta\in\theta(\mu)\in\Omega\) _such that_ \(\mathbb{E}_\theta[\phi(X)]=\mu\).

For \(\theta=(\theta_1,\theta_2)\), defining (with the correspondence \(\theta_1=-\lambda_1\) and \(\theta_2=-\lambda_2\))<tbc>

\(A(\theta):=\mathrm{log}\left(\sum_{a,b}w(a,b)e^{\theta_1a+\theta_2b}\right)\)

<tbc>gives the log-partition function of the exponential family supported on \(\{(a,b)\in\mathbb{N}_{>0}^2:1\le b\le a\}\) with mass function \(p_\theta(a,b)\) defined via

\(p_\theta(a,b)\propto w(a,b)e^{\theta_1a+\theta_2b}\Longrightarrow p_\theta(a,b)=w(a,b)e^{\langle\theta,(a,b)\rangle-A(\theta)}.\)

