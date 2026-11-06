The two formulations have different computational costs, so Épi uses a higher resolution for the lower bound. Each endpoint has a retained witness that can be checked separately. Appendix A gives the resolutions.

## 5.4 Optimizing a tion: MAX-4-CUT

Épi starts from the MAX-4-CUT gadget framework of Nagda et al. (2025) and optimizes its edge weights. With the gadget structure and relevant completeness assignments fixed, the competing colorings have objectives that are linear in those weights.

This allows the agent to normalize one side of the hardness ratio and optimize the other through a linear program. Coloring constraints enforce the required properties of the gadget.

The reference ratio follows from the gadget parameters in Lemma C.2 and the reduction in Theorem C.2 of Nagda et al. (2025). The final integer weighted gadget changes it from

\(\frac{195581}{198140}\approx 0.987085\text{to}\frac{84931}{86101}\approx 0.986411.\) (5)

The released weighted edge list and finite checks recover this ratio exactly. Substituting the new gadget into the published reduction gives the improved hardness bound. This formulation provides a reusable optimization procedure: researchers can fix the gadget structure, optimize its weights subject to explicit coloring constraints, and verify the resulting ratio exactly.

## 5.5 A Finite Construction for the Spencer Constant

The square-matrix discrepancy problem asks how well signs can balance the rows of a real matrix with entries in [-1,1]. Épi found an \(8\times 8\) matrix whose discrepancy is exactly five. Exhausting its 256 sign assignments gives row-maximum norms of five or seven, so the minimum is five. The matrix therefore raises the record lower bound on the universal constant from \(7/\sqrt{17}\) to \(5/\sqrt{8}\) (Tao et al., 2026).

Figure 5 shows the entire matrix. Its entries lie in {-1,0,1}, within the allowed range [-1,1], and the claim can be checked by enumerating its sign assignments.



A Narrowing the n-queens interval
B Spencer discrepancy
-1
-1
-1
-1
-1
-1
-1
0
-1
-1
-1
1
1
1
1
0
-1
-1
1
-1
1
1
-1
0
-1
-1
1
1
-1
-1
1
0
-1
1
-1
1
-1
1
0
-1
1
-1
1
-1
1
-1
0
-1
1
1
-1
1
1
0
-1
1
1
1
1
-1
1
0
-1
1
1
1
1
-1
1
0
7/v17
5/v8
Width 3.30 x 10-7 3.94 x 10-9
256 sign assignments discrepancy exactly 5

**Figure 5:** Two new mathematical records. Left: the interval for the _n_-queens constant is approximately 84 times narrower. Right: an explicit \(8\times 8\) matrix with discrepancy five gives the Spencer lower bound \(5/\sqrt{8}\). The matrix entries are -1,0, and 1.

