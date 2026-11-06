2. **_Precision:_** _Calculations are performed with a precision of L=O(T<sub>E</sub>_) _bits after the binary point to ensure the ellipsoid contains P._<tbc>

_3._ **_Running Time:_** _The total time complexity is_ \(O\left(T_E\cdot(d^2\cdot\mathcal{M}(L)+T_\mathrm{SEP})\right)\) _where_ M(_L_) _is the cost of arithmetic on L-bit numbers and T_<sub>SEP</sub> _is the oracle cost._

**Remark 3.2.** Assume that _P_ is guaranteed to be full-dimensional whenever it is non-empty. Furthermore, suppose the separation oracle is strengthened to report tight constraints for points on the boundary of _P_, rather than only reporting violated constraints (i.e., if \(x\in\partial P\), the oracle returns a defining hyperplane). Under these conditions, the Ellipsoid algorithm in Algorithm 3 returns a point in the _strict interior_ of _P_ or correctly asserts that _P_ is empty.

The final step before describing the dual ellipsoid algorithm is defining the polyhedron _P_ we will work with and an implementation of the strong separation oracle SEP_<sub>P</sub>_ using the Conic-Certification Oracle.

## 3.3 The Hyperplane Arrangement Induced by P

Given a point set \(\mathcal{P}=\{x_1,\dots,x_N\}\subseteq\mathbb{R}^d\), denote

\(H_{i,j}=\{w\in\mathbb{R}^d:\langle w,x_i\rangle\ge\langle w,x_j\rangle\},\text{and}h_{\{i,j\}}=\{w\in\mathbb{R}^d:\langle w,x_i-x_j\rangle=0\}.\) (2)

Notice that querying \(\mathrm{sign}(\langle w^*,x_i-x_j\rangle)\) is equivalent to checking whether \(w^*\in H_{i,j}\). The _hyperplane arrangement_ \(\mathcal{A}=\bigcup_{i,j\in[N]}h_{\{i,j\}}\) partitions R_<sup>d</sup>_ into _cells_, where each cell is a maximal connected region of R_<sup>d</sup>_ that does not share any interior points with any hyperplane in A. It follows that these cells are convex polyhedra with facets defined by a subset of hyperplanes from the arrangement.

**Definition 3.3.** For each permutation \(\pi\in S_N\), define

\(C_\pi=\{w\in\mathbb{R}^d:\langle w,x_{\pi(1)}\rangle\le\langle w,x_{\pi(2)}\rangle\le\cdots\le\langle w,x_{\pi(N)}\rangle\}\) (3)

\(=\cap_{1\le i\le N-1}H_{\pi(i+1),\pi(i)}.\) (4)

Similarly, for any partial order \(\sigma\) on the set of indices \[_N_\], define

\(C_\sigma=\{w\in\mathbb{R}^d:\langle w,x_i\rangle\le\langle w,x_j\rangle\text{for all}i\unknown_\sigma j\}.\) (5)

**Lemma 3.4.** _The following statements are true:_

1. _Any full dimensional_ \(C_\pi\) _is a cell of the arrangement_ A_. Moreover, every cell of_ A _is a full dimensional set of the form_ \(C_\pi\) _for some_ \(\pi\in S_N\).<tbc>

_2._ _For any partial order_ \(\sigma\)_, the set_ \(C_\sigma\) _is a convex polyhedron. Furthermore,_ \(C_\sigma=\bigcup_{\pi\in\mathcal{L}(\sigma)}C_\pi\)_, where_ \(\mathcal{L}(\sigma)\) _denotes the set of linear extensions of_ \(\sigma\) _(permutations consistent with_ \(\sigma\)_)._

We defer the proof to Section B. Define \(\sigma^*\) to be the partial order on \[_N_\] determined by the strict inequalities of _w_<sup>∗</sup>, such that \(i\unknown_{\sigma^*}j\) if and only if \(\langle w^*,x_j-x_i\rangle>0\).

**Lemma 3.5.** _The weight vector w_<sup>∗</sup> _lies in the interior of_ \(C_{\sigma^*}\)_. Furthermore, for any_ \(\widehat{w}\in\mathrm{int}(C_{\sigma^*})\)_, the implication_

\(\langle\widehat{w},x_i-x_j\rangle\le 0\Longrightarrow\langle w^*,x_i-x_j\rangle\le 0\)

_holds for all_ \(i,j\in[N]\).

