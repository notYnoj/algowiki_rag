\(\sum_{g\in\mathcal{G}}\|c_g\|_2\le\tau,\) (45)

or by adding \(\lambda_1\sum_g\|c_g\|_2\) to the objective. Reweighted variants can be used after an initial solve to reduce bias and sharpen the active set. Sparsity is primarily a model-selection device: it identifies a small set of active modes from a much larger sampled dictionary. These active modes should be interpreted as candidate pole regions rather than certified continuous pole estimates; they can guide local resampling or nonlinear refinement when the data, separation, signal-to-noise ratio, and design conditioning are favorable.

## 7.2 Stability, settling, and tail budgets

A stability margin is imposed by sampling only poles with \(|p_m|\le\rho<1\). This is a hard prior; no solver constraint is needed. For pointwise impulse-response settling after time _T<sub>s</sub>_,

\(sup_{t\ge T_s}|h(t)|\le\sum_{m=1}^M|c_m||p_m|^{T_s}\le\epsilon_h.\) (46)

This mode-resolved envelope is tighter than the common- radius bound \(\rho^{T_s}\sum_m|c_m|\) when the sampled poles have different radii. For truncation error or bounded-input robustness, the relevant quantity is the \(\ell_1\) tail,

\(\sum_{t=T_s}^\infty|h(t)|\le\sum_{m=1}^M\frac{|c_m||p_m|^{T_s}}{1-|p_m|}.\) (47)

The global BIBO budget is the case _T<sub>s</sub>_=0:

\(\sum_{m=1}^M\frac{|c_m|}{1-|p_m|}\le h_\mathrm{max}.\) (48)

Similarly, the denominator |1-_p<sub>m</sub>_| belongs to step- response and DC-gain quantities. If \(s(t)=\sum_{\tau=0}^th(\tau)\), then

\(|s_\infty-s(t)|\le\sum_m\frac{|c_m||p_m|^{t+1}}{|1-p_m|}.\) (49)

For complex residues, constraints involving |_c<sub>m</sub>_| are implemented with epigraph variables \(a_m\ge|c_m|\), equivalently \(\sqrt{(\Re c_m)^2+(\unknown c_m)^2}\le a_m\), so the resulting inequalities are SOCP-representable.

## 7.3 Modal localization

Known time constants can be encoded by sampling radii near \(r=e^{-\alpha_i}\) or by imposing annular regions \(r\in[r_i^\mathrm{min},r_i^\mathrm{max}]\). Resonant bands are encoded by restricting angles \(\theta_m\in\Theta=\cup_b[\omega_b^\mathrm{min},\omega_b^\mathrm{max}]\). Soft preferences can be added through weighted penalties or through sampling distributions concentrated near expected modes. Hard exclusions, such as rejecting unstable or nonphysical modes, are enforced by simply not sampling those regions.

## 7.4 DC gain and static constraints

For

\(G(z)=D+\sum_m\frac{c_m}{1-p_mz^{-1}},\) (50)

the DC gain is

\(G(1)=D+\sum_m\frac{c_m}{1-p_m}.\) (51)

A bound \(|G(1)|\le G_\mathrm{max}\) is an SOCP constraint after splitting real and imaginary parts; a known DC gain is imposed by equality. Similar affine constraints can encode known Markov parameters, zero steady-state error under a specified input class, or sign information at selected frequencies.

## 7.5 Passivity

A finite RAF model has the parallel realization

\(A=\mathrm{diag}(p_1,\dots,p_M),B=\mathbf{1},\)<br> \(C=[c_1\cdots c_M],D\in\mathbb{R}.\) (52)

Discrete-time positive realness can be imposed by the positive-real KYP LMI (Boyd et al., 1994). In the RAF model, _A_ and _B_ are fixed by the sampled poles, while _C_ and _D_ are affine in the decision variables. The KYP condition is therefore convex in the unknowns together with the storage matrix \(P\succ 0\).

## 7.6 Monotonicity, no overshoot, and relative degree

For step monotonicity, restrict to real poles \(p_m\in(0,1)\) and impose \(c_m\ge 0\). Then \(h(t)\ge 0\) and the step response \(s(n)=\sum_{t=0}^nh(t)\) is nondecreasing. Discrete concavity or no-overshoot refinements can be written as linear inequalities because

\(\Delta(p^t)=p^t-p^{t-1}=-(1-p)p^{t-1}.\) (53)

Relative degree _r<sub>d</sub>_ is enforced by

\(\sum_{m=1}^Mc_mp_m^k=0,k=0,\dots,r_d-1.\) (54)

Equivalently, shifted features \(\phi_m^{(r_d)}(t)=p_m^{t-r_d}\mathbf{1}\{t\ge r_d\}\) can be used so that the first _r<sub>d</sub>_ taps vanish by construction.

## 7.7 Time-domain error bounds

Given measured output _y_<sub>meas</sub> and model output _y_<sub>model</sub>=_Xc+Du_, elementwise tolerance bounds are

\(-\varepsilon(t)\le y_\mathrm{meas}(t)-(Xc+Du)_t\le\varepsilon(t),t=0,\dots,T-1.\) (55)

These are linear inequalities. Windowed RMS bounds over segments can be imposed as

\(\|W_\ell(y_\mathrm{meas}-Xc-Du)\|_2\le\eta_\ell,\ell=1,\dots,K_\mathrm{win},\) (56)

which are SOCP constraints. Such constraints are useful in set-membership identification, where the model must fit the data within known time-domain uncertainty envelopes rather than merely minimize average squared error.

## 7.8 Frequency response masks

At a grid \(\omega_k\in[0,\pi]\),

\(G_k=D+\sum_{m=1}^M\frac{c_m}{1-p_me^{-i\omega_k}}\) (57)

is affine in (_c,D_). For MIMO systems, the exact constraint \(\sigma_\mathrm{max}(G_k)\le\gamma_k\) is equivalent to

\(\left[\begin{array}{ c c }
\gamma_kI & G_k \\
G_k^* & \gamma_kI
\end{array}\right]\unknown 0.\) (58)

