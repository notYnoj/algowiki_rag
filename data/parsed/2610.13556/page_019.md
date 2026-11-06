<tbc>There are at most 2<sup>_s+e_</sup>(2_<sup>s</sup>_+1)_<sup>e</sup>_ choices of \(N'\), and a number depending only on _e_ of assignments of its positive excesses. Each map on the union label set has at most 3_e_ nonstar occurrences and at most 2_e_ nonstar labels. Its descriptions are therefore bounded in number by

\((2e+1)^s(2e2^s+1)^{3e}.\)

Minimize over the target profiles and descriptions for this fixed _w_, then maximize over source descriptions and admissible source profile shapes. The order of these operations is exactly the order in Theorem 2.2. This proves the second running-time bound. The displayed description and orbit bounds, the number of profile shapes, and Theorem 5.6 give the stated choice of _f(s,e_), with the cases _e_=0 interpreted directly. □

### 5.5. The recognition algorithm.

_Proof of Theorem 5.1._ Fix _t_. If _G_ is empty, return zero for both parameters. Otherwise, compute a maximum matching in _G_. If its size is at most _t_, its endpoints form a vertex cover of size at most 2_t_. Theorem 5.5 computes both parameters exactly; truncate each answer at _t_+1.

Otherwise \(\nu(G)>t\). Compute a maximum matching in <o>_G_</o>. If \(\nu(\overline{G})>2t\), then \(\chi(G)\le n-\nu(\overline{G})<n-2t\). Theorem 5.3 implies _B_<sub>w</sub>(_G)\>t_, and hence also _B(G)\>t_. Return _t_+1 for both parameters.

In the remaining case, the endpoints of a maximum matching in <o>_G_</o> give a set _U_ of size at most 4_t_ whose complement is a clique in _G_. Compute \(\chi(G)\) using Theorem 5.6. If \(\chi(G)<n-2t\), the same dichotomy again gives both answers as _t_+1. If \(\chi(G)\ge n-2t\), apply Theorem 5.8 with \(s\le 4t\) and \(e\le 2t\), and truncate the exact answers at _t_+1.

This exhausts all graphs and proves correctness. By Theorem 5.5, the first branch takes time _g_(2_t_)(_n_+1)<sup>_O_(1)</sup>, after replacing _g_ by a nondecreasing computable bound if necessary. By Theorem 5.8, the complement-cover branch takes time 2<sup>_O_((_t_+1)<sup>2</sup>)</sup>(_n_+1)<sup>_O_(1)</sup>. Input processing and matching computations add only fixed polynomial factors. Their exponents are independent of _t_, proving the stated bound with a computable _f_. The argument includes _t_=0.

To obtain the exact values with weak villainy as parameter, run this structural algorithm at thresholds 0,1,2,4_,..._. Whenever an exact-computation branch is reached, retain both answers before truncation and stop. Continue only after a rejection, which certifies _B_<sub>w</sub>(_G)\>t_. By Theorem 5.3, rejection is impossible once \(t\ge B_\mathrm{w}(G)\). If \(B_\mathrm{w}(G)\ge 1\), the largest tested threshold is at most 2_B_<sub>w</sub>(_G_); if it is zero, the first run succeeds. Taking a nondecreasing envelope of the parameter bounds and absorbing the number of runs proves the claim. □

**Corollary 5.9.** _Unless_ P=NP_, there is no fixed integer t for which recognition of B(G_)=_t is NP-complete. The same conclusion holds for B_<sub>w</sub>(_G_)=_t._

## 6. Concluding remarks and questions

The composition laws quantify how global color counts couple components. For repeated copies, Theorems 4.6 and 4.11 give effective eventual formulas for both repair rules. Their slopes also decide whether the difference between the two values stays bounded. The next questions ask for structural descriptions and sharper bounds than the finite local optimizations provide.

**Problem 6.1.** Find structural or efficiently checkable versions of the criteria in Theorems 4.4 and 4.10. In particular, characterize the graphs satisfying \(B_\mathrm{w}(G)=F_{\chi(G)}(G)\), equivalently those for which weak villainy is additive over every repetition.

For either parameter _F_, the _superadditivity deficit_ is \(F(G)+F(H)-F(G\sqcup H)\); a positive value measures a failure of superadditivity.

