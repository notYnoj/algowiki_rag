# Simple in-place yet comparison-optimal Mergesort

**Christian Siebert**<br> University of Stuttgart, High-Performance Computing Center Stuttgart, Germany

**Abstract**

_Mergesort_ is one of the few efficient sorting algorithms and, despite being the oldest one, often still the method of choice today. In contrast to some alternative algorithms, it always runs efficiently using O(_n_log_n_) element comparisons and usually works in a stable manner. Its only practical disadvantage is the need for a second array, and thus twice the amount of memory. This can be an impeding factor, especially when handling large amounts of data, where it is often either impractical or even impossible to fall back to slower or unstable sorting alternatives. Therefore, many attempts have been made to fix this problem by adapting _Mergesort_ to work _in place_. While it is known that such algorithms exist, the previously published solutions are mostly not efficient, become unstable, and/or are very complex. This renders them practically useless for real-world applications.

In this paper, we propose a novel _in-place Mergesort_ algorithm that is stable by design. Albeit its running time of O(_n_log<sup>2</sup>_n_) is not quite optimal, it still works efficiently, both in theory using the optimal number of O(_n_log_n_) comparisons and in practice with low constants, while being easily comprehensible. The baseline for this new algorithm includes just two prerequisites: 1) an optimal array rotation; and 2) the _co-ranking_ idea, published in 2014 and originally intended to parallelize _Mergesort_. Although it would certainly be possible to parallelize the presented algorithm, this paper focuses on the sequential aspect of this efficient, stable and _in-place Mergesort_ algorithm. Additionally, we implemented our algorithm and present performance results measured on one of the largest shared memory systems currently available.

**2012 ACM Subject Classification** Theory of computation \(\rightarrow\) Sorting and searching; Theory of computation \(\rightarrow\) Complexity classes

**Keywords and phrases** Sorting Algorithm, Mergesort, Co-ranking, in-place, stable

### 1 Introduction

Sorting is one of the most fundamental problems in computer science and is used in many applications. A sorting algorithm brings a given set of elements into a specified order. W.l.o.g., we are concentrating on data structures that allow random access to their elements, such as simple arrays. In the following, such arrays are depicted, for example, as _A_[0_...n_-1], where _A_ is the name of the array containing all elements, and 0 as well as _n_-1 are the lower and upper bounds--both inclusive--of element entries, meaning the number of elements in this array is _n_=|_A_|. Although there are very specialized sorting algorithms restricting its use, for example, to small element types (e.g., _radix sort_), we consider the generic and unrestricted case based on comparisons. In such comparison-based sorting algorithms the order of elements is specified using a comparison operator, which takes two elements as input, compares their respective keys, and returns whether the first element either precedes \(\prec\) or succeeds \(\succ\) the second element, or if both have identical keys =, i.e., they are equal. For example, in the standard C library, this comparison operator is a function that uses a return value of type integer to encode these three options. As such, a valid comparison function can return -1, 1, and 0, respectively. This would also define the sorting order to be ascending. On the other hand, a descending order can be achieved by instead returning 1, -1, and 0, respectively. Two further terms that are necessary for the basic understanding of this paper are stability and rank. A sorting algorithm is said to be stable if elements with equal keys stay in the same relative order during sorting. The rank of an element corresponds to the unique index of this element if all elements have been sorted in a stable manner.

CC
f
BY
licensed under Creative Commons License CC-BY 4.0
This publication was submitted to ESA 2024, to SOSA ’25 and again to ESA 2025, but got rejected all the time.
Leibniz International Proceedings in Informatics
LIPICS
Schloss Dagstuhl - Leibniz-Zentrum für Informatik, Dagstuhl Publishing, Germany

