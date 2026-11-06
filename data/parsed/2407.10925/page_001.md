# Improved Lower Bounds on the Expected Length of Longest Common Subsequences

**Abstract**

It has been proven [8] that, when normalized by _n_, the expected length of a longest common subsequence of _d_ random strings of length _n_ over an alphabet of size \(\sigma\) converges to some constant that depends only on _d_ and \(\sigma\). These values are known as the Chvátal-Sankoff constants, and determining their exact values is a well- known open problem. Upper and lower bounds are known for some combinations of \(\sigma\) and _d_, with the best lower and upper bounds for the most studied case, \(\sigma=2,d=2\), at 0.788071 and 0.826280, respectively [20]. Building off previous algorithms for lower-bounding the constants, we implement runtime optimizations, parallelization, and an efficient memory reading and writing scheme to obtain an improved lower bound of 0.792665992 for \(\sigma=2,d=2\). We additionally improve upon almost all previously reported lower bounds for the Chvátal-Sankoff constants when either the size of alphabet, the number of strings, or both are larger than 2.

### 1 Introduction

A **_subsequence_** of a given string is a string obtained by removing zero or more characters. Given two strings _a,b_ over an alphabet \(\Sigma\), a **_Longest Common Subsequence_** (LCS) of the two strings is the longest string that occurs as a subsequence of both _a_ and _b_. Computing an LCS is a fundamental algorithmic problem in computer science and is solvable using a classical text book example of a polynomial-time dynamic programming algorithm (see, e.g., [4, 11]). The LCS problem is relevant to many different fields including computational biology [15, 24], cryptography [7, 23], and computational linguistics [14, 19, 21], and sees applications in remarkably diverse areas including data comparison tools, revision control systems, stratigraphy, and even in the mathematical analysis of bird songs [14, 18].

A major open problem related to longest common subsequences concerns determining the expected length of an LCS of _d_ random strings of length _n_ whose

characters are chosen independently and uniformly over an alphabet of size \(\sigma\). It has been shown that as _n_ goes towards infinity, the expected LCS length normalized by _n_ converges to a constant that depends only on \(\sigma\) and _d_ [8, 16]. These constants are called the Chvátal-Sankoff constants and their exact values are unknown [8]. The Chvátal-Sankoff constants were originally defined for an LCS of only two strings, but were later expanded for an arbitrary number of strings _d_. We denote the generalized constants as \(\gamma_{\sigma,d}\), and use \(\gamma\) or write simply ‘the Chvátal-Sankoff constant’ when referring to the constant for two binary strings. Formally,

Definition 1.1. _The Chvátal-Sankoff constant_ \(\gamma_{\sigma,d}\) _is defined as_

\(\gamma_{\sigma,d}=lim_{n\rightarrow\infty}\frac{\mathbb{E}(X_{\sigma,d,n})}{n}\)

_where_ \(X_{\sigma,d,n}\) _is a discrete random variable for the length of a longest common subsequence of d strings of length n whose characters are independently and uniformly selected from an alphabet with_ \(\sigma\) _symbols._

The problem of calculating the Chvátal-Sankoff constants has received significant attention and is explicitly mentioned in several textbooks (see [22, 26, 27, 30]). Accordingly, extensive effort has been put into approximating and calculating lower and upper bounds for \(\gamma\) and for various \(\gamma_{\sigma,d}\) (see Section 2). In continuing these efforts, we improve upon nearly all previously reported lower bounds on the Chvátal-Sankoff constants, with particular attention towards \(\gamma_{2,2}\), bringing its lower bound from 0.788071 up to 0.792665992.

**Our Approach.** To improve on previous lower bounds, we build off of algorithms for generating lower bounds by Lueker [20] and Kiwi and Soto [16]. We take advantage of the independent nature of the performed calculations to parallelize the algorithms, and implement them from scratch in C++ with several runtime optimizations. We focus primarily on \(\sigma=2,d=2\), where our changes speed up the algorithm substantially and allow us to compute values for larger string lengths than previously possible. In addition to parallelization, we employ

\*Worcester Polytechnic Institute, United States

George T. Heineman<sup>∗</sup> Chase Miller Gábor Sárközy

Daniel Reichman Andrew Sails Duncan Soiffer

