<tbc>It can be seen that the GPR parameter selection strategy is overall significantly superior to Default. For example, for \((\gamma_1,\gamma_2)=(1.2,1.2)\) and _N_=512, Default requires 21 iterations and 23.8595 s, whereas GPR requires only 14 iterations and 17.0781 s; for \((\gamma_1,\gamma_2)=(1.8,1.8)\) and _N_=512, Default requires 18 iterations and 20.4062 s, whereas GPR requires only 14 iterations and 15.9375 s. As _N_ increases, the iteration counts of GPR remain basically stable at 13-14, exhibiting a favorable mesh-independent convergence trend; although the iteration counts of Default also decrease with increasing _N_, they are still overall higher than those of GPR, and the gap is particularly evident at _N_=64 and _N_=128. The iteration counts and CPU times of CG grow fastest with _N_; at _N_=512, CG usually requires hundreds of iterations and hundreds of seconds of CPU time. For instance, for \((\gamma_1,\gamma_2)=(1.8,1.8)\), CG requires 568 iterations and 688.1875 s, which is far higher than those of the two multigrid methods. For a few parameter combinations (such as \((\gamma_1,\gamma_2)=(1.5,1.5)\) and _N_=512), the CPU times of Default and GPR are already relatively close, but GPR is still no worse than Default. Over all test cases, the relaxation parameters predicted by GPR can effectively reduce both the iteration counts and the computing time, further verifying the effectiveness and superiority of the data-driven parameter selection strategy for accelerating the multigrid method.

## 6. Conclusion

In this paper, the weighted Jacobi method is adopted as the smoother in a multigrid method for solving the two-dimensional Riesz space fractional diffusion equation. To address the problem of relaxation parameter selection, a GPR-based parameter selection strategy is proposed. Numerical experiments verify the correctness of the relevant theory and confirm the high computational efficiency of this data-driven algorithm. Moreover, the combination of neural networks and traditional numerical methods has become increasingly important in<tbc>

\begin{tabular}{ccccccc}
\multirow{2}{*}{\((\gamma_1,\gamma_2)\)} & \multirow{2}{*}{Method} & \multirow{2}{*}{Index} & \multicolumn{4}{c}{_N_} \\
 & & & 64 & 128 & 256 & 512 \\
\multirow{6}{*}{(1.2,1.2)} & \multirow{2}{*}{Default} & IT & 39 & 29 & 22 & 21 \\
 & & CPU & 0.1875 & 1.2812 & 4.0469 & 23.8595 \\
 & \multirow{2}{*}{GPR} & IT & 13 & 14 & 14 & 14 \\
 & & CPU & 0.0781 & 0.5312 & 2.8906 & 17.0781 \\
 & \multirow{2}{*}{CG} & IT & 71 & 117 & 189 & 302 \\
 & & CPU & 0.2031 & 1.3906 & 22.8125 & 397.6406 \\
\multirow{6}{*}{(1.5,1.5)} & \multirow{2}{*}{Default} & IT & 30 & 24 & 17 & 16 \\
 & & CPU & 0.3281 & 1.0625 & 3.2188 & 18.4712 \\
 & \multirow{2}{*}{GPR} & IT & 13 & 13 & 13 & 14 \\
 & & CPU & 0.1406 & 0.3125 & 2.4219 & 16.5000 \\
 & \multirow{2}{*}{CG} & IT & 72 & 125 & 215 & 369 \\
 & & CPU & 0.1406 & 1.5469 & 24.6250 & 419.6719 \\
\multirow{6}{*}{(1.8,1.8)} & \multirow{2}{*}{Default} & IT & 59 & 49 & 34 & 18 \\
 & & CPU & 0.2970 & 1.7500 & 6.0938 & 20.4062 \\
 & \multirow{2}{*}{GPR} & IT & 14 & 14 & 14 & 14 \\
 & & CPU & 0.0781 & 0.3906 & 2.7031 & 15.9375 \\
 & \multirow{2}{*}{CG} & IT & 83 & 161 & 302 & 568 \\
 & & CPU & 0.2031 & 2.1406 & 36.0000 & 688.1875 \\
\end{tabular}

3: Example 5.2

