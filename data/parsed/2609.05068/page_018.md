## 3.2 Convex envelope of _f_ on \(\mathcal{S}_{\epsilon,\theta,\eta,\zeta}\)

We define the function \(s_{\epsilon,\theta}:\mathcal{X}_{\epsilon,\theta,\zeta,\eta}\rightarrow\mathbb{R}\) as \(s_{\epsilon,\theta}(x,y)=\frac{x}{1-\theta-\frac{x}{1-\frac{y-x-\theta}{1-\epsilon-\theta}}}\) if \((x,y)\neq(0,1-\epsilon)\), and \(s_{\epsilon,\theta}(0,1-\epsilon)=0\).

**Proposition 3.2.** \(s_{\epsilon,\theta}\) _is a convex under-estimator of f on_ \(\mathcal{X}_{\epsilon,\theta,\zeta,\eta}\)_. When f is restricted to_ \(\mathcal{S}_{\epsilon,\theta,\zeta,\eta}\)_, its convex envelope is given by_ \(s_{\epsilon,\theta}\) _(i.e.,_ \(\breve{f}_{\mathcal{S}_{\epsilon,\theta,\zeta,\eta}}=s_{\epsilon,\theta}\)).

_Proof._ Let us first check that the denominator of \(s_{\epsilon,\theta}(x,y)\) is strictly positive. Observe that \(1-\theta-\frac{x}{1-\frac{y-x-\theta}{1-\epsilon-\theta}}=1-\theta-x\frac{1-\epsilon-\theta}{1-\epsilon-y+x}\). \(1-\epsilon-y+x\) is non-zero on \(\mathcal{X}_{\epsilon,\theta,\zeta,\eta}\) if \((x,y)\neq(0,1-\epsilon)\). Using \(y-x\ge\theta\), we get \(1-\theta-\frac{x}{1-\frac{y-x-\theta}{1-\epsilon-\theta}}\ge 1-\theta-x\ge 1-y\ge\epsilon>0\). \(s_{\epsilon,\theta}\) is then well-defined on \(\mathcal{X}_{\epsilon,\theta,\zeta,\eta}\) and positive. It is also easy to prove the continuity of the function at \((0,1-\epsilon)\) since \(lim_{(x,y)\rightarrow(0,1-\epsilon)}s_{\epsilon,\theta}(x,y)=0=s_{\epsilon,\theta}(0,1-\epsilon)\).

To prove the convexity of \(s_{\epsilon,\theta}\) on \(\mathcal{X}_{\epsilon,\theta,\zeta,\eta}\), one can for example use the fact that the perspective function of a convex function is also convex. Consider the function \(f_\theta\) defined on \([0,1[\) by \(f_\theta(x)=f(x,x+\theta)=\frac{x}{1-x-\theta}\). \(f_\theta\) is obviously convex. Therefore, its perspective function _p_ defined as \(p_s(x,t)=tf_\theta(x/t)=\frac{x}{1-\theta-x/t}\) is convex. Since \(s_{\epsilon,\theta}(x,y)=p_s(x,1-\frac{y-x-\theta}{1-\epsilon-\theta})\) is the composition of a convex and an affine function, \(s_{\epsilon,\theta}\) is convex.

To show that \(s_{\epsilon,\theta}\) is an under-estimator of _f_ over \(\mathcal{X}_{\epsilon,\theta,\zeta,\eta}\) for _x\>_0, we should prove that, for \((x,y)\in\mathcal{X}_{\epsilon,\theta,\zeta,\eta}\), \(\frac{s_{\epsilon,\theta}(x,y)}{f(x,y)}=\frac{1-y}{1-\theta-\frac{x}{1-\frac{y-x-\theta}{1-\epsilon-\theta}}}=\frac{(1-y)(1-\epsilon+x-y)}{(1-\theta)(1-\epsilon+x-y)-x(1-\epsilon-\theta)}\) is less than 1. Considering the difference between the numerator and the denominator we get:

\((1-y)(1-\epsilon+x-y)-(1-\theta)(1-\epsilon+x-y)+x(1-\epsilon-\theta)=(\theta+x-y)(1-\epsilon-y)\)

which is obviously non-positive on the set \(\mathcal{X}_{\epsilon,\theta,\zeta,\eta}\). For _x_=0, both functions are equal to 0.

Finally, let us restrict _f_ to \(\mathcal{S}_{\epsilon,\theta,\zeta,\eta}\). Since \(s_{\epsilon,\theta}\) is a convex under-estimator of _f_, we already have \(\breve{f}_{\mathcal{S}_{\epsilon,\theta,\zeta,\eta}}\ge s_{\epsilon,\theta}\). For the other direction, given any \((x,y)\in\mathcal{S}_{\epsilon,\theta,\zeta,\eta}\), let \(\alpha=\frac{1-\epsilon+x-y}{1-\epsilon-\theta}\) and \(x_0=y_0-\theta=\frac{x}{\alpha}\). Observe that (_x_<sub>0</sub>_,y_<sub>0</sub>) and \((0,1-\epsilon)\) are both in \(\mathcal{S}_{\epsilon,\theta,\zeta,\eta}\), and (_x,y_) is a convex combination<tbc>

