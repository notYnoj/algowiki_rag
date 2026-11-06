<tbc>in expectation (as \(\delta\le\frac{1}{logn}\)), we get that<tbc>

\(\mathbb{E}[Q]\le(1+o(1))\left(\frac{logn}{I(p)}+\frac{2log(1/\delta)}{(1-2p)log\frac{1-p}{p}}\right)+\mathbb{E}[Q]\cdot\mathbb{P}[restart].\)

<tbc>Therefore,

\(\mathbb{E}[Q]\le(1+o(1))\cdot\frac{1}{1-\frac{2}{logn}}\cdot\left(\frac{logn}{I(p)}+\frac{2log(1/\delta)}{(1-2p)log\frac{1-p}{p}}\right)\)<br>
\(\le(1+o(1))\left(\frac{logn}{I(p)}+\frac{2log(1/\delta)}{(1-2p)log\frac{1-p}{p}}\right),\)

as desired.

## 6 Discussions

In this section we discuss a few possible extensions of our results.

### Varying _p_.

In our main results for Noisy Sorting, we have assumed that _p_ remains constant as \(n\rightarrow\infty\). This assumption is necessary in several places of our proofs as discussed below and we leave it as an open problem to drop this assumption.

For \(p\rightarrow\frac{1}{2}\) as \(n\rightarrow\infty\), Theorem 1 still holds. For the proof, one needs to suitably modify Corollary 12, Lemma 17, Lemma 18, Corollary 19, Lemma 20 to handle \(p\rightarrow\frac{1}{2}\) correctly. For example, in our current statement of Corollary 19 we ignore constants related to _p_ in the expressions for \(Var[\tau]\). By choosing _m_ in Lemma 18 carefully, we can let \(Var[\tau]=(\mathbb{E}[\tau])^2polylog(n)\) even for growing _p_, which suffices for the concentration results. For the lower bound (Theorem 2), Lemma 27 may become problematic. It seems possible to modify the proof of Lemma 27 to handle the case _I(p_)=_n_<sup>-_o_(1)</sup>. However, for \(I(p)=n^{-\Omega(1)}\) a stronger method is needed.

For \(p\rightarrow 0\) as \(n\rightarrow\infty\), the lower bounds hold without any change. For the algorithms, our derandomization method would result in too many queries when _p=O_(1/log_n_).

We similarly leave the task of dropping the assumption that _p_ remains a constant in our Noisy Binary Search results as an open problem.

### Non-uniform _p_ and semi-random adversary.

In our main results we have assumed that the probability of error in the comparisons remains constant. One possible extension is that in each noisy comparison, the result is flipped with some probability at most _p_, where this probability can be adversarially chosen for each query. (The algorithm knows _p_ but does not know the flip probability for individual comparisons.) This model is sometimes called semi-random adversary in literature (e.g., \[MWR18\]). It is an interesting open problem to generalize our results to this model.

### Dependency on \(\delta\).

In our bounds for Noisy Sorting, we simply used _o_(1) as our error probability. We leave it as an open problem to generalize our bounds to the case where the error probability \(\delta\) can also be specified.

