<tbc>connected components, TOSCC) -- an execution order is then in terms of these components. For this system, this yields

\((N_3,N_4),N_1,N_2\) (3)

where only the first component is cyclic and has multiple nodes. Each cycle in the graph indicates a consistency requirement and thus the need to solve it in some way.

Summarising, if a set of pure functions and their input/outputs are defined, a dependency graph can be assembled and checked for validity (checks G1 and G2). Its TOSCC then yields a valid execution order if acyclic, and otherwise a sequence of components, each a single function or a cycle that requires resolving (e.g. by some form of solver).

## B. Conditional nodes

The Sellar example cannot be run directly due to its cycle (indicated by the broken component outline in Figure 3c). Although in this simple example it can be simply iterated until it is converged, we use this as an opportunity to introduce the _conditional node_ extension to the dependency graph which provides a useful unification of solvers and optimisers.

A conditional node imposes a condition on some variables and may own variables (its _unknownns_) that it can vary to satisfy those conditions. These conditional nodes can (given they have unknowns and a _driver_) iterate their strongly connected component in order to satisfy their conditions -- in contrast to functions which may only execute themselves. For an executable graph, the following checks are then required to pass:

**Check E1 (Conditions determined)** _Every conditional node has to have unknowns that its conditions depend on: otherwise, it cannot ensure that its conditions are satisfied when the graph is executed._

**Check E2 (Functionally acyclic)** _Only conditional nodes may receive feedback: once they are removed, the graph has to be acyclic as functions cannot make feedback consistent._

**Check E3 (Drivers assigned)** _Every conditional node is assigned a compatible driver (one that can satisfy the condition: an optimiser driver on an optimisation-type condition), which varies its unknowns until its conditions are satisfied._

In the Sellar example, a functional node has feedback in its SCC, and this has to be converted to a graph with a conditional node obtaining that feedback and a driver iterating it. The chain of operations doing so is shown in Figure 4.

