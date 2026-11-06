of (_x_<sub>0</sub>_,y_<sub>0</sub>) and \((0,1-\epsilon)\): \((x,y)=\alpha(x_0,y_0)+(1-\alpha)(0,1-\epsilon)\). Moreover, one can easily check that \(s_{\epsilon,\theta}(x,y)=\alpha f(x_0,y_0)+(1-\alpha)f(0,1-\epsilon)\). By convexity of \(\breve{f}_{\mathcal{S}_{\epsilon,\theta,\zeta,\eta}}\), we deduce that \(\breve{f}_{\mathcal{S}_{\epsilon,\theta,\zeta,\eta}}\le s_{\epsilon,\theta}\).

The next proposition states that a constraint of form \(s_{\epsilon,\theta}(x,y)\le d\) can be expressed through second-order cone programming.

**Proposition 3.3.** \(s_{\epsilon,\theta}(x,y)\le d\) _can be expressed as the hyperbolic constraint_ \((z+d)(z-\frac{1}{1-\theta}x)\ge z^2\) _and the linear constraint_ \(z=1-\frac{y-x-\theta}{1-\epsilon-\theta}\).

_Proof._ Let \(z=1-\frac{y-x-\theta}{1-\epsilon-\theta}\) . Then:

\(s_{\epsilon,\theta}(x,y)\le d\Longleftrightarrow\frac{x}{1-\theta-\frac{x}{z}}\le d\Longleftrightarrow\frac{\frac{1}{1-\theta}xz}{z-\frac{1}{1-\theta}x}+z\le z+d\Longleftrightarrow\frac{z^2}{z-\frac{1}{1-\theta}x}\le z+d.\) (14)

Using the fact that \((z-\frac{1}{1-\theta}x)\) is strictly positive (from the first part of the proof of Proposition 3.2), the last inequality is equivalent to \(z^2\le(z+d)(z-\frac{1}{1-\theta}x)\).

Note that Proposition 3.3 provides a second proof of the convexity of \(s_{\epsilon,\theta}\) since its epigraph is shown to be convex.

## 3.3 Convex envelope of _f_ on \(\mathcal{T}_{\epsilon,\theta,\zeta}\)

Consider the function \(t_{\epsilon,\zeta}:\mathcal{X}_{\epsilon,\theta,\zeta,\eta}\rightarrow\mathbb{R}\) where \(t_{\epsilon,\zeta}(x,y)=\frac{x^2}{(1-\zeta)(1-\epsilon)+\epsilon x-(1-\zeta)y}\) if \((x,y)\neq(0,1-\epsilon)\), and \(t_{\epsilon,\zeta}(0,1-\epsilon)=0\).

**Proposition 3.4.** \(t_{\epsilon,\zeta}\) _is a convex under-estimator of f on_ \(\mathcal{X}_{\epsilon,\theta,\zeta,\eta}\)_. When f is restricted to_ \(\mathcal{T}_{\epsilon,\theta,\zeta}\)_, its convex envelope is given by_ \(t_{\epsilon,\zeta}\) _(i.e.,_ \(\breve{f}_{\mathcal{S}_{\epsilon,\theta,\zeta,\eta}}=t_{\epsilon,\zeta}\)_)._

_Proof._ The proof is similar to the proof of Proposition 3.2.

First, the denominator in the fraction that defines \(t_{\epsilon,\zeta}\) is strictly positive. Indeed, \((1-\zeta)(1-\epsilon)+\epsilon x-(1-\zeta)y=(1-\zeta)(1-\epsilon-y)+\epsilon x>0\) if \((x,y)\in\mathcal{X}_{\epsilon,\theta,\zeta,\eta}\backslash\{(0,1-\epsilon)\}\). So \(t_{\epsilon,\zeta}\) is well-defined on \(\mathcal{X}_{\epsilon,\theta,\zeta,\eta}\). It is also easy to prove the continuity of the function at \((0,1-\epsilon)\) since \(lim_{(x,y)\rightarrow(0,1-\epsilon)}t_{\epsilon,\zeta}(x,y)=0=t_{\epsilon,\zeta}(0,1-\epsilon)\).

