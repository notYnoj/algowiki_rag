each \(v(x_j^d)\) is matched to either \(v_i^1\) (where _V<sub>i</sub>_ is the variable such that either \(C_j^d=V_i\) or \(C_j^d=\bar{V}_i\)) or \(v_i^2\). Because \(v(x_j^d)\) prefers \(x_j^d\) to \(v_i^2\) (again, where _V<sub>i</sub>_ is the variable such that either \(C_j^d=V_i\) or \(C_j^d=\bar{V}_i\)), the only better options than \(x_j^d\) on \(\succ_{v(x_j^d)}\) are \(v_i^1\) and possibly the first occurrence of the literal at \(x_1(v(x_j^d))\) (if \(C_j^d\) corresponds to the second occurrence of the variable, i.e., \(x_j^d=x_2(v(x_j^d))\)). However, due to the forcing gadgets on the variable agents, \(\{v(x_j^d),x_1(v(x_j^d))\}\) cannot be in the matching without causing at least one agent to be in at least _k_+1 blocking pairs, so the only possible match for \(v(x_j^d)\) better than \(x_j^d\) is \(v_i^1\). Thus, if \(v(x_j^d)=v_i^T\) (for some \(1\le i\le n\)), then \(\{v_i^T,v_i^1\}\in M\), in which case we must also have \(\{v_i^F,v_i^2\}\in M\) (as otherwise \(v_i^2\) is not matched to an agent on \(P_{v_i^2}\), which results in too many blocking pairs as argued above), and if \(v(x_j^d)=v_i^F\) (for some \(1\le i\le n\)), then \(\{v_i^F,v_i^1\}\in M\), in which case we must also have \(\{v_i^T,v_i^2\}\in M\). In the former case, we defined _f(V<sub>i</sub>_)=_T_, and in the latter case we defined _f(V<sub>i</sub>_)=_F_, so either way the literal \(C_j^d\) satisfies the clause _C<sub>j</sub>_. Thus, there cannot exist any unsatisfied clause _C<sub>j</sub>_ with respect to truth assignment _f_, so _f_ is a satisfying truth assignment of _B_, i.e., _B_ is satisfiable as required.

Together, Claims 10-11 establish that _k_-Max-AlmostStable-sri is NP-hard. This finishes the proof of Theorem 4.6.

We can also extend our reduction from Theorem 4.4 for _k_-Max-AlmostStable-Max-smi to any positive integer _k_.

**Theorem 4.7.** _k_-Max-AlmostStable-Max-smi _is_ NP-complete _for any fixed positive integer k._

_Proof._ Let _k_ be fixed. In the proof of Theorem 4.4, we already noted that _k_-Max-AlmostStable- sri is in NP. To show that the problem is NP-hard, we start with the construction of smi instance \(I=(A,\succ)\) from the proof of Theorem 4.4. Now, we will modify this construction to an smi instance \(J=(A^J,\succ^J)\). We will use a similar approach as in the proof of Theorem 4.6 to force agents in clause gadgets to have a higher number of blocking pairs when they are not matched to their first choice. For every \(c_j^s\) agent in each clause gadget, we introduce 2(_k_-1) additional agents \(U=\{u_\alpha^1(c_j^s),u_\alpha^2(c_j^s)|1\le\alpha\le k-1\}\) and transform \(c_j^s\)’s preference list from the original construction<tbc>

\(c_j^s:p_j^sx(c_j^s)q_j\)

<tbc>to a new construction<tbc>

\(c_j^s:p_j^sx(c_j^s)u_1^1(c_j^s)u_2^1(c_j^s)\dots u_{k-1}^1(c_j^s)q_j\)

<tbc>We also define the preferences of the \(u_\alpha^1(c_j^s)\) and \(u_\alpha^2(c_j^s)\) agents as follows:

\(u_\alpha^1(c_j^s):c_j^su_\alpha^2(c_j^s),\text{and}\)<br>
\(u_\alpha^2(c_j^s):u_\alpha^1(c_j^s).\)

The construction is illustrated in Figure 11.

Notice that now the size of _A<sup>J</sup>_ increases from the original 8(_n+m_) agents (where _n_ is the number of variables and _m_ is the number of clauses) to 8_n_+2_m_(1+3_k_) agents, which is still polynomial in the size of the (2,2)-e3-sat instance _B_ that we originally reduce from (in the construction of _I_).

Furthermore, we know from our previous reduction that _I_ admits perfect matchings. Hence, by inspection of our modification above, the modified instance _J_ admits perfect matchings, and, for every such matching \(M\in\mathcal{M}^p(J)\), we must have \(\{u_\alpha^1(c_j^s),u_\alpha^2(c_j^s)\}\in M\) for all \(c_j^s\) and for all \(\alpha\). Hence, our modification introduces no new flexibility with regard to the perfect matchings. Also, note that, for every \(M\in\mathcal{M}^p(J)\), we must have exactly one \(c_j^s\) agent matched to _q<sub>j</sub>_ in<tbc>

