The two cases are separated from the threshold \(|\kappa_N|\) by at least \(3|\kappa_N|/4\), so the magnitude comparisons below can be made using a further _O(N_) bits of ordinary numerical precision. Let \(\widehat{a}_k\) denote the recovered coefficients. For _k\>D<sub>⋆</sub>_ the true coefficient vanishes, so \(|\widehat{a}_k|\le\varepsilon<|\kappa_N|\). Using \(|\#\text{MC}(H)|\ge 2\) (global spin reversal preserves the cut value),

\(|\widehat{a}_{D_\star}|\ge|\kappa_N||\#\text{MC}(H)|-\varepsilon\ge\frac{7}{4}|\kappa_N|>|\kappa_N|.\)

Hence _D<sub>⋆</sub>_ is the largest exponent whose recovered coefficient exceeds \(|\kappa_N|\) in magnitude, a threshold computable from _N_ and \(\beta\). Dividing \(\widehat{a}_{D_\star}\) by the known nonzero factor \(-\kappa_N\) yields |#MC(_H_)| to additive error at most 1/4_\<_1/2, so rounding to the unique nearest integer recovers the counts |#MC(_G_)| and |#MC(_H_)| exactly.

The same arguments apply for the single correlator \(\langle Z_rZ_s\rangle\). In that case Theorem 2.4 gives the coefficient directly without the \(-\frac{1}{2}\) factor from Eq. (30). Thus the same threshold and rounding argument recovers |#MC(_G_)| and |#MC(_H_)| directly; only the known multiplicative factor relating the extreme coefficient to the count is changed.

Finally, choose a fixed integer \(\alpha>\alpha_0+1\). Since every graph in the constructed family has \(N\ge 2\), \(b_N\le(\alpha-1)N+2\le\alpha N\). Requesting \(b=\alpha N\) in unary therefore gives the stated error bound \(2^{-\alpha N}\) with _O(N_) accuracy bits, and the recovery argument above applies.

## 3 Hardness of gradients and Hessians

Consider the setting of Theorem 1.2 where we restrict to the tied-phase line<tbc>

\(F_G(\phi):=\langle C_G\rangle_{\gamma_1=\gamma_2=\phi}.\)

<tbc>The same statements hold with _C<sub>G</sub>_ replaced by the designated observable _Z<sub>r</sub>Z<sub>s</sub>_. As above,

\(F_G(\phi)=\sum_{k=-D}^Da_ke^{ik\phi},\) (36)

where \(D\le 2|E(G)|=\text{poly}(|G|)\). For the graph G(_H_) produced by the reduction we again use that in either case by Theorem 2.4 there is a _D<sub>⋆</sub>\>_0 such that \(a_{D_\star}(G)=\kappa(H)|\#\text{MC}(H)|\), with \(\kappa(H)\neq 0\) computable from _N_ and the chosen observable. The exponent _D<sub>⋆</sub>_ itself need not be known in advance, since it contains MC(_H_). Differentiating \(F_G(\phi)\) preserves the count encoded in its extreme coefficient, giving the same hardness for derivatives along the tied cost phase.

**Theorem 3.1** (Hardness of phase derivatives)**.** _For every fixed_ \(p\ge 2\) _and every fixed integer_ \(r\ge 1\)_, exact computation of_

\(F_G^{(r)}(\phi)=\frac{dr}{d\phi^r}F_G(\phi)\)

_is_ #P_-hard under deterministic polynomial-time Turing reductions. This holds for unweighted simple connected MaxCut instances for the parameter choices of Theorem 1.2, and for both the total MaxCut expectation and the correlator_ \(\langle Z_rZ_s\rangle\).

To the best of our knowledge we are not aware of an earlier #P-hardness result for exact derivatives of the standard fixed-depth QAOA for MaxCut objective.

