\(|\mathcal{Z}_{i,e,H_0^c}^-(\alpha,\beta,\gamma)|:=\)<br>
\(\left\{\begin{array}{ c c }
(1\pm O(t_0^{-\epsilon}))\sum_{z\in\mathcal{Z}_{i,e,H_0^-(\alpha,\beta,\gamma)}}\prod_{u\in z\backslash e}(1-d_{w_0^o}(u)) & \text{\textit{if}}\alpha\neq 0\text{\textit{and}}\gamma=0, \\
O\left(j_ik_ip_\mathrm{gr}^{12}\right) & \text{\textit{if}}\alpha=0,\beta=0,\gamma=4, \\
O\left(j_ik_ip_\mathrm{gr}^{12}\right) & \text{\textit{if}}\alpha=0,\beta=1,\gamma=3, \\
0 & \text{\textit{otherwise.}}
\end{array}\right.\)

_Finally, for every bad edge e,_<tbc>

<tbc>\(|\mathcal{Z}_{i,e,H_0^c}^2|=O\left(k_it_1p_\mathrm{gr}^{12}\right).\)<tbc>

_(iv)_ _For every_ \(J\in\{X,Y,X+Y,X-Y\}\) _and every J-layer interval_ \(S\subseteq I_{t_1}\) _of size at least_ \(t_0^{1-\epsilon/2}\),<tbc>

<tbc>\(|V_{O/E}^J(H_0^c[S])|=(1\pm O(t_0^{-\epsilon}))\sum_{v\in V_{O/E}^J(H_0[S])}(1-d_{w_0^o}(v)),\)<tbc>

_(v)_ _For every_ \(J\in\{X,YX+Y,X-Y\}\) _and every J-layer interval I<sup>J</sup> contained in I_<sub>_t_<sub>1</sub></sub> _of size at least_ \(t_0^{1-\epsilon/2}\) _and_ \(v\notin J\) _with_ \(v\in V(H_0^c)\),<tbc>

<tbc>\(|E_{H_0^c}(v,I^J,O/E)|=(1\pm O(t_0^{-\epsilon}))\sum_{e\in E_{H_0}(v,I^J,O/E)}\prod_{u\in e\backslash\{v\}}(1-d_{w_0^o}(u)).\)<tbc>

_(vi)_ _When n is odd, for each_ \(AB\in\{OE,EO\}\),<tbc>

<tbc>\(|M_0^o\cap E_{AB}(H_0^o[I_{t_0}\backslash I_{t_{20}}])|=(1\pm t_0^{-\epsilon})\sum_{e\in E_{AB}(H_0^o[I_{t_0}\backslash I_{t_{20}}])}w_0(e).\)

Proof. The proof of (i)-(v) again follows the same strategy as the proof of Theorem 6.28, using Proposition 6.79 in place of Corollary 6.27 to lower bound \(1-d_{w_0^o}(u)\) for each \(u\in I_{t_1}\). For (vi) we appeal directly to Theorem 6.2. By the same reasoning as for Theorem 6.28, we know that the hypotheses are satisfied. Let \(q_{AB}:E(H_0^o)\rightarrow\mathbb{R}_{\ge 0}\) be defined by \(q_{AB}(e)=\unknown_{e\in E_{AB}(H_0^o[I_{t_0}\backslash I_{t_{20}}])}\). Then \(q_{AB}(E(H_0^o))=|E_{AB}(H_0^o[I_{t_0}\backslash I_{t_{20}}])|\) and \(\mathrm{max}_{e\in E(H_0^o)}q(e)=1\) for every \(AB\in\{OE,EO\}\). It suffices to show that \(|E_{AB}(H_0^o[I_{t_0}\backslash I_{t_{20}}])|\ge\frac{t_0^{1+\eta}}{1-t_0^{-1}}\) for each \(AB\in\{OE,EO\}\). First note that by Fact 3.30 (iii), for each \(v\in(I_{t_0}\backslash I_{t_1})\cap(X\cup Y)\), there are at least _n/_50 wrap around edges of each relevant type which contain only other vertices in _I_<sub>_t_<sub>1</sub></sub>\\_I_<sub>_t_<sub>20</sub></sub>. That is, \(|E_\mathcal{T}(v,I_v^*,O/E)|\ge\frac{t_0}{50}\) for each \(v\in(V(\mathcal{T})\backslash I_{t_1})\cap(X\cup Y)\), where \(I_v^*\) is the relevant layer interval that counts only edges with all other vertices in _I_<sub>_t_<sub>1</sub></sub>\\_I_<sub>_t_<sub>20</sub></sub>. Then by Lemma 6.73(v), there exists a constant _c_<sub>1</sub> such that \(|E_{H_0^o}(v,I_v^*,O/E)|=|E_{H_0}(v,I_v^*,O/E)|\ge c_1t_0p_\mathrm{gr}^3\) for every \(v\in(V(H_0)\backslash I_{t_1})\cap X\). Furthermore, by Lemma 6.73(iv), there exists a constant _c_<sub>2</sub> such that \(|(V(H_0^o)\backslash I_{t_1})\cap X|=|(V(H_0)\backslash I_{t_1})\cap X|\ge c_2t_0p_\mathrm{gr}\). Then

(6.22) \(|E_{AB}(H_0^o[I_{t_0}\backslash I_{t_{20}}])|\ge\sum_{v\in(V(H_0^o)\backslash I_{t_1})\cap X}|E_{H_0^o}(v,I_v^*,O/E)|\ge c_1c_2t_0^2p_\mathrm{gr}^4,\)

