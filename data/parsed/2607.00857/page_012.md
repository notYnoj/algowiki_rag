\(\blacktriangleright\) **Lemma 5.** _For all_ (_u,v_) _with_ \(D[u,v]\neq d(u,v)\)_, there is_ \((a,b)\in U\)_, potentially equal to u or v, with d(u,v_)=_d(u,a_)+_d(a,b_)+_d(b,v)._

**Proof.** Consider a pair (_u,v_) with \(D[u,v]=min_{w\in V}D[u,w]+D[w,v]\) and \(D[u,v]\neq d(u,v)\). Let _P_ be a shortest (_u,v_)-path with the fewest number of edges. If _P_=(_u,v_), this is a contradiction to the assumption that _D[u,v_] is not the correct distance by Lemma 3.

Otherwise, let _w_ be an intermediate vertex on _P_. Since \(D[u,v]\le D[u,w]+D[w,v]\), at least one of _D[u,w_] and _D[w,v_] is also not the correct distance, say _D[u,w_]. If \((u,w)\in U\), we are done. Otherwise, we have \(D[u,w]=min_{x\in V}D[u,x]+D[x,w]\) and we can repeat the same argument with (_u,w_) instead of (_u,v_). This way, the number of edges on the fewest-hop shortest path decreases by at least one. Hence at some point we arrive at a pair in _U_. \(\blacktriangleleft\)

## 4 Stage 3: Fixing the distance estimates

In this section, we give the final stage of our algorithm and prove Theorem 1. It works similar in spirit to Stage 1 as we fix entries in increasing order of distance. We rely on the following observation when computing the length of a shortest path from _u_ to _v_. Since all subpaths have smaller or equal distance, their values are correct. Furthermore, this means that if _D[u,v_] is unchanged and successfully verified, we can skip all relaxations of _D[u,v_].

\(\blacktriangleright\) **Theorem 1.** _There is an algorithm that, given an n-vertex graph G_=(_V,E,w<sub>G</sub>), a certificate C with_ \(|C[u,v]|=q\le n\) _for all_ \(u,v\in V\)_, and a parameter_ \(p\le q\)_, computes APSP in G in time_

\(\mathcal{O}(n^2(q+logn)+n^{3.66}/p+\eta(G,C,p)\cdot n).\)

_For_ \(p=\Theta(n^{0.83})\) _and_ \(q=\Theta(p)\) _it runs in time_ \(\mathcal{O}(n^{2.83}+\eta n)\).

**Proof.** Remember that we can assume that all edge weights are non-negative by a standard preprocessing step, as discussed in Section 5. First, we run the algorithm from Lemma 3 to compute the matrix _D_ from _C_. Then, we use Lemma 4 to compute the set _U_. We call all pairs \((u,v)\in U\) marked. During the algorithm we will relax _D_ to turn it into the correct distance matrix for _G_. If at any point a distance changes, we also mark the corresponding pair. The remaining algorithm (see Algorithm 4) is similar to the one in Lemma 3 but distributes the total amount of work only on marked pairs.

Initialize a priority queue _Q_ with all pairs \((u,v)\in V^2\) and priorities _D[u,v_].

While _Q_ is nonempty, extract the pair (_u,v_) with minimum _D[u,v_], and do the following:

If (_u,v_) is marked, iterate over all \(w\in V\) . Relax _D[u,w_] with _D[u,v_]+_D[v,w_]. Relax _D[w,v_] with _D[w,u_]+_D[u,v_]. If anything changed, mark the corresponding entry and update the key in _Q_.

If (_u,v_) is not marked, iterate only over \(w\in V\) where (_u,w_) or (_w,v_) is marked. Relax _D[u,w_] with _D[u,v_]+_D[v,w_]. Relax _D[w,v_] with _D[w,u_]+_D[u,v_]. Update _Q_.

When _Q_ is empty, return _D_ as the distance matrix of _G_.

Running time. Let (_u,v_) be a pair of vertices that does not contribute to the error \(\eta\). Therefore, we have _D[u,v_]=_d(u,v_) and \((u,v)\in V^2\backslash\mathrm{U}(G,C,p)\). By Lemma 4, every pair \((u,v)\in V^2\backslash\mathrm{U}(G,C,p)\) is also not in _U_. It is hence not marked initially. Since _D_ always contains an upper bound to the true distances in _G_, the entry _D[u,v_] will never be changed. So, (_u,v_) will not be marked during the algorithm. This shows that at most \(\eta\) pairs will become marked during the whole algorithm.

\(\blacktriangleright\) **Lemma 5.** _For all_ (_u,v_) _with_ \(D[u,v]\neq d(u,v)\)_, there is_ \((a,b)\in U\)_, potentially equal to u or v, with d(u,v_)=_d(u,a_)+_d(a,b_)+_d(b,v)._

