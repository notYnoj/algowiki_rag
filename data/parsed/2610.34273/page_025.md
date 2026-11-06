The interpolation identity holds for every choice of the input coefficients. Equating their coefficients therefore gives the tensor identity

\(\mathcal{C}_n(a_1,\dots,a_{n-1})=\sum_{r=1}^Dv_{1,r}\otimes_C\cdots\otimes_Cv_{n-1,r}\otimes_Cc_r.\)

This is a sum of _D_ simple tensors, so the rank is at most _D_.

For the reverse inequality, flatten the output leg against all input legs, as in Definition A.1. For every integer \(0\le s<D\), row _s_ has entry 1 precisely at the input tuples with \(i_1+\cdots+i_{n-1}=s\). Such a tuple exists for every _s_: the sum of the integer intervals \[_a<sub>j</sub>_\]<sub>0</sub>, for \(1\le j\le n-1\), is the integer interval \[_D_\]<sub>0</sub>. To see this directly, the sum of {0_,...,r_} and {0_,...,t_} is {0_,...,r+t_}, since an integer _s_ in the latter interval can be written as min{_s,r_}+(_s_-min{_s,r_}). Repeatedly applying this observation proves the claim about the input intervals.

Thus every row is nonzero. Different rows have disjoint supports, because an input tuple has a unique coordinate sum. The _D_ rows are therefore linearly independent. The flattening has matrix rank _D_, and every simple tensor has flattening rank at most one. Hence the tensor rank is at least _D_, proving equality.

We next attach one number to each pair of tensor legs. These numbers depend on a chosen spectral point. They are distinct from the graph edge exponent \(\tau(G)\) in Definition 2.22, which is defined using asymptotic rank itself.

**Definition 4.3** (spectral edge weights)**.** Let \(n\ge 2\) be an integer, and let \(\phi\in\Phi_n\). For every pair of integers \(1\le i<j\le n\), define

\(p_{i,j}^{(\phi)}=log_2\phi(E_{i,j}^{(2)}).\)

Here \(E_{i,j}^{(2)}\) is the complex _n_-th order edge tensor from Definition 2.20: only legs _i_ and _j_ have dimension greater than one. We call \(p_{i,j}^{(\phi)}\) its _spectral edge weight under_ \(\phi\).

The next lemma extends the single-edge calculation in \[Ope26a, Section 2\]. It shows that this weight determines the spectral value for every edge dimension, not only dimension two.

**Lemma 4.4** (spectral edge weights)**.** _Let_ \(n\ge 2\) _be an integer, let_ \(\phi\in\Phi_n\)_, and let_ \(p_{i,j}^{(\phi)}\) _be as in Definition 4.3. For all integers_ \(1\le i<j\le n\) _and_ \(q\ge 1\)_, we have_ \(0\le p_{i,j}^{(\phi)}\le 1\) _and_ \(\phi(E_{i,j}^{(q)})=q^{p_{i,j}^{(\phi)}}\)_. Moreover,_

\(\sum_{j=2}^np_{1,j}^{(\phi)}\ge 1,\phi(\mathsf{GT}_q(K_n))=q^{\sum_{1\le i<j\le n}p_{i,j}^{(\phi)}}(q\ge 1).\)

_Proof._ Fix integers \(1\le i<j\le n\), and set \(f(q)=\phi(E_{i,j}^{(q)})\) for every positive integer _q_. If \(q\le r\), projecting the two nontrivial legs onto their first _q_ coordinates restricts \(E_{i,j}^{(r)}\) to \(E_{i,j}^{(q)}\). Thus _f_ is nondecreasing. For all positive integers _q,r_, the local pairing of the edge labels gives \(E_{i,j}^{(q)}\otimes_KE_{i,j}^{(r)}\cong E_{i,j}^{(qr)}\), so _f(qr_)=_f(q)f(r_). The tensor \(E_{i,j}^{(q)}\) is nonzero and has rank _q_: its defining sum has _q_ terms, and its flattening across leg _i_ has rank _q_. Hence \(1\le f(q)\le q\), which in particular proves \(0\le p_{i,j}^{(\phi)}=log_2f(2)\le 1\).

Let \(q\ge 2\) be an integer. For every positive integer _N_, put \(\ell_N=\lfloor Nlog_2q\rfloor\). Since \(2^{\ell_N}\le q^N<2^{\ell_N+1}\), monotonicity and multiplicativity give<tbc>

\(f(2)^{\ell_N}\le f(q)^N\le f(2)^{\ell_N+1}.\)

