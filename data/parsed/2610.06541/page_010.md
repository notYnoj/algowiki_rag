**Definition 3.12.** When _H_(0) and _H(T_) have a gap \(\Gamma\) around intervals _I_ and _J_, respectively, we define the _continuous leakage_ as the leakage of _U(T_) from _P<sub>I</sub>(H_(0)) to _P<sub>J</sub>(H(T_)). For a product _W_ and precision _k_, we define the _discrete leakage_ as the leakage of _W_ from _P_<sub>_I_<sup>+</sup></sub>(_H_<sup>(_k_)</sup>(0)) to _P_<sub>_J_<sup>+</sup></sub>(_H_<sup>(_k_)</sup>(_T_)).

## 3.5. Adiabatic consequences.

By the reverse triangle inequality, either product of Theorem 3.11 has discrete leakage within \(\varepsilon>0\) of the continuous leakage whenever \(2^k\ge\sqrt{2}\sigma(T+4/\Gamma)/\varepsilon\).

_Remark_ 3.13. The leakage comparison is exact in the limit \(k\rightarrow\infty\). Lemmas 3.4 and 3.8 give \(W\rightarrow U(T)\), Theorem 3.11 gives convergence of the leakages, while the proof of Lemma 3.9 gives \(\|P'-P\|,\|Q'-Q\|\le 2\sqrt{2}\sigma 2^{-k}/\Gamma\rightarrow 0\).

For a band of _m_ eigenvalues, counted with multiplicity and isolated from the rest of the spectrum by a gap, we use the continuous bound of Jansen, Ruskai, and Seiler \[16\]. I do not claim it is the tightest available, and its dependence on the multiplicity _m_ is an artifact of that analysis that can always be improved \[7\].

**Definition 3.14.** For an integer \(m\ge 1\) and functions \(u,v\ge 0\) and _g\>_0 on \[0,1\], the _Jansen-Ruskai-Seiler coefficient_ is

(3.1) \(J_m(u,v,g)=\frac{mu(0)}{g(0)^2}+\frac{mu(1)}{g(1)^2}+\int_0^1\big(\frac{mv}{g^2}+7m\sqrt{m}\frac{u^2}{g^3}\big)ds.\)

A _C_<sup>2</sup> path \(\tilde{H}\) on \[0,1\] with such a band and gap _g_ has leakage at most \(J_m(\|\tilde{H}'\|,\|\tilde{H}''\|,g)/T\) when traversed as \(H(t)=\tilde{H}(t/T)\) on \[0_,T_\] \[16, Theorem 3\]. Since _J<sub>m</sub>_ increases with _u_ and _v_, the bound remains valid when the derivative norms are replaced by envelopes \(u\ge\|\tilde{H}'\|\) and \(v\ge\|\tilde{H}''\|\).

**Corollary 3.15.** _Let_ \(\tilde{H}\) _be_ \(\sigma\)_-sparse and twice continuously differentiable on an open interval containing_ \[0,1\]_. Let_ \(\tilde{H}(s)\) _have a band of m eigenvalues, counted with multiplicity, isolated from the rest of its spectrum by a gap g(s)\>_0_, as in_ \[16, Theorem 3\]_, and let P and Q be the band’s spectral projectors at s_=0 _and s_=1_. Put_ \(C=J_m(\|\tilde{H}'\|,\|\tilde{H}''\|,g)\)_, and let_ \(\ell\) _be the total variation of_ \(\tilde{H}\) _on_ \[0,1\]_. Suppose that C and_ \(\ell\) _are positive, and let_ \(H(t)=\tilde{H}(t/T)\)_. Assume the continuous bound_ \(\|(1-Q)U(T)P\|\le C/T\) _of that theorem, and suppose that_ \(C\le\sqrt{2}\sigma T^2\)_. Let_<tbc>

\(k=\lceil log_2(\sqrt{2}\sigma T^2/C)\rceil,\)

<tbc>_and let W be the midpoint product with the equal-variation checkpoints of Lemma 3.6, as in Lemma 3.8(2). Then W has_ (_k_+1)_-bit generators,_ \(n\le 1+4\ell T^2/C\) _unitary factors, and leakage_ \(\|(1-Q)WP\|\le 2C/T\)_. For a target leakage_ \(\delta>0\) _and_ \(T=2C/\delta\)_, provided_ \(\delta^2\le 4\sqrt{2}\sigma C\)_, the entry precision and the number of unitaries obey_

\(k+1\le 2log_2(1/\delta)+log_2(4\sqrt{2}\sigma C)+2,\)<br>
\(n\le 1+16\ell C/\delta^2.\) (3.2)

_Proof._ We apply Lemma 3.8(2) at accuracy \(\varepsilon=C/T\) to _H_, which has variation \(\ell\) because the increasing rescaling \(t\mapsto t/T\) preserves total variation. Since _C/T\>_0, for every \(j\in\mathbb{N}\), \(2^j\ge\sqrt{2}\sigma T/(C/T)\) is equivalent to \(log_2(\sqrt{2}\sigma T^2/C)\le j\). Since \(C\le\sqrt{2}\sigma T^2\), the logarithm is nonnegative, so _k_ is the least precision for accuracy _C/T_. Lemma 3.8(2) gives the count and \(\|W-U(T)\|\le C/T\), so \(\|(1-Q)WP\|\le\|(1-Q)U(T)P\|+\|W-U(T)\|\le 2C/T\).

For (3.2), \(\delta^2\le 4\sqrt{2}\sigma C\) is \(C\le\sqrt{2}\sigma T^2\) at \(T=2C/\delta\). Substituting \(T^2/C=4C/\delta^2\) in the count gives \(n\le 1+4\ell T^2/C=1+16\ell C/\delta^2\), and in the precision gives

\(k+1\le log_2(\sqrt{2}\sigma T^2/C)+2\text{since}\lceil x\rceil\le x+1\)<br>
\(=2log_2(1/\delta)+log_2(4\sqrt{2}\sigma C)+2\text{since}T=2C/\delta.\)

□

Corollary 3.15 keeps the band’s own projectors, so its leakage has no \(4/\Gamma\) term. The standard fine-step bound (3.2) counts \(O(1/\delta^2)\) unitaries, and improving it at fine steps requires further structure, whereas at unit steps the count is \(O(1/\delta)\) (Corollary 6.7).

