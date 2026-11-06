(_a)_ (3SUM) 3_SUM on n integers of absolute value at most_ \(n^\nu\) _reduces deterministically, in n_<sup>3/2+_o_(1)</sup> _time, to n_<sup>1/2+_o_(1)</sup> _instances of Exact Triangle on n_<sup>1/2+_o_(1)</sup> _vertices per part with weights of absolute value n_<sup>_O_(1)</sup> _\[CH20, VW13\]._<tbc>

_(b)_ ((min,+)-product and APSP) _If a deterministic algorithm solves Exact Triangle on s vertices per part with weights of absolute value at most cU, for a suitable constant c, in time T(s_) _with T(s)/s nondecreasing, then the_ (min,+)_-product of two_ \(n\times n\) _integer matrices with entries of absolute value at most U can be computed deterministically in O(n_<sup>2</sup>_T(n_<sup>1/3</sup>)log<sup>2</sup>_U_) _time, and APSP on directed n-vertex graphs with integer weights of absolute value at most_ \(n^\nu\) _and no negative cycles in O(n_<sup>2</sup>_T(n_<sup>1/3</sup>)log<sup>3</sup>_n_) _time \[VW10, VW18, VW13\]._

Using the above known reductions we solve both 3SUM and APSP polynomially faster:

**Theorem 22** (3SUM and APSP)**.** _Let_ \(\nu\) _be a constant. Using Theorem 5 (through Theorem 19), deterministic algorithms solve_ 3_SUM on n integers of absolute value at most_ \(n^\nu\) _in_ \(n^{2-1/1296+o(1)}\le O(n^{1.99923})\) _time, and the_ (min,+)_-product of two_ \(n\times n\) _integer matrices with entries of absolute value at most_ \(n^\nu\)_, as well as APSP on directed n-vertex graphs with integer weights of absolute value at most_ \(n^\nu\) _and no negative cycles, in_ \(\tilde{O}(n^{3-1/1944})\le O(n^{2.99949})\) _time. Using Corollary 26 instead, the times are_ \(n^{2-\varepsilon^\prime/2+o(1)}\le O(n^{1.9992})\) _and_ \(\tilde{O}(n^{3-\varepsilon^\prime/3})\le O(n^{2.99942})\).

_Proof._ Plug Theorem 19 into Theorem 21. With the bound _O(n_<sup>3-1/648</sup>log<sup>2</sup>_n_) of Theorem 19, the cost for 3SUM is

\(n^{3/2+o(1)}+n^{1/2+o(1)}\cdot O\big((n^{1/2+o(1)})^{3-1/648}\mathrm{log}^2n\big)=n^{2-1/1296+o(1)}=n^{1.999228\dots+o(1)},\)

and for the (min,+)-product and APSP, with _T(s_)=_O(s_<sup>3-1/648</sup>log<sup>2</sup>_s_), for which _T(s)/s_ is nondecreasing, it is<tbc>

\(\tilde{O}\big(n^2(n^{1/3})^{3-1/648}\big)=\tilde{O}\big(n^{3-1/1944}\big),3-1/1944=2.99948\dots<2.99949.\)

<tbc>With the bound \(O(n^{3-\varepsilon^\prime}\mathrm{log}n)\) instead, the cost for 3SUM is<tbc>

\(n^{3/2+o(1)}+n^{1/2+o(1)}\cdot O\big((n^{1/2+o(1)})^{3-\varepsilon^\prime}\mathrm{log}n\big)=n^{2-\varepsilon^\prime/2+o(1)}=n^{1.999125+o(1)},\)

<tbc>and for the (min,+)-product and APSP, with \(T(s)=O(s^{3-\varepsilon^\prime}\mathrm{log}s)\), it is

\(\tilde{O}\big(n^2(n^{1/3})^{3-\varepsilon^\prime}\big)=\tilde{O}\big(n^{3-\varepsilon^\prime/3}\big),3-\varepsilon'/3=2.99941\dots<2.99942.\)

_Remark_ 23 (3XOR). The same approach as for 3SUM gives a deterministic truly subquadratic algorithm for 3XOR (given three lists of _n_ vectors in \(\mathbb{F}_2^{O(\mathrm{log}n)}\), find one vector from each list such that the three XOR to zero \[JV16, DSW18\]), using linear hash functions over F<sub>2</sub> whose rows are chosen one at a time from an \(\varepsilon\)-biased set \[AGHP92\] by the method of conditional expectations.

## 4 The matrix theorem in general: a data structure

In this section, we extend our algorithm from Section 2 in two directions. First, we turn it into a data structure. After preprocessing _X_ and _Y_ in less time than it takes to write down _XY_ , the data structure answers a query for any single entry of _XY_ , not known in advance, in time<tbc>

