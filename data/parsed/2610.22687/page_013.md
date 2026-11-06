<tbc>Although this example is simple, the same strategy can be used for an arbitrarily complex set of models, as will be done in the PROCESS case study (Section V), where exactly these recipes for MDF and SAND are used for a set of over 140 interconnected models.

Finally, these classifications are not exhaustive: an MDAO architecture can arbitrarily be built from locally and globally resolved couplings and models (e.g. the MDF architecture could as well root-find the entire Sellar system at once by combining the FP and the _S_<sub>3</sub>), which these graph operations support -- in other words, these operations make it possible to mix and match elements from any architecture (e.g. almost all couplings globally except some difficult local solves), addressing requirements 2 and 3.

## F. Summary

In engineering design and optimisation, the starting point is often a set of explicit models, implicit models (defined as a solver and a residual computation) and conditional nodes (which include both consistency constraints and optimality conditions).

If these are all built from pure functions with explicit inputs and outputs, they define a dependency graph of which the validity can be checked using checks G1 to G3. This graph yields a valid execution order in terms of components: either a single function (in which case it can be executed), or a component with multiple functions and conditional nodes (cyclic), in which case it has to be resolved.

The graph operations (Cut, Determine, Nest, Combine, Assign) can be used to manipulate the graph until the executability checks E1 to E4 pass. Finally, as shown in Section IIIE, sequences of graph operations can be used to automatically assign an MDAO architecture; the graph operations can then be used to modify these standard options to better suit the problem at hand.

This graph-based theory addresses requirements 1 to 3: arbitrary design problems (e.g. different design variables are supported by changing the unknowns of the optimiser) can be used, an automated MDAO architecture can be defined for any design problem, and this can be flexibly modified using graph operations. Requirements 4 and 5 are addressed in the following section, which discusses the implementation of the graph-based theory in `cottax`.

