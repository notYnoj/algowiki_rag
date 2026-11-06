1. **A faster asymptotic algorithm from a compact construction.** The rational witness specifies an instance of the level-four combination-loss construction with _q_=5. Shared descendant parameters and binary-tree position symmetries give a 212820-coordinate family in which the improved exponent is attained. Unfolding the shared graph preserves admissibility, and six global coordinate permutations produce equal final matrix dimensions.<tbc>

2. **Conditioning adapted to constituent masses.** We rescale each numerical coordinate using its occurrence mass and local probability, including marginal-variance weights for entropy-dual coordinates. This addresses the disparate gradient scales of the recursive construction. The rescaling is refreshed between limited-memory quasi-Newton solves, with a larger scale range for low-mass constituents.<tbc>

3. **A six-control correction for extraction bottlenecks.** The root and two constituent stages each contribute a minimum of three role totals. We couple an augmented-Lagrangian continuation to a separate correction using two controls per stage. A \(6\times 6\) Newton system targets the six role differences, and candidate selection uses the original minimum-based objective. This focuses the correction on the bottlenecks that directly determine the exponent.<tbc>

4. **An exact, independently checkable construction.** The export preserves positive entropy- dual factors as arbitrary-size rational numbers. An independent verifier expands ordinary ternary strings and assembles all physical-coordinate contributions before applying the published minima. The resulting finite certificate can be checked offline, separately from the optimization implementation.

These contributions build on the tensor theorem of Alman et al. and the optimization formulation of Dupont et al. The orbit representation and equality-constrained approach were informed by computational notes shared by Eric Naslund. Softmax parameterization, quasi-Newton optimization, augmented Lagrangians, entropy duality, and rational interval arithmetic are established tools; the methodological contribution is their specified adaptation and integration for the construction certified here.

Section 2 specifies the construction and the restricted parameter family. Section 3 describes the numerical continuation and rational export. Section 4 gives the certificate and the proof of Theorem 1. The appendix supplies implementation-level lemmas for shared parameters and logarithm enclosures.

## 2 Construction and parameter family

The construction is an instance of the combination-loss framework of [2], in the formulation of [9, Section 2]. The new algorithm is specified by a rational recursive extraction construction within that framework. Its parameters determine the retained matrix products and their asymptotic dimensions. We use the Coppersmith–Winograd tensor with parameter _q_=5 and recursion level \(\ell^*=4\). Thus the starting tensor is \(\mathrm{CW}_5^{\otimes 8}\), whose asymptotic rank cost, in binary logarithms, is

\(C=2^{\ell^*-1}\mathrm{log}_2(q+2)=8\mathrm{log}_27.\) (1)

Below we specify the restricted family used in the numerical search. All restrictions are parameter identifications or symmetries allowed by the published construction.

