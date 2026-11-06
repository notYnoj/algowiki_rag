## 6.1. Time-delay system.

We consider the time-delay system

\(\dot{x}(t)=A_0x(t)+A_1x(t-1)-bu(t),\)<br>
\(y(t)=C^Tx(t),\)

whose transfer function is

\(H(s)=C^T(-sI+A_0+A_1e^{-s})^{-1}b.\)

Let _A(s_)=-_sI+A_<sub>0</sub>+_A_<sub>1</sub>_e_<sup>-_s_</sup> and we need to solve _A(s)x(s_)=_b_. We follow the matrices and parameter choices of the delay example in \[6\], where the authors use the expansion center _s_<sub>0</sub>=0 and scaling factor _w_=1 for both _s_=0.1 and _s_=0.4.

In this experiment, we test our four algorithms: fully refreshed TiGMRES, Toeplitz infGMRES, Dynamic TiGMRES with \(\tau=100\), and IR-TiGMRES. Figure 1 shows the residual histories. At _s_=0.1, all four methods first reach 10<sup>-8</sup> at iteration 14, with final residuals of order 10<sup>-13</sup>. At _s_=0.4, fully refreshed TiGMRES, Dynamic TiGMRES, and IR-TiGMRES first reach 10<sup>-8</sup> at iteration 31, with final residuals lower than 10<sup>-13</sup>. Toeplitz infGMRES instead stops improving at \(3.55\times 10^{-4}\) because of the cancellation described in Section 3.3. Dynamic TiGMRES and IR-TiGMRES remain stable.

## 6.2. Parameterized Helmholtz equation.

We consider the boundary-value problem

\(\big(\nabla^2+f_1(s)(1+sk(x))^2+f_2(s)\beta(x)\big)u(x)=h(x),x\in\Omega,\)<br>
\(u(x)=0,x\in\partial\Omega,\)

where, for _x_=(_x_<sub>1</sub>_,x_<sub>2</sub>),

\(k(x)=\left\{\begin{array}{ c c }
1+x_1\mathrm{sin}(\alpha\pi x_1), & x_1\in[0,1/2), \\
1+(1-x_1)\mathrm{sin}(\alpha\pi x_1), & x_1\in[1/2,1],
\end{array}\right.\)

100
fully refreshed TiGMRES
10-2
Teeplitz infGMRES
Dynamic TiGMRES
IR-TiGMRES
10-4
10-6
Relative residual
10-8
10-10
10-12
10-14
0
5
10
15
20
25 Iteration k
30
35
40
45
50
10-10
10-12
10-14
0
5
10
15
20
25 Iteration k
30
35
40
45
50
102
fully refreshed TiGMRES
10-6
Teeplitz infGMRES
Dynamic TiGMRES
IR-TiGMRES
10-2
10-4
Relative residual
10-6
10-8
10-10
10-12
10-14
0
5
10
15
20
25 Iteration k
30
35
40
45
50
(a) = 0.1.
(b) = 0.4.

Fig. 1: Relative residual histories for the time-delay system. (a) shows the residual versus iteration results for _s_=0.1 and (b) shows the results for _s_=0.4.

