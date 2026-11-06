## 2 Fault-Tolerant Bounded Flow Preservers

FT-BFP has in-degree at most \(4^{k+\lambda}(k+\lambda)\). They also showed that a \((k+\lambda-1)\)-FTRS of a graph G also serves as it’s \((\lambda,k)\)-FT-BFP. Using this result in conjunction with the algorithm from [4], they obtain an alternate construction of a \((k,\lambda)\)-FT-BFP with at most \(2^{k+\lambda} n\) edges. However, this bound is quadratic in _n_ for any \(\lambda\) larger than log_n_.

We consider the problem of obtaining a tight bound on \((\lambda,k)\)-FT-BFP. Specifically, we aim to answer the following question:

_Given a directed graph_ G=(_V,E_) _with a source s, and a flow threshold_ \(\lambda\ge logn\)_, can we construct a_ sparse \((\lambda,k)\)_-FT-BFP_ \(\mathcal{H}=(V,E_H\subset E)\)_? If so, can we present graphs for which the construction turns out to be tight?_

In this paper, we affirmatively answer the question above. We provide construction for FT-BFP that has a linear dependence on \(\lambda\). In particular, we prove the following.

\(\blacktriangleright\) **Theorem 2.** _There exists an algorithm that for any directed graph_ G _on n vertices and m edges, and any integers_ \(\lambda,k\ge 1\)_, computes in_ \(O(\lambda 2^kmn)\) _time a_ \((\lambda,k)\)_-FT-BFP for_ G _with at most_ \(\lambda 2^kn\) _edges._

Furthermore, we show that the extremal bound of \(\lambda 2^kn\) in the above construction is tight by presenting the following lower bound.

\(\blacktriangleright\) **Theorem 3.** _For every_ \(\lambda,k,n\ge 1\)_, there exists a construction of an n-vertex directed graph whose optimal_ \((\lambda,k)\)_-FT-BFP contains_ \(\Omega(min\{2^k\lambda n,n^2\})\) _edges._

We next consider the problem of approximating \((\lambda,k)\)-FT-BFP structures. We show that unless _P=NP_, there is no polynomial-time algorithm to obtain a \(log(\lambda^{-1}n)\) approximation to optimal \((\lambda,k)\)-FT-BFP.

\(\blacktriangleright\) **Theorem 4.** _For any_ \(\lambda,k,n\ge 1\) _satisfying_ \(k=\Omega(log(\lambda^{-1}n))\)_, the problem of computing an_ \(O(log(\lambda^{-1}n))\) _approximate_ \((\lambda,k)\)_-FT-BFP for n vertex digraphs is NP-hard._

We finally present application of our FT-BFP construction in computing all-pairs fault- tolerant \(\lambda\)-reachability oracle.

\(\blacktriangleright\) **Theorem 5.** _Given any directed graph_ G=(_V,E_) _on n vertices and any positive constants_ \(\lambda,k\ge 1\)_, we can preprocess_ G _in polynomial time to build an O(n_<sup>2</sup>) _size data structure that, given any query vertex-pair_ (_x,y_) _and any set F of k edges, reports the_ \((x,y)\lambda\)_-reachability in_ G\\_F in O(n_<sup>1+_o_(1)</sup>) _time._

## 1.1 Existing Works

For undirected graphs, there exists a tight construction for \((\lambda,k)\)-FT-BFP with \(O((k+\lambda)\cdot n)\) edges that directly follows from \(\alpha\)-edge connectivity certificate constructions provided by Nagamochi and Ibaraki [19].

A closely related problem to that of graph preservers is fault-tolerant reachability oracles. For dual failures, the work of [11] obtained an _O(n_) size single source reachability oracle with constant query time for directed graphs. Brand and Saranurak [23], showed construction of an \(\widetilde{O}(n^2)\) sized _k_-fault-tolerant all-pairs reachability oracle that has \(O(k\omega)\) query time.

Recently, Baswana et al. [2] considered the problem of sensitivity oracle for reporting max- flow value for a single source-destination pair. They presented an _O(n_<sup>2</sup>) size data-structure that after failure of any two edges, reports the max-flow value of the surviving graph in constant time.

