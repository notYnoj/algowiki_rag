<tbc>The model time (excluding driver-internal overhead and computations) of the `cottax` port is two to three orders of magnitude faster for the optimisation configurations, and for `stellarator\_helias` a significant part of this difference is shown to be gained by removing per-model dispatch and graph-traversal overhead (requirement 5). This demonstrates graph-based flexibility and computational efficiency for a large number of low-fidelity models using `cottax`.

## VI. DISCUSSION

Fusion reactor design, and in particular stellarator design, requires integrated analysis and optimisation using increasingly high-fidelity models. To keep the future stellarator MDAO framework flexible and modular, we proposed a generic coordination and execution core which addresses the requirements given in Section IA with a two-layered approach.

The graph-based coordination layer aims to satisfy requirements 1 to 3, while the JAX-based execution layer addresses requirements 4 and 5. We will discuss each requirement and how it is addressed here and provide limitations and future work.

### A. Design problem agnostic

Requirement 1 is addressed by using functionally pure models in a generalised dependency graph. Parametrisations are also a node in the graph (e.g. a function that determines the analysis geometry as a function of major radius). A different problem formulation is an optimiser node with different unknowns; e.g. the optimiser determining a major radius or a magnetic field strength. The generality of this dependency graph ensures that no particular selection is enforced.

This does require a functionally pure set of models and parametrisations. For existing design frameworks this may require porting (as in PROCESS), but for future development, we would argue this is good practice in any case. By forcing explicit interfaces between models of subsystems it removes hidden dependencies that are also difficult to order, coordinate, and interpret manually.

### B. Automated coordination

The standard MDAO architecture recipes of Sections IIIE and IVG enable automated coordination for arbitrary design problems; for an acyclic set of models the topological ordering alone enables this. This has been shown concretely in the PROCESS results: for different model collections -- the tokamak and stellarator have vastly different model sets -- and various problem formulations (different design variables, objectives, and constraints) the MDAO architecture can be defined and run automatically.

The implemented monolithic MDAO architectures might not be the most efficient (see also requirement 3), and additional architectures might be desirable as standard recipes. In particular, no distributed architectures [58] have been implemented. We propose they can however be obtained by sequences of the graph operations of Section IIID with additional functional nodes and conditional nodes.

### C. Flexible MDAO architectures

The graph operations of Section IIID can be used to define a highly customised MDAO architecture with arbitrarily deeply nested solves or optimisers.

The additional solver flexibility enabled by the graph operations is only relevant for cases where the standard MDAO architectures do not yield sufficient performance. This has not been shown in this paper yet: all applied MDAO architectures are one of the standard approaches. However,  III does demonstrate that the difference in performance can be significant between architectures.

Also, while the graph operations allow for customised MDAO architecture, there currently is no built-in check that guarantees the solved design optimisation problem is equal to the desired one. A possible future avenue to obtain such a check is to consider the fundamental problem graph [26] and from there restrict the graph operations to a solution-set-preserving subset.

