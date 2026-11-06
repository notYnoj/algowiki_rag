**Theorem 4.2.** _The_ Pigeonhole Modular Equal Subset Sum _problem can be solved in quantum time O_<sup>∗</sup>(3<sup>2_n/_7</sup>).

_Proof._ Replacing every _A_\[_i_\] by _A_\[_i_\] mod_q_ does not change the set of solutions, so we assume that \(0\le A[i]<q\) for all \(i\in[n]\).

A solution is equivalent to a nonzero vector \(\varepsilon\in\{-1,0,1\}^n\) satisfying<tbc>

\(\sum_{i\in[n]}\varepsilon[i]A[i]\equiv 0modq.\)

<tbc>As \(0\le A[i]<q\) for all _i_, the left-hand side lies in the interval (-_nq,nq_), so the congruence holds if and only if

\(\sum_{i\in[n]}\varepsilon[i]A[i]=cq\text{for some integer}c\text{with}|c|<n.\)

Partition \[_n_\] into seven blocks _B_<sub>1</sub>_,...,B_<sub>7</sub>, each of size at most \(\lceil n/7\rceil\). For each \(j\in[7]\), construct a list _L<sub>j</sub>_ indexed by vectors \(\varepsilon\in\{-1,0,1\}^{B_j}\), with \(L_j[\varepsilon]=\sum_{i\in B_j}\varepsilon[i]A[i]\). Each list has size at most \(M=3^{\lceil n/7\rceil}\). For a fixed _c_, finding a vector \(\varepsilon\in\{-1,0,1\}^n\) with \(\sum_{i\in[n]}\varepsilon[i]A[i]=cq\) is exactly a 7-SUM instance on the lists _L_<sub>1</sub>_,...,L_<sub>7</sub> with target _cq_.

For _c_=0, one may get the zero vector as an answer, so we need to force at least one coordinate of \(\varepsilon\) to be nonzero. For \(i\in[n]\), \(\sigma\in\{-1,1\}\), and an integer _c_ with |_c|\<n_, let _j(i_) denote the index of the block containing _i_, and let \(I_{i,\sigma,c}\) be the 7-SUM instance with target _cq_ obtained from _L_<sub>1</sub>_,...,L_<sub>7</sub> by restricting _L_<sub>_j(i_)</sub> to the indices \(\varepsilon\in\{-1,0,1\}^{B_{j(i)}}\) with \(\varepsilon[i]=\sigma\). Every solution of \(I_{i,\sigma,c}\) satisfies \(\varepsilon[i]=\sigma\) and is therefore a nonzero solution of the displayed congruence. By Theorem 1.2 with _k_=7, each of them is solved in time \(\widetilde{O}(M^2)\), so the total running time is

\(O(n^2)\cdot\widetilde{O}(M^2)=O^*(3^{2n/7}).\)

## Acknowledgments

The authors used ChatGPT to assist with verifying all proofs, identifying typos, and conducting the literature review. The authors assume responsibility for all content.

## References

