As the Laurent exponent interval \[-2_m,_2_m_\] has width 4_m\<Q_, two distinct exponents in this interval are never congruent modulo _Q_. Hence the inverse discrete Fourier transform does not suffer from aliasing and recovers the ordinary Laurent coefficients, including those with negative indices.

_Proof of Theorem 1.2._ The _p_=1 statement is Proposition A.1. For _p_=2, start from an instance _H_ of counting maximum cuts. Set

\(\mathrm{cos}\beta_1=\frac{2}{\sqrt{5}},\mathrm{sin}\beta_1=\frac{1}{\sqrt{5}},\) (33)

which satisfies \(\mathrm{tan}\beta_1=1/2\). The coefficient (27) is nonzero for every even _N_ and directly determines |#MC(_G_)|=2|#MC(_H_)|. All coefficients are obtained from Eq. (32), and the largest exponent with nonzero coefficient is selected. Theorem 2.4 guarantees that this exponent is _D<sub>⋆</sub>_ and that its coefficient is nonzero. Thus exact evaluation is #P-hard at QAOA depth two for either the global expectation or the designated correlator.

For any fixed _p\>_2, set all angles in layers 3_,...,p_ to zero. These layers are the identity, so the depth-_p_ oracle value equals the depth-two value. This proves the #P-hardness statement for every fixed \(p\ge 2\).

_Proof of Corollary 1.3._ The depth-one correlator formula is given in Appendix A. For _p_=2, the proof above recovers the extreme coefficient directly from _H<sub>e<sub>⋆</sub></sub>_, so no other correlator is needed. The same identity padding applies for _p\>_2.

**Remark 2.5.** _The reduction of Theorem 1.2 recovers more than the count of maximum cuts: the extreme exponent D<sub>⋆</sub>=MC(G_)+2_N_-4 _itself reveals MC(G), and hence MC(H_) _via Eq._ (12)_, before the coefficient is examined. Thus a single run of the interpolation recovers both the maximum cut value and the number of maximum cuts of H, so the present construction also reproduces the NP-hardness conclusions of \[5\] directly._

## Hardness on diameter-two graphs

**Corollary 2.6.** _For every fixed_ \(p\ge 2\)_, exact evaluation of the MaxCut QAOA expectation is_ #P_-hard under deterministic polynomial-time Turing reductions, even when restricted to connected, unweighted, simple graphs of diameter two. The same conclusion holds for the expectation of the designated two-qubit observable Z<sub>r</sub>Z<sub>s</sub>, where_ {_r,s_} _is an edge joining two universal vertices._

_Proof._ The graph G(_H_) constructed in the proof of Theorem 1.2 is unweighted, simple, and connected. The two anchor vertices _r_ and _s_ are adjacent to one another and to every vertex in every variable gadget. Let \(u,v\in V(\mathcal{G}(H))\). If neither vertex is _r_, then both are adjacent to _r_, and hence there is a path _u-r-v_ of length at most two. If one of the vertices is _r_, then the pair is adjacent. Thus every pair of distinct vertices is joined by a path of length at most two, so \(\mathrm{diam}(\mathcal{G}(H))\le 2\). The graph is not complete: for example, two distinct vertices in the same part _A<sub>v</sub>_ of a variable gadget _K<sub>L,L</sub>_ are nonadjacent. Hence diam(G(_H_))=2.

**Remark 2.7.** _The diameter-two restriction is obtained at the expense of large degree that scales with the problem size, as it must: any diameter-two graph on N vertices has maximum degree at least_ \(\sqrt{N-1}\) _(because from any vertex, at most_ \(1+\Delta+\Delta(\Delta-1)=\Delta^2+1\) _vertices can lie within distance two). Each anchor is adjacent to every gadget vertex, and the vertices within each K<sub>L,L</sub> gadget have degree growing with the source-instance input problem size. Consequently, the corollary does not establish hardness for bounded-degree graph families._

