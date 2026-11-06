<tbc>\(\alpha\lesssim 2^{k/3}\). Yet, there remains a huge exponential gap between this bound and the clustering threshold \(\alpha_\mathrm{clust}\approx 2^k(\mathrm{ln}k)/k\) for searching algorithms.

Meanwhile, message-passing algorithms such as belief and survey propagation from the cavity method are naturally inference algorithms for estimating marginal probabilities and are believed to work all the way up to the clustering threshold. Given the close relationship between inference and counting/sampling, this seems to suggest that counting and sampling may also be tractable up to the clustering threshold, which is the conjectured threshold for searching algorithms. Therefore, it is natural to ask the following question:

_For random k-SAT, are counting and sampling tractable up to the algorithmic threshold for searching?_

## 1.1. Counting and sampling for random _k_-SAT.

We establish the tractability of approximate counting and almost uniform sampling for random _k_-SAT up to densities \(\alpha\le 2^k/\mathrm{poly}(k)\). In particular, the exponential term 2_<sup>k</sup>_ matches the satisfiability and algorithmic threshold for random _k_-SAT and extends beyond the lower bound for worst-case _k_-SAT instances (see Remark 1.5 for more discussion).

The random _k_-SAT model is formally defined as follows.

**Definition 1.1** (random _k_-SAT formulas)**.** For \(k\ge 3\), define \(\Phi(k,n,m)\) as the law of the _k_-SAT formula chosen uniformly at random from all _k_-SAT formulas with _n_ variables and _m_ constraints.

Specifically, the random _k_-SAT formula \(\Phi=(V,C)\sim\Phi(k,n,m)\) is generated as follows:

\(\bullet\) The variable set is defined as _V_={_v_<sub>1</sub>_,v_<sub>2</sub>_,...,v<sub>n</sub>_}.<tbc>

\(\bullet\) The constraint set is defined as _C_={_c_<sub>1</sub>_,c_<sub>2</sub>_,...,c<sub>m</sub>_}, where each constraint _c<sub>i</sub>_ consists of exactly _k_ literals \(\ell_{i,1},\ell_{i,2},\dots,\ell_{i,k}\), with each literal \(\ell_{i,j}\) chosen uniformly at random from all 2_n_ literals {_v_<sub>1</sub>_,v_<sub>2</sub>_,...,v<sub>n</sub>_,\(\neg v_1,\neg v_2,\dots,\neg v_n\}\).

We present results for efficient (approximate) counting and (almost uniform) sampling of random _k_-SAT up to densities \(\alpha\le 2^k/\mathrm{poly}(k)\), improving upon the previous best regime \(\alpha\lesssim 2^{k/3}\) \[HWY23\].

**Theorem 1.2** (counting and sampling random _k_-SAT solutions)**.** _There exists a universal constant_ \(c\ge 1\) _such that the following holds with high probability over the choice of the random k-SAT formula_ \(\Phi=(V,C)\sim\Phi(k,n,\lfloor\alpha n\rfloor)\) _where_ \(0<\alpha\le 2^k/k^c\).

_For any_ \(\varepsilon>0\)_, there exist the following algorithms, both with running time_ \((n/\varepsilon)^{\mathrm{poly}(k,\alpha)}\):

\(\bullet\) _(Counting) A deterministic algorithm that outputs_ \(\hat{Z}\) _which is an_ \(\varepsilon\)_-approximation of the number of solutions_ \(Z(\Phi)\) _of_ \(\Phi\)_, i.e.,_ \((1-\varepsilon)Z(\Phi)\le\hat{Z}\le(1+\varepsilon)Z(\Phi)\);<tbc>

\(\bullet\) _(Sampling) An algorithm that outputs a random assignment_ \(X\in\{\text{True, False}\}^V\) _that is_ \(\varepsilon\)_-close in total variation distance to_ \(\mu_\Phi\)_, the uniform distribution over all solutions of_ \(\Phi\).

One may hope to estimate the number of solutions \(Z(\Phi)\) by simply computing and outputting \(\mathbb{E}[Z(\Phi)]\); this however does not provide an effective approximation algorithm. The random _k_-SAT model does not enjoy the _superconcentration property_ \[BCE17, CCM<sup>+</sup>24\] where \(Z(\Phi)\) concentrates around \(\mathbb{E}[Z(\Phi)]\) with constant or tiny \(\omega(1)\) factors with high probability, and furthermore, the standard trick for boosting poly(_n_) approximation ratios to FPTAS \[SJ89\] does not apply on such random instances.

We remark that while we consider random _k_-SAT in Theorem 1.2, we can easily obtain similar results for random _regular k_-SAT of variable-degree \(d=k\alpha\) whose analysis would be simpler due to the absence of high-degree vertices. For the random regular hypergraph independent set problem (equivalently, random regular _monotone k_-SAT), it was shown that the Glauber dynamics for sampling is rapidly mixing at density \(\alpha=O(2^k/k^2)\) \[HSZ19\].

Our counting and sampling algorithms apply to general random atomic CSPs. Here, we present results for random hypergraph colorings. A hypergraph _H_=(_V,_E) is _k_-uniform if |_e_|=_k_ for all \(e\in\mathcal{E}\). We adopt the following definition for the random generation of _k_-uniform hypergraphs.

**Definition 1.3** (Erdős-Rényi hypergraph)**.** For \(k\ge 2\), define _H(k,n,m_) as the uniform distribution over all _k_-uniform hypergraphs with _n_ vertices and _m_ distinct hyperedges.

For a hypergraph _H_=(_V,_E), a proper hypergraph _q_-coloring \(X\in[q]^V\) assigns one of the _q_ colors to each \(v\in V\) , ensuring no hyperedge is monochromatic. We present results for efficiently counting and sampling proper _q_-colorings of random _k_-uniform hypergraphs up to densities \(\alpha\le q^k/\mathrm{poly}(k,q)\).<tbc>

