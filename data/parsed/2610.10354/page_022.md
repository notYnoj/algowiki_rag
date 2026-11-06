**Theorem 4.1** (Low-Rank 3SUM)**.** _For every_ \(0<\rho\le 1/2\) _there is some_ \(\delta=\delta(\rho)>0\) _such that the following holds. There is a randomized algorithm that solves a given All-Integer 3SUM instance_ (_A,B,C), when additionally provided with a set_ \(X\subseteq\mathbb{Z}\) _of size_ \(|X|\le n^{1-\rho}\) _satisfying_ \(A\subseteq X+X\)_, and runs in time_

\(3SUM(n|r\le n^{1-\rho})=O(n^{2-\delta}).\)

We will prove Theorem 4.1 by a sequence of two reduction steps to reduce from any given low- rank instance to few instances exhibiting even more structure. That structure is that the sets _A,B,C_ are all contained in some larger set _H_ with small doubling. For ease of notation we will typically refer to _H_ as a _low-doubling container_, formally defined as follows.

**Definition 4.2** (Low-Doubling Container)**.** We say that _H_ is a (_K,N)-container_ of some set _A_ if

• \(A\subseteq H\),<tbc>

• \(|H+H|\le K|H|\), and<tbc>

• \(|H|\le N\).

Our reduction can then be phrased as follows:

**Lemma 4.3** (From Low Rank to Low-Doubling Containment)**.** _For every_ \(\epsilon>0\) _and_ \(0<\rho\le 1/2\) _there is some_ \(\delta=\delta(\rho,\epsilon)>0\) _such that the following holds. There is a randomized algorithm that, given a 3SUM instance_ (_A,B,C_) _and a set X of size_ \(|X|\le n^{1-\rho}\) _such that_ \(C\subseteq X+X\)_, computes_

• \(O(n^\epsilon)\) _subinstances_ \((A'\subseteq A,B'\subseteq B,C'\subseteq C)\)_, each provided with a_ \((O(n^\epsilon),O(n^{2-2\rho}))\)_-container of_ \(A'\cup B'\cup C'\)_, and_

• _a set of 3SUM solutions_ \(\mathcal{T}\subseteq A\times B\times C\),

_so that each solution is either part of exactly one subinstance or part of_ T _. The algorithm runs in time_ \(O(n^{2-\delta})\).

We devote the following two subsections to the proof of Lemma 4.3. Once established, the proof of Theorem 4.1 is almost immediate by the following simple lemma.

**Lemma 4.4** (3SUM for Small Sumsets)**.** _Any All-Integer 3SUM instance_ (_A,B,C_) _with universe_ \[_u_\] _can be solved in deterministic time_ (|_A+B_|+|_B-C_|+|_A-C_|)(log_u_)<sup>_O_(1)</sup>.

**Proof.** To detect all elements in _C_ that are part of a solution, we compute the sumset _A+B_ by a sparse convolution in time |_A+B_|(log_u_)<sup>_O_(1)</sup> by Lemma 2.2, and report all elements in \(C\cap(A+B)\). To detect all elements in _A_ and _B_ that are part of a solution, we proceed similarly with _A_ and _B_ in place of _C_.

**Proof of Theorem 4.1.** Let \(\epsilon>0\) be a parameter to be determined. We apply Lemma 4.3 to the given instance (_A,B,C_) (by relabeling the input sets, we may assume _C_ has a low-doubling container as required by Lemma 4.3), and obtain \(O(n^\epsilon)\) subinstances \((A',B',C')\) and some set of 3SUM solutions T , with the promise that each solution in (_A,B,C_) either appears in a subinstance or in T . We report all items present in T . Then we solve all subinstances by Lemma 4.4, and further report all items that appear in a solution in at least one subinstance. The correctness is clear.

