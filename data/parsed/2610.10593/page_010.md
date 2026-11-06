## 4 Rigorous verification

Let _E_pub denote the retained exponent computed with exact maximum-entropy penalties, and let \(\widehat{E}\) denote the value in (11), using the positive-factor bounds (4). Since these bounds only increase the penalties, and all mass weights are nonnegative,

\(\widehat{E}\le E_\mathrm{pub}.\) (19)

Every sum and minimum occurring after the replacement is coordinatewise nondecreasing, which preserves this inequality.

**Proposition 1** (Certificate implication)**.** _For admissible parameters, suppose the six-copy construction gives the conservative retained exponent_ \(\widehat{E}\)_, common matrix-size exponent M\>_0_, and rank exponent C. Then_

\(\omega\le\frac{C-\widehat{E}}{M}.\)

_Consequently, a rational target_ \(\tau\) _satisfying_ \(\widehat{E}+\tau M-C>0\) _proves_ \(\omega<\tau\).

_Proof._ The combination-loss theorem [2], in the formulation of [9, Theorem 1], together with the asymptotic sum inequality [13], gives \(E_\mathrm{pub}+M\omega\le C\). Apply (19), divide by _M\>_0, and rearrange the strict feasibility inequality.

### 4.1 Exact checks and interval evaluation

The witness is a JSON file containing integer numerators for the probabilities and entropy-dual factors, together with node shapes, levels, regional data, and child references. Both declared denominators are 2<sup>96</sup>. The checker reconstructs the distributions on ordinary ordered ternary strings, without importing the optimizer or its orbit representation. It checks the integer types, support, nonnegativity, normalization, strictly positive dual factors, child levels and shapes, complementary split indices, and leaf-parameter ranges. The directed graph represents the recursively unfolded parameter tree; the validity of mass accumulation under this sharing is proved in Lemma 1.

All probability and mass arithmetic is exact rational arithmetic. Every logarithm is enclosed using a positive series with an explicit remainder bound and outward rounding on a 2<sup>-192</sup> grid, as detailed in Lemma 2. Subsequent expressions are evaluated by rational interval operations. In particular, for \(x_i\in[a_i,b_i]\), the checker uses

\(\mathrm{min}_ix_i\in[\mathrm{min}_ia_i,\mathrm{min}_ib_i].\)

It explicitly sums the physical-coordinate contributions of all six global copies and six local regions, and then applies the original regional minima. This provides a second implementation of the symmetry reduction used during optimization.

2 gives outward decimal enclosures for the final calculation. Each printed endpoint denotes an exact terminating rational number; the accompanying result file contains the full rational endpoints. The interval for \(\widehat{\Omega}\) encloses the value of \((C-\widehat{E})/M\) for this particular witness. It is not a two-sided estimate of \(\omega\) and does not establish global optimality.

At the exact rational target \(\tau=2.37115924\), the checker obtains

\(\widehat{E}+\tau M-C\in[8.5159631350886\cdot 10^{-9},8.5159631350887\cdot 10^{-9}].\) (20)

The positive lower endpoint supplies the strict inequality, with _M\>_0 certified separately.

