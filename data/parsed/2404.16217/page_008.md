## 8 Fault-Tolerant Bounded Flow Preservers

**3.** For every node \(y\in V\backslash\{s,t\}\) if _x_<sub>1</sub>_,...,x<sub>p</sub>_ are in-neighbours of _y_ in G and _z_<sub>1</sub>_,...,z<sub>q</sub>_ are out-neighbours of _y_ in G, then we replace vertex _y_ (in current H) by _p_ binary trees as follows. First we remove node _y_ from H. Next for each \(x_i\in\mathrm{in}(y,\mathcal{G})\) insert a binary tree _B<sub>x<sub>i</sub>,y</sub>_ to H (along with new internal nodes and edges) whose root is _r<sub>x<sub>i</sub>,y</sub>_ and leaves are \(\ell_{y,z_1},\dots,\ell_{y,z_q}\).

Notice that H has _O(mn_) edges and vertices. Indeed for every vertex _v_ (other than _s_ and _t_) in G, |in(_v,_G)| binary trees have been added to H, each of size _O_(|out(_v,G_)|). So the number of edges and vertices in the transformed graph is \(O(\sum_{v\in V}|\mathrm{in}(v,G)|\cdot|\mathrm{out}(v,\mathcal{G})|))=O(mn)\). Also, observe that the out-degree of each vertex in H other than _s_ bounded by two.

\(\blacktriangleright\) **Lemma 15.** _max-flow(s,t,_G)=_max-flow(s,t,_H)

**Proof.** We will show that each _s_ to _t_ path in G now corresponds to a unique _s_ to _t_ path in H. Suppose there exists a path (_s=u_<sub>0</sub>_,u_<sub>1</sub>_,u_<sub>2</sub>_,...,u<sub>k</sub>=t_) in G. Then we will have an equivalent path in H as

\((s,\ell_{u_0,u_1},r_{u_0,u_1})\circ\mathrm{path}(r_{u_0,u_1},\ell_{u_1,u_2},B_{u_0,u_1})\circ(\ell_{u_1,u_2},r_{u_1,u_2})\circ\ell\cdots\circ\)<br> \(\mathrm{path}(r_{u_{k-2},u_{k-1}},\ell_{u_{k-1},u_k},B_{u_{k-1},u_k})\circ\ell_{u_{k-1},u_k},r_{u_{k-1},u_k})\circ(r_{u_{k-1},u_k},t)\)

where \(\mathrm{path}(r,\ell,B)\) denotes the path from _r_ to \(\ell\) using edges in binary tree _B_. Therefore, the (_s,t_)-max-flow values in graphs G and H are identical. \(\blacktriangleleft\)

We will now justify the significance of our transformation by providing a way to construct a (_k+f_-1)-FTRS of G if we know a (_k+f_-1)-FTRS for H such that the in-degree of _t_ in both the FTRSs is identical.

\(\blacktriangleright\) **Lemma 16.** _A_ (_k+f_-1)_-FTRS for_ G _can be constructed by knowing a_ (_k+f_-1)_-FTRS of_ H_, that preserves the in-degree of node t._

**Proof.** Let H<sup>∗</sup> be a (_k+f_-1)-FTRS of H. We want to construct G<sup>∗</sup>, a (_k+f_-1)-FTRS for G satisfying the condition that in-degree of _t_ in graphs G<sup>∗</sup> and H<sup>∗</sup> is identical.

The construction of G<sup>∗</sup> is as follows: For each in-neighbour _w_ of the vertex _t_ in G, include edge (_w,t_) in G<sup>∗</sup> if and only if edge (_r<sub>w,t</sub>,t_) is present in H<sup>∗</sup>. Thus, the in-degree of _t_ in graphs G<sup>∗</sup> and _H_<sup>∗</sup> is identical. For vertices _v_ other than _t_, we include all in-neighbours of _v_ in G<sup>∗</sup>.

We will now prove that G<sup>∗</sup> is a (_k+f_-1)-FTRS of G. Consider any set _F_ of at most _k_ failed edges in G. Define a set _F_<sub>0</sub> of failed edges in H by including edge \((\ell_{u,v},r_{u,v})\) in _F_<sub>0</sub> for every \((u,v)\in F\). From the path correspondence above and the fact that H<sup>∗</sup> is a (_k+f_-1)-FTRS of H, it is evident that for any \(r\le\lambda\), there are _r_-edge-disjoint paths from _s_ to _t_ in G<sup>∗</sup>\\_F_ if and only if there are _r_-edge-disjoint paths from _s_ to _t_ in H<sup>∗</sup>\\_F_<sub>0</sub>. Therefore, G<sup>∗</sup> is a (_k+f_-1)-FTRS of G. \(\blacktriangleleft\)

It was shown in [4] that if out-degree of _s_ is one, and out-degree of all other vertices is bounded by two, then Algorithm 1 computes a _k_-FTRS for G in which in-degree of _t_ is at most 2_<sup>k</sup>_. We will prove in the next lemma that if max-flow(_s,t,_G)=_f_, and out-degree of every vertex other than _s_ is bounded by two, then Algorithm 1 in fact computes a (_k+f_-1)-FTRS for G in which the in-degree of _t_ is at most 2_<sup>k</sup>f_.

\(\blacktriangleright\) **Lemma 17.** _Let_ G _be a directed graph satisfying that the out-degree of every vertex other than the designated source s is bounded by_ 2_, and_ \(k\ge 1\) _be an integer parameter. Let_ \(t\in V(\mathcal{G})\) _satisfy_ max-flow(_s,t,_G)=_f, for some positive integer f. Then Algorithm 1 computes a_ (_k+f_-1)_-FTRS for_ G _in which the in-degree of node t is at most_ 2_<sup>k</sup>f._

