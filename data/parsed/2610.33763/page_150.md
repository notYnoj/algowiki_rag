We now recall the result proven in \[1\], concerning the general GLT setting with \(d,r\ge 1\) and when at least one of the involved GLT symbols is invertible a.e.

**Theorem 9.3 \[1\], Theorem 5)** _Let_ \(r,d\ge 1\)_. Suppose_ \(\{A_\mathbf{n}\}_\mathbf{n}\sim_\mathrm{GLT}\kappa\) _and_ \(\{B_\mathbf{n}\}_\mathbf{n}\sim_\mathrm{GLT}\xi\)_, where_ \(A_\mathbf{n},B_\mathbf{n}\in\mathcal{P}_\mathbf{n}\) _for every multi-index **n**. Assume that at least one of the minimal eigenvalue of_ \(\kappa\) _and the minimal eigenvalue of_ \(\xi\) _is nonzero almost everywhere. Then_

\(\{G(A_\mathbf{n},B_\mathbf{n})\}_\mathbf{n}\sim_\mathrm{GLT}G(\kappa,\xi),\) (9.7)

_and_

\(\{G(A_\mathbf{n},B_\mathbf{n})\}_\mathbf{n}\sim_{\sigma,\lambda} G(\kappa,\xi).\) (9.8)

_Furthermore_ \(G(\kappa,\xi)=(\kappa\xi)^{1/2}\) _whenever the GLT symbols_ \(\kappa\) _and_ \(\xi\) _commute._

Assume that \(\{A_n\}_n\sim_\mathrm{GLT}\kappa\) and \(\{B_n\}_n\sim_\mathrm{GLT}\xi\), where \(A_n,B_n\in\mathcal{P}_\mathbf{n}\) for every multi-index **n**, with P**<sub>n</sub>** denoting the set of HPD matrices of size _rN_(**n**), where \(N(\mathbf{n})=\prod_{r=1}^dn_r\).

**Theorem 9.4** _Let r\>_1 _and_ \(d\ge 1\)_. Assume that_ \(\{A_\mathbf{n}\}_\mathbf{n}\sim_\mathrm{GLT}\kappa\) _and_ \(\{B_\mathbf{n}\}_\mathbf{n}\sim_\mathrm{GLT}\xi\)_, where_ \(A_\mathbf{n},B_\mathbf{n}\in\mathcal{P}_\mathbf{n}\) _for every multi-index **n**, with_ P**<sub>n</sub>** _denoting the set of HPD matrices of size rN_(**_n_**)_. Under the assumption that_ \(\kappa\) _and_ \(\xi\) _commute we infer_

\(\{G(A_\mathbf{n},B_\mathbf{n})\}_\mathbf{n}\sim_\mathrm{GLT}(\kappa\xi)^{1/2},\)<br>
\(\{G(A_\mathbf{n},B_\mathbf{n})\}_\mathbf{n}\sim_{\sigma,\lambda}(\kappa\xi)^{1/2},\)

**Proof:** Since \(\{A_\mathbf{n}\}_\mathbf{n}\sim_\mathrm{GLT}\kappa\), \(\{B_\mathbf{n}\}_\mathbf{n}\sim_\mathrm{GLT}\xi\), we deduce that \(\kappa,\xi:[0,1]^d\times[-\pi,\pi]^d\rightarrow\mathbb{C}^{r\times r}\) are Hermitian nonnegative definite, because, by the assumptions, _A<sub>**n**</sub>,B<sub>**n**</sub>_ are HPD matrices \(\forall\mathbf{n}\). Therefore, the minimal eigenvalue of \(\kappa\) and the minimal eigenvalue of \(\xi\) are nonnegative almost everywhere. Here, we assume that \(\mu_{2d}(\lambda_\mathrm{min}(\kappa)\equiv 0)>0\) and \(\mu_{2d}(\lambda_\mathrm{min}(\xi)\equiv 0)>0\), in such a way that the hypotheses of Theorem 9.3 are violated. Let \(\varepsilon>0\), let \(\kappa_\varepsilon=\kappa+\varepsilon I_r\), _I<sub>r</sub>_ being the identity of size _r_, and let \(A_{\mathbf{n},\varepsilon}=A_\mathbf{n}+\varepsilon I_{rN(\mathbf{n})}\). Now \(\{\varepsilon I_{rN(\mathbf{n})}=T_\mathbf{n}(\varepsilon I_r)\}_\mathbf{n}\sim_\mathrm{GLT}\varepsilon I_r\) by the first part of GLT 2 (the identity _I_<sub>_rN_(**_n_**)</sub> is a special multilevel block Toeplitz matrix with GLT symbol _I<sub>r</sub>_). Consequently, by exploiting linearity i.e. the second item of GLT 3, it follows that<tbc>

\(\{A_{\mathbf{n},\varepsilon}\}_\mathbf{n}\sim_\mathrm{GLT}\kappa_\varepsilon,\kappa_\varepsilon\ge\varepsilon I_r\text{a.e.}\)

<tbc>Since \(\kappa,\xi\) are both nonnegative definite almost everywhere. Hence, by Theorem 9.3, we have \(\{G(A_{\mathbf{n},\varepsilon},B_\mathbf{n})\}_\mathbf{n}\sim_\mathrm{GLT}(\kappa_\varepsilon\xi)^\frac{1}{2}\), since the commutation between \(\kappa\) and \(\xi\) implies the commutation between \(\kappa_\varepsilon=\kappa+\varepsilon I_r\) and \(\xi\). By exploiting the ∗-algebra features of the GLT matrix sequences, and specifically the third item of GLT 3 and GLT 6 with the function \(f(z)=z^\frac{1}{4}\), we deduce \(\{(A_{\mathbf{n},\varepsilon} B_\mathbf{n}^2A_{\mathbf{n},\varepsilon})^\frac{1}{4}\}_\mathbf{n}\sim_\mathrm{GLT}(\kappa_\varepsilon^2\xi^2)^\frac{1}{4}=(\kappa_\varepsilon\xi)^\frac{1}{2}\), which is the very same GLT symbol of \(\{G(A_{\mathbf{n},\varepsilon},B_\mathbf{n})\}_\mathbf{n}\). As a result, again by the second item of GLT 3, the difference between these sequences satisfies the following asymptotic relation

\(\{G(A_{\mathbf{n},\varepsilon},B_\mathbf{n})-(A_{\mathbf{n},\varepsilon} B_\mathbf{n}^2A_{\mathbf{n},\varepsilon})^\frac{1}{4}\}_\mathbf{n}\sim_\mathrm{GLT}0.\) (9.9)

In other words, we have written a new GLT matrix sequence having the same symbol as the geometric mean matrix sequence \(\{G(A_{\mathbf{n},\varepsilon},B_\mathbf{n})\}_\mathbf{n}\), but where no inversion is<tbc>

