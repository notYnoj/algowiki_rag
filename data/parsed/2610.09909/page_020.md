<tbc>where the bump centers (_X<sub>j</sub>,Y<sub>j</sub>_) are distributed on a circle of radius _r_<sub>0</sub>,

\((X_j,Y_j):=\big(r_0cos\theta_j,r_0sin\theta_j\big),\theta_j:=\frac{2\pi j}{6},j=0,\dots,5.\) (5.3)

Let \(u_\text{base}(x,y):=exp\big(-\frac{(x-0.3)^2+(y-0.7)^2}{\sigma^2}\big)\), we prescribe the exact solution \(u_\text{ex}(x,y):=\phi(x,y)u_\text{base}\). In this test, we take _r_<sub>0</sub>=0.2, \(\sigma_0=0.1\), _A_=0.5 and \(\sigma=0.06\).

Starting from an initial \(32\times 32\) background mesh, we compare the performance of uniform refinement against the proposed adaptive strategy. Fig. 2 illustrates the evolution of the indicator \(\eta\) and the exact errors with respect to the active DOFs. While both strategies successfully achieve the optimal asymptotic rates (O(_h_<sup>3</sup>) in _H_<sup>1</sup>-norm and O(_h_<sup>2</sup>) in _H_<sup>2</sup>- norm), the adaptive method drastically reduces the computational cost.

The superior efficiency is further quantified in  2. The adaptive approach attains an accuracy level comparable to that of uniform refinement using nearly 60% fewer DOFs (6128 vs. 14764). Conversely, for a fixed DOF budget, adaptivity reduces the numerical error by almost an order of magnitude. This targeted efficiency is visually confirmed in Fig. 3; the generated adaptive T-mesh (3328 leaf cells) automatically concentrates the refinement in the local region \([0.2,0.5]\times[0.5,0.8]\) to strictly resolve the sharp peak at (0.3,0.7), demonstrating the robustness of the _a posteriori_ indicator.

\begin{tabular}{ccccc}
_h_ & \(\|u_h-u_\text{ex}\|_{H^1(\Omega_h)}\) & order & \(\|u_h-u_\text{ex}\|_{H^2(\Omega_h)}\) & order \\
1/16 & 1.58E-07 & - & 1.63E-05 & - \\
1/32 & 1.94E-08 & 3.03 & 4.00E-06 & 2.02 \\
1/64 & 2.39E-09 & 3.02 & 9.90E-07 & 2.02 \\
1/128 & 2.98E-10 & 3.00 & 2.47E-07 & 2.00 \\
\end{tabular}

\begin{tabular}{cccc}
Refinement strategy & DOFs & \(\|e_h\|_{H^1(\Omega_h)}\) & \(\|e_h\|_{H^2(\Omega_h)}\) \\
Uniform & 14764 & 4.82E-5 & 3.50E-2 \\
Adaptive & 6128 & 3.03E-5 & 2.05E-2 \\
Adaptive & 14932 & 4.82E-6 & 5.71E-3 \\
\end{tabular}

100
10-2
10-4
Error
Uniform u uh H2
O(h2)
10-6
Adaptive u uh H2
O(h2)
Uniform u uh H1
O(h3)
Adaptive u uh H1
O(h3)
Adaptive n
10-8
102
103
104
105
DOFs

1. Convergence results with uniformly refined meshes for Example 5.1.

2. Comparison between different refinements for Example 5.2.

Figure 2. Error versus DOFs on uniform and adaptively refined meshes for Example 5.2.

