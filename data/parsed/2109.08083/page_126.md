<tbc>of the edges in _E<sub>H<sub>i</sub></sub>(v,I<sub>t<sub>i</sub></sub>_) are _i_-reachable, and thus we have that _d_<sub>_w_<sub>_i_+1</sub>_,H_<sub>_i_+1</sub></sub>(_v_)=_w_<sub>_i_+1</sub>(_E_<sub>_H_<sub>_i_+1</sub></sub>(_v,I_<sub>_t_<sub>_i_+1</sub></sub>))=_w_<sub>1∗</sub>(_E_<sub>_H_<sub>1∗</sub></sub>(_v,I_<sub>_t_<sub>_i_+1</sub></sub>))=_w_<sub>1∗</sub>(_E_<sub>_H_<sub>1∗</sub></sub>(_v,I_<sub>_t_<sub>1</sub></sub>))=_d_<sub>_w_<sub>1∗</sub>_,H_<sub>1∗</sub></sub>(_v_).

In general it is clear, by nature of Plan 6.34, that the lemma holds for all properties we consider when variables are not _i_-reachable. Considering \(e\in H_{i+1}\) that is _i_-reachable, we have by (6.20) and the definitions of _w_<sub>_i_+1</sub> and _w_<sub>_i,_2</sub> that \(w_{i+1}(e)=\frac{w_{i,2}(e)}{d_i^*}=(1\pm 1.1t_i^{-1.5\epsilon_1})w_{i,2}(e)=(1\pm 1.1t_i^{-1.5\epsilon_1})\frac{w_{i,1}(e)}{1-p_e^i}\). By Proposi tion 6.51, then, we have that \(w_{i+1}(e)=(1\pm 1.1t_i^{-1.5\epsilon_1})(1\pm 1.1p_e^i)w_{i,1}(e)\). Then by Corollary 6.39, \(w_{i+1}(e)=(1\pm(1.1p_e^i+2.2\mathrm{log}^{3l_3+7}(n)t_i^{-\epsilon_1}))w_{i,0}(e)\). Since \(e\subseteq I_{t_{i+1}}\) and _e_ is _i_-reachable, we further have that \(w_{i+1}(e)=(1\pm(1.1p_e^i+2.2\mathrm{log}^{3l_3+7}(n)t_i^{-\epsilon_1}))\frac{w_i(e)}{\prod_{u\in e}(1-d_{w_i^o}(u))}\). Then by the upper bound on \(p_e^i\) given in Propo sition 6.51, we have that (ii) follows.

To see (iii) for each (i+1)-valid subset which is _i_-reachable, we have by Lemma 6.44 that \(\sum_{v\in V(H_{i+1}[S])}p_S(v)=(1\pm t_i^{-1.5\epsilon_1})\sum_{v\in V(H_{i,1}[S])}p_S(v)(1-p_v^i)=(1\pm t_i^{-1.5\epsilon_1})(1\pm\mathrm{max}_vp_v^i)\sum_{v\in V(H_{i,1}[S])}p_S(v)\). Then by Theorem 6.28(K1) we have that<tbc>

\(\sum_{v\in V(H_{i,1}[S])}p_S(v)=(1\pm c_1^{-1}\mathrm{log}^{l_3+2}(n)t_i^{-\epsilon_1})\sum_{v\in V(H_i[S])}p_S(v)(1-d_{w_i^o}(v)).\)

<tbc>Thus using the upper bound on \(p_v^i\) given by Proposition 6.51 we have that (iii) follows. In particular, taking \(p_S=\unknown_{v\in H_i[S]}\), we have that

\(|V(H_{i+1}[S])|=(1\pm(4.1m_i+1.1c_1^{-1}\mathrm{log}^{l_3+2}(n)t_i^{-\epsilon_1}))\sum_{v\in V(H_i[S])}(1-d_{w_i^o}(v)),\)

as claimed.

For (iv) we have by Proposition 6.50 that

\(w_{i+1}(E_{H_{i+1}}(v,S_1,S_2,S_3))=\)<br>
\((1\pm 1.1\mathrm{log}^{3l_3+7}(n)t_i^{-\epsilon_1})\sum_{e\in E_{H_i}(v,S_1,S_2,S_3)}w_{i,0}(e)\prod_{u\in e\backslash\{v\}}(1-d_{w_i^o}(u)).\)

Since the edges considered all have their vertices contained in _I_<sub>_t_<sub>_i_+1</sub></sub>, but are also _i_-reachable, we have that \(w_{i,0}(e)\prod_{u\in e\backslash\{v\}}(1-d_{w_i^o}(u))=\frac{w_i(e)}{1-d_{w_i^o}(v)}\) for each \(e\in E_{H_i}(v,S_1,S_2,S_3)\), and hence<tbc>

\(\sum_{e\in E_{H_i}(v,S_1,S_2,S_3)}w_{i,0}(e)\prod_{u\in e\backslash\{v\}}(1-d_{w_i^o}(u))=\frac{w_i(E_{H_i}(v,S_1,S_2,S_3))}{1-d_{w_i^o}(v)}.\)

<tbc>Then by Proposition 6.30, since \(v\in V(H_{i+1})\),

\(\frac{w_i(E_{H_i}(v,S_1,S_2,S_3))}{1-d_{w_i^o}(v)}=\left(1\pm\frac{1.1c_{H_i,v}}{\delta_{H_i,v}}\right)\frac{w_i(E_{H_i}(v,S_1,S_2,S_3))}{w_i(E_{H_i}(v,I_{t_{i+1}}))},\)

and the result follows.

Finally, to see (v), we have from Lemma 6.46 that

\(f(E_{H_{i+1}}(v,S_1,S_2,S_3))=\left(1\pm t_i^{-1.5\epsilon_1}\right)\sum_{e\in E_{H_{i,1}}(v,S_1,S_2,S_3)}f(e)(1-p_e^i)\)<br>
\(=(1\pm t_i^{-1.5\epsilon_1})(1\pm\mathrm{max}_ep_e^i)f(E_{H_{i,1}}(v,S_1,S_2,S_3)).\)

