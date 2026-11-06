## 4 Warm-Starting All-Pairs Shortest Paths with Predictions

_with w._ Remember that a good certificate _C[u,v_] is supposed to contain vertices _w_ such that _D_<sup>∗</sup>[_u,w_]+_D_<sup>∗</sup>[_w,v_] is close to _D_<sup>∗</sup>[_u,v_]. If we trust the certificate, it hence does not make sense to relax _M[u,v_] with vertices _w_ that are not present in _C[u,v_].

The matrix _D<sub>G,C</sub>_ is the best (i.e., element-wise minimum) matrix achievable when initializing _M_ with edge weights and repeatedly performing only relaxations as indicated by the certificate, that is, relaxing _M[u,v_] only with vertices \(w\in C[u,v]\). Therefore, if _C[u,v_] contains at least one intermediate vertex on a shortest path from _u_ to _v_ in _G_ for every \(u,v\in V\) (with a shortest path of at least two edges), then _D<sub>G,C</sub>_ is the correct shortest paths matrix for _G_, i.e., _D<sub>G,C</sub>[u,v_]=_d(u,v_), for every \(u,v\in V\) . In Section 2 we show how to compute _D<sub>G,C</sub>_ efficiently, in time O(_n_<sup>2</sup>(_q_+log_n_)), i.e., proportional to the number of allowed relaxations _n_<sup>2</sup>_q_. Surprisingly, this requires moving away from the intuition from Floyd-Warshall and towards a Dijkstra-like order of relaxations.

**Error definition.** Now we define how we measure how "far" the predicted certificate (given in the input to our algorithm) is from a ground-truth certificate. Morally, the prediction error \(\eta\) counts the number of pairs \((u,v)\in V^2\), for which there is a vertex _w_ with small detour<sub>_D_<sup>∗</sup>_,u,v_</sub>(_w_) that is missing from the certificate _C[u,v_], where _D_<sup>∗</sup> denotes the true shortest paths matrix. These are exactly the entries _D_<sup>∗</sup>[_u,v_] for which _C[u,v_] does not provide enough information to verify their optimality. Since we can only verify _D<sub>G,C</sub>_ instead of _D_<sup>∗</sup>[_u,v_], we define the error based on the estimate matrix.

For a graph _G_, a certificate _C_, and a parameter \(p\le q\), we define the set U(_G,C,p_) of **_unverifiable pairs_** (_u,v_) for which there is a vertex _w_ not in the certificate _C[u,v_] that is among the _p_ vertices with the smallest detour<sub>_D,u,v_</sub>(_w_) values. Formally,

\(\mathrm{U}(G,C,p):=\big\{(u,v):\exists w\in V\backslash C[u,v]:|\{c\in C[u,v]:\mathrm{detour}_{D,u,v}(c)\le\mathrm{detour}_{D,u,v}(w)\}|<p\big\}.\)

Now we are ready to define the **_prediction error_** measure

\(\eta(G,C,p):=\big|\{(u,v):D_{G,C}[u,v]\neq d_G(u,v)\}\cup\mathrm{U}(G,C,p)\big|,\)

or just \(\eta\) when the parameters are clear from the context. Our main theorem reads as follows.

\(\blacktriangleright\) **Theorem 1.** _There is an algorithm that, given an n-vertex graph G_=(_V,E,w<sub>G</sub>), a certificate C with_ \(|C[u,v]|=q\le n\) _for all_ \(u,v\in V\) _, and a parameter_ \(p\le q\)_, computes APSP in G in time_

\(\mathcal{O}(n^2(q+\mathrm{log}n)+n^{3.66}/p+\eta(G,C,p)\cdot n).\)

_For_ \(p=\Theta(n^{0.83})\) _and_ \(q=\Theta(p)\) _it runs in time_ \(\mathcal{O}(n^{2.83}+\eta n)\).

For a fixed _q_, the parameter _p_ can be used as a trade-off between error and verification time. For \(p'\le p\), notice that \(\mathrm{U}(G,C,p')\subseteq\mathrm{U}(G,C,p)\), so also \(\eta(G,C,p')\le\eta(G,C,p)\). In other words, a smaller value of _p_ leads to a smaller prediction error but a longer verification time. In the case when the error value \(\eta\) is small enough not to dominate the running time, it is reasonable to choose _p_ and _q_ to balance the remaining running time. This leads to the choice of \(p=\Theta(n^{0.83})\), and gives the claimed running time guarantee.

We remark that the intricacies of our error definition seem hard to avoid with our current understanding of the APSP problem. Indeed, as discussed earlier, any learning-augmented algorithm has to degenerate to a co-nondeterministic algorithm when the prediction is perfect. The error measure hence has to capture the amount of additional work imposed on the verification algorithm by inaccuracies in the prediction. Given that there are only two known

