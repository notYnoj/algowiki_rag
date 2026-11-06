Accordingly, define the critical independence difference of _G_ as

\(id_c(G)=max\{d(X):X\subseteq V,X\text{is independent}\}.\)

Every critical independent set _I_ satisfies _d(I_)=_id<sub>c</sub>(G_). The maximization allows the empty set, so \(d(\varnothing)=0\) implies \(id_c(G)\ge 0\).

Larson gave a polynomial-time algorithm for computing a maximum- cardinality critical independent set [11]. We use the independent set _I_ returned by this algorithm as the starting point for a case analysis based on its difference and cardinality, leading to a polynomial-time algorithm for small blocking set detection and construction.

## 3. Classification using critical independent sets

Compute a maximum-cardinality critical independent set _I_ and let

\(\delta=d(I)=id_c(G).\)

Since \(\delta\ge 0\), we consider the cases \(\delta>0\) and \(\delta=0\) separately.

### 3.1. Positive critical difference

We use the following result of Ayoubi and Narayanan. Here, a _blocking set_ is a nonempty independent set _S_ satisfying |_S_|=|_N(S_)|, without the strict cardinality requirement in Definition 1.

**Lemma 1** (Ayoubi and Narayanan [10, Lemma 5])**.** _If a nonempty independent set I in a connected graph satisfies_<tbc>

\(|I|\ge|N(I)|,\)

<tbc>_then deleting vertices one at a time constructs a blocking set_ \(S\subseteq I\) _satisfying_

\(|S|\le|N(I)|.\)

This immediately gives the required positive-difference branch.

**Corollary 1.** _If_ \(\delta>0\)_, a small blocking set can be constructed in polynomial time._

