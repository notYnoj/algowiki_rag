<tbc>and

(6.8) \(\sum_{\bar{v}\in\genfrac(){pt}{2}{V(M)}{l}}p_l(\bar{v})-\Gamma=\left(1\pm\frac{\Delta^{-\epsilon}}{2}\right)\left(1\pm\frac{l^2r}{\Delta^{\eta-\psi}}\right)\sum_{\bar{v}\in\genfrac(){pt}{2}{V(H)}{l}}p_l(\bar{v})\prod_{v\in\bar{v}}\frac{d_H(v)}{\Delta}.\)

Claim 6.8. _There exists a distribution on matchings M in H such that with high probability_

\(\Gamma\le\Delta^{-20Lr\epsilon}\sum_{\bar{v}\in\genfrac(){pt}{2}{V(H)}{l}}p_l(\bar{v}).\)

Proof of Claim. We follow the proof of Theorem 6.3 from \[**18**\] which uses a result of Alon and Yuster \[**2**\]. They find _M_ as above by taking a random partition of the vertex set of _H_ into \(V_1,\cdots V_t\), where \(t=\Delta^{20Lr\epsilon}\). Write _H<sub>i</sub>_:=_H_\[_V<sub>i</sub>_\]. Then each _H<sub>i</sub>_ is randomly (edge) partitioned into _H_<sub>_i_1</sub>_,...,H<sub>is</sub>_, where \(s=\Delta^{1-20(r-1+\frac{1}{4L})Lr\epsilon}\). In particular, _t_ is a very small power of \(\Delta\), and _s_ is such that \(\Delta/s\) is also a very small power of \(\Delta\) (but larger than _t_). _M_ is constructed as follows: each _H<sub>ij</sub>_ is partitioned into _q<sub>j</sub>_ matchings and this dictates a partition of _H<sub>i</sub>_ into \(\prod_{j\in[s]}q_j\) matchings. Then _M_ is formed by, for each \(i\in[t]\), independently choosing one of the partition matchings of _H<sub>i</sub>_ uniformly at random from all such matchings of _H<sub>i</sub>_. We write \(M=\bigcup_{i\in[t]}M_i\), where _M<sub>i</sub>_ is the matching in part _V<sub>i</sub>_. Then letting \(\Gamma_i:=\sum_{e\in M_i}\sum_{\bar{v}_2\subseteq e,\bar{v}_{l-2}\in\genfrac(){pt}{2}{V(M)\backslash\bar{v}_2}{l-2}}p(\bar{v}_2\cup\bar{v}_{l-2})\) we have that \(\Gamma\le\sum_{i\in[t]}\Gamma_i\) and<tbc>

\(\Gamma_i\le\mathrm{max}_j\sum_{e\in H_i}\unknown_{e\in H_{ij}}\cdot\mathcal{P}_{e,2},\)

<tbc>where \(\mathcal{P}_{e,2}:=\sum_{\bar{v}_2\subseteq e,\bar{v}_{l-2}\in\genfrac(){pt}{2}{V(M)\backslash\bar{v}_2}{l-2}}p_l(\bar{v}_2\cup\bar{v}_{l-2})\). Furthermore,<tbc>

\(\mathbb{E}(\Gamma_i)\le\frac{1}{s}\sum_{e\in H_i}\mathcal{P}_{e,2}.\)

<tbc>Since the indicator variables \(\unknown_{e\in H_{ij}}\) are independent, we may use Bernstein’s inequality (Lemma 2.8) to bound each \(\Gamma_i\) whp. Write<tbc>

\(Z_e:=\unknown_{e\in H_{ij}}\mathcal{P}_{e,2}\)

<tbc>for each \(e\in H_i\), so \(\{Z_e\}_{e\in H_i}\) are independent variables taking the value<tbc>

\(Z_e=\left\{\begin{array}{ c c }
\mathcal{P}_{e,2} & \text{with probability}1/s,\text{and} \\
0 & \text{otherwise.}
\end{array}\right.\)

<tbc>Furthermore, using (6.7), note that for all _e_,<tbc>

\(|Z_e|\le\mathcal{P}_{e,2}\le r^2\mathrm{max}_{v\in e}p(\{v\})\le\frac{1}{2r^{l-2}\Delta^{2\eta}}\sum_{\bar{v}\in\genfrac(){pt}{2}{V(H)}{l}}p(\bar{v}).\)

<tbc>It follows that

\(\sum_{e\in H_i}\mathbb{E}(Z_e^2)\le\mathrm{max}_{e\in H_i}|Z_e|\sum_{e\in H_i}\mathbb{E}(Z_e)\le\left(\frac{1}{2r^{l-2}\Delta^{2\eta}}\sum_{\bar{v}\in\genfrac(){pt}{2}{V(H)}{l}}p(\bar{v})\right)\mathbb{E}(\Gamma_i).\)

