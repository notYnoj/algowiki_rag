<tbc>Hence \(N\le 2n\) and \(M\le 2m\). Apply Theorem 2.6. Input preparation costs at most 2(_n+m)d_<sup>6_k_</sup>. Since \(NM\le 4nm\), the capped count satisfies

\(B_t=\sum_{s=0}^t\genfrac(){pt}{2}{t}{s}6^smin\left\{w,\frac{NM}{k^s}\right\}\le 4\sum_{s=0}^t\genfrac(){pt}{2}{t}{s}6^smin\left\{w,\frac{nm}{k^s}\right\}.\)

The extra factor _O(t_) for reconstruction and request generation, and the cost of sorting and deduplicating requests, are absorbed by \(\widetilde{O}\).

If the input entries have absolute value at most \(L\ge 1\), each preparation or reconstruction step combines _O(k_) values. All intermediate values are therefore bounded by (6_k_)<sup>_O(t_)</sup>_L_<sup>2</sup>. Since _k_ is fixed, _t=O_(log_d_), and _L_ is polynomially bounded, these integers have _O_(log(_n+m_)) bits. This proves equation (2).

## 3 Applications to fine grained algorithms

Fine grained algorithms seek to improve the exponent in a problem’s running time. Here our goal is to go below quadratic time for integer 3SUM and below cubic time for APSP. We do this through a convenient intermediate problem, Offline Set Disjointness, which asks whether specified pairs of sets intersect.

This problem connects directly to our matrix multiplication algorithm: the product of two incidence matrices records the intersection sizes, and we only need the entries corresponding to the queried pairs. Known reductions then turn a faster algorithm for this intermediate problem into faster algorithms for 3SUM and APSP. We first give the set-disjointness algorithm, then apply these reductions.

### 3.1 Offline Set Disjointness

An instance of the _Offline Set Disjointness_ problem consists of two families \(S_1,\dots,S_n,T_1,\dots,T_n\subseteq[d]\) and a set \(W\subseteq[n]\times[n]\) of _w_ requested pairs. For each \((i,j)\in W\), we must determine whether \(S_i\cap T_j=\varnothing\).

**Lemma 3.1.** _There is an absolute integer_ \(K\ge 2\) _such that, whenever_ \(d^K\le n\) _and_ \(w\le n^2/\sqrt{d}\)_, Offline Set Disjointness can be solved deterministically in time_ \(\widetilde{O}(n^2/d^{1/8})\).

_Proof._ Take \(\tau=1/8\) in Theorem 1.1, and set \(K=\kappa(1/8)+1\). Form the incidence matrices \(X\in\{0,1\}^{n\times d}\) and \(Y\in\{0,1\}^{d\times n}\). Since \((XY)_{ij}=|S_i\cap T_j|\), it suffices to compute the entries indexed by _W_. The theorem gives running time

\(\widetilde{O}(nd^{K-1}+nd^{1/8}\sqrt{w})\le\widetilde{O}(n^2/d+n^2/d^{1/8})=\widetilde{O}(n^2/d^{1/8}).\)

Forming the incidence matrices and reading the queries costs _O(nd+w_), which is absorbed by this bound.

### 3.2 Known reductions

To identify the offline set disjointness problem with its graph formulation, use one vertex for each _S<sub>i</sub>_, one for each _T<sub>j</sub>_, and a middle vertex for each element of \[_d_\]. Join sets to their elements and add an outer edge for every requested pair. That edge lies in a triangle exactly when the two sets are not disjoint. This is the _Lopsided All-Edges Sparse Triangle_ formulation \[6, 1\], with a small middle part.<tbc>

