**(i)** The support of the asymptotic eigenvalue distribution of {_G(A<sub>n</sub>,B<sub>n</sub>_)}_<sub>n</sub>_ coincides with the intersection set \(\text{essRan}(\kappa)\cap\text{essRan}(\xi)\) see Section 9.2.4.

**(ii)** The eigenvalues appear to converge in distribution to a candidate symbol which is rank-deficient and, in general, distinct from the classical geometric mean \(G(\kappa,\xi)\).

Clearly, the relation \(G(A_n,B_n)\sim_\text{GLT}G(\kappa,\xi)\) cannot hold under hypotheses 1.-2., and the experiments show the substantial differences in this case compared to the commuting or invertible scenarios. If this case can be studied within the GLT framework, it requires a more technical application of GLT and a.c.s. theory, along with a deeper functional calculus of matrix means.

## Setup of the numerical experiments

Below, we provide the setup of the numerical tets.<br>
We construct four pairs of unilevel GLT matrix sequences {_A<sub>n</sub>}<sub>n</sub>,{B<sub>n</sub>}<sub>n</sub>_, whose symbols simultaneously satisfy the hypothesis stated at the beginning of Section 9.2.4 (rank deficiency and non-commutation). These examples are organized according to the property of rank loss:

• **Case 1** - each symbol is full rank on a set of positive measure;

• **Case 2** - each symbol is rank-deficient almost everywhere.

**Case 1, Example 1.**<br>
Define<tbc>

\(f(\theta)=\left\{\begin{array}{ c c }
0, & \theta\in[-\pi,0], \\
\theta, & \theta\in(0,\pi],
\end{array}\right.g(\theta)=f(-\theta),\)

<tbc>and set<tbc>

\(F(\theta)=f(\theta)\otimes\left[\begin{array}{ c c }
2 & 1 \\
1 & 2
\end{array}\right],G(\theta)=g(\theta)\otimes\left[\begin{array}{ c c }
3 & 1 \\
1 & 1
\end{array}\right].\)

<tbc>With the \(2n\times 2n\) Toeplitz matrices _T<sub>n</sub>(F_) and _T<sub>n</sub>(G_), define

\(A_n=T_n(F)+\frac{1}{n^3}I_{2n},B_n=T_n(G)+\frac{1}{n^3}I_{2n}.\) (9.10)

**Case 1, Example 2.**<br>
Let \(\chi_{[-a,a]}\) be the characteristic function of [-_a,a_], \(0<a<\pi\), and set<tbc>

\(f(\theta)=\chi_{[-1/2,1/2]}(\theta),g(\theta)=\chi_{[-1/4,1/4]}(\theta),\)<br>
\(A=\left[\begin{array}{ c c }
2 & 1 \\
1 & 2
\end{array}\right],B=\left[\begin{array}{ c c }
3 & 1 \\
1 & 1
\end{array}\right],\)<br>
\(F(\theta)=f(\theta)\otimes A,G(\theta)=g(\theta)\otimes B.\)

<tbc>Define<tbc>

\(A_n=T_n(F)+\frac{1}{n^3}I_{2n},B_n=T_n(G)+\frac{1}{n^3}I_{2n}.\) (9.11)

