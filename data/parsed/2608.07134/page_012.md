elements of \(X\cup\mathcal{D}(\varnothing,\mathcal{S})\). This is precisely the set \(\Delta\) returned by \(\hat{H}\) during synchronization. At the same time, Lemma 2.3 implies that this set is D(_X,_S). Therefore, \(\Delta=\mathcal{D}(X,\mathcal{S})\), as claimed.

**Time complexity.** Processing the block S takes \(\mathcal{O}(|\mathcal{S}|+\delta log(n/\delta))\) time, where _n_ is the total number of operations. (Here, \(\delta log(n/\delta)=0\) if \(\delta=0.\)) In total, the algorithm takes

\(\mathcal{O}\big(n+\sum_{i=1}^k\delta_ilog(n/\delta_i)\big)\) (1)

time, where \(\delta_i\) is the number of successful deletions between observations _i_-1 and _i_. We omit terms for which \(\delta_i=0\) and rewrite

\(n+\sum_{i=1}^k\delta_ilog(n/\delta_i)\le 2n+\sum_{i=1}^k\delta_ilog_2(n/\delta_i)=2n+2\sum_{i=1}^k\delta_ilog_2i+\sum_{i=1}^k\delta_ilog_2(n/(i^2\delta_i))\)<br> \(\le 2n+2\sum_{i=1}^k\delta_ilog_2i+\sum_{i=1}^kn/i^2.\)

Because \(\sum_{i=1}^k1/i^2=\mathcal{O}(1)\), we conclude the proof of the time complexity bound. Each of the _n_ operations is charged with O(1), and each deletion between observations _i_-1 and _i_ is additionally charged O(log_i_).

The time complexity of Theorem 3.1 is optimal due to an information-theoretic lower bound. The lower bound holds even without `reveal-deletions` operations. If all insertions happen before the first `delete-min`, the problem becomes the _multiple selection problem_: given an array of size _N_, compute the elements of (zero-based) ranks _p_<sub>1</sub>_,p_<sub>2</sub>_,...,p<sub>k</sub>_, where _p<sub>i</sub>_ is the number of (silent) `delete-min` operations before the _i_-th `find-min` query. It is known [DM81, Theorem 1] that solving the multiple selection problem requires

\(\Omega\left(N+\sum_{i=1}^k(p_i-p_{i-1})log\left(\frac{N}{p_i-p_{i-1}}\right)\right)\)

comparisons, where _p_<sub>0</sub>=-1. Informally, Dobkin and Munro show [DM81, Theorem 1] that computing elements of ranks _p_<sub>1</sub>_,p_<sub>2</sub>_,...,p<sub>k</sub>_ is sufficient to break the array elements into _k_+1 subarrays according to the gaps between the ranks. Sorting the whole array can now be reduced to sorting each individual subarray in \(\mathcal{O}(\sum_{i=1}^{k+1}(p_i-p_{i-1})log(p_i-p_{i-1}))\) total time, where _p_<sub>_k_+1</sub>=_N_. Hence, the sorting lower bound \(\Omega(NlogN)\) implies the multiple selection lower bound. This bound exactly matches the time complexity of our algorithm (1) up to a constant factor. In the worst case, when all ranks _p_ are evenly spaced, we recover the \(\Omega(Nlogk)\) lower bound.

**Acknowledgements.** All scientific ideas and results in this paper were developed by the authors, who also wrote the entire manuscript, including the complete initial draft. After this human-authored draft was completed, large language models were used to suggest ways to simplify the presentation of some proofs in §2. They were subsequently used to flag minor errors and to suggest improvements in wording. The authors independently evaluated each suggestion and decided whether and how to incorporate it. The authors take full responsibility for the content of the paper.

