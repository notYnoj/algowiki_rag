We formalize the corresponding testing problems and prove hardness results that answer both questions negatively.

**Definition 4.1.** _Let G_=(_P,E_) _be a directed graph, let d be a metric on P, let_ \(\alpha>1\)_, and let d_<sub>0</sub>_\>_0_. The_ single-scale \(\alpha\)-navigability testing problem _asks to report all pairs_ \((s,t)\in P\times P\) _such that d(s,t_)=_d_<sub>0</sub> _and there exists_ \(u\in P\) _with_

\((s,u)\in E\text{\textit{and}}d(u,t)\le\frac{1}{\alpha}d(s,t).\)

Question (1) asks whether one can avoid the bottleneck of matrix multiplication in solving this problem. Lemma 4.3 answers this question in the negative, showing that a reduction exists in the opposite direction, and that this problem is essentially equivalent to Boolean matrix multiplication.

**Definition 4.2.** _Let G_=(_P,E_) _be a directed graph, let d be a metric on P, and let_ \(\alpha>1\)_. The_ \(\alpha\)-navigability testing problem _asks to report all pairs_ \((s,t)\in P\times P\) _such that there exists_ \(u\in P\) _with_

\((s,u)\in E\text{\textit{and}}d(u,t)\le\frac{1}{\alpha}d(s,t).\)

Question (2) asks whether any \(O(n^{2.5-\varepsilon})\)-time implementation exists, as such an implementation would improve upon the state of the art single-criterion approximation. Corollary 4.9 answers this question in the negative by demonstrating APSP-hardness.

**Lemma 4.3.** _There is a reduction from Boolean matrix multiplication on two_ \(n\times n\) _matrices to single-scale_ \(\alpha\)_-navigability testing that uses one oracle call and O(n_<sup>2</sup>) _additional time._

_Proof._ Let \(A,B\in\{0,1\}^{n\times n}\). We construct an instance of single-scale \(\alpha\)-navigability testing as follows.

Let \(P=S\unknown U\unknown T\), where _S_={_s_<sub>1</sub>_,...,s<sub>n</sub>_}, _U_={_u_<sub>1</sub>_,...,u<sub>n</sub>_}, and _T_={_t_<sub>1</sub>_,...,t<sub>n</sub>_}.

We first define a metric _d_ on _P_. Let _H_ be the undirected weighted graph on vertex set _P_ containing the following edges:

• for every \(i,j\in[n]\), an edge {_s<sub>i</sub>,t<sub>j</sub>_} of weight 1;<tbc>

• for every \(k,j\in[n]\) with _B<sub>k,j</sub>_=1, an edge {_u<sub>k</sub>,t<sub>j</sub>_} of weight \(1/\alpha\).

Let _d_ be the shortest-path metric of _H_.

Next, define a directed graph _G_=(_P,E_) by adding the edge (_s<sub>i</sub>,u<sub>k</sub>_) to _E_ if and only if _A<sub>i,k</sub>_=1.

We claim that one call to the single-scale \(\alpha\)-navigability testing oracle with parameter _d_<sub>0</sub>=1 suffices to compute the Boolean product _AB_.

First observe that in _H_, for every \(i,j\in[n]\), the direct edge {_s<sub>i</sub>,t<sub>j</sub>_} has weight 1. This edge realizes the shortest-path distance, since alternative path from _s<sub>i</sub>_ to _t<sub>j</sub>_ has length greater than 1, as there are no direct edges between _S_ and _U_. Hence, _d(s<sub>i</sub>,t<sub>j</sub>_)=1.

Therefore, for every \(i,j\in[n]\), the oracle reports (_s<sub>i</sub>,t<sub>j</sub>_) if and only if there exists \(k\in[n]\) such that<tbc>

\((s_i,u_k)\in E\Longleftrightarrow A_{i,k}=1\text{and}d(u_k,t_j)\le\frac{1}{\alpha}\cdot d(s_i,t_j)=\frac{1}{\alpha}.\)

<tbc>Further note, for every \(k,j\in[n]\),

\(d(u_k,t_j)\le\frac{1}{\alpha}\Longleftrightarrow B_{k,j}=1,\)

because the only possible path in _H_ of weight \(\le\frac{1}{\alpha}\) between _u<sub>k</sub>_ and _t<sub>j</sub>_ in _H_, is the direct edge (_u<sub>k</sub>,t<sub>j</sub>_) which is present if and only if _B<sub>k,j</sub>_=1. Overall, a pair (_s<sub>i</sub>,t<sub>j</sub>_) is reported if and only if there exists \(k\in[n]\) such that _A<sub>i,k</sub>=B<sub>k,j</sub>_=1.

