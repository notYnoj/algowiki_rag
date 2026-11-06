<tbc>We conclude this section with two more corollaries which will be extremely useful in the next section. Both will be useful for our ‘cover’ step going from _H<sub>i</sub>_ to _H_<sub>_i_+1</sub> which is ‘Step 3’ of Plan 6.34 introduced at the start of the next section.

Corollary 6.32. _Given that_ \((G,\omega)\) _is i-permissible and we obtain_ \(G'\) _from G as in Theorem 6.28, the following properties hold for_ \(G'\):

(_G1)_ \(|V(G'[I_{t_i}\backslash I_{t_{i+1}}])|\le 2.1c_2\mathrm{log}^{l_4}(n)t_i^{1-\epsilon_1}p_\mathrm{gr}\).<tbc>

_(G2)_ _For every_ \(v\in V(G')\), \(d_{G^\prime}(v)\ge|E_{G^\prime}(v,I_{t_{i+1}})|\ge\frac{0.9c_1^3t_ip_\mathrm{gr}^3}{\mathrm{log}^{4l_3+6}(n)}\).<tbc>

_(G3)_ _For every_ \(v\in V(G'[I_{t_{i+1}}])\), \(|E_{G^\prime}(v,I_{t_i}\backslash I_{t_{i+1}},*,*)|\le 2c_3t_i^{1-\epsilon_1}\mathrm{log}^{l_4}(n)p_\mathrm{gr}^3\).

Proof. By (6.11) we have that<tbc>

\(|V(G'[I_{t_i}\backslash I_{t_{i+1}}])|=|V(G[I_{t_i}\backslash I_{t_{i+1}}])|-(1\pm t_i^{-\epsilon_1})\sum_{v\in V(G[I_{t_i}\backslash I_{t_{i+1}}])}d_{w^o}(v).\)

<tbc>By (P2) it follows that

\(|V(G'[I_{t_i}\backslash I_{t_{i+1}}])|\le|V(G[I_{t_i}\backslash I_{t_{i+1}}])|\)<br>
\(-(1-t_i^{-\epsilon_1})\sum_{v\in V(G[I_{t_i}\backslash I_{t_{i+1}}])}(1-\mathrm{log}^{l_4}(n)t_i^{-\epsilon_1})\)<br>
\(\le 2.1c_2\mathrm{log}^{l_4}(n)t_i^{1-\epsilon_1}p_\mathrm{gr},\)

where the last line follows using (P4) and that \(|I_{t_i}\backslash I_{t_{i+1}}|\le 2t_i\).

Now, we also know from (K2) that

\(d_{G^\prime}(v)=|E_{G^\prime}(v,I_{t_i})|\ge|E_{G^\prime}(v,I_{t_{i+1}})|\)<br>
\(=(1\pm\mathrm{log}^{3l_3+7}(n)t_i^{-\epsilon_1})\sum_{e\in E_G(v,I_{t_{i+1}})}\prod_{u\in e\backslash\{v\}}(1-d_{\omega^o}(u)),\)

noting that \(e\backslash\{v\}\subseteq I_{t_{i+1}}\) for every \(e\in E_G(v,I_{t_{i+1}})\). Furthermore, for each \(e\in E_G(v,I_{t_{i+1}})\) and \(u\in e\backslash\{v\}\) we have by Proposition 6.30 that \(1-d_{\omega^o}(u)=(1\pm\frac{c_G}{\delta_G})\omega(E_G(u,I_{t_{i+1}}))\). Hence,<tbc>

\(d_{G^\prime}(v)\ge\left(1-\mathrm{log}^{3l_3+7}(n)t_i^{-\epsilon_1}\right)\left(1-3.1\frac{c_G}{\delta_G}\right)\sum_{e\in E_G(v,I_{t_{i+1}})}\prod_{u\in e\backslash\{v\}}\omega(E_G(u,I_{t_{i+1}})).\)

<tbc>Since \((G,\omega)\) is _i_-permissible we have by Corollary 6.27 that \(\omega(E_G(u,I_{t_{i+1}}))\ge\frac{c_1}{\mathrm{log}^{l_3+2}(n)}\) for every \(u\in V(G[I_{t_{i+1}}])\) and by (P5) that \(|E_G(v,I_{t_{i+1}})|\ge\frac{p_\mathrm{gr}^3t_i}{\mathrm{log}^{l_3}(n)}\) for every \(v\in V(G)\). This yields that<tbc>

\(d_{G^\prime}(v)\ge\left(1-\mathrm{log}^{3l_3+7}(n)t_i^{-\epsilon_1}\right)\left(1-3.1\frac{c_G}{\delta_G}\right)\frac{c_1^3t_ip_\mathrm{gr}^3}{\mathrm{log}^{4l_3+6}(n)}.\)

<tbc>By Proposition 6.31 the second claim follows. Finally, considering a vertex \(v\in V(G'[I_{t_{i+1}}])\), by Proposition 6.17 we have that

\(|E_{G^\prime}(v,I_{t_i}\backslash I_{t_{i+1}},*,*)|\le\sum_{e\in E_G(v,I_{t_i}\backslash I_{t_{i+1}},*,*)}\prod_{u\in e\backslash\{v\}}(1-d_{w^o}(u))\)<br>
\(+O\left(t_i^{-\epsilon_1}|E_G(v,I_{t_i}\backslash I_{t_{i+1}},*,*)|\right).\)

