<tbc>**Algorithm 1** Building decision trees.

**Input:** a set E<sup>+</sup> of examples, an integer \(k\ge 0\)<br>
**Output:** a well-founded relation R such that \(\forall(\widetilde{x},\widetilde{x}')\in\mathcal{E}^+,R(\widetilde{x},\widetilde{x}')\)<br>
1: **if** E has a cycle **then**<br>
2: **return** unsatisfiable<br>
3: **end if**<br>
4: D:= ResolveCase2(E)<br>
5: **while** true **do**<br>
6: C:= GetConstraints(D,E)<br>
7: O:= SumAbsParams(D)<br>
8: \(\rho:=\) Minimize(O,C)<br>
9: **if** \(\rho\) is defined **then**<br>
10: \(\widetilde{f}(\widetilde{x}):=\widetilde{f}_{\rho(D)}(\widetilde{x})\)<br>
11: **return** \(R_\widetilde{f}\)<br>
12: **else**<br>
13: get an unsat core in C<br>
14: find an implicit cycle \((\widetilde{v}_1,\widetilde{v}'_1),\dots,(\widetilde{v}_l,\widetilde{v}'_l)\) in the unsat core<br>
15: find a cell C and two distinct points \(\widetilde{v}'_i,\widetilde{v}_{i+1}\in C\) in the implicit cycle<br>
16: add a halfspace to separate \(\widetilde{v}'_i\) and \(\widetilde{v}_{i+1}\) and update D<br>
17: **end if**<br>
18: **end while**

## 5.4 Our Decision Tree Learning Algorithm

We design a concrete algorithm based on Theorem 17. It is shown in Algorithm 1 and consists of three phases. We shall describe the three phases one by one.

**Phase 1** Phase 1 (Line 1-3) detects explicit cycles in E<sup>+</sup> to exclude Case 1. Here, we use a cycle detection algorithm for directed graphs.

**Phase 2** Phase 2 (Line 4) detects and resolves Case 2 by using ResolveCase2 (Algorithm 2), which is a function that grows a decision tree recursively. ResolveCase2 takes non-crossing examples in a leaf, divides the leaf, and returns a _template tree_ that is fine enough to avoid Case 2. Here, template trees are decision trees whose leaves are labeled by affine templates.

Algorithm 2 shows the detail of ResolveCase2. ResolveCase2 builds a template tree recursively starting from the trivial segmentation \(S=\perp\) and all given examples. In each polyhedron, ResolveCase2 checks whether the set C of constraints imposed by non-crossing examples can be satisfied by an affine lexicographic ranking function on the polyhedron (Line 2-3). If the set C of constraints is not satisfiable, then ResolveCase2 chooses a halfspace \(h(\widetilde{x})\ge 0\) (Line 6) and divides the current polyhedron by the halfspace.

There is a certain amount of freedom in the choice of halfspaces. To guarantee termination of the whole algorithm, we require that the chosen halfspace h separates at least one point in \(\underline{\mathcal{E}'^+}:=\{\widetilde{v}|(\widetilde{v},\widetilde{v}')\in\mathcal{E}'^+\}\cup\{\widetilde{v}'|(\widetilde{v},\widetilde{v}')\in\mathcal{E}'^+\}\) from the other points in \(\underline{\mathcal{E}'^+}\). That is:

