# Managing complexity for integrated fusion reactor design using a differentiable graph-based MDAO approach: PROCESS as a case study

Timo J. Bogaarts,<sup>1</sup>,<sup>∗</sup> Willem Rutten,<sup>1</sup> and Felix Warmer<sup>1,2</sup>

<sup>1</sup>_Eindhoven University of Technology, PO Box 513, 5600 MB, Eindhoven, Netherlands_

<sup>2</sup>_Max-Planck-Institut für Plasmaphysik, Teilinstitut Greifswald,_

_Wendelsteinstrasse 1, Greifswald D-17491, Germany_

(Dated: October 19, 2026)

Integrated design of nuclear fusion reactors requires combining an increasingly large number of models from different disciplines self-consistently, with model selection and parametrisation changing between design studies. Manual definition of execution order and solvers for cyclic dependencies is error-prone, inefficient, and inflexible. We propose to use a generic graph-based coordination and execution core that enables automated execution order, cycle detection, and solver architecture specification for any set of models or parametrisation. To this end, a computational dependency graph of purely functional models is extended by a conditional node and nesting edges, treating solvers and optimisers in the same way. A minimal set of graph operations then allows for fine-tuned control on feedback resolution, making both optimiser and solver architectures easily reconfigurable. Existing monolithic multidisciplinary design analysis and optimisation (MDAO) architectures can be recovered by sequentially applying these operations. The `cottax` package implements this extended dependency graph, graph operations, executability checks, and a JAX-based execution layer. This execution layer eliminates runtime overhead and provides native gradient computation through the whole graph. As a proof of principle, `cottax` is then applied to the PROCESS systems code. Graph sequencing shows that for PROCESS only three small coupled components need to be solved every optimiser iteration. Monolithic MDAO architectures are then assigned to seven different PROCESS configurations, demonstrating the ease of (re)configuring its architecture. Compared to PROCESS, the sequencing and execution back-end together yield a two to three orders of magnitude reduction in model runtime during optimisation. `cottax` is currently being considered as the basis for developing an integrated stellarator MDAO framework.

### I. INTRODUCTION

Nuclear fusion reactors are complex to design, requiring highly specialised teams of experts working on interdependent subsystems. A complete engineering design may take years, which precludes the many evaluations required for design space exploration and optimisation. In practice, exploration and optimisation are thus carried out with a reduced parametrisation of the reactor (a small set of high-level decisions such as major radius, magnetic field strength, net electric power, blanket type and thickness) and with reduced-fidelity models of its behaviour [1].

Fusion systems codes [2–4] integrate a set of low- or medium-fidelity models self-consistently to compute system-level design objectives (e.g. cost of electricity) and engineering constraint satisfaction as a function of these high-level decisions. With an optimisation algorithm [5] these models are then executed iteratively to find an optimal design candidate within this parametrisation -- an approach more generally known as multidisciplinary design analysis and optimisation (MDAO) [6–8]. The resulting optimum serves as the starting point for detailed engineering design.

However, the behaviour predicted by the low-fidelity models often turns out to be inconsistent with that obtained in detailed engineering design [9, 10] (e.g. the breeding blanket might not produce its target tritium breeding ratio when 3D effects are taken into account). Since the optimality and engineering constraint satisfaction of the design candidate were established with respect to the low-fidelity models, such inconsistencies imply it is at best non-optimal and at worst unviable, in which case the high-level decisions must change. This is expensive: the strong coupling between subsystems [1] means such a change rarely stays local. For example, a thicker blanket also affects the coil geometry, vacuum vessel, and support structure, which then all require a detailed redesign.

Using coupled higher-fidelity parametrisations and models directly in the system-level analysis and optimisation reduces the chance of such inconsistencies and thereby the need for detailed design iterations [9, 11, 12]. Higher-fidelity system-level analysis and parametrisation is especially crucial for stellarators. First, their three-dimensional shaping increases the likelihood of inconsistencies arising between analytic models or scaling laws (typically adapted from tokamaks [13, 14]) and a detailed design. Second, this shaping introduces additional design parameters whose effects<tbc>

<sup>∗</sup> timobogaarts@gmail.com

