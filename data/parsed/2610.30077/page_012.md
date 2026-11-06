## 7 Numerical results

We verify the scheme using the configuration in  1 below (domain \(\Omega=(0,1)^2\), interface parameter \(\gamma=10^{-3}\)), which we call the _reference configuration_ and refer to by that name for the rest of the paper. All stability, solvability and convergence claims established above hold regardless of this choice; the reference configuration is used purely for demonstration.

### 7.1 Headline demonstration: energy, mass, \(\Delta t\)-robustness

In the style of \[24\], we run the coupled model from the IC above, _N_=128, to _T_=10, at three widely separated step sizes spanning two orders of magnitude, \(\Delta t\in\{10^{-2},10^{-3},10^{-4}\}(10^3,10^4,10^5\) steps respectively), with GMRES solved to a relative tolerance of 10<sup>-10</sup> at every step.

\begin{tabular}{cc}
\(c(\phi)\) & \(\sqrt{1.6\phi^2(1-\phi)^2+0.1}\) \\
\(b(\phi)\) & \((1+\varepsilon_1)c(\phi)^2\), \(\varepsilon_1=10^{-3}\) \\
\(f(\phi)\) & \(3\phi^2(1-\phi)^2\) \\
\(\kappa(\phi)\) & \(10^{-3}(10\phi^2+10^{-3})^{-1}\) \\
\(A(\phi)\) & \(\frac{1}{2}\big(1+tanh(10[cot\pi\phi^*-cot\pi\phi])\big)\), \(\phi^*=0.4\) \\
\(\gamma=\varepsilon_q\) & 10<sup>-3</sup> \\
IC & \(\phi_0=0.4+\xi\), \(\xi\sim Unif[-0.0025,0.0025]\), _q_<sub>0</sub>=0 \\
\end{tabular}

\begin{tabular}{cccccc}
\(\Delta t\) & steps & _E_(10) & mass drift (max) & GMRES/step (med., max) & clamp frac (max) \\
10<sup>-2</sup> & 10<sup>3</sup> & 0.1199 & \(2.2\times 10^{-14}\) & 675, 845 & 0.026 \\
10<sup>-3</sup> & 10<sup>4</sup> & 0.0704 & \(5.1\times 10^{-12}\) & 333, 418 & 0.034 \\
10<sup>-4</sup> & 10<sup>5</sup> & 0.0618 & \(1.0\times 10^{-9}\) & 84, 102 & 0.012 \\
\end{tabular}

Reference-implementation coefficient forms
(Ω = (0,1)2, - = 10-3, N= 128, T= 10)
At = 1e 2
At = 1e - 3
0.16
At = 1e - 4
0.14
true energy E(t)
0.12
0.10
0.08
0.06
0
2
4
6
8
10
t

1: The reference configuration (\(\Omega=(0,1)^2\), _d_<sub>0</sub>=1, _C_<sub>0</sub>=1 throughout), which satisfies the model’s stated structural conditions (Equation 5).

Figure 1: True energy _E(t_), all three \(\Delta t\). The two finer \(\Delta t\) track each other closely to _t_≈3 before separating; \(\Delta t=10^{-2}\) diverges from both much earlier and settles at a visibly higher energy.

