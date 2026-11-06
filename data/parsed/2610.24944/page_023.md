For a box with componentwise bounds \(\ell\le m\le u\), the certificate gives a triangle cover _Fu_ meeting every triangle in the upper-multiplicity graph _Gu_ and an edge-disjoint triangle packing \(P_\ell\) in the lower-multiplicity graph \(G_\ell\), satisfying \(|F_u|\le 2|P_\ell|\). The cover meets both the triangles inside _C_ and every triangle _xuv_ with \(x\in I\) and \(u,v\in N_G(x)\cap C\). Adding copies preserves the smaller graph as a subgraph. Hence

\(\tau_\triangle(G_m)\le|F_u|\le 2|P_\ell|\le 2\nu_\triangle(G_m).\)

A separate checker reconstructs the graphs, enumerates every triangle in each upper-multiplicity graph, checks that its stored cover meets every such triangle, and verifies that the stored packing consists of edge- disjoint triangles in the lower-multiplicity graph. It also checks the cardinality inequality and coverage of every integer multiplicity vector. All 560 profiles and 18,444 boxes passed. The certificates cover the remaining profiles, and truncation extends the conclusion to arbitrary multiplicities. This proves Theorem 1.

## B Additional Construction Results

For the 34-pentagon case in Section 5.1, the enclosing triangle side length decreases from 12.98141 to 12.97563735803487. The released coordinates retain the construction at full precision.

7 records the three non-packing records in the construction collection. Each row compares the same task instance and objective convention. All objectives in this table are minimized.

### Vehicle routing.

The final construction contains 238 routes serving 1,047 customers with vehicle capacity 128. The objective uses the instance’s rounded Euclidean distances (CVRPLIB, 2026). The route list determines customer coverage, capacity feasibility, and total length.

### Autocorrelation.

The comparison uses the signed-maximum task and archived reference from EinsteinArena (2026). For signed step values _a_<sub>1</sub>_,...,a<sub>n</sub>_, the objective is

\(J(a)=\frac{2n|max_j(a*a)_j|}{(\sum_ia_i)^2},\)

where _a∗a_ is the discrete self-convolution. The absolute value is taken after the maximum. The maximum- absolute-value variant instead uses max<sub>_j_</sub>|(_a∗a)<sub>j</sub>_| in the numerator; the two objectives can differ for signed constructions. Under the signed-maximum objective, the released construction improves the archived reference by approximately 7.65 × 10<sup>-4</sup>.

### Zhang-Zagier.

The comparison uses the archived reference from maaxgrin (2026). The _c_<sub>82</sub> construction has an accompanying Arb-based numerical certificate for its objective.

\begin{tabular}{ccc}
**Problem** & **Archived reference** & **Épi** \\
Vehicle routing,
XL-n1048-k237 & 380107 & 380092 \\
Autocorrelation (signed
maximum) & 1.4515718639 & 1.4508066395 \\
Zhang-Zagier, _c_<sub>82</sub> & 0.2536331090 & 0.2535744749 \\
\end{tabular}



** 7:** Non-packing construction results in the construction collection.

