## 7.2.1 Warm Up: The _k_-Bounded Case

From Theorem 7.2 and Theorem 6.2, the following result is immediate:

**Theorem 7.3.** _Let G_=(_V,E,**c**_) _be an undirected graph with integer edge costs in_ \[-_W,W_\] _and degree bounds_ \(\alpha\le k\)_. Then there exist the following sensitivity oracles that, for any update set U with f_=|_U|, answer queries on G+U with high probability:_

_Proof. Existence._ We preprocess _M_|<sub>_Y_=1</sub> with Theorem A.2 in the scalar case (_d_=0). Since \(N\le nk\), this requires \(O((kn)^\omega)\) processing time. For a query set _U_, _C_ has \(\delta=O(fk^2)\) non-zero entries. By applying Theorem A.2 to compute the determinant of \(M'=M+C\), the query time is \(O(\delta^\omega)=O(f^\omega k^{2\omega})\).

_Min-cost._ We apply Theorem A.2 to the polynomial matrix _M_ with _d=O(W_). The query \(M'=M+C\) involves computing the polynomial determinant via Theorem A.2, which takes \(\widetilde{O}(dN\delta^\omega)\) operations. Substituting _d=O(W_), \(N\le nk\), and \(\delta=O(fk^2)\), we obtain:

\(\widetilde{O}\big(W\cdot(kn)\cdot(fk^2)^\omega\big)=\widetilde{O}(Wnf^\omega k^{2\omega+1}).\)

Extracting the minimal exponent as in Theorem 6.2 yields the weight. \(\square\)

## 7.2.2 Arbitrary Degree Bounds via Auxiliary Graphs

We now drop the assumption \(\alpha\le k\). A direct expansion into \(\alpha(v)\) copies would yield a Tutte matrix of dimension \(O(nmax_v\alpha(v))\), which may be prohibitively large. Instead, we will fix a precomputed min-cost \(\alpha\)-factor _M_ of _G_ (we assume such an \(\alpha\)-factor exists in _G_, this assumption is justified as ideas of Section A.4 can be used to augment _G_ such that it always admits an \(\alpha\)-factor) and build an _auxiliary graph H_ that captures the symmetric difference \(M\triangle M'\) between _M_ and an updated \(\alpha\)-factor \(M'\) of _G+U_.

For this, we first introduce some definitions. A trail T is called a closed trail if T starts and ends at the same vertex. A sub-trail \(\mathcal{T}'\) of T is a trail which uses only the edges of T , with no repetitions. Note that \(\mathcal{T}'\) need not have the same order of walk as T , just that all the edges used by \(\mathcal{T}'\) should lie in T . We now define the notion of closed alternating trails. A closed alternating trail \(\mathcal{T}=(e_1,e_2,\dots,e_{2k})\), \(k\in\mathbb{N}\) is defined as a closed trail of even length such that if \(e_i\in M\), then \(e_{i+1}\in M'\) (and vice versa). It can also be seen that \(e_1\in M\Longleftrightarrow e_{2k}\in M'\). Since every vertex has both _M_-degree and \(M'\)-degree equal to \(\alpha(v)\), the following observation is immediate.

**Observation 7.4.** _The edge set_ \(M\triangle M'\) _decomposes into edge-disjoint closed alternating trails._

The following lemma proves that for any update set _U_, there exists an \(\alpha\)-factor \(M'\) in _G+U_ such that the number of closed alternating trails in \(M\triangle M'\) is bounded by at most |_U_|.

**Lemma 7.5.** _If G+U admits an_ \(\alpha\)_-factor, then it admits a min-cost_ \(\alpha\)_-factor_ \(M'\) _such that_ \(D:=M\triangle M'\) _contains no closed alternating trail_ T _all of whose edges belong to both G and G+U._

_Proof._ Among all min-cost \(\alpha\)-factors of _G+U_, choose \(M'\) minimizing \(|M\triangle M'|\). By Theorem 7.4, _D_ decomposes into edge-disjoint closed alternating trails. Suppose _D_ contains an alternating trail T<tbc>

\begin{tabular}{ccccc}
_Oracle_ & _Prep._ & _Space_ & _Query_ & _Output_ \\
_Existence_ & \(O((kn)^\omega)\) & _O_((_kn_)<sup>2</sup>log_n_) & \(O(f^\omega k^{2\omega})\) & _Whether G+U has an_ \(\alpha\)_-factor_ \\
_Min-Cost_ & \(\widetilde{O}(W(kn)^3)\) & _O(W(kn_)<sup>3</sup>log_n_) & \(\widetilde{O}(Wnf^\omega k^{2\omega+1})\) & _Weight of a min-cost_ \(\alpha\)_-factor of G+U_ \\
\end{tabular}

