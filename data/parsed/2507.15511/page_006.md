## Instance Complexity (IC).

Orponen-Ko-Schöning-Watanabe Instance Complexity \[OKSW94\] formalises the idea that hard problems can have easy instances--even without randomization or approximation. The IC of an instance _x_ under time bound _t_ is defined as the bit-length of the shortest program _P_ that outputs the correct answer on _x_ within time _t_. It is denoted IC_<sub>t</sub>(x_).

For Subset-Sum, the list \(\Sigma(S)\) plays a dual role. It is not only a certificate but also a low- complexity proxy for a correct decision procedure. Once \(\Sigma(S)\) is known, any target _t_ can be resolved in time _O_(1) via a membership query. Hence, \(\Sigma(S)\) encodes a special-case program of length \(O(Ulog(n\cdot max(S)))\), yielding a concrete upper bound on IC_<sub>t</sub>_((_S,t_)). When the goal is to construct a solution, the richer certificate consisting of \((\sigma,bitmask)\) pairs provides a special-case program of length \(O(U\cdot n)\). For a formal IC program that satisfies partial correctness on _all_ inputs, we pair \(\Sigma(S)\) with an input-checking wrapper; see §4.3.

## Operational Parameters for Halves.

When _S_ is split into two halves \(\ell_0,\ell_1\) (sizes within \(\pm 1\)), we write \(U_0:=|\Sigma(\ell_0)|\), \(U_1:=|\Sigma(\ell_1)|\), and \(\widehat{U}:=max\{U_0,U_1\}\). When we state bounds that scale with _U_, we refer to full enumeration of \(\Sigma(S)\); for meet-in-the-middle solvers operating on halves, the governing parameter is \(\widehat{U}\).

## Controlled Aliasing Convention.

In the _Controlled Aliasing_ rule, each half designates an _arbitrary_ ordered pair (_x_<sub>0</sub>_,x_<sub>1</sub>) of distinct elements at indices (_i_<sub>0</sub>_,i_<sub>1</sub>) and treats occurrences of _x_<sub>1</sub> as _x_<sub>0</sub> during subset-sum generation for that half. We will key memo entries by a 2-lane identifier \((\tilde{\sigma},\chi)\), where \(\tilde{\sigma}\) is the aliased sum and \(\chi\in\{0,1\}\) records whether _x_<sub>1</sub> is present; witness selection remains lexicographic within each lane. Unless otherwise stated, the choice of alias pairs is independent of the target _t_ (and of any randomness), and all guarantees hold for _all_ targets _t_.

_Count-based canonical normal form (CNF)._ We restrict expansions to canonical aliased states using a fixed, target-independent policy: for a bitmask _b_, let \(c(b):=b[i_0]+b[i_1]\in\{0,1,2\}\) and \(\chi(b):=b[i_1]\in\{0,1\}\). A newly discovered state with mask _b_ is enqueued for extension iff

\((c(b)=0)\vee(c(b)=2)\vee\big(c(b)=1\wedge\chi(b)=0\big).\)

This CNF policy preserves completeness and enables the 3/4 expansion accounting; see §5.2 and App. E (Lemmas 9-10).

## Trivial and Degenerate Cases.

Instances with _n_=0 or _t_=0 are handled in _O_(1) time. If _U_=1 (e.g., all subset sums collide), enumeration and decision terminate immediately. Duplicates in _S_ are handled natively by our canonical memoization and require no additional promises.

## Instance Assumptions.

We consider the Subset Sum problem over a multiset _S_={_a_<sub>1</sub>_,...,a<sub>n</sub>_} of nonnegative integers \((a_i\in\mathbb{Z}_{\ge 0})\) and an integer target \(t\ge 0\). Elements are not required to be distinct; duplicates are treated as separate items. We assume without loss of generality that \(n\ge 1\) and that \(t\le\sum_{a\in S}a\) (instances with _t\<_0 or \(t>\sum S\) are decided trivially). Zero-valued elements may appear and are processed without special handling. While they do not generate new sum values (leaving \(U=|\Sigma(S)|\) unchanged), they can introduce additional witness subsets for existing sums. The algorithm’s correctness is unaffected, as its canonicalization logic correctly identifies the lexicographically minimal witness in all cases. Even if _t_=0, our algorithms enumerate the full constructive certificate for \(\Sigma(S)\), including the canonical witness for every achievable sum, unless the run is terminated early. All algorithms operate under the Word-RAM model described above, with \(w=\Theta(logM)\) where \(M:=max\{\sum_{a\in S}a,t\}\).

