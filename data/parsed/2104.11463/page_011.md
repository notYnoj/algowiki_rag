## Synthesizer.

The input for a synthesizer is a set E of examples of C collected from previous CEGIS iterations. The synthesizer tries to find a candidate solution \(\sigma\) consistent with E instead of a genuine solution for (C,R). If the candidate solution \(\sigma\) is found, then \(\sigma\) is passed to the validator. If E is unsatisfiable, then E witnesses unsatisfiability of (C,R). Details of our synthesizer is described in Sect. 5.

## Validator.

A validator checks whether the candidate solution \(\sigma\) from the synthesizer is a genuine solution of (C,R) by using SMT solvers. That is, satisfiability of \(\vDash\neg\wedge\sigma(\mathcal{C})\) is checked. If \(\vDash\neg\wedge\sigma(\mathcal{C})\) is not satisfiable, then \(\sigma\) is a genuine solution of the original pwCSP (C,R), so the validator accepts this. Otherwise, the validator adds new examples to the set E of examples. Finally, the synthesizer is invoked again with the updated set E of examples.

If \(\vDash\neg\wedge\sigma(\mathcal{C})\) is satisfiable, new examples are constructed as follows. Using SMT solvers, the validator obtains an assignment \(\theta\) to term variables such that \(\vDash\neg\theta(\psi)\) holds for some \(\psi\in\sigma(\mathcal{C})\). By (4), \(\vDash\neg\theta(\psi)\) is a clause of the form \(\vDash\neg\theta(\phi)\wedge\big(\wedge_{i=1}^\ell\neg\sigma(X_i)(\theta(\widetilde{t}_i))\big)\wedge\big(\wedge_{i=\ell+1}^m\sigma(X_i)(\theta(\widetilde{t}_i))\big)\). To prevent this counterexample from being found in the next CEGIS iteration again, the validator adds the following example to E.

\(\vee_{i=1}^\ell X_i(\theta(\widetilde{t}_i))\vee\vee_{i=\ell+1}^m\neg X_i(\theta(\widetilde{t}_i))\) (9)

The CEGIS architecture repeats this interaction between the synthesizer and the validator until a genuine solution for (C,R) is found or E witnesses unsatisfiability of (C,R).

## Extraction of positive/negative examples.

Examples obtained in the above explanation are a bit complex to handle in our decision tree-based synthesizer: each example in E is a disjunction (9) of literals, which may contain multiple predicate variables.

To simplify the form of examples, we extract from E the sets \(\mathcal{E}_X^+\) and \(\mathcal{E}_X^-\) of _positive examples_ (i.e., examples of the form \(X(\widetilde{v})\)) and _negative examples_ (i.e., examples of the form \(\neg X(\widetilde{v})\)) for each \(X\in fpv(\mathcal{E})\). This allows us to synthesize a predicate \(\sigma(X)\) for each predicate variable \(X\in fpv(\mathcal{E})\) separately. For simplicity, we write \(\widetilde{v}\in\mathcal{E}_X^+\) and \(\widetilde{v}\in\mathcal{E}_X^-\) instead of \(X(\widetilde{v})\in\mathcal{E}_X^+\) and \(\neg X(\widetilde{v})\in\mathcal{E}_X^-\).

The extraction is done as follows. We first substitute for each predicate variable application \(X(\widetilde{v})\) in E a boolean variable \(b_{X(\widetilde{v})}\) to obtain a SAT problem **SAT**(E). Then, we use SAT solvers to obtain an assignment \(\eta\) that is a solution for **SAT**(E). If a solution \(\eta\) exists, then we construct positive/negative examples from \(\eta\); otherwise, E is unsatisfiable.

**Definition 12.** Let \(\eta\) be a solution for **SAT**(E). For each predicate variable \(X\in fpv(\mathcal{E})\), we define the set \(\mathcal{E}_X^+\) of _positive examples_ and the set \(\mathcal{E}_X^+\) of _negative examples_ under the assignment \(\eta\) by \(\mathcal{E}_X^+:=\{\widetilde{v}|\eta(b_{X(\widetilde{v})})=\text{\textbf{true}}\}\) and \(\mathcal{E}_X^-:=\{\widetilde{v}|\eta(b_{X(\widetilde{v})})=\text{\textbf{false}}\}\).

