It is widely known that for any \(\varepsilon\in(0,1)\), any graph _G_ has an \(\varepsilon\)-cut sparsifier with \(\widetilde{O}(n/\varepsilon^2)\) edges. We state the version of sparsifer we need via the following theorem.

**Theorem 2.6.** _Let G be an unweighted undirected connected graph with n vertices and average degree d. Then, for any_ \(\varepsilon\in(0,1)\)_, there exists an_ \(\varepsilon\)_-cut sparsifier of G with_ \(O\left(\frac{nlog^2n}{\varepsilon^2}\right)\) _edges and weights bounded by_ \(O\left(\frac{\varepsilon^2d}{log^2n}\right)\).

We make several remarks. First, the theorem establishes an asymptotically optimal trade-off between the number of edges and the maximum weight of the sparsifier. To see this, let _G_ be a graph with _m_ edges. Any \(\varepsilon\)-cut sparsifier must have total weight at least \((1-\varepsilon)m=\Omega(m)\). Since our sparsifier contains \(O\left(\frac{nlog^2n}{\varepsilon^2}\right)\) edges, at least one edge must carry a weight \(\frac{\Omega(m)}{O\left(\frac{nlog^2n}{\varepsilon^2}\right)}=\Omega\left(\frac{\varepsilon^2d}{log^2n}\right)\), which matches our upper bound up to constant factors.

Second, for completeness, the proof of Theorem 2.6 is deferred to Section B. In fact, we prove a stronger statement for an extended notion known as a _spectral_ sparsifier. We emphasize that our proof does not claim novelty in technique. Many foundational results on sparsification are well established \[Kar99; BK15; FHHP19; SS11; ST11; BSS12; CGP+23; LWZ25\], and our argument merely follows prior approaches, such as that of \[CGP+23\]. However, to the best of our knowledge, previous work has not explicitly addressed bounding the maximum edge weight in sparsifiers. When bounds are provided, they are typically of order \(\widetilde{O}(\varepsilon^2n)\). Our contribution lies in explicitly deriving _asymptotically optimal_ bounds on the maximum edge weight. This refinement turns out to be critical for our algorithmic applications.

## 2.1 Cut-Query Model

In this setting, an input graph _G_=(_V,E_) is hidden from us, and we are only allow to make _cut- queries_ to the graph. In particular, for each query we can specify a cut (_S,T_) to an oracle, and receives |_E<sub>G</sub>(S,T_)| in return. Our objective is to compute a task (in this case, a minimum _s-t_ cut) while minimizing the query complexity of our algorithm. Note that the only notion of cost here is the queries; thus, we can assume to have an unlimited local computation power.

Many fundamental tasks can be simulated efficiently via cut queries. For instance, we can find out if an edge (_a,b_) exists in the graph within _O_(1) queries, learn all the _m_ edges in the graph within _O(n+m_log_n_) queries, or uniformly sample an edge of the graph with an amortized cost of _O_(log_n_) queries. This random sampling primitive also opens up many doors of opportunity to the world of sequential algorithm. Perhaps one of the most insightful takeaways from \[RSW18\] is that we can obtain a cut sparsifier of _G_ within not-too-many cut queries to _G_, thereby enabling us to obtain a \((1\pm\varepsilon)\)-approximation of the _value_ of the minimum _s-t_ cut.

**Lemma 2.7** (Theorem 3.5 of \[RSW18\])**.** _For any_ \(\varepsilon\in(0,1)\)_, there is a randomized algorithm that computes an_ \(\varepsilon\)_-cut sparsifier of G with_ \(\widetilde{O}(n/\varepsilon^2)\) _edges and maximum weight_ \(\widetilde{O}(\varepsilon^2n)\)_. The algorithm uses_ \(\widetilde{O}(n/\varepsilon^2)\) _cut queries to G and succeeds w.h.p._

**Corollary 2.8.** _For any_ \(\varepsilon\in(0,1)\)_, there is a randomized algorithm that computes f such that_ \((1-\varepsilon)\nu(G)\le f\le(1+\varepsilon)\nu(G)\)_. The algorithm uses_ \(\widetilde{O}(n/\varepsilon^2)\) _cut queries to G and succeeds w.h.p._

Throughout this paper, we will utilize a more specific type of query to a graph _G_=(_V,E_) called the _find-edge query_ which can be simulated efficiently via cut queries.

**Definition 2.9** (Find-edge query)**.** _Let G_=(_V,E_) _be an underlying graph. A_ find-edge _query takes in as inputs disjoint sets_ \(A,B\subseteq V\) _, and outputs_ FindEdge(_A,B_) _which is either_ "NONE" _if_ \(E\cap(A\times B)=\emptyset\)_, or an edge_ \((a,b)\in E\cap(A\times B)\) _if otherwise._

