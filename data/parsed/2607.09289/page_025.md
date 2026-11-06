**Claim 3.5.** _Suppose that_ \(|\Phi|\ge p_\mathrm{max}\) _and_ \(p_\mathrm{max}=2^{\Theta(n)}\)_. Then, with constant probability, we have_ \(|\{a\mathrm{mod}p|a\in\Phi\}|\ge\Omega(p/n^2)\).

We follow the proof of \[25, Lemma 3.6\]. Let \(a_1,a_2\in\Phi\) be two distinct elements. Then \(a_1\equiv a_2(\mathrm{mod}p)\) holds if and only if _p_ divides |_a_<sub>1</sub>-_a_<sub>2</sub>|. By Lemma 2.3, we have \(|a_1-a_2|\le 2^{O(n)}\), and hence |_a_<sub>1</sub>-_a_<sub>2</sub>| has only _O(n_) distinct prime divisors. On the other hand, by Lemma A.1, for sufficiently large _n_, the interval \[_p_<sub>max</sub>,2_p_<sub>max</sub>\] contains at least \(\Omega\left(\frac{p_\mathrm{max}}{\mathrm{log}p_\mathrm{max}}\right)=\Omega\left(\frac{p_\mathrm{max}}{n}\right)\) primes, where we use \(p_\mathrm{max}=2^{\Theta(n)}\). Since _p_ is chosen uniformly at random from the primes in \[_p_<sub>max</sub>,2_p_<sub>max</sub>\], the collision probability for this fixed pair _a_<sub>1</sub>_,a_<sub>2</sub> is at most _O(n_<sup>2</sup>_/p_<sub>max</sub>).

Let<tbc>

\(q=\sum_{r=0}^{p-1}|\{a\in\Phi|a\equiv r(\mathrm{mod}p)\}|^2,\)

<tbc>which is the number of collisions, including trivial ones. By linearity of expectation and \(p_\mathrm{max}\le|\Phi|\), we have<tbc>

\(\mathbb{E}[q]\le O\left(|\Phi|+|\Phi|^2\cdot\frac{n^2}{p_\mathrm{max}}\right)\le O\left(\frac{(|\Phi|n)^2}{p_\mathrm{max}}\right).\)

<tbc>By Markov’s inequality, with constant probability, we have \(q\le O\left(\frac{(|\Phi|n)^2}{p_\mathrm{max}}\right)\). If this happens, then by the Cauchy-Schwarz inequality,

\(|\{a\mathrm{mod}p|a\in\Phi\}|\ge\frac{|\Phi|^2}{q}\ge\Omega(p_\mathrm{max}/n^2)=\Omega(p/n^2),\)

where the last follows from \(p_\mathrm{max}\le p\le 2p_\mathrm{max}\).

## B.2 Small-Space Generation of Modular Subset-Sum Lists

Input: Integer lists A and B, and modulus p<br>
Output: The multiset C={{(a+b)mod} \(p|a\in A,b\in B\}\) generated in ascending order<br>
Replace each element of A and B by its residue modulo p.<br>
Sort B in ascending order.<br>
Write A=\[a<sub>1</sub>,...,a<sub>m</sub>\] and B=\[b<sub>1</sub>,...,b<sub>n</sub>\].<br>
Initialize an array D=\[d<sub>1</sub>,...,d<sub>m</sub>\].<br>
Initialize a min-priority queue Q.<br>
for i=1,...,m do<br>
   Let d<sub>i</sub> be the smallest index j such that \(b_j\ge p-a_i\); if no such index exists, set d<sub>i</sub>=1.<br>
   Insert \(\left((a_i+b_{d_i})\mathrm{mod}p,i,0\right)\) into Q.<br>
while Q is not empty do<br>
   Extract \(\left(s,i,t\right)\) from Q.<br>
   Output s.<br>
   if t+1\<n then<br>
   Let \(j'=((d_i+t)\mathrm{mod}n)+1\).<br>
   Insert \(\left((a_i+b_{j^\prime})\mathrm{mod}p,i,t+1\right)\) into Q.

Lemma B.1 is used implicitly in the balanced 4-table algorithm of Schroeppel and Shamir \[29\].

**Algorithm 5:** ModuloSmallSpaceGenerator

