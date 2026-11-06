Therefore, if a graph class admits an integrality gap of at most \(\alpha\), then there exists a set of small diameter decompositions that do not cut any fixed edge too many times. We describe this in detail in Section 4.

Our crucial insight is that if the integrality gap is \(\alpha\) for a class of graphs, then there exists a well-structured set of small diameter decompositions that can be used to construct the aforementioned convex combination. These structured decompositions are inspired by the well-known single-source distance-based decomposition algorithms for trees. We also describe this in detail in Section 4. The final step of the proof involves using these structural insights to argue that there cannot exist a small diameter decomposition with a small value of \(\alpha\) for the family of cactus graphs. Note that this proof is non-constructive and does not lead to an explicit example with a large gap. Nevertheless, this proof provides sufficient structural insights into instances with a large integrality gap, allowing us to construct explicit examples of cactus graphs where the gap is at least \(\frac{20}{9}\) (unfortunately, we were unable to find an explicit example showing a lower bound of \(\frac{16}{7}\) ). We emphasize that we attempted to construct these examples through an exhaustive computer search and manual crafting but were unsuccessful. Furthermore, the structural properties established in the first proof hold for very general classes of graphs, specifically those closed under edge subdivision and 1-sum operations, and may prove useful in other settings as well.

## 4 The Integrality Gap of Multicut and Small Diameter Decomposition

Let G be a family of graphs closed under taking minors and under edge subdivisions, and let M(G) denote the corresponding family of all minimum multicut instances on G. Theorem 1, which is a direct application of the work of Carr and Vempala \[CV02\] to the minimum multicut problem, shows that any feasible fractional solution to the LP relaxation can be approximately represented as a convex combination of feasible multicuts. For completeness, we include a proof, although it is not a novel contribution of this work.

**Theorem 1.** _Suppose we are given an instance_ \(M\in\mathcal{M}(\mathcal{G})\)_. Let_ \(\mathcal{F}\subseteq 2^{E(G)}\) _be the set of all feasible multicuts for M, and let x be a feasible fractional solution to the LP relaxation_ (1)_. Then there exists a probability distribution y over_ F _such that_<tbc>

\(\sum_{F\in\mathcal{F}e\in F}y_F\le\alpha_{\mathcal{M}(\mathcal{G})}\cdot x(e)\forall e\in E(G).\)

<tbc>_Proof._ Suppose the statement does not hold. Then the following linear system (2) is infeasible.

\(\sum_{F\in\mathcal{F}}y_F=1\sum_{F\in\mathcal{F}e\in F}y_F\le\alpha\cdot x(e)\forall e\in E(G)y_F\ge 0\text{(2)}\)

This implies that the following system (3) is infeasible as well. The reason is that if the system below is feasible, then we can scale down the feasible solution appropriately and obtain a feasible solution for the system above.

