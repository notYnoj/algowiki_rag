<tbc>**Assumption 2** (Empirical per-merge degradation model, calibrated on this substrate)**.** Integrating one batch of _c_ inserts via M_<sub>c</sub>_ into _G_<sub>0</sub> (over _N_ points) reduces expected disk-graph recall@_k_, relative to a from-scratch \(\alpha\)-RNG build on the same final set, by

\(g(c,N)=min\big(g_0(L)+\Theta\big(min(c^2/N,Rc)^\psi\big),\frac{c}{N+c}\big),\) (1)

the **batch term** (M1, super-linear in _c_; _R_-cap-limited, lifted near-linearly \(\psi\approx 1\) to recall) plus a small budget-soft _V_<sub>0</sub> **floor** _g_<sub>0</sub>(_L_) (M2), capped by the batch fraction.

_Calibration (full fits, sample sizes and diagnostics in §V-B)._ The exponent is fit on two independent axes that must not be conflated. On the **topology** axis (counting missing intra-batch edges) it is \(\theta\)=1.46 (95% CI \[1.33,1.59\]), with \(b=0.50\pm 0.04\); on the **recall** axis (the one the theorem needs) _a_<sub>recall</sub>=1.28 (95% CI \[1.03,1.52\]) at _N_<sub>0</sub>=100K, and a \(\mu\)-matched three- base fit gives _a_<sub>recall</sub>=1.45. Both place the exponent above 1 (super-linear) while individual CIs are wide, so the design rests on the sign, not the value (§III-A). The fit is valid over \(0.05\le c/N\le 0.45\); below _c/N_≈0.02 the per-merge loss falls under the 0.02 pp reporting floor and is excluded from every fit, so no claim is made for _c/N\<_0.05.

**Theorem 3** (Toy bound: anti-amortization)**.** _Under Poisson inserts-only arrivals and Assumption 2, over horizon T with_ \(M=\lceil\lambda_\mathrm{ins}T/c\rceil\) _merges whose per-merge losses assemble additively as an_ upper bound _(measurement finds the assembly subadditive,_ \(\eta<1\)_, so_ \(M\cdot g\) _over-states L_<sup>∗</sup>_; §V-B), and_ \(g(c,N)=\Theta(c^aN^{-b})\) _on the calibrated range_ \(0.05\le c/N\le 0.45\),

\(L^*(c,T)\le O\big(\lambda_\mathrm{ins}Tc^{a-1}N_0^{-b}\big),a-1\in[0.03,0.52]\) _(95% CI),_ \(\hat{a}-1\approx 0.28,\) (2)

_so this upper bound is_ non-decreasing _in the merge size c (strictly increasing on the point estimate) and L_<sup>∗</sup>(_c_) _itself is measured non-decreasing directly (§V-B): the naive "batch bigger to amortize" (_\(L^*\propto 1/c\)_) is wrong in direction. Merge- induced degradation is_ irreducible by batching_, and each merge’s damage is capped by_ \(g\le c/(N+c)\)_, binding only as_ \(c\rightarrow N\).

## a) Scope of the toy bound.:

The central claim is the _sign:_ \(a\ge 1\), i.e. batching does not amortize. That sign forbids re- sizing merges as a recall lever, and it is supported by three fits on independent data (topology \(\theta\)=1.46, recall _a_=1.28 at fixed _N_<sub>0</sub>, \(\mu\)-matched recall _a_=1.45). The _magnitude_ is looser (_a_-1 could be as small as 0.03), so we rest the design on the sign, not the strength, of the super-linearity. Additive assembly is an assumption, and measurement finds it _conservative_, with twelve sequential merges at _c_=5000, _N_<sub>0</sub>=100K losing 0.38- 0.46 pp cumulatively against \(M\cdot g=1.04\) pp predicted (accumulation efficiency \(\eta\in[0.37,0.44]\)); _Mg_ thus over-states _L_<sup>∗</sup> in the conservative direction for an upper bound, though the constant is loose by \(2.3-2.7\times\). The _c_-dependence of _L_<sup>∗</sup> at horizon scale is instead _measured directly_ (§V-B(c)), where the twelve-merge run repeated across \(c\in\{1000,\dots,20000\}\) at a fixed 60K-insert horizon gives terminal recall monotonically decreasing in _c_, i.e. _L_<sup>∗</sup>(_c_) monotonically _increasing_ (0.42<tbc>

<tbc>pp over a \(20\times\) range), so anti-amortization at horizon scale is a measurement rather than an extrapolation. The same five points also corroborate the _form_. With _a_-1=0.28 from the independent single-merge fit, _L_<sup>∗</sup>(_c_)-_L_<sup>∗</sup>(_c_<sub>min</sub>)=_A(c_<sup>_a_-1</sup>-_c_<sub>min</sub><sup>_a_-1</sup>) holds with _A_ constant to \(\pm 7\%\), whereas the _c<sup>a</sup>_ construction needs _A_ to move \(4.5\times\), so the 1_/c_ merge-count factor is measured, not assumed. The _c_-trend of \(\eta\) is reference- dependent and not pinned without a measured from-scratch 160K anchor, but neither the sub-additivity nor the measured _sign_ of _L_<sup>∗</sup>(_c_) depends on that constant.

