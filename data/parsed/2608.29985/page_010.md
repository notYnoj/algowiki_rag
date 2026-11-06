<tbc>_Proof._ Let **u**=(_x;y_) be an eigenvector associated with the eigenvalue \(\zeta\), i.e.,

\(\mathscr{P}_\mathrm{VBP}^{-1}\mathscr{A}\mathbf{u}=\zeta\mathbf{u},\text{equivalently}\mathscr{A}\mathbf{u}=\zeta\mathscr{P}_\mathrm{VBP}\mathbf{u}.\)

This relation expands to

\(\left[\begin{array}{ c c }
T & -W \\
W & T
\end{array}\right]\left[\begin{array}{ c }
x \\
y
\end{array}\right]=\zeta\left[\begin{array}{ c c }
T+\alpha I-\gamma W^2 & -\gamma WT \\
W & T
\end{array}\right]\left[\begin{array}{ c }
x \\
y
\end{array}\right],\) (27)

where \(x,y\in\mathbb{R}^n\). Equation (27) is equivalent to the system

\(Tx-Wy=\zeta\big(Tx+\alpha x-\gamma W^2x-\gamma WTy\big),\) (28)

\(Wx+Ty=\zeta(Wx+Ty).\) (29)

The eigenvalue \(\zeta\) cannot be zero because both matrices P<sub>VBP</sub> and A are nonsingular. Hence, we consider the following cases.

**Case 1 (**\(\zeta=1\)**):** Substituting \(\zeta=1\) into equation (28) yields

\((\gamma WT-W)y=(\alpha I-\gamma W^2)x.\) (30)

Let \(\mu\) be an eigenvalue of the matrix _W_. Then the matrix

\(\alpha I-\gamma W^2\)

is nonsingular if and only if

\(\frac{\alpha}{\gamma}\neq\mu^2\)

for every eigenvalue \(\mu\) of _W_.

Therefore, from relation (30), we conclude that

\(x=(\alpha I-\gamma W^2)^{-1}(\gamma WT-W)y.\)

Hence, the eigenvector corresponding to the eigenvalue \(\zeta=1\) is given by

\(\mathbf{u}=\left[\begin{array}{ c }
(\alpha I-\gamma W^2)^{-1}(\gamma WT-W)y \\
y
\end{array}\right],y\neq 0.\)

**Case 2 (**\(\zeta\neq 1\)**):** For \(\zeta\neq 1\), equation (29) gives _y_=-_T_<sup>-1</sup>_Wx_. Substituting this into equation (28), we have

\(\big((1-\zeta)T+WT^{-1}W-\alpha\zeta\big)x=0.\) (31)

