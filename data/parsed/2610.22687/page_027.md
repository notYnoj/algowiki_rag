<tbc>Due to the arbitrary model collection support and flexible MDAO architecture definition, `cottax` is not specific to stellarator MDAO or even fusion in general. The graph-based executability checks are general and could even be adapted to existing MDAO platforms such as OpenMDAO and GEMSEO.

## VII. CONCLUSIONS

Motivated by the need for design optimisation including both high-fidelity models and many disciplines in nuclear fusion reactor design, we present the generic coordination and execution core `cottax` that enables flexible (re)configuration and execution of multidisciplinary design analysis and optimisation (MDAO) architectures.

To achieve high flexibility, a graph-based definition of MDAO architectures is adopted. In particular, we develop a method to control the solver structure on the level of individual iteration loops using a few elementary graph operations. Standard monolithic MDAO architectures can be automatically assigned for arbitrary design problems. Furthermore, the general representation of both solvers and optimisers as iteration cycles with a condition to be satisfied allows future hybrid/custom approaches to also customise the MDAO architecture as desired, extending the flexibility of other graph-based approaches.

To obtain high computational efficiency for cases with higher-fidelity models and/or many low-fidelity models, a JAX execution layer is adopted. JAX features just-in-time compilation, which eliminates overhead from the graph machinery and model dispatch which may bottleneck cases with a high number of low-fidelity models. The JAX execution layer allows the transformations of JAX -- differentiation and batching -- to be used directly on the `cottax` graph itself. This allows low-level parallelisation (using `vmap`) of low-fidelity models for database creation or uncertainty quantification applications and implicit differentiation over arbitrarily nested solves. High-fidelity models can be directly included if they are JAX-native or otherwise wrapped. We consider the JAX execution layer to be a suitable approach for a future stellarator MDAO framework, though other approaches (e.g. Julia) may be coupled to the graph coordination layer in future as well if needed.

The PROCESS case study illustrates the potential of the combined approach, as the JAX execution layer and MDAO architecture together reduce the model time during optimisation by two to three orders of magnitude.

Though full integration of a larger number of high-fidelity and/or black-box models remains to be demonstrated, the proposed coordination and execution core `cottax` paves the way for design studies using selections of both high- and low-fidelity models which can easily and efficiently be combined to address a variety of design problems.

`cottax` is designed to be general, modular, and extensible, and we hope that the ideas contained in it find broader use.

## ACKNOWLEDGMENTS

We would like to thank the PROCESS team at UKAEA for supporting this work. Their modernisation efforts have been critical in enabling the application of `cottax` to PROCESS. We hope to contribute elements of this work to support the ongoing development of the PROCESS code.

