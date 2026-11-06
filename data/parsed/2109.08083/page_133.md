<tbc>Proof. The proof is similar to that of Lemma 6.57. By Lemma 6.52(iii) we have that<tbc>

\(|V(H_{l+1}[S])|=\left(1\pm\left(4.1m_l+1.1c_1^{-1}log^{l_3+2}(n)t_l^{-\epsilon_1}\right)\right)\sum_{v\in V(H_l[S])}(1-d_{w_l^o}(v)),\)

<tbc>and so by Proposition 6.55,<tbc>

\(|V(H_{l+1}[S])|=\left(1\pm\frac{32.8c_3}{(\delta_*^-)^3}log^{m^*+2l_3+3}(n)t_l^{-\epsilon_1}\right)\sum_{v\in V(H_l[S])}(1-d_{w_l^o}(v)).\)

<tbc>Since \(S\subseteq I_{t_{l+1}}\), we have by Proposition 6.30 that we may replace \(1-d_{w_l^o}(v)\) by \(\left(1\pm\frac{c_{H_l}}{\delta_{H_l}}\right)w_l(E_{H_l}(u,I_{t_{l+1}}))\), so that<tbc>

\(|V(H_{l+1}[S])|=\left(1\pm\frac{33c_3}{(\delta_*^-)^3}log^{m^*+2l_3+3}(n)t_l^{-\epsilon_1}\right)\sum_{v\in V(H_l[S])}w_l(E_{H_l}(v,I_{t_{l+1}})).\)

<tbc>We claim that for every \(i\le l\),

\(\sum_{v\in V(H_i[S])}w_i(E_{H_i}(v,I_{t_{l+1}}))=\)<br>
\(\left(1\pm\frac{33c_3}{(\delta_*^-)^3}log^{m^*+2l_3+3}(n)t_l^{-\epsilon_1}\right)\sum_{v\in V(H_{i-1}[S])}w_{i-1}(E_{H_{i-1}}(v,I_{t_{l+1}})).\)

Indeed we may use (6.21) and note that by Proposition 6.59 we have that \(\frac{w_{i-1}(E_{H_{i-1}}(v,I_{t_{l+1}}))}{1-d_{w_{i-1}^o}(v)}\) is vertex allowable for \((H_{i-1},w_{i-1},t_{i-1},\eta_1)\). Then again by Lemma 6.52(iii)

\(\sum_{v\in V(H_i[S])}w_i(E_{H_i}(v,I_{t_{l+1}}))=\)<br>
\(\left(1\pm\frac{33c_3}{(\delta_*^-)^3}log^{m^*+2l_3+3}(n)t_l^{-\epsilon_1}\right)\sum_{v\in V(H_{i-1}[S])}w_{i-1}(E_{H_{i-1}}(v,I_{t_{l+1}})),\)

as claimed. Then

\(\sum_{v\in V(H_l[S])}w_l(E_{H_l}(v,I_{t_{l+1}}))=\)<br>
\(\prod_{t^*(k_{j-3})\le i\le l}\left(1\pm\frac{33c_3}{(\delta_*^-)^3}log^{m^*+2l_3+3}(n)t_l^{-\epsilon_1}\right)\sum_{v\in V(H_{1^*}[S])}w_{1^*}(E_{H_{1^*}}(v,I_{t_{l+1}})),\)

and so

\(|V(H_{l+1}[S])|=\left(1\pm\frac{33c_3}{(\delta_*^-)^3}log^{m^*+2l_3+4}(n)t_l^{-\epsilon_1}\right)\sum_{v\in V(H_{1^*}[S])}w_{1^*}(E_{H_{1^*}}(v,I_{t_{l+1}})).\)

□

Corollary 6.61. _Suppose that_ (_H<sub>i</sub>,w<sub>i</sub>_) _is i-permissible for every_ \(i\le l\)_, and that H<sub>l</sub> has depth j, and S is_ (_l_+1)_-valid and l-reachable. Then_

\(\frac{c_{1,3}c_{1,5}c_{1,1}^*|S|p_\text{gr}}{2log^2(n)}\le|V(H_{l+1}[S])|\le c_{1,4}|S|p_\text{gr}.\)

