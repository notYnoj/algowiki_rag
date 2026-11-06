<tbc>Finally, the core should not dominate runtime even when extremely fast, low-fidelity models are used. For applications such as uncertainty quantification [19] or design database generation [20, 21], fast design analysis can be crucial.

Together this yields the following set of requirements:

1. **Design problem agnostic**: any design problem (a selection of models, their parametrisation, and a problem formulation) should be usable without changes to the core.<tbc>

2. **Automated coordination**: the execution order and solver structure of models should be automatically derivable for any such design problem.<tbc>

3. **Flexible MDAO architecture**: the MDAO architecture should be easily modifiable beyond a default implementation to allow (re)configuration of analysis or optimisation problems.<tbc>

4. **Gradient computation**: gradients should be available natively using automatic and implicit differentiation.<tbc>

5. **Low overhead**: the core itself should not dominate runtime even for low-fidelity fast models.

Building on existing state-of-the-art fusion design codes or general-purpose MDAO frameworks would be preferable; however, this combination of requirements defines a particular niche that falls outside their scope. In fusion, design optimisation codes such as PROCESS [2, 3], BLUEMIRA [9, 12, 22] or SIMSOPT [23] have a modular software architecture, but require manual specification of model execution order and only support a hard-coded MDAO architecture, making them unsuitable for building the stellarator MDAO framework on. Recent codes such as DESC [24] and FUSE [11] can use advanced gradient computation (JAX and Julia, respectively) but also lack the automated coordination we require.

Outside of fusion, general-purpose multidisciplinary design and optimisation frameworks such as OpenMDAO [8] and GEMSEO [25] in principle provide flexibility in MDAO architecture, but either require significant manual coordination to reconfigure MDAO architectures (OpenMDAO) or are limited in flexibility of the MDAO architecture (GEMSEO). Novel approaches such as the AGILE paradigm [26, 27] use a graph-based approach to automate the coordination and ease (re)configuration for predefined optimisation architectures, but the openly available execution layer introduces too much overhead for our purposes. For a more detailed discussion, see Section II.

This has motivated the development of the herein presented graph-based generic coordination and execution core `cottax` that aims to satisfy these requirements.

## B. Contribution

Similar to [25, 26, 28], we use a graph approach based on purely functional models connected by their input/output variables. The resulting graph allows the use of topological ordering and strongly connected component algorithms [29] that find the smallest groups of coupled models that have to be solved together. Whereas these previous approaches start from the definition of an MDAO problem and then derive an architecture from it, we start from the definition of what an executable graph is and allow any graph that passes a set of executability checks to be executed (whether it corresponds to a standard MDAO architecture or not).

The contribution of this work is then twofold: by enabling the graph to represent any MDAO architecture, we extend the flexibility of a graph-based approach, and we allow this same graph to be directly and efficiently executed using JAX.

Our first contribution is the extension of a computational dependency graph by _conditional nodes_ and _nesting edges_ supported with a set of mathematical checks that define when this extended graph is executable. These conditional nodes are a generalisation of optimiser and solver iteration loops that can represent (among others) a fixed-point iteration, a residual (root-finding) solver, an optimisation problem, a consistency constraint, and an ordinary differential equation. Nesting edges indicate which conditional node iterates which other conditional node. The executability checks are generic: they only depend on the conditions and unknowns of a conditional node, and not on its type. The unification of solvers and optimisers as a single conditional node type combined with the nesting allows the creation of highly customised MDAO architectures: solvers and optimisers can be freely nested and combined with each other. The optimiser, solvers converging coupling variables, and the solvers of individual models have no special role: they are conditional nodes like any other. We also define a small set of graph operations that can turn any design problem into an executable graph. Standard monolithic MDAO architectures are then a sequential application of these graph operations instead of predefined presets, and can therefore be automatically assigned and easily modified. This graph representation, the executability checks, the graph operations, and the architectures are implemented in the Python package `cottax` in a generic way (i.e. an MDAO architecture can be defined and checked without implementations of the models and solvers).

