## 1.1 Our Contributions

In the streaming setting, \[6\] sparsify weighted (hyper)graphs by treating weighted edges as multiedges and then uniformly subsampling each edge. However, this result does not generalize to the cut query model, as we cannot simulate a uniformly random edge sample in weighted graphs; instead, the cut sampler returns edge _e_ with probability proportional to _w(e_). Our first observation is that this primitive is intrinsically an _importance sampler_. We build on this to obtain a \((1+\varepsilon)\)-approximation to Densest Subgraph on weighted graphs.

**Theorem 3.4.** Let _G_=(_V,E_) be a weighted graph. There is a randomized algorithm that makes \(O(nlog^2n/\varepsilon^2)\) cut queries and returns a \((1+\varepsilon)\)-approximation to the densest subgraph of _G_.

In Lemma 3.5, we prove that for any \(\delta>0\), a \((2-\delta)\)-approximation for DSG requires \(\Omega(n/logn)\) queries, leaving a modest gap on the optimal query complexity of approximation schemes. More generally, we show that uniform sparsification gives approximations for all heavy subgraph problems in the cut query model, sharpening the bound on sample complexity obtained in \[16\] while doing so. As an application of this meta-algorithm, we give a \((1+\varepsilon)\)-approximation for weighted Max Cut using \(O(nlog^2n/\varepsilon^2)\) cut queries. This improves upon the bound of Plevrakis et al. \[33\], who introduced this problem to the cut query model and achieved a bound of \(O(nlog^3n(logn+1/\varepsilon^2))\) queries. Their algorithm goes through cut-sparsifier machinery and is somewhat technical. With a much simpler approach, we are able to sharpen this upper bound by up to an _O_(log<sup>2</sup>_n_) factor, pushing nearer to their lower bound of \(\Omega(n/logn)\) queries.

**Corollary 3.6.** Let _G_=(_V,E_) be a weighted graph. There is a randomized algorithm that makes \(O(nlog^2n/\varepsilon^2)\) cut queries and returns a \((1+\varepsilon)\)-approximation to the maximum cut of _G_.

We also consider the Densest Subhypergraph problem (DSH). In Section 4.1, we prove that it is impossible to obtain an \(o(\sqrt{n})\)-approximation for DSH with cut queries alone. However, using the edge oracle introduced in \[14\], we are able to uniformly sparsify hypergraphs by augmenting our importance sampling approach with rejection sampling techniques.

**Theorem 3.7.** Let _H_=(_V,E_) be a weighted hypergraph, with rank _r_ unknown. There is a randomized algorithm that makes \(O(nrlogn/\varepsilon^2)\) cut and edge queries and returns a \((1+\varepsilon)\)- approximation to the densest subhypergraph of _H_.

As in the classical regime, Densest _k_-Subgraph is a much harder problem in the cut query model than its unconstrained sibling; for exact D_k_S, we show that one cannot beat the trivial approach of learning _G_ entirely and (inefficiently) solving D_k_S offline, settling its query complexity up to an _O_(log_n_) gap for randomized algorithms in weighted graphs. We summarize our bounds on the exact query complexity of DSG and D_k_S in  1. In particular, our lower bound on randomized algorithms for Densest _k_-Subgraph also rules out any approximation schemes.

**Lemma 5.4.** The randomized query complexity of a \((1.5-\delta)\)-approximation for D_k_S on unweighted graphs is \(\Omega(n^2/logn)\), for any \(\delta>0\).

The Densest _k_-Subhypergraph problem (D_k_SH) turns out to be widely intractable in the query model. Section 4 rules out approximations of any kind using only cut queries or only edge queries, with additional cut lower bounds presented in Section 5.1. In Section 5.2, we then generalize our results for D_k_S to achieve exponential lower bounds on the exact query complexity of Densest _k_-Subhypergraph for algorithms with access to cut, edge, and add queries. We are even able to show mild inapproximability for D_k_SH with the full query suite.

**Theorem 5.6.** The randomized query complexity of a \((1+1/(r+1)-\delta)\)-approximation of D_k_SH on rank-_r_ hypergraphs is at least \(\Omega(\genfrac(){pt}{2}{n}{r-1}/(n^2rlogn))\), for any \(\delta>0\) and any combination of cut, add, and edge queries. If _r=O_(1), this yields a lower bound of \(\Omega(n^{r-3}/logn)\) queries.

