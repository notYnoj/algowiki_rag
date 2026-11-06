### D.3 Summary

Across all knobs (density, duplicates, additive progressions), _U_ varies by orders of magnitude, and IC-SubsetSum’s wall-time tracks this variation closely. These measurements are consistent with the proven certificate-sensitive scaling--\(T=\Theta(U)\cdot\mathrm{poly}(n)\)--and illustrate that structural compressibility, not just _n_, governs practical difficulty. For reproducibility, we include generator seeds, configuration files, and raw logs in the artifact accompanying \[Sal25\].

## E Controlled Aliasing: Correctness and Implementation

**Preface.** Section 5.2 contains a self-contained summary of Controlled Aliasing (including the CNF expansion policy, the \(2\times 2\) compensatory merge, and Theorem 6). This appendix provides the full proofs and implementation details.<br>
**Navigation.** For ease of reading, the lemma names and labels in this appendix _match those cited in_ §5.2: Lemma 8 (state-space reduction), Lemma 6 (01\(\rightarrow\)10 shadowing), Lemma 7 (successor preservation), Lemma 9 (expansion accounting), Lemma 10 (policy safety), and the lane/merge lemmas (Lemmas 11-13).

To ensure correctness under value aliasing, we introduce a 2-lane memoization scheme keyed by an aliased sum and a 1-bit correction tag. Each reachable _aliased_ sum stores up to two canonical bitmasks, corresponding to whether the substituted element _x_<sub>1</sub> is absent or present in the true subset. This enables both decision and construction variants of Subset-Sum to be solved without error, even when synthetic collisions are introduced.

### Memoization Structure

Fix an alias pair (_x_<sub>0</sub>_,x_<sub>1</sub>) in a half \(\ell\) of size _k_ at positions (_i_<sub>0</sub>_,i_<sub>1</sub>) with \(x_0\neq x_1\). For a subset \(P\subseteq\ell\) with _local_ bitmask \(b\in\{0,1\}^k\), define the tag<tbc>

\(\chi(P):=\mathbf{1}[x_1\in P]=b[i_1],\)

<tbc>and the aliased value<tbc>

\(\tilde{\sigma}(P):=\sigma(P)-\chi(P)\cdot(x_1-x_0),\text{so that}\sigma(P)=\tilde{\sigma}(P)+\chi(P)\cdot(x_1-x_0).\)

<tbc>We maintain

\(\mathtt{Memo}:\mathbb{Z}\longrightarrow\left(\{\perp\}\cup\{0,1\}^k\right)^2,\mathtt{Memo}[\tilde{\sigma}][\chi]\in\{\perp\}\cup\{0,1\}^k,\)

storing, for each key \((\tilde{\sigma},\chi)\), the _lexicographically minimal_ witness bitmask (in the local index order of \(\ell\)).

### Canonical Normal Form (CNF).

Define the normalization map \(\mathtt{canon}:\{0,1\}^k\rightarrow\{0,1\}^k\) at the alias indices (_i_<sub>0</sub>_,i_<sub>1</sub>) by

\(\mathtt{canon}(b)=\left\{\begin{array}{ c c }
b, & \text{if}b[i_0]+b[i_1]\in\{0,2\}\text{or}(b[i_0],b[i_1])=(1,0), \\
b' & \text{if}(b[i_0],b[i_1])=(0,1),
\end{array}\right.\)

where \(b'\) is _b_ with the pair (_i_<sub>0</sub>_,i_<sub>1</sub>) flipped from (0,1) to (1,0). The enumerator _enqueues/expands only canonical states b_=`canon`(_b_); non-canonical states may still be stored in `Memo` for correctness but are flagged `doNotExtend` (non-expandable). This policy is scheduler- and target-independent.

