spatial grid) and hence the time space matrix becomes

\(\left[\begin{array}{ c c c c c }
L_\bar{a} &  &  &  &  \\
-2I_m & L_\bar{a} &  &  &  \\
L_\bar{a} & -2I_m & L_\bar{a} &  &  \\
 & \ddots & \ddots & \ddots &  \\
 &  & L_\bar{a} & -2I_m & L_\bar{a}
\end{array}\right],\) (3.3)

where \(L_\bar{a}=I_m-\frac{\bar{a}\tau^2}{2}\Delta_h\in\mathbb{R}^{m\times m}\) with \(\Delta_h\) denoting the discretization matrix for the constant Laplacian operator. Then, both our proposed preconditioner \(\mathcal{P}_\alpha\) and P<sub>1</sub> for the matrix (3.3) are fast invertible. Thus, we use them as the preconditioners for (3.2) and test their performance on Example 2.

**Example 2.** In this example, we consider the wave equation (3.1) with

\(d=2,\Omega=(0,1)\times(0,1),T=1,\psi_1(x)=\psi_0(x)=x_2(1-x_2)x_1(1-x_1),\)<br>
\(a(x)=(30+sin(x_1)^2)(30+sin(x_2)^2),\)<br>
\(f(x,t)=exp(t)[x_1(1-x_1)x_2(1-x_2)-sin(2x_1)(30+sin(x_2)^2)(1-2x_1)x_2(1-x_2)\)<br>
\(-sin(2x_2)(30+sin(x_1)^2)(1-2x_2)x_1(1-x_1)+2a(x)(x_1(1-x_1)+x_2(1-x_2))].\)

We apply MINRES-\(\mathcal{P}_\alpha\) and MINRES-P<sub>1</sub> for Example 2. s 3 shows that (i) MINRES- \(\mathcal{P}_\alpha\) is much more efficient than MINRES-P<sub>1</sub> in terms of iteration number and computational time while accuracy of the both solvers are roughly the same; (ii) iteration number of MINRES- \(\mathcal{P}_\alpha\) is stable with respect to changes of \(\tau\) and _h_.

\begin{tabular}{ccccccccc}
\multirow{2}{*}{\(\tau\)} & \multirow{2}{*}{_h_} & \multirow{2}{*}{DoF} & \multicolumn{2}{c}{MINRES-\(\mathcal{P}_\alpha\)} & \multicolumn{2}{c}{MINRES-P<sub>1</sub>} & \multicolumn{2}{c}{MINRES-_I<sub>mn</sub>_} \\
 & & & Iter & CPU(s) & Iter & CPU(s) & Iter & CPU(s) \\
\multirow{4}{*}{2<sup>-4</sup>} & 2<sup>-4</sup> & 3600 & 8 & 0.015 & 415 & 0.54 & 3046 & 0.62 \\
 & 2<sup>-5</sup> & 15376 & 8 & 0.032 & 1719 & 6.31 & 12891 & 12.84 \\
 & 2<sup>-6</sup> & 63504 & 8 & 0.084 & 7100 & 62.41 & 52655 & 301.21 \\
 & 2<sup>-7</sup> & 258064 & 8 & 0.24 & 28911 & 711.78 & _\>_200000 & - \\
\multirow{4}{*}{2<sup>-5</sup>} & 2<sup>-4</sup> & 7200 & 8 & 0.021 & 342 & 0.61 & 5879 & 1.52 \\
 & 2<sup>-5</sup> & 30752 & 8 & 0.045 & 1275 & 6.52 & 24428 & 47.58 \\
 & 2<sup>-6</sup> & 127008 & 8 & 0.11 & 5002 & 63.61 & 88205 & 563.18 \\
 & 2<sup>-7</sup> & 516128 & 8 & 0.44 & 20072 & 904.18 & _\>_200000 & - \\
\multirow{4}{*}{2<sup>-6</sup>} & 2<sup>-4</sup> & 14400 & 8 & 0.031 & 122 & 0.41 & 9428 & 8.09 \\
 & 2<sup>-5</sup> & 61504 & 8 & 0.074 & 434 & 3.48 & 38225 & 195.13 \\
 & 2<sup>-6</sup> & 254016 & 8 & 0.23 & 1709 & 38.11 & 154255 & 1416.21 \\
 & 2<sup>-7</sup> & 1032256 & 9 & 0.99 & 6907 & 661.72 & _\>_200000 & - \\
\multirow{4}{*}{2<sup>-7</sup>} & 2<sup>-4</sup> & 28800 & 10 & 0.055 & 134 & 0.67 & 10752 & 21.37 \\
 & 2<sup>-5</sup> & 123008 & 10 & 0.15 & 186 & 2.37 & 45062 & 282.98 \\
 & 2<sup>-6</sup> & 508032 & 10 & 0.55 & 270 & 11.94 & 182323 & 3262.76 \\
 & 2<sup>-7</sup> & 2064512 & 10 & 3.06 & 976 & 264.01 & _\>_200000 & - \\
\end{tabular}

3: Iteration numbers and CPU times of MINRES-\(\mathcal{P}_\alpha\), MINRES-P<sub>1</sub>, and MINRES-_I<sub>mn</sub>_ for Example 2.

