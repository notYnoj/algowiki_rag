## 5.1 Lower Bound

In this section, we prove our lower bound for Noisy Binary Search using techniques similar to our lower bound for Noisy Sorting.

**Theorem 3** (Noisy Binary Search Lower Bound)**.** _Any (deterministic or randomized) algorithm for_ NoisyBinarySearch(_n_) _with error probability_ \(\le\delta\) _must make at least_

\((1-o(1))\left((1-\delta)\frac{logn}{I(p)}+\frac{2log\frac{1}{\delta}}{(1-2p)log\frac{1-p}{p}}\right)\)

_noisy comparisons in expectation, even if the position of the element to search for is uniformly random._

We define the following intermediate problem:

**Definition 30** (OracleNoisyBinarySearch(_n_))**.** Given a sorted list _L_ of _n_ elements and an element _x_ that is unequal to any element in the list, a solver needs to output the predecessor of _x_ in _L_ by asking the following type of query OracleQuery(_x,y_) for \(y\in L\):

• If _y_ is the predecessor of _x_, output symbol _P_;<tbc>

• If _y_ is the successor of _x_, output symbol _S_;<tbc>

• Otherwise, output NoisyComparison(_x,y_).

**Lemma 31.** _Fix an algorithm_ A _for_ NoisyBinarySearch(_n_) _with error probability_ \(\delta\)_. Let L be the input list and x be the input element of_ NoisyBinarySearch(_n). Let_ \(U^\unknown\) _denote the number of noisy comparisons_ A _makes between x and elements that are not the predecessor or successor of x._

_Then there exists an algorithm for_ OracleNoisyBinarySearch(_n_) _with error probability at most_ \(\delta\) _which makes at most_ \(\mathbb{E}[U^\unknown]+1\) _queries in expectation._

_Proof._ The algorithm for OracleNoisyBinarySearch(_n_) simulates A as follows:

• Every time A attempts to make a NoisyComparison(_x,y_) between some _x_ and some element _y_ in _L_, the algorithm makes OracleQuery(_x,y_) instead. If OracleQuery(_x,y_) returns _P_ or _S_, we have found the predecessor of _x_, so we can return the predecessor and finish the execution; otherwise, we pass the result of OracleQuery(_x,y_) (which will be NoisyComparison(_x,y_)) to A.<tbc>

• If A returns a predecessor or _x_, then we also return the same predecessor, finishing the execution.

The error probability bound and number of queries easily follow.

**Lemma 32.** _Any (deterministic or randomized) algorithm for_ OracleNoisyBinarySearch(_n_) _with error probability_ \(\le\delta\) _makes at least_ \((1-\delta-o(1))\frac{logn}{I(p)}\) _queries in expectation, even if the position of the element to search for is uniformly random._

