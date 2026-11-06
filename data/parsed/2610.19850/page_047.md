Each gadget is connected to _a_ and _b_. In Figure 17, the diamond green vertices represent the mandatory set _M_. Variable gadgets are thus made up of two mandatory vertices _a<sub>i</sub>_ and _b<sub>i</sub>_, and four other which can be used for extension: \(\alpha_i,\overline{\alpha_i},\beta_i,\overline{\beta_i}\). Observe that each variable gadget, attached with vertices _a_ and _b_, form a hypercube of dimension 3.

We complete variable gadgets by adding clause vertices. Each clause _C<sub>j</sub>_ is represented by a vertex in _M_ adjacent to _a_, and for every literals \(\ell_i\in\overline{C_j}\), we add an edge from _C<sub>j</sub>_ to \(\beta_i\) if \(\ell_i=x_i\), otherwise to \(\overline{\beta_i}\) if \(\ell_i=\overline{x_i}\). This graph can naturally be built in polynomial time since for a formula with _n_ variables and _m_ clauses, we need 6_n+m_+2 vertices and at most 12_n_+4_m_ edges.

To achieve the reduction, we show the following claim, which highlights a bijection between the truth assignments \(\sigma\) of \(\Phi\) and the minimal (_a,b_)-separators of \(G(\Phi)\) extending _M_.

_Claim_: The minimal (_a,b_)-separators of \(G(\Phi)\) containing _M_ are exactly the sets

\(S(\sigma)=M\cup\{T_i(\Phi,\sigma)\}_{1\le i\le n},\)

for all truth assignments \(\sigma\) of \(\Phi\), where \(T_i(\Phi,\sigma)=\{\alpha_i,\beta_i\}\) if \(\sigma(x_i)=\text{True}\), otherwise \(T_i(\Phi,\sigma)=\{\overline{\alpha_i},\overline{\beta_i}\}\). See Figure 18 for an example of \(S(\sigma)\).

**From 3-SAT to minimal** (_a,b_)**-separators.** Let \(\sigma\) be a truth assignment of \(\Phi\), where \(\sigma(x_i)\) takes value True or False. By definition of \(\sigma\), for every clause, there is at least one literal that makes this clause true. We show that \(S(\sigma)\), as defined above, is a minimal (_a,b_)- separator.

In any variable gadget, it is not possible to highlight an (_a,b_)-path which does not traverse _S_. Moreover, clause vertices belong to \(M\unknown S\). Hence, \(S(\sigma)\) is an (_a,b_)-separator. Let us prove its minimality: we must have \(N(C(a,S(\sigma)))=N(C(b,S(\sigma)))=S(\sigma)\). As respectively one vertex among \(\{\alpha_i,\overline{\alpha_i}\}\) and \(\{\beta_i,\overline{\beta_i}\}\) does not belong to _S_, then all vertices of \(S(\sigma)\) contained in variable gadgets can reach _a_ and _b_ despite \(S(\sigma)\). Concerning clause vertices (which belong to \(S(\sigma)\)), they are adjacent to _a_ but their adjacency towards \(C(b,S(\sigma))\) is ensured by the fact that \(\sigma\) is a truth assignment. Indeed, for each _C<sub>j</sub>_, there is at least one literal \(\ell_i\) from <o>_C<sub>j</sub>_</o> which is False: so, one vertex \(\beta_i\) or \(\overline{\beta_i}\) adjacent to _C<sub>j</sub>_ is not in the separator \(S(\sigma)\). Hence, any vertex _C<sub>j</sub>_ is adjacent to \(C(b,S(\sigma))\). This completes the proof that \(S(\sigma)\) is a minimal (_a,b_)-separator.

**From minimal** (_a,b_)**-separators to 3-SAT.** Consider a minimal (_a,b_)-separator _S_ such that \(M\unknown S\). Fix some arbitrary \(1\le i\le n\) and \(A_i=\{\alpha_i,\overline{\alpha_i},\beta_i,\overline{\beta_i}\}\). On one hand, we cannot<tbc>

b
Bi
bi
Bi
a
a
a
a

b
Bi
Bi
Cj
βk
a
a
a
a

(a) Variable gadget for _x<sub>i</sub>_ with its connection to _a_ and _b_.

(b) How clause vertices are connected to variable gadgets: example with \(C_j=x_i\vee\overline{x_k}\).

Figure 17: The variable gadgets and their links with clause vertices.

