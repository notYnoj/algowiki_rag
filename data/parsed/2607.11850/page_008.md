<tbc>divides the current value interval into 2000 buckets, even a strongly concentrated mixture requires only a few recursive levels in expectation.

The results are summarized in  1. These examples show that, for broad classes of common distributions, the expected recursion depth can remain very small even for large inputs. The reason is that each level divides the value range into a large number of buckets. Unless the input density is extremely concentrated, the number of elements in the bucket containing a typical element decreases rapidly with depth. This helps explain why recursive distribution sorting can behave close to linearly in practice on many numeric inputs.

### 4.4 Adversarial Inputs

The inputs most likely to be adversarial for NFS Sort are those that cause equal-width bucket refinement to make little progress. Since buckets are chosen according to value intervals rather than ranks, the algorithm performs best when the input values are reasonably spread across the current range. It can be challenged when many elements occupy a very small portion of that range.

However, these cases generally need to be quite extreme. As the examples in Section 4.3 show, even substantially non-uniform distributions can still lead to very small expected recursion depths. For instance, the clustered mixture distribution summarized in  1 places most of its probability mass in a narrow interval, yet the expected-depth bound remains small because each recursive step divides the value range into many buckets.

A more adversarial pattern consists of a large dense cluster together with a small number of extreme outliers. For example, an array in which almost all values lie in a very narrow interval, but a few values are near the minimum and maximum of the numeric range, can cause the initial bucket widths to be much larger than the dense region. As a result, almost all elements may be assigned to a single bucket, producing little reduction in subproblem size.

Another difficult case is a recursively clustered distribution. In such an input, the largest bucket at one level again contains values concentrated in a small subinterval of its analytical bounds. This can cause several consecutive recursive calls to isolate only a few elements while leaving most of the array inside one dominant bucket.

Inputs with many nearly equal floating-point values can have a similar effect, especially when a few distant values enlarge the observed range. Although the values are not identical, their numerical spread may be small compared with the current interval, so they repeatedly fall into the same bucket.

These adversarial inputs are not necessarily ordered in a special way in memory. Their difficulty comes primarily from the geometry of the value distribution: large gaps, extreme outliers, very dense clusters, or nested clusters can make equal-width value partitioning poorly balanced. In practice, this means that an input must be highly concentrated relative to its surrounding value range, often over multiple recursive levels, before it becomes genuinely adversarial. Mild or even high skew is not enough by itself; the problematic cases are extreme distributions in which almost all elements remain concentrated inside a tiny part of the current value interval over multiple recursive levels.

### 5 Experiments

In this section, we test NFSS against several popular state-of-the- art sorting algorithms on both synthetic and real-world datasets. For contending algorithms, we selected both a learned sorting algorithm, _Balanced Learned Sort_ (BLS) [3], and plain, non-learned sorting algorithms: _Boost Spreadsort, In-place Parallel Super Scalar Samplesort_ (IPS<sup>4</sup>o) [1], _Pattern-Defeating Quicksort_ (PDQSort) [9], and the standard C++ std::sort [7].

Synthetic datasets were generated with the following distributions: **uniform**, **already sorted**, **reverse sorted**, **organ pipe**, **normal**, **nearly sorted**, **few unique values**, **exponential**, and **clustered** distributions. For real-world datasets, we selected _Search on Sorted Data_ (SOSD) datasets [4, 6]. We used SOSD **books**, **Facebook**, **OpenStreetMap cell-id**, and **Wikipedia timestamp** datasets. We also include SOSD’s distributional datasets, namely **lognormal**, **normal**, **dense-uniform**, and **sparse-uniform** keys, to cover controlled non-real-world key distributions.

Tests are run for various dataset sizes, ranging from 10<sup>4</sup> to 10<sup>9</sup> for all distributions. For this purpose, we sample the real-world datasets by shuffling them and taking the first _n_ items, where _n_ is the selected dataset size. This allows us to test the real-world datasets at arbitrary dataset sizes while preserving the underlying distribution.

All experiments were run on a single core of an AMD EPYC 9354 processor. The benchmark was compiled as an optimized C++20 binary using release settings -03 -march=native -DNDEBUG. Each reported runtime is based on 10 runs. Each run uses a separate seed, which controls synthetic dataset generation and real-world dataset shuffling. The seed is shared across all algorithms, meaning each algorithm receives the same dataset as the others in each run. Timing is measured only around the sorting call using std::chron::steady_clock, and sorting correctness is validated.

Notably, as shown in Figures 1 and 2, NFSS performs better than BLS on small dataset sizes, while sustaining comparable performance on larger sets and outperforming other sorting algorithms. Figures 3 and 4 further visualise the average speed-up against other algorithms for every dataset. We base the speed-up ratios on a mean of all sizes.

### 6 Conclusion

In this paper, we introduced _Need for Speed Sort_ (NFS Sort), a recursive distribution-based sorting algorithm designed to efficiently handle numeric arrays. By systematically refining dense value intervals and propagating analytical bounds, NFS Sort exploits the structure of the input’s value range while circumventing the overhead of repeated linear scans. Furthermore, the integration of a strategic fallback mechanism guarantees a worst-case time complexity of O(_n_log_n_) and an auxiliary space footprint of O(log_n_), ensuring robust performance even against highly adversarial inputs.

Our theoretical analysis demonstrated that, for a wide variety of input distributions, the expected recursion depth remains shallow, allowing the algorithm to operate in near-linear time in practice. This theoretical efficiency is strongly supported by our extensive empirical evaluation across diverse synthetic and real-world (SOSD)<tbc>

