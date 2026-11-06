<tbc>Proof of Claim. Fix \(\bar{e}_k\in\genfrac(){pt}{2}{E(H)}{k}'\) and let \(\bar{v}_{k,1},\dots,\bar{v}_{k,r^k}\) be an enumeration of the _r<sup>k</sup>_ different \(\bar{v}_k\in\bar{e}_k\). Then

\(q_l(\bar{e}_k)=\sum_{\bar{e}_{l-k}\in\genfrac(){pt}{2}{E(H)\backslash\bar{e}_k}{l-k}}q_l(\bar{e}_k\cup\bar{e}_{l-k})\)<br>
\(=\sum_{\bar{e}_{l-k}\in\genfrac(){pt}{2}{E(H)\backslash\bar{e}_k}{l-k}}\sum_{\bar{v}\in\bar{e}_k\cup\bar{e}_{l-k}}p_l(\bar{v})\)<br>
\(=\sum_{i\in[r^k]}\left(\sum_{\bar{e}_{l-k}\in\genfrac(){pt}{2}{E(H)\backslash\bar{e}_k}{l-k}}\sum_{\bar{v}_{l-k}\in\bar{e}_{l-k}}p_l(\bar{v}_{k,i}\cup\bar{v}_{l-k})\right)\)<br>
\(\le r^kmax_{i\in[r^k]}\left(\sum_{\bar{e}_{l-k}\in\genfrac(){pt}{2}{E(H)\backslash\bar{e}_k}{l-k}}\sum_{\bar{v}_{l-k}\in\bar{e}_{l-k}}p_l(\bar{v}_{k,i}\cup\bar{v}_{l-k})\right)\)<br>
\(\le\Delta^{l-k}r^kmax_{\bar{v}_k\in\genfrac(){pt}{2}{V(H)}{k}}\sum_{\bar{v}_{l-k}\in\genfrac(){pt}{2}{V(H)}{l-k}}p_l(\bar{v}_k\cup\bar{v}_{l-k}),\)

where the last inequality holds since for a fixed \(\bar{v}\in\genfrac(){pt}{2}{V(H)}{l}\) over which the summa tion holds, we have that \(\bar{v}=\bar{v}_k\cup\bar{v}_{l-k}\), where \(\bar{v}_{l-k}\) is obtained from any \(\bar{v}_{l-k}\in\bar{e}_{l-k}\) such that \(\bar{e}_{l-k}\in\genfrac(){pt}{2}{E(H)\backslash\bar{e}_k}{l-k}'\). There are at most \(\Delta^{l-k}\) sets \(\bar{e}_{l-k}\in\genfrac(){pt}{2}{E(H)\backslash\bar{e}_k}{l-k}'\) which contain such a \(\bar{v}_{l-k}\) yielding the inequality.

Furthermore, observe that

\(q_l(E(H))\ge\sum_{\bar{v}\in\genfrac(){pt}{2}{V(H)}{l}}p_l(\bar{v})\prod_{v\in\bar{v}}(d_H(v)-r(l-1)\Delta^\mathrm{co}),\)

since \(\bar{v}=\{v_1,v_2,\dots,v_l\}\) is counted every time there is a disjoint _l_-set of edges {_e_<sub>1</sub>_,e_<sub>2</sub>_,...,e<sub>l</sub>_} such that \(v_i\in e_i\). There are _d<sub>H</sub>(v<sub>i</sub>_) edges containing _v<sub>i</sub>_, and for the choice of (_l_-1) other edges that could be in \(\bar{e}\), each one _e<sub>j</sub>_ must contain _v<sub>j</sub>_ but not share a vertex with any other _e<sub>j</sub>_. In particular, fixing an _l_-set {_v_<sub>1</sub>_,v_<sub>2</sub>_,...,v<sub>l</sub>_} and enumerating how many \(\bar{e}\) count \(\bar{v}\), the choices for _e_<sub>1</sub> are those such that \(e_1\unknown v_1\) and _e_<sub>1</sub> does not contain _v_<sub>2</sub>_,...,v<sub>l</sub>_. There are at least \(d_H(v_1)-(l-1)\Delta^\mathrm{co}\) such choices for _e_<sub>1</sub>. Then for each of these we can take all edges containing _v_<sub>2</sub> for _e_<sub>2</sub> except those containing a vertex from _e_<sub>1</sub> or a vertex in {_v_<sub>3</sub>_,...,v<sub>l</sub>_}. Then there are at least \(d_H(v_2)-(r+(l-2))\Delta^\mathrm{co}\) choices for _e_<sub>2</sub>. Continuing this way, there are at least \(d_H(v_j)-((j-1)r+(l-j))\Delta^\mathrm{co}\ge d_H(v_j)-(l-1)r\Delta^\mathrm{co}\) choices for _e<sub>j</sub>_ for every \(j\in[l]\), thus giving the above inequality. Then, since \(d_H(v)\ge\Delta^{1-\psi}\), we have

\(q_l(E(H))\ge\left(\Delta^{1-\psi}-r(l-1)\Delta^\mathrm{co}\right)^l\sum_{\bar{v}\in\genfrac(){pt}{2}{V(H)}{l}}p_l(\bar{v})\)<br>
\(\ge\Delta^{l(1-\psi)}\left(1-\frac{rl^2}{\Delta^{\eta-\psi}}\right)\sum_{\bar{v}\in\genfrac(){pt}{2}{V(H)}{l}}p_l(\bar{v}).\)

