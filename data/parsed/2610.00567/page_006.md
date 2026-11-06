<tbc>**Definition 11.** _A tree decomposition T of G has_ width (_p,q_) _if for each bag B of T, there exist vertices_ \(u_1,\dots,u_i\in B\) _with_ \(i\le p\) _and edges_ \(e_1,\dots,e_j\in E(G[B])\) _with_ \(j\le q\) _such that_

\(E\big(G[B]\backslash\{u_1,\dots,u_i\}\big)=\{e_1,\dots,e_j\},\)

_and moreover every vertex of B_\\{_u_<sub>1</sub>_,...,u<sub>i</sub>_} _is an endpoint of some_ \(e_\ell\), \(\ell\le j\).

_We say that the vertices u_<sub>1</sub>_,...,u<sub>i</sub> and edges e_<sub>1</sub>_,...,e<sub>j</sub> is a_ (_p,q_)-witness _of the bag B._

The same edge could occur in multiple bags in a tree decomposition. We have to ensure that an edge occuring in the image of a homomorphism is only multiplied in once in the term corresponding to the homomorphism. We define a notion of _local vertex_ for this purpose.

**Definition 12.** _Let T be a tree decomposition of G. Fix a function_ \(f:V(G)\rightarrow V(T)\) _assigning each vertex_ \(v\in V(G)\) _to some bag f(v_) _(such a bag exists by the definition of tree decomposition). We say v is_ local _to bag B if f(v_)=_B, and write_

\(V_B=\{v\in V(G):f(v)=B\}.\)

Note that since _f_ is a function, each vertex of _G_ is local to exactly one bag in the tree decomposition.

We now prove that we can efficiently construct circuits for homomorphism polynomials from (_p,q_)-width tree decompositions. Our proof is a refinement of the dynamic programming algorithm by Díaz, Serna, and Thilikos \[4\].

**Theorem 1.** _Let G be a k-vertex pattern graph having a tree decomposition T of_ (_p,q)-width, and let H be a host graph with n vertices and m edges. Then an arithmetic circuit of size O(n<sup>p</sup>m<sup>q</sup>_) _computing Hom<sub>G,H</sub> can be constructed in time_ \(\widetilde{O}(n^pm^q)\).

_Proof._ We describe the construction of the arithmetic circuit for Hom<sub>_G,H_</sub>.

Let _T_ be a tree decomposition of _G_ of (_p,q_)-width, rooted at the bag _R_. For any bag _B_ in _T_, let _T<sub>B</sub>_ denote the subtree of _T_ rooted at _B_, and define

\(G_B=G[V'],\text{where}V'=\bigcup_{B^\prime\in V(T_B)}B'\)

.

The circuit will have two kinds of gates, denoted by \(g_{B,\phi}\) and \(h_{B,\phi}\), where _B_ is a bag in _T_ and \(\phi\) is some partial homomorphism from _G_ to _H_ defined on a subgraph of _G_ to be specified later.

We define \(g_{B,\phi}\) so that the polynomial computed at \(g_{B,\phi}\) is:

\(g_{B,\phi}=\sum_{\phi^\prime:G_B\rightarrow H\phi^\prime\sim\phi}\prod_{v\in V(G_B)v\text{is local to some bag in}T_B}y_{\phi^\prime(v)}\) (1)

