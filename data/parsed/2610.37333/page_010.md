deadband, the statistic that decides the order, and the handling of startup and failures. `JBDF` and `JIDA` follow their SUNDIALS references \[31, 63\], while `JNDF` follows the adaptive scheme of Shampine and Reichelt \[35\] adopted by `QNDF` \[34\].

\begin{tabular}{cccc}
 & **JBDF** & **JIDA** & **JNDF** \\
Deadband & Hold for \(\eta<1.5\) and grow otherwise. An accepted step never reduces _h_. & Hold for \(1<\eta<2\). Growth is restricted to doubling and reductions to factors in \[0.5, 0.9\]. & Hold within a constant-step window lasting through _q_+2 consecutive constant steps. A steady-state window suppresses mild reductions, but an accepted step may reduce _h_. \\
Order statistic & Largest candidate growth factor among _q_-1, _q_, and _q_+1. & Smallest scaled truncation-error estimate among _q_-1, _q_, and _q_+1. & Largest proposed step size among _q_-1, _q_, and _q_+1. \\
Order cadence & Only after a wait counter expires. The wait is _q_+1 steps after an order change and at least two otherwise. & Every accepted step. Order increases require constant-(_h,q_) history. & Every accepted step. \\
Startup & No separate regime. The first-step growth cap is large. & After the first accepted step, increase the order and double _h_ until the order stops increasing or a step fails. & No separate regime. \\
Failure recovery & Progressively reduce _h_, possibly lower the order, and restart at order 1 if necessary. Suppress further changes on the first accepted recovery step. & The first rejection reduces _h_ and may lower the order, the second applies a fixed reduction, and the third forces order 1. Convergence failures reduce _h_ and refresh _J_. & The second consecutive rejection halves _h_, the third lowers the order, and a fourth rejection at order 1 restarts the history. \\
\end{tabular}

1: Comparison of step-size and order control in the three solvers. After each accepted step, all three form \(\eta\propto\mathrm{err}^{-1/(q+1)}\) and suppress changes in _h_ that do not justify refactorizing _W<sub>n</sub>_.

