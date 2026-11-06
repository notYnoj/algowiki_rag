<tbc>_for every_ \(e\in H\)_. Furthermore, for every_ \(e\in H_0\) _we have that_<tbc>

\((1-1.1C_0p_\mathrm{gr}^{-2}t_0^{-\epsilon})w_H(e)\le w_0(e)\le 82w_H(e).\)

<tbc>Proof. Now, since by Proposition 6.75, \(d_{w_{H.0},H_0}(v)\le 1+1.1C_0p_\mathrm{gr}^{-2}t_0^{-\epsilon}\) for every \(v\in V(H_0)\), we have that<tbc>

\(w_{H.0}(e)\ge w_0(e)\ge\frac{w_{H.0}(e)}{1+1.1C_0p_\mathrm{gr}^{-2}t_0^{-\epsilon}},\)

<tbc>for every edge \(e\in H_0\). In particular, this gives the first two statements. By Proposition 6.65 we have that \(1\ge(1-d_{w_H^o}(u))\ge\frac{1}{3}-O(\alpha_G)\) for every \(u\in V(H_0)\). Hence \(w_H(e)\le w_{H.0}(e)\le 81.1w_H(e)\). It then follows from the second statement of the proposition that

\((1-1.1C_0p_\mathrm{gr}^{-2}t_0^{-\epsilon})w_H(e)\le w_0(e)\le 82w_H(e)\)

for every \(e\in H_0\), as claimed. □

Proposition 6.78. _w_<sub>0</sub> _is a fractional matching for H_<sub>0</sub> _such that_<tbc>

\(d_{w_0,H_0}(v)\ge 1-2.2C_0p_\mathrm{gr}^{-2}t_0^{-\epsilon}\)

<tbc>_for every_ \(v\in V(H_0)\)_. Furthermore, given a_ 0_-valid tuple_ (_v,S_<sub>1</sub>_,S_<sub>2</sub>_,S_<sub>3</sub>)_, we have that_<tbc>

\(w_0(E_{H_0}(v,S_1,S_2,S_3))=(1\pm 2.2C_0p_\mathrm{gr}^{-2}t_0^{-\epsilon})\frac{w_H(E_H(v,S_1,S_2,S_3))}{w_H(E_H(v,I_{t_0}))}.\)

<tbc>Proof. That _w_<sub>0</sub> is a fractional matching for _H_<sub>0</sub> follows from the construction of _w_<sub>0</sub>. Considering a 0-valid tuple (_v,S_<sub>1</sub>_,S_<sub>2</sub>_,S_<sub>3</sub>) we have that<tbc>

\(w_0(E_{H_0}(v,S_1,S_2,S_3))=(1\pm 1.1C_0p_\mathrm{gr}^{-2}t_0^{-\epsilon})\sum_{e\in E_{H_0}(v,S_1,S_2,S_3)}w_{H.0}(e)\)

<tbc>by Proposition 6.77. Then since _w_<sub>_H._0</sub> is edge allowable for \((H,w_H,t_0,\eta)\) we have by Lemma 6.73, that<tbc>

\(\sum_{e\in E_{H_0}(v,S_1,S_2,S_3)}w_{H.0}(e)=(1\pm C_0p_\mathrm{gr}^{-2}t_0^{-\epsilon})\sum_{e\in E_H(v,S_1,S_2,S_3)}w_{H.0}(e)\prod_{u\in e\backslash\{v\}}(1-d_{w_H^o}(u)).\)

<tbc>Since for \(v\unknown e\), and \(e\in H[I_{t_0}]\) we have that \(w_{H.0}(e)\prod_{u\in e\backslash\{v\}}(1-d_{w_H^o}(u))=\frac{w_H(e)}{1-d_{w_H^o}(v)}\). Using Proposition 6.65 (iv) we get that

\(w_0(E_{H_0}(v,S_1,S_2,S_3))=\)<br>
\((1\pm 1.1C_0p_\mathrm{gr}^{-2}t_0^{-\epsilon})(1\pm C_0p_\mathrm{gr}^{-2}t_0^{-\epsilon})(1\pm 6.1\alpha_G)\frac{w_H(E_H(v,S_1,S_2,S_3))}{w_H(v,I_{t_0})},\)

and the final claim follows. In particular, this gives that

\(w_0(E_{H_0}(v,I_{t_0}))=(1\pm 2.2C_0p_\mathrm{gr}^{-2}t_0^{-\epsilon})\frac{w_H(v,I_{t_0})}{w_H(v,I_{t_0})},\)

that is, \(d_{w_0,H_0}(v)=w_0(E_{H_0}(v,I_{t_0}))\ge 1-2.2C_0p_\mathrm{gr}^{-2}t_0^{-\epsilon}\), as required. □

In particular, we note that every edge _e_ has \(w_0(e)=\Theta(w_H(e))\), and so it follows that for every _v_, \(d_{H_0}(v)=\Theta(d_H(v))\), since \(d_{w_0,H_0}(v)=(1\pm o(1))d_{w_H,H}(v)\) (as _w<sub>H</sub>_ and _w_<sub>0</sub> are both almost-perfect fractional matchings for _H_ and _H_<sub>0</sub> respectively).

