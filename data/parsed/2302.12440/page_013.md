_3._ _Given_ \(\delta=O(\frac{1}{n^3})\)_, there exists a randomized algorithm_ SafeWeakSort _for_ NoisySorting(_n), with error probability_ \(\le\delta\)_, with the number of queries_ \(\tau\) _satisfying_<tbc>

<tbc>\(\mathbb{E}[\tau]=O(n\mathrm{log}n)+(1+o(1))\frac{n\mathrm{log}\frac{1}{\delta}}{(1-2p)\mathrm{log}\frac{1-p}{p}},\mathrm{Var}[\tau]=O(n^3\mathrm{log}^3\frac{1}{\delta}).\)<tbc>

<tbc>_and with the number of used random bits r satisfying_

<tbc>\(\mathbb{E}[r]=O(n\mathrm{log}n),\mathrm{Var}[r]=O(n^2\mathrm{log}^2n).\)

_Proof._ Apply Lemma 18 to Theorem 10, Lemma 13, and Lemma 17 respectively.

We introduce our last subroutine below, which is used to sort a subset of \(\Theta(\frac{n}{\mathrm{log}n})\) elements in the main algorithm.

**Lemma 20.** _There exists a randomized algorithm_ SafeSimpleSort _for_ NoisySorting(_n_) _with error probability o_(1) _which always uses O(n_log_n_) _queries and O(n_log_n_) _random bits always._

_Proof._ Consider the following algorithm A:

• Keep an array of the first _i_ elements for _i_ from 1 to _n_. Each time a new element needs to be inserted, the algorithm uses SafeBinarySearch to find the correct position, with error probability \(\frac{1}{n\mathrm{log}n}\).<tbc>

• Output the resulting array.

We have (_n_-1) calls to SafeBinarySearch. Let _E<sub>i</sub>_ be the event that the _i_-th call to SafeBinarySearch returns the correct value, and let _E_ be the event that all _E<sub>i</sub>_ happens. By union bound, probability of error \(\mathbb{P}[\neg E]\) is at most \((n-1)\cdot\frac{1}{n\mathrm{log}n}=o(1)\).

Let \(\tau_i\) be the number of queries used in the _i_-th call to SafeBinarySearch. By Corollary 19 Part 1, we have<tbc>

\(\mathbb{E}[\tau_i|E]=\mathbb{E}\left[\tau_i|\wedge_{1\le j\le i}E_j\right]\le\frac{\mathbb{E}\left[\tau_i|\wedge_{1\le j<i}E_j\right]}{\mathbb{P}\left[E_i|\wedge_{1\le j<i}E_j\right]}=O(\mathrm{log}n),\)

<tbc>and<tbc>

\(\mathrm{Var}[\tau_i|E]=\mathrm{Var}\left[\tau_i|\wedge_{1\le j\le i}E_j\right]\le\mathbb{E}\left[\tau_i^2|\wedge_{1\le j\le i}E_j\right]\le\frac{\mathbb{E}\left[\tau_i^2|\wedge_{1\le j<i}E_j\right]}{\mathbb{P}\left[E_i|\wedge_{1\le j<i}E_j\right]}\)<br>
\(\le O\left(\mathrm{Var}\left[\tau_i|\wedge_{1\le j<i}E_j\right]+\mathbb{E}\left[\tau_i|\wedge_{1\le j<i}E_j\right]^2\right)=O(\mathrm{log}^3n).\)

<tbc>Conditioned on _E_, \(\tau_i\)’s are independent because they use disjoint source of randomness. Thus, by Chebyshev’s inequality,

\(\mathbb{P}\left[\sum_{i\in[n-1]}\tau_i\ge\sum_{i\in[n-1]}\mathbb{E}[\tau_i]+n^{2/3}|E\right]\le O\left(\frac{n\mathrm{log}^3n}{\left(n^{2/3}\right)^2}\right)=o(1).\)

