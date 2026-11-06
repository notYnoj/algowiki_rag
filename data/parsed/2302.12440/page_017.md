**Line 17.** We have a few calls to SafeWeakSort where every input length is at most 6log<sup>2</sup>_n_, and total input length is at most _n_. By Corollary 19 Part 3,<tbc>

\(\mathbb{E}[\text{number of queries}]=(1+o(1))\frac{nlogn}{(1-2p)log\frac{1-p}{p}}.\)

<tbc>By Corollary 19 Part 3 and Chebyshev’s inequality,<tbc>

\(\mathbb{P}[\text{number of queries}>\mathbb{E}[\text{number of queries}]+n^{2/3}]=o(1).\)

<tbc>**Line 20, 27.** Conditioned on _E_<sub>1</sub>, _E_<sub>3</sub>, _E_<sub>4</sub>, the number of calls to SafeLessThan is<tbc>

\(O(|S|)+O(\text{number of elements in the wrong bucket})=O(\frac{n}{logn}).\)

<tbc>By Corollary 19 Part 2,<tbc>

\(\mathbb{E}[\text{number of queries}]=O(n).\)

<tbc>By Corollary 19 Part 2 and Chebyshev’s inequality,<tbc>

\(\mathbb{P}[\text{number of queries}>\mathbb{E}[\text{number of queries}]+n^{2/3}]=o(1).\)

<tbc>**Line 34.** Conditioned on _E_<sub>5</sub>, the number of calls to SafeBinarySearch is \(O(\frac{n}{logn})\). By Corollary 19 Part 1,<tbc>

\(\mathbb{E}[\text{number of queries}]=O(n)\)

<tbc>By Corollary 19 Part 1 and Chebyshev’s inequality,<tbc>

\(\mathbb{P}[\text{number of queries}>\mathbb{E}[\text{number of queries}]+n^{2/3}]=o(1).\)

<tbc>Summarizing the above, excluding events with _o_(1) probability in total, the total number of queries made is

\(O(n)+(1+o(1))\frac{nlogn}{I(p)}+(1+o(1))\frac{nlogn}{(1-2p)log\frac{1-p}{p}}+O(n)+O(n)+O(n^{2/3})\)<br>
\(=(1+o(1))\left(\frac{nlogn}{I(p)}+\frac{nlogn}{(1-2p)log\frac{1-p}{p}}\right).\)

Finally, we analyze the expected number of random bits used by the algorithm.

**Lemma 24.** _Algorithm 3 uses O(n_) _random bits in expectation._

_Proof._ We consider all the places Algorithm 3 uses randomness.

**Line 4.** Any biased random bits can be simulated by _O_(1) random bits in expectation \[KY76\], so Line 4 uses _O(n_) random bits in expectation.

