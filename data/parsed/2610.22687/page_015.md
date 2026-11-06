## A. Relational

Relational conditional node types unify common types of MDAO solvers in one node type that can be combined and classified.

A relation is defined as comparing two quantities in the graph (e.g. _a=b_ or \(a\le b\), where _b_ is either another variable or a number) and the conditional node type combines these relations into one node type.

Conditional nodes can then be classified by their relations and objective once the unknowns are chosen as in  II. These conditions can be simply combined by adding the set of relations, unknowns, and objective(s), which may change their classification and thus their compatible drivers.

II: Relational conditional nodes classified as a problem type by the relations and objective in their condition. _x_ is the unknown (one or more); _a_, _b_ and _f_ are variables that depend on _x_ through the nodes between them (note these can all be written as _c(x_)=0 on the right-hand side without loss of generality). \(\checkmark\): present, (\(\checkmark\)): may be present. Fixed point and root find only differ in that the unknown _x_ is present directly in the fixed-point problem.

## B. Ordinary differential equations

Ordinary differential equations can be computed algebraically (using a residual-like formulation) using the relational conditional node types through collocation (see e.g. Dymos \[59\]), but this module implements a rate conditional node type for initial value problem integration.

This conditional node satisfies its condition when it has integrated this rate to the specified final time (by iterating its subgraph). The trajectory can be optionally returned. Solvers such as Diffrax \[60\] can then be used. These conditional node types can be used within the same dependency graph (e.g. a root find can be nested in a rate cycle).

## C. PyTree

A PyTree \[30\] is an arbitrarily nested hierarchical Python data structure. Each segment is then an index in a data structure (e.g. a `DictKey` for a dictionary key, a `GetAttrKey` for attribute access, and a `SequenceKey` for list and tuple indexing). Both node labels and variable places are then in terms of the PyTree keys, enabling the use of any Python structure built off of the primitive indexes (and others can be added) for both the function definition tree and the data structure.

## D. Exporting

The graph is in all cases a set of labelled nodes with input and output names and the nesting edges, possibly with some implementation object, and can be readily exported. Currently, two exports are available: a standard pickle, and a JSON that serialises the entire graph to strings.

The pickle and JSON are designed to be lossless: a graph can be exported and then reloaded (to separate construction of the graph from execution or visualisation). For executable graphs, this requires the implementations to be constructible from a reference (i.e. forbidding closures, unnamed lambdas, and local functions). Non-Python functions (e.g. references to functions in different languages or repository locations) can be used and exported as long as they are serialisable; this is useful as a starting point for exporting to different execution or inspection backends in the future.

<sup>a</sup> Jacobi and Gauss-Seidel are not drivers but rather a different dependency graph: they differ in the readers of the copy \(\hat{y}_2\): for Jacobi all, for Gauss-Seidel only the minimal set for a particular ordering.

\begin{tabular}{cccccc}
 & \multicolumn{3}{c}{Relations} & Objective & \\
Problem & _x=b(x_) & _a(x_)=_b(x_) & \(a(x)\le b(x)\) & min_f(x_) & Drivers (examples) \\
Fixed point & \(\checkmark\) & & & & Picard, Anderson<sup>a</sup> \\
Root find & & \(\checkmark\) & & & Newton, Broyden \\
Feasibility & & (\(\checkmark\)) & \(\checkmark\) & & constrained optimiser, no objective \\
Unconstrained optimisation & & & & \(\checkmark\) & BFGS, Nelder-Mead \\
Constrained optimisation & & (\(\checkmark\)) & (\(\checkmark\)) & \(\checkmark\) & SLSQP, VMCON, IPOPT \\
\end{tabular}

