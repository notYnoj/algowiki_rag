where we will specify the \(x(c_j^s)\) entries later. Figure 2 illustrates this construction. Importantly, a _G<sub>C<sub>j</sub></sub>_ gadget admits the following three perfect matchings:

\(M_{C_j}^1=\{\{c_j^1,q_j\},\{c_j^2,p_j^2\},\{c_j^3,p_j^3\},\{p_j^1,z_j\}\},\)<br>
\(M_{C_j}^2=\{\{c_j^1,p_j^1\},\{c_j^2,q_j\},\{c_j^3,p_j^3\},\{p_j^2,z_j\}\},\text{and}\)<br>
\(M_{C_j}^3=\{\{c_j^1,p_j^1\},\{c_j^2,p_j^2\},\{c_j^3,q_j\},\{p_j^3,z_j\}\}.\)

Notice that \(bp(M_{C_j}^1)\cap\mathbb{P}_2(A_c)=\varnothing\), \(bp(M_{C_j}^2)\cap\mathbb{P}_2(A_c)=\{\{p_j^s,z_j\}\}\), and \(bp(M_{C_j}^3)\cap\mathbb{P}_2(A_c)=\{\{p_j^1,z_j\},\{p_j^2,z_j\}\}\). Intuitively, \(M_{C_j}^1,M_{C_j}^2\) and \(M_{C_j}^3\) correspond to the first, second, and third literals of _C<sub>j</sub>_ being true, respectively.

We now connect the gadgets in the following way: let \(C_j^s\) correspond to the _s_th literal in _C<sub>j</sub>_ (for \(1\le j\le m,1\le s\le 3\)), which is either an unnegated or a negated occurrence of variable _V<sub>i</sub>_. Assuming that _B_ is read sequentially, if \(C_j^s\) is the

• first unnegated occurrence of _V<sub>i</sub>_, then let \(x(c_j^s)=x_i^1\) and let \(c(x_i^1)=c_j^s\);<tbc>

• second unnegated occurrence of _V<sub>i</sub>_, then let \(x(c_j^s)=x_i^2\) and let \(c(x_i^2)=c_j^s\);<tbc>

• first negated occurrence of _V<sub>i</sub>_, then let \(x(c_j^s)=x_i^3\) and let \(c(x_i^3)=c_j^s\);<tbc>

• second negated occurrence of _V<sub>i</sub>_, then let \(x(c_j^s)=x_i^4\) and let \(c(x_i^4)=c_j^s\).

Now we define the set of deviators to be the \(c_j^s\) agents, i.e., \(D=\{c_j^s;1\le j\le m\wedge 1\le s\le 3\}\), and prove the following claim.

**Claim 1.** _B is satisfiable if and only if I admits a perfect matching M such that no agent in D is in a blocking pair._

_Proof of Claim 1._ First, suppose that _B_ is satisfiable and that _f_ is a satisfying truth assignment. We define a complete matching _M_ in _I_ as follows. For each variable \(V_i\in V\) , if _f(V<sub>i</sub>_) is true, then add \(M_{V_i}^1\) to _M_, otherwise add \(M_{V_i}^2\) to _M_. For each clause \(C_j\in C\), there must exist at least one literal that is true under _f_ by assumption. Let this be \(C_j^s\) (if multiple literals satisfy _C<sub>j</sub>_, pick an arbitrary true literal of _C<sub>j</sub>_). Then we add \(M_{C_j}^s\) to _M_. Clearly, at the conclusion of this process, _M_ is a perfect matching, as we include one perfect matching within each gadget in _M_. Now it is straightforward to see that no agent in _D_ is blocking. We already noted that there can be no blocking pair involving an agent in _D_ within the clause gadgets. Now consider any pair \(\{c_j^s,x(c_j^s)\}\) for \(1\le j\le m\) and \(1\le s\le 3\). If \(C_j^s\) is the chosen satisfying literal in _C<sub>j</sub>_, then \(x(c_j^s)\) is matched to their first choice in _M_, so they cannot block with \(c_j^s\). Otherwise, if \(C_j^s\)<tbc>

