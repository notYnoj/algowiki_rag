<tbc> 4.2 reports the methods used in the numerical experiments.

During the first iterations, the perturbation size _t_ has little effect on the difference between deflated CG and \(\mathbf{PCG}(U^{\theta_m})\). Their convergence curves separate mainly near the end of the iteration history, once the error is small. For both \(\rho=0.9\) and \(\rho=0.94\), \(\mathbf{PCG}(U^{\theta_m})\) substantially improves upon CG and closely follows deflated CG at moderate accuracy. The difference is most visible at high accuracy and for the largest perturbation, _t_=1; it narrows for _t_=10<sup>-3</sup> and 10<sup>-6</sup>. Increasing _k_ from 60 to 80 reduces the gap between \(\mathbf{PCG}(U^{\theta_m})\) and deflated CG, especially during the final iterations. Increasing _k_ removes more of the largest eigenvalues and decreases \(\lambda_k\). Consequently, the terms \(q_k^{2\ell}\) and \(\ell q_k^{2\ell-1}\) in the perturbation remainder are reduced.

Thus, _t_ primarily affects the number of late iterations, rather than the initial convergence rate. PCG with \(\theta_m\) retains most of the benefit of deflation but may require a few additional iterations at high accuracy. This cost can be modest relative to constructing the deflation projector, which requires _k_ matrix-vector products with _A(t_). The preconditioned approach is therefore especially attractive when these products are expensive. The same conclusion holds for \(\mathbf{PCG}(U^{\lambda_k})\), although \(\mathbf{PCG}(U^{\theta_m})\) performs better, consistently with Proposition 3.9.

\begin{tabular}{cc}
Method & Description \\
**CG** & CG applied to _A(t)x=b_, starting with _x_<sub>0</sub>=_z_<sub>0</sub> \\
**Deflated CG** & CG applied to the projected system _P(t)A(t)z=P(t)b_ \\
\(\mathbf{PCG}(U^{\theta_m})\) & CG applied to \(U^\theta A(t)U^\theta y=U^\theta b\), with \(\theta=\theta_m\) and \(x=U^\theta y\) \\
\(\mathbf{PCG}(U^{\lambda_k})\) & CG applied to \(U^\theta A(t)U^\theta y=U^\theta b\), with \(\theta=\lambda_k\) and \(x=U^\theta y\) \\
\end{tabular}

CG
PCG(U
PCG(U
Deflated CG
t = 1
t = 0.001
t = 1e - 06
100
100
100
100
10-3
10-3
10-3
10-3
10-6
10-6
10-6
10-6
10-9
10-9
10-9
10-9
10-12
10-12
10-12
0
30
60
90
120
0
30
60
90
120
0
30
60
90
120
100
100
100
100
10-3
10-3
10-3
10-6
10-6
10-6
10-9
10-9
10-9
10-12
10-12
10-12
0
30
60
90
120
0
30
60
90
120
0
30
60
90
120
Iteration l
Iteration l
Iteration l

4.2

_Description of methods used in the numerical experiments_

Fig. 4.3. _Squared energy-norm convergence for_ \(\rho=0.9\)_. The top and bottom rows correspond to k_=60 _and k_=80_, respectively; from left to right, the columns correspond to t_=1,10<sup>-3</sup>_, and_ 10<sup>-6</sup>.

