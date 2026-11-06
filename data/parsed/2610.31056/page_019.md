where \(\Delta(\cdot,\cdot)\) denotes statistical distance. Applying Lemma C.0.1, we obtain

\(\Delta\big((\mathbf{x}^{(1)},\dots,\mathbf{x}^{(N)}),(\mathbf{x}^\prime^{(1)}+\tau_1\mathbf{v}^*,\dots,\mathbf{x}^\prime^{(N)}+\tau_N\mathbf{v}^*)\big)\)<br>
\(\le\mathcal{O}(B^{-1}).\)

We will set _B_ to be large polynomial, and hence O(_B_<sup>-1</sup>) will be 1/poly(_n_). In particular, the failure probability of the original reduction is at most the failure probability of the modified reduction plus an additive O(_B_<sup>-1</sup>) term. Combining this with the negligible discrepancy between the actual sampler and the idealized sampler, it remains to bound the failure probability of the modified reduction.<br>
We do so in three steps with respect to the correct guess \(\tilde{\lambda}_n\), i.e., \(\lambda_n(\mathcal{L})\le\tilde{\lambda}_n\le 2\lambda_n(\mathcal{L})\).

(1) We bound the \(\ell_\infty\)-norms of the sampled vectors **x**<sup>(_i_)</sup> with sufficiently high probability. This will allow us to control the encoding range and determine a suitable choice of _W_.<tbc>

(2) We show that the resulting multiset of integers (_a_<sub>1</sub>_,...,a<sub>N</sub>_) forms a valid PESS instance, in particular that its total sum is at most 2<sup>_o(N_)</sup>. This ensures that the PESS algorithm returns a valid solution, from which the reduction constructs a lattice vector of the desired length.<tbc>

(3) Finally, we show that the output lattice vector is nonzero with constant probability.

## Proof of Property (1):

We first bound the \(\ell_\infty\)-norms of the sampled lattice vectors. Recall that the reduction sets \(s:=4\pi\sqrt{n}N\left\|\mathbf{D}\right\|_2\). By Theorem 5.2, for any \(R\ge s\sqrt{nlogn}N\), the sampled vectors satisfy<tbc>

\(\left\|\mathbf{x}^\prime^{(i)}\right\|_\infty\le R\text{for all}i\in[N],\)

<tbc>except with probability at most 2<sup>-_n_</sup>. Note that for all sufficiently large _n_, \(BN^2\tilde{\lambda}_n\ge s\sqrt{nlogn}N\). Indeed, by substituting the value of _s_, this condition becomes<tbc>

\(BN^2\tilde{\lambda}_n\ge 4\pi\sqrt{n}N\left\|\mathbf{D}\right\|_2\cdot\sqrt{nlogn}N,\)

<tbc>which is equivalent to \(N\ge 2\pi n\sqrt{logN}\). This holds for all sufficiently large _n_ since we set \(N=\Omega(nlogn)\). Therefore, we conclude that, except with probability at most 2<sup>-_n_</sup>,

\(\left\|\mathbf{x}^\prime^{(i)}\right\|_\infty\le BN^2\tilde{\lambda}_n\text{for all}i\in[N].\)

In the remainder of the correctness analysis, we condition on this event. In particular, this bound will allow us to choose a suitable value of _W_ and to control the magnitudes of the encoded integers _a<sub>i</sub>_.

## Proof of Property (2):

We now show that, conditioned on the event<tbc>

\(\left\|\mathbf{x}^\prime^{(i)}\right\|_\infty\le BN^2\tilde{\lambda}_n\text{for all}i\in[N],\)

<tbc>the constructed multiset A:={_a_<sub>1</sub>_,...,a<sub>N</sub>_} is a valid input to the PESS algorithm, and that any equal-sum solution returned by PESS yields a short lattice vector. Recall that the reduction sets _W_:=8_BN_<sup>3</sup> and<tbc>

\(a_i=f(\mathbf{x}^{(i)}):=W^n+\sum_{j=1}^nW^{j-1}\left\lfloor\frac{(\mathbf{x}^\prime^{(i)})_j/\tilde{\lambda}_n+s_j}{r_j}\right\rfloor,\)

