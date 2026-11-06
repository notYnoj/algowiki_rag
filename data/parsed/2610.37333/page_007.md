Predict Extrapolate the accepted history at trial (h, qn) to initialize yn+1 (0)
Form the implicit corrector Construct the nonlinear system Gn (yn+1) = 0
Linear-solver setup gate Reuse the saved Jn and factors of Wn, or update Jn and refactorize Wn
Modified Newton correction Solve Wn8(m) = - - (m), then set yn+1 (m+1) = yn+1 + 8(m)
iterate
Newton status
converged
Retry the trial step Error rejection reduces hn and may lower qn. Nonlinear failure refreshes Jn and Wn and may reduce hn
reject
Local error | |
| |
accept
Accept the step Commit yn+1 and update the multistep history and local-error estimates
VSVO controller
n n+1
Compare qn 1, qn, and qn + 1, then choose hn+1 and qn+1

Figure 1: Control flow of one trial step in a variable-step, variable-order implicit multistep integrator. The predictor extrapolates the accepted history at (_h<sub>n</sub>,q<sub>n</sub>_), and a modified Newton iteration solves the corrector equation using reused or refreshed sparse LU factors of _W<sub>n</sub>_. Blue boxes mark the linear-solver work that dominates the cost for large systems. A step attempt can fail from the nonlinear solve if the Newton increments diverge or their contraction rate predicts that the corrector cannot reach tolerance within the iteration budget. Additionally, the step can be rejected if the corrector converges, but the weighted local-error estimate exceeds tolerance. Before retrying the same step, nonlinear failure refreshes _J<sub>n</sub>_ and _W<sub>n</sub>_ and may reduce _h<sub>n</sub>_, while error rejection reduces _h<sub>n</sub>_ and may lower _q<sub>n</sub>_. Acceptance commits the history and advances to the next step at (_h_<sub>_n_+1</sub>_,q_<sub>_n_+1</sub>).

