<tbc>Since these functions are pure, only the output (first column) and inputs (second column, arguments) need to be considered for the dependency graph, shown in Figure 2a, where I are the inputs (no function produces these values) and O the outputs (no function uses these values as inputs).

For a valid dependency graph, we require:

**Check G1 (One producer per variable)** _No two nodes produce the same output variable: otherwise, the answers would be different depending on which function executed first._

**Check G2 (No self-reads)** _No node takes its own output variables as inputs: such a function cannot be executed without recursion (whose termination criteria cannot be read off the graph)._

A dependency graph can also be visualised in an adjacency matrix, by a matrix with each node on the diagonal<sup>1</sup> and a non-zero entry off the diagonal at _ij_ if function _i_ outputs that variable and function _j_ takes it as input, shown in Figure 2b.

This particular graph admits a (non-unique) ordering in which each function can be evaluated: _N_<sub>3</sub>_,N_<sub>1</sub>_,N_<sub>2</sub>. In general, such an ordering can be generated automatically using a topological ordering algorithm. The adjacency matrix has an implicit ordering from top-left to bottom-right, and the topological ordering can thus be visualised in Figure 2c. After topological ordering, there is no variable under the diagonal, indicating no feedback and thus a valid feed-forward execution order. However, not every graph can be topologically ordered; adding the function

\(y_2=N_4(x,y_1)=\sqrt{y_1}+x_2+x_3\) (2)

to the system of Equation (1) yields the cyclic dependency graph shown in Figure 3a. This graph cannot be topologically ordered directly, but a strongly connected components (SCC) algorithm yields a set of components (sets of mutually dependent nodes or a single node) that can be topologically ordered (topologically ordered strongly<tbc>

<sup>1</sup> Since self-reads are excluded (check G2), there are no self-loops so the diagonal can be used to display the function name itself. Furthermore, we expand the input/output nodes to fully show the variable names there too; this is not standard and as such they are differently coloured. This is similar to the XDSM [35] but that focuses on the final executable graph instead of the intermediate representations used here -- it does not have a convention for the conditional nodes in Section IIIB nor for the nesting. Finally, the graph is always shown fully sequenced (topologically ordered strongly connected components) except in Figures 2b and 3b

J
X
X
N3
X
y1
y2
y1
X
N4
y1
N2
y2
g
N1
f
O

J
X
X
X
N1
f
N2
g
y1
y1
N3
y1
y2
y2
N4
O

J
X
X
X
N3
y1
y1
y1
y2
N4
y2
N1
f
N2
g
O

(a)

(b)

(c)

Figure 3: The cyclic dependency graph given by the system of Equation (1) with the additional node of Equation (2) in node-linking format (a) and adjacency matrix format (b). Such cyclic graphs do not admit a feed-forward ordering, but their strongly connected components can be topologically ordered to yield an execution order in terms of components (sets of mutually dependent models or a single function), shown in (c). The one multi-function component (_N_<sub>3</sub>_,N_<sub>4</sub>) is grouped in a shaded region -- no feedback is present from component to component, only within the shaded component.

