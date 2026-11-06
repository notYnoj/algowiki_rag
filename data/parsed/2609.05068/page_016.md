\(\sum_{a\in p}f(\frac{b^kx_p^k}{c_a},\frac{y_a}{c_a})\le b^kx_p^k\times d^k\forall k\in K,p\in P^k.\) (11)

To obtain good convex relaxations, one can then focus on the convex envelope of _f_. More precisely, one can notice that, for every \(k\in K\), \(p\in P^k\) and \(a\in A\), the domain of \(\frac{b^kx_p^k}{c_a}\) and \(\frac{y_a}{c_a}\) is narrower than \[0,1\]<sup>2</sup>:

- Inequality (2) ensures that \(\frac{b^kx_p^k}{c_a}\le\frac{y_a}{c_a}\).<tbc>

- Inequality (3) ensures that \(\frac{y_a}{c_a}<1\) (otherwise the delay of link _a_ would be infinite, violating the delay constraint).<tbc>

- Finally, both the \(x_p^k\) and _y<sub>a</sub>_ variable are nonnegative.

Therefore we will compute the convex envelope \(\breve{f}\) of _f_ on the polyhedral subset \(\mathcal{X}_{\epsilon,\theta,\zeta,\eta}\) defined for \((\epsilon,\zeta,\eta,\theta)\) in \(]0,1[^2\times[0,1]^2\) by:

\(\mathcal{X}_{\epsilon,\theta,\zeta,\eta}=\{(x,y)\in[0,1]^2:y\ge x+\theta,y\in[\eta,1-\epsilon],x\le 1-\zeta\}.\) (12)

As will be shown in Section 3.6, given some \(p\in P^k\) and \(a\in p\), inequalities relating \(x_p^k\) and _y<sub>a</sub>_ can be easily used to deduce possible values of \((\epsilon,\theta,\zeta,\eta)\in[0,1]^4\). Note that these values will depend on _p_ and _a_ and one can solve some intermediate convex problems to get the best values. Before providing complete details in Section 3.6, let us start for now by computing the convex envelope of _f_ on \(\mathcal{X}_{\epsilon,\theta,\zeta,\eta}\).

Let us first divide \(\mathcal{X}_{\epsilon,\theta,\zeta,\eta}\) into 3 polyhedral subsets (see Figure 2 for illustration) \(\mathcal{X}_{\epsilon,\theta,\zeta,\eta}=\mathcal{R}_{\epsilon,\theta,\eta}\cup\mathcal{S}_{\epsilon,\theta,\zeta,\eta}\cup\mathcal{T}_{\epsilon,\theta,\zeta}\), where

\(\mathcal{R}_{\epsilon,\theta,\eta}=\left\{(x,y)\in[0,1]^2:y\ge\eta,y\le 1-\epsilon-\frac{1-\epsilon-\eta}{\eta-\theta}x\right\}\)<br>
\(\mathcal{S}_{\epsilon,\theta,\zeta,\eta}=\left\{(x,y)\in[0,1]^2:y\ge x+\theta,y\ge 1-\epsilon-\frac{1-\epsilon-\eta}{\eta-\theta}x,y\le 1-\epsilon-\frac{\zeta-\epsilon-\theta}{1-\zeta}x\right\}\)<br>
\(\mathcal{T}_{\epsilon,\theta,\zeta}=\left\{(x,y)\in[0,1]^2:y\le 1-\epsilon,x\le 1-\zeta,y\ge 1-\epsilon-\frac{\zeta-\epsilon-\theta}{1-\zeta}x\right\}.\)

Notice that the partition makes sense (i.e., the 3 subsets are well-defined) only if

\(0\le\theta\le\eta\le 1-\zeta+\theta\le 1-\epsilon\le 1.\) (13)

We will compute the convex envelope of _f_ on each of the subsets \(\mathcal{R}_{\epsilon,\theta,\eta}\), \(\mathcal{S}_{\epsilon,\theta,\zeta,\eta}\) and \(\mathcal{T}_{\epsilon,\zeta,\eta}\). Then we will show that they can be combined to obtain<tbc>

