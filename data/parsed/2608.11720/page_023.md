<tbc>_Suppose that the state of_ \(\mathsf{X}\otimes\mathsf{E}\) _is some pure state u and_ \(\mathsf{Y}\otimes\mathsf{Z}\) _is the maximally entangled pair_

\(|\Phi\rangle=\frac{1}{\sqrt{d}}\sum_{i=1}^d|ii\rangle.\)

_There exists an orthonormal basis_ \(\{|\Phi_k\rangle:k\in[d^2]\}\) _of_ \(\mathbb{C}^d\otimes\mathbb{C}^d\) _and a unitary basis_ \(\{P_k:k\in[d^2]\}\) _of_ Mat_<sub>d</sub>_(C) _such that_

\(|u\rangle_{\mathsf{X},\mathsf{E}}\otimes|\Phi\rangle_{\mathsf{Y},\mathsf{Z}}=\frac{1}{d}\sum_{k\in[d^2]}|\Phi_k\rangle_{\mathsf{X},\mathsf{Y}}\otimes(P_k^\dagger\otimes\mathbb{1}_\mathsf{E})|u\rangle_{\mathsf{Z},\mathsf{E}}.\)

_Proof._ Let _X_ and _Z_ be the operators such that for all \(j\in[d]\),

\(X|j\rangle=|j+1modd\rangle\text{and}Z|j\rangle=\omega^j|j\rangle\text{where}\omega=exp(2i\pi/d).\)

For \(a,b\in[d]\), we define _W<sub>a,b</sub>=X<sup>a</sup>Z<sup>b</sup>_ and \(|\Phi_{a,b}\rangle=(\mathbb{1}\otimes W_{a,b})|\Phi\rangle\). Since

\(\langle\Phi_{a,b}|\Phi_{c,d}\rangle=\langle\Phi|\mathbb{1}\otimes W_{a,b}^\dagger W_{c,d}|\Phi\rangle=(1/d)Tr(W_{a,b}^\dagger W_{c,d})=\delta_{a,c}\delta_{b,d},\)

the \(|\Phi_{a,b}\rangle\) are an orthonormal basis of \(\mathbb{C}^d\otimes\mathbb{C}^d\).

Let us now compute the coefficient of \(|v\rangle\otimes|\Phi\rangle\) in the basis \(\{|\Phi_{a,b}\rangle\otimes|c\rangle:a,b,c\in[d]\}\) for some state \(|v\rangle\in\mathbb{C}^d\). Fix \(a,b\in[d]\), then

\(\langle\Phi_{a,b}\otimes\mathbb{1}|v\otimes\Phi\rangle=\langle\Phi\otimes\mathbb{1}|\mathbb{1}\otimes W_{a,b}^\dagger\otimes\mathbb{1}|v\otimes\Phi\rangle=\langle\Phi\otimes\mathbb{1}|v\otimes(W_{a,b}^\dagger\otimes\mathbb{1})\Phi\rangle\)

Using that \(M\otimes\mathbb{1}|\Phi\rangle=\mathbb{1}\otimes M^\top|\Phi\rangle\) for all \(M\in\mathrm{Mat}_d(\mathbb{C})\) and that \((W_{a,b}^\dagger)^\top=\overline{W_{a,b}}\), we can rewrite

\(\langle\Phi_{a,b}\otimes\mathbb{1}|v\otimes\Phi\rangle=\langle\Phi\otimes\mathbb{1}|\mathbb{1}\otimes\mathbb{1}\otimes\overline{W_{a,b}}|v\otimes\Phi\rangle=\overline{W_{a,b}}\langle\Phi\otimes\mathbb{1}|v\otimes\Phi\rangle=(1/d)\overline{W_{a,b}}|v\rangle_\mathsf{Z}\)

where we use that <o>_W_</o><sub>a,b</sub> acts only on Z here. Hence, we have that

(12) \(|v\rangle_\mathsf{X}\otimes|\Phi\rangle_\mathsf{YZ}=\frac{1}{d}\sum_{a,b\in[d]}|\Phi_{a,b}\rangle_{\mathsf{X},\mathsf{Y}}\otimes\overline{W_{a,b}}|v\rangle_\mathsf{Z}.\)

Consider now the Schmidt decomposition of \(|u\rangle\) in \(\mathsf{X}\otimes\mathsf{E}\),

\(|u\rangle=\sum_{i=1}^r|v_i\rangle_\mathsf{X}\otimes|w_i\rangle_\mathsf{E}.\)

Applying Eq (12) for each _v<sub>i</sub>_ and using linearity,

\(|u\rangle_{\mathsf{X},\mathsf{E}}\otimes|\Phi\rangle_{\mathsf{Y},\mathsf{Z}}=\frac{1}{d}\sum_{i=1}^r\sum_{a,b\in[d]}|\Phi_{a,b}\rangle_{\mathsf{X},\mathsf{Y}}\otimes\overline{W_{a,b}}|v_i\rangle_\mathsf{Z}\otimes|w_i\rangle_\mathsf{E}\)<br>
\(=\frac{1}{d}\sum_{a,b\in[d]}|\Phi_{a,b}\rangle_{\mathsf{X},\mathsf{Y}}\otimes(\overline{W_{a,b}}\otimes\mathbb{1}_\mathsf{E})\big(\sum_{i=1}^r|v_i\rangle_\mathsf{Z}\otimes|w_i\rangle_\mathsf{E}\big)\)<br>
\(=\frac{1}{d}\sum_{a,b\in[d]}|\Phi_{a,b}\rangle_{\mathsf{X},\mathsf{Y}}\otimes(\overline{W_{a,b}}\otimes\mathbb{1}_\mathsf{E})|u\rangle_{\mathsf{Z},\mathsf{E}}.\)

And thus if one measures \(\mathsf{X}\otimes\mathsf{Y}\) in the basis \(\{|\Phi_{a,b}\rangle\}\) and obtains some outcome _k_=(_a,b_), after applying \(\overline{W_{a,b}^\dagger}\) to Z, we obtain the state \(|u\rangle_{\mathsf{Z},\mathsf{E}}\) which is the same as relabeling X as Z. To recover the notation in the statement, use \(P_k:=W_{a,b}^\top\).

