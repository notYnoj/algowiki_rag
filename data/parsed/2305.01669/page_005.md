<tbc>\(F'(x)\) needs to be invertible. Invertibility of all \(F'_i\) follows immediately. Their (w.l.o.g.) _LU_ factorization \[4\] yields

(2.7) \(F_i\equiv F_i(x^{i-1})=L_i(x^{i-1})\cdot U_i(x^{i-1})\equiv L_i\cdot U_i\)

with lower triangular _L<sub>i</sub>_ and upper triangular _U<sub>i</sub>_. In-place factorization yields _L<sub>i</sub>-I<sub>n</sub>+U<sub>i</sub>_ at a computational cost of O(_n_<sup>3</sup>). The matrix \(I_n\in\mathbb{R}^{n\times n}\) denotes the identity in R_<sup>n</sup>_. From Equation (2.6) it follows that

(2.8) \(\begin{array}{ c c c c }
\Delta x & = & -U_1^{-1}\cdot L_1^{-1}\cdot\dots\cdot U_q^{-1}\cdot L_q^{-1}\cdot y \\
 & = & -U_1^{-1}\cdot\left(L_1^{-1}\cdot\dots\cdot\left(U_q^{-1}\cdot\left(L_q^{-1}\cdot y\right)\right)\dots\right)
\end{array}\)

yielding 2_q_ linear systems to be solved as efficiently as possible in order to undercut the computational cost of the standard Newton method. The new method is matrix- free in the sense that \(F'\) is not accumulated explicitly. The analogy with adjoint AD is illustrated by Figure 2, where the reversed edges indicate products of vectors with inverse local Jacobians. For the example in Figure 1, the standard _"accumulate first, then factorize"_ approach yields the Newton step<tbc>

\(\underbrace{\left(\left(\begin{array}{ c c }
\partial_{3,1} & 0 \\
\partial_{4,1} & \partial_{4,2}
\end{array}\right)\left(\begin{array}{ c c }
\partial_{1,-1} & \partial_{1,0} \\
0 & \partial_{2,0}
\end{array}\right)\right)}_{\mathcal{O}(qn^3)\doteq 5}\genfrac(){pt}{2}{y_0}{y_1}\)

<tbc>at the expense of 12fma. The alternative _"factorize first, then accumulate"_ method

\(\underbrace{\left(\begin{array}{ c c }
\partial_{1,-1} & \partial_{1,0} \\
0 & \partial_{2,0}
\end{array}\right)}_{\mathcal{O}(qn^2)\doteq 6}\underbrace{\left(\left(\begin{array}{ c c }
\partial_{3,1} & 0 \\
\partial_{4,1} & \partial_{4,2}
\end{array}\right)^{-1}\left(\begin{array}{ c c }
y_0 \\
y_1
\end{array}\right)\right)}_{\mathcal{O}(n^2)\doteq 3}\)

performs the same task using only 6fma. Admittedly, this example is extreme in the sense that all elemental Jacobians are already triangular. Products of their inverses with a vector can hence be computed very efficiently by simple forward or backward substitution. More realistically, the individual factors need to be transformed into triangular form first. Ideally, the exploitation of sparsity of the elemental Jacobians is expected to keep the corresponding additional effort low. However, the usual challenges faced in the context of direct methods for sparse linear algebra \[4\] need to be addressed. A representative special case is discussed in the next section. It illustrates the potential of the new method and it serves as motivation for further generalization in Section 4 with the aim to enable applicability to a wider range of practically relevant problems.

**3. Banded Elemental Jacobians.** Let all \(F'_i\) have (maximum) bandwidth 2_m_+1 (_m_ off-diagonals) with \(m\checkmark n\). Their in-place _LU_ factorization as in Equation (2.7) yields _L<sub>i</sub>-I<sub>n</sub>+U<sub>i</sub>_ with the same bandwidth at a computational cost of O(_m_<sup>2</sup>_n_). The resulting 2_q_ triangular linear systems can be solved efficiently with a cost of O(_mn_) by simple substitution, respectively. The total computational cost of the matrix-free Newton method can hence be estimated as O(_qm_<sup>2</sup>_n_).

