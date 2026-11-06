Convexity of \(t_{\epsilon,\zeta}\) can be proven by considering the convex function \(f_\zeta\) defined on \([-\infty,1-\epsilon]\) by \(f_\zeta(y)=f(1-\zeta,y)=\frac{1-\zeta}{1-y}\). Because \(f_\zeta\) is convex, its perspective function _p<sub>t</sub>_ defined as \(p_t(x,t)=tf_\zeta(\frac{x}{t})=\frac{t^2(1-\zeta)}{t-y}\) is convex. Since \(t_{\epsilon,\zeta}(x,y)=p_t(y-(1-\frac{x}{1-\zeta})(1-\epsilon)\), \(\frac{x}{1-\zeta})\) is the composition of a convex and an affine function, \(t_{\epsilon,\zeta}\) is convex.

To show that \(t_{\epsilon,\zeta}\) is an under-estimator of _f_ over \(\mathcal{X}_{\epsilon,\theta,\zeta,\eta}\) for _x\>_0, we should prove that, for \((x,y)\in\mathcal{X}_{\epsilon,\theta,\zeta,\eta}\), \(\frac{t_{\epsilon,\zeta}(x,y)}{f(x,y)}=\frac{x(1-y)}{(1-\zeta)(1-\epsilon)+\epsilon x-(1-\zeta)y}\) is less than 1. Considering the difference between the numerator and the denominator, we get:

\(x-yx-(1-\zeta)(1-\epsilon)-\epsilon x+(1-\zeta)y=(1-\epsilon)(1-\zeta-x)+y(1-\zeta-x)=-(1-\epsilon-y)(1-\zeta-x)\)

which is obviously nonpositive on \(\mathcal{X}_{\epsilon,\theta,\zeta,\eta}\) (for _x_=0, we have \(f(x,y)=t_{\epsilon,\zeta}(x,y)=0\)).

Finally, let us consider the restriction of _f_ to \(\mathcal{T}_{\epsilon,\theta,\zeta}\). As \(t_{\epsilon,\zeta}\) is a convex under-estimator of _f_, it satisfies \(t_{\epsilon,\zeta}(x,y)\le\breve{f}_{\mathcal{T}_{\epsilon,\zeta}}(x,y)\). Observe that each (_x,y_) of \(\mathcal{T}_{\epsilon,\theta,\zeta}\) can be expressed as a convex combination of two members of \(\mathcal{T}_{\epsilon,\theta,\zeta}\): \((x,y)=\alpha(1-\zeta,y_0)+(1-\alpha)(0,1-\epsilon)\), with \(\alpha=\frac{x}{1-\zeta}\) and \(y_0=y\frac{1-\zeta}{x}-\frac{(1-\zeta)(1-\epsilon)}{x}+1-\epsilon\). Moreover, one can easily check that \(t_{\epsilon,\zeta}(x,y)=\alpha f(1-\zeta,y_0)+(1-\alpha)f(0,1-\epsilon)\) proving, by convexity of \(\breve{f}_{\mathcal{T}_{\epsilon,\theta,\zeta}}\), that \(t_{\epsilon,\zeta}(x,y)\ge\breve{f}_{\mathcal{T}_{\epsilon,\theta,\zeta}}(x,y)\).

**Remark 3.1.** _The constraint_ \(t_{\epsilon,\zeta}(x,y)\le d\) _can be expressed through second-order cone programming since the inequality_ \(d\times((1-\zeta)(1-\epsilon)+\epsilon x-(1-\zeta)y)\ge x^2\) _is a convex hyperbolic constraint._

Note that Remark 3.1 also allows to prove convexity of \(t_{\epsilon,\zeta}\).

## 3.4 Convex envelope of _f_ on \(\mathcal{X}_{\epsilon,\theta,\zeta,\eta}\)

**Theorem 3.1.** _The convex envelope of f on_ \(\mathcal{X}_{\epsilon,\theta,\zeta,\eta}\) _is given by:_

\(\breve{f}_{\mathcal{X}_{\epsilon,\theta,\zeta,\eta}}(x,y)=max(r_\eta(x,y),s_{\epsilon,\theta}(x,y),t_{\epsilon,\zeta}(x,y))\breve{f}_{\mathcal{X}_{\epsilon,\theta,\zeta,\eta}}(x,y)=max(\frac{x}{1-\eta},\frac{x}{1-\theta-\frac{y-x-\theta}{1-\epsilon-\theta}},\frac{x^2}{(1-\zeta)(1-\epsilon)+\epsilon x-(1-\zeta)y}).\) (15)

