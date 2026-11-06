### Beyond NP.

Which natural problems complete for classes such as PSPACE, EXPTIME, or NEXPTIME admit polynomial preprocessing and query times in the Isomorphic-Priors model?<sup>16</sup> How does this question extend to exact counting problems complete for #P, when the exact counts are supplied with the priors? More generally, which structural properties allow answers to classically hard problems to be efficiently reused, and which problems admit conditional lower bounds through isomorphism-preserving reductions? Understanding this landscape would clarify how the complexity of reusing prior answers differs from that of computing them from scratch.

### The Power of Invariant Representations.

Our algorithmic results rely on efficiently computable invariant representations (e.g., WL coloring or spanning tree polynomial) whose equality guarantees equality of optimal values. Does this approach characterize polynomial-time solvability in the Isomorphic-Priors model? Specifically, if a problem admits polynomial preprocessing and query times, must there exist a polynomial-time computable function _f_ such that

\(G\cong H\Longrightarrow f(G)=f(H)\Longrightarrow OPT(G)=OPT(H)?\)

Here, _f_ must be computable from the input graph alone, without access to its optimal value or to a database of priors. Alternatively, can jointly processing a query and the supplied prior answers yield algorithms that cannot be captured by such representations?

### Characterizing Tractability.

Our algorithmic results for NP-hard problems (consider for example Constrained Shortest Path or Constrained Spanning Tree) exploit numerical edge attributes, whereas problems on unweighted graphs such as Vertex Cover and Hamiltonian Cycle remain conditionally hard. To what extent do these attributes account for the difference? Can we identify natural NP-hard problems on unweighted undirected graphs, with no additional vertex or edge attributes, that admit polynomial preprocessing and query times? Here, we seek positive results beyond those that follow immediately from efficient isomorphism testing on restricted graph classes.

Constrained Shortest Path and Constrained Spanning Tree provide examples of weakly NP-hard problems that become tractable in our model. Do all problems admitting pseudopolynomial algorithms admit polynomial preprocessing and query times with isomorphic priors? Conversely, are there natural weakly NP-hard problems that remain conditionally intractable in our model? Understanding these questions would help distinguish the roles of numerical information and graph structure in enabling the reuse of prior computations.

### From Values to Solutions.

Our algorithms can reconstruct optimal solutions when suitable optimal witnesses are supplied with the priors, but these reconstruction arguments are problem- specific. Is there a general principle that converts efficient value-retrieval algorithms into efficient solution-reconstruction algorithms in our model? Standard decision-to-search reductions do not immediately suffice: the modified instances they generate need not be isomorphic to any prior, so the algorithm may abstain on them. Which properties of the witnesses or invariant representations permit efficient reconstruction? Can we identify a natural separation between retrieving optimal values and reconstructing optimal solutions, even when optimal prior solutions are supplied?

### More Concrete Problems.

Can makespan scheduling of unit-length jobs with precedence constraints on a fixed number of identical machines [NSW25], or Rabin games [MST24], be solved<tbc>

<sup>16</sup>NFA Universality and Existential Length Universality for NFAs are PSPACE-complete and NEXPTIME-complete, respectively [GLR<sup>+</sup>20]. We believe that both admit polynomial preprocessing and query times in our setting by adapting our 1-WL techniques, under isomorphisms that preserve transition labels and initial and accepting states. However, a formal treatment of these extensions is beyond the scope of this paper.

