<tbc>strictly increasing common subsequence of length LCIS(_A,B_)+_K_. These two constructions achieve both alternatives in the maximum. \(\sqcap\sqcup\)

Choose _K_=min{_n,m_}+1. Since \(LCBS(A,B)\le min\{n,m\}\), the second alternative strictly dominates, and

\(LCBS(A\circ Z,B\circ Z)=LCIS(A,B)+K.\) (6)

The construction has linear size. Fresh symbols can be represented as tagged ordered symbols following the original alphabet. For integer inputs, a linear scan finds the maximum and the fresh symbols can be consecutive larger integers. Every optimal padded solution is increasing and contains all fresh symbols; otherwise a missing fresh symbol could be inserted. Removing the suffix therefore recovers an LCIS witness as well as its length. The construction adds exactly _K_ matches, since each new symbol occurs once in each input and matches no old symbol.

**Corollary 6.2.** Assuming SETH, LCBS on two length-_N_ integer sequences has no \(O(N^{2-\varepsilon})\) algorithm for any fixed \(\varepsilon>0\).

**Proof:**<br>
Given two length-_N_ LCIS inputs, take _K=N_+1. Each padded input has length 2_N_+1. A strongly subquadratic LCBS algorithm, followed by subtracting _K_, would solve LCIS in strongly subquadratic time, contradicting the lower bound of Duraj et al. \[1\]. \(\sqcap\sqcup\)

This is a worst-case, conditional statement for unrestricted inputs. It does not establish an unconditional quadratic lower bound, optimality of the logarithmic factors in Theorem 5.1, or hardness of every sparse regime. In particular, a bound depending on _M_ is consistent with the corollary because _M_ can be quadratic in _N_.

## 7. Reproducible implementation and experiments

The accompanying supplement contains new Python implementations of the dense scan and the compressed two-dimensional Fenwick algorithm. Both recover match-coordinate witnesses and include preprocessing and reconstruction in their measured runtime. A third routine uses immediate strict updates as a diagnostic. No third-party Python packages are needed to run the algorithms, tests, or benchmarks. The measurements below were generated specifically for this revision; they do not reuse timings from earlier drafts.

### 7.1. Independent correctness checks

An independent oracle enumerates all subsequences of the first input and tests their bitonicity and membership in the second input. Exhaustive testing covers all pairs of sequences of length zero through four over a three-symbol alphabet: 121<sup>2</sup>=14641 pairs. Another 1,000 seeded random pairs have lengths zero through eight and values from -3 through 4. For every pair, the tests compare the dense, batched sparse, and immediate sparse optimum lengths with the oracle, and check all reconstructed coordinates and values. They additionally compare every forward and backward endpoint

