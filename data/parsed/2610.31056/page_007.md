sponding worst-case regime. However, these results still leave open the possibility of quasipolynomial- time, or even subexponential-time (see Problem 2), algorithms for worst-case PESS when \(M\ge 2^{log^{2+\varepsilon}(n)}\).

## Technique behind our lower bound.

Inspired by the above, we show a connection between lattice problems and PESS. We achieve a tight lower bound, but in comparison to \[VV25\]: (i) we work only in the worst-case setting, (ii) we only show lower bounds against subexponential time algorithms, and (iii) Hypothesis 1 is much stronger than the assumptions in \[VV25\] (see discussion in Section 3).

Our reduction is from _n<sup>th</sup>-Successive Minima Problem_ (nSMP) (see Definition 4). The task in nSMP<sup>7</sup> is to find a nonzero lattice vector \(\mathbf{v}\in\mathcal{L}\) such that \(\|\mathbf{v}\|_2\le\lambda_n(\mathcal{L})\). By Theorem B.3, this formulation is equivalent (up to an irrelevant to us loss in approximation), to the approximate SIVP.

At a high level, the reduction is motivated by the classical sieve of Ajtai, Kumar, and Sivakumar \[AKS01\] for obtaining a short vector. However, our proof does not literally simulate a sieve. Instead, it samples many lattice vectors, encodes them as positive integers, invokes the assumed black-box PESS algorithm on the resulting instance, and decodes the returned equal-sum collision into a short lattice vector. Thus, PESS plays the role of a collision-finding primitive analogous in spirit to the sieve step.

More concretely, on input we are given an _n_-dimensional lattice L and we will use hypothetical _M_<sup>_o_(1/log_N_)</sup>-time algorithm that solves PESS on instances with \(N=\Theta(n^2)\) integers bounded by _M_=2<sup>O(_n_log_n_)</sup>. We start by preprocessing an _n_-dimensional lattice L. First, we compute a short basis **D**. If we use the state-of-the-art algorithms (e.g., \[Sch87, ALNSD20\]) in time \(\mathcal{O}(2^{\varepsilon n})\) we can compute a basis of length \(B\cdot\lambda_n(\mathcal{L})\), where \(B=n^{\Theta(1/\varepsilon)}\) for any tunable \(\varepsilon>0\). Next, we sample independent lattice points **x**<sup>(1)</sup>_,...,_**x**<sup>(_N_)</sup>∼_D_<sub>L_,s_</sub> using the (good) basis **D** generated in the first step, for a suitable Gaussian parameter \(s=\Theta(\sqrt{n}N\|\mathbf{D}\|_2)\). Standard tail bounds imply that, except with negligible probability, all sampled vectors satisfy<tbc>

\(\left\|\mathbf{x}^{(i)}\right\|_\infty\le BN^2\lambda_n(\mathcal{L})\text{for every}i\in[N].\)

<tbc>We then encode each sampled vector as a positive integer using a base-_W_ representation, where \(W=\Theta(BN^3)\). Schematically, the encoding has the form

\(a_i=W^n+\sum_{j=1}^nW^{j-1}\left\lfloor\frac{(\mathbf{x}^{(i)})_j/\lambda_n(\mathcal{L})}{r_j}\right\rfloor,\)

where each _r<sub>j</sub>_ is a random prime in \[_N_<sup>3</sup>\]; in the actual proof, we also add independent random shifts before rounding to ensure all integers are different with high probability. The additive term _W<sup>n</sup>_ ensures positivity, while the choice of _W_ is large enough to prevent carries between coordinates. Strictly speaking, the reduction does not know \(\lambda_n(\mathcal{L})\) in advance. Instead, it guesses this quantity up to a factor of 2 by enumerating powers of two, and for the correct guess obtains \(\widetilde{\lambda}_n\) satisfying \(\lambda_n(\mathcal{L})\le\widetilde{\lambda}_n\le 2\lambda_n(\mathcal{L})\) (similarly to Ajtai et al. \[AKS01\]). Accordingly, the encoding uses \(\widetilde{\lambda}_n\) in place of \(\lambda_n(\mathcal{L})\).

Since each coordinate contributes only O(_BN_<sup>2</sup>) to a digit, every encoded integer is at most _M_=(_BN_)<sup>O(_n_)</sup>. For our choice of parameters, this satisfies \(M\le 2^{o(N)}\), so the resulting instance lies in the subexponential input range covered by the assumed PESS algorithm.

<sup>7</sup>There is a well-studied lattice problem called the _Successive Minima Problem_ (SMP) \[Mic08\], which asks for _n_ linearly independent lattice vectors **v**<sub>1</sub>_,...,_**v**_<sub>n</sub>_ such that \(\|\mathbf{v}_i\|=\lambda_i(\mathcal{L})\) for every \(i\in[n]\).

