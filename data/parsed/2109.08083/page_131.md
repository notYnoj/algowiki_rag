<tbc>again using Proposition 6.55,<tbc>

\(w_{l+1}(e)=\left(1\pm\frac{137.1c_3}{(\delta_*^-)^3}log^{m^*+4l_3+8}(n)t_l^{-\epsilon_1}\right)\frac{w_l(e)}{\prod_{u\in e}w_l(E_{H_l}(u,I_{t_{l+1}}))}.\)

<tbc>We claim that for every \(i\le l\),

\(\frac{w_i(e)}{\prod_{u\in e}w_i(E_{H_i}(u,I_{t_{l+1}}))}=\)<br>
\(\left(1\pm\frac{137.1c_3}{(\delta_*^-)^3}log^{m^*+4l_3+8}(n)t_l^{-\epsilon_1}\right)\frac{w_{i-1}(e)}{\prod_{u\in e}w_{i-1}(E_{H_{i-1}}(u,I_{t_{l+1}}))}.\)

Indeed, by Lemma 6.52(iv),

(6.21) \(w_i(E_{H_i}(u,I_{t_{l+1}}))=(1\pm 1.1log^{3l_3+7}(n)t_i^{-\epsilon_1})\frac{w_{i-1}(E_{H_{i-1}}(u,I_{t_{l+1}}))}{1-d_{w_{i-1}^o}(u)},\)

for each \(u\in e\). Then using Lemma 6.52 (ii) again the claim follows. Subsequently, we see that

\(\frac{w_l(e)}{\prod_{u\in e}(1-d_{w_l^o}(u))}=\)<br>
\(\prod_{t^*(k_{j-3})\le i\le l}\left(1\pm\frac{137.1c_3}{(\delta_*^-)^3}log^{m^*+4l_3+8}(n)t_l^{-\epsilon_1}\right)\frac{w_{1^*}(e)}{\prod_{u\in e}(1-d_{w_{1^*}^o}(u))}.\)

Since _H<sub>l</sub>_ has depth _j_, we have that \(l-t^*(k_{j-3})\le 40loglog(n)\). Thus,

\(w_{l+1}(e)=\)<br>
\(\left(1\pm\frac{137.1c_3}{(\delta_*^-)^3}log^{m^*+4l_3+8}(n)t_l^{-\epsilon_1}\right)^{l-t^*(k_{j-3})+1}\frac{w_{1^*}(e)}{\prod_{u\in e}w_{1^*}(E_{H_{1^*}}(u,I_{t_{l+1}}))}\)<br>
\(=\left(1\pm\frac{137.1c_3}{(\delta_*^-)^3}log^{m^*+4l_3+9}(n)t_l^{-\epsilon_1}\right)\frac{w_{1^*}(e)}{\prod_{u\in e}w_{1^*}(E_{H_{1^*}}(u,I_{t_{l+1}}))}.\)

□

Corollary 6.58. _Suppose that_ (_H<sub>i</sub>,w<sub>i</sub>_) _is i-permissible for every_ \(i\le l\)_. Furthermore, suppose that H<sub>l</sub> has depth j and that_ \(e\in H_{l+1}\) _is l-reachable. Then, recalling that l_<sub>1</sub>=10_, we have that_<tbc>

\(\frac{c_{1,1}^*}{2t_{l+1}p_\mathrm{gr}^3log^2(n)}\le w_{l+1}(e)\le\frac{2c_{1,2}^*log^9(n)}{(c_{1,5}c_{1,1}^*)^4t_{l+1}p_\mathrm{gr}^3}.\)

<tbc>Proof. By Lemma 6.57 we have that<tbc>

\(w_{l+1}(e)=(1\pm o(1))\frac{w_{1^*}(e)}{\prod_{u\in e}w_{1^*}(E_{H_{1^*}}(u,I_{t_{l+1}}))}.\)

<tbc>Each \(w_{1^*}(E_{H_{1^*}}(u,I_{t_{l+1}}))\le 1\), so certainly \(w_{l+1}(e)\ge w_{1^*}(e)/2\). Now, given that _e_ is _l_-reachable, and _H<sub>l</sub>_ has depth _j_, we have that _e_ is of type (4,0,0)<sub>_j_-1</sub>, \((\alpha,\beta,0)_j\) or \((\alpha,\beta,0)_{j+1}\) for \(\alpha\neq 0\). By Theorem 6.12 it follows that \(\frac{c_{1,1}^*}{k_{j-1}p_\mathrm{gr}^3log(n)}\le w_{1^*}(e)\le\frac{c_{1,2}^*}{k_{j+1}p_\mathrm{gr}^3log(n)}\) for every _l_-reachable \(e\in H_{l+1}\). Thus we have that

\(w_{l+1}(e)\ge\frac{c_{1,1}^*}{2k_{j-1}p_\mathrm{gr}^3log(n)}\ge\frac{c_{1,1}^*}{2t_{l+1}p_\mathrm{gr}^3log^2(n)}.\)

