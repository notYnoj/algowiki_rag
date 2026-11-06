<tbc>by the uniform factor established in Lemma 5.3 to ensure the satisfaction of the delay constraints.

**Lemma 5.4.** _Given a DCMCF instance and a scalar_ \(\alpha>1\)_, it is possible to build in polynomial time a relaxation DCMF<sub>env</sub> with upper bounds u<sub>a</sub> of variable y<sub>a</sub> for every_ \(a\in A\) _and a solution with objective value_ \(\gamma^*\)_, such that_ \(u_a\le\alpha(\sum_{k\in K}b^k)\gamma^*\).

Lemma 5.4 ensures that sufficiently tight upper bounds _u<sub>a</sub>_ on the arc loads can be computed. The proof, provided in Appendix B.4, relies on an iterative process that repeatedly solves the relaxation until the bounding criterion is met. Combining these tight load bounds with the ex-post guarantee from Proposition 5.2 allows us to establish the overall approximation ratio of the algorithm:

**Theorem 5.2.** _Given a scalar_ \(\alpha>1\)_, it is possible to build a_ \(\frac{1}{\alpha\beta|K|(|P|-1)+1}\) _approx imation of the DCMCF problem in polynomial time, with_ \(\beta=\frac{max_{k\in K}b^k}{min_{k\in K}b^k}\).

The proof of Theorem 5.2 is given in Appendix B.5, where we consolidate the previous bounds to extract the final approximation factor.

## 6 Numerical experiments

In order to assess the relevance of the new relaxations presented in this work, we implemented them with SCIP 10.0 \[18\] in C++. Tests were conducted with 16 CPUs and 64 GB of RAM.

The reformulations of the DCMCF problem described above were implemented. All of them included the Big-M constraints (26) and (27) introduced in Section 4.1, and all of them (except the first one) include additional tightening constraints:

• BIG-M : the Big-M formulation introduced in Section 4.1.<tbc>

• CONVEX : the Big-M formulation with Constraints (18) to (25) from the DCMF<sub>env</sub> relaxation.<tbc>

