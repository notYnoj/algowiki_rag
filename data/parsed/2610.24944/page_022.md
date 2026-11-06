## A.11 Quantum-Capacity Thresholds

Following the permutation-invariant state formulation of Agarwal et al. (2026), Épi finds 40-qubit input states with positive coherent information at

\(p_{XZ}=\frac{1198803}{1000000}=0.1198803,p_{2P}=\frac{238683}{200000}=0.1193415.\)

These improve the reported independent X-Z and Two-Pauli thresholds of approximately 0.118371 and 0.118067, respectively. Separate interval spectral calculations verify positive coherent information for both states, establishing positive quantum capacity at the stated noise parameters.

## A.12 Water-Network Design: Waterund36

For the original continuous waterund36 minimization problem (MINLPLib, 2026), the certificate establishes

\(f^*\ge 662.80702839.\)

It excludes objective values at or below the exact rational cutoff

\(\frac{6628070283996671}{10^{13}}.\)

The displayed lower bound is rounded downward. Compared with MINLPLib’s lower bound 655.5441707 and known feasible value 662.8070384, the remaining gap is about 0.00001001. The instance also appears in Castro’s study of global optimization with mixed-integer relaxations (Castro, 2023).

The proof rules out every network cheaper than the cutoff by deriving a contradiction from that cost assumption. It first lifts each feasible network into a bounded relaxation using flow and contaminant conservation. For a linear relaxation \(Ax\le b\) with box bounds \(L\le x\le U\), any nonpositive row multiplier vector _y_ gives the valid lower support

\(c^Tx\ge y^Tb+min_{L\le z\le U}(c-A^Ty)^Tz.\)

Equality-row multipliers may have either sign. The box minimum is evaluated componentwise. Rational support inequalities and bound propagation eventually yield incompatible bounds under the cutoff assumption. Containment of the original feasible set in the relaxation then establishes the global lower bound. The released certificate supplies the model, witnesses and exact comparisons needed for this argument.

## A.13 Tuza’s Conjecture: Proof for Three Neighborhood Types

For the partition in Theorem 1, discard independent vertices with fewer than two clique neighbors: they occur in no triangle. The remaining vertices have at most three distinct neighborhoods in _C_. We call a triple of these neighborhoods, considered up to relabeling _C_ and permuting the three types, a neighborhood profile.

### Finite reduction.

Zeng’s multiplicity-truncation lemma (Zeng, 2026) preserves both \(\tau_\Delta\) and \(\upsilon_\Delta\) when each type is truncated to 28 copies. Every triangle uses a clique edge, so a packing uses at most 28 triangles and at most 28 independent vertices of any type. For covers, all 28 clique edges suffice. If a minimum cover of the truncated graph has fewer than 28 edges, some copy of every saturated type has no incident cover edge. All clique edges within that type’s neighborhood must then be covered, which also covers triangles through any additional copies. Thus the finite multiplicity range suffices for the infinite statement.

### Completeness and certificates.

An independent enumeration gives 872 profiles with three distinct active types. Of these, 35 have nested neighborhoods and fall under the threshold-graph theorem of Bonamy et al. (2022). Another 277 satisfy Zeng’s maximum-cut criterion (Zeng, 2026). The cases with at most two types follow from Zeng’s theorem. The remaining 560 profiles are covered by exact certificates containing 18,444 integer boxes in {0_,...,_28}<sup>3</sup>.



