We show that this definition is equivalent to the result differing from the "actual" _i_-th smallest element by at most _k_.

**Lemma 1.4.** _An item x<sub>j</sub> is a k-approximate i-selection if and only if_ \(|x_j-x_i|\le k\) _where x<sub>i</sub> is the actual i-th smallest element of X._

We proceed with our results. We begin in the non-parallel setting (although our algorithms still have good round guarantees). We provide the following near-optimal approximate sorting algorithm.

**Theorem 1.5.** _There exists a randomized algorithm that takes O(n_log<sup>2</sup>_n_) _comparisons, uses O_(log_n_) _parallel rounds, and returns a_ 4_-approximate sorting with probability_ \(>1-\frac{1}{n^2}\).

Since any approximate sorting algorithm must be able to correctly sort any list of numbers after scaling, such an algorithm must take \(\Omega(n\mathrm{log}n)\) comparisons by the well-known lower bound. Thus, this result is a log factor away from optimal. Note that no algorithm can give better than a 2-approximation, as the adversary can force 0_\>_1_\>_2_\>_0, which can make 0,1,2 indistinguishable \[AFJ<sup>+</sup>18\]. The best prior result is of \[AFJ<sup>+</sup>18\], where they show quicksort gives a 2-approximate sorting in _O(n_log_n_) expected comparisons against the non-adaptive adversary. This approach falls apart against the adaptive adversary, however, as if all values are the same, the adversary can force all pivots to compare less than all elements, forcing the algorithm to do \(\Omega(n^2)\) comparisons. Our result shows that it is possible to get a constant approximate sorting in near-optimal number of comparisons even against the adaptive adversary. Previously, this problem had also been studied in the deterministic case \[AFHN15\], where an upper bound of \(O(4^k\cdot n^{1+1/2^{k-1}})\) and a lower bound of \(\Omega(n^{1+1/2^{k-1}})\) comparisons were proven for _k_-approximate sorting. Taking this result with _k_=4, we get a lower bound of \(\Omega(n^{9/8})\) for 4-approximate deterministic sorting. Thus, our algorithm shows a distinction between randomized and deterministic algorithms in this problem. To get an \(\widetilde{O}(n)\) deterministic algorithm, one could at best provide a \(\Omega(\mathrm{loglog}n)\)-approximation.

Our algorithm uses the fact that randomized quicksort has good comparison complexity if there are not big groups of close elements, as the adversary cannot force the pivots too far away. Thus, if randomized quicksort does not work, there must be a large cluster of close elements that we can exploit. We then estimate the order of each element using a _O_(log_n_) size sample of items, using the existence of this cluster to guarantee our estimates are accurate. Finally, we use these approximate orders to find a partition of the input items, and recursively solve as in quicksort.

Our algorithm also implies a similar selection algorithm.

**Corollary 1.6.** _For any i, there exists a randomized algorithm that takes O(n_log_n_) _comparisons, uses O_(log_n_) _parallel rounds, and returns a_ 4_-approximate i-selection with probability_ \(>1-\frac{1}{n^2}\).

Similarly, this result is a log factor away from optimal. Again, the best prior result is of \[AFJ<sup>+</sup>18\], where their analysis also shows that quicksselect gives a 2-approximate selection in _O(n_) expected comparisons against the non-adaptive adversary. Against the adaptive adversary, this approach fails in an identical way to quicksort. Our result shows that it is possible to get a constant approximate selection in near-optimal number of comparisons even against the adaptive adversary. This was also studied in the deterministic setting \[AFHN15\], where an equivalent \(\Omega(n^{9/8})\) lower bound was shown, so we also show a distinction between randomized and deterministic in this case. Similarly, any \(\widetilde{O}(n)\) deterministic algorithm could at best return a \(\Omega(\mathrm{loglog}n)\)-approximation.

Our approach is identical to the sorting algorithm, except we only have to recursively solve on the relevant side of the partition, as in quicksselect.

Next, we provide a family of algorithms that explore the tradeoff between number of rounds, number of comparisons, and approximation factor in the sorting case.

