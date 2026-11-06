## 8:18 Beating Trivial Time for Tricky Triangle Tasks

_w_ prime factors, and their sum has at most 2_w_ prime factors.) By a union bound over all _t_<sup>3</sup> triples of nodes in \(I',J',K'\), the probability that some \(i,j,k\in I',J',K'\) do not form an exact triangle yet the mod triangle check returns yes on \(I',J',K'\) is at most 20_t_<sup>3</sup>(log_w)/w_<sup>9</sup>. As there are (_n/t_)<sup>3</sup> triples in total, the _expected_ number of false-positive triples (there is no exact triangle yet the mod triangle check returns yes) is at most 20_n_<sup>3</sup>(log_w)/w_<sup>9</sup>. By Markov’s inequality, the probability that the number of false-positive triples exceeds _n_<sup>3</sup>/(_t_<sup>3</sup>_w_<sup>3</sup>) is at most

\(20t^3(logw)/w^6<20w^{3/2}(logw)/w^6<20/w^4\)

for _w_ sufficiently large. Therefore the probability the algorithm outputs _don’t know_ is at most 20_/w_<sup>4</sup>, which is _o_(1). \(\blacktriangleleft\)

## 6 Attacks on 4-Cycle

We now turn to the problem of 4-cycle detection. Our high-level approach to reduce to a problem called Concatenated Element Distinctness, and then speed up that problem via packing into words. We assume without loss of generality that the graph is bipartite: by imposing a random bipartition and deleting edges that violate it, any 4-cycle is preserved with constant nonzero probability. We now show that it suffices to solve 4-cycle in graphs with maximum degree \(O(\sqrt{n})\).

\(\blacktriangleright\) **Lemma 25.** _Suppose a bipartite graph_ \(G=(L\cup R,E)\) _on n\>_2 _nodes is 4-cycle free. Then for all_ \(d\ge\sqrt{2n}\)_, G has at most_ 2_n/d nodes with degree at least d._

**Proof of Lemma 25.** Suppose there exist _N_:=2_n/d_+1 nodes with degree at least _d_, which we will call _v_<sub>1</sub>_,...,v<sub>N</sub>_. Because _G_ is 4-cycle free by assumption, each of the neighborhoods of these nodes have intersection of size at most 1. _v_<sub>1</sub> has _d_ neighbors. The number of neighbors of _v_<sub>2</sub> that are not neighbors of _v_<sub>1</sub> is at least _d_-1, and the neighbors of _v_<sub>3</sub> that are not neighbors of either _v_<sub>1</sub> or _v_<sub>2</sub> is at least _d_-2. So the total number of distinct neighbors of these nodes is

\(d+(d-1)+\cdots+(d-N+1)=dN-\sum_{i=1}^{N-1}i=d\left(\frac{2n}{d}+1\right)-\frac{N(N-1)}{2}=2n\left(1-\frac{n}{d^2}\right)+\left(d-\frac{n}{d}\right).\)

Observe that if we let \(d\ge\sqrt{2n}\), this expression is at least _n_+1 for _n\>_2, which is a contradiction. \(\blacktriangleleft\)

Thus, the number of high-degree nodes is relatively small, which allows us to brute-force over them in subquadratic time. In particular, we can run the following preprocessing step.

\(\blacktriangleright\) **Lemma 26.** _Given a bipartite graph G_=(_V,E), there is a O(n_<sup>3/2</sup>) _preprocessing algorithm that either returns "4-cycle" or produces a graph_ \(G'\) _with maximum degree_ \(\Delta=\sqrt{2n}\) _such that solving 4-cycle on G and_ \(G'\) _gives the same answer._

**Proof of Lemma 26.** If \(|E|\ge\frac{n}{4}(1+\sqrt{4n-3})\) or if more than \(\sqrt{2n}\) vertices with degree at least \(\sqrt{2n}\), return "4-cycle" (by Reiman’s theorem and Lemma 25, respectively). Otherwise, let \(N\le\sqrt{2n}\) be the number of vertices that have degree at least \(\sqrt{2n}\). From each of these vertices, run a modified version of breadth-first search that terminates when any node is visited twice (this corresponds to cycle detection). This requires _O(n_) time per node, for a total of _O(n_<sup>3/2</sup>) time. If any of these breadth-first searches terminate after running three

