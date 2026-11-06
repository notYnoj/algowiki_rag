quotient lifts leaves an element of the output kernel. There are consequently unique complex coefficients \(\eta_{r,i}(f)\), for \(0\le r\le S+b-2\) and \(0\le i\le b\), such that

\(fq_{b-1,i}=\sum_{r=0}^{S+b}c_{r-i}q_{S+b-1,r}+\sum_{r=0}^{S+b-2}\eta_{r,i}(f)k_{S+b-1,r}(0\le i\le b),fk_{b-1,j}=\sum_{r=0}^{S+b-2}c_{r-j}k_{S+b-1,r}(0\le j\le b-2).\text{(3)}\)

The second equality follows by expanding _fDu_<sup>_b_-2-_j_</sup>_v<sup>j</sup>_. In particular, a kernel input has no quotient output. A quotient input can have a kernel output, and the coefficients \(\eta_{r,i}(f)\) record precisely those terms.

The chosen input and output bases depend only on _b_ and _S_. They do not depend on _f_, or on its factorization as \(\prod_{j=1}^{n-2}f_j\). Therefore (3) holds simultaneously for every choice of basis vector on each of the first _n_-2 input legs. The two basis changes are invertible local maps on the last input and output legs; no shared leg is changed. On the input leg, the coefficient tensor uses the dual of the basis-change matrix, which is again invertible.

Assign weight zero to all shared coordinates and quotient coordinates. Assign weight -1 to the last-input kernel coordinates and weight +1 to the output kernel coordinates. Every term in the first sum of (3) has total weight zero. Every term involving \(\eta_{r,i}(f)\) has weight +1, and every term in its second line has weight zero. The only coordinate pairs that could have weight -1 are a kernel input and a quotient output; their coefficients are zero. The weight degeneration of Remark 2.16 therefore discards exactly the terms involving \(\eta_{r,i}(f)\).

The remaining quotient-to-quotient coefficients _c_<sub>_r-i_</sub> express multiplication from _V<sub>b</sub>_ to _V_<sub>_S+b_</sub>. The remaining kernel-to-kernel coefficients _c_<sub>_r-j_</sub> express multiplication from _V_<sub>_b_-2</sub> to _V_<sub>_S+b_-2</sub>. Taking their dependence on the separate shared inputs into account identifies the two retained coefficient tensors as

\(C_+=\mathcal{C}_n(a_1,\dots,a_{n-2},b+1),C_-=\mathcal{C}_n(a_1,\dots,a_{n-2},b-1).\)

They share the first _n_-2 legs and occupy disjoint matched sectors in the last two legs. Their last-input dimensions are _b_+1 and _b_-1, and their output dimensions are _S+b_+1 and _S+b_-1, respectively. These dimensions agree with Definition 4.1.

Write _C_=C_<sub>n</sub>(a_<sub>1</sub>_,...,a_<sub>_n_-2</sub>_,b_). For every \(\pi\in S_n\) and every real number \(0\le\theta\le 1\), degeneration monotonicity and Corollary 3.2 imply

\(2^{p_{n-1,n}^{(\phi\pi)}}\phi_\pi(C)\ge exp\big(p_{n-1,n}^{(\phi\pi)}H(\theta,1-\theta)\big)\phi_\pi(C_+)^\theta\phi_\pi(C_-)^{1-\theta}.\)

The factor on the left is the spectral value of the additional edge tensor \(E_{n-1,n}^{(2)}\). The entropy factor on the right uses the same pair of legs, because these are precisely the two unshared legs of the retained blocks.

Use one common value of \(\theta\) for all permutations. Multiply over all \(\pi\in S_n\), take the power \(1/(n!t_\phi)\), and apply (2). By the definition of \(P_\phi\), the resulting inequality is<tbc>

\(2P_\phi(a_1,\dots,a_{n-2},b)\ge e^{H(\theta,1-\theta)}P_\phi(a_1,\dots,a_{n-2},b+1)^\theta P_\phi(a_1,\dots,a_{n-2},b-1)^{1-\theta}.\)

<tbc>Put \(A=P_\phi(a_1,\dots,a_{n-2},b+1)\) and \(B=P_\phi(a_1,\dots,a_{n-2},b-1)\). Both are positive by Lemma 4.6, so we may choose \(\theta=A/(A+B)\). Then \(A/\theta=B/(1-\theta)=A+B\), and<tbc>

\(e^{H(\theta,1-\theta)}A^\theta B^{1-\theta}=\big(\frac{A}{\theta}\big)^\theta\big(\frac{B}{1-\theta}\big)^{1-\theta}=A+B.\)

