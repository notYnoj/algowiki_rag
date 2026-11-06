<tbc>Intersection had a approximation ratio of 1/(_k_-1) \[27\].

We do mention that only unweighted problems were discussed before. Edmonds \[12\] (also in \[38\]) gives exact polynomial-time algorithms for Max-Weight 2-Matroid Intersection. For weighted MIS2P in linearly represented matroids \[7, 37\] give pseudopolynomial algorithms and approximation schemes, and Iwata and Kobayashi \[23\] gives a polynomial-time algorithm. Linhares, Olver, Swamy, and Zenklusen \[30\] gives a (1/2)-approximation for Max-Weight 3-Matroid Intersection.

## 2 Preliminaries

In the introduction, a matroid was defined as a polymatroid which has the additional condition that \(f(\{i\})\le 1\) for all \(i\in N\). An alternative definition is: A _matroid_ (defined in \[10, 38\]) is an ordered pair _M_=(_E,_I) satisfying the following conditions:

1. _E_ is a nonempty finite set.<tbc>

2. I is a nonempty family of subsets of _E_, called _independent_ subsets of _E_, such that if \(B\in\mathcal{I}\) and \(A\subseteq B\), then \(A\in\mathcal{I}\).<tbc>

3. If \(A\in\mathcal{I},B\in\mathcal{I}\), and |_A|\<|B_|, then there exists some element \(x\in B\backslash A\) such that \(A\cup\{x\}\in\mathcal{I}\).

To construct _M_=(_E,_I) from the polymatroid _f_, let _E=N_ and I be the sets that are defined as independent in the polymatroid _f_. It is known \[38\] and not hard to prove that the three conditions above hold, assuming that \(f(\{i\})\le 1\) for all \(i\in N\). To construct a polymatroid from the alternative definition above, for set \(A\subseteq E\), define the _rank_ function \(r(A)=\mathrm{max}_{B\subseteq A}\) and \(_{B\in\mathcal{I}}|B|\). This definition implies that \(A\in\mathcal{I}\) if and only if |_A_|=_r(A_). It is not hard to prove (see \[38\]) that _r_() is a monotone submodular function with \(r(\emptyset)=0\), and thus _r_ is a polymatroid. Also, \(r(\{i\})\le 1\) for all \(i\in E\).

Given a matroid _M_=(_E,_I), we say that \(A\in\mathcal{I}\) is a maximal independent subset of _M_, or a _basis_ of _M_ if there exists no \(x\in E\backslash A\) such that \(A\cup\{x\}\in\mathcal{I}\). It is known that all bases of a matroid have the same size. We will use:

**Theorem 2.1** (Theorem 3.3 of \[17\])**.** _Consider a matroid and let Q,P be two of its bases. Let X_<sub>1</sub>_,X_<sub>2</sub>_,...,X<sub>t</sub> be a partition of Q. Then there is a partition Y_<sub>1</sub>_,Y_<sub>2</sub>_,...,Y<sub>t</sub> of P such that for all i_=1,2_,...,t,_ \((Q\backslash X_i)\cup Y_i\) _is a basis._

Given matroid _M_=(_E,_I) and \(Z\subseteq E\), let _X_ be a maximal independent subset of _Z_. Let \(M/Z=(E',\mathcal{I}')\) where \(E'=E\backslash Z\) and \(\mathcal{I}'=\{A\subseteq E'\big|A\cup X\in\mathcal{I}\}\). We call _M/Z_ the _contraction_ of _M_ by set _Z_ (it is known and not hard to prove that the choice of _X_ does not matter). The rank function \(r'\) of _M/Z_ satisfies \(r'(Y)=r(Y\cup Z)-r(Z)\) (this is not hard to see, and appears in \[38\]).<tbc>

