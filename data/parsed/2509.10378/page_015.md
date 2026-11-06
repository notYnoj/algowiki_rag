<tbc>surprising that this relation is approximately learned for \(\kappa\) near criticality.  5 shows that the transformed gauge configurations are effective at generating preconditioning operators for the original linear operators, only marginally worse compared to the neural network-produced \(\tilde{U}_\mu(x)\). However, the slightly inferior performance of \(\tilde{U}_\mu^\text{simple}(x)\) constructed from this simple relationship, suggests that correlations in the changes from \(U_\mu(x)\) to \(\tilde{U}_\mu(x)\) across \(\mu\) and _x_ are important relative to the learned \(\tilde{U}_\mu(x)\). We leave further investigation in future work.

## 5 Conclusion

In this work, we have proposed an operator learning-based neural preconditioner framework for Wilson-Dirac normal equations in the lattice gauge theory. Note that although this study focuses solely on Wilson-discretized Dirac operators, the proposed framework is applicable to other discretization schemes whose operators share the same structure as the constructed preconditioners. Our method is matrix-free and efficient to train. Once trained, it is immediately applicable for different lattice geometries and parameter ranges, achieving the same level of performance as models tailored to specific problems. Such preconditioners are effective in accelerating the convergence of CG solvers by reducing the number of iterations required, while maintaining per-step efficiency<tbc>

\begin{tabular}{cccc}
 & _L_=8 & _L_=16 & _L_=32 \\
Unprecond. & 78 \(\pm\) 4 & 201 \(\pm\) 14 & 548 \(\pm\) 41 \\
\(U_\mu^\text{simple}(x)\)-precond. & 43 \(\pm\) 2 & 104 \(\pm\) 7 & 278 \(\pm\) 20 \\
\(\mathcal{N}_L^\text{FNO}\)-precond. & 40 \(\pm\) 2 & 99 \(\pm\) 7 & 267 \(\pm\) 21 \\
\end{tabular}

