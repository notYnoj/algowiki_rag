It can be seen that the GPR parameter selection strategy is significantly superior to the Default strategy in most cases. For example, in  2 for \((\gamma_1,\gamma_2)=(1.4,1.4)\) and _N_=512, Default requires 18 iterations and 20.7812 s, whereas GPR requires only 14 iterations and 15.3594 s; in  2 for \((\gamma_1,\gamma_2)=(1.8,1.8)\) and _N_=512, Default requires 18 iterations and 20.4062 s, whereas GPR requires only 14 iterations and 15.9375 s. As _N_ increases, the iteration counts of GPR remain basically in the range of 13-31, exhibiting a favorable mesh-independent convergence trend; although the iteration counts of Default decrease with increasing _N_ in some test cases, they are still overall higher than those of GPR. The iteration counts and CPU times of CG grow fastest with _N_; at _N_=512, CG usually requires hundreds of iterations and hundreds of seconds of CPU time, which is far higher than those of the two multigrid methods. For a few parameter combinations, the CPU times of Default and GPR are already relatively close. However, over all test cases, the relaxation parameters predicted by GPR can effectively reduce both the iteration counts and the computing time.

**Example 5.2.** Consider the two-dimensional Riesz space fractional diffusion equation (1.1) defined on the domain \((0,1)\times(0,1)\times(0,1)\). The exact solution is given by \(u(x,y,t)=e^{-2t}sin(\pi x)sin(\pi y)\), and the initial condition is \(u_0(x,y)=sin(\pi x)sin(\pi y)\).We take _d(x,y,t_)=10<sup>-6</sup>. The source term _f_ is derived from the exact solution.

\begin{tabular}{ccccccc}
\multirow{2}{*}{\((\gamma_1,\gamma_2)\)} & \multirow{2}{*}{Method} & \multirow{2}{*}{Index} & \multicolumn{4}{c}{_N_} \\
 & & & 64 & 128 & 256 & 512 \\
\multirow{6}{*}{(1.4,1.4)} & \multirow{2}{*}{Default} & IT & 27 & 21 & 19 & 18 \\
 & & CPU & 0.1710 & 1.0781 & 3.7969 & 20.7812 \\
 & \multirow{2}{*}{GPR} & IT & 13 & 14 & 14 & 14 \\
 & & CPU & 0.0625 & 0.3596 & 2.1875 & 15.3594 \\
 & \multirow{2}{*}{CG} & IT & 97 & 161 & 278 & 447 \\
 & & CPU & 0.2969 & 2.3125 & 32.7656 & 440.1875 \\
\multirow{6}{*}{(1.5,1.6)} & \multirow{2}{*}{Default} & IT & 30 & 24 & 20 & 17 \\
 & & CPU & 0.2656 & 1.1562 & 3.5781 & 21.0781 \\
 & \multirow{2}{*}{GPR} & IT & 16 & 17 & 18 & 19 \\
 & & CPU & 0.1094 & 0.5156 & 2.8212 & 21.6406 \\
 & \multirow{2}{*}{CG} & IT & 111 & 199 & 345 & 585 \\
 & & CPU & 0.1875 & 2.5940 & 42.6407 & 552.3438 \\
\multirow{6}{*}{(1.7,1.9)} & \multirow{2}{*}{Default} & IT & 72 & 60 & 44 & 33 \\
 & & CPU & 0.3906 & 2.0469 & 7.2656 & 39.1406 \\
 & \multirow{2}{*}{GPR} & IT & 23 & 26 & 30 & 31 \\
 & & CPU & 0.0938 & 0.8125 & 4.3975 & 37.4217 \\
 & \multirow{2}{*}{CG} & IT & 155 & 303 & 567 & 1072 \\
 & & CPU & 0.2812 & 3.7969 & 67.3438 & 1067.7187 \\
\end{tabular}

2: Example 5.1

