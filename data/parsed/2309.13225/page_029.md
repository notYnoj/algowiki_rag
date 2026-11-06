## Algorithm

Algorithm 4 and Algorithm 5 are similar overall, so we only highlight the differences here. In Phase 1, we use a bounded (min,+) product to replace the edge sets \(D_{j_1}\times D_{j_2}\).

In Line 61, we decompose the graph _G_ into (1-_x_)log_n_ degree thresholds and at each threshold invoke `dominatingSetAPASP` to compute approximate distances between \(D_{l-\frac{l_0}{2}}\) and \(D_{l-\frac{l_0}{2}+1}\) in Line 63. In Phase 2, for each level \(j\ge l_0+1\), we execute `Dijkstra` from each vertex \(w\in D_j\) on the graph \(G_{j,w}=(V,E_j\cup E^*\cup(w\times V))\) in Line 68.

Finally, we take the minimum of our estimate with the estimate produced by `BK2APASP` and `DenseAPASP`.

## Analysis

We briefly argue that Algorithm 5 equipped with fast matrix multiplication should outperform the combinatorial Algorithm 4. Indeed, suppose we use naive matrix multiplication, so that the largest matrix multiplication contains matrices of size \(D_{l-\frac{l_0}{2}}\times D_{l_0}\) and \(D_{l_0}\times D_{l-\frac{l_0}{2}+1}\) which requires time,

\(\tilde{O}\left(\frac{n^3}{s_{l_0}s_{l-\frac{l_0}{2}}s_{l-\frac{l_0}{2}+1}}\right)=\tilde{O}\left(n^{3-\left(1+\frac{l_0}{2(l-l_0))}+\frac{l_0-2}{2(l-l_0}\right)x}\right)\)<br>
\(=\tilde{O}\left(n^{3-\left(\frac{2l-2}{2(l-l_0)}\right)x}\right)\)

Balancing the running times,

\(3-\frac{l-1}{l-l_0}x=2+\frac{x}{l-l_0}\)

we obtain,

\(x=\frac{l-l_0}{l}\)

so that the overall running time is \(2+\frac{1}{l}\), which matches the combinatorial algorithm Algorithm 4.

### Warm-Up: _k_=4

We begin by showing that we can obtain a (2,0) approximation for \(\delta(u,v)\ge 4\) in time \(\tilde{O}(n^{2.01973523})\).

_Proof._ Using \[Bra\], we set parameters _x_=0.51973523 and _l_=29 so that _l_<sub>0</sub>=2. Choosing _M_=35 suffices to ensure `DenseAPASP` requires time \(\tilde{O}\left(n^{2.0195}\right)\) (Lemma 3.2).

Decompose the graph with degree thresholds _s_<sub>2</sub>=_n<sup>x</sup>,s_<sub>3</sub>=_n_<sup>26_x/_27</sup>_,...,s_<sub>28</sub>=_n_<sup>_x/_27</sup>. Let _P_ be a shortest path of length at least 4. If \(P\subset E_3\), then we execute `BK2APASP`(_G_<sub>3</sub>) in time _n_<sup>1.5+_x_</sup>=_n_<sup>2.01973523</sup> where _G_<sub>3</sub>=(_V,E_<sub>3</sub>) has maximum degree _s_<sub>2</sub>=_n<sup>x</sup>_. If \(\delta(u,v)\ge M\), then `DenseAPASP` computes a +_M_ approximation and we obtain a (2,0) approximation.

Then, assume \(P\unknown\subset E_3\) is of length at most _M_ and vertex \(w\in P\) of maximum degree has \(deg(w)\ge s_2\). Suppose \(deg(v)\ge deg(u)\). Let _z=b(v,P_) be the blocking vertex so \(deg(z)\ge s_{28}\) and \(z^*=r(z,D_{\ell(z)})\in D_{28}\). If _z=w_, we obtain a +4 approximation as in Algorithm 4.

Assume \(z\neq w\). Let \(\frac{n}{2^i}\le deg(w)\le\frac{n}{2^{i-1}}\). Since \(P\subset F_i\), we obtain the estimates,

\(\hat{\delta}(w^*,z^*)\le\delta(w,z)+2\le M+2\)<br>
\(\hat{\delta}(w^*,v)\le\delta(w,v)+1\le M+1\)

Then, the bounded (min,+) product computes,

\(\hat{\delta}(v,z^*)\le\delta(v,z)+3\)

