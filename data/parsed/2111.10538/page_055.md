By Chernoff bound, Step 14 to Step 22 of Algorithm 11 accepts on ps_<sub>j</sub>_ with probability at least \(1-\mathrm{exp}(-\Omega(\mathrm{log}^2n))\).

Consider the case of<tbc>

\(\mathrm{lis}^{[\ell,r]}(A)\le f\left(\frac{\lambda^4}{2^{32}}\right)\frac{\lambda^4}{2^{33}}n.\)

<tbc>Then for any pseudo-solution ps_<sub>j</sub>_, we have<tbc>

\(\mathfrak{q}(\mathfrak{ps}_j)\le f\left(\frac{\lambda^4}{2^{32}}\right)\frac{\lambda^4}{2^{33}}n.\)

<tbc>Let \(\beta\) denote the number of subarrays sa_<sub>i</sub>_ such that \(\mathrm{lis}^{[\ell_i,r_i]}(\mathfrak{sa}_i)\ge f(\lambda^4/2^{32})n/\zeta\) where \([\ell_i,r_i]\) is the interval for subarray sa_<sub>i</sub>_ in ps_<sub>j</sub>_. We have

\(\beta\le\frac{\mathfrak{q}(\mathfrak{ps}_j)}{f(\lambda^4/2^{32})n/\zeta}\le\frac{\lambda^4}{2^{33}}\zeta.\)

By Chernoff bound, Step 14 to Step 22 of Algorithm 11 do not accept on ps_<sub>j</sub>_ with probability at least \(1-\mathrm{exp}(-\Omega(\mathrm{log}^2n))\). By union bound, Algorithm 11 rejects with probability at least \(1-\mathrm{exp}(-\Omega(\mathrm{log}^2n))\).

Hence, Algorithm 11 is a \(\left(f\left(\frac{\lambda^4}{2^{32}}\right)\cdot\frac{\lambda^4}{2^{33}}\right)\)-approximate algorithm for LIS of length _n_ with success probability at least \(1-\mathrm{exp}(-\Omega(\mathrm{log}^2n))\).

Finally, we discuss the running time of Algorithm 11. By the definition of procedures ConstructCandidateDomains and ConstructPseudoSolutions, the running time of Step 5 to Step 9 of Algorithm 11 is \(O(\lambda^{-9}\zeta\mathrm{log}^{O(1)}n)\). By Lemma 6.3, \(t=O(\lambda^{-3})\), and by Chernoff bound with probability \(1-\mathrm{exp}(-\Omega(\mathrm{log}^2n))\) the size of _Q_ is at most \(O(\lambda^{-4}\mathrm{log}^4n)\). Hence, the running time of Step 12 to Step 24 of Algorithm 11 is \(O(\lambda^{-7}g(n/\zeta,\lambda^4/2^{32})\mathrm{log}^4n)\).

By definition, we have the following basic fact about approximate ratio.

**Fact 6.10.** _Let f and_ \(f'\) _be two functions mapping_ (0,1) _to_ (0,1) _such that_ \(f(\lambda)\ge f'(\lambda)\) _for any_ \(\lambda\in(0,1)\)_. If there is a_ \(f(\lambda)\)_-approximate LIS algorithm, then the algorithm is also_ \(f'(\lambda)\)_- approximate._

Now we present algorithm to approximate LIS using \(\widetilde{O}(n^\kappa\mathrm{poly}(\lambda^{-1}))\) space by applying the pseudo-solution construction-evaluation framework recursively. In particular, we use the same algorithm on subarrays as an oracle and apply Lemma 6.9 recursively to approximate the entire sequence with slightly worse approximation ratio (compared with approximation ratio of the oracle).

**Lemma 6.11.** _Let_ \(\kappa\) _be a constant of_ (0,1) _and_ \(\lambda\in(0,1)\)_. Algorithm 12 approximates LIS with approximation ratio_

\(\frac{\lambda^{2\cdot 4^{(\lceil 1/\kappa\rceil-1)}}}{256^{3\cdot 4^{(\lceil 1/\kappa\rceil-1)}}}\)

_and running time_ \(O(n^\kappa\cdot\lambda^{-4^{O(1/\kappa)}}\mathrm{log}^{O(1)}n)\) _and success probability_ \(1-\mathrm{exp}(-\Omega(\mathrm{log}^3n))\).

_Proof._ We first prove the correctness of the algorithm by induction. Without loss of generality, we assume \(1/\kappa\) is an integer.

For \(i\in\{2,3,\dots,1/\kappa\}\), denote<tbc>

\(h_i(\lambda)=\frac{\lambda^{2\cdot 4^{(i-1)}-4}}{256^{2\cdot 4^{(i-1)}+3\cdot 4^{(i-2)}-7}}.\)

