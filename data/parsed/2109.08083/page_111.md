<tbc>We have that \(O\left(t_i^{-\epsilon_1}|E_G(v,I_{t_i}\backslash I_{t_{i+1}},*,*)|\right)=O\left(t_i^{1-\epsilon_1}p_\mathrm{gr}^3\right)\) since from (P5) it also follows that \(|E_G(v,I_{t_i}\backslash I_{t_{i+1}},*,*)|\le 1.9c_3t_ip_\mathrm{gr}^3\). Furthermore, for every \(e\in E_G(v,I_{t_i}\backslash I_{t_{i+1}},*,*)\), _e_\\{_v_} contains at least one vertex \(v_1\in I_{t_i}\backslash I_{t_{i+1}}\). Thus \(d_{\omega^o}(v_1)=d_{\omega,G}(v_1)\) and so \(1-d_{\omega^o}(v_1)\le\mathrm{log}^{l_4}(n)t_i^{-\epsilon_1}\). This gives

\(\sum_{e\in E_G(v,I_{t_i}\backslash I_{t_{i+1}},*,*)}\prod_{u\in e\backslash\{v\}}(1-d_{w^o}(u))\le\mathrm{log}^{l_4}(n)t_i^{-\epsilon_1}|E_G(v,I_{t_i}\backslash I_{t_{i+1}},*,*)|\)<br>
\(\le\frac{\mathrm{log}^{l_4}(n)}{t_i^{\epsilon_1}}\cdot c_3|I_{t_i}\backslash I_{t_{i+1}}|p_\mathrm{gr}^3\le 1.9c_3t_i^{1-\epsilon_1}\mathrm{log}^{l_4}(n)p_\mathrm{gr}^3,\)

completing the proof. □

Corollary 6.33. _Given that S is i-reachable and_ \(S\subseteq I_{t_{i+1}}\),<tbc>

\(|V(G'[S])|\ge\frac{0.9c_1t_ip_\mathrm{gr}}{\mathrm{log}^{l_2+l_3+4}(n)}.\)

<tbc>_Furthermore, given that_ (_v,S_<sub>1</sub>_,S_<sub>2</sub>_,S_<sub>3</sub>) _is an open or closed i-reachable tuple such that_ \(S_1\subseteq I_{t_{i+1}}\)_, we have that_

\(|E_{G^\prime}(v,S_1,S_2,S_3)|\ge\frac{0.9c_1^3t_ip_\mathrm{gr}^3}{\mathrm{log}^{4l_3+8}(n)}.\)

Proof. First note that given that _G_ has depth _j_, we have that \(S\subseteq K_{j-1}\backslash K_{j+1}\), and since _S_ is _i_-valid it follows that \(|S|\ge k_{j+1}\). Since \(k_{j-1}\ge t_i\), it follows that \(|S|\ge\frac{t_i}{\mathrm{log}^2(n)}\). Similarly, for (_v,S_<sub>1</sub>_,S_<sub>2</sub>_,S_<sub>3</sub>) we have that \(|S_1|\ge\frac{t_i}{\mathrm{log}^2(n)}\). Furthermore, combining Propositions 6.30 and 6.31, we have for every \(v\in V(G[I_{t_{i+1}}])\) that \(1-d_{\omega^o}(v)\ge 0.99\omega(E_G(v,I_{t_{i+1}}))\), and by Proposition 6.26, that \(0.99\omega(E_G(v,I_{t_{i+1}}))\ge\frac{0.99c_1}{\mathrm{log}^{l_3+2}(n)}\). Additionally by _i_-permissibility we have that \(|V(G[S])|\ge\frac{t_ip_\mathrm{gr}}{\mathrm{log}^{l_2+2}(n)}\) and \(|E_G(v,S_1,S_2,S_3)|\ge\frac{t_ip_\mathrm{gr}^3}{\mathrm{log}^{l_3+2}(n)}\). Thus, by Theorem 6.28, we find that

\(|V(G'[S])|\ge\frac{0.9c_1t_ip_\mathrm{gr}}{\mathrm{log}^{l_2+l_3+4}(n)},\)

and

\(|E_{G^\prime}(v,S_1,S_2,S_3)|\ge\frac{0.9c_1^3t_ip_\mathrm{gr}^3}{\mathrm{log}^{4l_3+8}(n)},\)

as required. □

## 6.4. Reaching _L_<sup>∗</sup>

In this section, starting from (_H_<sub>1∗</sub>_,w_<sub>1∗</sub>) as in Theorem 6.12, we describe the process to reach _L_<sup>∗</sup> via the vortex described in Section 3.1. We summarise our strategy roughly in the following plan. Each iteration of the plan starts with a weighted hypergraph (_H<sub>i</sub>,w<sub>i</sub>_) and subsequently outputs a weighted hypergraph (_H_<sub>_i_+1</sub>_,w_<sub>_i_+1</sub>) which is used as the input for the next iteration. Crucially, we actually start with (_H_<sub>1∗</sub>_,w_<sub>1∗</sub>) but for the purposes of the plan below, by abuse of notation (since _H_<sub>1</sub> and _w_<sub>1</sub> are defined differently elsewhere), we relabel (_H_<sub>1∗</sub>_,w_<sub>1∗</sub>) as (_H_<sub>1</sub>_,w_<sub>1</sub>), only for within the plan below.

