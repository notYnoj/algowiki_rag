<tbc>\(v\in V(H_{i.1}[I_{t_i}\backslash I_{t_{i+1}}])\),<tbc>

\(\sum_{e\in E_{H_i}(v,I_{t_{i+1}})}w_{i.0}(e)\prod_{u\in e\backslash\{v\}}(1-d_{w_i^o}(u))=\sum_{e\in E_{H_i}(v,I_{t_{i+1}})}w_i(e)\)<br>
\(=w_i(E_{H_i}(v,I_{t_{i+1}}))\le 1,\)

<tbc>and for \(v\in V(H_{i.1}[I_{t_{i+1}}])\),

(6.17) \(\sum_{e\in E_{H_i}(v,I_{t_{i+1}})}w_{i.0}(e)\prod_{u\in e\backslash\{v\}}(1-d_{w_i^o}(u))=\frac{\sum_{e\in E_{H_i}(v,I_{t_{i+1}})}w_i(e)}{1-d_{w_i^o}(v)}=\frac{w_i(E_{H_i}(v,I_{t_{i+1}}))}{1-d_{w_i^o}(v)}.\)

Now, by Proposition 6.25, for \(v\in H_i[I_{t_{i+1}}]\) we have that \(\frac{w_i(E_{H_i}(v,I_{t_{i+1}}))}{1-d_{w_i^o}(v)}\le 1\). It follows that \(w_{i.0}(E_{H_{i.1}}(v,I_{t_{i+1}}))\le 1+log^{3l_3+7}(n)t_i^{-\epsilon_1}\) for every \(v\in V(H_{i.1})\), as required. □

Corollary 6.38. _w_<sub>_i._1</sub> _is edge allowable for_ \((H_i,w_i,t_i,\eta_1)\).

Proof. Just as in Proposition 6.36, it suffices to show that over all _i_-reachable edges _e_, that \(\frac{max_ew_{i.1}(e)}{min_ew_{i.1}(e)}\le log^{500}(n)\). Indeed, \(max_ew_{i.1}(e)\le max_ew_{i.0}(e)\) and by Proposition 6.37, \(min_ew_{i.1}(e)\ge min_ew_{i.0}(e)/2\). Thus

\(\frac{max_ew_{i.1}(e)}{min_ew_{i.1}(e)}\le\frac{4log^{l_1+4l_3+8}(n)}{c_1^5}\le log^{500}(n),\)

as required. □

Corollary 6.39. _w_<sub>_i._1</sub> _is a fractional matching for H_<sub>_i._1</sub>\[_I_<sub>_t<sub>i</sub>_+1</sub>\] _such that_<tbc>

\(w_{i.1}(E_{H_{i.1}}(v,I_{t_{i+1}}))\ge 1-\left(\frac{c_{H_i,v}}{\delta_{H_i,v}}+2.1log^{3l_3+7}(n)t_i^{-\epsilon_1}\right)\)

<tbc>_for every_ \(v\in V(H_{i.1}[I_{t_{i+1}}])\)_. Furthermore,_<tbc>

(6.18) \(w_{i.1}(e)=\left\{\begin{array}{ c c }
(1\pm log^{3l_3+7}(n)t_i^{-\epsilon_1})w_{i.0}(e) & \text{\textit{if}}e\in H_i\text{\textit{is}}i\text{\textit{-reachable}} \\
w_{1^*}(e) & \text{\textit{otherwise.}}
\end{array}\right.\)

<tbc>Proof. That _w_<sub>_i._1</sub> is a fractional matching for _H_<sub>_i._1</sub>\[_I_<sub>_t<sub>i</sub>_+1</sub>\] follows immediately from the construction. From (6.17) we have that for every \(v\in H_i[I_{t_{i+1}}]\),<tbc>

\(w_{i.0}(E_{H_{i.1}}(v,I_{t_{i+1}}))=(1\pm log^{3l_3+7}(n)t_i^{-\epsilon_1})\frac{w_i(E_{H_i}(v,I_{t_{i+1}}))}{1-d_{w_i^o}(v)},\)

<tbc>and by Proposition 6.30 we have that \(1-d_{w_i^o}(v)=\left(1\pm\frac{c_{H_i,v}}{\delta_{H_i,v}}\right)w_i(E_{H_i}(v,I_{t_{i+1}}))\). Thus

\(w_{i.0}(E_{H_{i.1}}(v,I_{t_{i+1}}))=\frac{(1\pm log^{3l_3+7}(n)t_i^{-\epsilon_1})}{\left(1\pm\frac{c_{H_i,v}}{\delta_{H_i,v}}\right)}\ge 1-\left(\frac{c_{H_i,v}}{\delta_{H_i,v}}+log^{3l_3+7}(n)t_i^{-\epsilon_1}\right).\)

Since by Proposition 6.37 we have that \(w_{i.1}(E_{H_{i.1}}(v,I_{t_{i+1}}))\ge\frac{w_{i.0}(E_{H_{i.1}}(v,I_{t_{i+1}}))}{1+log^{3l_3+7}(n)t_i^{-\epsilon_1}}\) , the first claim follows.

Finally, also by Proposition 6.37, for each _e_ which is _i_-reachable, \(w_{i.0}(e)\ge w_{i.1}(e)\ge\frac{w_{i.0}(e)}{1+log^{3l_3+7}(n)t_i^{-\epsilon_1}}\). This yields that \(w_{i.1}(e)=(1\pm log^{3l_3+7}(n)t_i^{-\epsilon_1})w_{i.0}(e)\), as required. □

