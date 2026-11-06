### Phase 2

In Phase 2, we have a graph _G<sub>x</sub>_ of maximum degree _n<sup>x</sup>_ and therefore \(m\le n^{1+x}\). From Lemma 2.6, the execution of `Decompose` requires _O(m_)=_O(n_<sup>1+_x_</sup>) time.

In Phase 2.1, we can upper bound \(|D_1|=\tilde{O}(n^{1-\frac{(k-1)}{k}x})\) by Lemma 2.6. Likewise, \(|D_{k-1}|=\tilde{O}(n^{1-\frac{x}{k}})\). Executing `BFS` on graph _G_<sub>_s_<sub>1</sub></sub> with _O(n_<sup>1+_x_</sup>) edges from each \(w\in D_1\) requires \(\tilde{O}(n^{2+\frac{x}{k}})\) time.

Now, computing the (min,+) product of _A,B_ requires time,

\(\tilde{O}\left(n^{\omega\left(1,1-\frac{k-1}{k}x,1-\frac{x}{k}\right)}\right)=\tilde{O}\left(n^{\omega(1,1-x,1)}\right)\)

by Proposition C.3.

In Phase 2.2, computing Line 30 requires time _O(n_<sup>2_x_</sup>) while computing Line 31 requires time \(O\left(n^{\frac{3k-4}{k}x}\right)\). Overall, Phase 2.2 requires time,

\(O\left(n^{1+2x}+n^{1+\frac{3k-4}{k}x}\right)\)

Finally, we turn our attention to Phase 2.3. Fix some iteration _i_. Since the sets _q(w,D<sub>i</sub>_) are disjoint, \(\sum_{w\in D_i}|q(w,D_i)|\le n\) so that Line 36 requires time _O(n_<sup>2</sup>) over all \(w\in D_i\). We bound \(|D_i|\le\tilde{O}(n^{1-\frac{k-i}{k}x})\) by Lemma 2.6. Each invocation of `Dijkstra` requires time \(|E_i|=O(n^{1+\frac{k-i+1}{k}x})\) so that across all \(w\in D_i\), all invocations of `Dijkstra` can be completed in time \(\tilde{O}(n^{2+\frac{x}{k}})\).

We ignore Phase 3 for now as we will find that it is not the computational bottleneck. Phases 1 and 2 require time,

\(\tilde{O}\left(n^{\omega(1,1-x,1)}+n^{1+2x}+n^{1+\frac{3k-4}{k}x}+n^{2+\frac{x}{k}}\right)\)

Using \[Bra\], we choose _x_=0.4414248 and _k_=7 to obtain the time complexity \(\tilde{O}(n^{2.07203166})\) for Phase 1 and 2. Finally, we conclude the proof by noting that `boundedAdaptiveAPASP`(_G,_6_,C_) requires time \(\tilde{O}(n^{2.05794292})\) by Corollary 5.14 and `DenseAPASP`(_G,C_) requires time \(\tilde{O}(n^{35/17})=\tilde{O}(n^{2.0589})\) by Lemma 3.2.

## 4 (2,0)-Multiplicative Approximations for Long Paths

In this section, we present algorithms for computing (2,0) approximations for paths of at least some length. We begin with a combinatorial result that gives a (2,0) multiplicative approximation for paths of length at least _k_ for even values of \(k\ge 4\).

### 4.1 Multiplicative Approximation for Long Paths

**Theorem 4.1.** _Let_ \(k\ge 4\) _be an even integer. Algorithm 4 computes a_ (2,0) _approximation for all paths of length_ \(\delta(u,v)\ge k\) _in expected time_ \(\tilde{O}\left(n^{2+\frac{1}{2(k-1)}}\right)\).

In Appendix E, we improve the above bound for _k_=4 and 5.

### High Level Overview

As a simple example, we begin with by showing that we can obtain a (2,0) approximation for \(\delta(u,v)\ge 4\) in time \(\tilde{O}(n^{13/6})\). Decompose the graph with degree thresholds _s_<sub>1</sub>=_n_<sup>5/6</sup>_,s_<sub>2</sub>=_n_<sup>4/6</sup>_,...,s_<sub>5</sub>=_n_<sup>1/6</sup>. Let _P_ be a shortest path of length at least 4. If \(P\subset E_3\), then we execute `BK2APASP`(_G_<sub>3</sub>) in time _n_<sup>13/6</sup> where _G_<sub>3</sub>=(_V,E_<sub>3</sub>) has maximum degree _s_<sub>2</sub>=_n_<sup>4/6</sup>. Otherwise, \(P\unknown\subset E_3\) and vertex \(w\in P\) of maximum degree has \(deg(w)\ge s_2\) and is dominated by<tbc>

