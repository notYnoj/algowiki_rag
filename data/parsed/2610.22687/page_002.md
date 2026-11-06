<tbc>low-fidelity models cannot capture. Finally, the plasma shape is typically optimised first -- before the system-level analysis -- using low-fidelity proxies for the engineering design (e.g. required plasma-coil distance), which again makes non-optimal or unviable designs more likely.

Yet, as illustrated in Figure 1, current stellarator analyses are either low-fidelity system-level analyses [13, 14] or high-fidelity few-discipline codes that cannot be readily coupled. Within the Stellarator-Reactor-Studies group at IPP Greifswald, a stellarator MDAO framework is being developed to fill this gap [15], enabling self-consistent, higher-fidelity stellarator design space exploration and optimisation and thereby accelerating the design process.

No single set of models and parametrisations (or even a common data structure) has been established for higher-fidelity stellarator MDAO. Moreover, the choice of parametrisation and model set could change per design study: for example, surrogates for optimisation around a known design point, low-fidelity models for large-scale design space exploration, or mixed-fidelity models to balance computational cost and accuracy. Even with a fixed model set and parametrisation, the problem formulation (which variables can vary, which constraints are considered, and which objective is pursued) may change: e.g. minimising major radius rather than maximising net electric power. Fixed choices for how models are coordinated and executed are thus incompatible with the development and usage of such a framework. Therefore, we argue for a generic core that handles the coordination and execution in a design-problem-agnostic way.

## A. Requirements for the coordination and execution core

The coordination and execution core of the stellarator MDAO framework needs to satisfy a set of requirements.

First, as argued, the core should support arbitrary design problems: changing the models, parametrisation, or problem formulation should not require changing the core itself.

Second, the core should be able to automatically generate a valid and efficient execution order of the models and their solvers (an MDAO architecture) for such arbitrary design problems. Manual coordination is feasible for a small set of models, but becomes error-prone and time-intensive as the number of models and their interdependencies increase. Furthermore, it has to be repeated for every change in model set, parametrisation, or problem formulation. A fixed-point iteration over all models to resolve coupling is always possible, but is not efficient (uncoupled models would be run unnecessarily) and may not converge at all.

Third, an automatically assigned architecture is not always the most efficient [16]. For example, the vastly different computational costs of different fidelity levels might warrant nesting of solvers or optimisers to iterate the lower-fidelity models more often (similar to the motivation for Asymmetric Subspace Optimization [7, 17]). Therefore, the core should be able to implement arbitrary solver and optimisation structures and allow for easy modifications whenever required by the particular problem (which, again, changes with the design problem).

Fourth, higher-fidelity parametrisations (e.g. plasma boundary or blanket shape parameters) have significantly more design variables than low-fidelity ones (e.g. size or average field strength). Gradient-free optimisation does not scale well in this regime [7], and therefore gradient-based methods should be natively supported and integrated. To minimise implementation effort and avoid the scaling and accuracy issues of finite differencing, automatic differentiation methods and implicit differentiation (e.g. adjoint methods) are strongly preferred [18].

Stellarator PROCESS
Stellarator MDAO
Nr. of disciplines
Analytic plant sizing
Single stage optimisation
Plasma optimisation
Coil optimisation
3D neutronics analysis
Detailed analyses
Fidelity

Figure 1: Stellarator reactors are currently analysed either with high fidelity or with a large number of disciplines. Stellarator MDAO aims to combine higher-fidelity models and a larger number of disciplines.

