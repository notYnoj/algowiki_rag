**Observation B.2.** _The matrices_ \(L_G,L_G^+,L_G^{+/2}\)_, and_ \(\Pi\) _have the same set of orthogonal eigenvectors u_<sub>1</sub>_,...,u_<sub>_n_-1</sub> _and_ \(\frac{1}{\sqrt{n}}\cdot\vec{1}\)_. They also share the same kernel which is_ \(span(\vec{1})\).

For any edge _e_, denote \(R_e:=\chi_e^\top L_G^+\chi_e\). This quantity is also known as _effective resistance_. A trace argument asserts that the weighted effective resistances sums up to exactly _n_-1. This is known as the Forster’s Theorem.

**Theorem B.3.** _For a connected graph G, we have_ \(\sum_{e\in G}w_eR_e=n-1\).

The following theorem characterizes the top and bottom eigenvalue of a matrix.

**Theorem B.4** (Courant-Fischer formula)**.** \(\lambda_1(M)=max_{v\neq\vec{0}}\frac{v^\top Mv}{v^\top v}\) _and_ \(\lambda_n(M)=min_{v\neq\vec{0}}\frac{v^\top Mv}{v^\top v}\) .

**Corollary B.5.** _For any vector_ \(v\in\mathbb{R}^n\)_, an_ \(n\times n\) _matrix_ \(vv^\top\) _is psd. Moreover, we have_ \(\lambda_1(vv^\top)=\|v\|_2^2\).

_Proof._ For any \(x\in\mathbb{R}^n\), we have \(x^\top(vv^\top)x=\|x^\top v\|_2^2\ge 0\). Thus, \(vv^\top\) is psd. Furthermore, for \(x\neq 0^n\), we have

\(\frac{x^\top(vv^\top)x}{\|x\|_2^2}=\frac{\|x^\top v\|_2^2}{\|x\|_2^2}=\frac{\langle x,v\rangle^2}{\|x\|_2^2}\le\|v\|^2\)

due to the Cauchy-Schwartz inequality. Moreover, the equality is attained when _x=v_. This implies \(\lambda_1(vv^\top)=\|v\|_2^2\) as wished.

We will later need the following matrix concentration bounds which is a simple extension of the the matrix Chernoff bounds \[Tro11\].

**Theorem B.6** (Extended Matrix Chernoff Bounds)**.** _Consider a finite sequence_ {_X<sub>k</sub>_} _of independent random, psd symmetric matrices of dimension n. Let R be a positive scalar such that each of the random matrix satisfies_ \(\lambda_1(X_k)\le R\) _almost surely. Also let_ \(\{\widetilde{X}_l\}\) _be a finite of (deterministic) symmetric psd matrices. Denote_ \(\mathsf{X}=\sum_{i\in[k]}X_i+\sum_{j\in[l]}\widetilde{X}_j\)_. Finally, define:_<tbc>

\(\mu_\mathrm{min}:=\lambda_n(\mathbb{E}[\mathsf{X}])\text{\textit{and}}\mu_\mathrm{max}:=\lambda_1(\mathbb{E}[\mathsf{X}]).\)

<tbc>_Then for any_ \(\delta\in(0,1)\)_, we have:_<tbc>

\(\mathrm{Pr}\left[\lambda_1(\mathsf{X})\ge(1+\delta)\mu_\mathrm{max}\right]\le n\cdot\mathrm{exp}\left(-\frac{\delta^2\mu_\mathrm{max}}{3R}\right)\)

<tbc>_and_

\(\mathrm{Pr}\left[\lambda_n(\mathsf{X})\le(1-\delta)\mu_\mathrm{min}\right]\le n\cdot\mathrm{exp}\left(-\frac{\delta^2\mu_\mathrm{min}}{2R}\right).\)

We make a few remarks regarding the theorem. First of all, unlike the original statement of \[Tro11\], here we include a set of deterministic matrices \(\{\widetilde{X}_l\}\). Secondly, we will eventually apply such theorem with a set of matrices that yields \(\mathbb{E}[\mathsf{X}]=\Pi\) whose eigenvalues are 1 with multiplicity _n_-1 and 0 with multiplicity 1 (w.r.t. eigenvector \(\vec{1}\)). Since it suffices to only work with vectors orthogonal to \(\vec{1}\), we can treat \(\Pi\) as having all eigenvalues 1.<sup>9</sup> These assumptions we made do not affect the integrity of such theorem nor of our proofs.

<sup>9</sup>To see this, let \(\Pi':=\Pi+\frac{1}{n}\cdot\vec{1}\vec{1}^\top\) so that it has the same set of eigenvectors as \(\Pi\) but now all eigenvalues are 1s. Then, for any vector \(v\perp\vec{1}\), we have \(v^\top\Pi'v=v^\top\Pi v\).

