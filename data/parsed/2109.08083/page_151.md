<tbc>Proof. By Proposition 6.81 (vi) we have that the number of wrap-around edges of each type used in \(M_0^o\) is

\(|M_0^o\cap E_{AB}(H_0^o[I_{t_0}\backslash I_{t_{20}}])|=(1\pm t_0^{-\epsilon})\sum_{e\in E_{AB}(H_0^o[I_{t_0}\backslash I_{t_{20}}])}w_0(e),\)

for \(AB\in\{OE,EO\}\). Recall that by Proposition 6.77, and since \(w_H(e)=(1\pm O(\alpha_G))\frac{1}{np_\mathrm{gr}^3}\), we have that \(w_0(e)\ge\frac{1}{2np_\mathrm{gr}^3}\) for every \(e\in E_{AB}(H_0^o[I_{t_0}\backslash I_{t_{20}}])\) and each \(AB\in\{OE,EO\}\). Furthermore by (6.22) we have a constant \(c'\) such that \(E_{AB}(H_0^o[I_{t_0}\backslash I_{t_{20}}])|\ge c't_0^2p_\mathrm{gr}^4\). Hence it follows that

\(|M_0^o\cap E_{AB}(H_0^o[I_{t_0}\backslash I_{t_{20}}])|\ge\frac{c'}{4}t_0p_\mathrm{gr},\)

so the claim holds. □

Since \(P_0^c=O(p_\mathrm{gr}t_0^{1-\epsilon/2})\) and \(M_0^o\) contains \(\Theta\left(t_0p_\mathrm{gr}\right)\) of each wrap around parity avoiding _I_<sub>_t_<sub>20</sub></sub>, we may greedily remove edges of the relevant wrap-around parity from \(M_0^o\) and thus reduce _P_<sub>0</sub> to 0, only affecting properties of vertices, edges and subsets which are not within _I_<sub>_t_<sub>20</sub></sub>. Let \(M'_0\subseteq M_0^o\) be the matching obtained in this way. We will then greedily cover all remaining vertices outside the target interval, including those which are now uncovered as a result of the wrap-around edge removal, without reintroducing any parity disparity. Let \(H'_0:=H_0[V(H_0)\backslash V(M'_0)]\). Note that any lower bounds for degree and interval properties of \(H_0^c\) remain valid for \(H'_0\), since we have only _added_ edges back in to go from \(H_0^c\) to \(H'_0\).

We now run the greedy cover, ensuring that we don’t introduce any parity problems. Let \(U_0=U_0^X\cup U_0^Y\cup U_0^{X+Y}\cup U_0^{X-Y}\) denote the set of uncovered vertices remaining outside the target interval.

Proposition 6.84. _The number of vertices remaining to cover in the greedy cover step, U_<sub>0</sub>_, satisfies_<tbc>

\(|U_0|=O(p_\mathrm{gr}t_0^{1-\epsilon/2}).\)

<tbc>Proof. Since \(P_0^c=O(p_\mathrm{gr}t_0^{1-\epsilon/2})\), we have added at most \(O(p_\mathrm{gr}t_0^{1-\epsilon/2})\) additional vertices to _U_<sub>0</sub> than those which already needed covering after removing \(M_0^o\). We have from (6.13) that

\(|V(H_0^c[I_{t_0}\backslash I_{t_1}])|=\sum_{v\in V(H_0[I_{t_0}\backslash I_{t_1}])}(1-d_{w_0^o}(v))\pm t_0^{-\epsilon}\sum_{V(H_0[I_{t_0}\backslash I_{t_1}])}d_{w_0^o}(v),\)

and for every \(v\in H_0[I_{t_0}\backslash I_{t_1}]\), we have that \(1-d_{w_0^o}(v)=1-d_{w_0,H_0}(v)\le 2.2p_\mathrm{gr}^{-2}t_0^{-\epsilon}\). Furthermore, we have that \(|V(H_0[I_{t_0}\backslash I_{t_1}])|\le\frac{4t_0p_\mathrm{gr}}{3}\) . It follows that \(|V(H_0^c[I_{t_0}\backslash I_{t_1}])|=O(p_\mathrm{gr}^{-1}t_0^{1-\epsilon})\), and thus since \(t_0^{-\epsilon/2}\checkmark p_\mathrm{gr}^2\), we have that \(|U_0|=O(p_\mathrm{gr}t_0^{1-\epsilon/2})\), as required. □

Proposition 6.85. _There exists an absolute constant c\>_0 _such that every vertex_ \(v\in U_0\) _is contained in at least_ \(ct_0p_\mathrm{gr}^3\) _edges in_ \(H'_0\) _which avoid vertices in I_<sub>_t_<sub>20</sub></sub> _and do not wrap-around._

Proof. In T , as per Fact 3.30(iv), such a vertex is in at least \(\frac{t_0}{150}\) such edges. Furthermore, for each such vertex _v_, one can lower bound the collection of non- wrap around edges containing _v_ via \(E_{H_0^\prime}(v,I^J,O)\cup E_{H_0^\prime}(v,I^J,E)\) for some _J_-layer interval of size \(\Theta(t_0)\) with _J_ such that \(v\notin J\). Thus by Theorem 3.28 we have

