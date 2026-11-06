## 2.2. Spectral projectors.

For adiabatic transfer, Davis-Kahan lets us replace endpoint subspaces by those of truncated matrices, with error proportional to truncation error over the gap (Lemma 3.9).

**Definition 2.6.** For a Hermitian matrix _H_ and a compact interval _I_, the _spectral projector P<sub>I</sub>(H_) projects orthogonally onto the span of the eigenvectors of _H_ with eigenvalues in _I_. For \(\Gamma>0\), _H_ has a _gap_ \(\Gamma\) _around I_ if every eigenvalue of _H_ outside _I_ lies at distance at least \(\Gamma\) from _I_, and _I_<sup>+</sup> is _I_ extended by \(\Gamma/2\) at each end. The _leakage_ of a matrix _X_ from a projector _P_ to a projector _Q_ is \(\|(1-Q)XP\|\).

For a unitary _X_, the squared leakage bounds the probability of finding \(X\psi\) outside the range of _Q_ for every unit vector \(\psi\) in the range of _P_.

**Theorem 2.7** (Davis-Kahan, \(sin\Theta\left[10\right]\))**.** _Let_ \(H,G\in\mathbb{C}^{d\times d}\) _be Hermitian, let I,J be compact intervals, and suppose every eigenvalue of G outside J lies at distance at least_ \(\Gamma>0\) _from I. Then_<tbc>

\(\left\|(1-P_J(G))P_I(H)\right\|\le\frac{\left\|(1-P_J(G))(H-G)P_I(H)\right\|}{\Gamma}\le\frac{\|H-G\|}{\Gamma}.\)

<tbc>_Proof._ Let _m,c_ be the midpoint and half-width of _I_, and put _P=P<sub>I</sub>(H_) and _Q_=1-_P<sub>J</sub>(G_). The spectral hypotheses give \(\|(H-m1)P\|\le c\) and \(\|(G-m1)Qv\|\ge(c+\Gamma)\|Qv\|\). Since _P_ commutes with _H_ and _Q_ with _G_, for every unit vector _v_,

\((c+\Gamma)\|QPv\|\le\|(G-m1)QPv\|=\|QP(H-m1)Pv+Q(G-H)Pv\|\le c\|QP\|+\|Q(G-H)P\|.\)

Taking the supremum over _v_ and subtracting \(c\|QP\|\) gives the first inequality, and projector contraction gives the second. □

See \[5, Theorem VII.3.1, (VII.30)\]. Kostrykin, Makarov, and Motovilov \[18\] already compare a spectral projector with that of the perturbed operator for the half-gap neighborhood of an isolated spectral part, as we do in Lemma 3.9, treating general spectral parts under a smallness condition on the perturbation. Yu, Wang, and Samworth \[32\] give a variant for eigenvectors indexed by eigenvalue order, with an eigengap assumed for one matrix only.

## 2.3. The derivative of the exponential.

Returning from unit-step products to continuous evolution uses the frame operator for comparison under separation (Section 6), and the inverse averaging operator for a walk’s logarithm (Section 6.3). Both come from differentiating a step, which averages conjugated changes in its generator over the whole step \[6, Lemma 2\],

(2.4) \(\left.\frac{d}{ds}e^{-i(H+sE)}\right|_{s=0}=-ie^{-iH}\int_0^1e^{i\tau H}Ee^{-i\tau H}d\tau.\)

**Definition 2.8.** For a matrix _H_, the _averaging operator_ is<tbc>

\(\Phi_H(E)=\int_0^1e^{i\tau H}Ee^{-i\tau H}d\tau,\)

<tbc>and the commutator map is _a<sub>H</sub>(E_)=_i(HE-EH_). The _spectral width_ of _H_ is the length of the smallest interval containing its eigenvalues. Write _B<sub>n</sub>_ for the Bernoulli numbers, with \(B_1=-\frac{1}{2}\). For \(0\le w<2\pi\) and \(x\notin 2\pi\mathbb{Z}\backslash\{0\}\), put

\(\mathcal{B}(w)=\sum_{n\ge 0}\frac{\left|B_n\right|}{n!}w^n,\mathcal{N}(x)=\frac{1-\frac{x}{2}cot\frac{x}{2}}{x^2},\mathcal{N}(0)=\frac{1}{12}.\)

For _H_ with no eigenvalue difference in \(2\pi\mathbb{Z}\backslash\{0\}\), the _frame operator_ \(\Theta_H\) multiplies the (_p,q_) entry of a matrix, written in an eigenbasis of _H_ with eigenvalues \(\lambda_p\), by \(\mathcal{N}(\lambda_p-\lambda_q)\). For \(\gamma>0\), a Hermitian matrix is \(\gamma\)_-separated_ if each of its eigenvalue differences _x_ satisfies _x_=0 or \(|x-2\pi n|\ge\gamma\) for every nonzero integer _n_.

Integrating \(e^{i\tau H}Ee^{-i\tau H}=e^{\tau a_H}(E)\) over \[0,1\] gives \(\Phi_H=(e^{a_H}-1)/a_H\), interpreted as a power series. The spectral width is at most _w_ exactly when _H_ is within _w/_2 of a real multiple of the identity, and then \(\|a_H\|\le w\). Euler’s formula \(\left|B_{2m}\right|/(2m)!=2\zeta(2m)/(2\pi)^{2m}\) for \(m\ge 1\), with \(\zeta(2m)<2\), gives \(\left|B_n\right|/n!\le 4(2\pi)^{-n}\), so B converges for \(w<2\pi\) and bounds the inverse averaging operator (Lemma 2.9). The even function N is regular at 0 and has poles at nonzero multiples of \(2\pi\) (Remark 2.10).

