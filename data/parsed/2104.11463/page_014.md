<tbc>no piecewise affine ranking function for E<sup>+</sup> with the segmentation _S_ exists, then there must be an implicit cycle by (the contraposition of) the following proposition.

**Proposition 16.** _Assume_ E<sup>+</sup> _is a set of examples that does not contain explicit cycles (i.e. Case 1 does not hold). Let S be a segmentation tree and assume that for each_ \(L\in S\)_, there exists an affine ranking function_ \(f_L(\widetilde{x})\) _for_ \(\mathcal{E}_{L,L}^+\) _(i.e. Case 2 does not hold). If the dependency graph G(S,_E<sup>+</sup>) _is acyclic, then there exists a decision tree D with the segmentation S(D_)=_S such that_ \(f_D(\widetilde{x})\) _is a ranking function for_ E<sup>+</sup>.

_Proof._ By induction on the height (i.e. the length of a longest path from a vertex) of vertices in _G(S,_E<sup>+</sup>). We construct a decision tree _D_ as follows. If the height of \(L\in S\) is 0, then we assign \(f'_L(\widetilde{x}):=f_L(\widetilde{x})\) to the leaf _L_ where \(f_L(\widetilde{x})\) is a ranking function for \(\mathcal{E}_{L,L}^+\). If the height of \(L\in S\) is _n\>_0, then we assign \(f'_L(\widetilde{x}):=f_L(\widetilde{x})+c\) to the leaf _L_ where \(c\in\mathbb{Z}\) is a constant that satisfies \(\forall(\widetilde{v},\widetilde{v}')\in\mathcal{E}_{L,L^\prime}^+,f_L(\widetilde{v})+c>f'_{L^\prime}(\widetilde{v}')\) for each cell \(L'\) with the height less than _n_. \(\sqcap\sqcup\)

Note that the converse of Proposition 16 does not hold: the existence of implicit cycles in _G(S,_E<sup>+</sup>) does not necessarily imply that no piecewise affine ranking function exists with the segmentation _S_.

## 5.3 Segmentation and (Explicit and Implicit) Cycles: Multi-Dimensional Lexicographic Case

We consider a more general case where \(\widetilde{f}(\widetilde{x})=(f_k(\widetilde{x}),\dots,f_0(\widetilde{x}))\) is a multi- dimensional lexicographic ranking function and _k_ is a fixed nonnegative integer.

Given a function \(\widetilde{f}(\widetilde{x})\), we consider the well-founded relation \(R_\widetilde{f}(\widetilde{x},\widetilde{x}')\) defined inductively as follows.

\(R_{()}(\widetilde{x},\widetilde{x}'):=\perp R_{(f_k,\dots,f_0)}(\widetilde{x},\widetilde{x}'):=f_k(\widetilde{x})\ge 0\wedge f_k(\widetilde{x})>f_k(\widetilde{x}')\) (10)

\(\vee f_k(\widetilde{x})=f_k(\widetilde{x}')\wedge R_{(f_{k-1},\dots,f_0)}(\widetilde{x},\widetilde{x}')\)

Our aim here is to find a lexicographic ranking function \(\widetilde{f}(\widetilde{x})\) for E<sup>+</sup>, i.e. a function \(\widetilde{f}(\widetilde{x})\) such that \(R_\widetilde{f}(\widetilde{v},\widetilde{v}')\) holds for each \((\widetilde{v},\widetilde{v}')\in\mathcal{E}^+\). Our synthesizer does so by building a decision tree. The same argument as the one-dimensional case holds for lexicographic ranking functions.

**Theorem 17 (cycle detection).** _Assume_ E<sup>+</sup> _is a set of examples that does not contain explicit cycles. Let S be a segmentation tree and assume that for each_ \(L\in S\)_, there exists an affine function_ \(f_L(\widetilde{x})\) _that satisfies_ \(\forall(\widetilde{v},\widetilde{v}')\in\mathcal{E}_{L,L}^+,R_{\widetilde{f}_L}(\widetilde{v},\widetilde{v}')\)_. If the dependency graph G(S,_E<sup>+</sup>) _is acyclic, then there exists a decision tree D with the segmentation S(D_)=_S such that_ \(R_{\widetilde{f}_D}(\widetilde{v},\widetilde{v}')\) _holds for each_ \((\widetilde{v},\widetilde{v}')\in\mathcal{E}^+\).

_Proof._ The proof is almost the same as Proposition 16. Here, note that if \(\widetilde{f}'(\widetilde{x})=\widetilde{f}(\widetilde{x})+\widetilde{c}\) where \(\widetilde{c}\) is a tuple of nonnegative integer constants, then \(R_{\widetilde{f}^\prime}(\widetilde{x},\widetilde{x}')\) subsumes \(R_\widetilde{f}(\widetilde{x},\widetilde{x}')\). \(\sqcap\sqcup\)

