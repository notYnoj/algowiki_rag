<tbc>Proposition 6.50. _w_<sub>_i_+1</sub> _is an almost-perfect fractional matching for H_<sub>_i_+1</sub> _such that_<tbc>

\(d_{w_{i+1},H_{i+1}}(v)\ge 1-\left(\frac{c_{H_i,v}}{\delta_{H_i,v}}+2.2\mathrm{log}^{3l_3+7}(n)t_i^{-\epsilon_1}\right),\)

<tbc>_and for every open and closed i-reachable tuple_ (_v,S_<sub>1</sub>_,S_<sub>2</sub>_,S_<sub>3</sub>) _we have_

\(w_{i+1}(E_{H_{i+1}}(v,S_1,S_2,S_3))=\)<br>
\((1\pm 1.1\mathrm{log}^{3l_3+7}(n)t_i^{-\epsilon_1})\sum_{e\in E_{H_i}(v,S_1,S_2,S_3)}w_{i.0}(e)\prod_{u\in e\backslash\{v\}}(1-d_{w_i^o}(u)).\)

Proof. That _w_<sub>_i_+1</sub> is a fractional matching for _H_<sub>_i_+1</sub> follows by construction and the fact that (_H<sub>i</sub>,w<sub>i</sub>_) is _i_-permissible. It is clear that no weights fall below 0 and all weights are at most 1 in the reweighting from _w<sub>i</sub>_, and we normalised to ensure that \(d_{w_{i+1},H_{i+1}}(v)\le 1\) for all \(v\in V(H_{i+1})\). Given that _w_<sub>_i_+1</sub> is a fractional matching for _H_<sub>_i_+1</sub> it remains to consider a lower bound for _d_<sub>_w_<sub>_i_+1</sub>_,H_<sub>_i_+1</sub></sub>(_v_) for each \(v\in V(H_{i+1})\). Now, by definition of _w_<sub>_i_+1</sub> and \(d_i^*\), we have that \(d_{w_{i+1},H_{i+1}}(v)=w_{i+1}(E_{H_{i+1}}(v,I_{t_{i+1}}))=\frac{w_{i.2}(E_{H_{i+1}}(v,I_{t_{i+1}}))}{d_i^*}\ge\frac{w_{i.2}(E_{H_{i+1}}(v,I_{t_{i+1}}))}{1+t_i^{-1.5\epsilon_1}}\) . Then by Corollary 6.49 we have that<tbc>

\(d_{w_{i+1},H_{i+1}}(v)\ge\frac{1-t_i^{-1.5\epsilon_1}}{1+t_i^{-1.5\epsilon_1}}w_{i.1}(E_{H_{i.1}}(v,I_{t_{i+1}})),\)

<tbc>and by Corollary 6.39,<tbc>

\(d_{w_{i+1},H_{i+1}}(v)\ge\frac{1-t_i^{-1.5\epsilon_1}}{1+t_i^{-1.5\epsilon_1}}\left(1-\frac{c_{H_i,v}}{\delta_{H_i,v}}-2.1\mathrm{log}^{3l_3+7}(n)t_i^{-\epsilon_1}\right).\)

<tbc>By Proposition 6.31, it follows that

\(d_{w_{i+1},H_{i+1}}(v)\ge 1-\left(\frac{c_{H_i,v}}{\delta_{H_i,v}}+2.2\mathrm{log}^{3l_3+7}(n)t_i^{-\epsilon_1}\right),\)

and in particular _d_<sub>_w_<sub>_i_+1</sub>_,H_<sub>_i_+1</sub></sub>(_v_)=1-_o_(1), so _w_<sub>_i_+1</sub> is an almost-perfect fractional matching for _H_<sub>_i_+1</sub>.

Using (6.19), (6.18), (K2) and the fact that we now only consider _i_-reachable \(S_1,S_2,S_3\subseteq I_{t_{i+1}}\),

\(w_{i+1}(E_{H_{i+1}}(v,S_1,S_2,S_3))=\sum_{e\in E_{H_{i+1}}(v,S_1,S_2,S_3)}w_{i+1}(e)\)<br>
\(=\sum_{e\in E_{H_{i+1}}(v,S_1,S_2,S_3)}\frac{w_{i.2}(e)}{d_i^*}=(1\pm 1.1t_i^{-1.5\epsilon_1})\sum_{e\in E_{H_{i+1}}(v,S_1,S_2,S_3)}w_{i.2}(e)\)<br>
\(=(1\pm 2.2t_i^{-1.5\epsilon_1})\sum_{e\in E_{H_{i.1}}(v,S_1,S_2,S_3)}w_{i.1}(e)\)<br>
\(=(1\pm 2.2t_i^{-1.5\epsilon_1})(1\pm\mathrm{log}^{3l_3+7}(n)t_i^{-\epsilon_1})\sum_{e\in E_{H_{i.1}}(v,S_1,S_2,S_3)}w_{i.0}(e)\)<br>
\(=(1\pm 1.1\mathrm{log}^{3l_3+7}(n)t_i^{-\epsilon_1})\sum_{e\in E_{H_i}(v,S_1,S_2,S_3)}w_{i.0}(e)\prod_{u\in e\backslash\{v\}}(1-d_{w_i^o}(u)).\)

□

