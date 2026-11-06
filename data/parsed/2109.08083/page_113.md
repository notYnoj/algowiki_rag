<tbc>1. Thus clearly \(\prod_{u\in e\cap I_{t_{i+1}}}(1-d_{w_i^o}(u))\le 1\) and

\(\prod_{u\in e\cap I_{t_{i+1}}}(1-d_{w_i^o}(u))=\prod_{u\in e\cap I_{t_{i+1}}}\left(1\pm\frac{log^{l_4+l_3+2}(n)}{c_1t_i^{\epsilon_1}}\right)w_i(E_{H_i}(u,I_{t_{i+1}}))\)<br>
\(\ge\left(1-\frac{log^{l_4+l_3+2}(n)}{c_1t_i^{\epsilon_1}}\right)^4\frac{c_1^4}{log^{4l_3+8}(n)}\)<br>
\(\ge\left(1-\frac{4.1log^{l_4+l_3+2}(n)}{c_1t_i^{\epsilon_1}}\right)\frac{c_1^4}{log^{4l_3+8}(n)}.\)

The result follows. □

Proposition 6.36. _w_<sub>_i,_0</sub> _is edge allowable for_ \((H_i,w_i,t_i,\eta_1)\).

Proof. By Theorem 6.28 and the remark following it, if we can show that for each _i_-reachable tuple (_v,S_<sub>1</sub>_,S_<sub>2</sub>_,S_<sub>3</sub>) that \(\frac{max_{e\in E_{H_i^o}(v,S_1,S_2,S_3)}w_{i,0}(e)}{min_{e\in E_{H_i^o}(v,S_1,S_2,S_3)}w_{i,0}(e)}\le log^{500}(n)\), then _w_<sub>_i,_0</sub> is indeed edge allowable for \((H_i,w_i,t_i,\eta_1)\). By Proposition 6.35 and (P3), for an _i_-reachable edge _e_ we have that \(w_{i,0}(e)\ge w_i(e)\ge\frac{c_1}{p_\text{gr}^3t_ilog^2(n)}\) and \(w_{i,0}(e)\le\frac{1.1log^{l_1+4l_3+8}(n)}{c_1^4t_ip_\text{gr}^3}\) .2 Then for each _i_-reachable tuple (_v,S_<sub>1</sub>_,S_<sub>2</sub>_,S_<sub>3</sub>) we certainly have

\(\frac{max_{e\in E_{H_i^o}(v,S_1,S_2,S_3)}w_{i,0}(e)}{min_{e\in E_{H_i^o}(v,S_1,S_2,S_3)}w_{i,0}(e)}\le\frac{2log^{l_1+4l_3+8}(n)}{c_1^5}\le log^{500}(n),\)

as required. □

We modify _w_<sub>_i,_0</sub> to find a fractional matching for _H_<sub>_i,_1</sub>\[_I_<sub>_t<sub>i</sub>_+1</sub>\]. Let<tbc>

\(d_{i,0}^*:=max_{v\in V(H_{i,1})}w_{i,0}(E_{H_{i,1}}(v,I_{t_{i+1}}))\)

<tbc>and define

\(w_{i,1}(e)=\left\{\begin{array}{ c c }
\frac{w_{i,0}(e)}{d_{i,0}^*} & \text{if}e\text{is}i\text{-reachable and}d_{i,0}^*\ge 1 \\
w_{i,0}(e) & \text{if}e\text{is}i\text{-reachable and}d_{i,0}^*<1 \\
w_{1^*}(e) & \text{otherwise.}
\end{array}\right..\)

Proposition 6.37. \(d_{i,0}^*\le 1+log^{3l_3+7}(n)t_i^{-\epsilon_1}\).

Proof. Since _w_<sub>_i,_0</sub> is edge allowable for \((H_i,w_i,t_i,\eta_1)\), we have by (K2) that for every \(v\in V(H_{i,1})\),

\(w_{i,0}(E_{H_{i,1}}(v,I_{t_{i+1}}))=(1\pm log^{3l_3+7}(n)t_i^{-\epsilon_1})\sum_{e\in E_{H_i}(v,I_{t_{i+1}})}w_{i,0}(e)\prod_{u\in e\backslash\{v\}}(1-d_{w_i^o}(u)).\)

Note that every edge \(e\in E_{H_i}(v,I_{t_{i+1}})\) either has all four vertices (including _v_) contained in _I_<sub>_t<sub>i</sub>_+1</sub>, or has all vertices except for _v_ contained in _I_<sub>_t<sub>i</sub>_+1</sub>. Then for

2Note that any edge _e_ that is _i_-reachable but not (_i_-1)-reachable satisfies this by Theorem 6.12 combined with (P3).

