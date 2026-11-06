<tbc>shown to solve this problem in _O(n_log_n_) comparisons with high probability: Pick a random nut, compare to all bolts, find the matching bolt, and compare that bolt to all nuts. The problem is now partitioned into two subproblems with the match at the boundary; recurse. In a later work by Alon, Blum, Fiat, Kannan, Naor, Ostrovsky \[1\] the authors developed a sophisticated deterministic algorithm in _O(n_ polylog_n_) time, which was then improved to an optimal _O(n_log_n_) by Komlós, Ma, Szémeredi \[10\]. Algorithms for nuts-and-bolts problem cannot be used for bichromatic sorting because of the lack of matches.

A preliminary version of this paper \[6\], that includes some further results, is published on arxiv.org.

### 1.2 Our Results

Let us consider bichromatic sorting with two sets _R_ (Red) of size _n_ and _B_ (Blue) of size _m_, and normalize the cost of _R-B_ comparisons to be 1. Let _N=n+m_ denote the total size of the two sets. Let \(\alpha\) and \(\beta\) denote the cost of _R-R_ and _B-B_ comparisons. Observe that if \(\alpha<1<\beta\) or \(\beta<1<\alpha\), then this can be solved as a monotonic structured cost \[7\]. The case when \(\alpha<1\) and \(\beta<1\) is discussed in Appendix A. Thus, the \(\alpha>1\) and \(\beta>1\) version posed in \[4\], where bichromatic comparisons are the cheapest, is the most interesting variant of bichromatic sorting, and our focus here. Surprisingly, no results are known for it, even though this is just "one step up" from unit-cost sorting! We show

**Theorem 1** (Polylog Competitiveness of InversionSort)**.** _There exists an algorithm InversionSort for bichromatic sorting and a constant c\>_0_, such that for every instance_ I_, the cost of InversionSort on_ I_, with probability at least_ 1-1_/N, is at most c_(log_N_)<sup>3</sup>_H_<sub>I</sub>_, where H_<sub>I</sub> _is the cost of the Hamiltonian._

Clearly, the \(\Omega(logN)\) lower bound on the competitive ratio carries over from unit-cost sorting. The above result shows that bichromatic sorting is almost as easy as the unit-cost setting. We remark that unlike most algorithms for generalized sorting (costs in \(\{1,\infty\}\)) that have a high polynomial runtime, InversionSort runs in _O(N_<sup>2</sup>) time. Further, we sketch (Appendix A) how InversionSort can be extended to the multichromatic-cost setting too. This result opens up the search for other, more complex variants that also admit polylog competitive ratios.

**Future Directions:** We believe that the _O_(log<sup>3</sup>_N_) competitive ratio of InversionSort can likely be reduced to an optimal _O_(log_N_). While InversionSort is randomized, it would also be very interesting to construct a deterministic algorithm for bichromatic sorting with similar guarantees. As we mention, bichromatic sorting generalizes the nuts-and-bolts problem, for which considerable effort was required \[1, 10\] to match the simple randomized _O(N_log_N_) run time by a deterministic algorithm. We believe that due to the absence of matches, there are interesting obstacles in this direction.

**Roadmap:** In Section 2 we describe InversionSort. Section 3 sketches the proof of the guarantee presented in Theorem 1. Finally, Section 4 gives the detailed analysis. Due to space constraints some proofs are moved to the appendix.

## 2 InversionSort: Definition

We first start by describing the setup of InversionSort. The design principle behind InversionSort is to focus on identifying the monochromatic stretches of the Hamiltonian called _stripes_. Intuitively, InversionSort operates like a variant of Quicksort, where the control flow is BFS-like instead of<tbc>

