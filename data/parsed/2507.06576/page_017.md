and doing the same argument for \(P'_b,P'_u,P'_v\), we obtain,<tbc>

\(\sum_{F\in A_b}y_F\le(w\cdot p)-1;\sum_{F\in A_c}y_F\le(w\cdot p)-1;\sum_{F\in A_d}y_F\le(w\cdot p)-1.\)

<tbc>Let \(A^*=A\backslash(A_a\cup A_b\cup A_c\cup A_d)\). From the discussion above, it follows that,

\(\sum_{F\in A^*}y_F=\sum_{F\in A}y_F-\sum_{F\in A_a\cup A_b\cup A_c\cup A_d}y_F\ge\left(1-\frac{w\cdot p}{2}\right)-4\cdot(w\cdot p-1)=5-\frac{9\cdot w\cdot p}{2}>0.\)

This shows that \(A^*\neq\varnothing\) and completes the proof of the claim. \(\blacktriangle\)

In Section 8, we use the construction from Theorem 6 to exhibit an explicit instance of the minimum multicut problem with \(\frac{\mathrm{OPT}_{IP}}{\mathrm{OPT}_{LP}}\ge\frac{20}{9}\) . In the following Section 7, we improve the lower bound to \(\frac{16}{7}\) .

## 7 \(\frac{16}{7}\) Lower Bound for Cactus Graphs

In this section, we build upon the ideas developed in the previous sections to improve the lower bound to \(\frac{16}{7}\) . In the proof of Theorem 6, the witness graph _G_ was obtained as the 1-sum of a cycle of length 2_w_ with two simple paths of length \(\frac{w}{2}\) . That argument invoked Theorem 5 to guarantee the existence of a suitable _SDD(G,_2_w,p,r_). We now strengthen this construction by replacing the two paths with carefully chosen cactus "amplifiers."

The starting point is that for any cactus _G_ and any \(r\in V(G)\) and \(k\in\{1,\dots,w\}\), there exists an _SDD(G,_2_w,p,r_) such that a _F_ drawn from this distribution satisfies \(\mathrm{rad}_F(r)\le k-1\) with probability at least 1-(_w-k)p_ (by Theorem 5). Our aim is to leverage components for which this success probability is as small as possible (i.e., the "hardest" attachments), and graft them into the cycle gadget.

**Definition 6.** _Let_ G _be a graph family containing K_<sub>2</sub> _and closed under taking minors and subdivisions. Fix_ \(k\in\{1,\dots,w\}\)_. Define_<tbc>

\(R_{(\mathcal{G},2w,p)}^k=\mathrm{inf}_{G\in\mathcal{G}r\in V(G)}\mathrm{max}_{y\text{\textit{is an}}SDD(G,2w,p,r)}\left\{\sum_{F\in\mathcal{F}_{2w}^k(G,r)}y_F\right\}.\)

<tbc>_By Theorem 5, we always have_ \(R_{(\mathcal{G},2w,p)}^k\ge 1-(w-k)p\)_. Moreover,_ \(R_{(\mathcal{G},2w,p)}^k\le k\cdot p\)_: indeed, for any G,r choose a shortest r-u path Q of length k. If_ \(\mathrm{rad}_F(r)\le k-1\) _then F must intersect E(Q); hence for any SDD(G,_2_w,p,r),_<tbc>

\(\sum_{F\in\mathcal{F}_{2w}^k(G,r)}y_F\le\sum_{F\in\mathcal{F}_{2w}^w(G,r)E(Q)\cap F\neq\varnothing} y_F\le\sum_{e\in E(Q)}\sum_{F\in\mathcal{F}_{2w}^w(G,r)e\in F}y_F\le k\cdot p.\)

<tbc>_Therefore,_

\(1-(w-k)p\le R_{(\mathcal{G},2w,p)}^k\le k\cdot p.\) (8)

_This upper bound will be used in the proof of Theorem 8._

To proceed, we require a structural extension, namely Theorem 7, which generalizes Theorem 5. For this purpose, we introduce the following Definition 7:

**Definition 7** (Generalized 1-sum)**.** _Let G be a non-empty graph, and let l be a natural number. Choose vertices_ \(u_1,\dots,u_l\in V(G)\)_. For each i_=1_,...,l, let G<sub>i</sub> be a non-empty_<tbc>

