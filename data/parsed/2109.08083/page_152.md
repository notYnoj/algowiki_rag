<tbc>that in _H_ the vertex _v_ is in at least \((1-\alpha_G)\frac{t_0p_\mathrm{gr}^3}{150}\) such edges. Since \(H'_0\supseteq H_0^c\), \(1-d_{w_0^c}(u)\ge 1/4\) and \(1-d_{w_H^c}(u)\ge 1/21\) for every \(u\in I_{t_1}\), by Proposition 6.81 (v) and Lemma 6.73 (v) the result follows. □

By Proposition 6.85 since \(|U_0|=O\left(p_\mathrm{gr}t_0^{1-\epsilon/2}\right)\) we are able to cover all of the vertices in _U_<sub>0</sub> greedily, without causing any parity problems. Let \(M_0^c\) be the matching obtained from such a greedy cover. Then setting<tbc>

\(M_0:=M'_0\cup M_0^c,\)

<tbc>we let<tbc>

\(H_1:=H_0[V(H_0)\backslash V(M_0)].\)

<tbc>Next we will define a weight function _w_<sub>1</sub> satisfying the requirements of Theorem 6.1. Let<tbc>

\(w_{0.0}(e)=\frac{w_0(e)}{\prod_{u\in(e\cap I_{t_1})}1-d_{w_0^c}(u)},\)

<tbc>for every \(e\in H_0\) and set

\(w_1(e):=\frac{w_{0.0}(e)}{\mathrm{max}_{v\in V(H_1)}d_{w_{0.0},H_1}(v)}.\)

It remains to prove that the statements of Theorem 6.1 indeed hold.

Proposition 6.86. _w_<sub>1</sub> _is a fractional matching for H_<sub>1</sub> _such that_ \(d_{w_1,H_1}(v)\ge 1-O(p_\mathrm{gr}^{-2}t_0^{-\epsilon/2})\) _for every_ \(v\in V(H_1)\)_. Furthermore,_ \(w_1(e)=(1\pm O(p_\mathrm{gr}^{-2}t_0^{-\epsilon/2}))w_{0.0}(e)\) _for every_ \(e\in H_0\).

Proof. The proof follows via the same strategy used to prove Propositions 6.75 6.77 and 6.78, the facts about _w_<sub>0</sub> and _d_<sub>_w_<sub>0</sub>_,H_<sub>0</sub></sub>(_v_). In particular, for each \(v\in V(H_1)\), we have that<tbc>

\(d_{w_{0.0},H_1}(v)=\sum_{e\in E_{H_1}(v,I_{t_1})}w_{0.0}(e)\le\left(\sum_{e\in E_{H_0^c}(v,I_{t_1})}w_{0.0}(e)\right)+O(p_\mathrm{gr}^{-2}t_0^{-\epsilon/2}),\)

<tbc>since by Proposition 6.82 we have from \(H_0^c\) to _H_<sub>1</sub> that we added at most \(P_0^c=O(p_\mathrm{gr}t_0^{1-\epsilon/2})\) edges, and the weight on each such edge has order \(\Theta(p_\mathrm{gr}^{-3}t_0^{-1})\). Then by Proposition 6.81 we have that

\(\sum_{e\in E_{H_0^c}(v,I_{t_1})}w_{0.0}(e)=(1\pm O(t_0^{-\epsilon}))\sum_{e\in E_{H_0}(v,I_{t_1})}w_{0.0}(e)\prod_{u\in e\backslash\{v\}}(1-d_{w_0^c}(u)),\)

where \(\sum_{e\in E_{H_0}(v,I_{t_1})}w_{0.0}(e)\prod_{u\in e\backslash\{v\}}(1-d_{w_0^c}(u))=\frac{w_0(E_{H_0}(v,I_{t_1}))}{1-d_{w_0^c}(v)}=1\pm O(p_\mathrm{gr}^{-2}t_0^{-\epsilon})\), where the last equality holds by Corollary 6.80. So we find that \(d_{w_{0.0},H_1}(v)\le 1+O(p_\mathrm{gr}^{-2}t_0^{-\epsilon/2})\). It follows then that \(w_1=(1\pm O(p_\mathrm{gr}^{-2}t_0^{-\epsilon/2}))w_{0.0}(e)\). Now, that _w_<sub>1</sub> is a fractional matching for _H_<sub>1</sub> follows by construction. Furthermore, we have that \(d_{w_1,H_1}(v)=\sum_{e\in E_{H_1}(v,I_{t_1})}w_1(e)=(1\pm O(p_\mathrm{gr}^{-2}t_0^{-\epsilon/2}))\sum_{e\in E_{H_1}(v,I_{t_1})}w_{0.0}(e)\) so from the above, we have that \(d_{w_1,H_1}(v)\ge 1-O(p_\mathrm{gr}^{-2}t_0^{-\epsilon/2})\), for every \(v\in V(H_1)\), as claimed. □

