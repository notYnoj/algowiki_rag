<tbc>hypergraphs, we generalize the definition of heavy subgraph problems and show their optimal solutions are still preserved by uniform sparsification.

**Definition 1** (Heavy Subgraph Problems)**.** Given a weighted (hyper)graph _H_=(_V,E,w_), a collection of feasible solutions S which are sub(hyper)graphs of _H_, and an objective function \(f:\rightarrow\mathbb{R}_{\ge 0}\), we say that the problem of finding S<sup>∗</sup>=argmax_f_(S) is a _subgraph problem_. If there exists a weight function \(w:E\rightarrow\mathbb{R}_{\ge 0}\), a partition of the solutions \(\mathbb{S}=\mathbb{S}_1\cup\mathbb{S}_2\cup\cdots\cup\mathbb{S}_\ell\), and constants \(f_1,\dots,f_\ell\) such that for all \(k\in[\ell]\) and all \(\mathcal{S}\in\mathbb{S}_k\), \(f(\mathcal{S})=f_k\cdot w(\mathcal{S})\), we say that the optimization problem is _locally linear of rank_ \(\ell\). We say that a locally linear optimization problem is \(\gamma\)_-bounded_ if for all \(k\in[\ell]\), \(f(\mathcal{S}^*)\ge f_k\frac{m}{n}max\{\gamma log|\mathbb{S}_k|,1\}\). Finally, a subgraph problem is \((\gamma,\ell)\)_-heavy_ if it is locally linear of rank \(\ell\) and \(\gamma\)-bounded.

Noting that sparsification is simply a reweighting of edges, we are able to altogether avoid the ‘hereditary property’ introduced in \[16\]. Avoiding this property allows for cleaner generalization to weighted instances and removes unnecessary complexity. We also marginally strengthen the \(\gamma\)-bound (adding the \(max\{\cdot,1\}\)) for technical reasons.

For some intuition on this definition, we sketch how Densest Subgraph is a \((\frac{1}{logn},n)\)-heavy subgraph problem. For a graph _G_=(_V,E,w_), the solutions to DSG are the induced subgraphs of _G_ and can be partitioned by number of vertices into \(\ell=n\) sets such that \(\mathcal{S}\in\mathbb{S}_k\) if |_V_(S)|=_k_. To satisfy local linearity, we set \(f_k=\frac{1}{k}\) for each _k_, yielding \(\rho(\mathcal{S})=|E(\mathcal{S})|/|V(\mathcal{S})|=f_k\cdot w(\mathcal{S})\). Lastly, one can verify the \(\gamma\) bound holds for \(\gamma=\frac{1}{logn}\) using \(|\mathbb{S}_k|=\genfrac(){pt}{2}{n}{k}\) and the bound \(\rho^*(G)\ge\rho(V)\ge m/n\). More generally, Esfandiari et al. show that the family of heavy subgraph problems includes a range of classic graph optimization problems.

**Proposition 3** (\[16, Theorem 1.4\])**.** The following statements hold.

• Densest Sub(hyper)graph is a \((\frac{1}{logn},n)\)-heavy subgraph problem.<tbc>

• Densest Bipartite Subgraph is a \((\frac{1}{2log2n},n)\)-heavy subgraph problem.<tbc>

• _d_-Max Cut is a \((\frac{1}{2logd},1)\)-heavy subgraph problem.<tbc>

• _d_-Sum-Max Clustering is an \((\frac{n-2d}{nlogd},1)\)-heavy subgraph problem.

In Section A, we show that Proposition 3 extends to weighted instances and our strengthened definition of \(\gamma\)-boundedness, as well as proving the inclusion of Densest Subhypergraph. For unweighted graphs, Esfandiari et al. show the following bound on the sample complexity required to uniformly sparsify heavy subgraph problems.

**Proposition 4** (\[16, Theorem 1.3\])**.** Let _G_=(_V,E_) be a simple graph, and let P be a \((\gamma,\ell)\)- heavy subgraph problem. There is a randomized algorithm that makes \(O(n(4+\delta)log\ell/(\gamma\varepsilon^2))\) random edge samples and returns a \((1+\varepsilon)\)-approximation for P on _G_ with probability \(1-e^{-\delta}\).

As a consequence of the fact that we can sample a uniformly random edge of _G_ in _O_(log_n_) queries, Cohen-Addad et al. \[15\] observe that this sampling approach immediately lifts to unweighted graphs in the cut query model.<sup>7</sup> Our first contribution is to generalize Proposition 4 to weighted graphs and hypergraphs in Theorem 3.1. While we cannot sample uniformly random edges on weighted graphs in the cut query model, we instead have access to a primitive Rand_<sub>G</sub>_ that outputs edge _e_ with probability _w(e)/w(G_). To uniformly sparsify our graph, upon drawing an edge _e_, we will therefore insert _e_ into our sampled graph with weight 1 rather _w(e_).<sup>8</sup> The key<tbc>

<sup>7</sup>It is even possible to sample edges at random without replacement using cut queries, as in the algorithm of \[16\], instead of oversampling and discarding duplicates. Additionally, in the sparse case, one can appeal to the graph learning result of \[9\] and learn _G_ exactly in _O(m_log_n/_log_m_) queries. <sup>8</sup>In spirit, this approach matches that of \[6\], which treats weighted edges as multiedges and then uniformly subsamples each individual edge to sparsify weighted (hyper)graphs. In their sampled graph, the multiplicity of edge _e_ is distributed according to Bin(_w(e),C/w(H_)), as opposed to Bin(_C,w(e)/w(H_)) for ours.

