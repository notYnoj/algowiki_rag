and then

\(2\left(\frac{1-p}{p}\right)^{-W/2}\ge 2\delta^{1-\sigma/8}.\)

Because the error probability is \(\le 1.1\delta\), with probability at least \(1-\frac{1.1\delta}{10\delta/\sigma}\ge 1-\frac{\sigma}{9}\), we have \(1-q_k\le 10\delta/\sigma\), which leads to \(q_{k-1}+q_{k+1}\le 10\delta/\sigma\). Therefore,

\(2\left(\frac{1-p}{p}\right)^{-W/2}\le\frac{q_{k-1}+q_{k+1}}{q_k}\le\frac{10\delta/\sigma}{1-10\delta/\sigma}<20\delta/\sigma.\)

(In the last step we use \(\delta\le 1/logn\) and thus \(1-10\delta/\sigma>\frac{1}{2}\) for sufficiently large _n_.) This is a contradiction because \(2\delta^{1-\sigma/8}\ge 20\delta/\sigma\) and \(\frac{\sigma}{8}+\left(1-\frac{\sigma}{9}\right)-o_{1/\delta}(1)>1\) when \(\delta\le 1/logn\) and _n_ is large enough.

Thus,

\(\mathbb{E}[U^\approx|k\unknown\in\{0,n\}]\ge(2-o(1))\frac{log\frac{1}{\delta}}{(1-2p)log\frac{1-p}{p}}.\)

Consequently,

\(\mathbb{E}[U^\approx]\ge\mathbb{E}[U^\approx|k\unknown\in\{0,n\}]\cdot Pr[k\unknown\in\{0,n\}]\ge(2-o(1))\frac{log\frac{1}{\delta}}{(1-2p)log\frac{1-p}{p}}.\)

Now we are ready to prove Theorem 3.

_Proof of Theorem 3._ If \(\delta\ge 1/logn\), then by Lemma 31, 32,

\(\mathbb{E}[U]\ge\mathbb{E}[U^\approx]\)<br>
\(\ge(1-\delta-o(1))\frac{logn}{I(p)}\)<br>
\(\ge(1-o(1))\left((1-\delta)\frac{logn}{I(p)}+\frac{2log\frac{1}{\delta}}{(1-2p)log\frac{1-p}{p}}\right).\)

If \(\delta\le 1/logn\), then by combining Lemma 31, 32, 33, for any algorithm, the number of queries _U_ satisfies

\(\mathbb{E}[U]\ge\mathbb{E}[U^\approx]+\mathbb{E}[U^\unknown]\)<br>
\(\ge(1-\delta-o(1))\frac{logn}{I(p)}+(2-o(1))\frac{log\frac{1}{\delta}}{(1-2p)log\frac{1-p}{p}}\)<br>
\(\ge(1-o(1))\left((1-\delta)\frac{logn}{I(p)}+\frac{2log\frac{1}{\delta}}{(1-2p)log\frac{1-p}{p}}\right).\)

