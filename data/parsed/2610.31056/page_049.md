### Support in an \(\ell_\infty\)-ball.

Fix any single sample \(x\leftarrow\mathcal{D}_{\mathcal{L},s}\). We bound \(\mathbb{P}[\|x\|_\infty>R]\). A standard tail bound for (discrete) Gaussian measures<sup>16</sup> implies that for any \(t\ge 1\),<tbc>

\(\mathbb{P}\big[\|\mathbf{x}\|_2\ge ts\big]\le 2e^{-\pi t^2}\)

<tbc>Therefore, for _N_ independent samples **x**<sup>(1)</sup>_,...,_**x**<sup>(_N_)</sup>, another union bound gives

\(\mathbb{P}\big[\exists j\in[N]:\|\mathbf{x}^{(j)}\|_\infty>R\big]\)<br>
\(\le\mathbb{P}\big[\exists j\in[N]:\|\mathbf{x}^{(j)}\|_\infty>\sqrt{n\mathrm{log}(N)}s\big]\)<br>
\(\le\mathbb{P}\big[\exists j\in[N]:\|\mathbf{x}^{(j)}\|_2>\sqrt{n\mathrm{log}(N)}s\big]\)<br>
\(\le 2Ne^{-\pi n\mathrm{log}(N)}\le 2^{-n},\)

and hence (except with negligible probability) all outputs lie in \(\mathcal{L}\cap\mathrm{Ball}_\infty(0,R)\).

**Lemma A.2.1.** _Let_ D _denote the distribution_ D<sub>L_,s_</sub> _and_ **v**<sup>∗</sup> _be a shortest vector of_ L_. Then, the statistical distance between_ D _and_ D+**v**<sup>∗</sup> _is upper bounded by_<tbc>

\(\Delta(\mathsf{D},\mathsf{D}+\mathbf{v}^*)\le\sqrt{\frac{\pi}{2}}\frac{\|\mathbf{v}^*\|}{s}.\)

<tbc>_Proof._ We bound \(\Delta(\mathsf{D},\mathsf{D}+\mathbf{v}^*)\) for a shortest nonzero vector \(\mathbf{v}^*\in\mathcal{L}\) given by Pinsker’s inequality,<tbc>

\(\Delta(\mathsf{D},\mathsf{D}+\mathbf{v}^*)\le\sqrt{\frac{1}{2}\mathcal{D}_\mathrm{KL}(\mathsf{D}\|\mathsf{D}+\mathbf{v}^*)}.\)

<tbc>where,

\(\mathcal{D}_\mathrm{KL}(\mathsf{D}\|\mathsf{D}+\mathbf{v}^*)=\sum_{\mathbf{x}\in\mathcal{L}}\mathsf{D}(\mathbf{x})\mathrm{log}\frac{\mathsf{D}(\mathbf{x})}{\mathsf{D}(\mathbf{x}-\mathbf{v}^*)}\)<br>
\(=\frac{\pi}{s^2}\sum_{\mathbf{x}\in\mathcal{L}}\mathsf{D}(\mathbf{x})\big(\|\mathbf{x}-\mathbf{v}^*\|^2-\|\mathbf{x}\|^2\big),\)

where we used that fact that \(\rho_s(\mathcal{L})=\rho_s(\mathcal{L}+\mathbf{v}^*)\). Since \(\|\mathbf{x}-\mathbf{v}^*\|^2-\|\mathbf{x}\|^2=-2\langle\mathbf{x},\mathbf{v}^*\rangle+\|\mathbf{v}^*\|^2\) and D<sub>L_,s_</sub> is symmetric, we have \(\mathbb{E}_{\mathbf{x}\sim\mathsf{D}}[\mathbf{x}]=0\). Hence \(\mathcal{D}_\mathrm{KL}(\mathsf{D}\|\mathsf{D}+\mathbf{v}^*)=\frac{\pi\|\mathbf{v}^*\|^2}{s^2}\) . Therefore

\(\Delta(\mathcal{D}_{\mathcal{L},s},\mathcal{D}_{\mathcal{L},s}+\mathbf{v}^*)\le\sqrt{\frac{\pi}{2}}\frac{\|\mathbf{v}^*\|}{s}.\)

## B Proof of Theorem 5.1

In this section, we prove the following statement.

**Theorem 5.1.** _For any_ \(\kappa>0\)_, there exists a constant C\>_0 _and an algorithm such that, given an n- dimensional lattice_ L_, computes a basis_ **D**=\[**d**<sub>1</sub>_,...,_**d**_<sub>n</sub>_\] _of_ L _in time_ \(\mathcal{O}(2^{Cn/\kappa})\) _such that_ \(\|\mathbf{D}\|_2=\mathrm{max}_{i\in[n]}\|\mathbf{d}_i\|_2\le B\cdot\lambda_n(\mathcal{L})\)_, where_ \(B=C\cdot n^\kappa\).

<sup>16</sup>Refer \[DD18, Theorem 12\]

