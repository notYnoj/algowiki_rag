**Example 1.** In this example, we consider a wave equation (1.1) with

\(d=2,\Omega=(0,1)\times(0,1),T=1,-\psi_1(x)=\psi_0(x)=x_1(x_1-1)x_2(x_2-1),\)<br>
\(f(x,t)=\mathrm{exp}(-t)(x_1(x_1-1)x_2(x_2-1)-2(x_1(x_1-1)+x_2(x_2-1))).\)

The exact solution of Example 1 is given by

\(u(x,t)=\mathrm{exp}(-t)x_1(x_1-1)x_2(x_2-1).\)

Applying the solver aforementioned for Example 1, the corresponding numerical results are presented.  1 shows that (i) MINRES-\(\mathcal{P}_\alpha\) is considerably more efficient than MINRES-P<sub>1</sub> in terms of computational time and iteration number, while the accuracy of both solvers are roughly the same; (ii) the convergence rate (i.e., the iteration number) of MINRES-\(\mathcal{P}_\alpha\) does not deteriorate as the temporal or spatial girds get refined. Evidently, the optimality of the proposed preconditioner is demonstrated, namely, the complexity of the proposed MINRES-\(\mathcal{P}_\alpha\) is merely proportional to the complexity of the matrix-vector multiplication.

As shown in  2, the errors by all solvers adopted are roughly the same. In fact, the errors of all solvers tested in this section are always roughly the same in each example. For this reason, we will skip the results of \(\mathrm{E}_{\tau,h}\) in the subsequent example.

\begin{tabular}{ccccccccc}
\multirow{2}{*}{\(\tau\)} & \multirow{2}{*}{_h_} & \multirow{2}{*}{DoF} & \multicolumn{2}{c}{MINRES-\(\mathcal{P}_\alpha\)} & \multicolumn{2}{c}{MINRES-P<sub>1</sub>} & \multicolumn{2}{c}{MINRES-_I<sub>mn</sub>_} \\
 & & & Iter & CPU(s) & Iter & CPU(s) & Iter & CPU(s) \\
\multirow{4}{*}{2<sup>-4</sup>} & 2<sup>-4</sup> & 3600 & 2 & 0.0059 & 140 & 0.21 & 614 & 0.12 \\
 & 2<sup>-5</sup> & 15376 & 2 & 0.015 & 87 & 0.31 & 1992 & 2.10 \\
 & 2<sup>-6</sup> & 63504 & 2 & 0.030 & 223 & 1.97 & 7659 & 44.38 \\
 & 2<sup>-7</sup> & 258064 & 2 & 0.089 & 476 & 12.12 & 30491 & 308.83 \\
\multirow{4}{*}{2<sup>-5</sup>} & 2<sup>-4</sup> & 7200 & 2 & 0.0089 & 146 & 0.27 & 1204 & 0.27 \\
 & 2<sup>-5</sup> & 30752 & 2 & 0.019 & 332 & 1.64 & 2574 & 5.13 \\
 & 2<sup>-6</sup> & 127008 & 2 & 0.049 & 710 & 9.35 & 7897 & 57.41 \\
 & 2<sup>-7</sup> & 516128 & 2 & 0.16 & 797 & 37.34 & 29386 & 564.35 \\
\multirow{4}{*}{2<sup>-6</sup>} & 2<sup>-4</sup> & 14400 & 2 & 0.013 & 198 & 0.67 & 3388 & 2.75 \\
 & 2<sup>-5</sup> & 61504 & 2 & 0.026 & 556 & 4.49 & 4695 & 25.13 \\
 & 2<sup>-6</sup> & 254016 & 2 & 0.084 & 1567 & 36.79 & 9331 & 84.19 \\
 & 2<sup>-7</sup> & 1032256 & 2 & 0.31 & 6498 & 625.95 & 27664 & 1138.95 \\
\multirow{4}{*}{2<sup>-7</sup>} & 2<sup>-4</sup> & 28800 & 2 & 0.017 & 236 & 1.17 & 11632 & 22.26 \\
 & 2<sup>-5</sup> & 123008 & 2 & 0.049 & 804 & 10.19 & 13062 & 87.66 \\
 & 2<sup>-6</sup> & 508032 & 2 & 0.014 & 3334 & 151.62 & 17164 & 314.98 \\
 & 2<sup>-7</sup> & 2064512 & 2 & 0.83 & 8445 & 2233.43 & 34255 & 2941.73 \\
\end{tabular}

1: Iteration numbers and CPU times of MINRES-\(\mathcal{P}_\alpha\), MINRES-P<sub>1</sub>, and MINRES-_I<sub>mn</sub>_ for Example 1.

