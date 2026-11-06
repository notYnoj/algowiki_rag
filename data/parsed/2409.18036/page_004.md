<tbc>already improves the current-best \(O(N\cdot\sqrt{loglogN})\) expected running time bound of Han and Thorup [18].

**Main Result 3: An Efficient Algorithm for Truncated Geometric Variate Generation.** Our third contribution is an efficient algorithm for generating _Truncated Geometric_ random variates in the Word RAM model. Specifically, for \(p\in(0,1)\) and a positive integer _n_, a truncated geometric distribution, T-Geo(_p,n_), returns a value \(i\in\{1,\dots,n\}\) with probability \(\frac{p(1-p)^{i-1}}{1-(1-p)^n}\) . As can be seen from the literature, c.f., the aforementioned ODSS algorithm and from our HALT algorithm, generating truncated geometric random variates is of great importance and a crucial building block in many sampling-related algorithms. Somewhat surprisingly, given its importance, we are not aware of any previous work on generating truncated geometric variates in _O_(1) expected time with _O(n_) worst-case space in the Word RAM model. We give the following theorem to make it documented:

Theorem 1.3. _Let_ \(p\in(0,1)\) _be a rational number whose numerator and denominator fit in O_(1) _words, and n be a positive integer fitting in O_(1) _words. There exists an algorithm that generates a random variate from_ T-Geo(_p,n_) _in O_(1) _expected time and O(n_) _space in the worst case in the Word RAM model._

Considering the importance of efficient geometric random variate generation to many research fields, we believe that our new algorithm is of independent interest.

The proofs of some statements (indicated by [\*]) have been deffered to the appendix. Meanwhile, the pseudocodes of our DPSS algorithms can be found in the appendix.

## 2 Preliminaries

In this section, we first introduce the _Word RAM model_ [12] and then formally define the problem of _Dynamic Parameterized Subset Sampling_ (DPSS).

### 2.1 The Word RAM Model

In the Word RAM model [12], each _word_ consists of _d_ bits. Each memory address is represented by _O_(1) words and hence, there are at most 2<sup>_O(d_)</sup> memory addresses, each corresponding to a unique memory cell. Each memory cell stores a word of content which can be considered as an integer in the range of {0,1_,...,_2_<sup>d</sup>_-1}. The content of each memory cell can be accessed by its memory address in _O_(1) time. Furthermore, given two one-word integers _a_ and _b_, each of the following basic arithmetic operations on _a_ and _b_ can be performed in _O_(1) time: addition (_a+b_), subtraction (_a-b_), multiplication (\(a\cdot b\)), division with rounding (\(\lfloor a/b\rfloor\)), comparison (_\>,\<,_=), truncation, and bit operations (e.g., finding the index of the highest or lowest non-zero bit in _a_). Moreover, every _long integer_ is represented by an array of words, and every _float number_ is represented by its exponent and mantissa, where each takes _O_(1) words. Finally, as a convention, we assume that a uniformly random word of _d_ bits can be generated in _O_(1) time. Throughout this paper, the space consumption of an algorithm is measured in words.

The following fact about the Word RAM model is useful:

Fact 2.1. [\*] _In the d-bit Word RAM model, consider the integer universe U_={0,1_,...,d_-1}_, and a set_ \(I\subseteq U\) _of n integers; there exists a data structure that maintains all the integers in I in a sorted linked list and supports each of the following operations in O_(1) _worst-case time:_

\(\bullet\) _each update (either an insertion of a new integer or a deletion of an existing integer) to I;_<tbc>

\(\bullet\) _finding the predecessor or successor for any integer_ \(q\in U\) _in I._

_Such a data structure consumes O(n_) _space at all times, where n is the current cardinality of I._

