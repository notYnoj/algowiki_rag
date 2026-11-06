## 5.2 Upper Bound

In this section we prove our upper bound for Noisy Binary Search.

**Theorem 4** (Noisy Binary Search Upper Bound)**.** _There exists a randomized algorithm for_ NoisyBinarySearch(_n_) _with error probability_ \(\le\delta\) _that makes at most_

\((1+o(1))\left((1-\delta)\frac{logn}{I(p)}+\frac{2log\frac{1}{\delta}}{(1-2p)log\frac{1-p}{p}}\right)\)

_noisy comparisons in expectation._

_Proof._ First, if \(\delta>\frac{1}{logn}\), we output an arbitrary answer and halt with probability \(\delta-\frac{1}{logn}\). Otherwise, we call Theorem 10 with error probability \(\frac{1}{logn}\). By union bound, the overall error probability is at most \(\delta\). The expected number of noisy comparisons is

\(\left(1-\delta+\frac{1}{logn}\right)\cdot(1+o(1))\left(\frac{logn+O(loglogn)}{I(p)}\right)=(1+o(1))(1-\delta)\frac{logn}{I(p)}\)

as required. In the following, we assume \(\delta\le\frac{1}{logn}\). We also assume \(logn\ge 4\) for simplicity, as we could pad dummy elements.

Let _x_ be the element for which we need to find the predecessor. First, we use Theorem 10 with error probability \(\frac{1}{logn}\) to find a candidate predecessor, which takes \((1+o(1))\left(\frac{logn+O(loglogn)}{I(p)}\right)=(1+o(1))\cdot\frac{logn}{I(p)}\) time. Then we use Lemma 13 to compare _x_ with this candidate predecessor _l_ and with the next element of this candidate predecessor _r_, with error probability \(\delta/4\). This takes \((2+o_{4/\delta}(1))\cdot\frac{log(4/\delta)}{(1-2p)log((1-p)/p)}=(2+o(1))\cdot\frac{log(1/\delta)}{(1-2p)log((1-p)/p)}\) time. If the comparison results are _l\<x_ and _x\<r_, we return _l_ as the predecessor of _x_, otherwise, we restart. See Algorithm 4.

**Algorithm 4**

procedure NoisyBinarySearch\((n,A,x,\delta)\)<br>
   while true do<br>
   Use Theorem 10 with error probability \(\frac{1}{logn}\) to search the predecessor _l_ of _x_ in \(A\cup\{-\infty\}\).<br>
   \(r\leftarrow\) next element of _l_ in \(A\cup\{\infty\}\).<br>
   if LessThan\((l,x,\delta/4)\) and LessThan\((x,r,\delta/4)\) then return _l_.

Let P\[restart\] be the probability that we restart a new iteration of the while loop. Clearly, if the call to Theorem 10 and both calls to LessThan are correct, then we will not restart. Thus, \(\mathbb{P}[restart]\le\frac{1}{logn}+\frac{\delta}{2}\le\frac{2}{logn}\). Note that as \(logn\ge 4\), \(\mathbb{P}[restart]\le\frac{1}{2}\).

Let _P<sub>e</sub>_ be the probability that this algorithm returns the wrong predecessor. In each iteration of the while loop, the algorithm returns the wrong answer only if at least one of the two calls to LessThan are incorrect. Therefore, \(P_e\le\frac{\delta}{2}+\mathbb{P}[restart]P_e\), so \(P_e\le\frac{\delta/2}{1-\mathbb{P}[restart]}\le\delta\).

Let E\[_Q_\] be the expected number of queries that this algorithm makes. Since the call to Theorem 10 uses \((1+o(1))\left(\frac{logn+O(loglogn)}{I(p)}\right)\le(1+o(1))\frac{logn}{I(p)}\) noisy comparisons in expectation, and each call to LessThan uses \((1+o_{1/\delta}(1))\frac{log(4/\delta)}{(1-2p)log\frac{1-p}{p}}\le(1+o(1))\frac{log(1/\delta)}{(1-2p)log\frac{1-p}{p}}\) noisy comparisons<tbc>

