For an edge \(e=(u,w)_i\in M\), let \(F_e\subseteq E\) be the set of edges _f_ such that one of _f_’s endpoints is _u_ or _w_ and the other is uncovered by _M_. Then, \(F_e\subseteq\delta_G(u)\cup\delta_G(w)\) and \(F_e\cap(\delta_G(u)\cap\delta_G(w))=\emptyset\). We now show \(\sum_{f\in F_e}p_f^*\le 1\). We can assume \(F_e\cap\delta_G(u)\neq\emptyset\) and \(F_e\cap\delta_G(w)\neq\emptyset\) since otherwise the claim is trivial. For any \(f\in F_e\cap\delta_G(u)\), its copy _x<sub>f</sub>_ in the modified instance is incident to _u_ and the other endpoint is uncovered by _M_<sup>∗</sup>, and hence the stability of _M_<sup>∗</sup> implies \(e^*\succ_1^*x_f\), where _e_<sup>∗</sup> is the _e_’s copy in _M_<sup>∗</sup> and \(\succ_1^*\) is the _U_-side total order in the modified instance. Similarly, for any \(g\in F_e\cap\delta_G(w)\), we obtain \(e^*\succ_2^*z_g\), where \(\succ_2^*\) is the _W_-side total order. By the construction of \(\succ_1^*,\succ_2^*\), these imply _e_<sup>∗</sup>=_y<sub>e</sub>_ and that we have \(e\succ_uf\) for every \(f\in F_e\cap\delta_G(u)\) and \(e\succ_wg\) for every \(g\in F_e\cap\delta_G(w)\). Thus, in the LP, every element in _F<sub>e</sub>_ appears either in inequality (1) for _u_ or that for _w_, and does not appear in the inequality (2) for _e_. By adding the inequalities (1) for _u_ and _w_ and subtracting (2) for _e_ from it, we obtain \(\sum_{f\in F_e}p_f^*\le 1\) as required.

Let \(\partial M\) denote the set of vertices in \(U\cup W\) covered by _M_. Observe that \(F:=\cup_{e\in M}F_e\) coincides with the set of edges connecting \(\partial M\) and \((U\cup W)\backslash\partial M\), and that \(\{F_e\}_{e\in M}\) forms a partition of _F_. Let \(\Delta:=\sum_{f\in F}p_f^*=\sum_{e\in M}\sum_{f\in F_e}p_f^*\le|M|\), where the last inequality follows from the fact \(\sum_{f\in F_e}p_f^*\le 1\) shown above.

Note that, as _M_ is stable, it is maximal, and hence every edge in _E_ has at least one endpoint in \(\partial M\). Therefore, every \(e\in E\backslash F\) has both endpoints in \(\partial M\). Then, by summing the inequalities (1) for all vertices in \(\partial M\), we obtain \(2\sum_{e\in E\backslash F}p_e^*+\sum_{f\in F}p_f^*\le|\partial M|=2|M|\), which implies \(\sum_{e\in E\backslash F}p_e^*\le|M|-\frac{1}{2}\Delta\). Combined with \(\Delta=\sum_{f\in F}p_f^*\le|M|\), this implies \(\sum_{e\in E}p_e^*\le|M|-\frac{1}{2}\Delta+\Delta=|M|+\frac{1}{2}\Delta\le\frac{3}{2}|M|\).

## 4.2 UGC-hardness of \((2-\delta)\)-approximation

In this section, we provide our hardness reduction to prove Theorem 3, i.e., we show that it is UGC-hard to beat the trivial 2-approximation for max-smpo with general partial orders. We use the following theorem of Bansal and Khot about independent set.

**Theorem 16** (Bansal and Khot \[5\])**.** _Assuming UGC, for any_ \(\varepsilon>0\) _it is NP-hard, given an n-vertex graph that has two disjoint independent sets of size_ \((\frac{1}{2}-\varepsilon)n\) _each, to find an independent set of size_ \(\varepsilon n\).

_Proof of Theorem 3._ We show that a \((2-\delta)\)-approximation algorithm for max-smpo implies that we can find an independent set of size at least \(\varepsilon n\) in an instance of Theorem 16, if \(\varepsilon\) is small enough, which is a contradiction.

Let _G_=(_V,E_) be an instance of independent set, and let _V_=(_v_<sub>1</sub>_,v_<sub>2</sub>_,...,v<sub>n</sub>_). We create an instance \((G'=(U,W;E'),\{\succ_v\}_{v\in U\cup W})\) of max-smpo as follows. For clarity, we refer to the elements of _V_ and \(U\cup W\) as "vertices" and "agents," respectively. For each vertex \(v_i\in V\) , we create four agents \(u_i,y_i\in U\) and \(w_i,x_i\in W\) and create six edges \(g_{i(\ell)}=(u_i,w_i)_\ell\) for \(\ell\in[2]\), \(h_{i(\ell)}=(u_i,x_i)_\ell\) for \(\ell\in[2]\), and \(h'_{i(\ell)}=(y_i,w_i)_\ell\) for \(\ell\in[2]\). Then, for each \((v_i,v_j)\in E\) we create four edges _e<sub>ij</sub>_=(_u<sub>i</sub>,w<sub>j</sub>_)<sub>1</sub>_,f<sub>ij</sub>_=(_u<sub>i</sub>,w<sub>j</sub>_)<sub>2</sub>_,e<sub>ji</sub>_=(_u<sub>j</sub>,w<sub>i</sub>_)<sub>1</sub>_,f<sub>ji</sub>_=(_u<sub>j</sub>,w<sub>i</sub>_)<sub>2</sub>. This completes the construction of the bipartite graph \(G'\). (See Figure 3 for an example.)

We describe the relations in the partial orders of the agents in  1.

Here, \[_X(v<sub>i</sub>_)\] for \(v_i\in\{u_i,w_i\}\) and \(X\in\{E,F\}\) denotes a strict ranking over the adjacent<tbc>

\begin{tabular}{ccccc}
_u<sub>i</sub>_: & \((g_{i(1)}\succ[F(u_i)]\succ h_{i(1)})\wedge(g_{i(2)}\succ[E(u_i)]\succ h_{i(2)})\) & & & \\
_w<sub>i</sub>_: & \((g_{i(2)}\succ[F(w_i)]\succ h'_{i(1)})\wedge(g_{i(1)}\succ[E(w_i)]\succ h'_{i(2)})\) & & & \\
\end{tabular}

1: Partial orders used in the proof of Theorem 3.

