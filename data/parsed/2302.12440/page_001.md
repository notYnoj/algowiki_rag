# Optimal Bounds for Noisy Sorting

**Abstract**

Sorting is a fundamental problem in computer science. In the classical setting, it is well- known that \((1\pm o(1))nlog_2n\) comparisons are both necessary and sufficient to sort a list of _n_ elements. In this paper, we study the Noisy Sorting problem, where each comparison result is flipped independently with probability _p_ for some fixed \(p\in(0,\frac{1}{2})\). As our main result, we show that

\((1\pm o(1))\left(\frac{1}{I(p)}+\frac{1}{(1-2p)log_2\left(\frac{1-p}{p}\right)}\right)nlog_2n\)

noisy comparisons are both necessary and sufficient to sort _n_ elements with error probability _o_(1) using noisy comparisons, where _I(p_)=1+_p_log<sub>2</sub>_p_+(1-_p_)log<sub>2</sub>(1-_p_) is capacity of BSC channel with crossover probability _p_. This simultaneously improves the previous best lower and upper bounds (Wang, Ghaddar and Wang, ISIT 2022) for this problem.

For the related Noisy Binary Search problem, we show that

\((1\pm o(1))\left((1-\delta)\frac{log_2(n)}{I(p)}+\frac{2log_2\left(\frac{1}{\delta}\right)}{(1-2p)log_2\left(\frac{1-p}{p}\right)}\right)\)

noisy comparisons are both necessary and sufficient to find the predecessor of an element among _n_ sorted elements with error probability \(\delta\). This extends the previous bounds of (Burnashev and Zigangirov, 1974), which are only tight for \(\delta=1/n^{o(1)}\).

Yuzhou Gu<br> MIT<br> yuzhougu@mit.edu

Yinzhan Xu<br> MIT<br> xyzhan@mit.edu

