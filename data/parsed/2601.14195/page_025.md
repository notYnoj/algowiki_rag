<tbc>ings.

**Claim 10.** _If B is satisfiable then there exists a matching M of I such that_ \(\mathrm{max}_{a_r\in A}|bp_{a_r}(M)|\le k\).

_Proof of Claim 10._ Let \(f:V\rightarrow\{T,F\}\) be a satisfying truth assignment of _B_ and consider the matching _M_ constructed as follows (starting from the empty set).

For every variable \(V_i\in V\) , if _f(V<sub>i</sub>_)=_T_ then, in the corresponding variable gadget _G<sub>V<sub>i</sub></sub>_, add \(\{v_i^T,v_i^1\}\) and \(\{v_i^F,v_i^2\}\) to _M_. If _f(V<sub>i</sub>_)=_F_ instead, then add \(\{v_i^T,v_i^2\}\) and \(\{v_i^F,v_i^1\}\) to _M_.

For every forcing gadget \(G_{F_{k+1}(v_i^z)}\) that was used in the construction of the variable gadgets, add \(\{f_{1,i}^{1,z},f_{1,i}^{2,z}\}\), \(\{f_{1,i}^{3,z},f_{1,i}^{4,z}\}\), \(\dots,\{f_{1,i}^{3^{k+1}-2,z},f_{1,i}^{3^{k+1}-1,z}\}\) to _M_.

For every clause \(C_j=(C_j^1\vee C_j^2\vee C_j^3)\) in _B_, pick one literal \(C_j^d\) such that either \(C_j^d\) is an unnegated variable _V<sub>s</sub>_ and _f(V<sub>s</sub>_)=_T_, or \(C_j^d\) is a negated variable \(\bar{V}_s\) and _f(V<sub>s</sub>_)=_F_ (i.e., \(C_j^d\) satisfies the clause _C<sub>j</sub>_; by the assumption that _B_ is satisfiable at least one such literal must exist in each clause). In the corresponding clause gadget _G<sub>C<sub>j</sub></sub>_, add \(\{x_j^{d-1},x_j^{d+1}\}\) (addition and subtraction taken modulo 3) to _M_ and leave \(x_j^d\) unmatched.

Match all agents \(\{u_\beta^1(x_j^z),u_\beta^2(x_j^z)\}\) for every \(1\le\beta\le k-1\), \(1\le j\le m\) and \(1\le z\le 3\). Furthermore, for every forcing gadget \(G_{F_{k+1}(u_\beta^2(x_j^s))}\) that is attached to an agent \(u_\beta^2(x_j^s)\), add \(\{f_{2,j}^{1,s,\beta},f_{2,j}^{2,s,\beta}\}\), \(\{f_{2,j}^{3,s,\beta},f_{2,j}^{4,s,\beta}\}\), \(\dots,\{f_{2,j}^{3^{k+1}-2,s,\beta},f_{2,j}^{3^{k+1}-1,s,\beta}\}\) to _M_. This completes the construction of _M_.

By our earlier discussions regarding the generalised forcing gadget, because each \(v_i^1\) and each \(v_i^2\) is matched to someone on \(P_{v_i^1}\) and \(P_{v_i^2}\) in _M_, respectively, no agent in any forcing gadget \(G_{F_{k+1}(v_i^z)}\) attached to one of these two agents is in more than _k_ blocking pairs.

By our previous Claim 2, within all variable gadgets where \(\{\{v_i^T,v_i^1\},\{v_i^F,v_i^2\}\}\subseteq M\), _M_ admits only the blocking pairs coming from the forcing gadgets. For those variable gadgets where, instead, it is the case that \(\{\{v_i^T,v_i^2\},\{v_i^F,v_i^1\}\}\subseteq M\), _M_ admits the blocking pair \(\{v_i^T,v_i^1\}\) in addition to the blocking pairs coming from the forcing gadgets (which cannot involve \(v_i^1\) and \(v_i^2\)). Either way, no agent is contained in more than _k_ blocking pairs within any variable gadget.

As shown in the proof of Claim 9, within each clause gadget (including the respective _A<sub>U</sub>_ and _A_<sub>_F_<sub>2</sub></sub> agents), _M_ is constructed such that no agent is contained in more than _k_ blocking pairs.

Hence, _M_ is a matching such that no agent from _I_ is contained in more than _k_ blocking pairs, i.e., \(\mathrm{max}_{a_r\in A}|bp_{a_r}(M)|\le k\) as required.

Now, let us prove the converse direction.

**Claim 11.** _If there exists a matching M of I such that_ \(\mathrm{max}_{a_r\in A}|bp_{a_r}(M)|\le k\)_, then B is satisfiable._

_Proof of Claim 11._ Suppose that there exists a matching _M_ of _I_ such that \(\mathrm{max}_{a_r\in A}|bp_{a_r}(M)|\le k\). We will construct a satisfying truth assignment \(f:V\rightarrow\{T,F\}\). By a simple extension of Claim 2, for every variable \(V_i\in V\) of _B_, it must be the case for the corresponding variable gadget that either \(\{\{v_i^T,v_i^1\},\{v_i^F,v_i^2\}\}\subseteq M\) or \(\{\{v_i^T,v_i^2\},\{v_i^F,v_i^1\}\}\subseteq M\) (and clearly not both because _M_ is a matching), since \(\mathrm{max}_{a_r\in A}|bp_{a_r}(M)|\le k\), and otherwise some agent in either \(G_{F_{k+1}(v_i^1)}\) or \(G_{F_{k+1}(v_i^1)}\) (for any \(1\le i\le n\)) must be in at least _k_+1 blocking pairs by construction. In the former case, set _f(V<sub>i</sub>_)=_T_ and, in the latter case, set _f(V<sub>i</sub>_)=_F_.

Clearly, _f_ is a truth assignment. Now to show that _f_ satisfies _B_, consider any clause \(C_j=(C_j^1\vee C_j^2\vee C_j^3)\) in _B_. Because \(\mathrm{max}_{a_r\in A}|bp_{a_r}(M)|\le k\), by Claim 9, it must be the case that, for at least one literal \(C_j^d\), agent \(v(x_j^d)\) must be matched to someone at least as good as \(x_j^d\); otherwise, no matter how the agents are matched, at least one agent must be in more than _k_ blocking pairs. However, we know that \(\{x_j^d,v(x_j^d)\}\notin M\), because we already argued above that<tbc>

