<tbc>Since \(\{e_j\}_{j=1}^n\) is the standard basis of R_<sup>n</sup>_, they are linearly independent, and therefore<tbc>

\(c_j^{(1)}=0,\forall j=1,\dots,n.\) (40)

<tbc>From (37) and (40), it follows that all coefficients are zero. Hence, only the trivial linear combination can yield the zero vector. Consequently, the set

\(\left\{\mathbf{u}_j^{(1)}\right\}_{j=1}^n\cup\left\{\mathbf{u}_j^{(2)}\right\}_{j=1}^r\)

consists of _n+r_ linearly independent vectors.

**Theorem 5.** _Let the VBP preconditioner_ P<sub>VBP</sub> _be defined as in_ (6)_. Then the degree of the minimal polynomial of the preconditioned matrix_ \(\mathscr{P}_\mathrm{VBP}^{-1}\mathscr{A}\) _is at most n_+1.

_Proof._ From (25), we recall that the preconditioned matrix admits the following block upper triangular representation<tbc>

\(\mathscr{P}_\mathrm{VBP}^{-1}\mathscr{A}=\left[\begin{array}{ c c }
\Theta_1 & \Theta_2 \\
0 & I
\end{array}\right],\) (41)

<tbc>where \(I\in\mathbb{R}^{n\times n}\) is the identity matrix, \(\Theta_1\in\mathbb{R}^{n\times n}\), and \(\Theta_2\in\mathbb{R}^{n\times n}\) are given by

\(\Theta_1=(T+WT^{-1}W)(T+\alpha I)^{-1},\)<br>
\(\Theta_2=\gamma(T+WT^{-1}W)(T+\alpha I)^{-1}W-WT^{-1}.\) (42)

Let \(\lambda_1,\lambda_2,\dots,\lambda_n\) denote the eigenvalues of the matrix \(\Theta_1\in\mathbb{R}^{n\times n}\). Since the matrix in (41) is block upper triangular, its spectrum is the union of the spectra of its diagonal blocks. Consequently, the eigenvalues of \(\mathscr{P}_\mathrm{VBP}^{-1}\mathscr{A}\) consist of \(\lambda_1,\dots,\lambda_n\) (from the (1,1) block \(\Theta_1\)) and 1 with multiplicity _n_ (from the (2,2) block _I_). Hence, the characteristic polynomial of \(\mathscr{P}_\mathrm{VBP}^{-1}\mathscr{A}\) is given by<tbc>

\(\Phi_{\mathscr{P}_\mathrm{VBP}^{-1}\mathscr{A}}(\lambda)=\mathrm{det}\left(\mathscr{P}_\mathrm{VBP}^{-1}\mathscr{A}-\lambda I\right)=\prod_{i=1}^n(\lambda-\lambda_i)(\lambda-1)^n.\) (43)

<tbc>Now define the polynomial \(\Psi(\lambda)\) of degree _n_+1 as follows

\(\Psi(\lambda):=\left(\prod_{i=1}^n(\lambda-\lambda_i)\right)(\lambda-1).\) (44)

We shall prove that \(\Psi\) is an annihilating polynomial of the preconditioned matrix, i.e., \(\Psi\left(\mathscr{P}_\mathrm{VBP}^{-1}\mathscr{A}\right)=0\).

