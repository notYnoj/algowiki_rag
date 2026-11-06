_Proof._ The block terms plainly count the forced changes in _S_. Fix a type _R_ and let _T<sub>R</sub>_ be the set of target colors assigned to its vertices, including colors represented by block nodes mapped to _R_. For every \(c\in T_R\) that already occurs in _R_, retain one initially _c_-colored vertex. These chosen vertices are distinct because the colors in _T<sub>R</sub>_ are distinct. Match the remaining target colors bijectively to the remaining vertices of _R_. Each such vertex changes color. Hence exactly one vertex can be kept for every target color already present in _R_, and all other vertices change. This is precisely the cost charged by the nodes of type _R_.

Conversely, in any realization, at most one vertex of _R_ can keep color _c_ because the target is proper on the clique. Such a vertex can exist only when _c_ occurs initially in _R_. Thus, no realization has smaller cost. The construction is independent for the different types and therefore realizes all zero-cost representatives simultaneously.

The resulting target coloring is proper. Every block of P is independent, distinct assignment nodes receive distinct colors, and all vertices of _C_ correspond to distinct assignment nodes. The colors shared between _S_ and _C_ are precisely

C R3 R1 Ri R2 S
P1 Pj

**Fig.3.** A guess \(\sigma\) for the distance-to-complete algorithm. For each block _P_ of the partition of _S_, the equality \(\sigma(P)=R\) means that _R_ is anticomplete to _P_ and that one vertex of _R_ reuses the color assigned to _P_; the equality \(\sigma(P)=\perp\) means that this color is absent from _C_. Solid arrows show one guess and dashed arrows other admissible choices.

