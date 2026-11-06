similar spirit, it is known that the 2-dimensional Weisfeiler-Leman (2-WL) algorithm subsumes the spectral information of the adjacency matrix (as well as other associated graph matrices) \[Für10, RS23, AFKV25\], which we exploit for our deterministic algorithms for Constrained Spanning Tree and \(\ell_p\)-Spanning Tree.

## 5 Our Model of Computation

### 5.1 Preliminary: Attributed Graphs and Isomorphism

Throughout this work, we consider graphs whose vertices and edges may carry _attributes_. For instance, a vertex attribute may be used to designate sources or sinks, while an edge may carry a vector attribute representing multiple edge weights. The specific attributes depend on the problem under consideration.

For example, in Negative Triangle, the attribute of each edge is simply its weight, and there are no vertex attributes (i.e., every vertex receives the same default attribute, denoted by \(\perp\)). For Constrained Shortest Path, the attribute of each edge _e_ with length \(\ell(e)\) and cost _c(e_) is the vector \(\alpha(e)=(\ell(e),c(e))\). The vertex attributes designate the terminals: \(\alpha(v)=\mathsf{s}\) if _v_ is the source, \(\alpha(v)=\mathsf{t}\) if _v_ is the sink, and \(\alpha(v)=\perp\) otherwise.

We adopt the natural notion of _isomorphism_ for attributed graphs: an isomorphism between two graphs _G_ and _H_ is a bijection between their vertex sets that preserves adjacency as well as all vertex and edge attributes.

**Definition 5.1** (Isomorphism of attributed graphs)**.** Let

\(G=(V_G,E_G,\alpha_G^V,\alpha_G^E)\text{and}H=(V_H,E_H,\alpha_H^V,\alpha_H^E)\)

be two graphs, where _V<sub>G</sub>,V<sub>H</sub>_ are vertex sets, _E<sub>G</sub>,E<sub>H</sub>_ are edge sets, and \(\alpha^V,\alpha^E\) assign attributes from alphabets \(\Sigma_V,\Sigma_E\) to the vertices and edges, respectively.

We say that _G_ and _H_ are _isomorphic_ (denoted \(G\cong H\)) if there exists a bijection \(\varphi:V_G\rightarrow V_H\) such that the following conditions hold.

1. **Adjacency is preserved:** \((u,v)\in E_G\Longleftrightarrow(\varphi(u),\varphi(v))\in E_H\) for all \(u,v\in V_G\).<tbc>

2. **Vertex attributes are preserved:** \(\alpha_G^V(u)=\alpha_H^V(\varphi(u))\) for all \(u\in V_G\).<tbc>

3. **Edge attributes are preserved:** \(\alpha_G^E(u,v)=\alpha_H^E(\varphi(u),\varphi(v))\) for all \((u,v)\in E_G\).

_Remark_ 5.2 (Isomorphism-closed problems). This paper focuses on _isomorphism-closed problems_, a class encompassing virtually all natural computational tasks on graphs and related objects. Let \(\Pi\) be a decision or optimization problem (e.g., Constrained Shortest Path, Negative Triangle, SAT, or Energy Game). Each problem \(\Pi\) we consider is equipped with an equivalence relation \(\cong\) defining when two problem instances are isomorphic.<sup>20</sup> We assume that \(\Pi\) is inherently _closed under isomorphism_. For a decision problem, this means \(I\cong J\) implies that _I_ is a YES-instance if and only if _J_ is a YES-instance. For an optimization problem, \(I\cong J\) implies that both instances share the identical optimal value, meaning \(OPT_\Pi(I)=OPT_\Pi(J)\).

### 5.2 The Isomorphic-Priors Model

We study every problem \(\Pi\) within a model consisting of two phases:

<sup>20</sup>For graph problems (e.g., GI, CSP, CST, IS, MaxCut), this corresponds to standard or attributed graph isomorphism (see Definition 5.1). For problems like SAT, two CNF formulas \(\Phi\) and \(\Phi'\) are isomorphic if \(\Phi'\) can be obtained from \(\Phi\) via a bijection of variables (preserving negations) alongside arbitrary permutations of clauses and literals.

