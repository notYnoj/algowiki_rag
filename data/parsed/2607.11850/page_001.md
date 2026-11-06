# Need for Speed Sort: A Recursive Distribution-Based Sorting Algorithm

### Abstract

We present _Need for Speed Sort_ (NFS Sort), a recursive distribution- based sorting algorithm designed for numeric arrays. The algorithm partitions elements into equal-width value intervals, recursively refines dense buckets, and propagates analytical interval bounds between recursive calls, avoiding repeated scans for local minima and maxima. NFS Sort combines a fragment-based, cache-conscious scatter procedure for large subarrays with a lower-overhead auxiliary- array approach for smaller inputs. Small buckets are deferred to a final insertion-sort cleanup, while a comparison-based fallback is activated when recursive partitioning repeatedly fails to reduce the problem size. This mechanism guarantees a worst-case running time of _O(n_log_n_) and auxiliary space usage of _O_(log_n_). Experimental evaluation on synthetic inputs and real-world datasets from the SOSD benchmark suite compares NFS Sort with Balanced Learned Sort, IPS4o, Boost Spreadsort, PDQSort, and std::sort. The results show that NFS Sort is competitive or better than established state-of-the-art sorting methods across dataset sizes and distributions, outperforming the learned baseline particularly on smaller inputs while retaining strong performance at larger scales. Overall, NFS Sort combines efficient recursive distribution, practical memory management, and robust worst-case guarantees for high-performance numeric sorting.

### 1 Introduction

Sorting is a fundamental problem in computer science and a core component of many software systems. Comparison-based algorithms such as quicksort, mergesort, heapsort, and introsort are robust and widely used, but they are limited by the \(\Omega(n\mathrm{log}n)\) lower bound in the comparison model [2]. For numeric values, distribution-based methods can avoid this bound by exploiting the structure of the value range [2, 5].

We introduce _Need for Speed Sort_ (NFS Sort), a recursive distribution- based sorting algorithm for numeric arrays. At each recursive step, NFS Sort divides the current value range into equally spaced buckets, scatters elements into those buckets, and recursively processes only those that remain larger than the set threshold. Small buckets are left for a final insertion-sort pass, which is efficient because all remaining disorder is confined to bounded-size regions.

NFS Sort combines ideas from existing distribution sorters. Inspired by Flashsort [8], it maps elements to buckets according to their relative position in the observed value range. Unlike a single-pass approach, it recursively refines dense regions. Its implementation also uses memory-management techniques inspired by IPS<sup>4</sup>o [1].

To avoid repeated memory accesses, NFS Sort propagates analytical bucket bounds instead of recomputing minima and maxima

during recursion. It also includes a fallback mechanism: if recursion repeatedly fails to reduce the size of a bucket, that bucket is sorted using a comparison-based sort. This preserves a worst- case _O(n_log_n_) bound while retaining the practical advantages of distribution sorting.

This paper describes the algorithm, analyses its time and space complexity, discusses adversarial inputs, and evaluates its empirical performance against established sorting methods.

To facilitate reproducibility, the source code for NFS Sort and the accompanying benchmark implementation are publicly available at https://github.com/fsucic/need-for-speed-sort.

The remainder of the paper is organized as follows. Section 2 discusses related work. Section 3 describes the algorithm and its implementation details. Section 4 analyzes the theoretical behavior of NFS Sort, including worst-case complexity, expected recursion depth under distributional assumptions, and adversarial inputs. Section 5 presents experimental results, and Section 6 concludes.

### 2 Related Work

Sorting algorithms are commonly divided into comparison-based and distribution-based methods. NFS Sort belongs to the distribution- based family. Distribution-based sorting algorithms exploit properties of the keys rather than relying only on comparisons. Bucket sort, radix sort, and counting sort can achieve linear time under suitable assumptions, but their performance depends on the key domain, input distribution, and memory requirements [2, 5]. Flashsort is particularly relevant to this work because it maps elements to buckets based on their relative position between the minimum and maximum input values, followed by local clean-up [8].

More recent work has focused on engineering distribution sorting for modern hardware. IPS<sup>4</sup>o [1], for example, uses efficient classification, buffering, and block permutation techniques to improve cache behaviour and reduce memory overhead. NFS Sort is inspired by these ideas, but applies a sequential recursive distribution strategy: it repeatedly refines dense value intervals, propagates analytical bounds between recursive calls, and uses a fallback sorter to avoid pathological recursion.

### 3 Algorithm

This section describes the design of NFS Sort. We first present a naive version of the algorithm to illustrate its core principles. We then introduce several optimisations that are incorporated in the final implementation and noticeably improve performance.

NFS Sort does not introduce a fundamentally new sorting paradigm, but rather combines existing ideas into an efficient overall design. Conceptually, it can be viewed as a recursive variant of

Fran Suˇci ́c<br> Independent Researcher<br> Croatia<br> fransucic46@gmail.com

Leo Vitasovi ́c<br> IT University of Copenhagen<br> Denmark<br> leov@itu.dk

Nikola Petruši ́c<br> Independent Researcher<br> Croatia<br> nikola.petrusic221@gmail.com

arXiv:2607.11850v1 [cs.DS] 13 Jul 2026

