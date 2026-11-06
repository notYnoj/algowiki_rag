\(c\cdot s'\) for some cost vector _c_. In LocalMax-_k_-SAT, \(s'\) in position _i_ has a 1 if the clause _C<sub>i</sub>_ is satisfied by _s_ and 0 else. The cost vector _c_ contains then the weight each clause. In both Flip and Polm, the value of a solution is just a bit string, interpreted as a binary number. Therefore, we have that \(s'\) is the bit string and _c<sub>i</sub>_=2_<sup>i</sup>_. We say they use a _lexicographic cost function_. This motivates the following problem:

\(\blacktriangleright\) **Search Problem 2** (LocalLexMax-_k_-SAT)**.** LocalLexMax-_k_-SAT _is_ LocalMax- _k_-SAT _where the clause C<sub>i</sub> has a weight of_ 2_<sup>i</sup>. Equivalently, we can view the problem as a FLIP instance with n input bits and m output bits where every output bit is computed by a single k-clause._

We are now ready to state our first main result:

\(\blacktriangleright\) **Theorem 3.** LocalLexMax-4-SAT _is PLS-complete, and so is_ Flip _with depth-1 circuits._

We will prove Theorem 3 in Section 4. Note that LocalLexMax-2-SAT can be solved polynomially; in fact, we can even compute a global maximum by the following greedy algorithm:

1. Set _G<sub>m</sub>_:=1, the empty CNF, always true. 2. For _i=m_-1_,...,_0: set \(G_i:=G_{i+1}\wedge Ci\) if this is satisfiable; otherwise, set _G<sub>i</sub>_:=_G_<sub>_i_+1</sub>. This algorithm works for all _k_-CNF formulas as long as the clause weights are lexicographic; it is efficient as long as we can check efficiently whether \(G_{i+1}\wedge Ci\) is satisfiable. Similarly, LocalMaxCut with lexicographic costs is in P.

One of the main ways to show the PLS-hardness of a problem _L_ is a reduction from FLIP using Krentel’s technique[15, 16] of simulating multiple circuits, one on the current input and some on (a subset of) its neighborhood and using a gadget to switch to the best neighbor. One must then use the machinery of _L_ to simulate how the circuits evaluate their inputs and how one switches from the current solution to a better neighbor. This is used in the proof of Theorem 3 as well as in [20, 6, 7, 19, 21, 8]. These proofs are often quite long and complicated.

LocalLexMax-4-SAT is a special case of Flip that is still PLS-complete and combines the simple cost function of Flip with the simple combinatorial structure of CNF formulas. We argue that for reductions showing PLS-completeness, LocalLexMax-4-SAT can often be a better starting point than Flip, leading to simpler proofs and stronger results. We demonstrate this in two cases:

\(\blacktriangleright\) **Theorem 4.** Permutation Orbit Local Minimum _is PLS-complete even when restricted to permutations_ \(\pi_1,\dots,\pi_k\) _that generate an Abelian group._

We prove Theorem 4 in Section 3; in fact, we prove that it stays PLS-complete even if we require that all permutations in \(\langle\pi_1,\dots,\pi_k\rangle\) have order 2. In Section C we prove that it stays PLS-complete even if we require the group \(\langle\pi_1,\dots,\pi_k\rangle\) to be cyclic. This answers an open question and strengthens the result from [20] as Abelian and cyclic groups allow less freedom for the permutations and also admit a potentially faster brute-force algorithm as \(\pi\circ\sigma=\sigma\circ\pi\).

Our final application of Theorem 3 comes from algorithmic game theory:

\(\blacktriangleright\) **Theorem 5.** _Finding an_ \(\alpha\)_-equilibrium for_ \(\alpha>1\) _in a congestion game is PLS-complete when all delay functions are step functions or all are exponential functions or all are polynomials with positive coefficients._

