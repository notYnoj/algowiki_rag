The main outstanding question is whether it is possible to sort in _O<sub>k</sub>(n_) time, and in particular, whether the Greedy- or SmoothHeap-based algorithms of \[CGK<sup>+</sup>15b, KS20\] already sort in time _O<sub>k</sub>(n_). It would also be interesting to give a non-trivial upper bound on the complexity of BST Sort with a Splay Tree \[ST85\], or Heap Sort with a Pairing Heap \[FSST86\].

## 1.1 New Results

### 1.1.1 Upper Bounds

Our main result is a new upper bound on the extremal function of \(P_\pi\otimes(\bullet)\)-type matrices that has a much weaker dependence on _k_, which immediately gives better upper bounds on the complexity of sorting \(\pi\)-free sequences via \[CGK<sup>+</sup>15b, KS20\].

**Theorem 1.3.** _Let_ \(P_\pi\) _be the_ \(k\times k\) _permutation matrix of_ \(\pi\) _and_ \(Q=P_\pi\otimes(\bullet)\) _be a_ \(2k\times 3k\) _light matrix. Then_

\(\mathrm{Ex}(Q,n)\le n\cdot\left(2^{O(k^2)}+O(\alpha(n))^{3k-2}\right)2^{\alpha(n)}=n\cdot 2^{O(k^2)+(1+o(1))\alpha(n)}.\)

**Corollary 1.4.** _If S is_ \(\pi\)_-free, then BST Sort using_ GreedyFuture _and Heap Sort using the_ SmoothHeap _will sort S in_ \(n\cdot 2^{O(k^2)+(1+o(1))\alpha(n)}\) _time._

One can view Corollary 1.4 as improving on the \(n2^{\alpha(n)^{3k/2-O(1)}}\) bound of (1) in two ways. It is an asymptotic improvement in _n_ as it brings the exponent of \(\alpha(n)\) from 3_k/_2-_O_(1) down to 1. However, even if one is tempted to consider \(\alpha(n)\) to be a small constant, it also reduces the dependency on _k_ from _doubly_ exponential to merely _singly_ exponential.

It is possible to improve the factor \(2^{\alpha(n)}\) for a specific product pattern. For example,

**Theorem 1.5.** _If I<sub>k</sub> is the_ \(k\times k\) _identity matrix, then_

\(\mathrm{Ex}(I_k\otimes(\bullet),n)\le 2(k-1)n\alpha(n)+O(kn).\)

### 1.1.2 Lower Bounds

When \(k\ge 2\), all \(Q=P_\pi\otimes(\bullet)\) patterns contain \(\genfrac(){pt}{2}{\bullet}{\bullet}\) or its reflection, which is known to have extremal function \(\mathrm{Ex}(\genfrac(){pt}{2}{\bullet}{\bullet},n)=2n\alpha(n)\pm O(n)\) \[HS86, FH92, Niv10, Pet15a\].

We prove that \(\mathrm{Ex}(P_\pi\otimes(\bullet),n)=\Omega(n2^{\alpha(n)})\) whenever \(\pi\) contains (3,1,2) or (2,1,3), or equivalently, when \(P_\pi\) contains \(\genfrac(){pt}{2}{\bullet}{\bullet}\cdot\) or \(\genfrac(){pt}{2}{\bullet}{\bullet}\cdot\). Thus, Theorem 1.6 implies that the general upper bound of Theorem 1.3 can only be improved in the \(\mathrm{poly}(\alpha(n))\) factor.

**Theorem 1.6.** \(\mathrm{Ex}(W,n)=\Theta(n2^{\alpha(n)})\)_, where_<tbc>

\(W=\left(\begin{array}{ c c c }
\bullet &  &  \\
 &  &  \\
 &  & \bullet \\
 & \bullet &  \\
 &  & \bullet
\end{array}\right).\)

