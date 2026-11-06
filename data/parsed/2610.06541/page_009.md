<tbc>For _t<sub>j</sub>\<t\<t_<sub>_j_+1</sub>, the triangle inequality through the midpoint sample \(H\big(\frac{t_j+t_{j+1}}{2}\big)\) and Lemma 3.3 at _k_+1 bits give

\(\|H(t)-G_j\|\le\sqrt{2}\sigma 2^{-k-1}+\sqrt{2}\sigma 2^{-k-1}=\sqrt{2}\sigma 2^{-k}.\)

Since _W_ is generated piecewise by _G<sub>j</sub>_, Lemma 2.4 and the choice of _k_ give \(\|W-U(T)\|\le\sqrt{2}\sigma 2^{-k}T\le\varepsilon\).

For _k\>_0, minimality gives \(\varepsilon 2^{k-1}<\sqrt{2}\sigma T\), hence \(2^{k+1}/(\sqrt{2}\sigma)\le 4T/\varepsilon\), and for _k_=0, the same bound follows from \(\varepsilon\le\sqrt{2}\sigma T\). The ceiling bound \(\lceil x\rceil\le x+1\) then gives both counts. □

When \(\ell(t)\) is hard to compute, any nondecreasing \(\varphi\) with \(\|H(t)-H(s)\|\le\varphi(t)-\varphi(s)\) for \(s\le t\) gives the same results in Lemma 3.6 and Lemma 3.8(2), replacing \(\ell(t)\) by \(\varphi(t)-\varphi(0)\) and \(\ell\) by \(\varphi(T)-\varphi(0)\). Since total variation is bounded by every such increase, equal-variation steps use no more checkpoints at the same precision.

## 3.4. Finite-precision transfer.

We now transfer leakage bounds to the induced and midpoint products, accounting for changes in the evolution and the endpoint projectors.

**Lemma 3.9.** _Let H_<sub>0</sub> _and H<sub>T</sub> have a gap_ \(\Gamma>0\) _around intervals I and J, respectively, and let D_<sub>0</sub> _and D<sub>T</sub> be Hermitian with_ \(\|H_0-D_0\|,\|H_T-D_T\|\le\eta'\)_. Write P and Q for the spectral projectors of H_<sub>0</sub> _for I and of H<sub>T</sub> for J, and_ \(P'\) _and_ \(Q'\) _for those of D_<sub>0</sub> _for I_<sup>+</sup> _and of D<sub>T</sub> for J_<sup>+</sup>_. Then for every matrix X of norm at most one and every matrix Y,_

\(\big\|(1-Q')YP'-(1-Q)XP\big\|\le\|Y-X\|+\frac{4\eta'}{\Gamma}.\)

_Proof._ Since _I_<sup>+</sup> widens _I_ by \(\Gamma/2\), eigenvalues of _D_<sub>0</sub> outside _I_<sup>+</sup> are more than \(\Gamma/2\) from _I_. The gap separates eigenvalues of _H_<sub>0</sub> outside _I_ from _I_<sup>+</sup> by at least \(\Gamma-\Gamma/2=\Gamma/2\). Thus, Theorem 2.7 in both directions, with gap \(\Gamma/2\), bounds \(\|(1-P')P\|\) and \(\|(1-P)P'\|\) by \(2\|H_0-D_0\|/\Gamma\). Their maximum is \(\|P-P'\|\), since \(P-P'\) is Hermitian and \((P-P')^2=P(1-P')P+(1-P)P'(1-P)\) is block diagonal on \(\mathrm{ran}P\oplus\mathrm{ker}P\), with block norms \(\|(1-P')P\|^2\) and \(\|(1-P)P'\|^2\). Hence, \(\|P-P'\|\le 2\eta'/\Gamma\) by the endpoint error bound. The same argument at _T_ gives \(\|Q-Q'\|\le 2\eta'/\Gamma\).

Adding and subtracting \((1-Q')XP\) and \((1-Q')XP'\) gives

\((1-Q')YP'-(1-Q)XP=(Q-Q')XP+(1-Q')(Y-X)P'+(1-Q')X(P'-P).\)

Since _X_ and the orthogonal projectors are contractions, the triangle inequality and submultiplicativity bound its norm by \(\|Q-Q'\|+\|Y-X\|+\|P'-P\|\le\|Y-X\|+4\eta'/\Gamma\). □

_Remark_ 3.10. The gap \(\Gamma\) enters Lemma 3.9 only through the replacement of _H_<sub>0</sub> and _H<sub>T</sub>_ by _D_<sub>0</sub> and _D<sub>T</sub>_. Any other perturbation bound for the endpoint projectors can replace Davis-Kahan, and it then decides how, if at all, a gap appears. Since the intervals _I_ and _J_ are chosen independently, the eigenvalues followed may even shift in energy between the ends.

With truncated endpoints, Lemma 3.9 applies to both products.

**Theorem 3.11.** _Let H be regulated and_ \(\sigma\)_-sparse, and let k be a nonnegative integer. Let W be either_

(1) _the induced product of a piecewise-constant truncation H_<sup>(_k_)</sup> _(Lemma 3.4), or_<tbc>

(2) _a midpoint product of Lemma 3.8 at some accuracy_ \(\varepsilon\)_, with k chosen for that accuracy and_ (_k_+1)_-bit generators._

_Let H_(0) _and H(T_) _have gaps_ \(\Gamma\) _around I and J, put P=P<sub>I</sub>(H_(0)) _and Q=P<sub>J</sub>(H(T_))_, and let_ \(P'\) _and_ \(Q'\) _be the spectral projectors of the k-bit endpoint truncations H_<sup>(_k_)</sup>(0) _for I_<sup>+</sup> _and H_<sup>(_k_)</sup>(_T_) _for J_<sup>+</sup>_. In either case,_

\(\big\|(1-Q')WP'-(1-Q)U(T)P\big\|\le\sqrt{2}\sigma 2^{-k}(T+4/\Gamma).\)

_Moreover,_ \(\|(1-S)(W-U(T))R\|\le\sqrt{2}\sigma 2^{-k}T\) _for arbitrary orthogonal projectors R,S._

_Proof._ By Lemma 3.4 or Lemma 3.8, \(\|W-U(T)\|\le\sqrt{2}\sigma 2^{-k}T\), so, by Lemma 3.3, Lemma 3.9 applies with Hermitian _D_<sub>0</sub>=_H_<sup>(_k_)</sup>(0), _D<sub>T</sub>=H_<sup>(_k_)</sup>(_T_), unitary _X=U(T_), _Y=W_, and \(\eta'=\sqrt{2}\sigma 2^{-k}\). For orthogonal projectors _R,S_, contractivity gives \(\|(1-S)(W-U(T))R\|\le\|W-U(T)\|\). □

