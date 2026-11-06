<tbc>which is a simple computation. Theorem 4.1 was proved in \[39, Theorem 3.5\] for the error operator \(E^{1,0}=E_+^{1,0}\) and the special case for _B=M_ HPD.<br>
For the last case, we consider a singular value decomposition (SVD) of _A_, i.e. \(A=U\Sigma V^H\) with unitary matrices \(U,V\in\mathbb{C}^{n\times n}\) and \(\Sigma=\mathrm{diag}(\sigma_1,\dots,\sigma_n)\). Then define _Q=VU<sup>H</sup>_ and \(B=QA=V\Sigma V^H\) for which we have

\((M^{-1}A)^+=(QA)^{-1}A^HM^{-H}QA=QM^{-H}QA.\)

Here, the restriction operator _R_<sub>∗</sub> can be easily computed again, since _R_<sub>∗</sub>=_A_<sup>-_H_</sup>_BP=UV<sup>H</sup>P=Q<sup>H</sup>P_ given some interpolation _P_.<br>
To avoid the computation of the post-smoother (_M_<sup>-1</sup>_A_)<sup>+</sup>, it seems natural to consider a simpler error operator, namely \(E^{\nu_1,\nu_2}\). For \(\nu_1=1\) and \(\nu_2=0\), it holds \(E_+^{1,0}=E^{1,0}\) and similar to before this case was already studied in \[1, 2\]. For arbitrary \(\nu_1\) and \(\nu_2\), analysis has been done in \[16\]. There, the general assumption was used that _M_<sup>-1</sup>_A_ is diagonalizable. With this diagonalization, a certain class of HPD matrices _B_ is established and then used to show convergence results for the operator \(E^{\nu_1,\nu_2}\) in this class of _B_-norms. The optimal transfer operators leading to the minimal _B_-norms are also given in \[16\].<br>
We now show that the assumption of diagonalizability of _M_<sup>-1</sup>_A_ and the resulting class of _B_-norms actually refer to _M_<sup>-1</sup>_A_ being _B_-normal.<br>
While Theorem 4.1 utilizes the eigenvalues and eigenvectors of \(\widehat{M}^{-1}B\), the idea used in \[1\] and then later in \[16\] was to build the optimal transfer operators with the eigenvectors of _M_<sup>-1</sup>_A_. Note, that Theorem 3.10 gives a relation between the eigenvectors and eigenvalues of _M_<sup>-1</sup>_A_ and \(\widetilde{M}^{-1}B\). The following result is proven in \[1, Lemma 4.1\].

Lemma 4.6. _Let_ \(A,M\in\mathbb{C}^{n\times n}\) _be such that M is invertible and M_<sup>-1</sup>_A is diagonalizable. Consider the left and right generalized eigenvectors_ \(V_l,V_r\in\mathbb{C}^{n\times n}\)_, respectively, of the generalized eigenvalue problem_ (3.14) _such that_

\(AV_r=MV_r\Lambda,\) (4.1)

\(V_l^HA=\Lambda V_l^HM\) (4.2)

_where_ \(\Lambda\in\mathbb{C}^{n\times n}\) _is a diagonal matrix containing the eigenvalues. Then V<sub>l</sub> and V<sub>r</sub> induce a matrix-based orthogonality, satisfying_

\(V_l^HAV_r=D_A,\) (4.3)

\(V_l^HMV_r=D_M\) (4.4)

_for nonsingular diagonal matrices_ \(D_A,D_M\in\mathbb{C}^{n\times n}\).<br>
Note that this Lemma can also be proven by using the Kronecker canonical form of matrix pairs (cf. \[18, 17\]).<br>
Since _M_ is nonsingular, _V<sub>r</sub>_ are the right generalized eigenvectors of the generalized eigenvalues problem (3.14) if and only if _V<sub>r</sub>_ are eigenvectors of _M_<sup>-1</sup>_A_. It also holds

\(\Lambda=V_r^{-1}M^{-1}AV_r=(V_l^HMV_r)^{-1}V_l^HAV_r=D_M^{-1}D_A.\)

Based on the right eigenvectors _V<sub>r</sub>_ of _M_<sup>-1</sup>_A_, \[16, Theorem 3.1\] characterizes all possible HPD matrices _B_ such that the coarse grid projection can be _B_-orthogonal. This structure of _B_ is also discussed in \[16, Section 3\]. The following result demonstrates that this structure actually refers to _B_-normality and its stronger version of _B_-orthogonality.

