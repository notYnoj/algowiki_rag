implication similarly relies on the simple subdivision technique used in \[TV93\], and again is not part of our new contributions. In this paper, we make use only of the forward implication of Theorem 2, but we also include the proof of the backward implication for completeness.

**Theorem 2.** _Let_ G _be a family of graphs closed under minors and edge subdivisions, and let_ \(\alpha\) _be a parameter. Then_<tbc>

\(\alpha_{\mathcal{M}(\mathcal{G})}\le\alpha\Longleftrightarrow\forall G\in\mathcal{G},\forall w\in\mathbb{N},\exists SDD\big(G,2w,\frac{\alpha}{2w}\big).\)

<tbc>_Proof._ Forward direction. Assume \(\alpha_{\mathcal{M}(\mathcal{G})}\le\alpha\), and let \(G\in\mathcal{G}\) be arbitrary and \(w\in\mathbb{N}\). We define a multicut instance _M_ on _G_ and apply Theorem 1. Let<tbc>

\(S=\{(u,v)\in V(G)\times V(G)|d_G(u,v)\ge 2w\}\)

<tbc>be the set of source-sink pairs, and assign unit costs to all edges. Define the fractional solution _x_ by setting \(x(e)=\frac{1}{2w}\) for all \(e\in E(G)\). This is easily seen to be a feasible solution to the LP relaxation (1). By Theorem 1, there exists a probability distribution _y_ over feasible multicuts of _M_ such that each edge \(e\in E(G)\) is cut with probability at most

\(\alpha_{\mathcal{M}(\mathcal{G})}\cdot\frac{1}{2w}\le\frac{\alpha}{2w}.\)

Finally, note that a set of edges is a feasible multicut for this instance if and only if it defines a 2_w_-diameter decomposition of _G_. This yields the desired \(SDD(G,2w,\frac{\alpha}{2w})\).

Backward direction. Assume that for every \(G\in\mathcal{G}\) and \(w\in\mathbb{N}\) there exists \(SDD(G,2w,\frac{\alpha}{2w})\). Let _M_ be an arbitrary instance of the minimum multicut problem on \(G\in\mathcal{G}\) with edge costs \(c:E(G)\rightarrow\mathbb{Z}_+\) and source-sink pairs \(\{(s_i,t_i)\}_{i=1}^k\). We will show that<tbc>

\(\frac{OPT_{IP}(M)}{OPT_{LP}(M)}\le\alpha.\)

<tbc>Let \(x=\{x_e\}_{e\in E(G)}\) be an optimal fractional solution to the LP relaxation (1). Since LP solutions are rational, we may assume \(x_e\in\mathbb{Q}\) for all _e_. Define the support of _x_ as<tbc>

\(A=\{e\in E(G)|x_e>0\}.\)

<tbc>Choose \(w\in\mathbb{N}\) such that 2_wx<sub>e</sub>_ is an integer for every \(e\in A\). Construct a new graph _S(G,M_) by contracting every edge \(e\notin A\) and replacing each edge \(e\in A\) with a path _P<sub>e</sub>_ of length 2_wx<sub>e</sub>_. Since G is closed under minors and edge subdivisions, we have \(S(G,M)\in\mathcal{G}\). By assumption, there exists \(SDD(S(G,M),2w,\frac{\alpha}{2w})\). This means there is a probability distribution _y_ over F<sub>2_w_</sub>(_S(G,M_)) (the family of edge sets inducing components of diameter at most 2_w_-1) such that<tbc>

\(\sum_{F\in\mathcal{F}_{2w}(S(G,M))e\in F}y_F\le\frac{\alpha}{2w},\forall e\in E(S(G,M)).\)

<tbc>**Claim 1.** _For the multicut instance M, we have_<tbc>

\(\frac{OPT_{IP}(M)}{OPT_{LP}(M)}\le\alpha.\)

<tbc>_Proof of Claim._ For each \(F\in\mathcal{F}_{2w}(S(G,M))\), define

\(g(F)=\{e\in E(G)|F\cap E(P_e)\neq\varnothing\}.\)

_g(F_) is a feasible multicut for the instance _M_. The reason is as follows. Suppose, for<tbc>

