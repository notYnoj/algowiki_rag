<tbc>the trivial matching" for LCS in binary strings. Thus, one might suspect then that these two problems are related, and we show indeed they are. On the other hand, adapting the techniques from \[GHL22\] to our setting is nontrivial as we need to (i) make the combinatorial techniques algorithmic and (ii) handle unequal length strings (note in Theorem 1.3 all strings are of the same length).

Computing LCS is also interesting over larger alphabets. Approximating LCS when there is no restriction on the alphabet has been well studied \[HSSS19, RSSS19, BD21, ANSS22, Nos21\], and currently the best result \[ANSS22, Nos21\] gives a randomized \(\frac{1}{n^{o(1)}}\)-approximation in linear time. Over an alphabet of a given size _q\>_2, there is, similar to the binary case, a trivial linear time \(\frac{1}{q}\)-approximation obtained by taking the longest common constant subsequence. For fixed _q_, over general _q_-ary inputs, this was the best known approximation, even in subquadratic time. For _q_-ary inputs where the two strings have the same length, Akmal and Vassilevska-Williams \[AW21\] (see also \[Akm21\]) generalized the result of Rubinstein and Song, showing for all \(\varepsilon>0\) there is a \((\frac{1}{q}+\delta)\)-approximation in \(n^{1+\varepsilon}\) time.

By the work of Akmal and Vassilevska-Williams \[AW21\], our main result immediately implies improved approximation algorithms over non-binary alphabets, for the general case of not-necessarily-equal length strings. Akmal and Vassilevska-Williams showed that if there is a \((\frac{1}{2}+\delta)\)-approximation for binary LCS (which we show), there is a \((\frac{1}{q}+\delta')\)-approximation for _q_-ary LCS in essentially the same runtime. Hence, we have the following corollary.

**Corollary 1.4** (Follows from Theorem 1.2 and Theorem 1 of \[AW21\])**.** _For all_ \(\varepsilon>0\) _and integers_ \(q\ge 2\)_, there exists an absolute constant_ \(\delta=\delta(\varepsilon)>0\) _and a deterministic algorithm that, given two q-ary strings x and y of not-necessarily-equal length, outputs a_ \((\frac{1}{q}+\delta)\)_-approximation of the longest common subsequence in time_ \(O(n^{1+\varepsilon})\) _where n_=max(|_x|,|y_|).

## 2 Preliminaries

For clarity of presentation, we sometimes drop floors and ceilings where they are not crucial.

### Strings

For a string _x_, a _subsequence_ of _x_ is any string obtained by deleting any number of bits of _x_. A _substring_ is a subsequence that appears as consecutive bits of _x_. Let 0(_x_) and 1(_x_) denote the number of zeros and ones, respectively, in _x_. A _property P_ of binary strings is a set of binary strings. We say a string _x satisfies/has_ a property _P_ if _x_ is in the set _P_.

### Intervals

We use interval notation similar to that of \[CDG<sup>+</sup>20\]. By convention, an interval _I_=\[_a,b_\] denotes the set {_a_+1_,a_+2_,...,b_}, and we write start_I=a_ and end_I=b_. Note that _I_ and \(I'\) are disjoint if and only if either \(\text{end}I'\le\text{start}I\) or \(\text{end}I\le\text{start}I'\). The _length_ of an interval _I_=\[_a,b_\] is _b-a_. For a string _x_, let _x<sub>I</sub>_ denote the contiguous substring \(x_{a+1}x_{a+2}\cdots x_b\). By abuse of notation, when the string _x_ is understood, we may use _I_ to refer to the substring _x<sub>I</sub>_. For an integer _w_, we say interval _I_ is _w-aligned_ if start_I_ and end_I_ are multiples of _w_. An interval is a _w-interval_ if it has length _w_ and is _w_-aligned. Let round_<sub>w</sub>(I_) denote the largest _w_-aligned subinterval of _I_. Note we always have |round_<sub>w</sub>(I_)|_\>|I_|-2_w_.

For an interval _I_ and integer _w_, let I_<sub>w</sub>(I_) be the collection of _w_-intervals that are subintervals of _I_. When a string _x_ is understood (as it always will be), we write I_<sub>w</sub>_:=I_<sub>w</sub>_(|_x_|). Note that if |_x_| is a multiple of _w_, the intervals of I_<sub>w</sub>_ partition \[_m_\].

A _rectangle_ is a product \(I\times J\) where _I_ and _J_ are intervals. A _square_ is a rectangle \(I\times J\) with |_I_|=|_J_|. A _certified rectangle_ is a pair \((I\times J,\kappa)\) where \(\kappa\) is a positive number.

Define a partial ordering on intervals, where \(I<I'\) iff \(\text{end}I\le\text{start}I'\). That is, every element of _I_ is less than every element of \(I'\). Note that if two intervals have nonempty intersection, they are incomparable. We also define a partial ordering on rectangles, where \(I\times J<I'\times J'\) iff \(I<I'\) and \(J<J'\). We say a collection<tbc>

