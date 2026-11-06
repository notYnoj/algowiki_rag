## D. Full workflow

A collection of models and nesting edges defines a dependency graph, which is considered valid if checks G1 to G3 pass. If these do not pass, the set of models has to be changed or the problematic nesting edges have to be removed. Then, for a fully executable graph, checks E1 to E4 have to be satisfied: a valid graph can be converted to an executable graph by using the graph operations Cut (check E2), Determine (check E1), Nest or Combine (check E4), and Assign (check E3).

The full workflow for turning a set of models and additional conditional nodes (such as optimality conditions or consistency constraints) into an executable dependency graph is shown in Figure 8. This does not have to be as linear as shown here: the graph contains functions and conditional nodes with or without unknowns and drivers at the same time; this is merely an order that is commonly encountered. It is possible to determine new design variables after obtaining an executable graph or start with already assigned drivers for e.g. implicit models. Finally, note that a set of acyclic functions with non-overlapping outputs would pass all checks immediately and is simply ordered and executed.

The workflow of Figure 8 can be used for arbitrary models and can create a highly customised MDAO architecture (addressing requirements 1 and 3). However, a sequence of manually chosen graph operations applies to one set of models and has to be redone whenever the design problem changes; requirement 2 would require at least an automated starting point for an MDAO architecture. This is the topic of the next section.

Figure 8: Schematic workflow of obtaining an executable graph from a set of functions and conditional nodes -- all checks need to pass before executing. First, the dependency graph implied by this set is checked for validity by checks G1 to G3 (if it is not valid, the declarations need to be amended), and its TOSCC is computed. Function cycles (functions depending on each other’s output) have to be Cut (which adds a conditional node, check E2), conditional nodes without unknowns that they depend on have to be Determined (check E1), conditional nodes sharing a component have to be correctly nested or combined (check E4), and finally conditional nodes without a driver need to be assigned one (check E3). Each operation amends the declarations, after which the checks are repeated. If all checks pass, the graph can be executed. The order does not have to be the one drawn: each conditional node is independent and could be assigned a driver before a function cycle is cut. Furthermore, an acyclic set of functions (without conditional nodes) would immediately pass all checks and can be executed after TOSCC.

## E. MDAO architectures as graph operations

Such starting points can be provided by the standard architectures in the MDAO literature [16]. Monolithic architectures (with a single top-level optimisation problem) can be implemented in terms of rule-based sequences of the graph operations in Figure 8, allowing for immediately and automatically obtaining an executable graph for any given design optimisation problem. After this, the graph operations can be used to modify this basic architecture to increase efficiency or convergence properties. Distributed architectures [58] require inserting additional functional nodes and optimisers; monolithic architectures do not.

The recipe for a monolithic architecture will be illustrated using the extended Sellar problem, where the _N_<sub>3</sub> explicit function is replaced by an implicit function (a residual _r_<sub>3</sub> and a root-find condition determining _y_<sub>1</sub> from that residual) and an optimiser minimises _f_ with \(g\le 0\) by varying _x_. This is shown without the optimiser in Figure 9(a).

1. Remove the optimiser and compute the TOSCC to find the couplings within each optimiser iteration.

CUT fig. 4(b)
DETERMINE fig. 6
NEST. Combine fig. 7
ASSIGN fig. 4(d)
declared at any stage
no
no
no
no
no
conditional nodes no unknowns
valid graph? G1-G3
graph TOSCC
functionally acyclic? E2
yes
conditions determined? E1
yes
valid nesting? E4
drivers assigned? E3
yes
execute
conditional nodes with unknowns
conditional nodes with driver
no

