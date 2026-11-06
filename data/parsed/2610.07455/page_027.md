The exact minimum of the stored sparsifier can be found after the stream by enumerating assignments; the model places no restriction on postprocessing time. This uses _O<sub>R</sub>(n_) additional bits for one assignment, which is absorbed because _R<sup>⋆</sup>_ is non-trivial and \(\mathsf{NRD}_n(R^\star)=\Omega_{R^\star}(n)\) by Observation 3.3. Theorem 6.1 with parameter \(\delta\) gives the space bound in part (i).

For part (ii), any finite-factor multiplicative approximation must output zero when OPT<sub>min</sub>=0 and a positive number when OPT<sub>min</sub>_\>_0. It therefore decides satisfiability. The lower bound follows directly from Theorem 5.1.

## 7 Exact-CSP

We now determine the one-pass streaming space needed to solve Exact-CSP(_R_) on simple instances. As in the previous sections, we first reduce _R_ to its core. After this reduction, the answer is governed by the degree of the core relation.

The two bounds use degree in different ways. For the upper bound, the degree-_d_ representation of **1**_<sub>R</sub>_ lets us write the number of satisfied constraints using only terms that involve at most _d_ variables. The algorithm keeps the coefficient of each such term. When \(d\ge 1\), the lower bound uses 2_<sup>d</sup>_ assignments and a signed sum of their values that isolates one chosen constraint. The construction in Lemma 4.6 then lets Bob recover each of these values from the exact optimum returned by the streaming algorithm.

**Theorem 7.1** (Exact-CSP)**.** _Let_ \(R\subseteq D^k\)_, let R<sup>⋆</sup>_=core(_R_) _have core domain C, and put d_=deg_<sub>C</sub>_(**1**_<sub>R<sup>⋆</sup></sub>). The following statements hold._

(_i)_ _There is a deterministic one-pass algorithm for_ Exact-CSP(_R_) _using O<sub>R</sub>(n<sup>d</sup>_log(_n_+1)) _bits on unweighted simple instances._<tbc>

(_ii)_ _If_ \(d\ge 1\)_, every randomized bounded-error one-pass algorithm for_ Exact-CSP(_R_) _on unweighted simple instances uses_ \(\Omega_R(n^d)\) _bits of space._<tbc>

_(iii)_ _If R is symmetric and_ \(d\ge 1\)_, the lower bound holds even when no unordered scope is repeated._

_Consequently, when_ \(d\ge 1\),

\(\Omega_R(n^d)\le\mathsf{SPACE}(\mathsf{Exact-CSP}(R))\le O_R(n^dlog(n+1)).\)

_When d_=0_, the relation R<sup>⋆</sup> is either empty or equal to C<sup>k</sup>. Thus the optimum is either always_ 0 _or is the number of constraints in the stream, and it can be found using O<sub>R</sub>_(log(_n_+1)) _bits on simple instances._

We prove the upper bound directly. We then prove the lower bound for a core relation and use Lemma 4.2 to obtain the result for an arbitrary relation.

The upper bound follows by keeping the coefficients of a low-degree representation of the objective. The Boolean version of this argument appears in \[KPSY23, Section 1.1\]. We give a generalization of their result to any finite domain.

**Lemma 7.2** (Exact-CSP upper bound)**.** _Let_ \(R\subseteq D^k\)_, let R<sup>⋆</sup>_=core(_R_) _have core domain C, and put d_=deg_<sub>C</sub>_(**1**_<sub>R<sup>⋆</sup></sub>). There is a deterministic one-pass algorithm that solves_ Exact-CSP(_R_) _on an instance with n variables and m constraints using O<sub>R</sub>(n<sup>d</sup>_(log(_n_+1)+log(_m_+1))) _bits of space. In particular, on simple instances the space is O<sub>R</sub>(n<sup>d</sup>_log(_n_+1)).

