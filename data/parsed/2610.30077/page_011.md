<tbc>itself costs no further accuracy: \(r^{n+1}G_\star=f'(\phi^{n+1})+O(\Delta t^2)\), by the standard SAV consistency argument \[18\]. A local truncation error of \(O(\Delta t^3)\), accumulated over the \(O(1/\Delta t)\) steps of a fixed time horizon, gives a global error of \(O(\Delta t^2)\) overall; this is confirmed numerically in Section 7.2, including when the trajectory is started by the (only first-order-accurate) backward-Euler step of Algorithm 1. A rigorous relative-energy error estimate, in the style of \[6\], is left for future work.

## Spatial discretisation.

Space is discretised by periodic Fourier-Galerkin collocation on an \(N\times N\) grid, without 2/3-rule dealiasing by default (Remark 4.2 discusses the optional filter used for the long-time runs). This choice is exactly what Theorem 4.1 needs: exact discrete integration by parts and the commutation \(\nabla D_2=D_2\nabla\) both hold automatically for a periodic Fourier discretisation, with no further assumption, since every pointwise product entering the proof is formed directly on the collocation grid. One technical point is worth flagging explicitly, since it is easy to get wrong and silently breaks the identity if missed: the discrete Laplacian must use the symbol \(-(k_x^2\mathbf{1}_{k_x\neq N/2}+k_y^2\mathbf{1}_{k_y\neq N/2})\), zeroing out the Nyquist-frequency contribution in each direction, rather than the naive symbol -|_k_|<sup>2</sup>. With the naive symbol, the discrete gradient and Laplacian become subtly inconsistent at the Nyquist mode, and (12) fails outright once the solution develops any content at that frequency.

## Solving the linear system.

Step 4 of Algorithm 1, a (2_N_<sup>2</sup>+1)-dimensional linear system, is solved in one of two ways: by a dense direct solve, exact up to machine precision and so used as a ground-truth reference on small grids (\(N\lesssim 40\)); or by matrix-free GMRES (the generalised minimal residual method, an iterative solver for linear systems that does not require storing the system matrix) with a Fourier-diagonal preconditioner, built from the frozen coefficients reduced to representative scalars, used on the larger grids needed for the physics study. The two methods agree to 10<sup>-12</sup> wherever both are affordable. Throughout Section 7, an independent nonlinear reference solver is also used as a cross-check: it treats \(f'(\phi^{n+1})\) fully implicitly by Newton iteration, with no SAV device at all, on the identical spatial discretisation, so that any disagreement with the SAV scheme isolates exactly the effect of the SAV reformulation, and nothing else.

\begin{tabular}{cc}
\multicolumn{2}{c}{**One time step of the SAV-BDF2 scheme, level** \(n\rightarrow n+1\) **(for** \(n\ge 1\)**).**} \\
1. & **Extrapolate:** \(\phi^\star\leftarrow 2\phi^n-\phi^{n-1}\). \\
2. & **Clamp:** \(\phi_b^\star\leftarrow\mathrm{clamp}(\phi^\star,\delta_c,1-\delta_c)\). \\
3. & **Freeze coefficients:** \\
\(b_\star,c_\star,A_\star,\kappa_\star\leftarrow b(\phi_b^\star)\), \(c(\phi_b^\star)\), \(A(\phi_b^\star)\), \(\kappa(\phi_b^\star)\), \(G_\star\leftarrow f'(\phi^\star)/\sqrt{E_f(\phi^\star)+C_0}\). \\
4. & **Solve** the linear system (S1)-(S4) for \((\phi^{n+1},\mu^{n+1},q^{n+1},r^{n+1})\). \\
5. & **Filter (optional):** \(\phi^{n+1}\leftarrow F\phi^{n+1}\), \(q^{n+1}\leftarrow Fq^{n+1}\) (2/3-rule; long-time runs of Section 7.3 only, Remark 4.2). \\
6. & Advance \(n\leftarrow n+1\) and repeat until _t=T_. \\
\end{tabular}

Algorithm 1: The computation performed at every step. Steps 1-3 cost _O(N_<sup>2</sup>log_N_) (a handful of FFTs); step 4 dominates the per-step cost (Section 7.2), by one of the two methods described below. The very first step (_n_=0) skips steps 1-3 (\(\phi^\star:=\phi^0\), nothing to extrapolate yet) and replaces step 4 by the first-order backward-Euler start of Section 3, or its Richardson-extrapolated variant.

