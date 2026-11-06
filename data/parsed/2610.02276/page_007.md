<tbc>For a type-_J_ non-centre output, (2) becomes<tbc>

\(q_J=\frac{N+W}{N(A+W)},\)

<tbc>and direct subtraction gives<tbc>

\(q_J-\frac{1}{A}=\frac{W}{NA(A+W)}.\) (4)

<tbc>Meanwhile, (3) is exactly<tbc>

\(p_c=\mathbb{E}\frac{1}{A+W}.\)

<tbc>Since E_W_=0,

\(p_c-\frac{1}{A}=-\mathbb{E}\frac{W}{A(A+W)}\) (5)

\(=\mathbb{E}\frac{W^2}{A^2(A+W)}.\) (6)

The second identity follows by adding the zero term E(_W/A_<sup>2</sup>). Its right-hand side is positive because _A+W\>_0 and _W_ is nonzero with positive probability.

Using the multiplicities \(\genfrac(){pt}{2}{k}{j}\) to convert the non-centre sum to expectation under _J_, (4) and (6) yield the exact identity

\(b(T_{k,N-k})=\frac{1}{2}\left(\mathbb{E}\frac{W^2}{A^2(A+W)}+\mathbb{E}\frac{|W|}{A(A+W)}\right)>0.\) (7)

This is the exact expectation identity in the frozen theorem package.

For the upper bound, \(W\ge-k\), so \(A+W\ge A-k\), while<tbc>

\(\mathbb{E}W^2=k,\mathbb{E}|W|\le\sqrt{\mathbb{E}W^2}=\sqrt{k}.\)

<tbc>Consequently<tbc>

\(b(T_{k,N-k})\le\frac{1}{2}\left(\frac{k}{A^2(A-k)}+\frac{\sqrt{k}}{A(A-k)}\right)=O\left(\frac{\sqrt{k}}{4^k}\right).\) (8)

<tbc>Finally, the vertex count is<tbc>

\(n_k=N+k+1.\)

<tbc>For \(k\ge 1\), \(N\le n_k\le 2N\), while _k_=log<sub>2</sub>_N=O_(log_n<sub>k</sub>_). Substituting these comparisons into (8) gives

\(b(T_{k,2^k-k})=O\left(\frac{\sqrt{logn_k}}{n_k^2}\right),\)

completing theorem 1.2.

## 7 Computational checks

Computation played a supporting role in theorem discovery and verification, but not in the all-tree proof. Exact rational arithmetic was used in two independent ways on small trees: direct enumeration of every vertex permutation, and the first-vertex recurrence (1). These methods agree on every nonisomorphic tree through seven vertices. A broader exact census generated all 436 nonisomorphic trees on one through eleven vertices (matching OEIS A000055 \[8\]); among them, exactly _K_<sub>1</sub> and _K_<sub>2</sub> have zero bias.

For the tuned mixed-spider family, some exact values are shown in table 1. These are checks of the closed formulas, not inputs to their proof.

