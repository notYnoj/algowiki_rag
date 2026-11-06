Thus, \(\dot{y}=-sgn(y-1)S(y)\) with _S\>_0 for \(y\neq 1\) and _y\>_0 such that the optimal control can recover ATP from any _y_(0)_\>_0. Fig. 4 shows ATP _y(t_) (left) and PFK activity _u(t_) (right) for the closed-loop system. Next, we discuss the results analytically. ATP rises only when the PFK activity exceeds \(c/\gamma(y)\), the level at which ATP production equals consumption. In the uncontrolled case (_u=c_), we observe an unstable equilibrium _y<sub>u</sub>\<_1 with \(\gamma(y_u)=1\). The optimal control adds \(S/\gamma>0\) at every _y\<_1 and returns ATP levels to _y_=1 at the cost of \(u^*\rightarrow\infty\) as \(y\rightarrow 0\). Each truncation _u<sub>N</sub>=c+v<sub>N</sub>_ is a bounded polynomial, thus it decreases to below \(c/\gamma\) near _y_=0. Since LQR is a bounded affine feedback, while the holding activity \(c/\gamma(y)\) grows without bound as \(y\rightarrow 0\), LQR cannot recover ATP from low levels.

## VI. CONCLUSION

Al’brekht’s method solves one Riccati equation and then an endless sequence of linear equations. We asked what these equations add up to. For scalar analytic input-affine systems, Carleman linearization gave the answer. They are the entries of a single infinite-dimensional Riccati equation in a lower- triangular Toeplitz matrix. The familiar Riccati equation of the standard linearization at the equilibrium is its first entry. The nonlinear terms fill the entries below it. The lifted equation has exactly one solution with positive diagonal entries. That solution is the derivative of the value function, and its finite sections converge to it exponentially. What is new is not the solution. In the scalar case, it has a closed form, and that closed form served as our benchmark. What is new is the structure the lift reveals: a Riccati equation that is decided by its first entry and solved exactly, one entry at a time. After lifting, the equation of linear optimal control and the equation of nonlinear optimal control are the same equation. Nothing in this structure depends on the state dimension. The extension to general nonlinear systems is the natural next step.

## APPENDIX

### A. Proof of Theorem 1

By direct computation, we have

\(\Psi^\top\mathbf{P}^\top\mathbf{A}\Psi=\sum_{m=2}^\infty\big(\sum_{i=1}^{m-1}\sum_{j=1}^{m-i}p(j,i)f_{m-i-j+1}\big)x^m\)<br>
\(=\sum_{m=2}^\infty\sum_{k=1}^{m-1}f_k\pi_{m-k+1}(\mathbf{P})x^m\)<br>
\(=\sum_{m=2}^\infty\big(\sum_{i+j=m}\sum_{k=1}^i\pi_{i-k+2}(\mathbf{P})f_k\delta_{j1}\big)x^m\)<br>
\(=\Psi^\top\unknown\bar{\mathbf{A}}\Psi,\) (40)

where \(\delta\) is the standard Kronecker delta symbol. By a similar argument, we obtain

\(\Psi^\top\mathbf{P}^\top\big(\mathbf{B}\Psi+\mathbf{b}_0\big)=\sum_{i=1}^\infty\sum_{j=1}^\infty\big(\sum_{k=1}^{j+1}p(k,i)g_{j-k+1}\big)x^{i+j}\)<br>
\(+g_0\sum_{i=1}^\infty p(1,i)x^i\)<br>
\(=\sum_{i=1}^\infty\sum_{j=0}^\infty\big(\sum_{k^\prime=0}^jp(j-k'+1,i)g_{k^\prime}\big)x^{i+j}\)<br>
\(=\sum_{k^\prime=0}^\infty g_{k^\prime}\big(\sum_{i=1}^\infty\sum_{j^\prime=0}^\infty p(j'+1,i)x^{i+j^\prime}\big)x^{k^\prime}\)<br>
\(=\sum_{k^\prime=0}^\infty g_{k^\prime}\sum_{m=2}^\infty\pi_m(\mathbf{P})x^{m-1+k^\prime}\)<br>
\(=\sum_{i=1}^\infty\sum_{j=1}^i\pi_{i-j+2}(\mathbf{P})g_{j-1}x^i=\Psi^\top\unknown\mathbf{g}.\) (41)

Applying the expressions (21) and (24) into (22), and then using (40) and (41) proves (27). The conclusion (28) then follows from combining equations (23), (24) and (41).

### B. Proof of Corollary 1

By (20), (40) and (41),

\(\Psi^\top(\unknown\bar{\mathbf{A}}+\bar{\mathbf{A}}^\top\unknown^\top)\Psi=2\Psi^\top\mathbf{P}^\top\mathbf{A}\Psi=f(x)U(x),\)<br>
\(\Psi^\top\unknown\mathbf{g}=\Psi^\top\mathbf{P}^\top(\mathbf{B}\Psi+\mathbf{b}_0)=\frac{1}{2}g(x)U(x).\)

Substituting the above two expressions and (21) into (27) and (28) proves both claims in the corollary.

### C. Proof of Theorem 2

By (21), (40) and (41), we can reformulate the algebraic Riccati-type equation (27) as

\(\sum_{m=0}^\infty 2\sum_{k=0}^mf_{m-k+1}\pi_{k+2}(\mathbf{P})x^{m+2}+\sum_{m=0}^\infty q_{m+2}x^{m+2}\)<br>
\(-\frac{x^2}{r}\big(\sum_{n=0}^\infty\sum_{j=0}^n\pi_{j+2}(\mathbf{P})g_{n-j}x^n\big)^2=0.\)

2
1
no control
1.8
N = 1 (LQR)
0.8
N = 3
N = 5
0.6
1.6
N = 8
ATP y(t)
PFK activity u(t)
optimal
0.4
1.4
0.2
1.2
0
1
0
2
4
6
0
2
4
6
t
t

Fig. 4. ATP _y(t_) (left) and PFK activity _u(t_) (right) from _y_(0)=0.40. Parameters used were _a_=1_,h_=2_,c_=1_,w_=1_,r_=1. The dashed line is the optimal closed loop, the dotted line in the left panel is the unstable equilibrium _y<sub>u</sub>_, and \(\times\) marks where the ATP level reaches zero.

