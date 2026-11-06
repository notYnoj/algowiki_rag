**Corollary 2.** _Let_ G _be the family of cactus graphs. If_ G _is strongly SDD_(2_w,p)-acceptable, then_ \(w\cdot p\ge\frac{8}{7}\).

_Proof._ Recall that before Theorem 8 we fixed a constant \(\epsilon>0\), and in that theorem we proved that<tbc>

\(w\cdot p\ge\frac{8}{7}-\frac{4\epsilon}{7}.\)

<tbc>Since this bound holds for every \(\epsilon>0\), taking the limit as \(\epsilon\rightarrow 0^+\) yields

\(w\cdot p\ge\frac{8}{7},\)

as claimed.

## 8 An Explicit Construction for the \(\frac{20}{9}\) Lower Bound

Inspired by the proof presented in Section 6, we now give an explicit example on a cactus graph where the integrality gap is at least \(\frac{20}{9}\) . In particular, given an \(\epsilon>0\), we are going to give an instance of the minimum multicut problem _M_ on a cactus graph _G_ such that,

\(\frac{\mathrm{OPT}_{IP}(M)}{\mathrm{OPT}_{LP}(M)}\ge\frac{20}{9}-\epsilon.\)

We will construct the graph _G_ by using two 1-_sum_ operations. Let _H_ be the following graph,

