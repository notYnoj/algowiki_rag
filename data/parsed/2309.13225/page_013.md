<tbc>have that there is some neighbor of _w_, say \(w^*=r(w,C_t)\in C_t\). Since \(\delta(u,v)\le C\), by the triangle inequality,

\(\delta(G_t,u,w^*)\le\delta(u,w)+1\le C+1\)

and similarly \(\delta(G_t,w^*,v)\le C+1\) so that both entries are finite in matrices _A,B_.

Then, computing the (min,+) product,<tbc>

\(\hat{\delta}_t(u,v)\le\delta(G_t,u,w^*)+\delta(G_t,w^*,v)\le\delta(u,w)+\delta(w,v)+2=\delta(u,v)+2\)

<tbc>Then, we immediately obtain,

\(\hat{\delta}(u,v)\le\delta(u,v)+2\le 2\delta(u,v)\)

## Time Complexity

_Proof._ We analyze the time complexity of our algorithm. _x,C_ are parameters that will be optimized.

### Phase 1

Fix some _t_=2_<sup>j</sup>_. We compute set _C<sub>t</sub>_ of size \(|C_t|=\tilde{O}(t)\) in time _O(m_)=_O(n_<sup>2</sup>) by Lemma 2.5. The graph _G<sub>t</sub>_ has at most \(\frac{2n^2}{t}\) edges, so execution of all |_C<sub>t</sub>_| **BFS** searches re quires \(\tilde{O}(n^2)\)-time. We can also upper bound _t_ as _t=O(n_<sup>1-_x_</sup>). Since _C=O_(1), computing the `boundedMinPlus`\((M_t,M_t^T,C+1)\) requires time \(Cn^{\omega(1,1-x,1)}\ge n^2\). Then, since there are at most log_n_ such _j_, Phase 1 requires overall time,

\(\tilde{O}\left(Cn^{\omega(1,1-x,1)}\right)\)

### Phase 2

In Phase 2, we call `BK2APASP` on the graph _G<sub>x</sub>_ which requires \(\tilde{O}(m\sqrt{n})=\tilde{O}(n^{1.5+x})\) expected time.

### Phase 3

In Phase 3, we call `denseAPASP` which requires time \(\tilde{O}(n^{2+2/(3C-2)})\). We can equivalently use `AdaptiveAPASP` from Section 5 but this will not affect the overall running time of our algorithm.

Then, balancing \(\omega(1,1-x,1)=1.5+x\), we choose _x_=0.53184039 \[Bra\], this leads to a time complexity of \(\tilde{O}(n^{2.03184039})\).

Then, we simply choose _C_ such that \(2+\frac{2}{3C-2}\le 2.03184039\), noting that _C_=22 suffices.

### Note.

Note that if we replace the `boundedMinPlus` computation by vanilla (min,+)-product, and set \(x=\frac{3}{4}\), then we get a combinatorial (randomized) algorithm matching \(\tilde{O}(n^{2.25})\) time bound obtained by Roditty \[Rod23\]. However, Roditty’s algorithm is deterministic. In the following Section 3.2, we give a deterministic algorithm that significantly improves upon Roditty’s bound.

## 3.2 A Deterministic (2,0)-Approximate APSP

We now move to our deterministic algorithm which gives a slightly weaker running time bound, but brings in many new ideas that will be useful in later sections. We prove the following theorem.

**Theorem 3.3.** _Let G be an undirected, unweighted graph with n vertices. Algorithm 3 deterministically computes a_ (2,0)_-approximate APSP solution in time_ \(\tilde{O}(n^{2.07203166})\).

