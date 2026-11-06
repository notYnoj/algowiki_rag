**Theorem 3.7.** _Let M_<sub>1</sub>=(_E,_I<sub>1</sub>) _and M_<sub>2</sub>=(_E,_I<sub>2</sub>) _be two linear matroids each of rank r on a ground set E of size m, with weight function_ \(wt:E\rightarrow[-W,W]\)_. Let E<sub>Q</sub> be a susceptible set of size_ \(\sigma\)_, and suppose M_<sub>1</sub> _and M_<sub>2</sub> _extend to linear matroids of (same) rank r on_ \(E_0:=E\cup E_Q\) _with_ \(r\times|E_0|\) _representation matrices_ \(\bar{A}_1\) _and_ \(\bar{A}_2\) _over_ F_. Then, for any_ \(k\ge 1\)_, there exist the following subset sensitivity oracles that, for any f updates confined to E<sub>Q</sub>, answer k-packing queries:_

1. **_Decision Oracle:_** _Decides if a k-packing exists. This oracle requires_ \(O(k^2(m+\sigma)+\sigma^2(kr)^{\omega-2}+(kr)^\omega)\) _preprocessing time,_ \(O(\sigma^2)\) _space, and answers queries in_ \(O(f^\omega)\) _time._<tbc>

_2._ **_Weighted Oracle:_** _Returns the exact minimum weight of a k-packing. This oracle requires_ \(\widetilde{O}(k^2(m+\sigma)+W\sigma^2(kr)^{\omega-1}+W(kr)^{\omega+1})\) _preprocessing time,_ \(\widetilde{O}(W\cdot kr\cdot\sigma^2)\) _space, and answers queries in_ \(\widetilde{O}(W\cdot kr\cdot f^\omega)\) _time._

_Proof._ Let \(\bar{U}_1,\bar{U}_2\in\mathbb{F}^{kr\times|E_0|}\) be the _k_-fold union representation matrices for the extensions of _M_<sub>1</sub> and _M_<sub>2</sub> to _E_<sub>0</sub>, constructed via Theorem 3.2 from \(\bar{A}_1\) and \(\bar{A}_2\). Let \(D\in\mathbb{F}_{2W}[Y]^{|E_0|\times|E_0|}\) be the diagonal weight matrix with \(D_{e,e}=x_eY^{W+wt(e)}\) for \(e\in E_0\), so that the Packing Laplacian is \(\mathcal{L}_\mathrm{pack}=\bar{U}_1D\bar{U}_2^T\). Computing L<sub>pack</sub> takes \(O(k^2(m+\sigma))\) time, since \(|E_0|=m+\sigma\) and each element contributes _O(k_<sup>2</sup>) entries to the Laplacian.

Since all queries modify only diagonal entries indexed by _E<sub>Q</sub>_, we invoke Theorem A.1 with \(A:=\bar{U}_1\), \(B:=\bar{U}_2\), the diagonal matrix _D_, and susceptible set _Q_:=_E<sub>Q</sub>_ of size \(\sigma\).

## Decision Oracle.

We apply the scalar formulation of Theorem A.1 with _d_:=0, working with L<sub>pack</sub>|<sub>_Y_=1</sub>. Substituting _r_:=_kr_ and \(\sigma=|E_Q|\) into Theorem A.1, the data structure construction takes \(O(\sigma^2(kr)^{\omega-2}+(kr)^\omega)\) time and \(O(\sigma^2)\) space. Combined with the \(O(k^2(m+\sigma))\) cost of computing L<sub>pack</sub>, the total preprocessing time is \(O(k^2(m+\sigma)+\sigma^2(kr)^{\omega-2}+(kr)^\omega)\). Each query takes \(O(f^\omega)\) time. By Theorem 3.4, the determinant is non-zero if and only if a valid _k_-packing exists.

## Weighted Oracle.

We apply the polynomial formulation of Theorem A.1 with _d_:=2_W_. Substituting _r_:=_kr_ into Theorem A.1, the data structure construction takes \(\widetilde{O}(W\sigma^2(kr)^{\omega-1}+W(kr)^{\omega+1})\) time and \(\widetilde{O}(W\cdot kr\cdot\sigma^2)\) space. Combined with the Laplacian computation, the total preprocessing time is \(\widetilde{O}(k^2(m+\sigma)+W\sigma^2(kr)^{\omega-1}+W(kr)^{\omega+1})\). Each query takes \(\widetilde{O}(W\cdot kr\cdot f^\omega)\) time. The minimum weight is extracted as the smallest exponent of _Y_ with a non-zero coefficient, minus _krW_. □

**Remark 3.8** (Comparison of Oracle Models)**.** _The general and subset sensitivity oracles for matroid packing offer complementary trade-offs:_

_The subset sensitivity oracle achieves query time independent of k, at the cost of space scaling with the susceptible set size_ \(\sigma\) _rather than the matroid rank. When_ \(\sigma\checkmark m\) _and k is large relative to f, the subset sensitivity model provides both smaller space and faster queries. When_ \(\sigma\) _is comparable to m, the general sensitivity oracle is more space-efficient._

\begin{tabular}{ccc}
 & **_General Sensitivity_** & **_Subset Sensitivity_** \\
 & _(Theorem 3.5)_ & _(Theorem 3.7)_ \\
_Space (decision)_ & _O_((_kr_)<sup>2</sup>log_k_) & \(O(\sigma^2)\) \\
_Query (decision)_ & \(O((k^2\delta)^\omega)\) & \(O(f^\omega)\) \\
\end{tabular}

