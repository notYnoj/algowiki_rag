In Section 6, a Hermitian frame absorbs the generator’s first-order change around the midpoint sample _h_ of each interior unit interval and takes the same value at both ends, so neighboring frames nearly cancel. That common value is \(\Theta_h(D)\), for the generator’s slope _D_, and it solves (2.5), which fixes its entries at nonzero eigenvalue differences through the multiplier N. The entries at zero differences are unconstrained, and choosing \(\mathcal{N}(0)=lim_{x\rightarrow 0}\mathcal{N}(x)=1/12\) keeps \(\Theta_h\) continuous in _h_ across eigenvalue coincidences.

**Lemma 2.9.** _Let_ \(h,\tilde{h}\) _be Hermitian._

(1) _Suppose that_ \(\gamma>0\) _and_ \(h,\tilde{h}\) _are_ \(\gamma\)_-separated of spectral width at most_ \(\bar{w}\)_. The frame operator_ \(\Theta_h\) _preserves Hermitian matrices and, for every matrix D, solves_<tbc>

\(e^{ih}\Theta_h(D)e^{-ih}-\Theta_h(D)=\int_0^1\big(\tau-\frac{1}{2}\big)e^{i\tau h}De^{-i\tau h}d\tau.\) \(\text{(2.5)}\)

_Moreover,_<tbc>

<tbc>\(\|\Theta_h\|\le N_\gamma,\|\Theta_h-\Theta_\tilde{h}\|\le N'_\gamma\|h-\tilde{h}\|,\)<tbc>

<tbc>_with dimension-independent constants depending only on_ \(\gamma\) _and_ \(\bar{w}\).<tbc>

(2) _If_ \(h,\tilde{h}\) _have spectral width at most_ \(w<2\pi\)_, they are_ \(\gamma'\)_-separated for every_ \(0<\gamma'\le 2\pi-w\)_. In this case, the frame-operator bounds hold with_ N(_w_) _and_ \(2\mathcal{N}'(w)\) _in place of_ \(N_\gamma\) _and_ \(N'_\gamma\).<tbc>

(3) _If_ \(h,\tilde{h}\) _have spectral width at most_ \(w<2\pi\)_, the inverse averaging operator used for walks is_<tbc>

<tbc>\(\Phi_h^{-1}=\sum_{n\ge 0}\frac{B_n}{n!}a_h^n.\)<tbc>

<tbc>_It preserves Hermitian matrices, with_<tbc>

<tbc>\(\|\Phi_h^{-1}\|\le\mathcal{B}(w),\|\Phi_h^{-1}-\Phi_\tilde{h}^{-1}\|\le 2\mathcal{B}'(w)\|h-\tilde{h}\|.\)<tbc>

<tbc>_Proof._ In an eigenbasis of _h_, let \(x=\lambda_p-\lambda_q\). Comparing the multipliers of _D<sub>pq</sub>_ reduces (2.5) to<tbc>

\((e^{ix}-1)\mathcal{N}(x)=\int_0^1\big(\tau-\frac{1}{2}\big)e^{i\tau x}d\tau.\)

<tbc>Both sides vanish at _x_=0. For \(x\notin 2\pi\mathbb{Z}\),

\((e^{ix}-1)\mathcal{N}(x)=\frac{e^{ix}-1}{x^2}+\frac{e^{ix}+1}{2ix}\text{since}\mathrm{cot}\frac{x}{2}=\frac{i(e^{ix}+1)}{e^{ix}-1},\)<br>
\(=\int_0^1\big(\tau-\frac{1}{2}\big)e^{i\tau x}d\tau\text{integrating by parts.}\)

Since N is real and even, the frame preserves Hermitian matrices entrywise. The eigenvalue differences allowed by \(\gamma\)-separation and width at most \(\bar{w}\) form a compact set avoiding the poles. Choose a smooth compactly supported cutoff \(\chi=1\) there, supported away from the poles, and let _g_ be the Fourier transform of the smooth extension \(\chi\mathcal{N}\). Fourier inversion gives \(\Theta_h(D)=\int_\mathbb{R}g(s)e^{2\pi ish}De^{-2\pi ish}ds\), so unitary invariance gives \(N_\gamma=\|g\|_1\). Duhamel bounds \(\|e^{2\pi ish}-e^{2\pi is\tilde{h}}\|\) by \(2\pi|s|\|h-\tilde{h}\|\) on each side of _D_, giving \(N'_\gamma=4\pi\int_\mathbb{R}|sg(s)|ds\), finite because _g_ decays faster than any power.

If \(|x|\le w<2\pi\) and \(n\neq 0\), then \(|x-2\pi n|\ge 2\pi|n|-|x|\ge 2\pi-w\). For (2)-(3), \(\|a_h\|\le w<2\pi\), and since a scalar shift of _h_ preserves _a<sub>h</sub>_ and gives \(\|h\|\le w/2<\pi\), the inverse formula follows from \[6, Lemma 3\] applied to _ih_.

For the explicit bounds of (2), since \(|x|\le w<2\pi\), the convergent series \(\sum_{n\ge 0}B_{n+2}a_h^n/(n+2)!\) mul tiplies entry (_p,q_) by (_z/(e<sup>z</sup>_-1)-1+_z/_2)_/z_<sup>2</sup> at _z=ix_, which is N(_x_) because _z/(e<sup>z</sup>_-1)+_z/_2=(_z/_2)coth(_z/_2), (_ix/_2)coth(_ix/_2)=(_x/_2)cot(_x/_2), and _z_<sup>2</sup>=-_x_<sup>2</sup>. So this series is \(\Theta_h\), and \(\mathcal{N}(x)=\sum_{m\ge 0}(-1)^mB_{2m+2}x^{2m}/(2m+2)!\), since odd Bernoulli numbers past _B_<sub>1</sub> vanish.

Since \(\|a_h^n\|\le w^n\) and (-1)_<sup>m</sup>B_<sub>2_m_+2</sub>=|_B_<sub>2_m_+2</sub>|, the absolute coefficient sums bound the operator norms by B(_w_) and N(_w_). Telescoping powers with \(\|i[h-\tilde{h},E]\|\le 2\|h-\tilde{h}\|\|E\|\) gives \(\|a_h^n-a_\tilde{h}^n\|\le nw^{n-1}\|a_h-a_\tilde{h}\|\le 2nw^{n-1}\|h-\tilde{h}\|\) for \(n\ge 1\). Termwise differentiation of the majorants then gives the Lipschitz bounds. Both series preserve Hermitian matrices, since their coefficients are real and _a<sub>h</sub>_ preserves Hermiticity. □

