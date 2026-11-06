It follows that the surviving terms satisfy the integer equality

\(u-v+2\sum_{j=1}^\ell(g_j-h)=0.\) (1)

For every target coordinate in the specified ranges, assign an integer weight by<tbc>

\(w(X_{j,a,g})=g^2,w(Y_{h,b,u})=hu-\ell h^2,w(Z_{h,c,v})=-hv.\)

<tbc>The total weight of a term satisfying (1) is

\(\sum_{j=1}^\ell g_j^2+h(u-v)-\ell h^2=\sum_{j=1}^\ell g_j^2-2h\sum_{j=1}^\ell(g_j-h)-\ell h^2\)<br>
\(=\sum_{j=1}^\ell(g_j-h)^2.\)

Every surviving term therefore has nonnegative total weight. Its weight is zero if and only if _g<sub>j</sub>=h_ for every \(1\le j\le\ell\), in which case (1) also gives _u=v_. When \(\ell=0\), the sum of squares is empty, and the Fourier condition itself gives _u=v_.

Apply the weight degeneration from Section 2: multiply each coordinate symbol by \(\varepsilon\) to the power of its weight and retain the coefficient of \(\varepsilon^0\). The resulting tensor is

\(\sum_{h=0}^{M-1}\sum_{a\in\mathcal{A}}\sum_{0\le b<b_h0\le c<c_h}\sum_{u=0}^{M-1}\alpha_{h,a,b,c}\left(\prod_{j=1}^\ell X_{j,a_j,h}\right)Y_{h,b,u}Z_{h,c,u}.\)

For a fixed _h_, the additional index _u_ is shared precisely by the last two legs. Relabeling the coordinates therefore identifies this block with \(A_h\otimes_KE_{k-1,k}^{(M)}\). The first \(\ell\) legs carry _h_ as their last coordinate index, and the last two legs already carry _h_ as their sector label. Hence no coordinate on any leg is shared between different values of _h_. If _A<sub>h</sub>_=0, delete its now separate coordinate sector on every leg by coordinate projection. Every such sector is zero, so this removes no supported term. The remaining tensor is the full direct sum in the statement, up to independent coordinate permutations within the legs. Composing the weight degeneration with these projections proves the claimed degeneration.

## 3.2 The entropy inequality

The construction uses (2_k_-1)_M_ source copies. When every _A<sub>h</sub>_ is nonzero, its output has _M_ direct-sum blocks, and each block retains an _M_-dimensional edge tensor. The edge index is not an additional direct-sum label. To obtain an asymptotic comparison, we apply the construction to Kronecker powers and retain sector words with prescribed frequencies. Their number is measured by entropy, while every retained block has the same spectral value. These two multiplicities give the following inequality.

**Corollary 3.2** (entropy inequality)**.** _Let_ \(k\ge 2\) _and_ \(s\ge 1\) _be integers. Let A be a complex k-th order tensor with nonzero blocks A_<sub>1</sub>_,...,A<sub>s</sub>, sharing their first k_-2 _legs and occupying matched, pairwise disjoint coordinate sectors on their last two legs, as defined in Theorem 3.1. Let_ \(\phi\in\Phi_k\) _and let_ \(p_{k-1,k}^{(\phi)}\) _be its spectral edge weight from Definition 4.3. For every probability vector_ \(\theta=(\theta_1,\dots,\theta_s)\),<tbc>

\(\phi(A)\ge exp(p_{k-1,k}^{(\phi)}H(\theta))\prod_{i=1}^s\phi(A_i)^{\theta_i},\)

