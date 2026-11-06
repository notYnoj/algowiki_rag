### 5.2 Algorithmic Part

The construction of _W_<sup>∗</sup> and _W_<sup>+</sup> can be easily generalized to Bounded Knapsack and can be done in \(\widetilde{O}(n)\) time. So we have:

Lemma 5.3. _In_ \(\widetilde{O}(n)\) _time, we can compute the partition_ (_W_<sup>+</sup>_,<o>W</o>_<sup>+</sup>_,<o>W</o>_<sup>∗</sup>) _of W such that_

(i) \(|W^+|\le 4c_Aw_\mathrm{max}^{2/5}\mathrm{log}^2w_\mathrm{max}\),<tbc>

(ii) \(|\overline{W^+}|\le 4c_Aw_\mathrm{max}^{3/5}\mathrm{log}w_\mathrm{max}\) _and_ \(\Delta(\mathcal{I}^{W^+})\le 8c_Bw_\mathrm{max}^{9/5}\),<tbc>

(iii) \(\Delta(\mathcal{I}^{W^*})\le 4c_Bw_\mathrm{max}^{7/5}\).

It is easy to verify that

\(|W^+|\Delta(\mathcal{I}^{W^+})+|\overline{W^+}|\Delta(\mathcal{I}^{W^+})+|\overline{W^*}|\Delta(\mathcal{I}^{W^*})\le\widetilde{O}(w_\mathrm{max}^{12/5}).\)

Therefore, Theorem 1.1 follows by Lemma 5.3 and 2.2.

## 6 Algorithms for Bounded Subset Sum

We consider Bounded Subset Sum. We have the following observation by Lemma 2.1.

Observation 6.1. _Without loss of generality, we may assume_ \(u_i\le 4w_\mathrm{max}\) _for all_ \(1\le i\le n\).

### 6.1 An \(\widetilde{O}(nw_\mathrm{max})\)-time Algorithm

In this subsection, we present an \(\widetilde{O}(nw_\mathrm{max})\)-time algorithm. It builds upon two ingredients: (i). a faster algorithm for computing the sumset of sets with a special structure, and (ii). a layering technique that transforms the input into a special structure.

### 6.1.1 Faster sumset algorithm for sets with a special structure

We first introduce some notations for integer sets. Given an integer (multi-)set _X_ and a number _a_, we let \(X-a:=\{x-a:x\in X\}\). We let m_<sub>X</sub>_ denote the largest number in _X_. We let \(rX:=\{rx:x\in X\}\) for any real number _r_. Given two integer multisets _A,B_, we let \(A+B:=\{a+b:a\in A\cup\{0\},b\in B\cup\{0\}\}\). It is easy to verify that _r(A+B_)=_rA+rB_.

It is known that the sumset _A+B_ can be computed via Fast Fourier Transform (FFT) in \(\widetilde{O}(\mathfrak{m}_A+\mathfrak{m}_B)\) time. More generally, the following is true:

Lemma 6.1. \[10\] _Given sets_ \(S_1,S_2,\cdots,S_\ell\subset\mathbb{N}\)_, we can compute_ \(S_1+S_2+\cdots+S_\ell\) _in_ \(O(\sigma\mathrm{log}\sigma\mathrm{log}\ell)\) _time, where_ \(\sigma=\mathfrak{m}_{S_0}+\mathfrak{m}_{S_1}+\cdots+\mathfrak{m}_{S_\ell}\).

For our purpose, given a target value _t_, we want to decide whether \(t\in A+kB\) quickly for some positive integer _k_. Using FFT, it takes _O_(m_<sub>A</sub>+k_m_<sub>B</sub>_) time, which is too much when _k_ is large. We show that _O_(m_<sub>A</sub>_+m_<sub>B</sub>_) time is sufficient, and the result can be further generalized by the following lemma.

Lemma 6.2. _Given sets_ \(S_0,S_1,\cdots,S_\ell\subset\mathbb{N}\)_, an integer_ \(k\in\mathbb{Z}_{>0}\) _and a target number t, we can determine whether_ \(t\in S_0+kS_1+\cdots+k^\ell S_\ell\) _in_ \(O(\sigma(\ell+1)\mathrm{log}\sigma)\) _time, where_ \(\sigma=\mathfrak{m}_{S_0}+\mathfrak{m}_{S_1}+\cdots+\mathfrak{m}_{S_\ell}\).

_Proof._ We prove by induction. The lemma is obviously true for \(\ell=0\). Suppose it is true for \(\ell=h-1\). That is, we can determine whether \(t\in S_0+kS_1+\cdots+k^{h-1}S_{h-1}\) in \(c_1(\sum_{i=0}^{h-1}\mathfrak{m}_{S_i})(h-1)\mathrm{log}(\sum_{i=0}^{h-1}\mathfrak{m}_{S_i})\) time for some sufficiently large constant _c_<sub>1</sub>. Now we consider the case \(\ell=h\).

Note that \(t\in S_0+kS_1+\cdots+k^hS_h\) if and only if \(t=t_0+t'\) where \(t_0\in S_0\) and \(t'\in kS_1+\cdots+k^hS_h\). It follows that \(t'\) is a multiple of _k_. Therefore, \(t\equiv t_0(\mathrm{mod}k)\). Let \(r_0\in[0,k-1]\) be the residue of _t_ modulo _k_, \(\bar{S}_0\subseteq S_0\) be the subset of integers in _S_<sub>0</sub> whose residue is _r_<sub>0</sub>. It is clear that every element in \(\bar{S}_0-r_0\) is a multiple of _k_, so \(\frac{1}{k}(\bar{S}_0-r_0)\) is an integer set. Moreover, it follows that \(t\in S_0+kS_1+\cdots+k^hS_h\) if and only if \(t\in\bar{S}_0+kS_1+\cdots+k^hS_h\), or equivalently, if and only if

\(\frac{t-r_0}{k}\in\frac{1}{k}\left((\bar{S}_0-r_0)+kS_1+\cdots+k^hS_h\right)=\frac{1}{k}(\bar{S}_0-r_0)+S_1+kS_2+\cdots+k^{h-1}S_h.\)

