the convex envelope on \(\mathcal{X}_{\epsilon,\theta,\zeta,\eta}\).

## 3.1 Convex envelope of _f_ on \(\mathcal{R}_{\epsilon,\theta,\eta}\)

Consider the function \(r_\eta:\mathcal{X}_{\epsilon,\theta,\zeta,\eta}\rightarrow\mathbb{R}\) where \(r_\eta(x,y)=\frac{x}{1-\eta}\).

**Proposition 3.1.** \(r_\eta\) _is a convex under-estimator of f on_ \(\mathcal{X}_{\epsilon,\theta,\zeta,\eta}\) _(i.e.,_ \(\forall(x,y)\in\mathcal{X}_{\epsilon,\theta,\zeta,\eta}\), \(r_\eta(x,y)\le\check{f}\mathcal{X}_{\epsilon,\theta,\zeta,\eta}(x,y)\le f(x,y)\)_). When f is restricted to_ \(\mathcal{R}_{\epsilon,\theta,\eta}\)_, its convex envelope is given by_ \(r_\eta\) _(i.e.,_ \(\check{f}=r_\eta\)).

_Proof._ \(r_\eta\) is linear and thus convex. We also have \(r_\eta\le f\) on \(\mathcal{X}_{\epsilon,\theta,\zeta,\eta}\) since \(y\ge\eta\).

So \(r_\eta\) is a convex under-estimator of _f_. To show that it is the convex envelope of _f_ on \(\mathcal{R}_{\epsilon,\theta,\eta}\), let us show that \(\check{f}(x,y)\le r_\eta(x,y),\forall(x,y)\in\mathcal{R}_{\epsilon,\theta,\eta}\). Observe that \((x,y)\in\mathcal{R}_{\epsilon,\theta,\eta}\) can be written as \(\alpha(x_0,\eta)+(1-\alpha)(0,1-\epsilon)\) with \(\alpha=\frac{x}{x_0}\in[0,1]\) and \(x_0=x\frac{1-\epsilon-\eta}{1-\epsilon-y}\) . Note that \((x_0,\eta)\) and \((0,1-\epsilon)\) both belong to \(\mathcal{R}_{\epsilon,\theta,\eta}\), and that \(r_\eta(x,y)=\alpha f(x_0,\eta)+(1-\alpha)f(0,1-\epsilon)\). By convexity of \(\check{f}\), we must have \(r_\eta\ge\check{f}\), and thus \(r_\eta\) is the convex envelope of _f_ restricted to \(R_{\epsilon,\theta,\eta}\).

y
1 - E
T e,0,
S e,0,
R e,0,n
n
θ
n - θ
1 -
x

Figure 2: Representation of the domain \(\mathcal{X}_{\epsilon,\theta,\zeta,\eta}\) of the function _f_, and its partition in \(\mathcal{R}_{\epsilon,\theta,\eta}\cup\mathcal{S}_{\epsilon,\theta,\zeta,\eta}\cup\mathcal{T}_{\epsilon,\theta,\zeta}\).

