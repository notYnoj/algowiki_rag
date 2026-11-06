<tbc>Considering upper bounds, we have that \(w_{1^*}(E_{H_{1^*}}(u,I_{t_{l+1}}))=d_{w_{1^*},H_{1^*}}(u)\ge 1-t_1^{-\epsilon_1}\) for each \(u\in K_{j+1}\). Otherwise \(u\in K_{j-1}\backslash K_{j+1}\) and so by Proposition 6.56 we have that \(w_{1^*}(E_{H_{1^*}}(u,I_{t_{l+1}}))\ge\frac{c_{1,5}c_{1,1}^*}{\mathrm{log}^2(n)}\).

It follows that \(w_{l+1}(e)\le\frac{c_{1,2}^*}{k_{j+1}p_\mathrm{gr}^3\mathrm{log}(n)}\cdot\frac{2\mathrm{log}^8(n)}{(c_{1,5}c_{1,1}^*)^4}\le\frac{2c_{1,2}^*\mathrm{log}^9(n)}{(c_{1,5}c_{1,1}^*)^4t_{l+1}p_\mathrm{gr}^3}\), as required. □

This gives (P3). To show (P4) and (P5), we first include the following proposition:

Proposition 6.59. _Suppose that H<sub>l</sub> has depth j. Let_<tbc>

\(p_S(v):=\frac{w_{i-1}(E_{H_{i-1}}(v,I_{t_{l+1}}))}{1-d_{w_{i-1}^o}(v)}\unknown_{v\in V(H_{i-1}[S])},\)

<tbc>_and_

\(f_v(e):=\left(\prod_{u\in e\backslash\{v\}}\frac{w_{i-1}(E_{H_{i-1}}(u,I_{t_{l+1}}))}{1-d_{w_{i-1}^o}(u)}\right)\unknown_{e\in E_{H_{i-1}}(v,S_1,S_2,S_3)}\)

_where_ \(t^*(k_{j-3})\le i-1\le l\)_. Then whenever S is i-reachable, or_ (_v,S_<sub>1</sub>_,S_<sub>2</sub>_,S_<sub>3</sub>) _is an i-reachable tuple with_ \(v\in V(H_{i-1}[I_{t_i}])\)_, we have that p<sub>S</sub> is vertex allowable for_ \((H_{i-1},w_{i-1},t_{i-1},\eta_1)\) _and f<sub>v</sub> is v-edge allowable for_ \((H_{i-1},w_{i-1},t_{i-1},\eta_1)\).

Proof. By the permissibility of (_H_<sub>_i_-1</sub>_,w_<sub>_i_-1</sub>) and using Propositions 6.26 and 6.30, in each case we have that<tbc>

\(\frac{w_{i-1}(E_{H_{i-1}}(v,I_{t_{l+1}}))}{1-d_{w_{i-1}^o}(v)}\le\frac{8c_3\mathrm{log}^{l_1+l_3+2}(n)t_{l+1}}{c_1t_i}\)

<tbc>and that<tbc>

\(\frac{w_{i-1}(E_{H_{i-1}}(v,I_{t_{l+1}}))}{1-d_{w_{i-1}^o}(v)}\ge\frac{c_1t_{l+1}}{8c_3\mathrm{log}^{l_1+l_3+2}(n)t_i}.\)

<tbc>Thus

\(\mathrm{max}\frac{\frac{w_{i-1}(E_{H_{i-1}}(v,I_{t_{l+1}}))}{1-d_{w_{i-1}^o}(v)}}{\mathrm{min}\frac{\frac{w_{i-1}(E_{H_{i-1}}(v,I_{t_{l+1}}))}{1-d_{w_{i-1}^o}(v)}}}{\le\frac{64c_3^2\mathrm{log}^{2l_1+2l_3+4}(n)}{c_1^2}\le\mathrm{log}^{500}(n).\)

By Remark 6.29 it follows that _p<sub>S</sub>_ is vertex allowable. Furthermore, we see immediately also that

\(\frac{\mathrm{max}_e\prod_{u\in e\backslash\{v\}}\frac{\frac{w_{i-1}(E_{H_{i-1}}(u,I_{t_{l+1}}))}{1-d_{w_{i-1}^o}(u)}}{\mathrm{min}_e\prod_{u\in e\backslash\{v\}}\frac{\frac{w_{i-1}(E_{H_{i-1}}(u,I_{t_{l+1}}))}{1-d_{w_{i-1}^o}(u)}}}{\le\frac{64^3c_3^6\mathrm{log}^{6l_1+6l_3+12}(n)}{c_1^6}\le\mathrm{log}^{500}(n),\)

so similarly _f<sub>v</sub>_ is _v_-edge allowable, as required. □

Proposition 6.60. _Suppose that_ (_H<sub>i</sub>,w<sub>i</sub>_) _is i-permissible for every_ \(i\le l\)_, that H<sub>l</sub> has depth j, and S is_ (_l_+1)_-valid and l-reachable. Then_

\(|V(H_{l+1}[S])|=\left(1\pm\frac{33c_3}{(\delta_*^-)^3}\mathrm{log}^{m^*+2l_3+4}(n)t_l^{-\epsilon_1}\right)\sum_{v\in V(H_{1^*}[S])}w_{1^*}(E_{H_{1^*}}(v,I_{t_{l+1}})).\)

