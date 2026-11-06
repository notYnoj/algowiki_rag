with \(\hat{a}(\hat{x},\hat{y})=a(L_1+(R_1-L_1)\hat{x},L_2+(R_2-L_2)\hat{y})\) and \((x,y)=(L_1+(R_1-L_1)\hat{x},L_2+(R_2-L_2)\hat{y})\), \((\hat{x},\hat{y})\in[0,1]^2\): as in the one-dimensional setting, the latter setting is a key point for deducing the Weyl distributions of the related matrix sequences, using the GLT axioms; see Remark 8.2.<br>
By combining the equations at all levels into the single comprehensive linear system, known as the all-at-once formulation, and repeating verbatim the manipulations considered in the one-dimensional setting, which are not formally influenced by the two-dimensional space variable, we obtain the equivalent formulation<tbc>

\(A_{\alpha,\mathbf{n},M}\mathbf{u}=\mathbf{f},\) (8.24)

<tbc>with matrix<tbc>

\(A_{\alpha,\mathbf{n},M}=G_{\alpha,\mathbf{n}}\otimes I_M+I_\mathbf{n}\otimes Q_{\theta,M},\)

<tbc>where \(Q_{\theta,M}\) is define as in (8.16), and transformed right-hand side<tbc>

\(\mathbf{f}=(I_\mathbf{n}\otimes H_\theta)^{-1}\widetilde{\mathbf{f}}=(I_\mathbf{n}\otimes H_\theta^{-1})\widetilde{\mathbf{f}},\)

<tbc>where \(\widetilde{\mathbf{f}}\) is obtained by reshaping the original right-hand side

\(\bar{\mathbf{f}}=\left[\begin{array}{ c c }
\Delta t\mathbf{f}_\mathbf{n}^{(1,\theta)}+(I_\mathbf{n}+(1-\theta)G_{\alpha,\mathbf{n}}u_\mathbf{n}^{(0)} &  \\
\Delta t\mathbf{f}_\mathbf{n}^{(2,\theta)} &  \\
\vdots &  \\
\Delta t\mathbf{f}_\mathbf{n}^{(M,\theta)} & 
\end{array}\right]\in\mathbb{R}^{\mathbf{n}M\times 1},\)

into an \(\mathbf{n}\times M\) matrix and then stacking its rows into a single column \(M\mathbf{n}\times 1\) vector. Equivalently, \(\widetilde{\mathbf{f}}\) is formed by stacking the columns of the transpose of the reshaped matrix.

## 8.1.2 GLT, singular value, and eigenvalue analysis

In the current section, we first introduce a basic definition, and then proceed with the GLT analysis of the coefficient matrix sequences derived from the previous approximation methods. More precisely the section is divided into two parts: in the first we study the matrix sequences arising from the space discretizations, both in 1D and 2D. Then, in the second part, we provide the GLT analysis for the global matrix sequences, incorporating also the term coming from the time discretization.

### GLT analysis of the space matrix sequences

**Definition 8.1** _The Wiener class is the set of functions_<tbc>

\(f(\theta)=\sum_{\mathbf{k}\in\mathbb{Z}^d}f_\mathbf{k}e^{i\langle\mathbf{k},\theta\rangle},\theta\in[-\pi,\pi]^d,\)

<tbc>_such that_

\(\sum_{\mathbf{k}\in\mathbb{Z}^d}|f_\mathbf{k}|<\infty,\)

_where_ \(i=\sqrt{-1}\) _and_ \(\langle\mathbf{k},\theta\rangle=k_1\theta_1+\cdots+k_d\theta_d\)_. The Wiener class forms a sub-algebra of the continuous_ \(2\pi\)_-periodic functions defined on_ \([-\pi,\pi]^d\).

