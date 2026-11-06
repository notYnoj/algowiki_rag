Directional SOCP approximations use fixed input directions \(v_\ell\):

\(\|G_kv_\ell\|_2\le\gamma_k,\ell=1,\dots,L_\mathrm{dir}.\) (59)

Input/output weights are included by replacing _G<sub>k</sub>_ with \(W_\mathrm{out}(\omega_k)G_kW_\mathrm{in}(\omega_k)\). These constraints provide grid-based frequency shaping within the same convex RAF estimation problem. A true full-band \(H_\infty\) certificate requires an additional bounded-real/KYP or equivalent robust-control condition rather than only a finite frequency grid.

### 7.9 Master problem

Combining these pieces gives a representative convex program. Let \(y_{t,m}^\mathcal{A}=(\phi_m*u)(t)\) and _y_<sub>model</sub>=_y_<sup>A</sup>_c+Du_. The objective is

\(\mathrm{min}_{c,D}\frac{1}{2}\|y_\mathrm{meas}-y^\mathcal{A}c-Du\|_2^2+\lambda_2\|c\|_2^2+\lambda_1\sum_{g\in\mathcal{G}}\|c_g\|_2.\) (60)

Representative optional constraints include

\(-\varepsilon\le y_\mathrm{meas}-y^\mathcal{A}c-Du\le\varepsilon,\) (61)

\(\|W_k(y_\mathrm{meas}-y^\mathcal{A}c-Du)\|_2\le\eta_k,k=1,\dots,K_\mathrm{win},\) (62)

\(G_k=D+\sum_{m=1}^M\frac{c_m}{1-p_me^{-i\omega_k}},k=1,\dots,K_\mathrm{in},\) (63)

\(\|G_kv_\ell\|_2\le\gamma_k,\ell=1,\dots,L_\mathrm{dir},\) (64)

\(\sum_{m=1}^Ma_m|p_m|^{T_s}\le\epsilon_h,\) (65)

\(\sum_{m=1}^M\frac{a_m}{1-|p_m|}\le h_\mathrm{max},\) (66)

\(\sum_{m=1}^Mc_mp_m^k=0,k=0,\dots,r_d-1,\) (67)

\(G(1)=D+\sum_{m=1}^M\frac{c_m}{1-p_m},\) (68)

\(|G(1)|\le G_\mathrm{max}.\) (69)

Here \(a_m\ge|c_m|\) are epigraph variables, implemented as second-order cones for complex residues. Monotone real- pole models add \(c_m\ge 0\) for \(p_m\in(0,1)\). All constraints above are linear, SOCP, or LMI representable after splitting complex variables into real and imaginary parts. Hard pole priors do not appear as constraints because they are already encoded in the sampled dictionary.

### 7.10 Pole localization and refinement

The convex RAF stage chooses residues over a fixed sampled pole dictionary and therefore does not solve the continuous nonlinear pole-estimation problem. The active RAF atoms should be interpreted as candidate pole regions, not as certified continuous pole estimates. Pole localization from a finite sampled pole dictionary requires additional assumptions: informative data, sufficiently separated true poles, low noise, adequate signal strength, and favorable conditioning of the normalized input-filtered design. Dictionary density alone is insufficient, since nearby

**Algorithm 1** Constrained Randomized Atomic Identification

1: **Inputs:** data (_u,y_); admissible pole region P; priors; number of atoms _M_.

2: Sample _p<sub>m</sub>_ i.i.d. in P and pair conjugates for real outputs.

3: Form the convolved design \(y_{t,m}^\mathcal{A}=(\phi_m*u)(t)\) and the parallel realization with _A_=diag(_p<sub>m</sub>_).

4: Solve the convex master problem with selected QP/SOCP/LMI constraints.

5: Prune active groups and optionally resample or refine locally around active poles.

6: **Return:** \(\widehat{h}(t)=\sum_m\widehat{c}_mp_m^t\) and \(\widehat{G}(z)=\widehat{D}+\sum_m\widehat{c}_m/(1-p_mz^{-1})\).

disk-pole atoms become highly coherent over any finite horizon; a sparse solver may select one of several nearly equivalent atoms, or a small cluster of atoms, without uniquely identifying the true pole.

In practice, we use the sparse RAF solution as a convex initialization. Active atoms are clustered in the pole plane, preferably using a disk-aware metric such as the pseudo- hyperbolic distance in (43). Cluster representatives then initialize a local nonlinear pole/residue fit, or a prediction- error refinement, subject to the same stability and prior constraints. The refined model should be validated by simulation error, frequency-domain fit, residual checks, and model-order diagnostics. This two-stage strategy preserves convexity in the main selection step while using the active support only as a warm start for continuous refinement; exact model-order or pole recovery is not guaranteed by dictionary density alone.

## 8. COMPUTATIONAL AND MODELING CONSIDERATIONS

This section collects practical considerations. The RAF estimator has three distinct approximation layers. The first is the modeling approximation: the true impulse response is approximated by a superposition of stable first-order atoms. The second is the random-feature approximation: a finite sampled dictionary approximates a continuous pole measure or atomic set. The third is the statistical approximation: the coefficients are estimated from finite, noisy, and possibly poorly exciting data. These layers should be kept conceptually separate. Increasing the number of sampled atoms improves dictionary resolution but can worsen conditioning. Increasing the data length improves statistical estimation but may not help identify modes that are not excited by the input. Adding physical constraints can reduce variance and rule out spurious explanations, but overly restrictive priors can bias the result.

### 8.1 Choice of sampling law and number of atoms

The sampling law is the primary mechanism for encoding qualitative model knowledge. A uniform distribution over the disk is rarely the best engineering choice. For lightly damped mechanical or electrical systems, radii near the stability boundary and angles in expected resonance bands are often more important than strongly damped modes. For thermal or diffusion-dominated systems, real positive

