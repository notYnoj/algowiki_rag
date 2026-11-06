<tbc>The objective function for the Maximum Independent Set problem is

\(F_\text{MIS}(x)=\sum_{v\in V}x_v.\) (64)

Up to an additive constant and an overall sign factor, the corresponding problem Hamiltonian is encoded as

\(H_{P,\text{MIS}}=\sum_{v\in V}Z_v.\) (65)

Because adjacent vertices cannot simultaneously belong to an independent set, the feasible configurations form a restricted subset of binary strings:

\(\mathcal{F}:=\{x\in\{0,1\}^n|x_ux_v=0\text{for all}\{u,v\}\in E\},\) (66)

inducing the feasible Hilbert subspace

\(W_\mathcal{F}:=\text{span}\{|x\rangle|x\in\mathcal{F}\}\subseteq W.\) (67)

To enforce feasibility in constrained optimization problems, we employ a subspace-preserving mixer Hamiltonian that leaves the feasible subspace _W_<sub>F</sub> invariant \[15, 16, 25, 30\]. Let \(\mathcal{N}_v:=\{w\in V|\{v,w\}\in E\}\) denote the open neighborhood of vertex \(v\in V\) . The local controlled-_X_ mixer _H<sub>CX,v</sub>_ acts on a computational basis state \(|x\rangle\) according to the rule

\(H_{CX,v}|x\rangle=\left\{\begin{array}{ c c }
\left|x^{(v)}\right\rangle, & \text{if}x_w=0\text{for all}w\in\mathcal{N}_v, \\
0, & \text{if}x_w=1\text{for some}w\in\mathcal{N}_v,
\end{array}\right.\) (68)

where _x_<sup>(_v_)</sup> denotes the bitstring obtained by flipping the _v_-th bit of _x_.

In terms of Pauli operators, each local mixer admits the explicit representation

\(\mathcal{P}_v:=\prod_{w\in\mathcal{N}_v}\frac{I+Z_w}{2},H_{CX,v}:=X_v\mathcal{P}_v,H_{CX}:=\sum_{v\in V}H_{CX,v},\) (69)

\begin{tabular}{cccccccc}
_i_ & \(\text{dim}\big(\mathfrak{g}_{\Gamma_i,\text{std}}\big)\) & \(\text{dim}\big(\mathfrak{g}_{\Gamma_i,\text{std}}^{v_1}\big)\) & \(\text{dim}\big(\mathfrak{g}_{\Gamma_i,\text{std}}^{v_2}\big)\) & \(\text{dim}\big(\mathfrak{g}_{\Gamma_i,\text{std}}^{v_3}\big)\) & \(\text{dim}\big(\mathfrak{g}_{\Gamma_i,\text{std}}^{v_4}\big)\) & \(\text{dim}\big(\mathfrak{g}_{\Gamma_i,\text{std}}^{v_5}\big)\) & \(\text{dim}\big(\mathfrak{g}_{\Gamma_i,\text{std}}^{v_6}\big)\) \\
1 & 1984 & 1023 & 1023 & 1023 & 1023 & 1023 & 258 \\
2 & 1970 & 258 & 1023 & 1023 & 1023 & 1023 & 258 \\
3 & 1983 & 258 & 1023 & 1023 & 1023 & 258 & 73 \\
4 & 1984 & 1023 & 1023 & 1023 & 1023 & 258 & 1023 \\
5 & 1984 & 1023 & 1023 & 1023 & 1023 & 258 & 1023 \\
6 & 1984 & 1023 & 1023 & 1023 & 1023 & 1023 & 1023 \\
7 & 1984 & 1023 & 1023 & 1023 & 1023 & 258 & 1023 \\
8 & 1984 & 1023 & 1023 & 1023 & 1023 & 1023 & 1023 \\
\end{tabular}

\begin{tabular}{cccccccc}
_i_ & \(\mathcal{D}_{\mathfrak{g}_{\Gamma_i,\text{std}}}\) & \(\mathcal{D}_{\mathfrak{g}_{\Gamma_i,\text{std}}^{v_1}}\) & \(\mathcal{D}_{\mathfrak{g}_{\Gamma_i,\text{std}}^{v_2}}\) & \(\mathcal{D}_{\mathfrak{g}_{\Gamma_i,\text{std}}^{v_3}}\) & \(\mathcal{D}_{\mathfrak{g}_{\Gamma_i,\text{std}}^{v_4}}\) & \(\mathcal{D}_{\mathfrak{g}_{\Gamma_i,\text{std}}^{v_5}}\) & \(\mathcal{D}_{\mathfrak{g}_{\Gamma_i,\text{std}}^{v_6}}\) \\
1 & 19 & 20 & 16 & 14 & 17 & 17 & 19 \\
2 & 21 & 17 & 18 & 18 & 18 & 19 & 17 \\
3 & 29 & 17 & 28 & 30 & 26 & 29 & 17 \\
4 & 19 & 16 & 17 & 14 & 16 & 13 & 16 \\
5 & 21 & 22 & 20 & 18 & 24 & 14 & 30 \\
6 & 17 & 18 & 14 & 15 & 15 & 14 & 20 \\
7 & 19 & 17 & 17 & 16 & 17 & 12 & 19 \\
8 & 17 & 14 & 14 & 14 & 14 & 14 & 14 \\
\end{tabular}

TABLE III. Comparison of dimensions and stabilization depths for reduced standard dynamical Lie algebras across all non-isomorphic asymmetric graphs of order 6.

