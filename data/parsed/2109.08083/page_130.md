<tbc>_and_

\(m_i=\frac{\mathrm{max}\{c_{H_i},\mathrm{log}(n)t_i^{-\epsilon_1}\}E_{out}^i}{\delta_{H_i}E_{in}^i}\le\frac{8c_3}{(\delta_*^-)^3}\mathrm{log}^{m^*+l_3}(n)t_l^{-\epsilon_1}.\)

Proof. The first claim is a direct corollary of Proposition 6.54 (noting that \(t_i^{-\epsilon_1}\le t_l^{-\epsilon_1}\) for every \(i\le l\)). For the second claim, it is clear from the first claim that \(m_i\le\frac{8\mathrm{log}^{m^*(n)t_l^{-\epsilon_1}}E_{out}^i}{(\delta_*^-)^3E_{in}^i}\) . So it remains to bound \(\frac{\mathrm{max}_{v\in H_i[I_{t_{i+1}}]}|E_{H_i}(v,I_{t_i}\backslash I_{t_{i+1}},*,*)|}{\mathrm{min}_{v\in H_i[I_{t_{i+1}}]}|E_{H_i}(v,I_{t_{i+1}})|}\) . Now, by _i_-permissibility of (_H<sub>i</sub>,w<sub>i</sub>_) we have from (P5) both that \(|E_{H_i}(v,I_{t_i}\backslash I_{t_{i+1}},*,*)|\le c_3|I_{t_i}\backslash I_{t_{i+1}}|p_\mathrm{gr}^3\) and \(|E_{H_i}(v,I_{t_{i+1}})|\ge\frac{|I_{t_{i+1}}|p_\mathrm{gr}^3}{\mathrm{log}^{l_3}(n)}\) , and so

\(\frac{|E_{H_i}(v,I_{t_i}\backslash I_{t_{i+1}},*,*)|}{|E_{H_i}(v,I_{t_{i+1}})|}\le c_3\mathrm{log}^{l_3}(n)\)

for every \(i\le l\) and every \(v\in V(H_i)\). The second claim follows. □

Proposition 6.56. _Suppose that H<sub>l</sub> has depth j and_ \(u\in K_{j-1}\backslash K_{j+1}\)_. Then_

\(w_{1^*}(E_{H_{1^*}}(u,I_{t_{l+1}}))\ge\frac{c_{1,5}c_{1,1}^*}{\mathrm{log}^2(n)}.\)

Proof. By Theorem 6.1 we have that \(|E_{H_1}(u,I_{t_{l+1}})|\ge c_{1,5}k_jp_\mathrm{gr}^3\). Further more, by Theorem 6.12, each edge in _E_<sub>_H_<sub>1</sub></sub>(_u,I_<sub>_t_<sub>_l_+1</sub></sub>) has weight at least \(\frac{c_{1,1}^*}{k_jp_\mathrm{gr}^3\mathrm{log}^2(n)}\). The proposition follows. □

It remains to check that (_H_<sub>_l_+1</sub>_,w_<sub>_l_+1</sub>) satisfies all of the properties that ensure it is (_l_+1)-permissible, given that (_H<sub>i</sub>,w<sub>i</sub>_) is _i_-permissible for every \(i\le l\). Note that in this case we reach (_H_<sub>_l_+1</sub>_,w_<sub>_l_+1</sub>) by Plan 6.34, and certainly have \(H_{l+1}\subseteq H_{1^*}[I_{t_{l+1}}]\), so (P1) holds. By Proposition 6.50 we have that _w_<sub>_l_+1</sub> is a fractional matching for _H_<sub>_l_+1</sub>, so \(1\ge d_{w_{l+1},H_{l+1}}(v)\) for every \(v\in V(H_{l+1})\). Furthermore, we have that \(d_{w_{l+1},H_{l+1}}(v)=1-c_{H_{l+1},v}\ge 1-\mathrm{log}^{m^*}(n)t_{l+1}^{-\epsilon_1}\) by Proposition 6.54 for all \(v\in V(H_{l+1})\) and for all _v_ which were not _l_-reachable, it is clear that _d_<sub>_w_<sub>_l_+1</sub>_,H_<sub>_l_+1</sub></sub>(_v_)=_d_<sub>_w_<sub>1</sub><sup>∗</sup>_,H_<sub>1<sup>∗</sup></sub>(_v_), so (P2) also holds. We consider the remaining properties, (P3)-(P5) of the definition of (_l_+1)-permissibility, in the following series of results, starting with (P3).

Lemma 6.57. _Suppose that_ (_H<sub>i</sub>,w<sub>i</sub>_) _is i-permissible for every_ \(i\le l\)_. Further suppose that H<sub>l</sub> has depth j and that_ \(e\in H_{l+1}\) _is l-reachable. Then_<tbc>

\(w_{l+1}(e)=\left(1\pm\frac{137.1c_3}{(\delta_*^-)^3}\mathrm{log}^{m^*+4l_3+9}(n)t_l^{-\epsilon_1}\right)\frac{w_{1^*}(e)}{\prod_{u\in e}w_{1^*}(E_{H_{1^*}}(u,I_{t_{l+1}}))}.\)

<tbc>Proof. By Lemma 6.52(ii) we have that<tbc>

\(w_{l+1}(e)=\left(1\pm\left(17.1m_i+2.2\mathrm{log}^{3l_3+7}(n)t_l^{-\epsilon_1}\right)\right)\frac{w_l(e)}{\prod_{u\in e}(1-d_{w_l^o}(u))},\)

<tbc>and so by Proposition 6.55,

\(w_{l+1}(e)=\left(1\pm\frac{137c_3}{(\delta_*^-)^3}\mathrm{log}^{m^*+4l_3+8}(n)t_l^{-\epsilon_1}\right)\frac{w_l(e)}{\prod_{u\in e}(1-d_{w_l^o}(u))}.\)

Since \(e\in E_{H_{l+1}}\), we have that for every \(u\in e\) that \(u\in I_{t_{l+1}}\). Thus by Proposition 6.30 we may replace \(\prod_{u\in e}(1-d_{w_l^o}(u))\) by \(\left(1\pm\frac{c_{H_l}}{\delta_{H_l}}\right)^3\prod_{u\in e}w_l(E_{H_l}(u,I_{t_{l+1}}))\) so that,

