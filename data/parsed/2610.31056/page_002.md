<tbc>standard meet-in-the-middle algorithm solves the problem in O_<sup>⋆</sup>_(3<sup>_n/_2</sup>), which can be improved to O_<sup>⋆</sup>_(1.7067_<sup>n</sup>_) \[MNPW19\].<sup>1</sup>

Papadimitriou \[Pap94\] introduced the total variant called the _Pigeonhole Equal Subset Sum_ (PESS). In this variant, the sum of the numbers is less than 2_<sup>n</sup>_-1, and the goal remains to find distinct subsets \(A,B\subseteq S\) with equal sums. Since there are 2_<sup>n</sup>_-1 non-empty subsets but only 2_<sup>n</sup>_-2 possible nonzero sums, a collision must exist by the pigeonhole principle. PESS belongs to the class TFNP and, more specifically, to PPP, and it is conjectured to be PPP-complete \[Pap94\]. The setting, when the number of collisions is even larger, e.g., the sum of integers is bounded by 2<sup>_n_-1</sup>, is called _weak-pigeonhole regime_ and is also an important setting \[SZZ18\]. In that weaker setting, PESS belongs to the class PWPP (problems whose totality is proven through the weak pigeonhole principle) \[SZZ18\]. For convenience, we will consider the variants where each of the numbers is bounded by either (2_<sup>n</sup>_-1)_/n_ or 2<sup>_n_-1</sup>_/n_, so the sum remains bounded by 2_<sup>n</sup>_-1 or 2<sup>_n_-1</sup>. To this effect, we introduce a parameter _M_ that denotes the bound on the integers we allow in our instances.

To the best of our knowledge, the first explicit algorithm for PESS was given by Vasilakis \[Vas22\], who obtained an \(\widetilde{\mathcal{O}}(nM)\) time dynamic programming algorithm<sup>2</sup>. Allcock, Hamoudi, Joux, Klingelhöfer and Santha \[AHJ<sup>+</sup>22\] gave an O_<sup>⋆</sup>_(2<sup>_n/_2</sup>)-time algorithm when the sum of the numbers is less than 2_<sup>n</sup>_-1. Notice that by discarding the largest items until we reach a modified instance with \(n'\) items whose sum is in \([2^{n^\prime-1}-1,2^{n^\prime}-1)\) and then running the algorithm of Allcock et al. \[AHJ<sup>+</sup>22\], the overall running-time can be presented as O_<sup>⋆</sup>(M_<sup>1/2</sup>). Later, Jin and Wu \[JW24\] refined the meet-in-the-middle approach of \[AHJ<sup>+</sup>22\] and achieved O_<sup>⋆</sup>(M_<sup>0.4</sup>) running time. The current best algorithm by Jin, Williams, and Zhang (ESA 2025) runs in O_<sup>⋆</sup>(M_<sup>1/3</sup>) \[JWZ25\] (see  1 for an overview). At the end of their paper, Jin, Williams, and Zhang raised the question of whether the _M_<sup>1/3</sup> barrier can be improved \[JWZ25\].

**Open Question 1** (\[JWZ25\])**.** _Can we get a_ \(\mathrm{poly}(n)\cdot M^{1/3-\varepsilon}\)_-time algorithm for Pigeonhole Equal Subset Sum for some_ \(\varepsilon>0\)?

Note that PESS is a total problem and, as such, is not expected to be NP-hard. As noted above, it lies in PPP. Inspired by these questions, Jin \[Jin24\] asked whether subexponential-time algorithms for PESS are possible:

**Open Question 2** (\[Jin24, JW24\])**.** _Can we get a subexponential-time algorithm for Pigeonhole Equal Subset Sum?_

More specifically, Jin \[Jin24\] asked for 2<sup>_o(n_)</sup>-time algorithm, which in parameterization by maximum integer can be expressed as \(\mathrm{poly}(n)\cdot M^{o(1)}\).

## 1.1 Our Results

In this work, we make partial progress on both of these questions. First, we present a \(\mathrm{poly}(n)\cdot M^{o(1)}\) - time algorithm for PESS in the regime _M_=2<sup>_o(n_)</sup>.

**Theorem 1.1.** _There exists a deterministic algorithm that, given an integer n and a set_ \(S\subseteq\{1,\dots,M\}\) _of size n such that nM\<_2_<sup>n</sup>_-1_, runs in time_ \(\mathrm{poly}(n)\cdot M^{\widetilde{\mathcal{O}}(1/\mathrm{log}\delta)}\) _and returns two distinct subsets of S with the same sum, where_ \(\delta=\delta(n,M):=n/\mathrm{log}M\) _is the density of the instance._

_As a corollary, when M_=2<sup>_o(n_)</sup>_, the algorithm runs in time_ \(\mathrm{poly}(n)\cdot M^{o(1)}\).

<sup>1</sup>\(\mathcal{O}^\star(\cdot)\) and \(\widetilde{\mathcal{O}}(\cdot)\) hide polynomial and polylogarithmic factors in the input respectively. <sup>2</sup>More precisely, algorithm of Vasilakis \[Vas22\] runs in \(\mathcal{O}(n+\Sigma(S)\mathrm{log}(\Sigma(S)))\) time, where \(\Sigma(S)\) is the sum of the input integers.

