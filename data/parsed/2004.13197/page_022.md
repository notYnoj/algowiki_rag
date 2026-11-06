<tbc>by algorithms that do not input the large elements too often (PLE-DFS) is smaller than algorithms that input large elements multiple times (e.g., PLE-BFS).

**Remark 2:** The upper and lower bounds on PLE(_S,L_) are tight for a wide range of parameters. Moreover, if the first and third terms in the complexity of sorting (Theorem 2) dominate the complexity of the associated PLE(_S,L_) problem, our sorting algorithms are tight.

**Remark 3:** We would like to draw the reader’s attention to the second terms in the lower and upper bounds of PLE(_S,L_):

\(\frac{k}{B}logS+\frac{L}{wB}logk\text{versus}klog_BS+\frac{L}{w}log_Bk\)

The gap appears because while our algorithm (the two-tree PLE-DFS) works on _B_-trees and gets a fanout of _B_ per I/O, our lower bound only forbids fanouts larger than 2_<sup>B</sup>_. One may wonder whether an upper bound of _B_ on the fan-out is possible, as is the case with almost all searching problems in external memory. Consider the perfectly interleaved case, i.e., _n_ short and long elements each, and _k=n_ (the "nuts and bolts" version)). We show that if _n_ is very large, _there is an algorithm that achieves a fanout of_ 2_<sup>B</sup>_! This algorithm does not exist for small _n_, but it nevertheless shows that obtaining an unconditional upper bound of a fanout of _B_ is not possible.

**Theorem 19.** _Consider the problem where k short elements are given sorted, k large elements each of size_ \(w\ge B\) _are given unsorted, and it is given that in the final sorted order the elements are perfectly interleaved. There exists_ \(k_0\in\mathbb{N}\) _such that for all input sizes k\>k_<sub>0</sub>_, there is an algorithm that after_ \(O\left(\frac{k}{B}log_{M/B}\frac{k}{B}\right)I/Os\) _in preprocessing outputs the sorted order in_ \(O\left(\frac{k}{B}logk+\frac{kw}{B}\right)\right)I/Os\).

_Proof._ We will assume that \(w\ge logM\). If not, then (_k_log_k)/B\>(kw/B_)log_<sub>M</sub>k_, and we already have an upper bound (the BFS algorithm in Section 6) that has complexity _O_((_kw/B_)log_<sub>M</sub>k_) I/Os. Also for simplicity, we will assume that _k_ and _B_ are powers of two.

Since we are looking for an upper bound of _O_((_k_log_k)/B+kw/B_), we need to achieve roughly a fan-out of 2_<sup>B</sup>_ per I/O. The basic idea is the following: assume there are _B_ large elements in memory, and their search spaces are \(S_1,\cdots S_B\). If an incoming short block has the medians of all the _S<sub>i</sub>_s, then the input of this short block reduces every _S<sub>i</sub>_ by a factor of 2, and we get the desired 2_<sup>B</sup>_ fan-out. Of course, for this to continue, we would need the appropriate short block (containing the medians of the new search spaces,<tbc>

