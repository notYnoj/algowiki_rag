<tbc>Proof. Clearly \(|V(H_{l+1}[S])|\le|V(H_{1*}[S])|\). By Theorems 6.1 and 6.12 this gives the upper bound. Furthermore, by Proposition 6.60 a lower bound is given by

\(\frac{|V(H_{1*}[S])|min_{v\in V(H_{1*}[S])}w_{1*}(E_{H_{1*}}(v,I_{t_{l+1}}))}{2}.\)

Using Proposition 6.56 along with Theorems 6.1 and 6.12 yields the given lower bound. □

Corollary 6.61 addresses (P4) in the definition of _l_+1 permissibility. It remains to address (P5).

Proposition 6.62. _Suppose that_ (_H<sub>i</sub>,w<sub>i</sub>_) _is i-permissible for every_ \(i\le l\)_, that H<sub>l</sub> has depth j, and_ (_v,S_<sub>1</sub>_,S_<sub>2</sub>_,S_<sub>3</sub>) _is an open or closed l-reachable tuple which is_ (_l_+1)_-permissible. Then_

\(|E_{H_{l+1}}(v,S_1,S_2,S_3)|=\)<br>
\(\left(1\pm\frac{129c_3}{(\delta_*^-)^3}log^{m^*+4l_3+9}(n)t_l^{-\epsilon_1}\right)\sum_{e\in E_{H_{1*}}(v,S_1,S_2,S_3)}\prod_{u\in e\backslash\{v\}}w_{1*}(E_{H_{1*}}(u,I_{t_{l+1}})).\)

Proof. Once again the proof uses the same strategy as that of Lemma 6.57 and Proposition 6.60. By Lemma 6.52(v) we have that

\(|E_{H_{l+1}}(v,S_1,S_2,S_3)|=\)<br>
\(\left(1\pm\left(16.1m_l+1.1log^{3l_3+7}(n)t_l^{-\epsilon_1}\right)\right)\sum_{e\in E_{H_l}(v,S_1,S_2,S_3)}\prod_{u\in e\backslash\{v\}}(1-d_{w_l^o}(u)),\)

and so by Proposition 6.55,

\(|E_{H_{l+1}}(v,S_1,S_2,S_3)|=\)<br>
\(\left(1\pm\frac{128.9c_3}{(\delta_*^-)^3}log^{m^*+4l_3+8}(n)t_l^{-\epsilon_1}\right)\sum_{e\in E_{H_l}(v,S_1,S_2,S_3)}\prod_{u\in e\backslash\{v\}}(1-d_{w_l^o}(u)).\)

Since \(S_1,S_2,S_3\subseteq I_{t_{l+1}}\) and \(u\in I_{t_{l+1}}\) for every \(u\in e\in E_{H_l}(v,S_1,S_2,S_3)\), we have by Proposition 6.30 we may replace each \((1-d_{w_l^o}(u))\) by \(\left(1\pm\frac{c_{H_l}}{\delta_{H_l}}\right)w_l(E_{H_l}(u,I_{t_{l+1}}))\) so that

\(|E_{H_{l+1}}(v,S_1,S_2,S_3)|=\)<br>
\(\left(1\pm\frac{129c_3}{(\delta_*^-)^3}log^{m^*+4l_3+8}(n)t_l^{-\epsilon_1}\right)\sum_{e\in E_{H_l}(v,S_1,S_2,S_3)}\prod_{u\in e\backslash\{v\}}w_l(E_{H_l}(u,I_{t_{l+1}})).\)

We claim that for every \(i\le l\),

\(\sum_{e\in E_{H_i}(v,S_1,S_2,S_3)}\prod_{u\in e\backslash\{v\}}w_i(E_{H_i}(u,I_{t_{l+1}}))=\)<br>
\(\left(1\pm\frac{129c_3}{(\delta_*^-)^3}log^{m^*+4l_3+8}(n)t_l^{-\epsilon_1}\right)\sum_{e\in E_{H_{i-1}}(v,S_1,S_2,S_3)}\prod_{u\in e\backslash\{v\}}w_{i-1}(E_{H_{i-1}}(u,I_{t_{l+1}})).\)

