<tbc>**Theorem 4.** _Let I be any maximum-cardinality critical independent set of G such that_<tbc>

\(id_c(G)=0,|I|=\frac{n}{2}.\)

<tbc>_Choose any perfect matching in H_=(_I,J;E<sub>H</sub>),_<tbc>

\(M=\{x_iy_i:1\le i\le k\},\)

<tbc>_where_

\(I=\{x_1,\dots,x_k\},J=\{y_1,\dots,y_k\},k=\frac{n}{2}.\)

_Construct a digraph D<sub>M</sub> with vertex set_ [_k_]={1_,...,k}. For distinct_ \(i,j\in[k]\)_, add an arc_ \(i\rightarrow j\) _if_ \(x_iy_j\in E\)_. Then_

_G contains a small blocking set_ \(\Longleftrightarrow D_M\) _is not strongly connected._

_When D<sub>M</sub> is not strongly connected, every sink strongly connected component C gives a small blocking set of G,_

\(T_C=\{x_i:i\in C\}.\)

_Proof._ By Theorem 3, in the case _id<sub>c</sub>(G_)=0 and |_I_|=_n/_2, the graph _G_ contains a small blocking set if and only if _I_ contains a nonempty proper tight subset. If _k_=1, then _I_ has no nonempty proper subset and _D<sub>M</sub>_ is a single-vertex strongly connected digraph, so the assertion holds directly. We henceforth consider \(k\ge 2\).

For a balanced bipartite graph with a perfect matching, classical Dulmage- Mendelsohn decomposition theory states that a nonempty proper subset \(S\unknown I\) satisfying |_N(S_)|=|_S_| exists if and only if the auxiliary digraph induced by the perfect matching is not strongly connected [13]. For any chosen perfect matching _M_, our digraph _D<sub>M</sub>_ is precisely the corresponding directed representation obtained by orienting edges from _I_ to _J_, contracting each matched pair _x<sub>i</sub>y<sub>i</sub>_, and omitting self-loops. Therefore,<tbc>

\(I\text{contains a nonempty proper tight subset}\Longleftrightarrow D_M\text{is not strongly connected. Here, all neighborhoods of subsets of}I\text{are the same in}H\text{and}G\text{.}\)

<tbc>This test does not depend on the particular choice of _M_. Indeed, for any nonempty proper tight subset \(S\unknown I\) and any perfect matching _M_, the set _M(S_) of vertices matched to _S_ satisfies<tbc>

\(M(S)\subseteq N(S),|M(S)|=|S|=|N(S)|,\)

