{0,1_,...,_2_<sup>n</sup>_-2} due to the promise, the pigeonhole principle guarantees that there exists a pair of subsets with the same subset sum.

Pigeonhole Equal Sums was introduced by Papadimitriou [20] as a natural example problem in the total search complexity class PPP. This problem has received attention in the TFNP literature [5, 21], and is conjectured to be PPP-complete [20].

From the algorithmic point of view, the current status of Pigeonhole Equal Sums is quite similar to that of the Subset Sum problem: a simple binary search with meet-in-middle solves Pigeonhole Equal Sums in _O_<sup>∗</sup>(2_<sup>n/_2)</sup> time (see Section 2).<sup>1</sup> Allcock, Hamoudi, Joux, Klingelhöfer, and Santha [1, Theorem 6.2] gave another _O_<sup>∗</sup>(2_<sup>n/_2)-time algorithm based on dynamic programming (which is analogous to the alternative _O_<sup>∗</sup>(2_<sup>n/_2)-time Subset Sum algorithm from [3]<sup>2</sup>). It remains open whether \(O(2^{(1/2-\varepsilon)n})\) time is possible for Pigeonhole Equal Sums. Improvement of such type was achieved for the Equal Sums problem (without the pigeonhole promise) by Mucha, Nederlof, Pawlewicz, and Węgrzycki [17] via the representation method with \(O(3^{(1/2-\varepsilon)n})\) run time for some \(\varepsilon>0.01\), but this result has no direct implications for Pigeonhole Equal Sums (for which the known _O_<sup>∗</sup>(2_<sup>n/_2) time bound is already much better than _O_(3_<sup>n/_2</sup>)).

### 1.1 Our results

We give an algorithm that solves Pigeonhole Equal Sums faster than the previous _O_<sup>∗</sup>(2_<sup>n/_2) running time [1].

\(\blacktriangleright\) **Theorem 1 (Main).** _Pigeonhole Equal Sums can be solved by a randomized algorithm in O_<sup>∗</sup>(2<sup>0.4_n_</sup>) _time._

Surprisingly, unlike previous works on other variants of Subset Sum, our algorithm does not use the representation method [15] or tools from coding theory [3, 4, 22]. Instead, our main insight is a simple structural characterization of Pigeonhole Equal Sums instances with few solutions.

Our techniques also yield a fast polynomial-space algorithm for Pigeonhole Equal Sums, in an analogous way to the previous \(O(3^{(1-\varepsilon)n})\)-time polynomial-space algorithm for Equal Sums [17].

\(\blacktriangleright\) **Theorem 2.** _Pigeonhole Equal Sums can be solved by a randomized algorithm in O_<sup>∗</sup>(2<sup>0.75_n_</sup>) _time and_ poly(_n_) _space._

For comparison, a straightforward algorithm based on binary search solves Pigeonhole Equal Sums in poly(_n_) space and _O_<sup>∗</sup>(2_<sup>n</sup>_) time (see the beginning of Section 4).

Theorem 1 and Theorem 2 will be proved in Section 3 and Section 4 respectively.

## 2 Preliminaries

Denote [_n_]={1_,...,n_}. Let \(O^*(\cdot),\Omega^*(\cdot)\) hide poly(_n_) factors, where _n_ is the number of input integers in the Pigeonhole Equal Sums problem.

Denote \(w(A)=\sum_{i\in A}w_i\) for \(A\subseteq[n]\). The pigeonhole promise states _w_([_n_])_\<_2_<sup>n</sup>_-1.

For a predicate _p_ we define **1**[_p_]=1 if _p_ is true and **1**[_p_]=0 if _p_ is false.

We need the following well-known lemma.

<sup>1</sup> We use \(O^*(\cdot)\) to hide poly(_n_) factors.

