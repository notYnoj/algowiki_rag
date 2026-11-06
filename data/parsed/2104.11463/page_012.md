<tbc>Note that some of predicate variable applications \(X(\widetilde{v})\) may not be assigned true nor false because they do not affect the evaluation of **SAT**(E). Such predicate variable applications are discarded from \(\{(\mathcal{E}_X^+,\mathcal{E}_X^-)\}_{X\in fpv(\mathcal{E})}\).

Our method uses the extraction of positive and negative examples when the validator passes examples to the synthesizer. If \(X\in fpv(\mathcal{E})\cap\mathcal{R}\), then we apply our ranking function synthesizer to \((\mathcal{E}_X^+,\mathcal{E}_X^-)\). If \(X\in fpv(\mathcal{E})\backslash\mathcal{R}\), then we apply an invariant synthesizer.

We say a candidate solution \(\sigma\) is consistent with \(\{(\mathcal{E}_X^+,\mathcal{E}_X^-)\}_{X\in fpv(\mathcal{E})}\) if \(\vDash\sigma(X)(\widetilde{v}^+)\) and \(\vDash\neg\sigma(X)(\widetilde{v}^-)\) hold for each predicate variable \(X\in fpv(\mathcal{E})\), \(\widetilde{v}^+\in\mathcal{E}_X^+\), and \(\widetilde{v}^-\in\mathcal{E}_X^-\). If a candidate solution \(\sigma\) is consistent with \(\{(\mathcal{E}_X^+,\mathcal{E}_X^-)\}_{X\in fpv(\mathcal{E})}\), then \(\sigma\) is also consistent with E.

Note that unsatisfiability of \(\{(\mathcal{E}_X^+,\mathcal{E}_X^-)\}_{X\in fpv(\mathcal{E})}\) does not immediately implies unsatisfiability of E nor (C,R) because \(\{(\mathcal{E}_X^+,\mathcal{E}_X^-)\}_{X\in fpv(\mathcal{E})}\) depends on the choice of the assignment \(\eta\). Therefore, the CEGIS architecture need to be modified: if synthesizers find unsatisfiability of \(\{(\mathcal{E}_X^+,\mathcal{E}_X^-)\}_{X\in fpv(\mathcal{E})}\), then we add the negation of an unsatisfiability core to E to prevent using the same assignment \(\eta\) again.

Note that some restricted forms of (9) have also been considered in previous work and are called implication examples in \[17\] and implication/negation constraints in \[12\]. Our extraction of positive and negative examples is applicable to the general form of (9).

## 5 Ranking Function Synthesis

In this section, we describe one of the main contributions, that is, our decision tree-based synthesizer, which synthesizes a candidate well-founded relation \(\sigma(R)\) from a finite set \(\mathcal{E}_R^+\) of examples. We assume that only positive examples are given because well-founded relations occur only positively in pwCSP for termination analysis (see Sect. 3). The aim of our synthesizer is to find a piecewise affine lexicographic ranking function \(\widetilde{f}(\widetilde{x})\) for the given set \(\mathcal{E}_R^+\) of examples. Below, we fix a predicate variable \(R\in\mathcal{R}\) and omit the subscript \(\mathcal{E}_R^+=\mathcal{E}^+\).

### 5.1 Basic Definitions

To represent piecewise affine lexicographic ranking functions, we use decision trees like the one in Figure 4. Let \(\widetilde{x}=(x_1,\dots,x_n)\) be the program variables where each _x<sub>i</sub>_ ranges over Z.

**Definition 13.** A _decision tree D_ is defined by \(D:=\widetilde{g}(\widetilde{x})|\) **if** \(h(\widetilde{x})\ge 0\) **then** _D_ **else** _D_ where \(\widetilde{g}(\widetilde{x})=(g_k(\widetilde{x}),\dots,g_0(\widetilde{x}))\) is a tuple of affine functions and \(h(\widetilde{x})\) is an affine function. A _segmentation tree S_ is defined as a decision tree with undefined leaves \(\perp\): that is, \(S:=\perp|\) **if** \(h(\widetilde{x})\ge 0\) **then** _S_ **else** _S_. For each decision tree D, we can canonically assign a segmentation tree by replacing the label of each leaf with \(\perp\). This is denoted by _S(D_). For each decision tree _D_, we denote the corresponding piecewise affine function by \(\widetilde{f}_D(\widetilde{x}):\mathbb{Z}^n\rightarrow\mathbb{Z}^{k+1}\).

