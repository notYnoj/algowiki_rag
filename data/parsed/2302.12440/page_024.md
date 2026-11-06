<tbc>then by regarding \(U^\equiv\) as \(\tau\) and _W_ as \(X_\tau\) in Lemma 28, with probability \(\Omega(\delta)-o_{|S|}(1)\), we have<tbc>

\(W\le\frac{|S|log|S|}{log\frac{1-p}{p}}\)

<tbc>and then

\(|S|\left(\frac{1-p}{p}\right)^{-W/|S|}\ge 1,\)

which is a contradiction.

Thus,

\(\mathbb{E}[U^\equiv]\ge(1-o(1))\frac{|S|log|S|}{(1-2p)log\frac{1-p}{p}},\)

as desired.

Now we are ready to prove Theorem 2.

_Proof of Theorem 2._ Fix an algorithm for NoisySorting(_n_) with error probability _o_(1).

Take _k_=log_n_. Let \(n'=k\lfloor n/k\rfloor\). Clearly, an algorithm for NoisySorting(_n_) can be used to solve NoisySorting(\(n'\)) with less or equal number of queries in expectation. Let \(U^\neq\), \(U^\equiv\) be as defined in Lemma 26, Lemma 29 for \(n'\) and _k_.

By Lemma 26 and Lemma 27, we have<tbc>

\(\mathbb{E}[U^\neq]\ge(1-o(1))\frac{n'logn'}{I(p)}-(n'-n'/k)=(1-o(1))\frac{n'logn'}{I(p)}.\)

<tbc>By Lemma 29, we have<tbc>

\(\mathbb{E}[U^\equiv]\ge(1-o(1))\frac{(n'-n'/k)log(n'-n'/k)}{(1-2p)log\frac{1-p}{p}}=(1-o(1))\frac{n'logn'}{(1-2p)log\frac{1-p}{p}}.\)

<tbc>Therefore expected number of queries made by the algorithm is at least

\(\mathbb{E}[U^\neq]+\mathbb{E}[U^\equiv]\ge(1-o(1))\left(\frac{1}{I(p)}+\frac{1}{(1-2p)log\frac{1-p}{p}}\right)n'logn'\)<br>
\(=(1-o(1))\left(\frac{1}{I(p)}+\frac{1}{(1-2p)log\frac{1-p}{p}}\right)nlogn.\)

## 5 Noisy Binary Search

In this section, we prove our lower and upper bounds for Noisy Binary Search.

