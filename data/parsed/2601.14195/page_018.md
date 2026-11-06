is \(v_i^1\). Thus, \(\{v(x_j^s),v_i^1\}\in M\), in which case literal \(C_j^s\) satisfies the clause, contradicting our assumptions about _C<sub>j</sub>_. Thus, there cannot exist any unsatisfied clause _C<sub>j</sub>_ with respect to truth assignment _f_, so _f_ is a satisfying truth assignment of _B_, i.e., _B_ is satisfiable as required.

Together, Claims 4-5 establish that 1-Max-AlmostStable-sri is NP-hard because (2,2)- e3-sat is NP-hard. This finishes the proof that _k_-Max-AlmostStable-sri is NP-complete. Finally, observe that, in our reduction, the agents \(v_i^z\) (where \(z\in\{1,2\}\)) connecting forcing and variable gadgets have the longest preference lists. Specifically, for each such \(v_i^z\), \(\text{length}(\succ_{v_i^z})=|(v_i^Tv_i^F)|+|(f_i^{1,z}f_i^{2,z}\dots f_i^{8,z})|=10\). This finishes the proof of Theorem 4.1.

We can also extend this intractability result to complete preference lists.

**Theorem 4.2.** _k_-Max-AlmostStable-sri _is_ NP-complete_, even if k_=1 _and all preference lists are complete._

_Proof._ To show this, we will modify the clause gadget in the reduction given in the proof of Theorem 4.1 slightly. Let _I_ be the sri instance constructed in the previous reduction, and let \(I'=(A',\succ')\) be a copy of _I_ that we will modify. For each clause gadget _G<sub>C<sub>j</sub></sub>_ in _I_, we introduce one additional agent \(x_j^4\) to the respective clause gadget \(G'_{C_j}\) in \(I'\) and append it to the end of the preference lists of each agent \(x_j^1,x_j^2\) and \(x_j^3\) (i.e., in the fourth position of their preference lists). Agent \(x_j^4\) shall rank the other agents \(x_j^1,x_j^2\) and \(x_j^3\) of \(G'_{C_j}\) in arbitrary order, followed by the attachment of a forcing gadget \(G_{F(x_j^4)}\) contributing eight additional agents \(\{f_j^1,f_j^2,\dots,f_j^8\}\). Specifically,<tbc>

\(x_j^4:x_j^1x_j^2x_j^3G_{F(x_j^4)}\)

<tbc>A visual example of the gadget construction is shown in Figure 7.

We can now complete all preference lists of all agents in the instance by appending all previously unranked agents in arbitrary order to the end of the preference lists. The resulting instance \(I'\), constructed from an original Boolean formula _B_ with _n_ variables and _m_ clauses, consists of \(|A'|=20n+12m\) agents. We now extend the main reduction argument as follows.

**Claim 6.** _There exists a matching M of I such that_ \(max_{a_r\in A}|bp_{a_r}(M)|\le 1\) _if and only if there exists a matching_ \(M'\) _of_ \(I'\) _such that_ \(max_{a_r\in A}|bp_{a_r}(M')|\le 1\).

_Proof of Claim 6._ First, suppose that there exists a matching _M_ of _I_ with \(max_{a_r\in A}|bp_{a_r}(M)|\le 1\). To start, let \(M'=M\). We have shown in the proof of Theorem 4.1 that, except for agents in clause gadgets, every other agent is matched in _M_. Furthermore, we showed that for every clause gadget _G<sub>C<sub>j</sub></sub>_, there exists at least one agent \(x_j^s\) such that \(M(x_j^s)=x_j^s\). If there exists exactly one such agent in _G<sub>C<sub>j</sub></sub>_, then we can update \(M'\) such that \(M'(x_j^s)=x_j^4\). If all agents in the clause gadget are unmatched in _M_ instead, then we can match \(M'(x_j^1)=x_j^2\) and \(M'(x_j^3)=x_j^4\), for example. In either case, for every agent \(x_j^l\) in _G<sub>C<sub>j</sub></sub>_, it is the case that \(|bp_{x_j^l}(M')|\le|bp_{x_j^l}(M)|\).<tbc>

3
1
2
1
2
4
1
4
3
1
2
1
4
2
4
2
4
2
x
j
j

Figure 7: Illustration of the modified clause gadget construction

