The preference list entries that we previously left to be specified are completed as follows: let \(C_j^s\) correspond to the _s_th literal in _C<sub>j</sub>_ (\(1\le j\le m,1\le s\le 3\)), which is either an unnegated or a negated occurrence of some variable _V<sub>i</sub>_. If, processing _B_ from left to right, \(c_j^s\) is the

• first unnegated occurrence of _V<sub>i</sub>_, then let \(x(c_j^s)=x_i^1\) and let \(c(x_i^1)=c_j^s\);<tbc>

• second unnegated occurrence of _V<sub>i</sub>_, then let \(x(c_j^s)=x_i^2\) and let \(c(x_i^2)=c_j^s\);<tbc>

• first negated occurrence of _V<sub>i</sub>_, then let \(x(c_j^s)=x_i^3\) and let \(c(x_i^3)=c_j^s\);<tbc>

• second negated occurrence of _V<sub>i</sub>_, then let \(x(c_j^s)=x_i^4\) and let \(c(x_i^4)=c_j^s\).

We also refer to these connections as the communication edges between variable and clause gadgets.

Recall that this construction is the same as given by Biró et al. \[10\]. The authors proved the following correspondence between satisfiability and blocking pairs.

**Claim 7** (\[10\])**.** _B is satisfiable if and only if I admits a perfect matching M such that_ \(|bp(M)|\le n+m\).

Now recall that we already pointed out the structure of perfect matchings in the clause and variable gadgets, none of which can involve a communication edge. Furthermore, we noted the necessary blocking pairs incurred from each of the possible matchings. Specifically, we pointed out that every perfect matching must incur at least one blocking pair within each clause and within each variable gadget. Hence, for any perfect matching _M_ of _I_, \(|bp(M)|\ge n+m\) by construction. In particular, notice that if _I_ admits a perfect matching _M_ with at most _n+m_ blocking pairs, then no communication edge is blocking _M_. Observe that, in this case, \(max_{a_r\in A}|bp_{a_r}(M)|\le 1\). Hence, if _B_ is satisfiable, then _I_ admits a perfect matching _M_ with \(max_{a_r\in A}|bp_{a_r}(M)|\le 1\).

Now, conversely, suppose that _I_ admits a perfect matching _M_ with \(max_{a_r\in A}|bp_{a_r}(M)|\le 1\). Then, because _M_ is a perfect matching, within every _G<sub>C<sub>j</sub></sub>_ gadget there exists exactly one \(c_j^s\) agent who is matched to agent _q<sub>j</sub>_, and every other agent \(c_j^{s^\prime}\) (for \(s\neq s'\)) is matched to \(p_j^{s^\prime}\). Clearly no _q<sub>j</sub>_ and no _z<sub>j</sub>_ agent is part of a blocking pair of _M_. Thus, notice that |_bp(M_)|_\>n+m_ only if some communication edge is blocking. However, \(p_j^{s^\prime}\) is the first choice of \(c_j^{s^\prime}\), so \(c_j^{s^\prime}\) does not block with their communication edge. Furthermore, \(c_j^s\) does block with \(p_j^s\) by construction, but we assume that \(max_{a_r\in A}|bp_{a_r}(M)|\le 1\), so \(c_j^s\) cannot block with their communication edge. Hence, no communication edge is blocking, in which case \(|bp(M)|\le n+m\), in which case _B_ is satisfiable as Biró et al. \[10\] proved.

Therefore, we have also established the following claim.

1
2
1
2
1
3
1
1
1
1
2
2
1
2
2
2
2
2
2
2
2
2
2
3
3
3
3
3
3
3
3
3
3
3
3
3
3
3
2
2
2
2
1
1

Figure 9: Illustration of the clause gadget construction

