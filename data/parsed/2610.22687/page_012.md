2. Cut and Determine the functional feedback to satisfy check E2. Possible options are to Cut all coupling variables in the component except to the solvers (_S_<sub>3</sub> in Figure 9) -- Jacobi -- or use Gauss-Seidel (which requires ordering) to cut a smaller set. See Figure 9(b) for the Jacobi version that cuts both _y_<sub>1</sub> and _y_<sub>2</sub>.<tbc>

3. Reinsert the optimiser node, Combine and Nest the original solvers (root finders, _S_<sub>3</sub> in Figure 9), the obtained fixed-point conditional nodes, and the optimiser node in some way; see Figure 10 for three examples.<tbc>

4. Assign all conditional nodes compatible drivers from a set of defaults (e.g. Newton for root finders, Picard for fixed points).

The multidisciplinary-feasible architecture (MDF) is shown in Figure 10(a): the two fixed-point iterations are combined, the original solver _S_<sub>3</sub> is nested in that fixed-point iteration, which is nested in the optimiser. The individual- discipline-feasible architecture (IDF) in Figure 10(b) combines the fixed-point iterations with the optimiser while nesting _S_<sub>3</sub> in the optimiser. Finally, the simultaneous-analysis-and-design architecture (SAND) in Figure 10(c) combines all conditional nodes in the top-level optimiser.

These monolithic architectures differ only in the nesting level at which the implicit models and the coupling between models (i.e. cycles in the graph) are resolved: locally with a solver, medium-level with a multidisciplinary analysis (MDA), or globally by the optimiser. The Nest and Combine operations are how these choices are made.

J
X
X
X
Opt
X
X
X
N4
y2
y2
min
S 0
y1
S3
y1
y1
y1
FP
1
y1
FP
2
y2
y2
N1
f
y2
N4
y2
N2
g
y1
S3
y1
y1
y1
O
r3
R3
f
N1
g
N2
CUT, DETERMINE
(a)
(b)

