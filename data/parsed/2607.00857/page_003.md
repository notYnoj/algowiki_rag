This naturally leads us to _co-nondeterministic_ algorithms. Such algorithms, running in truly subcubic time, are known for APSP [11, 12]. Informally, they assert the existence of short witnesses whose validity can be quickly checked. In our setting, the prediction plays the role of such a witness. However, not every co-nondeterministic approach is suitable for us. For instance, the construction of [11], which relies on hashing after a reduction to the so-called Exact Triangle problem, does not appear to degrade gracefully under small inaccuracies in the witness. Instead, we build on the alternative framework based on Fredman’s trick and dominance product [12], which was originally proposed to handle real weights.

## 1.1 Our contribution

We propose an APSP algorithm that takes as prediction a _certificate_ consisting of sets of vertices causing the shortest _detour_ for each pair of vertices. The algorithm runs in time \(\mathcal{O}(n^{2.83}+\eta n)\), where \(\eta\) denotes the _prediction error_ defined as the number of pairs of vertices for which, informally speaking, the prediction was not sufficient to compute and certify optimality of the shortest path length. In this section we define all these notions formally.

Certificate. For an _n_-vertex weighted graph _G_=(_V,E,w<sub>G</sub>_), a **_certificate_** is a matrix \(C\in\mathcal{P}(V)^{V\times V}\) that contains, for every \(u,v\in V\) , a set \(C[u,v]\subseteq V\) of exactly _q_ vertices, where \(q\le n\) is a parameter to be chosen. The certificate hence has size \(\sum_{u,v\in V(G)}|C[u,v]|=n^2q\).

This describes the form of a certificate. Let us now give some intuition behind its semantics. In a ground-truth certificate, each entry _C[u,v_] should be the set of "best intermediate vertices" for a path from _u_ to _v_ in _G_. More formally, for a \(V\times V\) matrix _D_, we define the **_detour_** of a vertex _w_ as

detour<sub>_D,u,v_</sub>(_w_):=_D[u,w_]+_D[w,v_]-_D[u,v_].

Since later we work with estimated distances, which correspond to lengths of paths that are not necessarily shortest, we define the detour for general matrices. Ideally, the certificate entry _C[u,v_] should contain vertices _w_ with the _q_ smallest values of detour<sub>_D_<sup>∗</sup>_,u,v_</sub>(_w_), where _D_<sup>∗</sup> is the true shortest paths matrix of _G_.

We note that breaking ties is not important here, since we later only need to make sure that vertices with strictly smaller detour than the ones in the certificate are also in the certificate. Hence, one can break ties, for example, by index. Clearly, one can compute a ground-truth certificate in time O(_n_<sup>3</sup>) with any APSP algorithm.

Distance estimate matrix. Morally, our error measure tries to capture the impact of inaccuracies in the certificate _C_ that lead the verification algorithm to fail verifying the true shortest paths matrix _D_<sup>∗</sup>. However, since the algorithm does not know _D_<sup>∗</sup>, we define the error based on an estimate of _D_<sup>∗</sup> that is guided by the certificate. For a graph _G_ and certificate _C_, we define the corresponding **_distance estimate matrix_** _D<sub>G,C</sub>_ to be the element-wise maximum matrix that satisfies, for all \(u,v\in V\) , both

1. \(d(u,v)\le D_{G,C}[u,v]\), and<br> 2. \(D_{G,C}[u,v]=min\{w_G(u,v),min_{w\in C[u,v]}D_{G,C}[u,w]+D_{G,C}[w,v]\}\).<br> When _G_ and _C_ are clear from context, we drop the subscripts and write just _D_.

To put this definition in context, consider the classical Floyd-Warshall algorithm for APSP [37, 23, 44]. At a high level, it works by repeatedly updating the shortest path between some vertex pair (_u,v_), i.e., a matrix entry _M[u,v_], by considering a detour via another vertex _w_, i.e., _M[u,w_]+_M[w,v_]. We call such an update a _relaxation of M[u,v_]

