_Proof._ First we analyze the running time. Note \(k=\tilde{O}(1)\) so that `decompose` requires \(\tilde{O}(n^2)\) time. Fix an iteration _i_. Then \(|D_i|=\tilde{O}\left(\frac{n}{s_i}\right)\), _E<sub>i</sub>_ has _ns_<sub>_i_-1</sub> edges, while \(E^*\cup(w\times V)\) have size \(\tilde{O}(n)\). Thus, each iteration _i_ requires \(\tilde{O}(n^2)\) time. Over log_n_ iterations, Algorithm 14 requires \(\tilde{O}(n^2)\) time.

Consider now \(\delta(u,v)=2\) and a path _P_=(_u,w,v_). Without loss of generality, assume \(\mathrm{deg}(u)\ge\mathrm{deg}(v)\) so that \(P\subset E_{\ell(u)}\). Let \(u^*\in D_{\ell(u)}\) be its representative \(r(u,D_{\ell(u)})\). Then, the execution of `Dijkstra` from _u_<sup>∗</sup> returns \(\hat{\delta}(u^*,v)\le 3\) via the path (_u_<sup>∗</sup>_,u,w,v_). Now, in the final iteration, we have \(\hat{\delta}(v,u)\le 4\) via the path (_v,u_<sup>∗</sup>_,u_) when executing `Dijkstra` from vertex _v_.

Finally, it is easy to observe that \(\hat{\delta}(u,v)\ge\delta(u,v)\) for all _u,v_ (without any assumption on the distance) since all traversed paths exist in the original graph _G_.

Combining Lemma D.1 with the algorithm of Baswana et al. \[BK10\] or Berman et al. \[BK07\] gives the desired result.

**Corollary D.2.** _There is an_ \(\tilde{O}(n^2)\)_-time algorithm that computes a_ \(\left(\frac{7}{3},0\right)\)_-approximate APSP solution in undirected, unweighted graphs._

_Proof._ Of course length 1 paths can be directly deduced from the adjacency matrix in time _O(n_<sup>2</sup>). From Lemma D.1, all distance 2 paths can be approximated within (2,0)-approximation in \(\tilde{O}\left(n^2\right)\) time. For paths of length 3 or more, a (2,1)-approximation is at least as good as a \((\frac{7}{3},0)\) approximation.

## E Faster Combinatorial (2,0)-approximation for path lengths \(\ge 4\).

In this section, we give an improved combinatorial algorithm for finding (2,0) approximations for paths with length \(k\ge 4\). We obtain a \(+\beta\)-additive approximations for paths of length at most \(\beta+1\) for every even \(\beta\) on dense graphs. In particular, we apply the algorithm with \(\beta=4\) to compute a +4 approximation on paths with length at most 5. This implies a (2,0) approximation for paths of length at least 4.

**Theorem E.1.** _Let G be an undirected, unweighted graph with n vertices. Let_ \(\beta\ge 4\) _be an even odd integer. Algorithm 15 computes in expected time_ \(\tilde{O}\left(n^{2+\frac{2}{3\beta+2}}\right)\) _a distance estimate_ \(\hat{\delta}\) _such that_ \(\delta(u,v)\le\hat{\delta}(u,v)\) _for all_ \(u,v\in V\) _and_ \(\hat{\delta}(u,v)\le\delta(u,v)+\beta\) _for all_ \(\delta(u,v)\le\beta+1\).

### Notation and Definitions

We define some notation that will be useful in this section. Let _G_ be an undirected, unweighted graph. Let \(\beta\) be an even integer, \(k=\frac{3\beta+2}{2}\) and \(k_0=\beta-2\). Let _s<sub>i</sub>,s_<sub>2</sub>_,...,s_<sub>_k_-1</sub> be degree thresholds. For \(k_0+1\le k\le k_0+\frac{\beta}{2}-1\) define \(r_i=\frac{\beta}{2}-(i-(k_0+1))\) and let \(N(u,r_i)=\{v\in V\text{s.t.}\delta(u,v)\le r_i\}\) be the _r<sub>i</sub>_-neighborhood of _u_.

**Definition E.2.** _For a vertex_ \(u\in V\) _and set_ \(S\subset V\) _, let_ \(p(u,S)=\mathrm{argmin}_{v\in S}\delta(u,v)\) _be the closest vertex in S to u._

We note that _p(u,S_) can be efficiently computed by executing `Dijkstra` on the graph _G_ augmented with a dummy vertex _w_ with 0 weight edges to every vertex \(v\in S\). For a given _i_, _X(u,i_) is an arbitrary subset of _N(u,r<sub>i</sub>_) if \(|N(u,r_i)|\ge s_i\) and \(C(u_i)=N(u,r_i)\cap D_{i+1}\) if \(|N(u,r_i)\cap D_{i+1}|\le 12s_{k-1}\mathrm{log}n\). Roughly speaking, _X(u,i_) is the first _s<sub>i</sub>_ vertices encountered when conducting a `BFS` from _u_. For details on how _X(u,i),C(u,i_) are computed see Lemma E.3.

