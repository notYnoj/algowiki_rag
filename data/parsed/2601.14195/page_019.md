Furthermore, for the forcing gadget \(G_{F(x_j^4)}\) attached to \(x_j^4\) in \(I'\), we can add \(\{f_j^1,f_j^2\}\), \(\{f_j^3,f_j^4\}\), \(\{f_j^5,f_j^6\}\) and \(\{f_j^7,f_j^8\}\) to \(M'\). Then \(|bp_{x_j^4}(M')|=0\). Doing this for every clause gadget establishes that \(max_{a_r\in A}|bp_{a_r}(M')|\le 1\).

Conversely, suppose that there exists a matching \(M'\) of \(I'\) where \(max_{a_r\in A}|bp_{a_r}(M')|\le 1\). Let \(M=M'\cap E\), where _E_ contains the edges in the acceptability graph of _I_, and let _M(a<sub>i</sub>_)=_a<sub>i</sub>_ for all agents of _I_ that are left unmatched in \(M'\cap E\). We claim that \(max_{a_r\in A}|bp_{a_r}(M)|\le 1\). Note that _M_ is clearly a matching of _I_. Furthermore, for every agent _a<sub>i</sub>_ in _I_, we have that \(M(a_i)=M'(a_i)\) if \(M'(a_i)\) is an agent in _I_ (i.e., \(M'(a_i)\neq x_j^4\) for some _j_) and \(\{a_i,M'(a_i)\}\) is acceptable in _I_, and _M(a<sub>i</sub>_)=_a<sub>i</sub>_ otherwise. Then \(bp_{a_i}(M)\subseteq bp_{a_i}(M')\), so \(max_{a_r\in A}|bp_{a_r}(M)|\le max_{a_r\in A}|bp_{a_r}(M')|\le 1\) as required.

This finishes the proof of 4.2 as the correspondence established in the claim above shows that _k_-Max-AlmostStable-sri is NP-hard even if _k_=1 and all preference lists are complete, and _k_-Max-AlmostStable-sri clearly remains in NP under these restrictions too.

This strong intractability highlights the computational limitations of enforcing individual- level stability guarantees in these multi-agent settings. Intractability of Minimax-AlmostStable- sri follows immediately, but we will state it again formally below. Note that a problem is para-NP-hard with respect to a parameter \(\kappa\) if it is NP-hard already for a constant value of \(\kappa\), and a problem is in XP with respect to \(\kappa\) if there exists an \(O(n^{f(\kappa)})\) algorithm. If a problem is para-NP-hard with respect to a parameter \(\kappa\), then it is not in XP with respect to \(\kappa\) unless P=NP (we refer to \[19\] for an introduction to parametrised complexity theory).

**Corollary 4.3.** _The problem_ Minimax-AlmostStable-sri _is_ para-NP-hard _with respect to parameter_ \(\kappa=min_{M\in\mathcal{M}}max_{a_i\in A}|bp_{a_i}(M)|\)_, regardless of whether preference lists are of bounded length at most 10 or whether preferences are complete._

_Proof._ This follows immediately from Theorems 4.1-4.2.

## 4.3 Hardness of Maximum Matchings in Bipartite Bounded-Degree Graphs

In a similar fashion to the previous subsection, the result below states that it is impossible to distinguish in polynomial time even between instances that admit a perfect matching in which every agent is in at most one blocking pair and instances where every perfect matching requires at least one agent to be in more than one blocking pair (unless P=NP).

**Theorem 4.4.** _k_-Max-AlmostStable-Perfect-smi _is_ NP-complete_, even if k_=1 _and all preference lists are of length at most 3._

_Proof._ First, note that membership of _k_-Max-AlmostStable-Perfect-smi in NP follows from the fact that, given a matching _M_, we can efficiently verify whether _M_ is perfect by checking that the size of _M_ is half the number of agents, and whether the maximum number of blocking pairs that any agent is a part of is at most _k_ by iterating through the preference lists.

We will show that _k_-Max-AlmostStable-Perfect-smi is NP-hard by reducing from the NP-complete problem (2,2)-e3-sat to 1-Max-AlmostStable-Perfect-smi. For the reduction itself, we use the same gadgets and leverage a central claim of Biró et al. \[10\] in their reduction from (2,2)-e3-sat to _k_-BP-AlmostStable-Perfect-smi. For completeness, we will outline their reduction below.

Let _B_ be a (2,2)-e3-sat instance with the variables _V_={_V_<sub>1</sub>_,V_<sub>2</sub>_,...,V<sub>n</sub>_} and the clauses _C_={_C_<sub>1</sub>_,C_<sub>2</sub>_,...,C<sub>m</sub>_}. We will construct an smi instance \(I=(A,\succ)\) from _B_, where the set of agents _A_ consists of the disjoint union of agents \(A_v=\{x_i^r,y_i^r;1\le i\le n\wedge 1\le r\le 4\}\) from the variable gadgets and \(A_c=\{c_j^s,p_j^s;1\le j\le m\wedge 1\le s\le 3\}\cup\{q_j,z_j;1\le j\le m\}\) from the clause gadgets. Altogether, |_A_|=8(_n+m_).

