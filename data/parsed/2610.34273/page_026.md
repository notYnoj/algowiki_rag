Taking logarithms and dividing by _N_ yields

\(\frac{\ell_N}{N}p_{i,j}^{(\phi)}\le\mathrm{log}_2f(q)\le\frac{\ell_N+1}{N}p_{i,j}^{(\phi)}.\)

Both outer expressions tend to \(p_{i,j}^{(\phi)}\mathrm{log}_2q\). Therefore \(f(q)=q^{p_{i,j}^{(\phi)}}\). For _q_=1, the formula follows from \(E_{i,j}^{(1)}=\mathsf{l}_n(1)\).

Consider the star tensor \(T=\otimes_{K_{j=2}}^nE_{1,j}^{(2)}\). At its first leg, a basis vector is indexed by a tuple \((b_2,\dots,b_n)\in\{0,1\}^{n-1}\). Apply the linear map sending this vector to \(e_b^{(2)}\) if \(b_2=\cdots=b_n=b\), and to zero otherwise. At leg _j_, for \(2\le j\le n\), leave the coordinate _b<sub>j</sub>_ unchanged. The surviving terms are exactly the two terms of l_<sub>n</sub>_(2). Restriction monotonicity and multiplicativity now imply

\(2=\phi(\mathsf{l}_n(2))\le\phi(T)=\prod_{j=2}^n\phi(E_{1,j}^{(2)})=2^{\sum_{j=2}^np_{1,j}^{(\phi)}}.\)

Taking logarithms proves the first inequality. Finally, \(\mathsf{GT}_q(K_n)=\otimes_{K_{1\le i<j\le n}}E_{i,j}^{(q)}\) by Definition 2.20. Applying multiplicativity and the edge formula proves the asserted value on the complete graph.

We now average over all permutations of the _n_ tensor legs. This extends the six-factor symmetrization used in \[Ope26a, Equation (4.4)\].

**Definition 4.5** (symmetric spectral profile)**.** Let \(n\ge 3\) be an integer, let \(\phi\in\Phi_n\), and let \(p_{i,j}^{(\phi)}\) be its spectral edge weights. Define their average by<tbc>

\(m=\genfrac(){pt}{2}{n}{2},t_\phi=\frac{1}{m}\sum_{1\le i<j\le n}p_{i,j}^{(\phi)}.\)

<tbc>For every permutation \(\pi\in S_n\), put \(\phi_\pi(T)=\phi(\pi T)\), where the action on tensor legs is defined in Section 2. For all positive integers _a_<sub>1</sub>_,...,a_<sub>_n_-1</sub>, define the _symmetric spectral profile_

\(P_\phi(a_1,\dots,a_{n-1})=\left(\prod_{\pi\in S_n}\phi_\pi\big(\mathcal{C}_n(a_1,\dots,a_{n-1})\big)\right)^{1/(n!t_\phi)}.\)

Lemma 4.4 gives \(t_\phi\ge 1/m>0\), so the definition uses a positive exponent. Every map \(\phi_\pi\) is a spectral point: permutation of the legs preserves restriction, the diagonal tensors, and both semiring operations.

For integers \(1\le u<v\le n\) and \(\pi\in S_n\), Definition 4.3 gives \(p_{u,v}^{(\phi_\pi)}=\mathrm{log}_2\phi_\pi(E_{u,v}^{(2)})\). The image of the pair (_u,v_) under \(\pi\) is the pair \((\mathrm{min}(\pi(u),\pi(v)),\mathrm{max}(\pi(u),\pi(v)))\). For any fixed pair \(1\le i<j\le n\), exactly 2(_n_-2)! permutations send (_u,v_) to (_i,j_) in this sense: there are two choices for the images of _u,v_, and (_n_-2)! choices for the remaining images. Consequently,<tbc>

\(\sum_{\pi\in S_n}p_{u,v}^{(\phi_\pi)}=2(n-2)!\sum_{1\le i<j\le n}p_{i,j}^{(\phi)}=n!t_\phi(1\le u<v\le n).\) (2)

<tbc>**Lemma 4.6** (basic properties of the profile)**.** _For every integer_ \(n\ge 3\) _and every spectral point_ \(\phi\in\Phi_n\)_, the profile in Definition 4.5 is positive and symmetric in its n_-1 _arguments. For every positive integer b and all positive integers a_<sub>1</sub>_,...,a_<sub>_n_-1</sub>_, it satisfies_<tbc>

\(P_\phi(1,\dots,1,b)=b,P_\phi(a_1,\dots,a_{n-1})\le\left(1+\sum_{j=1}^{n-1}(a_j-1)\right)^{1/t_\phi}.\)

