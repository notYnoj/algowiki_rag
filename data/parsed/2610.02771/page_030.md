_Proof._ Recall<tbc>

\(\beta_j(n)=\frac{\rho_j}{64}+2\sqrt{\frac{3\alpha_j\sigma^2x_n(\gamma)}{n}}+\frac{32\alpha_j\sigma^2x_n(\gamma)}{\rho_jn}.\)

<tbc>The bias term is already \(\rho_j/64\). It remains to make each of the two stochastic terms at most \(\rho_j/64\). First we bound the stitched logarithm at \(n_j^\circ\). Since<tbc>

\(x_n(\gamma)=log\left(\frac{\pi^2(1+\lfloor log_2n\rfloor)^2}{3\gamma}\right),\)

<tbc>there is a universal constant _c_<sub>1</sub>_\>_0 such that for all \(n\ge 2\),<tbc>

\(x_n(\gamma)\le c_1+log\frac{1}{\gamma}+2loglog(e^en).\)

<tbc>Here \(\gamma=\delta/[K(J+1)]\), so<tbc>

\(log\frac{1}{\gamma}=log\frac{K(J+1)}{\delta}.\)

<tbc>Moreover,<tbc>

\(n_j^\circ\le C_1\frac{\alpha_j\sigma^2}{\rho_j^2}\Gamma_j\)

<tbc>for a universal constant _C_<sub>1</sub> depending only on _C_, and<tbc>

\(\alpha_j=1+log\frac{32\sigma}{\rho_j}\le C_2log\left(e^e\frac{\sigma}{\rho_j}\right).\)

<tbc>Therefore<tbc>

\(loglog(e^en_j^\circ)\le C_3+loglog\left(e^e\frac{\sigma}{\rho_j}\right)+loglog\left(e^e\frac{K(J+1)}{\delta}\right),\)

<tbc>where the last term absorbs the dependence on \(\Gamma_j\). Hence, for a universal constant _C_<sub>0</sub>_\>_0,<tbc>

\(x_{n_j^\circ}(\gamma)\le C_0\Gamma_j.\) (7)

<tbc>Now choose the constant _C_ in the definition of \(n_j^\circ\) large enough so that<tbc>

\(2\sqrt{\frac{3\alpha_j\sigma^2C_0\Gamma_j}{n_j^\circ}}\le\frac{\rho_j}{64}\)

<tbc>and<tbc>

\(\frac{32\alpha_j\sigma^2C_0\Gamma_j}{\rho_jn_j^\circ}\le\frac{\rho_j}{64}.\)

<tbc>Using (7), both stochastic terms in \(\beta_j(n_j^\circ)\) are at most \(\rho_j/64\). Thus

\(\beta_j(n_j^\circ)\le\frac{\rho_j}{64}+\frac{\rho_j}{64}+\frac{\rho_j}{64}=\frac{3\rho_j}{64}<\frac{\rho_j}{16}=r_j.\)

In the algorithm, once an arm has \(\beta_{k,j}\le r_j\), it is not queried again in that phase unless all active arms already satisfy the same condition, in which case the phase ends. Therefore an arm receives at most \(n_j^\circ\) phase-_j_ samples.

**Lemma 28** (Elimination at the right scale)**.** _Assume_ E<sub>ph</sub> _holds. Fix a phase j. If a suboptimal active arm_ \(k\neq k^\star\) _satisfies_

\(\Delta_k>\varepsilon+\frac{\rho_j}{4},\)

_then by the time phase j ends, either the algorithm has already stopped or arm k has been eliminated._

_Proof._ If the algorithm stops during phase _j_, there is nothing to prove. Otherwise, phase _j_ ends only after every active arm has phase radius at most \(r_j=\rho_j/16\), and the elimination rule has been applied. Let _A_ be the active set at that point and define<tbc>

\(m:=max_{i\in A}LCB_{i,j}.\)

