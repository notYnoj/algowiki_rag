**Lemma 1** (Tree and cotree, Chapter 4.5 of \[13\])**.** _T is a spanning tree of G iff the_ cotree _T_<sup>∗</sup>=_E_\\_T is a spanning tree of G_<sup>∗</sup>.

**Fundamental cuts and cycles.** We use the duality between cycles defined by _T_ and cuts defined by _T_<sup>∗</sup>:

**Definition 1** (Fundamental cuts)**.** Removing an edge \(e\in T\) from _T_, breaks _T_ into two connected components. The set \(\delta_G(T,e)\) of edges of _G_ that have one endpoint in each component is called the fundamental cut of _T_ with respect to _e_ in _G_.

**Definition 2** (Fundamental cycles)**.** Adding an edge \(e\in G\backslash T\) to _T_, closes one simple cycle _C<sub>G</sub>(T,e_) with _T_. The cycle _C<sub>G</sub>(T,e_) is called the fundamental cycle of _T_ with respect to _e_ in _G_.

When _G_ is clear from the context, we use \(\delta(T,e)\) and _C(T,e_) to denote \(\delta_G(T,e)\) and _C<sub>G</sub>(T,e_) respectively.

**Lemma 2** (Fundamental cut-cycle duality \[13\])**.** _Let T_<sup>∗</sup> _be a spanning tree of G_<sup>∗</sup> _and T=E_\\_T_<sup>∗</sup> _be its cotree. T_<sup>∗</sup> _defines a fundamental cut in G_<sup>∗</sup> _w.r.t. an edge e_<sup>∗</sup> _iff T defines a fundamental cycle in G w.r.t. e. That is,_ \(\delta_{G^*}(T^*,e^*)=C_G(T,e)\).

**Separators.** Let \(w_A(\cdot)\) be a weight function on \(A\in\{V,F\}\).

**Definition 3** (\(\alpha\)-proper weights)**.** \(w_A(\cdot)\) is \(\alpha\)-proper for \(\alpha\in(0,1)\) if \(w_A(a)\le\alpha\cdot w_A(G)\) for each \(a\in A\).

**Definition 4** (Balanced separators)**.** Let _c\<_1 be a constant. A _c_-balanced separator _S_ is a set of vertices s.t. the connected components of _G_\\_S_ are of size at most \(c\cdot w_A(G)\).

**Definition 5** (Fundamental cycle separators)**.** Let _c\<_1 be a constant, and let _T_ be a spanning tree of _G_. A fundamental cycle separator of _G_ is a _c_-balanced separator _S_ which constitutes a fundamental cycle of _T_. I.e., there exists an edge \(e\notin T\) s.t. _S=C(T,e_), and \(w_A(S_{in}^-)\), \(w_A(S_{out}^-)\le c\cdot w_A(G)\).

**Balanced and critical nodes.** We use the following definitions of \[9\] that discusses rooted trees. For a node \(f\in T^*\), let \(T_f^*\) denote the subtree of _T_<sup>∗</sup> rooted at _f_. We denote by _w(T_<sup>∗</sup>) the total weight of all nodes of _T_<sup>∗</sup>.

**Definition 6** (Balanced node)**.** \(f\in T^*\) is \((\alpha,\beta)\)-balanced for constants \(\alpha<\beta\le 1\) if \(\alpha\cdot w(T^*)\le w(T_f^*)\le\beta\cdot w(T^*)\).

**Definition 7** (Critical node)**.** \(f\in T^*\) is \((\alpha,\beta)\)-critical for constants \(\alpha<\beta\le 1\) if \(w(T_f^*)>\beta\cdot w(T^*)\), and \(w(T_h^*)<\alpha\cdot w(T^*)\) for every child _h_ of _f_ in _T_<sup>∗</sup>.

## 3 Technical Overview and Related Work

Computing a balanced separator is a fundamental building block in many algorithms for planar graphs. In distributed algorithms, it is desired that the separator is a path _P_ in some given spanning tree _T_ s.t. adding to _P_ an edge \(e\unknown\in T\) (perhaps even \(e\unknown\in G\)) that connects _P_’s endpoints closes a fundamental cycle _C(T,e_) in _G_ (or in \(G\cup\{e\}\) if \(e\unknown\in G\)). Setting _T_ to be a BFS tree, we get a separator of size _O(D_). The goal is therefore to find such an edge _e_ where _C(T,e_) encloses a constant 0_\<c\<_1 fraction of _G_’s total weight of vertices. Finding such an edge _e_ is not an easy task.

However, if the weights were assigned to faces (rather than vertices), then the problem becomes easy, as it amounts to finding a balanced node _f_ in the dual tree _T_<sup>∗</sup>. Indeed, such a node _f_ naturally defines a fundamental cut \(\delta_{G^*}(T^*,e^*)\) in _G_<sup>∗</sup> (i.e., _e_<sup>∗</sup>=(_f_, parent(_f_))) and hence a fundamental cycle _C(T,e_) in _G_ (Lemma 2). See Figure 1. Since _f_ is balanced, the weight of _f_’s subtree \(T_f^*\) in _G_<sup>∗</sup> (the weight of all faces enclosed by _C(T,e_) in _G_) is a constant fraction of _G_’s total weight of faces. Formally:

