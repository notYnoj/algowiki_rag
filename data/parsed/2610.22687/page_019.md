## V. PROCESS

PROCESS [2, 3, 14] is a fusion systems code with more than 140 interconnected models (differs per specific run) that are mostly scalar arithmetic. This provides a compelling test case for the graph-based coordination and execution core: complex interdependencies with very fast single models.

This required PROCESS to be converted to a purely functional collection of models. We converted, and in some cases split up, all models using LLM agents (Claude Sonnet 4.6 in most cases), testing each model against the existing PROCESS model extensively, including autodiff vs PROCESS’s native finite differences. Some non-differentiable functions were smoothed slightly to obtain a differentiable version, taking care that this does not affect the result.

We then reproduced the input file optimisation runs to within reasonable tolerances (≈10<sup>-3</sup>) using the `cottax` JAX execution layer (and the MDAO architectures in Section IIIE), which gives us confidence that it is correctly ported.

In this section, first, the collection of PROCESS models is sequenced for both a tokamak and a stellarator configuration, and the MDAO architectures are applied to this collection of models. Then, some iteration, convergence, and performance characteristics are shown of the ported models including a comparison with the base PROCESS code for different MDAO architectures.

### A. Sequencing and MDAO architecture

PROCESS contains models for both stellarators and tokamaks but also several device-agnostic models used for both. We consider the `stellarator\_helias` (stellarator) and `low\_aspect\_ratio\_DEMO` (tokamak) example input files here -- these select a subset of the total models and pick which constraints to include and the design or iteration variables to vary.

In Figure 14 the adjacency matrix of the tokamak is shown (similar to the figures in Section III but without variable or node names in the graph and only one edge per coupling), coloured by the model provenance (e.g. physics, buildings, or coils) and ordered per provenance (without any graph operations to make it executable). The non-sparsity below the diagonal indicates many coupling models in this particular run order. However, after a TOSCC of this graph, shown in Figure 14(b), only very few cyclic components remain, and moreover, they are very small.

PROCESS itself runs a large fixed-point iteration over almost all its models -- this shows that with targeted ordering and solving, it can be reduced to only three small blocks of 4, 8, and 9 nodes (of a total of 242 here). Moreover, they<tbc>

(a) ordered by provenance
(b) ordered by structure
initialisation
tokamak
physics
power
buildings
vacuum
availability
costs

Figure 14: The tokamak (`low\_aspect\_ratio\_DEMO`) model collection (containing 242 models) ordered by provenance (a) and by a TOSCC (b), showing that the seemingly strongly cyclic nature of the model collection is an artefact of provenance-based ordering (PROCESS itself has a different ordering done by hand). The resulting cycles are small: see Figure 15 for their precise definition.

