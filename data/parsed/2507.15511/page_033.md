\(s_L\leftarrow\text{CorrectedSum}(\tilde{\sigma}_L,\chi_L,x_0,x_1)\)<br>
\(s_R\leftarrow t-s_L\)<br>
\(\text{\textbf{for}}\chi_R\in\{0,1\}\text{\textbf{do}}\)<br>
\(\tilde{\sigma}_R\leftarrow\text{AliasedValue}(s_R,\chi_R,y_0,y_1)\)<br>
\(\text{\textbf{if}}\tilde{\sigma}_R\in\text{\texttt{MemoRight then}}\)<br>
\(b_R\leftarrow\text{\texttt{MemoRight}}[\tilde{\sigma}_R][\chi_R]\)<br>
\(\text{\textbf{if}}b_R\neq\perp\text{\textbf{then}}\)<br>
\(\text{\textbf{return}}b_L\|b_R\triangleright\) concatenate local masks into the global mask<br>
**return** None

## Complexity Summary

• Each reachable aliased sum stores up to two bitmasks (one per \(\chi\in\{0,1\}\)).<tbc>

• All probes are _O_(1) expected time with hashing; lex-compare occurs only on true collisions.<tbc>

• Under the expansion policy, the number of _expanded_ states per half is at most \(\frac{3}{4}\cdot 2^k\) (Lemma 9); this drives the worst-case runtime accounting.<tbc>

• Time/space per half: \(O(E\cdot n^2)\) deterministic or \(O(E\cdot n)\) randomized, with \(E\le\frac{3}{4}\cdot 2^k\); storage \(O(U'\cdot n)\) where \(U'\) is the aliased-sum count.

## Correctness of Controlled Aliasing: Lemma Chain

### Setup and notation.

Fix one half \(\ell\) (let \(k:=|\ell|\)) and its alias pair (_x_<sub>0</sub>_,x_<sub>1</sub>) at positions (_i_<sub>0</sub>_,i_<sub>1</sub>) with \(x_0\neq x_1\). For any subset \(P\subseteq\ell\) with local bitmask \(b\in\{0,1\}^k\), write \(\chi(P):=b[i_1]\in\{0,1\}\). Let \(\sigma(P)\) denote the true sum and \(\tilde{\sigma}(P)\) the aliased sum. For a reachable value \(\tau\), the table stores a 2-tuple \(Memo[\tau]\in(\{\perp\}\cup\{0,1\}^k)^2\), with the lex-minimal bitmask in bucket \(\chi\) if any.

_Lemma_ 11 (Lane Invariant)_. For every subset_ \(P\subseteq\ell\)_, the pair_ \((\tilde{\sigma}(P),\chi(P))\) _identifies a unique bucket in the memoization table. During enumeration, the algorithm maintains for each fixed_ \((\tau,\chi)\) _the lexicographically minimal bitmask among all P with_ \(\tilde{\sigma}(P)=\tau\) _and_ \(\chi(P)=\chi\).

_Proof._ \(\chi\) depends only on the inclusion bit at _i_<sub>1</sub>, partitioning subsets into two classes. The update rule keeps, for each \((\tilde{\sigma},\chi)\), the lex-minimal witness under the total order \(\prec\).

_Lemma_ 12 (Soundness of Compensatory Merge)_. If the merge routine returns a witness_ \(W=W_L\cup W_R\) _(with_ \(W_L\subseteq\ell_0\) _and_ \(W_R\subseteq\ell_1\)_), then_ \(\sigma(W_L)+\sigma(W_R)=t\).

_Proof._ The merge checks the four corrected equalities

\(\tilde{\sigma}(W_L)+\tilde{\sigma}(W_R)+\chi_R(y_1-y_0)+\chi_L(x_1-x_0)=t\)

for all \(\chi_L,\chi_R\in\{0,1\}\). As \(\sigma(\cdot)=\tilde{\sigma}(\cdot)+\chi(\cdot)\cdot(\cdot)\), any returned witness satisfies \(\sigma(W_L)+\sigma(W_R)=t\).

_Lemma_ 13 (Completeness of Compensatory Merge)_. If there exists a solution_ \(W=W_L\cup W_R\)_, then the merge routine will find and return a valid witness._

_Proof._ For a valid solution, the two halves appear in buckets \((\tilde{\sigma}(W_L),\chi(W_L))\) and \((\tilde{\sigma}(W_R),\chi(W_R))\) by the Lane Invariant. The merge enumerates these tag pairs and restores true sums, so the corresponding check succeeds.

