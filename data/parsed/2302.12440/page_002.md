## 1 Introduction

Sorting is one of the most fundamental problems in computer science. Among the wide variety of sorting algorithms, an important class is comparison-based sorting. It is well-known that sorting a list of _n_ numbers requires (1-_o_(1))_n_log_n_ comparisons (see e.g., \[CLRS22\]), even if the input list is a random permutation.<sup>1</sup> A good number of algorithms require only (1+_o_(1))_n_log_n_ comparisons, such as binary insertion sort, merge sort (see e.g., \[Knu98\]), and merge insertion sort \[FJ59\].

Sorting is run on many real-world applications with large data sets. Thus, it is important to consider faults that arise unavoidably in large systems. For comparison-based sorting, this means that the result of a comparison could be incorrect. We consider one well-studied model for simulating such faults, studied in, e.g., \[Hor63, Gal78, Pel89, BM86, FRPU94, BMW16\]. In this model, the result of each query (or noisy comparison in the context of sorting) is flipped independently with probability _p_ for some fixed \(p\in(0,\frac{1}{2})\) and repeated queries are allowed. Let us call it the noisy model. In this model, we define NoisySorting(_n_) as the task to sort _n_ elements using noisy comparisons. As this model inherently has errors and no algorithm can always produce correct outputs, we consider algorithms with _o_(1) error probability.

If we repeat each noisy comparison \(\Theta(logn)\) times, the majority of the returned results is the correct comparison result with high probability. Therefore, we can modify any classical comparison- based sorting algorithm with _O(n_log_n_) comparisons, by replacing each comparison with \(\Theta(logn)\) noisy comparisons, to get an _O(n_log<sup>2</sup>_n_)-comparison algorithm for Noisy Sorting that succeeds with 1-_o_(1) probability.

In fact, better algorithms were known. Feige, Raghavan, Peleg, and Upfal \[FRPU94\] gave an algorithm for NoisySorting(_n_) with only _O(n_log_n_) noisy comparisons. Recently, Wang, Ghaddar, Wang \[WGW22\] analyzed the constant factor hidden in \[FRPU94\]’s algorithm,<sup>2</sup> and gave an improved upper bound of \((1+o(1))\frac{2}{log\left(\frac{1}{\frac{1}{2}+\sqrt{p(1-p)}}\right)}nlogn\) noisy comparisons. They also showed that \((1-o(1))\frac{1}{I(p)}nlogn\) comparisons are necessary for any algorithm with _o_(1) error probability, where _I(p_)=1-_h(p_) is the capacity of BSC channel with crossover probability _p_ (which is also the amount of information each noisy comparison gives) and _h(p_)=-_p_log_p_-(1-_p_)log(1-_p_) is the binary entropy function.

Despite these progresses, there is still a big gap between the upper and lower bounds. For instance, when _p_=0.1, the constant in front of _n_log_n_ for the lower bound is roughly 1.88322, whereas the constant for the upper bound is roughly 6.21257, more than three times as large. It is a fascinating question to narrow down this gap, or even close it like the case of classical sorting.

As the main result of our paper, we show that it is indeed possible to close this gap by giving both an improved upper bound and an improved lower bound:

**Theorem 1** (Noisy Sorting Upper Bound)**.** _There exists a deterministic algorithm for_ NoisySorting(_n_) _with error probability o_(1) _which always uses at most_

\((1+o(1))\left(\frac{1}{I(p)}+\frac{1}{(1-2p)log\frac{1-p}{p}}\right)nlogn\)

_noisy comparisons._

<sup>1</sup>All logarithms in the paper are of base 2. <sup>2</sup>The actual constant is quite complicated, see \[WGW22\] for details.

