**Algorithm 1**

Require: Graph G on vertices V with a cut oracle, a \((\gamma,\ell)\)-heavy subgraph problem P, and tolerances \(\delta,\varepsilon>0\)<br>
Ensure: \((1+\varepsilon)\)-approximation for P(G) w.p. at least \(1-e^{-\delta}\)<br>
\(C\leftarrow 240n(1+\delta+log\ell+\gamma^{-1})/\varepsilon^2\)<br>
for all \(v\in V\) do<br>
\(deg(v)\leftarrow\mathsf{cut}(\{v\})\triangleright n\) queries<br>
\(\hat{G}\leftarrow(V,E,\hat{w}=0)\)<br>
for i=1...C do \(\triangleright C\) iterations<br>
Sample \(e\leftarrow\) a random edge of G using Rand<br>
\(\hat{w}(e)\leftarrow\hat{w}(e)+1\)<br>
return \(\mathcal{P}(\hat{G})\)

We note that our refined analysis in Theorem 3.1 shaves off an O(log<sup>2</sup>_n_)-factor in the meta- algorithm’s bound, matching the best-known \(O(nlogn/\varepsilon^2)\)-sample complexity for sparsifying DSG on unweighted graphs \[16, 30\]. In fact, we are able to show that our result is a polylogarithmic factor off of the ideal query complexity for DSG, up to dependence on \(\varepsilon\). To do so, we first introduce the disjointness problem DISJ<sub>N</sub>(x,y_) on _N_-bit vectors _x_ and _y_, which takes value `True` if their coordinate-wise AND is all zeroes \((x\wedge y=0^N)\), or `False` otherwise (if \(\exists i\in[N]:x_i\wedge y_i=1\)).

**Lemma 3.5.** The randomized query complexity of a \((2-\delta)\)-approximation for DSG is \(\Omega(n/logn)\), for any \(\delta>0\).

_Proof._ Reduction from DISJ<sub>N</sub>(x,y_) on _N_ bits. We will define a multigraph _G_ on _n_=6_N_ vertices. For each index _i_, we create a gadget of three disjoint pairs of vertices, adding edge (_u<sub>i</sub>,v<sub>i</sub>_) if _x<sub>i</sub>_=1 and otherwise edge (_a<sub>i</sub>,b<sub>i</sub>_), and similarly adding edge (_u<sub>i</sub>,v<sub>i</sub>_) if _y<sub>i</sub>_=1 or else edge (_c<sub>i</sub>,d<sub>i</sub>_). If DISJ<sub>N</sub>(x,y_), then \(\rho^*(G)=1/2\); otherwise, there is some index _i_ where _x<sub>i</sub>=y<sub>i</sub>_, and so \(\rho^*(G)=\rho(\{u_i,v_i\})=1\). Observe that the two players can simulate a cut query on _G_ with _O_(log_n_) bits of communication. Assume that they have an _f(n_)-query \((2-\delta)\)-approximation for DSG, for some \(\delta>0\). The players can solve DISJ<sub>N</sub>(x,y_) by outputting `False` if they find a subgraph of density at least \(1/(2-\delta)>1/2\), and `True` otherwise. This gives an _O(f(n_)log(_n_)) bit communication protocol for DISJ. However, the randomized communication complexity of DISJ is \(\Omega(N)\) \[22\]. By _n_=6_N_, we have \(f(n)=\Omega(n/logn)\) as claimed.

In particular, this gives the \(\Omega(n/logn)\) lower bound on the query complexity of both exact and \((1+\varepsilon)\)-approximate DSG (in the \(\varepsilon<1\) regime). For unweighted graphs, we give a slightly weaker analog of this result in Section B.1. We note that Lemma 3.5 also applies to D_k_S, but is superseded in most regimes by the lower bounds in Section 5.

Another heavy subgraph problem is _d_-Max Cut, which is the standard Max Cut problem when _d_=2. Plevrakis et al. \[33\] give a \((1+\varepsilon)\)-approximation for weighted Max Cut in \(O(nlogn^3n(logn+1/\varepsilon^2))\) queries, with an accompanying lower bound of \(\Omega(n/logn)\) queries. Since Max Cut is a (0.5,1)-heavy subgraph problem, we improve their upper bound by up to an _O_(log<sup>2</sup>_n_)-factor (in the regime \(\varepsilon=\Theta(1)\)) as another application of Theorem 3.3.

**Corollary 3.6.** Let _G_=(_V,E_) be a weighted graph. There is a randomized algorithm that makes \(O(nlogn^2n/\varepsilon^2)\mathsf{cut}\) queries and returns a \((1+\varepsilon)\)-approximation to the maximum cut of _G_.

In addition to reducing the number of queries required, our approach is much simpler than the algorithm of \[33\], which constructs a full cut-sparsifier for the graph. This technique has yielded a host of exact algorithms for minimum cut problems in the query model, but it seems<tbc>

