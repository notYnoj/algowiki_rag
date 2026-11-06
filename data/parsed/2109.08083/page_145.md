<tbc>in total the at most \(10t_0^{1-\epsilon} p_\mathrm{gr}\) vertices which have been removed to reach _H_<sub>0</sub> remove at most \(O(j_it_0^{1-\epsilon} p_\mathrm{gr})\) and \(O(t_1t_0^{1-\epsilon} p_\mathrm{gr})\) configurations, respectively, and the result follows. □

**6.5.3. Reweighting.** We now wish to update the weighting _w<sub>H</sub>_ for edges remaining in _H_<sub>0</sub>. The strategy for this is very similar to the strategy for reweighting for subsequent steps described in Section 6.4, however we only require one intermediate step, rather than two. We first define a new weighting _w_<sub>_H,_0</sub> as follows:<tbc>

\(w_{H.0}(e):=\frac{w_H(e)}{\prod_{v\in e\cap I_{t_0}}(1-d_{w_H^o}(v))},\)

<tbc>for every \(e\in E(H)\). Supposing now that _d_<sub>_w_<sub>_H,_0</sub>_,H_<sub>0</sub></sub>(_v)\>_1 for some \(v\in V(H_0)\), let \(d_H:=\mathrm{max}_{v\in V(H_0)}d_{w_{H.0},H_0}(v)\). Then define

\(w_0(e):=\frac{w_{H.0}(e)}{d_H},\)

for every \(e\in E(H)\).

Proposition 6.74. _w_<sub>_H,_0</sub> _is edge allowable for_ \((H,w_H,t_0,\eta)\).

Proof. Recall that \(1\ge 1-d_{w_H^o}(v)\ge 1/4\) for every \(v\in V(H[I_{t_0}])\). Thus _w_<sub>_H,_0</sub>(_e_) has the same order as _w<sub>H</sub>(e_) for each \(e\in E(H)\). In particular we have that \(w_{H.0}(e)=\Theta\left(t_0p_\mathrm{gr}^3\right)\) for every \(e\in E(H)\). Thus by Remark 6.29 it follows that _w_<sub>_H,_0</sub> is edge allowable for \((H,w_H,t_0,\eta)\). □

Proposition 6.75. \(d_H\le 1+1.1C_0p_\mathrm{gr}^{-2}t_0^{-\epsilon}\).

Proof. Since _w_<sub>_H,_0</sub> is edge allowable for \((H,w_H,t_0,\eta)\), using Lemma 6.73, we have that

\(d_{w_{H.0},H_0}(v)=\)<br>
\(w_{H.0}(E_{H_0}(v,I_{t_0}))=(1\pm C_0p_\mathrm{gr}^{-2}t_0^{-\epsilon})\sum_{e\in E_H(v,I_{t_0})}w_{H.0}(e)\prod_{u\in e\backslash\{v\}}(1-d_{w_H^o}(u)),\)

for every \(v\in V(H_0)\). Note that

\(\sum_{e\in E_H(v,I_{t_0})}w_{H.0}(e)\prod_{u\in e\backslash\{v\}}(1-d_{w_H^o}(u))=\sum_{e\in E_H(v,I_{t_0})}\frac{w_H(e)}{1-d_{w_H^o}(v)}=\frac{w_H(E_H(v,I_{t_0}))}{1-d_{w_H^o}(v)}.\)

By Proposition 6.65 we have that \(1-d_{w_H^o}(v)=(1\pm 6.1\alpha_G)w_H(E_H(v,I_{t_0}))\) and hence \(\sum_{e\in E_H(v,I_{t_0})}w_{H.0}(e)\prod_{u\in e\backslash\{v\}}(1-d_{w_H^o}(u))=1\pm 12.3\alpha_G\). This yields that \(d_{w_{H.0},H_0}(v)=1\pm 1.1C_0p_\mathrm{gr}^{-2}t_0^{-\epsilon}\) for every \(v\in V(H_0)\) and so in particular \(d_H\le 1+1.1C_0p_\mathrm{gr}^{-2}t_0^{-\epsilon}\) as required. □

Corollary 6.76. _w_<sub>0</sub> _is edge allowable for_ \((H,w_H,t_0,\eta)\).

Proof. The proof follows from Proposition 6.75 in the same way as Corollary 6.38 follows from Proposition 6.37. □

Proposition 6.77. _We have that_<tbc>

\(w_0(e)=(1\pm 1.1C_0p_\mathrm{gr}^{-2}t_0^{-\epsilon})w_{H.0}(e)\)

<tbc>_and_

\(w_{H.0}(e)=(1\pm 1.1C_0p_\mathrm{gr}^{-2}t_0^{-\epsilon})w_0(e)\)

