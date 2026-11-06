## D. Gradient computation

JAX provides a wide variety of transformations on compatible Python functions, including gradients in forward or reverse mode. As the `cottax` graph is such a function, it can be differentiated easily, including deeply nested solves using implicit differentiation techniques available in the JAX ecosystem.

The efficiency of the algorithmic and implicit differentiation of a `cottax` graph has to be shown for a large set of higher-fidelity models. PROCESS uses mostly scalar arithmetic and as such does not provide a sufficient test for this requirement. JAX is also already used for differentiable higher-fidelity simulations in fusion, e.g. DESC [24] and TORAX [69]. Also, a to-be-published blanket optimisation with 200 design variables containing a higher-fidelity (over a billion degrees of freedom) differentiable neutronics model had no measurable difference in computational efficiency compared to our previous handwritten implementation (which is unsurprising given that the resulting compiled object does not contain `cottax` machinery, see Appendix B).

Wrapping of non-JAX models (with possibly finite differences for gradients) has been tested (e.g. the PROCESS optimisers of Section VB are wrapped). In principle, with callbacks, this procedure would be similar to Python orchestration (e.g. OpenMDAO and GEMSEO), but no large-scale optimisations with opaque closed-source models have been attempted yet. In addition, using non-JAX differentiable components [65] for opaque models that are not in JAX but can provide derivatives would be an interesting option: `cottax` only requires explicit outputs and inputs and thus would natively support this.

Besides testing on a large set of higher-fidelity models and large-scale optimisations with opaque models, the development of a JAX-compatible constrained optimiser that can be implicitly differentiated and batched would be useful to reduce overhead and enable applications such as sensitivity analysis. Finally, inclusion of a MAUD-like [42] derivative computation option could also be interesting.

## E. Low overhead

The just-in-time compilation of the `cottax` graph eliminates runtime overhead (Section VB) and enables batching of the same graph (Figure 20).

Compilation overhead is relatively small in the PROCESS case (less than five seconds), but can be significant (tens of seconds) for very large and deeply nested graphs (thousands of nodes and more than four nesting layers). This can be worked around by e.g. exporting (precompiling) the function or using callbacks to particularly compile-intensive subprograms.

JAX does not natively support parallel execution of different models; callbacks could be used to parallelise this in the future, or a different execution layer could be used (see Section VIF).

Overhead reduction of a coordination and execution core is mostly relevant for cases with a relatively large number of models and relatively low computational time. PROCESS is precisely this: it would be interesting to benchmark this overhead reduction in other applications.

## F. Further outlook

As mentioned, the JAX execution layer has to be shown to be compatible with a larger set of higher-fidelity models. If it does not scale well in that regime, an alternative would be to develop a different execution layer while still using the `cottax` coordination; the coordination does not depend on an implementation type (e.g. Julia functions or even repository locations are supported) and can even be performed without any implementation defined (Section IVG). Examples of possible execution layers are Julia (which could be an interesting option due to its relatively mature differentiable simulation ecosystem) or OpenMDAO. Exporting to e.g. CMDOWS [70] could enable easier integration.

The experimental `ode` conditional node type has to be tested more extensively and could be used for mixed algebraic / ODE usage for e.g. transport / integrated modelling, optimal control, or other time-dependent analyses.

A graph-based approach is useful beyond execution; it provides insight into model coupling and the required solves and can automatically define an MDAO architecture without even considering the function implementations. Insight into which models are coupled could be used to develop strongly coupled solves where needed using specialised software such as MOOSE [71]. The reach of the graph (which variables are affected by which other) can also be used to determine valid design variables or unknowns for root finds. Finally, the `cottax` graph could be integrated with model-based systems engineering, which also extensively uses graphs to similarly analyse design dependencies.

The stellarator MDAO framework requires a large amount of development still: models need to be developed for all relevant subsystems, a shared parametrised design ontology needs to be built (which these models have to be able to interface in) and these models and their coupled solves need to be verified and validated.

