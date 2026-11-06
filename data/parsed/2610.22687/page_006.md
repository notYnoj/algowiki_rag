## III. THEORY FOR GRAPH-BASED COORDINATION AND EXECUTION

This section describes how the graph-based approach of `cottax` can turn a set of functions or models into an executable analysis that can be reconfigured with simple graph operations (requirements 1 to 3). First, well-known material concerning pure functions, dependency graphs, orderings, and visualisations of such graphs is covered in Section IIIA. Then, the extensions of the dependency graph by conditional nodes and nesting edges are discussed in Sections IIIB and IIIC. The checks an executable graph must pass are then given in Section IIID. Finally, Section IIIE shows how monolithic MDAO architectures can be obtained from a set of simple graph operations.

Mathematical detail is kept to a minimum; formal definitions of both the node types and the executability criteria are instead given in Appendix A together with a comparison to similar graph-based MDAO approaches \[26, 56\].

### A. Pure functions and dependency graphs

Pure functions are referentially transparent functions without any side effects: they do not mutate or read global state, they do not mutate their inputs, do not write to files or to the terminal, and only return an output that is solely dependent on its inputs. The execution of a function therefore cannot affect the execution of another function unless through its inputs.

Given two functions _N<sub>i</sub>_ and _N<sub>j</sub>_, we can therefore reason that _N<sub>i</sub>_ only depends on _N<sub>j</sub>_ if its inputs _I<sub>i</sub>_ contain an element of the outputs _O<sub>j</sub>_ of _N<sub>j</sub>_. If not, _N<sub>i</sub>_ is free to execute before _N<sub>j</sub>_, and moreover, if _N<sub>j</sub>_ conversely does not depend on _N<sub>i</sub>_, they can be executed in parallel. Such a dependency structure can be formalised in a computational dependency graph (hereafter, dependency graph) with the pure functions as nodes, connected by directed edges labelled by the variables.

As an example, consider the following set of pure functions (derived from the Sellar problem \[57\]):

\(f=N_1(x,y_1,y_2)=x_1^2+x_3+y_1+e^{-y_2}g=N_2(y_1)=3.16-y_1y_1=N_3(x,y_2)=x_2^2+x_3+x_1-0.2y_2\) (1)

J
X, y2
X, y2
N3
y1
y1
N1
N2
f
g
O

X
X
J
y2
y2
N1
f
N2
g
y1
y1
N3
O

X
X
J
y2
y2
N3
y1
y1
N1
f
N2
g
O

(a)

(b)

(c)

Figure 2: The dependency graph given by the system of Equation (1) in node-linking format (a) and the adjacency matrix (b). Inputs (not produced by any function) are denoted by the node I, and outputs (not used as input by any function) by O. The topologically sorted adjacency matrix (using as ordering top-left to bottom-right) is shown in (c), where an absence of variables under the diagonal after ordering indicates an acyclic graph.

