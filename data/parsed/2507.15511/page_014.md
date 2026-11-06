<tbc>_and explores only canonical aliased states b_=canon(_b_) _(CNF; Appendix E). Then the deterministic running time satisfies_

\(T(n)=O^*\big(2^{n/2-\varepsilon}\big)\text{\textit{with}}\varepsilon=log_2\big(\frac{4}{3}\big)\approx 0.415,\)

_and the space usage is O_<sup>∗</sup>(2<sup>_n/_2</sup>)_. The randomized variant achieves the same_ \(O^*\big(2^{n/2-\varepsilon}\big)\) _bound in expectation._

_(Scope and unconditional bound.)_ If a half \(\ell_i\) has fewer than two distinct element values, CNF is vacuous on that side and we revert to the certificate-sensitive bound of Theorem 4: \(T(n)=O\big((U_0+U_1)n^2\big)\) deterministically and _O_\(\big(\)(_U_<sub>0</sub>+_U_<sub>1</sub>)_n_\(\big)\) in expectation, which is _O_<sup>∗</sup>(2<sup>_n/_2</sup>) in the worst case. Otherwise each half has at least two distinct values, so an alias pair exists per half and the bound above applies, yielding _O_<sup>∗</sup>\(\big(\)2<sup>_n/_2-log<sub>2</sub>(4/3)</sup>\(\big)\).

_Proof._ Immediate from Lemma 9 (each half expands at most \(E_i\le\frac{3}{4}2^k\) with _k=n/_2) and Theorem 4 applied with _E<sub>i</sub>_ in place of _U<sub>i</sub>_.

_Remark_ 3 (Conservative statements). We state slightly conservative bounds for readability; the following routine tightenings are available without changing the algorithm: (i) Space under aliasing is _O_((_E_<sub>0</sub>+_E_<sub>1</sub>)_n_)=_O_<sup>∗</sup>(2<sup>_n/_2-log<sub>2</sub>(4/3)</sup>); (ii) The randomized bound holds w.h.p. using standard load-controlled hashing; (iii) A deterministic time _O(Un_log_n_) follows by replacing hashing with balanced maps and using _O_(log_n_) lex-compare primitives. We omit these proofs as they are straightforward variations on the analyses given.

## 6 A Nuanced Structural View of Fine-Grained Hardness

Our algorithm adds a structural dimension--via the number of distinct subset sums _U_ (equivalently, low collision entropy _H<sub>c</sub>(S_)=_n_-log<sub>2</sub>_U_)--and makes explicit that many classical hardness arguments implicitly target a structure-resistant slice of instances. We formalize this dependence.

### 6.1 The Collision-Resistant Slice

We begin by formalizing the slice of Subset-Sum where classical worst-case barriers are most informative.

_Definition_ 3 (Collision-Resistant Subset-Sum)_. For_ \(\delta\in(0,1]\)_, define_

\(\text{Subset-Sum}^{\ge\delta}:=\{(S,t):|\Sigma(S)|\ge 2^{\delta n}\}.\)

_A reduction to_ Subset-Sum _is_ collision-resistant _if, for some constant c\>_0_, its outputs lie in_ Subset-Sum\(^{\ge c}\).

_Example._ The classical powers-of-two SAT\(\rightarrow\)Subset-Sum encoding yields _U_=2_<sup>n</sup>_, i.e., \((S,t)\in\text{Subset-Sum}^{\ge 1}\).

The Horowitz-Sahni algorithm runs in _O_<sup>∗</sup>(2<sup>_n/_2</sup>) time. Thus, to preclude algorithms that beat this bound under a certificate-sensitive lens, a SETH-based hardness claim should (at minimum) target instances in Subset-Sum\(^{\ge 1/2}\), i.e., enforce \(U\ge 2^{n/2}\) on the image of the reduction. This pinpoints the regime where adaptive methods cannot short-circuit via structural collisions and where classical worst-case lower bounds are most informative.

