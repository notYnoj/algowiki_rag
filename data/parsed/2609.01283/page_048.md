diagonal entry in the selection matrix _D_. Furthermore, the data structure dynamically toggles at most _f_ auxiliary random columns in _R<sub>switch</sub>_ to maintain a perfectly square active submatrix.

Thus, the total number of toggled diagonal entries is at most 2_f_. Substituting the matroid rank _r=n_-1 and the susceptible set size \(\sigma\) into the bounds of Theorem 3.11 yields the result. The space complexity relies strictly on the susceptible set, \(O(\sigma^2)\), and the query time is fully decoupled from the graph size and the parameter _k_, taking exactly \(O(f^\omega)\) operations. \(\square\)

## 8.3 Subset Sensitivity for Matroid Parity

Recall from Section 6 that enumerating or finding the minimum-weight parity basis of a linear matroid of rank _r_ with _m_ pairs reduces to maintaining the determinant (or Pfaffian) of the \(r\times r\) skew-symmetric Linear Matroid Parity (LMP) matrix:

\(\mathcal{M}_{LMP}:=ADB^T-BDA^T,\)

where \(A,B\in\mathbb{F}^{r\times m}\) represent the static coordinate vectors of the pairs, and \(D\in\mathbb{F}(x)[Y]^{m\times m}\) is the diagonal matrix encoding pair weights and formal variables.

To maintain det(M_<sub>LMP</sub>_) in the sensitivity setting using our framework (Theorem A.1), we fac torize it into the standard form \(\hat{U}D_{ext}\hat{V}^T\). We define two augmented representation matrices:<tbc>

\(\hat{U}:=[A|B]\in\mathbb{F}^{r\times 2m}\text{and}\hat{V}:=[B|-A]\in\mathbb{F}^{r\times 2m}.\)

<tbc>Let _D<sub>ext</sub>_ be the \(2m\times 2m\) block-diagonal matrix constructed by duplicating _D_:<tbc>

\(D_{ext}:=\left(\begin{array}{ c c }
D & 0 \\
0 & D
\end{array}\right).\)

<tbc>The _Parity Laplacian_ is defined as follows and is equivalent to the LMP matrix:

\(\mathcal{L}_{parity}:=\hat{U}D_{ext}\hat{V}^T=ADB^T-BDA^T=\mathcal{M}_{LMP}.\)

This block-matrix factorization allows us to directly apply our subset sensitivity determinant data structures.

Suppose the representations of the pairs or their weights undergo an update set _U_ of size _f_. An update to pair _i_ modifies exactly two diagonal entries in _D<sub>ext</sub>_ (at indices _i_ and _i+m_). Therefore, applying _f_ pair updates translates to modifying at most 2_f_ diagonal entries in _D<sub>ext</sub>_.

**Theorem 8.11** (Matroid Parity Subset Sensitivity Oracle)**.** _Let_ \(E_Q\subseteq E\) _be a susceptible set of_ \(\sigma\) _pairs. There exist randomized subset sensitivity oracles that, given f updates confined to pairs in E<sub>Q</sub>, answer parity basis queries with high probability:_

1. **_Decision Oracle:_** _Requires_ \(O(\sigma^2r^{\omega-2}+r^\omega)\) _preprocessing time,_ \(O(\sigma^2)\) _space, and answers queries in_ \(O(f^\omega)\) _time._<tbc>

_2._ **_Weighted Oracle:_** _Requires_ \(\widetilde{O}(W\sigma^2r^{\omega-1}+Wr^{\omega+1})\) _preprocessing time,_ \(\widetilde{O}(Wr\sigma^2)\) _space, and answers queries in_ \(\widetilde{O}(Wrf^\omega)\) _time._

_Proof._ We invoke Theorem A.1 on the factorization \(\hat{U}D_{ext}\hat{V}^T\). The matrix _D<sub>ext</sub>_ has dimension \(2m\times 2m\). The designated susceptible set corresponds to the \(2\sigma\) diagonal entries representing the pairs in _E<sub>Q</sub>_. Modifying _f_ pairs toggles at most 2_f_ diagonal entries within this susceptible set. Substituting the susceptible size \(2\sigma\) and update size 2_f_ directly into the bounds of Theorem A.1 completes the proof, reducing the space complexity to \(O(\sigma^2)\). \(\square\)

