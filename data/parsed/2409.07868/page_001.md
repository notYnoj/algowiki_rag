# An Optimal Algorithm for Sorting Pattern-Avoiding Sequences

**Abstract**

We present a deterministic comparison-based algorithm that sorts sequences avoiding a fixed permutation \(\pi\) in linear time, even if \(\pi\) is a priori unkown. Moreover, the dependence of the multiplicative constant on the pattern \(\pi\) matches the information-theoretic lower bound. A crucial ingredient is an algorithm for performing efficient multi-way merge based on the Marcus- Tardos theorem. As a direct corollary, we obtain a linear-time algorithm for sorting permutations of bounded twin-width.

### 1 Introduction

The information-theoretic lower bound on sorting states that any comparison-based sorting algorithm must take \(\Omega(nlogn)\) time in the worst case for sorting inputs of length _n_, see [CLRS22]. Naturally, it invites the question about complexity of sorting restricted sets of inputs, and this problem has indeed been studied for decades. In this paper, we resolve the complexity of sorting input sequences restricted by avoiding a fixed permutation pattern.

We distinguish between arbitrary sequences and permutations that contain no repeated values. A sequence _S=s_<sub>1</sub>_,...,s<sub>n</sub> contains_ a permutation \(\pi=\pi_1,\dots,\pi_k\) if there are indices \(i_1<\cdots<i_k\) such that \(s_{i_j}<s_{i_\ell}\) if and only if \(\pi_j<\pi_\ell\) for all \(j,\ell\in[k]\). We say that the subsequence _s_<sub>_i_<sub>1</sub></sub>_,...,s<sub>ik</sub>_ of _S_ is _order-isomorphic_ to \(\pi\). Otherwise, _S_ avoids \(\pi\).

Lower bounds. A standard argument shows that any comparison-based algorithm for sorting a set of permutations \(\Gamma\), each of length _n_, must make at least \(\Omega(log|\Gamma|+n)\) comparisons in the worst case. Fredman [Fre76] showed that \(O(log|\Gamma|+n)\) comparisons suffice if we have complete knowledge of \(\Gamma\) and unrestricted computational power. Specifically, Fredman’s argument proves the existence of a decision tree of depth \(O(log|\Gamma|+n)\) that correctly sorts \(\Gamma\). In order to apply these bounds on pattern-avoiding sequences, it invites the natural question of how many pattern-avoiding permutations of given length are there. In fact, it has been a long-standing open problem in the world of pattern-avoiding permutations whether the number of \(\pi\)-avoiding permutations of length _n_ grows at most exponentially in _n_. This question, known as the _Stanley-Wilf conjecture_, was eventually

<sup>∗</sup>This work was co-funded by the European Union under the project Robotics and advanced industrial production (reg. no. CZ.02.01.01/00/22_008/0004590).

arXiv:2409.07868v1 [cs.DS] 12 Sep 2024

Michal Oppler<sup>∗</sup>

Czech Technical University in Prague, Czech Republic

