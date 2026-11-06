_Proof._ Let \(T=T_1\oplus_1\cdots\oplus_1T_m\). Then _U_ is the first leg of _T_. Let \(V=V_1\oplus\cdots\oplus V_m\) and \(W=W_1\oplus\cdots\oplus W_m\) be its second and third legs with the decompositions of the partial direct sum. Let \(n\ge 1\) be an integer and consider \(T^{\otimes n}\). For a sequence \(\alpha=(\alpha_1,\dots,\alpha_n)\in[m]^n\), let \(V_\alpha:=V_{\alpha_1}\otimes\cdots\otimes V_{\alpha_n}\), \(W_\alpha:=W_{\alpha_1}\otimes\cdots\otimes W_{\alpha_n}\) and \(T_\alpha:=T_{\alpha_1}\otimes\cdots\otimes T_{\alpha_n}\). Since the tensor product distributes over direct sums, the second leg \(V^{\otimes n}\) of \(T^{\otimes n}\) is the direct sum of the subspaces \(V_\alpha\), and its third leg \(W^{\otimes n}\) is the direct sum of the subspaces \(W_\alpha\). Expanding \(T^{\otimes n}=(T_1+\cdots+T_m)^{\otimes n}\) gives \(T^{\otimes n}=\sum_\alpha T_\alpha\). Since \(T_i\in U\otimes V_i\otimes W_i\) for every _i_, and the tensor product of tensors is formed leg by leg (Section 2.1), \(T_\alpha\in U^{\otimes n}\otimes V_\alpha\otimes W_\alpha\) for every \(\alpha\). We observe that \(T^{\otimes n}\) is the partial direct sum of the tensors \(T_\alpha\), \(\alpha\in[m]^n\): the tensor product distributes over partial direct sums.

Fix integers \(k_1,\dots,k_m\ge 0\) with \(k_1+\cdots+k_m=n\) and let _J_ be the set of sequences \(\alpha\in[m]^n\) in which every \(i\in[m]\) occurs exactly _k<sub>i</sub>_ times (i.e. the elements of _J_ have "type" _k_). We have<tbc>

\(|J|=\frac{n!}{k_1!\cdots k_m!}.\)

<tbc>Projecting the second and third legs of \(T^{\otimes n}\) onto \(\oplus_{\alpha\in J}V_\alpha\) and \(\oplus_{\alpha\in J}W_\alpha\) gives a tensor _S_ for which \(S\le T^{\otimes n}\). Then _S_ is also a partial direct sum, with shared first leg \(U^{\otimes n}\), of the |_J_| summands \(T_\alpha\) with \(\alpha\in J\). Each such summand \(T_\alpha=T_{\alpha_1}\otimes\cdots\otimes T_{\alpha_n}\) is isomorphic to \(T_1^{\otimes k_1}\otimes\cdots\otimes T_m^{\otimes k_m}\), where \(T_i^{\otimes 0}=\langle 1\rangle\). Since \(S\le T^{\otimes n}\), and \(\phi\) is multiplicative and monotone, Lemma 4.5, applied to _S_, gives<tbc>

\(\phi(T)^n=\phi(T^{\otimes n})\ge\phi(S)\ge\frac{1}{2}|J|^p\phi(T_1)^{k_1}\cdots\phi(T_m)^{k_m}.\)

<tbc>There are at most (_n_+1)_<sup>m</sup>_ tuples of integers \(k_1,\dots,k_m\ge 0\) with \(k_1+\cdots+k_m=n\). Raising to the power 1_/p_, summing over these tuples, and using the multinomial theorem gives

\(2^{1/p}(n+1)^m\phi(T)^{n/p}\ge\big(\phi(T_1)^{1/p}+\cdots+\phi(T_m)^{1/p}\big)^n.\)

Taking _n_th roots and letting \(n\rightarrow\infty\) proves the claim.

**Remark 4.7.** Partial direct sums and direct sums need not be equivalent under asymptotic restriction. Indeed, the spectral point R<sub>(1)</sub> is 1 on \(\langle 1\rangle\oplus_1\langle 1\rangle\cong\langle 1,1,2\rangle\) (Lemma 3.4) and 2 on \(\langle 1\rangle\oplus\langle 1\rangle=\langle 2\rangle\). So \(\langle 2\rangle\) is not an asymptotic restriction of \(\langle 1,1,2\rangle\).

As a first application of Lemma 4.6, we obtain an upper bound on \(\omega_\mathbb{F}\) from a tensor of Strassen. For an integer \(q\ge 1\), let<tbc>

\(\mathrm{Str}_q:=\sum_{i=1}^q\big(e_i\otimes e_0\otimes e_i+e_i\otimes e_i\otimes e_0\big)\in\mathbb{F}^q\otimes\mathbb{F}^{q+1}\otimes\mathbb{F}^{q+1},\)

<tbc>where the first leg has basis _e_<sub>1</sub>_,...,e<sub>q</sub>_ and the other two have basis _e_<sub>0</sub>_,...,e<sub>q</sub>_. This is Strassen’s tensor \[Str87, Lemma 7.4\], with the first and third legs exchanged so that the shared leg comes first; see also Bläser \[Blä13, Section 8\]. The sums with _e_<sub>0</sub> on the second and on the third leg are isomorphic to \(\langle q,1,1\rangle\) and \(\langle 1,q,1\rangle\), respectively, and \(\mathrm{Str}_q=\langle q,1,1\rangle\oplus_1\langle 1,q,1\rangle\), since on the second and on the third leg they use the complementary subspaces span(_e_<sub>0</sub>) and span(_e_<sub>1</sub>_,...,e<sub>q</sub>_). It is known that \(\mathrm{Str}_q\triangleleft\langle q+1\rangle\), which follows from

\(\sum_{i=1}^qe_i\otimes(e_0+\varepsilon e_i)\otimes(e_0+\varepsilon e_i)-\big(\sum_{i=1}^qe_i\big)\otimes e_0\otimes e_0=\varepsilon\mathrm{Str}_q+\varepsilon^2\sum_{i=1}^qe_i\otimes e_i\otimes e_i,\)

where the left-hand side is a sum of _q_+1 tensors of tensor rank one.

**Proposition 4.8.** _For every integer_ \(q\ge 1\)_, we have_ \((2q)^{\omega_\mathbb{F}}\le(q+1)^3\)_. For q_=3 _this gives_ \(6^{\omega_\mathbb{F}}\le 64\)_, so_ \(\omega_\mathbb{F}<2.3212\).

