<tbc>Each leaf in a segmentation tree _S_ corresponds to a polyhedron. We often identify the segmentation tree _S_ with the set of leaves of _S_ and a leaf with the polyhedron corresponding to the leaf. For example, we say something like "for each \(L\in S\), \(\widetilde{v}\in L\) is a point in the polyhedron _L_".

Suppose we are given a segmentation tree _S_ and a set E<sup>+</sup> of examples.

**Definition 14.** For each \(L_1,L_2\in S\), we denote the set of example transitions from _L_<sub>1</sub> to _L_<sub>2</sub> by \(\mathcal{E}_{L_1,L_2}^+:=\{(\widetilde{v},\widetilde{v}')\in\mathcal{E}^+|\widetilde{v}\in L_1,\widetilde{v}'\in L_2\}\). An example \((\widetilde{v},\widetilde{v}')\in\mathcal{E}^+\) is _crossing_ w.r.t. _S_ if \((\widetilde{v},\widetilde{v}')\in\mathcal{E}_{L_1,L_2}^+\) for some \(L_1\neq L_2\), and _non- crossing_ if \((\widetilde{v},\widetilde{v}')\in\mathcal{E}_{L,L}^+\) for some _L_.

**Definition 15.** We define the _dependency graph G(S,_E<sup>+</sup>) for _S_ and E<sup>+</sup> by the graph (_V,E_) where vertices _V=S_ are leaves, and edges \(E=\{(L_1,L_2)|L_1\neq L_2,\exists(\widetilde{v},\widetilde{v}')\in\mathcal{E}_{L_1,L_2}^+\}\) are crossing examples.

We denote the set of start points \(\widetilde{v}\) and end points \(\widetilde{v}'\) of examples \((\widetilde{v},\widetilde{v}')\in\mathcal{E}^+\) by \(\underline{\mathcal{E}^+}:=\{\widetilde{v}|(\widetilde{v},\widetilde{v}')\in\mathcal{E}^+\}\cup\{\widetilde{v}'|(\widetilde{v},\widetilde{v}')\in\mathcal{E}^+\}\).

## 5.2 Segmentation and (Explicit and Implicit) Cycles: One-Dimensional Case

For simplicity, we first consider the case where \(\widetilde{f}(\widetilde{x})=f(\widetilde{x}):\mathbb{Z}^n\rightarrow\mathbb{Z}\) is a one- dimensional ranking function. Our aim is to find a ranking function \(f(\widetilde{x})\) for E<sup>+</sup>, which satisfies \(\forall(\widetilde{v},\widetilde{v}')\in\mathcal{E}^+\). \(f(\widetilde{v})>f(\widetilde{v}')\) and \(\forall(\widetilde{v},\widetilde{v}')\in\mathcal{E}^+\). \(f(\widetilde{v})\ge 0\). If our ranking function synthesizer finds such a ranking function \(f(\widetilde{x})\), then a candidate well-founded relation _R<sub>f</sub>_ is constructed as \(R_f(\widetilde{x},\widetilde{x}'):=f(\widetilde{x})\ge 0\wedge f(\widetilde{x})>f(\widetilde{x}')\).

Our synthesizer builds a decision tree _D_ to find a ranking function \(f_D(\widetilde{x})\) for E<sup>+</sup>. The main question in doing so is "when and how should we refine partitions of decision trees?" To answer this question, we consider the case where there is no ranking function \(f_D(\widetilde{x})\) for E<sup>+</sup> with a fixed segmentation _S_, and classify reasons for this into three cases as follows.

_Case 1: explicit cycles in examples._ We define an _explicit cycle_ in E<sup>+</sup> as a cycle in the graph (Z_<sup>n</sup>,_E<sup>+</sup>). An explicit cycle witnesses that there is no ranking function for E<sup>+</sup> (see e.g., Example 4).

_Case 2: non-crossing examples are unsatisfiable._ The second case is when there is a leaf \(L\in S\) such that no affine (not _piecewise_ affine) ranking function for the set \(\mathcal{E}_{L,L}^+\) of non-crossing examples exists. This prohibits the existence of piecewise affine function \(f_D(\widetilde{x})\) for E<sup>+</sup> with segmentation _S=S(D_) because the restriction of \(f_D(\widetilde{x})\) to \(L\in S\) must be an affine ranking function for \(\mathcal{E}_{L,L}^+\).

_Case 3: implicit cycles in the dependency graph._ We define an _implicit cycle_ by a cycle in the dependency graph _G(S,_E<sup>+</sup>). Case 3 is the case where an implicit cycle prohibits the existence of piecewise affine ranking functions for E<sup>+</sup> with the segmentation _S_ (e.g., Example 5). If Case 1 and Case 2 do not hold but

