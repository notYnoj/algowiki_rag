_Proof._ For any continuous segment of length _L_ in the sorted order of _A_, the probability that none of these element is in _S_ is \((1-1/logn)^L\le exp(-L/logn)\). By union bound, the probability that there exists _L_ continuous elements not in _S_ is at most _n_exp(-_L/logn_). Taking \(L=2log_en\cdot logn\le 3log^2n\), we see that with probability \(\ge 1-\frac{1}{n}\), all continuous segments of length _L_ have at least one element in _S_, which implies all buckets have size \(\le 3log^2n\).

**Lemma 23.** _With probability_ 1-_o_(1)_, Algorithm 3 uses at most_ \((1+o(1))\left(\frac{1}{I(p)}+\frac{1}{(1-2p)log\frac{1-L}{p}}\right)nlogn\) _queries._

_Proof._ Because erring only makes the algorithm exit earlier, in the analysis we ignore the effect of erring caused by insufficient random bits. We define the following events:

• Let _E_<sub>1</sub> be the event that \(|S|\le\frac{n}{logn}+n^{2/3}=(1+o(1))\frac{n}{logn}\). By Chernoff bound, P\[_E_<sub>1</sub>\]=1-_o_(1).<tbc>

• Let _E_<sub>2</sub> be the event that all buckets have size at most 3log<sup>2</sup>_n_. By Lemma 22, P\[_E_<sub>2</sub>\]=1-_o_(1).<tbc>

• Let _E_<sub>3</sub> be the event that at most \(\frac{n}{logn}+n^{2/3}=(1+o(1))\frac{n}{logn}\) elements _a_ have the wrong predecessor \(\hat{l}_a\) at Line 7. By Chebyshev’s inequality, P\[_E_<sub>3</sub>\]=1-_o_(1).<tbc>

• Let _E_<sub>4</sub> be the event that all calls to SafeLessThan on Line 20, 27 return the correct values. Because there are at most 2_n_ calls, by union bound, P\[_E_<sub>4</sub>\]=1-_o_(1).<tbc>

• Let _E_<sub>5</sub> be the event that \(|X|\le O(\frac{n}{logn})\). If _E_<sub>2</sub>, _E_<sub>3</sub>, and _E_<sub>4</sub> all happen, then _E_<sub>5</sub> happens, for the following reasons. First, at Line 15, _B<sub>l</sub>_ has size greater than 6log<sup>2</sup>_n_, while the sizes of all buckets are at most 3log<sup>2</sup>_n_ conditioned on _E_<sub>2</sub>. Thus, at least half of the elements in _B<sub>l</sub>_ have the wrong predecessor \(\hat{l}_a\) at Line 7. Thus, the amount of elements added to _X_ at Line 15 is at most twice the number of elements _a_ with the wrong predecessor \(\hat{l}_a\), which is bounded by \(O(\frac{n}{logn})\) conditioned on _E_<sub>3</sub>. Also, if an element _x_ is added to _X_ at Line 22 or 29 and _E_<sub>4</sub> happens, _x_ must also have the wrong predecessor. Thus, overall, \(|X|\le O(\frac{n}{logn})\) if _E_<sub>2</sub>, _E_<sub>3</sub>, and _E_<sub>4</sub> all happen.

We make queries in the following lines: Line 5, 7, 17, 20, 27, 34. Let us consider them separately.

**Line 5.** By Lemma 20, conditioned on _E_<sub>1</sub>, with probability 1-_o_(1), Line 5 uses _O(n_) queries.

**Line 7.** We have at most _n_ calls to SafeBinarySearch whose number of queries are independent. By Corollary 19 Part 1,<tbc>

\(\mathbb{E}[\text{number of queries}]=(1+o(1))\frac{nlogn}{I(p)}.\)

<tbc>By Corollary 19 Part 1 and Chebyshev’s inequality,

\(\mathbb{P}[\text{number of queries}>\mathbb{E}[\text{number of queries}]+n^{2/3}]=o(1).\)

