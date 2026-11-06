**Definition 2.12** (Strongly base-orderable)**.** _A matroid M on E is_ strongly base-orderable _(SBO) if, for any two bases B_<sub>1</sub> _and B_<sub>2</sub> _of M, there exists a bijection_ \(\pi:B_1\rightarrow B_2\) _such that for every_ \(X\subseteq B_1\)_, both_

\((B_1\backslash X)\cup\pi(X)\text{\textit{and}}(B_2\backslash\pi(X))\cup X\)

_are bases of M._

Important families of SBO matroids include partition matroids, transversal matroids, gammoids, graphic matroids on _K_<sub>4</sub>-minor-free graphs, etc.

While packing common basis of two arbitrary matroids is an NP-Hard problem under the rank oracle model (NP-Hard even for two arbitrary linear matroids with given representation) \[BS21\], the following theorem by Davies and McDiarmid provides a nice characterisation for packing common basis in SBO matroids.

**Theorem 2.13** (Davies-McDiarmid \[DM76\])**.** _Let M_<sub>1</sub> _and M_<sub>2</sub> _be strongly base-orderable matroids on the same ground set E. Then for any_ \(S\subseteq E\)_, S can be partitioned into k common independent sets of M_<sub>1</sub> _and M_<sub>2</sub> _if and only if S can be partitioned into k independent sets of M_<sub>1</sub> _and into k independent sets of M_<sub>2</sub>.

## 3 Matroid Packing and Matroid Covering

In this section, we present an algebraic framework for addressing _matroid intersection packing_ and _matroid covering_ problems in the general sensitivity setting as well as _subset_ sensitivity setting.

### 3.1 Sensitivity Oracle for Matroid Intersection Packing

Let _M_<sub>1</sub>=(_E,_I<sub>1</sub>) and _M_<sub>2</sub>=(_E,_I<sub>2</sub>) be two linear matroids of rank _r_ defined on a common ground set _E_ of size _m_, and let \(wt:E\rightarrow[-W,W]\) be a weight function. Given an integer _k_, the _decision version_ of the _k_-packing problem asks whether there exists a subset _S_ of _E_ such that _S_ can be partitioned into _k_ pairwise disjoint common bases of _M_<sub>1</sub> as well as _M_<sub>2</sub> (observe that the partitioning of _S_ may differ in the two cases). The _weighted version_ asks for the minimum total weight of such a _k_-packing-set _S_, provided one exists. We approach this problem by analyzing the intersection of the _k_-fold unions of _M_<sub>1</sub> and _M_<sub>2</sub>.

#### _k_-fold Matroid Union

Let _M_ be a linear matroid defined on a ground set _E_ of size _m_. Suppose _M_ has rank _r_ and is represented by a \(r\times m\) matrix _A_ over a finite field F. The _k_-fold union of _M_, denoted \(M^{\vee k}\), is a matroid whose independent sets are those subsets \(S\subseteq E\) that can be partitioned into _k_ disjoint sets \(S_1\unknown S_2\unknown\cdots\unknown S_k\) such that each _S<sub>i</sub>_ is an independent set in _M_. Note that the rank of \(M^{\vee k}\) may be much smaller than _kr_.

**Definition 3.1** (Randomized Union Representation)**.** _Let_ \(M^{\vee k}\) _be the k-fold union of a matroid M_=(_E,_I) _of rank r on m elements. A random matrix_ \(U\in\mathbb{F}^{kr\times m}\) _is a randomized union representation of_ \(M^{\vee k}\) _if it satisfies the following two properties:_

1. _If a set_ \(S\subseteq E\) _is independent in_ \(M^{\vee k}\)_, then U<sub>S</sub> has full column rank with probability at least_ \(1-\frac{1}{(kr)^{\Omega(1)}}\).<tbc>

_2._ _If a set_ \(S\subseteq E\) _is dependent in_ \(M^{\vee k}\)_, then U<sub>S</sub> does not have full column rank (this holds deterministically)._<tbc>

