<tbc>Consequently, the spectrum of the preconditioned matrix, denoted by \(\sigma(\mathscr{P}_\mathrm{VBP}^{-1}\mathscr{A})\), is contained within the following interval

\(\sigma(\mathscr{P}_\mathrm{VBP}^{-1}\mathscr{A})\subset\left[\frac{\lambda_\mathrm{min}(T)+\sigma_\mathrm{min}^2(W)/\lambda_\mathrm{max}(T)}{\alpha+\lambda_\mathrm{max}(T)},\frac{\lambda_\mathrm{max}(T)+\sigma_\mathrm{max}^2(W)/\lambda_\mathrm{min}(T)}{\alpha+\lambda_\mathrm{min}(T)}\right].\) (24)

This completes the proof.

**Theorem 3.** _Assuming the conditions stated in Theorem 1 are satisfied, the preconditioned matrix_ \(\mathscr{P}_\mathrm{VBP}^{-1}\mathscr{A}\) _possesses the eigenvalue_ 1 _with algebraic multiplicity at least n. Furthermore, the remaining eigenvalues are entirely real and reside in a positive real interval_ (24).

_Proof._ A straightforward algebraic manipulation reveals that the preconditioned matrix can be expressed as<tbc>

\(\mathscr{A}\mathscr{P}_\mathrm{VBP}^{-1}=\left[\begin{array}{ c c }
\Theta_1 & \Theta_2 \\
0 & I
\end{array}\right],\) (25)

<tbc>where

\(\Theta_1=(T+WT^{-1}W)(T+\alpha I)^{-1},\Theta_2=\gamma(T+WT^{-1}W)(T+\alpha I)^{-1}W-WT^{-1}.\) (26)

Note that the matrix \(\mathscr{A}\mathscr{P}_\mathrm{VBP}^{-1}\) is similar to \(\mathscr{P}_\mathrm{VBP}^{-1}\mathscr{A}\); hence, they have identical spectra.

From this block triangular structure, it is immediately clear that the matrix \(\mathscr{P}_\mathrm{VBP}^{-1}\mathscr{A}\) admits the eigenvalue 1 with algebraic multiplicity at least _n_. Moreover, the remaining eigenvalues coincide with those of the matrix \(\Theta_1\), which have been characterized in relation (22). As established therein, these eigenvalues are all real and positive, and they lie within the interval specified in (24).

**Theorem 4.** _Assume that the preconditioner_ P<sub>VBP</sub> _is given by_ (6)_. Then, the linear independence of n+r eigenvectors of the preconditioned matrix_ \(\mathscr{P}_\mathrm{VBP}^{-1}\mathscr{A}\) _(with_ \(0\le r\le n\)_) admits the following characterization_

**_Case I (_**\(\zeta=1\)**_)._** _The eigenvalue_ \(\zeta=1\) _has eigenvectors of the form_<tbc>

\(\mathbf{u}=\left[\begin{array}{ c }
Ky \\
y
\end{array}\right],y\neq 0,\)

<tbc>_where_

\(K=(\alpha I-\gamma W^2)^{-1}(\gamma WT-W)\)

_and_ \(\frac{\alpha}{\gamma}\neq\mu^2\) _for every eigenvalue_ \(\mu\) _of W._

**_Case II (_**\(\zeta\neq 1\)**_)._** _For each_ \(\zeta\neq 1\)_, a corresponding eigenvector is given by_

\(\mathbf{u}=\left[\begin{array}{ c }
x \\
-T^{-1}Wx
\end{array}\right],x\neq 0.\)

