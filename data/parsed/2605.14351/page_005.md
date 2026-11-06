_K(s,t_)-_K(s_+1_,t_+1) is also PSD. Its diagonal moments are

\(K(0,0)=1,K(1,1)=1,K(k,k)=0(k\ge 2).\) (26)

If a positive disk measure existed, these equations would imply

\(\int 1d\mu=1,\int|p|^2d\mu=1,\int|p|^4d\mu=0.\) (27)

The last equality forces _p_=0 almost everywhere, contradicting the second. Thus shift-contractivity alone does not characterize disk moment kernels.

## 5. RADIUS NORMALIZATION AND THE NEVANLINNA-PICK CONNECTION

Nevanlinna-Pick (NP) theory is a statement about Schur- class analytic functions on the unit disk. To avoid notational ambiguity, this section uses the delay variable

\(\zeta=z^{-1},\)

so that a stable discrete-time transfer function is written as

\(H(\zeta)=D+\sum_m\frac{c_m}{1-p_m\zeta},|\zeta|<1.\) (28)

The usual frequency response is recovered by setting \(\zeta=e^{-i\omega}\). Thus the pole parameter _p<sub>m</sub>_ is the discrete-time system pole, while \(\zeta\) is the analytic variable used by Schur and NP theory.

There are two related but distinct normalizations. The first is the pole-radius normalization of the Disk-Bochner kernel. If

\(K(s,t)=\int_{|p|\le\rho} p^s\bar{p}^td\mu(p),0<\rho\le 1,\)

then

\(\widetilde{K}(s,t)=\frac{K(s,t)}{\gamma^2\rho^{s+t}}\) (29)

is, up to the scalar factor \(\gamma^{-2}\), the pole-moment kernel associated with the normalized pole coordinate \(q=p/\rho\). The corresponding defect identity is

\(\widetilde{K}(s,t)-\widetilde{K}(s+1,t+1)=\frac{\rho^2K(s,t)-K(s+1,t+1)}{\gamma^2\rho^{s+t+2}}.\) (30)

Hence support in \(|p|\le\rho\) implies the radius defect

\(\rho^2K(s,t)-K(s+1,t+1)\unknown 0.\) (31)

This is a structural pole-geometry condition.

The second normalization is the gain normalization used for NP interpolation. If

\(\|H\|_{H_\infty}:=sup_{|\zeta|<1}\|H(\zeta)\|\le\gamma,\)

then

\(F(\zeta)=\gamma^{-1}H(\zeta)\) (32)

belongs to the Schur class. Given interpolation data

\(F(\zeta_i)=W_i,|\zeta_i|<1,\)

the matrix-valued NP theorem states that a feasible Schur function exists if and only if

\(\left[\frac{I-W_iW_j^*}{1-\zeta_i\bar{\zeta}_j}\right]_{i,j}\unknown 0.\) (33)

When (33) is feasible, all solutions are parameterized by a linear fractional transformation

\(F=\mathcal{T}_\Theta[Q],Q\in\mathcal{S},\) (34)

where \(\Theta\) is determined by the interpolation data and _Q_ is a free Schur parameter. In MIMO problems this is the standard Redheffer/LFT parametrization. Thus NP theory gives an exact set-membership description of all gain-normalized analytic transfer functions satisfying the interpolation data (Sarason, 1994; Rotstein, 1996; Parrilo et al., 1998).

The pole-radius normalization \(q=p/\rho\) and the gain normalization \(F=H/\gamma\) should not be conflated. If one rewrites (28) in normalized pole coordinates \(p=\rho q\), then

\(H(\zeta)=D+\sum_m\frac{c_m}{1-\rho q_m\zeta}.\)

Equivalently, the transfer function with poles _q<sub>m</sub>_ is obtained from the scaled argument \(H(\eta/\rho)\). A Schur certificate for \(\gamma^{-1}H(\eta/\rho)\) is therefore a gain certificate for a scaled-domain function, not automatically the same as the usual unit-circle \(H_\infty\) bound for \(H(\zeta)\). In the RAF formulation we keep these roles separate: pole-radius priors are imposed by sampling \(|p_m|\le\rho\) and by the radius defect, while gain constraints are imposed directly on the transfer function in the delay variable \(\zeta\) through Pick, KYP, or frequency-grid constraints.

The RAF dictionary is then a finite-dimensional coordinate system for searching inside a Schur set-membership problem. Define the rational RAF span in the delay variable by

\(\mathcal{V}_M=\left\{\gamma^{-1}\left(D+\sum_{m=1}^M\frac{b_m}{1-p_m\zeta}\right):|p_m|\le\rho\right\}.\) (35)

For a fixed NP data set, let

\(\mathcal{F}_\mathrm{NP}=\{F\in\mathcal{S}:F(\zeta_i)=W_i,i=1,\dots,N\}\) (36)

and

\(\mathcal{F}_M=\mathcal{F}_\mathrm{NP}\cap\mathcal{V}_M,\) (37)

possibly with additional finite-dimensional convex side constraints. Then F_<sub>M</sub>_ is a certified inner approximation of the NP feasible set: every RAF model satisfying the normalized Pick or gain constraints is a member of F<sub>NP</sub>.

_Proposition 5._ (RAF inner approximation). Assume nested sampled pole sets dense in a compact subset of the open disk \(|p|<\rho\). Then:

(1) \(\mathcal{F}_M\subseteq\mathcal{F}_\mathrm{NP}\) for every _M_.<tbc>

(2) On any finite impulse-response horizon, _T_ distinct sampled poles span all length-_T_ impulse-response vectors.<tbc>

(3) In _H_<sub>2</sub>, equivalently in \(\ell_2\) impulse-response norm, the closed span of the atoms _a(p_)=(1_,p,p_<sup>2</sup>_,..._) over any set with an accumulation point in the disk is the whole space.<tbc>

(4) Simple-pole rational members of F<sub>NP</sub> whose poles are included in the dictionary are represented exactly. More general rational or Schur-feasible functions can be approximated in finite-horizon, compact-open, and _H_<sub>2</sub>-type topologies, provided the approximants are also certified by the imposed Schur/Pick or conic constraints. No equality with the full \(H_\infty\) Schur class, and no \(H_\infty\)-norm density for a fixed finite dictionary, is claimed.

