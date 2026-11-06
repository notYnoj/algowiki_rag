of _k_-Max-AlmostStable-sri as follows. Let \(A=A_{F_1}\cup A_{F_2}\cup A_U\cup A_V\cup A_C\) be a set of 2_n_(3<sup>_k_+1</sup>+1)+_m_((_k_-1)3<sup>_k_+2</sup>+3_k_) agents, where

\(A_{F_1}=\{f_{1,i}^{\alpha,z};1\le i\le n\wedge 1\le\alpha\le 3^{k+1}-1\wedge 1\le z\le 2\},\)<br>
\(A_{F_2}=\{f_{2,j}^{\alpha,z,\beta};1\le j\le m\wedge 1\le\alpha\le 3^{k+1}-1\wedge 1\le z\le 3\wedge 1\le\beta\le k-1\},\)<br>
\(A_U=\{u_\beta^1(x_j^s),u_\beta^2(x_j^s);1\le j\le m\wedge 1\le s\le 3\wedge 1\le\beta\le k-1\},\)<br>
\(A_V=\{v_i^T,v_i^F,v_i^1,v_i^2;1\le i\le n\},\text{and}\)<br>
\(A_C=\{x_j^s;1\le j\le m\wedge 1\le s\le 3\}.\)

These disjoint sets of agents correspond to those from forcing gadgets attached to agents in the variable gadgets, forcing gadgets attached to agents in the clause gadgets, blocking-pair introducing gadgets in the clause gadgets, the variable gadgets, and the clause gadgets, respectively. Notice that, although the size of _I_ is exponential in _k_, it is polynomial in _n_ and _m_ (the size of _B_), and we treat _k_ as a fixed constant. Therefore, this is a polynomial-time reduction (in the size of _B_).

We start by constructing the variable and clause gadgets as in the proof of Theorem 4.1, but replacing the use of forcing gadgets _G_<sub>_F(a<sub>r</sub>_)</sub> in the variable gadgets with copies of _G_<sub>_F_<sub>_k_+1</sub>(_a<sub>r</sub>_)</sub> (the agents from these copies make up _A_<sub>_F_<sub>1</sub></sub>). We refer back to Figures 4-6 for the original constructions. Next, for every \(x_j^s\) agent in each clause gadget, we connect the 2(_k_-1) agents \(\{u_\beta^1(x_j^s),u_\beta^2(x_j^s)|1\le\beta\le k-1\}\) (which collectively make up _A<sub>U</sub>_) and transform \(x_j^s\)’s preference list from the original construction<tbc>

\(x_j^s:x_j^{s+1}x_j^{s-1}v(x_j^s)\)

<tbc>(where addition and subtraction is taken modulo 3) to a new preference list<tbc>

\(x_j^s:x_j^{s+1}x_j^{s-1}v(x_j^s)u_1^1(x_j^s)u_2^1(x_j^s)\dots u_{k-1}^1(x_j^s).\)

<tbc>We define the preferences of the \(u_\beta^1(x_j^s)\) and \(u_\beta^2(x_j^s)\) agents as follows:

\(u_\beta^1(x_j^s):x_j^su_\beta^2(x_j^s),\text{and}\)<br>
\(u_\beta^2(x_j^s):u_\beta^1(x_j^s).\)

Finally, we attach one copy of the \(G_{F_{k+1}(u_\beta^2(x_j^s))}\) gadget to each \(u_\beta^2(x_j^s)\) agent (the agents of these gadgets make up _A_<sub>_F_<sub>2</sub></sub>). The construction is illustrated in Figure 10.

Notice that Claim 3, which argued how agents in the clause gadget must be matched for the matching to have desirable properties, can be extended to this new construction as follows.

**Claim 9.** _Let_ \(G_{C_j}^*\) _be an occurrence of the clause gadget together with its attached agents in A<sub>U</sub> and A_<sub>_F_<sub>2</sub></sub><sup>4</sup>_, and let M be a matching of I. If it is true that_ \(max_{a_r\in A[G_{C_j}^*]}|bp_{a_r}(M)|\le k\)_, then there exists at least one_ \(x_j^d\) _in_ \(G_{C_j}^*\) _such that_ \(M(v(x_j^d))\unknown_{v(x_j^d)}x_j^d\)_. Conversely, if there exists at least one_ \(x_j^d\) _in_ \(G_{C_j}^*\) _such that_ \(M(v(x_j^d))\unknown_{v(x_j^d)}x_j^d\) _and, furthermore,_ \(\{x_j^{d-1},x_j^{d+1}\}\in M\) _(addition modulo 3), then the remaining agents in_ \(G_{C_j}^*\) _can be matched among each other such that_ \(max_{a_r\in A[G_{C_j}^*]}|bp_{a_r}(M)|\le k\).

_Proof of Claim 9._ For the first part of the statement, suppose that \(max_{a_r\in A[G_{C_j}^*]}|bp_{a_r}(M)|\le k\) and notice that, for at least one \(x_j^d\) agent in \(G_{C_j}^*\), it must be the case that \(v(x_j^d)\unknown_{x_j^d}M(x_j^d)\)<tbc>

<sup>4</sup>We use the <sup>∗</sup> notation to indicate that this is a generalised clause gadget compared to the construction in the proof of Theorem 4.1.

