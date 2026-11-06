## 23:2 Simple in-place yet comparison-optimal Mergesort

It is well known that any comparison-based sorting algorithm needs \(\Omega(nlogn)\) comparisons in the worst case (see, e.g., [5], p. 193). As such, we are, in particular when handling large amounts of data, mostly interested in sorting algorithms that usually achieve this theoretical lower bound. While there are many different sorting algorithms, only a few of them are appropriate in this context. For instance, the corresponding Wikipedia page [4] currently lists, explains and compares more than 45 different sorting algorithms, whereas the interesting ones for large _n_ are represented by _Quicksort_, _Mergesort_ and _Heapsort_. These three can also be varied and combined.  1 compares the aforementioned major algorithms with respect to their properties and features, marking these either with a thumbs-up if this is considered good or with a thumbs-down if not. In addition to the theoretical performance, we compare also the practical constant factor, which is ignored in the theoretical O-notation. This constant can be obtained for a specific implementation and architecture by measuring its running time for different numbers of elements and fitting the resulting performance data to the formula \(c\cdot nlogn\).

For example, _Quicksort_ is popular because it has, in practice, a small hidden constant in the theoretical O-notation and achieves O(_n_log_n_) comparisons in many cases, such as on average whenever pivots are picked at random. However, if unsuited pivot values are chosen (e.g., with fixed pivots and pre-sorted inputs), it can slow down to as low as O(_n_<sup>2</sup>), which is catastrophic for large _n_. _Heapsort_, on the other hand, always achieves O(_n_log_n_) comparisons and needs no additional memory but is cache-inefficient and thus results in larger practical constants. Additionally, both of these sorting algorithms do not preserve the order of equal elements, so they are not stable. Although _Mergesort_ meets this stability criterion and is efficient, it works wastefully regarding additional memory. In essence, an application programmer can only pick up to three good features out of the four compared properties and hence has to decide which sorting algorithm is best suited for a specific application.

While there are attempts to improve upon certain disadvantages, such as improved pivot-selection strategies for _Quicksort_ or reintroducing stability, this usually worsens one or more of the other properties. For example, every sorting algorithm can be turned into a stable sort by adding the original index to each element and comparing also the indices for equal elements. However, this will directly lead to an additional memory consumption of O(_n_). This paper concentrates on making _Mergesort_ memory efficient, which is described by the algorithmic term _in-place_. A formal definition of this term will be given in Definition 2. The goal is to create an _in-place Mergesort_ that is still stable, works with an optimal number of comparisons and with low constants. Ideally, it should nevertheless be simple enough to be easily comprehensible.

## 1.1 Related work

There are numerous publications on how to make _Mergesort_ memory efficient. Naive approaches can reduce the additional space consumption down to O(1), but at the cost of drastically increasing the number of comparisons to O(_n_<sup>2</sup>) or even O(_n_<sup>2</sup>log_n_). Intermediate

\begin{tabular}{cccccc}
Algorithm & \(\sharp\) Comparisons & Constant & Stability & \multicolumn{2}{c}{Memory} \\
_Quicksort_ & O(_n_<sup>2</sup>) & small & unstable & O(log_n_) & \\
_Mergesort_ & O(_n_log_n_) & small & stable & O(_n_) & \\
_Heapsort_ & O(_n_log_n_) & large & unstable & O(1) & \\
\end{tabular}

1 Properties and features of "fast" sorting algorithms

