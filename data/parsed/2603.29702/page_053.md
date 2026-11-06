<tbc>to the total length of _p_). Since the total sum of sizes of recursion intervals is at most _O(Sn_)=_O(n_log_n_), there are at most \(n/2^{\Omega\left(\mathrm{log}^{0.01}(n)\right)}\) dispensable columns before which the weight of _p_ is non-zero, which can be ignored since this number is \(o\left(\frac{w(p)}{M\mathrm{log}^{0.02}(n)}\right)\). Notice that for every interval \(((i-1)\cdot\mathcal{B}_x,i\cdot\mathcal{B}_x]\), the columns inside it are either all dispensable or all indispensable. We define a new non-negative sequence \(B'=\{b'_i\}\) whose \((i\cdot\mathcal{B}_x)\)-th element is<tbc>

\(b_{i\cdot\mathcal{B}_x}^{^\prime}=\left\{\begin{array}{ c c }
b_{i\cdot\mathcal{B}_x} & \text{if every}x\in((i-1)\cdot\mathcal{B}_x,i\cdot\mathcal{B}_x]\text{is indispensable} \\
a_{i\cdot\mathcal{B}_x} & \text{if every}x\in((i-1)\cdot\mathcal{B}_x,i\cdot\mathcal{B}_x]\text{is dispensable}
\end{array}\right..\)

<tbc>Since the diagonal edges of the Rotated LCS Grid Graph have a weight of 0, we have \(b_{i\cdot\mathcal{B}_x}\le a_{i\cdot\mathcal{B}_x}\) and thus \(b_{i\cdot\mathcal{B}_x}\le b_{i\cdot\mathcal{B}_x}^{^\prime}\). Therefore<tbc>

\(\includegraphics{}\text{SD}_{M^3,S/3}(A,B)\le\includegraphics{}\text{SD}_{M^3,S/3}(A,B').\)

<tbc>Moreover, it is not hard to see that for every recursion interval (_l,r_] we have<tbc>

\(\frac{1}{2^{\mathrm{log}^{0.01}(n)}}A_{\Sigma(l,r]}\le B'_{\Sigma(l,r]}\le A_{\Sigma(l,r]}.\)

<tbc>Thus, we apply Lemma 4.3 on (the defined entries of) \(A,B'\) with \(\alpha=\frac{1}{2^{\mathrm{log}^{0.01}(n)}}\) to obtain<tbc>

\(\includegraphics{}\text{SD}_{M^3,S/3}(A,B)\le\includegraphics{}\text{SD}_{M^3,S/3}(A,B')=O\left(\sum_xb_x^{^\prime}\left(S^{0.51}\mathrm{log}^{0.01}(n)\right)+n/2^{\mathrm{log}_M^{0.015}(n)}\right),\)

<tbc>Where the \(n/2^{\mathrm{log}_M^{0.015}(n)}\) term is from<tbc>

\(\underbrace{2\mathcal{B}_x}_\text{max absolute value of}A\cdot\underbrace{(n/\mathcal{B}_x)}_\text{number of indices that are multiples of}\mathcal{B}_x=O\left(n/2^{\mathrm{log}_M^{0.015}(n)}\right).\)

<tbc>Since the number of dispensable columns is at most \(n/2^{\Omega\left(\mathrm{log}^{0.01}(n)\right)}\) and _w(p_)=_n/_2<sup>_o_\(\left(\mathrm{log}^{0.01}(n)\right)\)</sup>, hence \(\sum_xb_x^{^\prime}=(1+o(1))w(p)\) and \(n/2^{\mathrm{log}_M^{0.015}(n)}\checkmark w(p)\). Thus we have

\(\frac{1}{w(p)}\sum_{s\in[S]\cap 3\mathbb{Z}}\sum_{(l,r]\in s}\mathrm{SD}_{M^3}(A(l,r],B(l,r])=O(S^{0.51}\mathrm{log}^{0.01}(n)).\)

Therefore, by Markov’s inequality, the expected number of \((l,r]\unknown x\) failing (29) is at most \(O(M^3S^{0.51}\mathrm{log}^{0.01}(n))=o\left(\frac{S^{0.98}}{M\mathrm{log}^{0.02}(n)}\right)\). Since we sample active scales with probability \(\Theta(1/S^{0.98})\), with probability \(o\left(\frac{1}{M\mathrm{log}^{0.02}(n)}\right)\), every interval \((l,r]\unknown x\) on an active scale _s_ satisfies (29) (and thereby (24) due to symmetry of the signs).

Now we have finished proving Lemma 7.3 and its ingredients. In Section 7.2, we will present how we can approximate the length of the longest \(\widetilde{S}\)-regular path \(\widehat{p}\) with a small multiplicative error with probability at least 3/4:

**Lemma 7.7.** _Let_ \(\widetilde{S}\subset[S]\) _be such that each scale that is a multiple of_ 3 _is chosen u.a.r. with probability_ 1_/S_<sup>0.98</sup>_. Let_ \(\widehat{p}\) _be the longest_ \(\widetilde{S}\)_-regular_ \(\langle 0,n_X\rangle\)-\(\langle n_X+n_Y,n_Y\rangle\) _path with_ \(w(\widehat{p})=n/2^{o\left(\mathrm{log}^{0.01}(n)\right)}\)_. With probability at least_ 3/4_, we can_ \((1\pm o(1))\)_-approximate_ \(w(\widehat{p})\) _in o(n_<sup>0.09</sup>) _time by querying only_ \(\frac{n^2\phi_y^2}{\mathcal{B}_x^2}/2^{\Omega\left(\mathrm{log}^{0.01}(n)\right)}\) _edge weights._

