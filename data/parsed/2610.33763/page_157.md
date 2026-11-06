**Case 2, Example 1.**<br>
With \(f(\theta)=2-cos\theta\), \(g(\theta)=3+cos\theta\) and rank one blocks<tbc>

\(A=\left[\begin{array}{ c c }
1 & 1 \\
1 & 1
\end{array}\right],B=\left[\begin{array}{ c c }
1 & 2 \\
2 & 4
\end{array}\right],\)

<tbc>let \(F(\theta)=f(\theta)\otimes A\) and \(G(\theta)=g(\theta)\otimes B\). Set

\(A_n=T_n(F)+\frac{1}{n^2}I_{2n},B_n=T_n(G)+\frac{1}{n^2}D_n(b),b(x)=(1+x)I_2.\)

Here, both symbols are rank 1 almost everywhere.

**Case 2, Example 2.**<br>
Define piecewise-linear scalar functions in \[0,1\]:<tbc>

\(a(x)=\left\{\begin{array}{ c c }
1-2x, & 0\le x\le\frac{1}{2}, \\
0, & \frac{1}{2}<x\le 1,
\end{array}\right.b(x)=\left\{\begin{array}{ c c }
0, & 0\le x\le\frac{1}{3}\text{or}\frac{2}{3}\le x\le 1, \\
x-\frac{1}{3}, & \frac{1}{3}<x\le\frac{1}{2}, \\
\frac{2}{3}-x, & \frac{1}{2}<x<\frac{2}{3},
\end{array}\right.\)

<tbc>and let _D<sub>n</sub>(a_), _D<sub>n</sub>(b_) be the corresponding sampling matrices. With \(f(\theta)=2+cos\theta\), \(g(\theta)=3+cos\theta\) and<tbc>

\(A=\left[\begin{array}{ c c c }
2 & 0 & 1 \\
0 & 2 & 1 \\
1 & 1 & 1
\end{array}\right],B=\left[\begin{array}{ c c c }
2 & 1 & 0 \\
1 & 1 & 1 \\
0 & 1 & 2
\end{array}\right],\)

<tbc>define \(F(\theta)=f(\theta)\otimes A\) and \(G(\theta)=g(\theta)\otimes B\), and set

\(A_n=\left(D_n^{1/2}(a)\otimes I_3\right)T_n(F)\left(D_n^{1/2}(a)\otimes I_3\right)+\frac{1}{5n}I_{3n},\) (9.12)

\(B_n=\left(D_n^{1/2}(b)\otimes I_3\right)T_n(G)\left(D_n^{1/2}(b)\otimes I_3\right)+\frac{1}{5n}I_{3n}.\) (9.13)

In every example we denote by \(\kappa\) and \(\xi\) the GLT symbols of {_A<sub>n</sub>}<sub>n</sub>_ and {_B<sub>n</sub>}<sub>n</sub>_, respectively.

## A candidate symbol for the geometric mean

Let {_A<sub>n</sub>}<sub>n</sub>_ and {_B<sub>n</sub>}<sub>n</sub>_ be GLT matrix sequences whose matrix-valued symbols

\(\kappa,\xi:[0,1]^d\times[-\pi,\pi]^d\longrightarrow\mathbb{C}^{r\times r},\)

are positive-semidefinite.<br>
For any \(\varepsilon>0\), define the strictly positive symbols \(\kappa_\varepsilon=\kappa+\varepsilon I_r\), \(\xi_\varepsilon=\xi+\varepsilon I_r\). Since the matrix geometric mean is monotone continuous in each argument, the limit below exists point-wise and it is unique (\[3, p.3\]):

**Definition 9.1 (Candidate symbol)** _For almost every_ \((x,\theta)\) _set_<tbc>

\(\widetilde{G}(\kappa,\xi)(x,\theta):=lim_{\varepsilon\rightarrow 0}G\big(\kappa_\varepsilon(x,\theta),\xi_\varepsilon(x,\theta)\big).\) (9.14)

