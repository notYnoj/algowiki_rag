bsort: A theoretically efficient non-comparison-based sorting algorithm for integer and floating-point numbers

**_Abstract_--This paper presents bsort, a non-comparison-based sorting algorithm for signed and unsigned integers, and floating- point values. The algorithm unifies these cases through an approach derived from binary quicksort, achieving O(wn) runtime asymptotic behavior and O(w) auxiliary space, where w is the element word size. This algorithm is highly efficient for data types with small word sizes, where empirical analysis exhibits performance competitive with highly optimized hybrid algorithms from popular libraries.**

**_Index Terms_--sorting algorithm, bitwise operations, in-place sorting, floating-point values, non-comparison sorting**

### I. INTRODUCTION

Sorting is a fundamental problem in computer science that involves arranging an input sequence (_v_<sub>1</sub>_,v_<sub>2</sub>_,...,v<sub>n</sub>_) into a monotonically non-decreasing or non-increasing sequence. Algorithms that solve this problem by comparing pairs of elements are known as comparison-based sorts. It is a well- established result that any such algorithm has a worst-case time complexity lower bound of \(\Omega(nlog(n))\) [1].

Non-comparison-based algorithms, such as radix sort, offer a compelling alternative to comparison-based methods, with linear-time performance. In-place variants that operate at the bit-level, such as binary quicksort [2], provide a memory- efficient solution but are limited to sorting equally-signed integer values. Extensions to handle sequences with both positive and negative integer elements [3] and separate out- of-place methods have been extended to handle floating-point values [4]. This paper aims to present a single, unified algorithm that is simultaneously in-place, and capable of sorting signed and unsigned integers, and floating-point values.

### II. BINARY QUICKSORT ALGORITHM

The binary quicksort algorithm is a divide-and-conquer algorithm which splits the array _a_=[_a_<sub>1</sub>_,a_<sub>2</sub>_,...,a<sub>n</sub>_] based on the bits of its elements. The process is applied recursively, starting from the most significant bit (MSB).

In a single partitioning step, the array is split into two sub- arrays, \(a'\) and \(a''\), which satisfy the following invariants:

(i) \(a_i\wedge m\neq 0\forall a_i\in a'\)

(ii) \(a_j\wedge m=0\forall a_j\in a''\)

Where \(\wedge\) is the bitwise AND operator, and _m_ is a single- bit mask used in the current iteration which is defined by \(m=1\le(s-i)\) where \(\le\) is the left-shift bitwise operator, \(s\in\mathbb{Z}^+\) is the number of bits every element in _a_ has, and \(i\in\mathbb{Z}:1\le i\le s\) the current iteration, starting at 1. If _a_<sub>1</sub> precedes _a_<sub>2</sub> or vice versa depends on the desired sort direction (ascending or descending). After partitioning on one bit, the algorithm recursively sorts these sub-arrays using the mask for the next significant bit. This continues until all _s_ bits have been processed, at which point the array is fully sorted.

For example, assuming _a_=[5,7,1,6,3,4,0], the entire tracing of the binary quicksort algorithm is illustrated in Fig. 1:

_bsort_ uses a modified version of the _binary quicksort_ algorithm as its core sub-procedure, which is described in Algorithm 1, and Algorithm 2 shows how this sub-procedure is used recursively to sort equally-signed integers.

5 7
1 6
3 4
0 m 101 111 001 110 011 100 000 100 1
3 0
5 7
6 4
m 001 011 000 101 111 110 100 010 k1 1
0 3
5 4
7 6
m 001 000 011 101 010 111 110 001 k2 k1 k'2 0
1 3
4 5
6 7
m 000 001 011 010 101 110 111 000

Benjamín Guzmán<sup>∗</sup><br> Independent researcher<br> Mexico City, Mexico<br> bg@benjaminguzman.dev<br> \*Work performed prior to joining Amazon.

arXiv:2603.08929v1 [cs.DS] 9 Mar 2026

Fig. 1: Tracing of binary quicksort algorithm

