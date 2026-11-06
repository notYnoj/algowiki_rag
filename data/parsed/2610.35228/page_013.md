The set _F_ is convex and closed.

_Claim 2: every_ \(y\in F\) _satisfies_ \(|y_T|\le 1\) _for all T; in particular,_ \(\mathrm{OPT}\le N\). For \(A\in\mathcal{I}_r\), the principal submatrix on the indices \(\emptyset,A\) gives \(0\le y_A\le 1\), as in Lemma 3.2-(a). For \(T\in\mathcal{I}_{2r}\), partition \(T=A\cup B\) into disjoint independent sets with \(|A|,|B|\le r\). The corresponding \(2\times 2\) submatrix has entries _y<sub>A</sub>,y<sub>T</sub>,y<sub>B</sub>_, so positive semidefiniteness gives \(y_T^2\le y_Ay_B\). The bounds on _y<sub>A</sub>_ and _y<sub>B</sub>_ give \(y_Ay_B\le 1\). Thus _F_ is bounded, and its closedness ensures that the maximum defining OPT is attained.

_Claim 3:_ \(\mathrm{OPT}\ge\alpha(G)\). Let _I_<sub>∗</sub> be a maximum independent set, and set \(y_T^*:=\mathbf{1}[T\subseteq I_*]\). For \(A\in\mathcal{I}_r\), define \(\chi_A:=\mathbf{1}[A\subseteq I_*]\). Then \(M(y^*)=\chi\chi^\top\unknown 0\). The first step follows from \(\mathbf{1}[A\cup B\subseteq I_*]=\chi_A\chi_B\), with both sides zero whenever \(A\cup B\) is not independent. The second step follows because an outer product is positive semidefinite. Moreover, _f(y_<sup>∗</sup>)=|_I_<sub>∗</sub>|, which proves the claim.

_Claim 4: the point_ \(y_T^0:=|\{I\in\mathcal{I}_r:T\subseteq I\}|/n_r\) _satisfies_ \(y^0\in F\) _and_ \(M(y^0)\unknown\widehat{\lambda}\mathrm{Id}\)_, where_ \(\widehat{\lambda}:=n_r^{-3}\). Let \(X\in\{0,1\}^{\mathcal{I}_r\times\mathcal{I}_r}\) have entries \(X(A,I):=\mathbf{1}[A\subseteq I]\). Then<tbc>

\((XX^\top)(A,B)=|\{I\in\mathcal{I}_r:A\cup B\subseteq I\}|.\)

<tbc>The equality follows by expanding the matrix product: each summand is 1 exactly when \(A\cup B\subseteq I\). This entry is zero if \(A\cup B\) is not independent, so \(M(y^0)=XX^\top/n_r\). The inverse of _X_ is given by<tbc>

\(X^{-1}(I,B)=(-1)^{|B|-|I|}\mathbf{1}[I\subseteq B].\)

<tbc>Indeed,<tbc>

\(\sum_{I\in\mathcal{I}_r}X(A,I)X^{-1}(I,B)=\sum_{I:A\subseteq I\subseteq B}(-1)^{|B|-|I|}=\mathbf{1}[A=B].\)

<tbc>The first step follows from the definitions; every subset of \(B\in\mathcal{I}_r\) belongs to I_<sub>r</sub>_. The second step follows from the binomial identity, with an empty sum when \(A\unknown\subseteq B\). Since every entry of _X_<sup>-1</sup> lies in {0,1,-1},<tbc>

\(\|X^{-1}\|_\mathrm{op}\le\|X^{-1}\|_\mathrm{F}\le n_r.\)

<tbc>The first step compares the operator and Frobenius norms, and the second step bounds the sum of the squares of the \(n_r^2\) entries. Consequently,

\(\lambda_\mathrm{min}(M(y^0))=n_r^{-1}\|X^{-1}\|_\mathrm{op}^{-2}\ge n_r^{-3}=\widehat{\lambda}.\)

The first step uses \(M(y^0)=XX^\top/n_r\) and the singular values of _X_. The second step uses the preceding norm bound, and the third step uses the definition of \(\widehat{\lambda}\). This proves Claim 4.

_Claim 5:_ \(M(y)-M(y')\unknown-n_r\|y-y'\|_2\mathrm{Id}\) _for all_ \(y,y'\). The map \(z\mapsto M(y+z)-M(y)\) is linear, and each entry of the resulting matrix is either zero or a coordinate of _z_. Therefore

\(\|M(y+z)-M(y)\|_\mathrm{op}\le\|M(y+z)-M(y)\|_\mathrm{F}\le n_r\|z\|_\infty\le n_r\|z\|_2.\)

The first step compares the operator and Frobenius norms, the second step bounds the \(n_r^2\) entries, and the third step compares vector norms. The lower bound on the eigenvalues of a symmetric matrix proves Claim 5.

Use the coordinates \((y_T)_{T\neq\emptyset}\), so that the affine constraint \(y_\emptyset=1\) is imposed implicitly. By Claims 2, 4, and 5, _F_ is a well-bounded, full-dimensional convex body in dimension _D_:=_n_<sub>2_r_</sub>-1. It contains the ball of radius \(\rho_0:=\widehat{\lambda}/n_r\) centered at _y_<sup>0</sup> and is contained in the ball of radius \(2\sqrt{D}\) centered at _y_<sup>0</sup>.

