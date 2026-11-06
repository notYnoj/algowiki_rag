This result suggests that the (optimal) stability of an approximate-to-exact APA matrix multiplication algorithm is characterized by the behavior of the corresponding stability factor/prefactor near the unit circle.

Before moving on, we note that using approximate roots of unity for \(\varepsilon_1,\dots,\varepsilon_p\) as suggested above will necessarily turn any APA algorithm into one with complex encoding matrices, which may considerably drive up the arithmetic cost of the algorithm (by a constant factor). This marks an efficiency/stability tradeoff for users to navigate. Of course, the bounds proved in this section are potentially loose, meaning that in practice, there may be little performance difference (in terms of accuracy) between Algorithm 4 with approximate roots of unity and real \(\varepsilon_1,\dots,\varepsilon_p\).

## 4.4 Extensions

A drawback of Algorithm 4 is the need to evaluate **AltBasis-Recursive-APA**\(_{\langle\phi,\psi,\nu\rangle}\) at _p=dL_+1 points, which ultimately leads to a logarithmic factor increase in its complexity. To get around this, we consider here an alternative, _truncated_ version of Algorithm 4, which evaluates **AltBasis-Recursive-APA**\(_{\langle\phi,\psi,\nu\rangle}\) a fixed _r\<p_ times and takes a linear combination of the outputs to cancel the first _r_-1 terms of the remainder (see Algorithm 5).

**Algorithm 5** Truncated Approximate-to-Exact Alternative Basis APA Matrix Multiplication<br>
**Input:** \(A\in\mathbb{C}^{m\times k}\), \(B\in\mathbb{C}^{k\times n}\) and parameters \(\varepsilon_1,\dots,\varepsilon_r\in\mathbb{C}\), where \(|\varepsilon_j|<1\) and \(r\le dL+1\).<br>
**Output:** \(C=AB+\left(\sum_{j=1}^r\alpha_j\varepsilon_j^r\right)R_r+\cdots+\left(\sum_{j=1}^r\alpha_j\varepsilon_j^{p-1}\right)R_{p-1}\).

1: \([\alpha_1,\dots,\alpha_r]=\text{\textbf{Vandermonde-Solve}}(\varepsilon_1,\dots,\varepsilon_r)\)

2: **for** _j_=1:_r_ **do**

3: \(C_j=\text{\textbf{AltBasis-Recursive-APA}}_{\langle\phi,\psi,\nu\rangle}(A,B,\varepsilon_j)\)

4: **end for**

5: \(C=\alpha_1C_1+\alpha_2C_2+\cdots+\alpha_rC_r\)

6: **return** _C_

If the evaluation parameters \(\varepsilon_1,\dots,\varepsilon_r\) satisfy \(|\varepsilon_j|<1\) for all _j_, we can expect that the output of this algorithm will be close to _C_, as the portion of the remainder left over depends on powers of \(\varepsilon\) that are _r_ or larger. Again, this trades stability for performance; in this setting, we have both a nonvanishing remainder _and_ evaluation parameters that are more tightly spaced (the latter increasing the error incurred by **Vandermonde-Solve** in floating point). Nevertheless, the improved efficiency is significant, particularly when _r=O_(1).

To derive an error bound for Algorithm 5, we first need the following technical lemma, which bounds the norms of the residual matrices _R_<sub>1</sub>_,...,R_<sub>_p_-1</sub>.

**Lemma 4.8.** _Let_ \(R_l\in\mathbb{C}^{m\times n}\), \(1\le l\le p-1\) _be the residual matrices associated to a recursive, alternative basis APA matrix multiplication routine (see Algorithm 2) with input matrices_ \(A\in\mathbb{C}^{m\times k}\) _and_ \(B\in\mathbb{C}^{k\times n}\)_. Then_

\(\|R_l\|\le\frac{(k/k_0^L)}{p}\left[\sum_{j=1}^pE(e^{2\pi ij/p})^L\right]\|A\|\|B\|,\)

_where_ \(\|\cdot\|\) _is the maximum entry norm and_ \(E(\varepsilon)\) _is the stability factor of the algorithm._

_Proof._ Let \((\alpha_1^l,\dots,\alpha_p^l)^T\in\mathbb{C}^p\) be the solution to the Vandermonde system (1.5) with the right hand side replaced by the (_l_+1)-st standard basis vector and the evaluation parameters \(\varepsilon_1,\dots,\varepsilon_p\) taken to be the _p_-th roots of unity - i.e., \(\varepsilon_j=e^{2\pi ij/p}\). If _C<sub>j</sub>_ is the exact-arithmetic output of one run of Algorithm 2 applied to _A_ and _B_ with evaluation parameter \(\varepsilon_j\), then we have<tbc>

\(R_l=\alpha_1^lC_1+\alpha_2^lC_2+\cdots+\alpha_p^lC_p.\)

<tbc>Recalling (4.4), we can bound \(\|C_j\|\) as \(\|C_j\|\le(k/k_0^L)E(\varepsilon_j)^L\|A\|\|B\|\) for each \(1\le j\le p\). Hence,<tbc>

\(\|R_l\|\le\sum_{j=1}^p|\alpha_j^l|\|C_j\|\le\frac{(k/k_0^L)}{p}\left[\sum_{j=1}^pE(e^{2\pi ij/p})^L\right]\|A\|\|B\|,\)

