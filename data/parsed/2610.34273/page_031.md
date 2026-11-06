To identify the middle block, define<tbc>

\(\bar{i}_j=a_j-1-i_j(1\le j\le n-2),r=z-(h+S).\)

<tbc>The middle output interval gives \(0\le r<h\). Replacing _i<sub>j</sub>_ by \(a_j-1-\bar{i}_j\) in the support equation gives

\(y=h+r+\sum_{j=1}^{n-2}\bar{i}_j,z=h+S+r.\)

Conversely, choose arbitrary integers \(0\le\bar{i}_j<a_j\) for \(1\le j\le n-2\) and \(0\le r<h\). These equations give \(h\le y\le 2h+S-1\) and \(h+S\le z\le 2h+S-1\), so they specify a supported entry in the middle block. Therefore the displayed parametrization describes all and only its supported entries, each with coefficient one.

Reflect each shared input basis, and subtract _h_ and _h+S_ from the last-input and output indices, respectively. With \(y'=y-h\), the equation is \(y'=r+\sum_{j=1}^{n-2}\bar{i}_j\). This is the defining support equation of _C_ with its last two legs exchanged: _r_ is its length-_h_ input, while \(y'\) is its length-(_h+S_) output. Let \(\sigma\in S_n\) denote that exchange. The middle block is thus locally isomorphic to \(\sigma C\). This identification concerns the middle block as an individual tensor; it does not apply a block-dependent map to the shared legs of the whole three-block tensor.

Apply Corollary 3.2 to the retained blocks with probability vector (1/3,1/3,1/3), whose entropy is ln3. For every \(\pi\in S_n\), degeneration monotonicity gives<tbc>

\(\phi_\pi\big(\mathcal{C}_n(a_1,\dots,a_{n-2},B)\big)\ge 3^{p_{n-1,n}^{(\phi_\pi)}}\phi_\pi(C)^{2/3}\phi_\pi(\sigma C)^{1/3}.\)

<tbc>Since \(\pi\mapsto\pi\sigma\) is a bijection of _S<sub>n</sub>_,<tbc>

\(\prod_{\pi\in S_n}\phi_\pi(\sigma C)=\prod_{\pi\in S_n}\phi_\pi(C).\)

<tbc>Multiplying the spectral inequalities over all \(\pi\in S_n\), and then taking the power \(1/(n!t_\phi)\), therefore gives

\(P_\phi(a_1,\dots,a_{n-2},B)\ge 3^\frac{1}{n!t_\phi}\sum_{\pi\in S_n}p_{n-1,n}^{(\phi_\pi)}\left(\prod_{\pi\in S_n}\phi_\pi(C)\right)^{1/(n!t_\phi)}=3P_\phi(a_1,\dots,a_{n-2},h),\)

where the final equality uses (2). Since _B_=3_h+S_, this is the required inequality.

## 4.4 Diagonal growth

We now extend the diagonal-growth step of OpenAI \[Ope26a, Section 5 and Lemma 5.1\] to _n_-1 input coordinates. Discrete concavity bounds a long increment by its first step, while shifted tripling gives a lower bound on that long increment. We apply the resulting estimate along a path that increases each coordinate once. Keeping track of all _n_-1 steps gives the exponent 2(_n_-1)_/n_. Comparing this growth with the linear rank bound from Subsection 4.1 then bounds the average spectral edge weight.

**Lemma 4.10** (diagonal growth)**.** _Let_ \(n\ge 3\) _be an integer. Suppose that_ \(F:\mathbb{N}_{>0}^{n-1}\rightarrow\mathbb{R}_{>0}\) _is symmetric, that F_(1_,...,_1)=1_, and that it satisfies the concavity and shifted tripling inequalities in Lemmas 4.8 and 4.9, with F in place of_ \(P_\phi\)_. Then, for every positive integer a,_<tbc>

\(F(\underbrace{a,\dots,a}_{n-1})\ge a^{2(n-1)/n}.\)

