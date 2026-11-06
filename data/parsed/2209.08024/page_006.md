Finally, we argue that every optimal STT is a \(\frac{2}{3}\)-centroid tree. A special case of this result (for BSTs) was shown by Hirschberg, Larmore, and Molodowitch \[HLM86\], who also showed that the ratio \(\frac{2}{3}\) is tight (in the special case of BSTs, and thus, also for STTs).

**Theorem 1.9.** _Let T be an optimal STT of_ (T_,w). Then, T is a_ \(\frac{2}{3}\)_-centroid tree of_ (T_,w)._

### Structure of the paper.

In Section 2 we state a number of technical results needed in the proofs. In Section 3 we prove the general upper and lower bounds on the approximation ratio of centroid trees (Theorems 1.1 and 1.2). In Section 4 we prove the fine-grained bounds on the approximation ratio of centroid trees (Theorems 1.3 and 1.4). Section 5 contains the algorithmic results (Theorem 1.5 and extensions) and the lower bounds (Theorems 1.6 and extensions). Results on \(\alpha\)-centroids (Theorems 1.7, 1.8, and 1.9) are proved in Section 6. In Section 7 we conclude with open questions.

### Related work.

Different models of searching in trees have also been considered, e.g., the one where we query edges instead of vertices \[BFN99, LN01, MOW08, OP06\], with connections to searching in posets \[LS85, HIT11\]. In the edge-query setting, Cicalese, Jacobs, Laber and Molinaro \[CJLM11, CJLM14\] study the problem of minimizing the average search time of a vertex, and show this to be an NP-hard problem \[CJLM11\]. They also show that an "edge-centroid" tree (in their terminology, a greedy algorithm) gives a 1.62-approximation of the optimum \[CJLM14\].

STTs generalize BSTs, therefore it is natural to ask to what extent the theory developed for BSTs can be extended to STTs. Defining a natural _rotation_ operation on STTs, Bose, Cardinal, Iacono, Koumoutsos, and Langerman \[BCI<sup>+</sup>20\] develop an _O_(loglog_n_) competitive dynamic STT, analogously to Tango BSTs \[DHIP07\]. In a similar spirit, Berendsohn and Kozma \[BK22\] generalize Splay trees \[ST85\] to STTs. The rotation operation on STTs naturally leads to the definition of _tree associahedra_, a combinatorial structure that extends the classical associahedron defined over BSTs or other Catalan-structures. Properties of tree- and more general graph associahedra have been studied in \[CD06, Dev09, CMPP15, CLP18, CPV21, Ber22\].

Searching in trees and graphs has also been motivated with applications, including file system synchronisation \[BFN99, MOW08\], software testing \[BFN99, MOW08\], asymmetric communication protocols \[LM11\], VLSI layout \[Lei80\], and assembly planning \[IRV88\].

## 2 Preliminaries

Given a graph _G_, we denote by _V(G_) its set of vertices, by _E(G_) its set of edges, and by C(_G_) its set of connected components. If \(v\in V(G)\), denote by _N<sub>G</sub>(v_) the set of neighbors of _v_ in _G_, and deg_<sub>G</sub>(v_)=|_N<sub>G</sub>(v_)|. For \(S\subseteq V(G)\), denote by _G_\[_S_\] the subgraph of _G_ induced by _S_, and for brevity, _G-v=G_\[_V(G_)-{_v_}\], and _G-S=G_\[_V(G_)-_S_\].

The following observation is straightforward.

**Observation 2.1.** _Let T be a search tree on_ T , \(w:V(\mathcal{T})\rightarrow\mathbb{R}_{\ge 0}\)_, m=w_(T) _and r_=`root`(_T). For each component_ \(\mathcal{H}\in\mathbb{C}(\mathcal{T}-r)\)_, denote by T_<sub>H</sub> _the subtree of T rooted at the unique child of r in_ H_. Then_

\(\mathtt{cost}_w(T)=m+\sum_{\mathcal{H}\in\mathbb{C}(\mathcal{T}-r)}\mathtt{cost}_w(T_\mathcal{H})\ge m+\sum_{\mathcal{H}\in\mathbb{C}(\mathcal{T}-r)}\mathtt{OPT}(\mathcal{H},w).\)

Given a search tree _T_ on a tree T and a subgraph H of T , we denote by `LCA`_<sub>T</sub>_(H) the vertex with maximal depth in _T_ that is an ancestor of all vertices of H.

The following two technical lemmas will be useful later.

**Lemma 2.1.** _Let T be a search tree on_ T _and_ H _a connected subgraph of_ T _. Then_ \(\mathtt{LCA}_T(\mathcal{H})\in V(\mathcal{H})\).

_Proof._ Denote \(\ell=\mathtt{LCA}_T(\mathcal{H})\) and assume \(\ell\notin V(\mathcal{H})\). Denote \(\tilde{\mathcal{H}}=\mathcal{T}[V(T_\ell)]\). We have \(\mathcal{H}\subseteq\tilde{\mathcal{H}}\). Since H is connected, between every two vertices of H, there is a path in \(\tilde{\mathcal{H}}\) that does not go through \(\ell\). It follows that \(\mathcal{H}\subseteq\mathcal{C}\) for some connected component \(\mathcal{C}\in\mathbb{C}(\tilde{\mathcal{H}}-\ell)\). Then `LCA`_<sub>T</sub>_(C) is a child of \(\ell\) and an ancestor of all the vertices in H, a contradiction to the choice of \(\ell\).

