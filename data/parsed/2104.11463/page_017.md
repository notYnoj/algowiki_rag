<tbc>ResolveCase2, intervals and octagons satisfy \(\emptyset\neq H':=\{h(\widetilde{x})\ge 0|\exists\widetilde{v},\widetilde{u}\in\mathcal{E}'^+.h(\widetilde{v})\ge 0\wedge h(\widetilde{u})<0\}\), so Assumption 18 is satisfied by choosing the best halfspace with respect to the quality measure from \(H'\).

For each halfspace \((h(\widetilde{x})\ge 0)\in H'\), we calculate QualityMeasure in Algorithm 3, and choose one that maximizes QualityMeasure\((h,\mathcal{E}'^+)\). QualityMeasure\((h,\mathcal{E}'^+)\) calculates the sum of the maximum number of satisfiable constraints in each leaf divided by \(h(\widetilde{x})\ge 0\) plus an additional term \((|E_{+-}|+|E_{-+}|)(1-entropy(|E_{+-}|,|E_{-+}|))\) where \(entropy(x,y)=-\frac{x}{x+y}log_2\frac{x}{x+y}-\frac{y}{x+y}log_2\frac{y}{x+y}\). Therefore, the term \((|E_{+-}|+|E_{-+}|)(1-entropy(|E_{+-}|,|E_{-+}|))\) is close to |_E_<sub>+-</sub>|+|_E_<sub>-+</sub>| if almost all examples in \(E_{+-}\cup E_{-+}\) cross _h_ in the same direction and close to 0 if |_E_<sub>+-</sub>| is almost equal to |_E_<sub>-+</sub>|.

## Lazy strategy.

In the lazy strategy, we lazily generate halfspaces. We divide the current polyhedron so that non-crossing examples in the cell point to almost the same direction.

First, we label states that occur in \(\mathcal{E}_{C,C}^+\) as follows. We find a direction that most examples in _C_ point to by solving the MAX-SMT \(\vec{a}:=max_\vec{a}\big|\{(\widetilde{v},\widetilde{v}')\in\mathcal{E}_{C,C}^+|\vec{a}\cdot(\widetilde{v}-\widetilde{v}')>0\}\big|\). For each \((\widetilde{v},\widetilde{v}')\in\mathcal{E}_{C,C}^+\), we label two points \(\widetilde{v},\widetilde{v}'\) with +1 if \(\vec{a}\cdot(\widetilde{v}-\widetilde{v}')>0\) and with -1 otherwise.

Then we apply weighted C-SVM to generate a hyperplane that separates most of the positive and negative points. To guarantee termination of Algorithm 1, we avoid "useless" hyperplanes that classify all the points by the same label. If we obtain such a useless hyperplane, then we undersample a majority class and apply C-SVM again. By undersampling suitably, we eventually get linearly separable data with at least one positive point and one negative point.

Note that since coefficients of hyperplanes extracted from C-SVM are floating point numbers, we have to approximate them by hyperplanes with rational coefficients. This is done by truncating continued fraction expansions of coefficients by a suitable length.

**Phase 3** In Line 5-18 of Algorithm 1, we further refine the segmentation _S(D_) to resolve Case 3. Once Case 2 is resolved by ResolveCase2, Case 2 never holds even after refining _S(D_) further. This enables to separate Phases 2 and 3.

Given a template tree _D_, we consider the set _C_ of constraints on parameters in _D_ that claims \(\widetilde{f}_D(\widetilde{x})\) is a ranking function for E<sup>+</sup> (Line 6).

If _C_ is satisfiable, we use an SMT solver to obtain a solution of _C_ (i.e. an assignment \(\rho\) of integers to parameters) while minimizing the sum of absolute values of unknown parameters in _D_ at the same time (Line 8). This minimization is intended to give a simple candidate ranking function. The solution \(\rho\) is used to instantiate the template tree _D_ (Line 11).

If _C_ cannot be satisfied, there must be an implicit cycle in the dependency graph _G(S(D),_E<sup>+</sup>) by Theorem 17. The implicit cycle can be found in an unsatisfiable core of _C_. We refine the segmentation of _D_ to cut the implicit cycle in Line 16. To guarantee termination, we choose a halfspace satisfying the following assumption, which is similar to Assumption 18.

