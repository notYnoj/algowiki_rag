<tbc>distribution-based sorting algorithm. It employs heuristic, type-aware analysis of key characteristics and bucket sizes to dynamically select between Radixsort, and _std::sort_, enabling high performance across a wide range of data distributions \[24\].  I provides the comparative study of existing algorithms across different aspects.

## III. Proposed Work

The proposed algorithm follows a distribution-based sorting paradigm in which the input problem set _S_={_s_<sub>1</sub>_,s_<sub>2</sub>_,...,s<sub>n</sub>_} is divided into _k_ disjoint clusters. Each element \(s_i\in S\) is deterministically assigned to exactly one cluster _C<sub>j</sub>_, where \(j\in\{0,1,2,\dots,k-1\}\), according to a predefined mapping function. This yields a collection of mutually exclusive subsets _C_<sub>0</sub>_,C_<sub>1</sub>_,...,C_<sub>_k_-1</sub> satisfying \(C_p\cap C_q=\emptyset\) for \(p\neq q\) and \(\bigcup_{j=0}^{k-1}C_j=S\).

The partitioning strategy enforces the ordering invariant max(_C<sub>j</sub>)\<_min(_C_<sub>_j_+1</sub>) for all adjacent clusters, thereby guaranteeing that the clusters are totally ordered and independent. As a result, the partitioning phase produces a partially ordered structure, after which each cluster _C<sub>j</sub>_ can be treated as an independent subproblem and processed recursively using the same strategy. The distribution of elements into their respective clusters is governed by a deterministic mapping function, denoted as _h(s<sub>i</sub>_). This function takes an element \(s_i\in S\) as input and maps it to an integer index \(j\in\{0,1,\dots,k-1\}\), thereby assigning _s<sub>i</sub>_ to the corresponding cluster _C<sub>j</sub>_ based on its normalized position within the data distribution. The mapping function _h_ is inspired by the z-score transformation, also known as standard scaling. The objective of this transformation is to normalize datasets with heterogeneous value ranges onto a common scale while preserving the relative ordering of elements. By maintaining order, the transformation ensures that the partitioning invariant established in the previous stage remains valid.

Each element \(s_i\in S\) is first standardized using the z- score transformation, defined as

\(z_i=\frac{s_i-\mu}{\sigma},i=1,2,\dots,n,\)

where \(\mu\) and \(\sigma\) denote the mean and standard deviation of the dataset, respectively. This transformation consists of two steps: centering and scaling. In the centering step, the mean \(\mu\) is subtracted from each data point, shifting the distribution so that its new mean is zero. In the subsequent scaling step, the centered values are divided by the standard deviation \(\sigma\), normalizing the dispersion<tbc>

<tbc>of the data such that the resulting distribution has unit variance.

After computing the z-scores for each element _s<sub>i</sub>_, the transformed values _z<sub>i</sub>_ may be either positive or negative. To shift the entire set into the nonnegative domain, we identify the minimum transformed value _z_<sub>min</sub> and add its absolute value to every element. This translation preserves the relative ordering of elements while ensuring all transformed values are nonnegative. Under the assumption of an approximately normal distribution, nearly 95% of data points fall within the interval \[-2,2\] in z-score space. Without further refinement, this range would yield only a small number of distinct clusters. To increase the granularity of partitioning, a scaling factor is applied, effectively subdividing the transformed range into a larger number of buckets. After shifting and scaling, each value is floored to obtain an integer index _j_, which constitutes the final output of the mapping function _h_. The mapping function can be formally expressed as

\(h(s_i)=\left(\frac{s_i-\mu}{\sigma}+z_\mathrm{min}\right)\cdot\mathrm{scale}\) (1)

where \(\mu\) and \(\sigma\) denote the mean and standard deviation of the input set, _z_<sub>min</sub> is the minimum z-score observed after standardization, and scale is a user-defined parameter that controls the number of clusters.

Using this mapping, each cluster _C<sub>j</sub>_ is defined as

\(C_j=\left\{s_i\in S\big|\mathrm{min}\big(\lfloor h(s_i)\rfloor,k-1\big)=j\right\},j=0,1,\dots,k-1\)

The \(\mathrm{min}(\cdot)\) operation ensures that all mapped values are clipped to the valid cluster index range. The fundamental working of mapping and sorting process based on equation 1 is shown in Figure 1. For the sample example, the number of clusters (_k_) and _scale_ are considered to be 4 and 1 respectively. Also, the minimum problem size is considered as 1. The selection of _k_ is extremely important as it directly affects memory utilization and depth of the recursion tree, A heuristic approach is opted with \(k=\sqrt{n}\), where _n_ denotes the size of the original problem set. Importantly, the value of _k_ is kept constant across all recursive invocations. This design choice fixes the recursion depth to two levels, since recursively partitioning a set of size _n_ into \(\sqrt{n}\) clusters yields subproblems of size \(\sqrt{n}\), which are resolved in the subsequent level. This approach is preferred over a single-level partitioning strategy with _k=n_, which is highly sensitive to skewed or non-uniform data distributions and may result in severe load imbalance across clusters. By maintaining a bounded recursion depth and uniform cluster sizes, the proposed strategy improves robustness and performance stability.

The proposed algorithm is inherently stable. Stability is guaranteed by processing elements strictly in their original input order and by avoiding any operations that could invert the relative ordering of equal keys. Consequently, for any two elements _s<sub>i</sub>_ and _s<sub>j</sub>_ with identical keys, where _i\<j_ in the input, their relative order is preserved in the final output. Furthermore, the algorithm’s performance is invariant to the input permutation. Its core computations<tbc>

\begin{tabular}{ccccccc}
Algorithm & Worst-Case & Locality & Aux Space & Stability & Adaptivity & Parallel \\
 & Time & & & & & \\
Timsort & _O(nlogn_) & High & _O(n_) & Yes & High & Low \\
_std::stable\_sort_ & _O(nlogn_) & Medium & _O(n_) & Yes & Low & Low \\
_std::flat\_stable\_sort_ & _O(n_log_n_) & Medium & _O(n_) & Yes & Medium & Low \\
Spinsort & _O(n_log_n_) & High & _O(n/_2) & Yes & Medium & Low \\
_std::sort_ & _O(nlogn_) & High & _O(logn_) & No & Low & Medium \\
Pdqsort & _O(n_log_n_) & V. High & _O(logn_) & No & High & Medium \\
Skasort & _O(n_) & High & _O(k_) & No & Medium & Medium \\
Spreadsort & _O(n_log_n_) & High & _O(k_) & No & High & Medium \\
LSD Radix & \(O(n\cdot w/b)\) & Low & _O(n+k_) & Yes & None & High \\
\end{tabular}

TABLE I

Comparative Study of Existing Algorithms

