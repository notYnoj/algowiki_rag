## A Mathematical Results and Supporting Evidence

This appendix records the twelve numerical result families and the Tuza theorem presented in the report. Numerical entries state the new bound, its previous record, and the final artifact that supports it. The Tuza entry explains the finite reduction and certificates behind Theorem 1. The four Cohn–Elkies dimensions, five _B<sub>h</sub>[g_] coefficients and two quantum channels each count as separate parameter settings in the 20 numerical records.

### A.1 Relevant Variables of Boolean Functions

The record bound on Wellens’ quantity \(D_\infty\) decreases from 4.3935 to 4.3654674227 (Wellens, 2020). This quantity controls the number of relevant variables relative to Boolean-function degree. The finite computation retains an exact infeasibility certificate and a rational feasibility witness for each degree from 1 to 48. The published formulation combines these per-degree certificates into the bound on \(D_\infty\).

### A.2 Cohn–Elkies Linear Programming

The final dual vectors establish the lower bounds in  2, using Li’s discrete reduction (Li, 2022). Each dimension has a retained vector and an exact bound expression. The comparison with three-point packing upper bounds (Cohn et al., 2022) establishes the separation in dimensions 10 and 11 described in Section 5.2. These values bound the optimum of the Cohn–Elkies program from below.

### A.3 Spencer Discrepancy Constant

For an \(n\times n\) real matrix _A_ with entries of magnitude at most one, define

\(\mathrm{disc}(A)=\mathrm{min}_{\varepsilon\in\{-1,1\}^n}\|A\varepsilon\|_\infty.\)

An explicit \(8\times 8\) matrix in the collection has discrepancy five. Exhausting all 256 sign assignments verifies this value. It yields the lower bound \(5/\sqrt{8}\approx 1.767767\) on the universal constant in the square-matrix discrepancy problem, improving the reference \(7/\sqrt{17}\approx 1.697749\) (Tao et al., 2026). The final artifact is the matrix itself.

### A.4 Dimer Entropy in Three Dimensions

The record upper bound on the per-site entropy of perfect matchings of the cubic lattice decreases from 0.452130 to 0.452010, extending the transfer-operator computation of He (2026). The retained positive integer vectors satisfy the transfer-operator inequalities. Evaluating the resulting logarithm gives approximately 0.452009597554483. The stated bound is rounded upward.

### A.5 The _n_-Queens Constant

The final lower and upper witnesses have resolutions 65,536 and 4,096, respectively. Rational feasibility checks and directed rounding give Equation (4). The interval is approximately 84 times narrower than the comparator from Nobel et al. (2023). Both witnesses are retained, so the two sides can be checked separately.

### A.6 Ramsey Multiplicity _c_<sub>4,5</sub>

A graph on 1,024 vertices changes the record upper bound from

\(\frac{2129191}{2^{28}}\text{to}\frac{4427841832181}{2^{49}}.\)

This is the asymmetric multiplicity problem involving a clique of order four in one color and a clique of order five in the other, following Parczyk et al. (2022a). The exact reference value is computed from the published 128-vertex graph in the accompanying dataset (Parczyk et al., 2022b). The final graph preserves the construction. A separate exact enumeration checks the graph and its complement.



