<tbc>simply being executable (as this work is). This work tries to formalise from as little as possible how a dependency graph with conditional nodes looks and when it is valid, and argues for MDAO architectures to be built on top of that, rather than starting from the MDAO formulation itself.

Pate et al. \[28\] and KADMOS \[26\] both use bipartite graphs instead: this maps one-to-one to the definition in Appendix A however. The main difference is that the conditional node extension is not explicit in KADMOS and therefore many checks are not expressible in KADMOS or vice versa.

Process graphs as in \[26\] are not considered in our formulation: a TOSCC after having checked executability explicitly defines a valid process graph and thus there is nothing to check. Furthermore, since we do not construct a repository connectivity graph (the collection of all possible models, which can have overlapping outputs), checks that reference it are not relevant here.

## Appendix B: Equality of programs: manual and cottax

In this appendix, the same model is constructed using imperative programming and cottax. These will yield the exact same `jaxpr` (intermediate representation of JAX), which is then just-in-time compiled. The same `jaxpr` yields the same computational graph.

In general this is only identical up to the level at which the topological sort is unambiguous: parallel-executable nodes may be reordered arbitrarily and as such in general not be equal to a manually ordered structure -- this example is unambiguous by construction.

Driven blocks are somewhat more complicated: the driven subgraph is evaluated once more after converging to ensure consistency of the data structure with the final unknowns (the unknowns can be updated after the last value iteration -- values in the data structure are one step stale). This ensures derivatives are computed accurately in all cases.

In some cases, this may be less efficient than a hand-written solver loop, which, given the internals of the solver and details of the problem, could eliminate some of this recomputation in favour of reusing final iterate values. Currently, in cottax, for simplicity, such elimination is not performed: the cost is low compared to the iterative cost (one value iteration extra compared to tens to hundreds of iterations possibly including Jacobians) and evaluates values and derivatives correctly whatever the problem or driver<sup>3</sup>

## Appendix C: Definition of PROCESS configurations

All PROCESS configurations considered here are in the regression suite of the PROCESS GitHub. The tables below give explicitly the iteration variables, objective (if present), and equality and inequality constraints. In the root-find (evaluation) configurations, only the equality constraints are solved; the listed inequalities are evaluated at the solution but not imposed. In  XIV the particular model switches are also shown for all seven configurations.

<sup>3</sup> This does not necessarily include driver outputs: iteration history is inherently dependent on the iterative path, while the conditions / unknowns are not. Such a history cannot be differentiated through the implicit function theorem; only by unrolling all iterations. Since this is extremely memory-intensive in reverse mode, this will be set to zero in all cases.

\begin{tabular}{cc}
Main text & Appendix \\
G1 & One producer per variable (A.1), (A.3) \\
G2 & No self-reads (A.2) \\
G3 & No nesting loops (A.11) \\
E1 & Conditions determined (A.13), (A.15) \\
E2 & Functionally acyclic (A.14) \\
E3 & Drivers assigned -- (implementation, not a graph check) \\
E4 & Valid nesting (A.9), (A.10), (A.12), (A.16) \\
-- (appendix only) & (A.4), (A.5), (A.6), (A.7), (A.8), (A.17) \\
\end{tabular}

IV: Correspondence between the checks of Section III and the checks of this appendix.

