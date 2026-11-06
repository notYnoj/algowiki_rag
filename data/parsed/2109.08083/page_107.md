<tbc>\(\frac{|I_{t_i}\backslash I_{t_{i+1}}|p_\mathrm{gr}^3}{\mathrm{log}^{l_3}(n)}\ge\frac{t_ip_\mathrm{gr}^3}{\mathrm{log}^{l_3}(n)}\). Furthermore, since \(\omega(e)\ge\frac{c_1}{p_\mathrm{gr}^3t_i\mathrm{log}^2(n)}\) for every edge \(e\in E_G(v,I_{t_i\backslash I_{t_{i+1}}},*,*)\), we therefore have that<tbc>

\(\delta_{\omega^o}(G^o)\ge\frac{c_1}{\mathrm{log}^{l_3+2}(n)}\ge\frac{t_i^{-\psi_1}}{1-t_i^{-1}}.\)

<tbc>It remains to check that the necessary functions discussed above do indeed all satisfy (6.1). Note also that the number of these functions we wish to keep an eye on is polynomial in _t<sub>i</sub>_. The property we need each function _p<sub>l</sub>_ to satisfy is:

(6.15) \(\mathrm{max}_{v\in V(G^o)}p_l(\{v\})\le\frac{\sum_{\bar{v}\in\genfrac(){pt}{2}{V(G^o)}{l}}p_l(\bar{v})}{2\cdot 4^lt_i^{2\eta_1}},\)

where we recall _r_=4 and _L_=16. Note that for every _i_-valid _S_ which is _i_-reachable, since T\[_I<sub>t<sub>i</sub></sub>_\] has depth _j_, we have that \(|S|\ge|I_{k_{j+1}-1}\backslash I_{k_{j+1}}|\ge k_{j+1}\ge\frac{t_i}{\mathrm{log}^2(n)}\).

In order to prove (K1), we wish to show that for every _i_-reachable \(S\subseteq I_{t_{i+1}}\), the function _p<sub>S</sub>_ described in Section 6.3.1.1 with \(\frac{\mathrm{max}_{v\in V(G^o[S])}p_S(v)}{\mathrm{min}_{v\in V(G^o[S])}p_S(v)}\le\mathrm{log}^{500}(n)\) satisfies (6.15). This will give us that (6.12) holds and applying Corollary 6.27, then yields (K1) for every _i_-reachable \(S\subseteq I_{t_{i+1}}\). Now, when _f<sub>S</sub>_=1, we have that \(\mathrm{max}_{v\in V(G^o[S])}p_S(\{v\})=\mathrm{max}_{v\in V(G^o[S])}\unknown_{v\in V(G^o[S])}\le 1\), and by _i_-permissibility and the lower bound on |_S_|,<tbc>

\(\sum_{v\in V(G^o[S])}p_S(\{v\})=|V(G^o[S])|\ge\frac{|S|p_\mathrm{gr}}{\mathrm{log}^{l_2}(n)}\ge\frac{p_\mathrm{gr}t_i}{\mathrm{log}^{l_2+2}(n)},\)

<tbc>for every _i_-reachable _S_, and so (6.15) holds. Considering some other function _f<sub>S</sub>_, we have that<tbc>

\(\mathrm{max}_{v\in V(G^o[S])}p_S(\{v\})=\mathrm{max}_{v\in V(G^o[S])}f_S(v)\unknown_{v\in V(G^o[S])}\le\mathrm{max}_{v\in V(G^o[S])}f_S(v),\)

<tbc>and that

\(\sum_{v\in V(G^o[S])}p_S(\{v\})\ge|V(G^o[S])|\mathrm{min}_{v\in V(G^o[S])}f_S(v)\)<br>
\(\ge\frac{|S|p_\mathrm{gr}\mathrm{min}_{v\in V(G^o[S])}f_S(v)}{\mathrm{log}^{l_2}(n)}\ge\frac{p_\mathrm{gr}t_i\mathrm{min}_{v\in V(G^o[S])}f_S(v)}{\mathrm{log}^{l_2+2}(n)}.\)

Then (6.15) holds, since \(\frac{\mathrm{max}_{v\in V(G[S])}p_S(v)}{\mathrm{min}_{v\in V(G[S])}p_S(v)}\le\mathrm{log}^{500}(n)\).

Similarly, to prove (K2) which only concerns _i_-reachable tuples, note that every open or closed _i_-permissible pair, uses (_S_<sub>1</sub>_,S_<sub>2</sub>_,S_<sub>3</sub>) which is _i_-valid and, by the same reasoning as above, also satisfies \(|S_1|\ge\frac{t_i}{\mathrm{log}^2(n)}\). Then we have that \(q_{(G^o,v,S_1,S_2,S_3)}^{(1)}\), \(q_{(G^o,v,S_1,S_2,S_3)}^{(2)}\), and \(q_{(G^o,v,S_1,S_2,S_3)}^{(3)}\), as described in Section 6.3.1.2, with _f<sub>v</sub>_=1, and every open or closed _i_-permissible tuple (_v,S_<sub>1</sub>_,S_<sub>2</sub>_,S_<sub>3</sub>) all satisfy

\(\mathrm{max}_{\bar{v}\in\genfrac(){pt}{2}{V(G^o)}{l}}q_{(G^o,v,S_1,S_2,S_3)}^{(l)}(\bar{v})\le 1,\)

where \(l\in[3]\), since they are all indicator functions. Furthermore note that

\(q_{(G^o,v,S_1,S_2,S_3)}^{(l)}(V(G^o))\ge|E_{G^o}(v,S_1,S_2,S_3)|\)