The consequence is the design principle of §IV: degradation cannot be reduced by re-sizing merges, only _re-prioritized_. Two mechanisms are isolated (Def. 1), M1 mutual invisibility (the super-linear driver, dominating \(c\unknown 0.1N\)) and a small _V_<sub>0</sub> hub-perturbation floor M2 (dominating \(c\lesssim 0.1N\)). A high- probability version also holds, since the _R_-cap gives _O(R_<sup>2</sup>) bounded influence per insert, so McDiarmid on the topology divergence and Bernstein on the (sparse, bounded) query loss give \(L^*\le\mathbb{E}[L^*](1+o(1))\) (proof in the supplementary material). Finally, small _c_ (recall-optimal) trades against tail latency (latency-optimal at large _c_: each merge inflates the tail for ≈_c/d_ seconds), the tension the scheduler navigates.

## b) The _V_<sub>0</sub> floor does not create an amortization regime.:

A natural objection: the floor _g_<sub>0</sub>(_L_) is _c_-independent, so paid once per merge it would contribute \(Mg_0=\lambda_\mathrm{ins}Tg_0/c\), _decreasing_ in _c_; adding it to the increasing batch term would produce an interior recall-optimal _c_<sup>∗</sup> and restore amortization at small _c_. Measurement settles it: over twelve merges the _V_<sub>0</sub> component _decays_ monotonically (\(4.80\rightarrow 3.43\rightarrow 2.51\rightarrow 1.38\) pp at _m_=1,4,8,12) rather than staying constant, and the cumulative loss is \(\checkmark Mg_0\). The floor is a saturating transient contributing _O_(1) rather than \(\Theta(M)\), so it generates no 1_/c_ term and _L_<sup>∗</sup>(_c_) has no interior optimum on the measured range. (The decomposition is scratch-free and not tie-aware, so its absolute magnitudes are confounded, but the conclusion rests only on the sign of the trend and the decomposition-free check \(L_\mathrm{cum}\checkmark Mg_0\).)

## c) Instantiating the constants.:

The \(\Theta(\cdot)\) hides constants we have measured, so the bound can be evaluated rather than merely asserted. On the calibrated range, with _g_ in recall points,

\(g(c,N)\approx 0.087(c/5000)^{1.28}(N/10^5)^{-0.64}\text{pp},L^*(c,T)\lesssim\big(\lambda_\mathrm{ins}T/c\big)g(c,N_0).\) (3)

Worked example: a tenant taking 10<sup>5</sup> inserts onto an _N_<sub>0</sub>=10<sup>5</sup> index at _c_=10<sup>4</sup> (_c/N_=0.1, inside range) sees _g_=0.21 pp per merge over _M_=10 merges, so \(L^*\le 2.1\) pp under additive assembly and ≈0.9 pp using the measured \(\eta\approx 0.4\); the per- merge cap _c/(N+c_)=0.091 is \(43\times\) slacker than the realized _g_<sub>frac</sub>=0.0021, so the cap is inactive, as it is everywhere below _c≈N_.

## B. The general theorem (C1-general): filtered, multi-tenant, deletes

Three assumptions lift the toy bound. The first formalizes local selectivity; the second is the modularity hinge; the third

