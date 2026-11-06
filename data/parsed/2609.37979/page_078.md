Similarly, we obtain that

\(\sum_{w\in N_{out}(v)}f(v,w)=\frac{1}{|\chi^{-1}(a)|}\sum_{b\in N_{out}(a)}f^*(a,b).\) (5)

Together, we conclude that

\(\sum_{u\in N_{in}(v)}f(u,v)=\frac{1}{|\chi^{-1}(a)|}\sum_{b\in N_{in}(a)}f^*(b,a)=\frac{1}{|\chi^{-1}(a)|}\sum_{b\in N_{out}(c)}f^*(a,b)=\sum_{w\in N_{out}(v)}f(v,w)\)

where the second equality holds since _f_<sup>∗</sup> is a flow. Also, we obtain that

\(\mathrm{val}(f)=\sum_{w\in N_{out}(s)}f(s,w)=\sum_{b\in N_{out}(\chi(s))}f^*(\chi(s),b)=\mathrm{val}(f^*)\)

since the color class containing _s_ has size one.

**Corollary A.13.** _Let_ \(G=(V,E,c:E\rightarrow\mathbb{R},s,t)\) _and_ \(G'=(V',E',c':E'\rightarrow\mathbb{R},s',t')\) _be two instances of_ Maximum Flow_. If_ \(G\equiv_{1\text{-}\mathrm{WL}}G'\)_, then G and_ \(G'\) _have the same maximum flow value._

_Proof._ If \(G\equiv_{1\text{-}\mathrm{WL}}G'\), then we obtain that \(G/\chi_\infty=G'/\chi_\infty\). Now, the statement follows from Lemmas A.11 and A.12.

_Proof of Theorem A.9._ The first part follows directly from Theorem 8.4 and Corollary A.13. For the second part, observe that Lemmas A.11 and A.12 provide an explicit method for obtaining a flow on _H_ given the flow for a prior graph _G<sub>i</sub>_ such that \(G_i\equiv_{1\text{-}\mathrm{WL}}H\).

## B More Conditional Lower Bounds

### B.1 Additional Problem Definitions

**Definition B.1** (0/1-Integer Linear Programming)**.** In the 0/1-Integer Linear Programming we are given an integer matrix _C_ and an integer _d_ and. We have to decide if there exist a 0/1-vector _x_ with _Cx=d_.

Two problem instances (_C,d_) and \((C',d')\) are isomorphic if there are permutation matrices _P_ and _Q_ with \(PCQ=C'\) and \(Pd=d'\).

Note that 0/1-Integer Linear Programming is closed under isomorphism since if _x_ is a solution to _Cx=d_ if and only if \(x'=Q^{-1}x\) is a solution to \(C'x'=d'\). For the remaining problem checking that they are closed under isomorphism is easy to see.

**Definition B.2** (_k_-Center)**.** In the _k_-Center problem we are given a simple graph _G_=(_V,E,w_) with edge weights \(w:E\rightarrow\mathbb{N}\), a number \(k\in\mathbb{N}\), and a value \(c\in\mathbb{N}\). We have to decide if there is a set \(X\subseteq V\) of size at most _k_ such that every \(v\in V\) has distance at most _c_ to the closest point in _X_.

Two problem instances (_G_=(_V,E,w),k,c_) and \((G'=(V',E',w'),k',c')\) are isomorphic if \(k=k'\), \(c=c'\) and _G_ is isomorphic to \(G'\).

**Definition B.3** (Clique)**.** In the Clique problem we are given a simple graph _G_ and a value _k_. We have to decide if _G_ contains _k_-clique (i.e., a subgraph with _k_ vertices such that each vertex is connected to each other vertex)

Two problem instances (_G,k_) and \((G',k')\) are isomorphic if _G_ and \(G'\) are isomorphic as graphs and \(k=k'\).

