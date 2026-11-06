• \(\ell'_4(\alpha)\): Theorem 5.9 and Theorem 5.12, for \(1/4<\alpha\le\frac{2}{3}(\mathrm{log}3-1)\).<tbc>

• \(\ell'_5(\alpha)\): Theorem 5.9 and Theorem 5.12, for \(\alpha_3<\alpha\le 1/4\).<tbc>

• \(\ell'_6(\alpha)\): Theorem 5.9 and Theorem 5.14, for \(\alpha_4<\alpha\le\alpha_3\).<tbc>

• \(\ell'_7(\alpha)\): Theorem 4.2 and Theorem 5.14, for \(0\le\alpha\le\alpha_4\).

Setting \(\epsilon=1/100\), we have \(\ell'_i(\alpha)<1-\epsilon\) for all \(i\in\{1,3,4,5,6\}\) and for every relevant value of \(\alpha\). Therefore, we can safely apply Theorems 5.1 and 5.9 as in  1. We also have \(1/2<\ell'_2(\alpha)\le\gamma_1<0.8\), where \(\gamma_1\) is defined in (6). Thus, we can apply Theorem 5.2 as in  1.

Once we have determined which lemma or theorem to apply for each pair of \(\alpha\) and \(\ell'\), we can compute, for each \(\alpha\), the value of \(\ell'\) that maximizes the running time. This is the bottleneck value of \(\ell'\) shown in the last column of  1. Using these values, we can express the worst-case running time under the space bound \(O^*(2^{\alpha n})\) as \(O^*(2^{\mathcal{T}(\alpha)n})\), where \(\mathcal{T}(\alpha)\) is defined as follows:

\(\mathcal{T}(\alpha)=\left\{\begin{array}{ c c }
\frac{H(\gamma_1)+\gamma_1}{2}=\tau_\text{rrb}(\gamma_1,\gamma_1-\alpha_1) & \text{if}\alpha_1<\alpha, \\
\frac{H(\ell'_1(\alpha))+\ell'_1(\alpha)}{2}=\tau_\text{rrb}(\ell'_1(\alpha),\ell'_1(\alpha)-\alpha) & \text{if}1/2<\alpha\le\alpha_1, \\
\frac{H(\ell'_2(\alpha))+\ell'_2(\alpha)}{2}=\tau_\text{rrb}\left(\ell'_2(\alpha),\ell'_2(\alpha)-\mathrm{phi}\mathrm{i}^{-1}(1-\alpha)\right) & \text{if}\alpha_2<\alpha\le 1/2, \\
\frac{H(\ell'_3(\alpha))+\ell'_3(\alpha)}{2}=\tau_\text{sbb}(\ell'_3(\alpha),\alpha) & \text{if}2-\mathrm{log}3<\alpha\le\alpha_2, \\
\tau_\text{sbu}\left(\frac{2}{3},\alpha\right) & \text{if}\frac{2}{3}(\mathrm{log}3-1)<\alpha\le 2-\mathrm{log}3,
\end{array}\right.\) (8)

Here, \(\gamma_1\), \(\tau_\text{rrb}\), \(\tau_\text{sbu}\), \(\tau_\text{sbb}\), and \(\tau_\text{subset}\) are defined in (6), (5), (12), (11), and (13), respectively. The function phi<sup>-1</sup> is defined in Theorem 5.2. For the case \(\alpha>\alpha_1\), we use Theorem 1.3, whose space complexity is bounded by \(O^*(2^{\alpha_1n})\le O^*(2^{\alpha n})\). This yields Theorem 1.5, restated below.

**Theorem 1.5.** _For every constant_ \(\alpha\) _satisfying_ \(0\le\alpha\le 1\)_, there is a Monte Carlo algorithm for ESS that runs in_ \(O^*(2^{\mathcal{T}(\alpha)n})\) _time and uses_ \(O^*(2^{\alpha n})\) _space, where_ \(\mathcal{T}(\alpha)\) _is defined in_ (8) _of Section 5.1._

## 5.2 Space-Bounded Algorithms via Theorem 3.8

We use Theorem 3.8 to obtain algorithms with smaller space bounds.

**Theorem 5.1.** _Assume that the minimum solution ratio satisfies_ \(\ell'\in(1/2,1-\epsilon]\) _for some constant_ \(\epsilon>0\)_. For every constant_ \(\alpha\) _satisfying_ \(1/2<\alpha\le\alpha_1\)_, where_ \(\alpha_1\) _is defined in_ (7)_, there is a Monte Carlo algorithm for ESS that uses_ \(O^*(2^{\alpha n})\) _space and runs in_ \(O^*(2^{\tau_\text{rrb}(\ell^\prime,\mathrm{max}\{0,\ell^\prime-\alpha\})n})\) _time._

_Proof._ Set \(k'=\mathrm{max}\{0,\ell'-\alpha\}\). Then \(k'\ge 0\). Moreover, since \(\alpha>1/2\) and \(\ell'<1\), we have \(2k'\le\ell'\), and we can apply Theorem 3.8. Since \(\ell'-k'=\mathrm{min}\{\ell',\alpha\}>1/2\), the space exponent is

\(\sigma_\text{rrb}(\ell',k')=\ell'-k'=\mathrm{min}\{\ell',\alpha\}\le\alpha.\)

Therefore, the space complexity is \(O^*(2^{\sigma_\text{rrb}(\ell^\prime,k^\prime)n})\le O^*(2^{\alpha n})\). The claimed running time follows directly from Theorem 3.8 with the above choice of \(k'\).

