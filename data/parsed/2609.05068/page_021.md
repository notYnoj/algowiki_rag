_Proof._ From Propositions 3.1, 3.2 and 3.4, \(max(r_\eta(x,y),s_{\epsilon,\theta}(x,y),t_{\epsilon,\zeta}(x,y))\) is a convex under-estimator of _f_ on \(\mathcal{X}_{\epsilon,\theta,\zeta,\eta}\), showing that \(\breve{f}_{\mathcal{X}_{\epsilon,\theta,\zeta,\eta}}\ge max(r_\eta(x,y),s_{\epsilon,\theta}(x,y),t_{\epsilon,\zeta}(x,y))\).

To show equality, first observe that \(\mathcal{R}_{\epsilon,\theta,\eta}\subset\mathcal{X}_{\epsilon,\theta,\zeta,\eta}\) implies that \(\breve{f}_{\mathcal{X}_{\epsilon,\theta,\zeta,\eta}}(x,y)\le\breve{f}_{\mathcal{R}_{\epsilon,\theta,\eta}}(x,y)\) for any \((x,y)\in\mathcal{R}_{\epsilon,\theta,\eta}\).

Similarly, \(\breve{f}_{\mathcal{X}_{\epsilon,\theta,\zeta,\eta}}(x,y)\le\breve{f}_{\mathcal{S}_{\epsilon,\theta,\eta,\zeta}}(x,y)\) for any \((x,y)\in\mathcal{S}_{\epsilon,\theta,\eta,\zeta}\), and \(\breve{f}_{\mathcal{X}_{\epsilon,\theta,\zeta,\eta}}(x,y)\le\breve{f}_{\mathcal{T}_{\epsilon,\theta,\zeta}}(x,y)\) for any \((x,y)\in\mathcal{T}_{\epsilon,\theta,\zeta}\).

Using that \(\breve{f}_{\mathcal{R}_{\epsilon,\theta,\eta}}=r_\eta\), \(\breve{f}_{\mathcal{S}_{\epsilon,\theta,\eta,\zeta}}=s_{\epsilon,\theta}\) and \(\breve{f}_{\mathcal{T}_{\epsilon,\theta,\zeta}}=t_{\epsilon,\zeta}\), we deduce that:

\(\forall(x,y)\in\mathcal{R}_{\epsilon,\theta,\eta},\breve{f}_{\mathcal{X}_{\epsilon,\theta,\zeta,\eta}}(x,y)\le r_\eta(x,y)=max(r_\eta(x,y),s_{\epsilon,\theta}(x,y),t_{\epsilon,\zeta}(x,y)),\)<br>
\(\forall(x,y)\in\mathcal{S}_{\epsilon,\theta,\eta,\zeta},\breve{f}_{\mathcal{X}_{\epsilon,\theta,\zeta,\eta}}(x,y)\le s_{\epsilon,\theta}(x,y)=max(r_\eta(x,y),s_{\epsilon,\theta}(x,y),t_{\epsilon,\zeta}(x,y)),\)<br>
\(\forall(x,y)\in\mathcal{T}_{\epsilon,\theta,\zeta},\breve{f}_{\mathcal{X}_{\epsilon,\theta,\zeta,\eta}}(x,y)\le t_{\epsilon,\zeta}(x,y)=max(r_\eta(x,y),s_{\epsilon,\theta}(x,y),t_{\epsilon,\zeta}(x,y)).\)

Since \(\mathcal{X}_{\epsilon,\theta,\zeta,\eta}=\mathcal{R}_{\epsilon,\theta,\eta}\cup\mathcal{S}_{\epsilon,\theta,\eta,\zeta}\cup\mathcal{T}_{\epsilon,\theta,\eta}\), \(\breve{f}_{\mathcal{X}_{\epsilon,\theta,\zeta,\eta}}(x,y)\le max(r_\eta(x,y),s_{\epsilon,\theta}(x,y),t_{\epsilon,\zeta}(x,y))\) for any \((x,y)\in\mathcal{X}_{\epsilon,\theta,\zeta,\eta}\).

Figure 3 illustrates the difference between the values of the function _f_ and those of its under-estimators, highlighting the tightness of the relaxation.

Observe that the relaxation is tighter when _x_ is large or when _y-x_ is small, corresponding respectively to high path usage and low arc usage by the other paths in the DCMCF problem.

**Proposition 3.5.** _A constraint of the type_ \(\breve{f}_{\mathcal{X}_{\epsilon,\theta,\zeta,\eta}}(x,y)\le d,\forall(x,y)\in\mathcal{X}_{\epsilon,\theta,\zeta,\eta}\) _can be formulated as a set of second-order cone programming constraints._

_Proof._ A constraint of type \(\breve{f}_{\mathcal{X}_{\epsilon,\theta,\zeta,\eta}}(x,y)=max(r_\eta(x,y),s_{\epsilon,\theta}(x,y),t_{\epsilon,\zeta}(x,y))\le\)<tbc>

1.0
f/ rn
1.0
f/ S
1.0
f/ t,
1.0
f/ max(rn, S,0, t,
0.8
0.8
0.8
0.8
2.166
1.736
0.6
0.6
0.6
0.6
1.515
1.372
>
>
1.269
0.4
0.4
0.4
0.4
1.190
1.128
0.2
0.2
0.2
1.077
1.034
0.0
0.0
0.0
0.0
0.0
0.00
0.25
0.50
0.75
1.00
0.00
0.25
0.50
0.75
1.00
0.00
0.25
0.50
0.75
1.00
1.000
X
X
X
X

Figure 3: Values and multiplicative errors of \(r_\eta\), \(s_{\epsilon,\theta}\), \(t_{\epsilon,\theta}\) and \(\breve{f}_{\mathcal{X}_{\epsilon,\theta,\zeta,\eta}}\) with \(\epsilon=0.1\), \(\zeta=0.3\), \(\eta=0.1\), and \(\theta=0\). Values are lower (in blue) when relaxations are closer to the actual value of _f_.

