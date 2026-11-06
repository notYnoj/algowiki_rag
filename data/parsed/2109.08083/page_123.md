6.4.1.5. (_H_<sub>_i_+1</sub>_,w_<sub>_i_+1</sub>) _in terms of_ (_H<sub>i</sub>,w<sub>i</sub>)._ As per the strategy to show that (_H_<sub>_i_+1</sub>_,w_<sub>_i_+1</sub>) is (_i_+1)-permissible, we wish to understand (_H_<sub>_i_+1</sub>_,w_<sub>_i_+1</sub>) in terms of (_H<sub>i</sub>,w<sub>i</sub>_). In the previous steps there are many properties of (_H_<sub>_i_+1</sub>_,w_<sub>_i_+1</sub>) described in terms of _H_<sub>_i_.1</sub>, the graph obtained from _H<sub>i</sub>_ after Step 1 of Plan 6.34. In this section we shift to understanding how such variables and properties ‘look’ in terms of (_H<sub>i</sub>,w<sub>i</sub>_). In particular, we start by upper bounding \(p_v^i\) and \(p_e^i\), before giving a more complete list of properties comparable to those considered in the definition of graph permissibility.

Proposition 6.51. _Given that_ (_H<sub>i</sub>,w<sub>i</sub>_) _is i-permissible, we have that_<tbc>

\(p_v^i\le\frac{4.1max\{c_{H_i},log(n)t_i^{-\epsilon_1}\}|E_{H_i}(v,I_{t_i}\backslash I_{t_{i+1}},*,*)|}{(\delta_{H_i})^3|E_{H_i}(v,I_{t_{i+1}})|},\)

<tbc>_for every_ \(v\in V(H_{i.1}[I_{t_{i+1}}])\)_, and_<tbc>

\(p_e^i\le max_{v\in e}\frac{16.1max\{c_{H_i},log(n)t_i^{-\epsilon_1}\}|E_{H_i}(v,I_{t_i}\backslash I_{t_{i+1}},*,*)|}{(\delta_{H_i})^3|E_{H_i}(v,I_{t_{i+1}})|},\)

<tbc>_for every_ \(e\in H_{i.1}[I_{t_{i+1}}]\)_. Additionally we have that_<tbc>

\(\frac{1}{1-p_e^i}\le 1+1.1p_e^i.\)

<tbc>Proof. We have from Proposition 6.40 that<tbc>

\(p_v^i\le\frac{2|E_{H_{i.1}}(v,I_{t_i}\backslash I_{t_{i+1}},*,*)|}{min_{v\in V(H_{i.1}[I_{t_i}\backslash I_{t_{i+1}}])}d_{H_{i.1}}(v)}.\)

<tbc>Now, we have that \(d_{H_{i.1}}(v)\ge|E_{H_{i.1}}(v,I_{t_{i+1}})|\) for each \(v\in V(H_{i.1}[I_{t_i}\backslash I_{t_{i+1}}])\), and by Theorem 6.28(K2) and Proposition 6.30,

\(|E_{H_{i.1}}(v,I_{t_{i+1}})|=(1\pm log^{3l_3+7}(n)t_i^{-\epsilon_1})\sum_{e\in E_{H_i}(v,I_{t_{i+1}})}\prod_{u\in e\backslash\{v\}}(1-d_{w_i^o}(u))\)<br>
\(=\left(1\pm\left(\frac{3.1c_{H_i}}{\delta_{H_i}}+log^{3l_3+7}(n)t_i^{-\epsilon_1}\right)\right)\sum_{e\in E_{H_i}(v,I_{t_{i+1}})}\prod_{u\in e\backslash\{v\}}w_i(E_{H_i}(u,I_{t_{i+1}}))\)<br>
\(\ge\left(1\pm\left(\frac{3.1c_{H_i}}{\delta_{H_i}}+log^{3l_3+7}(n)t_i^{-\epsilon_1}\right)\right)\delta_{H_i}^3|E_{H_i}(v,I_{t_{i+1}})|.\)

Recalling Proposition 6.17, we also have that

\(|E_{H_{i.1}}(v,I_{t_i}\backslash I_{t_{i+1}},*,*)|=\sum_{e\in E_{H_i}(v,I_{t_i}\backslash I_{t_{i+1}},*,*)}\prod_{u\in e\backslash\{v\}}(1-d_{w_i^o}(v))\)<br>
\(\pm O\left(t_i^{-\epsilon_1}|E_{H_i}(v,I_{t_i}\backslash I_{t_{i+1}},*,*)|\right)\)<br>
\(\le\left(1\pm\frac{2.1c_{H_i}}{\delta_{H_i}}\right)c_{H_i}\sum_{e\in E_{H_i}(v,I_{t_i}\backslash I_{t_{i+1}},*,*)}\prod_{u\in(e\backslash\{v\})\cap I_{t_{i+1}}}w_i(E_{H_i}(u,I_{t_{i+1}}))\)<br>
\(\pm O\left(t_i^{-\epsilon_1}|E_{H_i}(v,I_{t_i}\backslash I_{t_{i+1}},*,*)|\right)\)<br>
\(\le\left(1\pm\frac{2.1c_{H_i}}{\delta_{H_i}}\right)2max\{c_{H_i},log(n)t_i^{-\epsilon_1}\}|E_{H_i}(v,I_{t_i}\backslash I_{t_{i+1}},*,*)|.\)

