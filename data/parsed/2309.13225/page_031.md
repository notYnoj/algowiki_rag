First, note \(\delta(u,v)\le\hat{\delta}(u,v)\) for all _u,v_ as `DominatingSetAPASP` returns \(\hat{\delta}(u,v)\ge\delta(G_i,u,v)\ge\delta(u,v)\) by Lemma C.1. In Phase 2, every edge weight in _G<sub>j,w</sub>_ is the length of some path previously found in the original graph _G_. Finally, `BK2APASP` and `DenseAPASP` return estimates \(\hat{\delta}(u,v)\ge\delta(u,v)\).

Now, we only need to show \(\hat{\delta}(u,v)\le 2\delta(u,v)\) If \(P\subset E_{l_0+1}\), this immediately follows from the correctness of `BK2APASP`. If \(\delta(u,v)\ge M\), then we have correctness by `DenseAPASP`, since,

\(\hat{\delta}(u,v)\le\delta(u,v)+M\le 2\delta(u,v)\)

Therefore, assume \(P\unknown\subset E_{l_0+1}\) and \(\delta(u,v)\le M\). Without loss of generality, suppose \(\ell(v)\le\ell(u)\). Recall from Lemma A.2 the blocking vertices _B(P_)={_x_<sub>0</sub>_,x_<sub>1</sub>_,...,x<sub>t</sub>_} and levels _L<sub>B</sub>(P_) of path _P_.

Let \(a=min_{\ell(x_i)\le l-\frac{l_0}{2}+1}i\) be the minimum index of an element in the blocking set such that \(\ell(x_i)\le l-\frac{l_0}{2}+1\). Since \(l\ge\ell(x_1)>\ell(x_2)>\dots>\ell(x_t)\ge 1\), we can upper bound,

\(a\le l-\left(l-\frac{l_0}{2}+1\right)=\frac{l_0}{2}-1=\frac{k}{2}-2\)

Since _P_ is not contained in _E_<sub>_l_<sub>0</sub>+1</sub>, we can assume _a_ exists and \(a\ge 1\).

Let \(x_a\in B(P)\) be the corresponding vertex in _B(P_). Since _P_ has an edge not in _E_<sub>_l_<sub>0</sub>+1</sub>, the last blocking vertex of minimum level must have \(\ell(x_t)\le l_0\). Recall that we denote \(v^*=r\left(v,D_{\ell(v)}\right)\) for any vertex _v_.

Let \(\frac{n}{2^{i^*}}\le deg(x_t)<\frac{n}{2^{i^*-1}}\) and \(x_t^*=r(x_t,C_{i^*})\). Since \(P\subset F_{i^*}\), the _i_<sup>∗</sup>-th invocation of `DominatingSetAPASP` computes

\(\hat{\delta}_{i^*}(x_t^*,x_a^*)\le\delta(x_t,x_a)+2\le M+2\)<br>
\(\hat{\delta}_{i^*}(x_t^*,x_{a+1}^*)\le\delta(x_t,x_{a+1})+2\le M+2\)

These entries are finite in the matrices _A_<sub>_i_<sup>∗</sup></sub>_,B_<sub>_i_<sup>∗</sup></sub> constructed by `DominatingSetAPASP`.

Note that \(x_t\in P_{x_a,x_{a+1}}\) (Lemma A.1). Furthermore, \(\ell(x_a)\le l-\frac{l_0}{2}+1\) implies \(x_a^*\in D_{l-\frac{l_0}{2}+1}\) and \(\ell(x_{a+1})<\ell(x_a)\) implies \(x_{a+1}^*\in D_{l-\frac{l_0}{2}}\). Then, the bounded (min,+) product computes,

\(\hat{\delta}_{i^*}(x_a^*,x_{a+1}^*)\le\hat{\delta}_{i^*}(x_a^*,x_t^*)+\hat{\delta}_{i^*}(x_t^*,x_{a+1}^*)\)<br>
\(\le\delta(x_a,x_t)+\delta(x_t,x_{a+1})+4\)<br>
\(\le\delta(x_a,x_{a+1})+4\)

Then, in the \(\ell(x_a)\)-th iteration, we can take the edge sequence \((x_a^*,x_{a+1}^*,x_{a+1})\) and the remaining edges in \(E_{\ell(x_a)}\) to compute a distance estimate at most,

\(\hat{\delta}(x_a^*,x_{a-1}^*)\le\hat{\delta}_{i^*}(x_a^*,x_{a+1}^*)+1+\delta(x_{a+1},x_{a-1})\le\delta(x_a,x_{a-1})+5\)

The remaining proof follows exactly as in Theorem 4.1.

## Time Complexity

_Proof._ We set \(l_0\leftarrow k-2\) and leave _x,l,M_ to be optimized. Phase 0 requires \(\tilde{O}(ln^2)\) time overall as we only invoke `Decompose`. Invoking `Dijkstra` requires \(\tilde{O}(n^{2+\frac{x}{l-l_0}})\) time as \(|D_j|=\tilde{O}(n/s_j)\) and \(|E_j|\le O(ns_{j-1})\). `BK2APASP` requires \(\tilde{O}(m\sqrt{n})=\tilde{O}(n^{1.5}s_{l_0})=\tilde{O}(n^{1.5+x})\) time as we call `BK2APASP` on graph _G_<sub>_l_<sub>0</sub>+1</sub>, a graph with maximum degree _s_<sub>_l_<sub>0</sub></sub>=_n<sup>x</sup>_.

