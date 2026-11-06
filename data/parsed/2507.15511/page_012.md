## 5.2 Worst-Case Runtime via Controlled Aliasing

In addition to its adaptive performance, IC-SubsetSum guarantees a strict worst-case improvement over Horowitz-Sahni, even on collision-free instances. This is achieved via a deterministic _Controlled Aliasing_ rule: a structural redundancy technique that reduces the enumeration space without sacrificing correctness. We describe an enhanced version that ensures full correctness for both the _decision_ and _constructive_ variants of Subset-Sum.

### Aliasing Rule (distinct aliased values).

Let _S_ be split into halves \(\ell_0\) and \(\ell_1\). In each half, select a pair of distinct elements--an _alias pair_--e.g., \((x_0,x_1)\in\ell_0\). During enumeration we compute an _aliased_ value<tbc>

\(\tilde{\sigma}(P):=\sigma(P)-\chi(P)\cdot(x_1-x_0),\text{where}\chi(P):=\mathbf{1}[x_1\in P].\)

<tbc>Thus \(\tilde{\sigma}\) replaces _x_<sub>1</sub> by _x_<sub>0</sub> in the sum while preserving the subset’s bitmask identity, and the true sum is recovered by \(\sigma(P)=\tilde{\sigma}(P)+\chi(P)\cdot(x_1-x_0)\). This mapping collapses the four inclusion patterns on {_x_<sub>0</sub>_,x_<sub>1</sub>} into at most three _distinct aliased sums_ per base subset, so the number of distinct aliased sums per half is at most

\(\frac{3}{4}\cdot 2^k\text{for}k=|\ell_i|,\)

as shown in Lemma 8 (Appendix E). This is a _counting_ statement about values; the runtime bound will follow once we restrict which states are _expanded_ (CNF below).

### Canonical Aliasing via 2-Lane Memoization.

To preserve correctness under aliasing, we maintain, for each aliased value \(\tilde{\sigma}\), two canonical entries indexed by the correction tag \(\chi\in\{0,1\}\):

\(\mathsf{Memo}[\tilde{\sigma}]\in\big(\{\perp\}\cup\{0,1\}^n\big)^2.\)

Each bucket stores the lexicographically minimal witness for its \((\tilde{\sigma},\chi)\) key. The buckets are disjoint: a new prefix competes only within its \(\chi\)-bucket for lexicographic minimality, so all semantically distinct witnesses are retained.

### Aliased Canonical Normal Form (CNF).

Fix an alias pair (_x_<sub>0</sub>_,x_<sub>1</sub>) on indices (_i_<sub>0</sub>_,i_<sub>1</sub>) in each half. Define a normalization map

\(\mathsf{canon}(b):=\left\{\begin{array}{ c c }
b & \text{if}b[i_0]+b[i_1]\in\{0,2\}\text{or}(b[i_0],b[i_1])=(1,0), \\
b' & \text{if}(b[i_0],b[i_1])=(0,1),
\end{array}\right.\)

where \(b'\) is _b_ with the pair (_i_<sub>0</sub>_,i_<sub>1</sub>) flipped from (0,1) to (1,0). The algorithm explores only states with _b_=canon(_b_) (canonical states); non-canonical states may be stored as witnesses but are flagged non-expandable. This quotients the search space by the alias-induced redundancy and is scheduler-agnostic (FIFO/LIFO/priority).

### Expansion Policy (CNF, inlined).

Equivalently, write \(c(b):=b[i_0]+b[i_1]\in\{0,1,2\}\) and \(\chi(b):=b[i_1]\in\{0,1\}\). A newly discovered state with mask _b_ is enqueued for extension iff

\((c(b)=0)\vee(c(b)=2)\vee\big(c(b)=1\wedge\chi(b)=0\big).\)

States with \((c,\chi)=(1,1)\) are recorded in the appropriate bucket but _not_ expanded. This explicit policy yields the 3/4 expansion accounting and is target-independent.

