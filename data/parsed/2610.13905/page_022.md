for \(\|\cdot\|\) the maximum-entry norm. This follows from (3.2), applied recursively, and was similarly observed by Schwartz et al. in the proof of \[53, Theorem 4.5\].

The focus of \[53\] is alternative basis _exact_ matrix multiplication (in the same model of floating-point arithmetic and using analogous definitions of stability factor/prefactor). Since their analysis does not assume that the bilinear form being evaluated is exact matrix multiplication, their bound immediately extends to the APA setting. Only one modification is necessary: the encoding matrices, basis transformations, and stability factor/prefactor now depend on the evaluation parameter \(\varepsilon\). We state a modified version of their main result below.

**Theorem 4.5** (Schwartz et al. \[53\])**.** _Let_ \(A\in\mathbb{C}^{m\times k}\) _and_ \(B\in\mathbb{C}^{k\times n}\) _and suppose that_ \(\widehat{C}\) _and C are the floating- point and exact arithmetic outputs of a recursive, alternative basis APA matrix multiplication algorithm (i.e., Algorithm 2) evaluated at_ \(\varepsilon\in\mathbb{C}\)_. If the base case of this algorithm multiplies_ \(m_0\times k_0\) _and_ \(k_0\times n_0\) _matrices, then we have_

\(\|\widehat{C}-C\|\le\left(k/k_0^L+Q(\varepsilon)L\right)\left(k/k_0^L\right)E(\varepsilon)^L\|A\|\|B\|\mathbf{u}+O(\mathbf{u}^2),\)

_where L is the required number of recursive steps,_ \(\|\cdot\|\) _is the maximum entry norm, and_ \(E(\varepsilon)\) _and_ \(Q(\varepsilon)\) _are the stability factor and prefactor of the algorithm, respectively._

## 4.2 Main Error Bound

We now prove the main result of this section, which exhibits (weak) forward stability for Algorithm 4 under some mild assumptions on the inputs and the two subroutines **Vandermonde-Solve** and **AltBasis- Recursive-APA**\(_{\langle\phi,\psi,\nu\rangle}\). The main insight of the proof is that Theorem 4.5 can be used to bound the error in a single evaluation of **AltBasis-Recursive-APA**\(_{\langle\phi,\psi,\nu\rangle}\) and moreover that this implies stability for Algorithm 4 when combined with the following observations:

• In the APA setting, the encoding matrices and basis transformations have functional entries, which must be evaluated at each evaluation point \(\varepsilon_j\). Nevertheless, if these entries are computed to high relative accuracy then only minor additional error is introduced (see Theorem A.3).<tbc>

• The sum reduction in line 5 is similarly unproblematic if **Vandermonde-Solve** satisfies (4.3).

Accordingly, Theorem 4.6 is stated in terms of two parameters \(\delta_1\) and \(\delta_2\), which denote how accurately (in terms of relative error) the solution to the Vandermonde system and the entries of the encoding matrices/basis transformations are computed. We choose to leave these as tunable parameters since, in practice, both the \(\alpha_j\) and the entries of \(U_\phi(\varepsilon_j)\), \(V_\psi(\varepsilon_j)\), \(W_\nu(\varepsilon_j)\), \(\phi_{\varepsilon_j}\), \(\psi_{\varepsilon_j}\) and \(\nu_{\varepsilon_j}^{-1}\) can be computed offline to whatever precision is desired (without changing the asymptotic cost of Algorithm 4). Recall that Theorem A.1 implies that \(\delta_1\) can be replaced with 3_p_**u**+_O_(**u**<sup>2</sup>) if we simply evaluate (4.1) directly.

**Theorem 4.6.** _Let_ \(A\in\mathbb{C}^{m\times k}\) _and_ \(B\in\mathbb{C}^{k\times n}\) _with C=AB. Suppose that_ \(\widehat{C}\) _is the output of a floating-point implementation of Algorithm 4 under the following conditions:_

1. _Both the entries of A and B and the evaluation parameters_ \(\varepsilon_1,\dots,\varepsilon_p\in\mathbb{C}\) _are normalized floating-point numbers. In addition, the_ \(\varepsilon_i\) _are nonzero with_ \(\varepsilon_i\neq\varepsilon_j\) _if_ \(i\neq j\).<tbc>

_2._ **Vandermonde-Solve** _satisfies the relative error bound_ (4.3) _for some small constant_ \(\delta_1>0\).<tbc>

_3._ **AltBasis-Recursive-APA**\(_{\langle\phi,\psi,\nu\rangle}\) _implements a recursive, alternative basis APA matrix multiplication algorithm, defined by encoding matrices_ \(U_\phi(\varepsilon)\), \(V_\psi(\varepsilon)\), \(W_\nu(\varepsilon)\) _and symbolic basis transformations_ \(\phi_\varepsilon\), \(\psi_\varepsilon\), \(\nu_\varepsilon^{-1}\)_. The base case of this algorithm, which is reached after_ \(L\in\mathbb{N}\) _recursive steps for_<tbc>

<tbc>\(L\le min\left\{log_{m_0}(m),log_{k_0}(k),log_{n_0}(n)\right\},\)<tbc>

<tbc>_defaults to classical matrix multiplication. We additionally assume that_ \(m_0^L\), \(k_0^L\)_, and_ \(n_0^L\) _divide m, k, and n, respectively._<tbc>

_4._ _For each_ \(\varepsilon_i\)_, the nonzero entries of_ \(U_\phi(\varepsilon_i)\), \(V_\psi(\varepsilon_i)\), \(W_\nu(\varepsilon_i)\), \(\phi_{\varepsilon_i}\), \(\psi_{\varepsilon_i}\)_, and_ \(\nu_{\varepsilon_i}^{-1}\) _belong to the normalized range of the floating-point system and are computed to relative accuracy_ \(\delta_2\) _for some_ \(0<\delta_2<1\).<tbc>

