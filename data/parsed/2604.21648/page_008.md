<tbc>Although the operator \(E_+^{\nu_1,\nu_2}\) is more complicated than \(E^{\nu_1,\nu_2}\), it is the natural generalization of the error propagation operator for Hermitian positive definite _A_ which is defined as

(3.5) \(E_\mathrm{HPD}^{\nu_1,\nu_2}(P,P):=(I-M^{-1}A)^{\nu_2}(I-P(P^HAP)^{-1}P^HA)(I-M^{-1}A)^{\nu_1}.\)

For _A=B_ HPD the _A_-adjoint of _M_<sup>-1</sup>_A_ is given by

\((M^{-1}A)^+=A^{-1}(M^{-1}A)^HA=M^{-HA}\)

and with _R=P_ the operator \(E_+^{\nu_1,\nu_2}(P,P)\) is exactly the operator \(E_\mathrm{HPD}^{\nu_1,\nu_2}(P,P)\).<br>
On the other hand, there is the simpler error operator \(E^{\nu_1,\nu_2}\) that uses the same smoother for pre- and post-smoothing, making the whole operator easier to apply. It was studied in \[31, 33\] and recently in \[16\]. For the simple case \(\nu_1=1\) and \(\nu_2=0\), it holds \(E_+^{1,0}=E^{1,0}\). This operator has been analyzed in \[1, 2, 39\].<br>
If _M_<sup>-1</sup>_A_ is _B_-orthogonal, it holds \(E_+^{\nu_1,\nu_2}(P,R)=E^{\nu_1,\nu_2}(P,R)\) and the error matrices coincide. However, in general the two operators differ from each other and therefore we analyze their convergence behavior separately.<br>
The next result illustrates the fact that \(E_+^{\nu_1,\nu_2}\) is the natural generalization of the error operator in the HPD case. It proves properties of \(E_+^{\nu_1,\nu_2}\) that reduce to known properties of \(E_\mathrm{HPD}^{\nu_1,\nu_2}\) if we consider _A=B_ to be HPD \[8\]. We also see that \(E^{\nu_1,\nu_2}\) requires additional assumptions to achieve the same results.

Theorem 3.2. _Let_ \(\Pi_A\) _be B-orthogonal and_ \(\nu\in\mathbb{N}_0\)_. Then it holds_<br>
_1)_ \((E_+^{\nu,\nu})^+=E_+^{\nu,\nu}\).<br>
_2)_ \((E_+^{\nu,0})^+=E_+^{0,\nu}\) _and_ \((E_+^{0,\nu})^+=E_+^{\nu,0}\)<br>
_3)_ \(B^{-1}(E_+^{\nu,0})^H=E_+^{0,\nu} B^{-1}\) _and_ \(B^{-1}(E_+^{0,\nu})^H=E_+^{\nu,0}B^{-1}\).<br>
_4)_ \(\|E_+^{\nu,\nu}\|_B=\|E_+^{\nu,0}\|_B^2=\|E_+^{0,\nu}\|_B^2\).<br>
_If additionally M_<sup>-1</sup>_A is B-orthogonal, then the above properties also hold for_ \(E^{\nu,\nu}\).

_Proof._ Let \(\Pi_A\) be _B_-orthogonal. _1)_ and _2)_ both follow from the properties of the _B_-adjoint. Since \(\Pi_A\) is _B_-orthogonal, it holds \((I-\Pi_A)^+=(I-\Pi_A)\) and thus

\((E_+^{\nu,\nu})^+=\big((I-(M^{-1}A)^+)^\nu(I-\Pi_A)(I-M^{-1}A)^\nu\big)^+\)<br>
\(=(I-(M^{-1}A)^+)^\nu(I-\Pi_A)^+(I-M^{-1}A)^\nu=E_+^{\nu,\nu}\)

and<tbc>

\((E_+^{\nu,0})^+=\big((I-\Pi_A)(I-M^{-1}A)^\nu\big)^+=(I-(M^{-1}A)^+)^\nu(I-\Pi_A^+)=E_+^{0,\nu}.\)

<tbc>Taking the _B_-adjoint on both sides yields the second equation of _2). 3)_ is then a reformulation of _2)_. And for _4)_ we use _2)_ and the fact that \(E_+^{\nu,\nu}=E_+^{0,\nu}\cdot E_+^{\nu,0}\) to obtain

\(\|E_+^{\nu,\nu}\|_B=\|E_+^{0,\nu} E_+^{\nu,0}\|_B=\|E_+^{0,\nu}(E_+^{0,\nu})^+\|_B=\|E_+^{0,\nu}\|_B^2\)

with Proposition 2.12. An analogous calculation shows \(\|E_+^{\nu,\nu}\|_B=\|E_+^{\nu,0}\|_B^2\). If additionally _M_<sup>-1</sup>_A_ is _B_-orthogonal, the operators \(E_+^{\nu,\nu}\) and \(E^{\nu,\nu}\) coincide and thus _1)_ to _4)_ also hold for \(E^{\nu,\nu}\). □

**3.3. Smoothing and generalized eigenvalue problems.** Our convergence analysis and in particular our optimality results depend on eigenvectors and eigenvalues of certain (generalized) eigenvalue problems. The first eigenvalue problem is given by

(3.6) \(M^{-1}Az=\lambda z.\)

