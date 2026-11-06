Therefore, for every \(k\in[n]\),<tbc>

\(\sum_{i\in X}\left\lfloor\frac{(\mathbf{x}^{(i)})_k/\tilde{\lambda}_n+s_k}{r_k}\right\rfloor=\sum_{j\in Y}\left\lfloor\frac{(\mathbf{x}^{(j)})_k/\tilde{\lambda}_n+s_k}{r_k}\right\rfloor.\)

<tbc>Using the elementary bound \(t-1\le\lfloor t\rfloor\le t\), we conclude that<tbc>

\(\left|\sum_{i\in X}\frac{(\mathbf{x}^{(i)})_k/\tilde{\lambda}_n+s_k}{r_k}-\sum_{j\in Y}\frac{(\mathbf{x}^{(j)})_k/\tilde{\lambda}_n+s_k}{r_k}\right|\le|X|+|Y|\le 2N.\)

<tbc>Since |_X_|=|_Y_|, the terms involving _s<sub>k</sub>_ cancel, and we obtain<tbc>

\(\left|\frac{1}{r_k\tilde{\lambda}_n}\left(\sum_{i\in X}(\mathbf{x}^{(i)})_k-\sum_{j\in Y}(\mathbf{x}^{(j)})_k\right)\right|\le 2N.\)

<tbc>By the definition of **v**, this is<tbc>

\(\frac{|\mathbf{v}_k|}{r_k\tilde{\lambda}_n}\le 2N.\)

<tbc>Since \(r_k\le N^3\), it follows that \(|\mathbf{v}_k|\le 2N^4\tilde{\lambda}_n\), for every \(k\in[n]\). Hence

\(\|\mathbf{v}\|_\infty\le 2N^4\tilde{\lambda}_n\text{and}\|\mathbf{v}\|_2\le 2\sqrt{n}N^4\tilde{\lambda}_n.\)

Thus, conditioned on the event that all sampled vectors satisfy \(\|\mathbf{x}^{(i)}\|_\infty\le N^2B\tilde{\lambda}_n\), the constructed multiset A is a valid strong-regime PESS instance, and the solution returned by PESS yields a lattice vector \(\mathbf{v}\in\mathcal{L}\) of norm at most \(2\sqrt{n}N^4\tilde{\lambda}_n\le 4\sqrt{n}N^4\lambda_n(\mathcal{L})\le N^5\cdot\lambda_n(\mathcal{L})\) as \(N=\Omega(nlogn)\).

## Proof of Property (3)

It remains to show that the lattice vector returned by the modified reduction is nonzero with constant probability. Recall that, in the modified reduction, each sampled vector is of the form

\(\mathbf{x}^{(i)}=\mathbf{x}'^{(i)}+\tau_i\mathbf{v}^*,\)

where \(\mathbf{x}'^{(i)}\sim\mathcal{D}_{\mathcal{L},s}\), each \(\tau_i\in\{0,1\}\) is an independent uniform bit, and **v**<sup>∗</sup> is a fixed shortest nonzero vector of L. We first bound the probability that the encoding changes when **v**<sup>∗</sup> is added.

**Claim 5.2.1.** _Let_ \(\alpha\) _be uniformly random in_ \[_N_<sup>2</sup>\] _and let_ \(\beta\) _be uniformly random among all primes in_ \[_N_<sup>3</sup>\]_. For fixed_ \(b,\varepsilon\in\mathbb{R}\) _satisfying_ \(b\in[-BN^2,BN^2]\) _and_ \(\varepsilon\in[-1,1]\)_, we have_<tbc>

\(\mathbb{P}_{\alpha,\beta}\left[\left\lfloor\frac{b+\alpha}{\beta}\right\rfloor\neq\left\lfloor\frac{b+\varepsilon+\alpha}{\beta}\right\rfloor\right]\le\mathcal{O}\left(\frac{1}{N^2}+\frac{log(BN^2+N^2)logN}{N^3}\right).\)

<tbc>_In particular, if_ \(B\ge N\)_, then this is_<tbc>

\(\mathcal{O}\left(\frac{1}{N^2}+\frac{log(BN)logN}{N^3}\right).\)

<tbc>_Proof:_ For a fixed value of \(\alpha\), define \(x:=b+\alpha\). Consider the bad event<tbc>

\(\mathcal{E}_{\alpha,\beta}:=\left\{\left\lfloor\frac{x}{\beta}\right\rfloor\neq\left\lfloor\frac{x+\varepsilon}{\beta}\right\rfloor\right\}.\)

