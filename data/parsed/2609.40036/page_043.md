**Conjecture 1** (Cycle-entropy transition)**.** _For every fixed_ \(D\ge 3\)_, finite field_ F_<sub>q</sub>, and_ \(c\in(0,1)\), \(\overline{\Phi_n}(p)\) _for Definition 4 converges for_ 0_\<p\<(q_-1)_/q to a function_ \(\Phi_{D,q,c}(p)\)_. Define_

\(\delta_\text{ent}(D,q)=inf\{p\in(0,(q-1)/q):\Phi_{D,q,c}(p)>0\}.\) (200)

_Then, with_

\(\delta_*=\delta_\text{rel}(D,q)=min\{\delta_\text{cyc}(D,q),\delta_\text{ent}(D,q)\},\) (201)

\(\unknown_GP_\text{S}^\text{ML}(G,p)\rightarrow\left\{\begin{array}{ c c }
1, & 0<p<\delta_*, \\
0, & \delta_*<p<(q-1)/q.
\end{array}\right.\) (202)

_No assertion is made at_ \(p=\delta_*\).

## Appendix B Proof of the LP-decoding guarantee

This appendix proves Theorem 6 using the direct LP formulation in (81). The final subsection gives the more compact formulation announced in §3.3.

Let _G_=(_V,E_) be the underlying simple graph, with _m_=|_E_|. Write _H=B<sup>T</sup>_ and take _h<sub>ve</sub>_ to denote the entry of the matrix _H_ indexed by vertex _v_ and edge _e_. Each edge represents a symbol in the codeword, and each vertex represents a parity check. If _e_={_u,v_}, then column _e_ has nonzero entries in rows _u_ and _v_ and zeros in all other rows. For each vertex _v_, write

\(\partial v=\{e\in E:h_{ve}\neq 0\},d_v=|\partial v|.\) (203)

Thus \(\partial v\) is the support of the parity check at _v_, or equivalently the set of edges that have _v_ as an endpoint. A symbol string \(\mathbf{b}\in\unknown_q^E\) has syndrome **s** precisely when

\(\sum_{e\in\partial v}h_{ve}b_e=s_v\text{for every}v\in V.\) (204)

Although Theorem 6 is stated for homological cycle codes, the proof below applies to arbitrary cycle codes ker_H_ over F_<sub>q</sub>_ with the column supports just specified. We do not require _h<sub>ue</sub>+h<sub>ve</sub>_=0 for _e_={_u,v_}. Consequently, the certified rate in Corollary 2 also applies to nonhomological cycle codes whose underlying graphs belong to the Linial-Simkin ensemble.

For fixed maximum degree _D_, the direct LP already has polynomial size in _n_=|_V_|, _m_, and _q_: each nonempty check involves at most _D_ symbols and has at most _q_<sup>_D_-1</sup> satisfying assignments. The recovery proof below uses only this formulation, with the symbol marginals _x<sub>e,a</sub>_, the local assignment probabilities \(\lambda_{v,\mathbf{b}}\), and the objective L defined in §3.3.

We first compare a competing feasible LP solution with the true error vector. For each edge, we consider the total probability that the solution’s symbol marginal assigns to values other than the true error value. We call these quantities _disagreement probabilities_. The parity checks impose inequalities on these probabilities, which we use to construct a distribution on nonbacktracking walks in _G_. A competing solution with no larger objective value would force some such walk to have at least half of its positions corrupted. Walks shorter than the girth are simple paths, so counting paths and bounding their error probabilities proves the theorem. Only after completing this recovery argument do we introduce a reformulation that removes the exponential dependence of the LP size on _D_.

