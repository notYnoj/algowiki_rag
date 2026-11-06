**Corollary 4.1** (Unconditional energy stability)**.** _Since every term after_ E<sup>_n_+1</sup>-E_<sup>n</sup> in_ (12) _is non-negative,_

\(\mathcal{E}^{n+1}\le\mathcal{E}^n\text{\textit{for every}}\Delta t>0.\)

_That is, the SAV-BDF2 scheme is unconditionally energy stable: the modified discrete energy never increases, at any step size. Since additionally_ \(\mathcal{E}^n\ge-C_0\) _is bounded below, the monotone sequence_ {E_<sup>n</sup>_} _converges._

**Remark 4.1** (The discrete energy bounds the solution)**.** Corollary 4.1 says that the modified energy E_<sup>n</sup>_ never increases. A decreasing energy is only useful if it also limits how large the fields can become. This is indeed the case.

The energy E_<sup>n</sup>_ is a sum of squares of \(\nabla\phi\), _q_ and _r_ at the two stored time levels _n_ and _n_-1. The two levels are combined through the form \(\Phi(u,v)=\|u\|^2+\|2u-v\|^2\). This combination is positive: it vanishes only if _u=v_=0, and it is bounded below and above by multiples of \(\|u\|^2+\|v\|^2\). Consequently, E_<sup>n</sup>+C_<sub>0</sub> is never smaller than a fixed positive multiple of

\(\gamma\left(\|\nabla\phi^n\|^2+\|\nabla\phi^{n-1}\|^2\right)+\|q^n\|^2+\|q^{n-1}\|^2+2\left((r^n)^2+(r^{n-1})^2\right).\)

Since \(\mathcal{E}^n\le\mathcal{E}^1\) for all \(n\ge 1\), none of these terms can exceed a fixed multiple of E<sup>1</sup>+_C_<sub>0</sub>. Hence \(\|\nabla\phi^n\|\), \(\|q^n\|\) and |_r<sup>n</sup>_| stay bounded for all times and for every \(\Delta t>0\).

Of the three quantities just bounded, _r_ already carries the effect of the bulk term \(E_f(\phi)\) by construction. What remains uncontrolled is \(\phi\) itself: E_<sup>n</sup>_ reaches \(\phi\) only through \(\nabla\phi\), and a gradient cannot see an additive constant, since \(\phi\) and \(\phi+\) const have the same gradient. The size of \(\phi\) itself is therefore controlled separately. By mass conservation (Proposition 5.1), the spatial average of \(\phi^n\) equals its initial value at every step. A field with fixed average and bounded gradient on a periodic domain cannot be arbitrarily large (Poincaré inequality), so \(\|\phi^n\|\) is bounded as well.

In summary, the numerical solution cannot blow up: \(\phi\), _q_ and _r_ remain bounded at all times, whatever the time step.

**Remark 4.2** (Stability of the filtered scheme actually used)**.** The long-time physics runs (Section 7.3) apply an optional 2/3-rule spectral filter _F_ to \((\phi,q)\) after every step (removing aliasing noise from evaluating nonlinear coefficients on the collocation grid). Since _F_ is an orthogonal, \(\nabla\)-commuting projection, a short argument (filtering cannot increase \(\Phi\): \(\Phi(Fu,v)=\Phi(u,v)-5\|(I-F)u\|^2\) for _Fv=v_; Appendix A) shows (12) extends exactly to the filtered scheme, with two explicit additional non-negative terms penalising the filtered-out content. Hence, the scheme actually producing the physics results shown in Section 7.3 is itself provably (not just empirically) stable for the same energy. We also confirmed numerically that both terms stay strictly positive, with genuine margin and not merely at round-off, over real trajectories.

**Remark 4.3** (Stability \(\neq\) accuracy)**.** Equation (12) does not show that \(\widetilde{\mathcal{D}}^{n+1}\), built from the extrapolated mobilities, approximates the physical dissipation D to second order under all circumstances. That is a consistency question settled, numerically in Section 7. Also, \(\mathcal{E}^n\neq E(\phi^n,q^n)\): the \(\Phi\)-form and (_r<sup>n</sup>_)<sup>2</sup>-_C_<sub>0</sub> each differ from the corresponding true quantities by \(O(\Delta t^2)\) (measured \(\approx 7\times 10^{-6}<\Delta t^2\)), so E_<sup>n</sup>_ decreases monotonically while \(E(\phi^n,q^n)\) may show \(O(\Delta t^2)\) non-monotonicities. Every figure claiming "energy decay" states which energy.

## 5 Structural properties

Section 4 showed that _if_ a solution of (S1)-(S4) exists at a given step, the discrete energy identity forces it to be well behaved: the modified energy can only decrease. That conditional phrasing hides a question energy stability alone does not answer: does (S1)-(S4), a linear system coupling four unknown fields at every step, actually _have_ a solution there, and is it unique? A scheme that<tbc>

