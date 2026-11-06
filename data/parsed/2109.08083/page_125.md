(_ii)_ _for every edge_ \(e\in H_{i+1}\) _which is i-reachable,_<tbc>

<tbc>\(w_{i+1}(e)=\left(1\pm\left(17.1m_i+2.2\mathrm{log}^{3l_3+7}(n)t_i^{-\epsilon_1}\right)\right)\frac{w_i(e)}{\prod_{u\in e}(1-d_{w_i^o}(u))},\)<tbc>

<tbc>_and every edge_ \(e\in H_{i+1}\) _which is not i-reachable satisfies w_<sub>_i_+1</sub>(_e_)=_w_<sub>1∗</sub>(_e)._<tbc>

(_iii)_ _for every_ (_i_+1)_-valid subset S which is i-reachable, and for polynomially many p<sub>S</sub> as defined in Theorem 6.28,_<tbc>

<tbc>\(\sum_{v\in V(H_{i+1}[S])}p_S(v)=\)<br>
\(\left(1\pm\left(4.1m_i+1.1c_1^{-1}\mathrm{log}^{l_3+2}(n)t_i^{-\epsilon_1}\right)\right)\sum_{v\in V(H_i[S])}p_S(v)(1-d_{w_i^o}(v)),\)<tbc>

<tbc>_and in particular_<tbc>

<tbc>\(|V(H_{i+1}[S])|=\left(1\pm\left(4.1m_i+1.1c_1^{-1}\mathrm{log}^{l_3+2}(n)t_i^{-\epsilon_1}\right)\right)\sum_{v\in V(H_i[S])}(1-d_{w_i^o}(v)).\)<tbc>

<tbc>_Furthermore, we have that_ |_V(H_<sub>_i_+1</sub>\[_S_\])|=|_V(H_<sub>1∗</sub>\[_S_\])| _for every_ (_i_+1)_-valid subset_ \(S\subseteq K_{j^\prime+1}\).<tbc>

(_iv)_ _For every open or closed i-reachable tuple_ (_v,S_<sub>1</sub>_,S_<sub>2</sub>_,S_<sub>3</sub>) _which is an_ (_i_+1)_- permissible tuple, we have that_<tbc>

<tbc>\(w_{i+1}(E_{H_{i+1}}(v,S_1,S_2,S_3))=(1\pm 1.1\mathrm{log}^{3l_3+7}(n)t_i^{-\epsilon_1})\frac{w_i(E_{H_i}(v,S_1,S_2,S_3))}{1-d_{w_i^o}(v)}\)<br>
\(=\left(1\pm\left(\frac{1.1c_{H_i,v}}{\delta_{H_i,v}}+1.2\mathrm{log}^{3l_3+7}(n)t_i^{-\epsilon_1}\right)\right)\frac{w_i(E_{H_i}(v,S_1,S_2,S_3))}{w_i(E_{H_i}(v,I_{t_{i+1}}))},\)<tbc>

<tbc>_and for every open or closed i_+1_-permissible tuple_ (_v,S_<sub>1</sub>_,S_<sub>2</sub>_,S_<sub>3</sub>) _with_ \(\bigcup\{e\backslash\{v\}:e\in E_\mathcal{T}(v,S_1,S_2,S_3)\}\subseteq K_{j^\prime+1}\),<tbc>

<tbc>\(w_{i+1}(E_{H_{i+1}}(v,S_1,S_2,S_3))=w_{1*}(E_{H_{1*}}(v,S_1,S_2,S_3)).\)<tbc>

(_v)_ _For every open or closed i-reachable tuple_ (_v,S_<sub>1</sub>_,S_<sub>2</sub>_,S_<sub>3</sub>) _which is an_ (_i_+1)_-permissible tuple, and polynomially many f which are edge allowable for_ \((H_i,w_i,t_i,\eta_1)\) _and as in Theorem 6.28, we have that_<tbc>

<tbc>\(f(E_{H_{i+1}}(v,S_1,S_2,S_3))=\)<tbc>

<tbc>\(\left(1\pm(16.1m_i+1.1\mathrm{log}^{3l_3+7}(n)t_i^{-\epsilon_1})\right)\sum_{e\in E_{H_i}(v,S_1,S_2,S_3)}f(e)\prod_{u\in e\backslash\{v\}}(1-d_{w_i^o}(u)),\)<tbc>

<tbc>_and in particular,_

\(|E_{H_{i+1}}(v,S_1,S_2,S_3)|=\)<br>
\(\left(1\pm(16.1m_i+1.1\mathrm{log}^{3l_3+7}(n)t_i^{-\epsilon_1})\right)\sum_{e\in E_{H_i}(v,S_1,S_2,S_3)}\prod_{u\in e\backslash\{v\}}(1-d_{w_i^o}(u)).\)

Proof. We have that \(H_{i+1}\subseteq H_{1*}[I_{t_{i+1}}]\) by the strategy, since \(H_i\subseteq H_{1*}[I_{t_i}]\) and Plan 6.34 ensures that we cover all vertices in _I<sub>t<sub>i</sub></sub>_\\_I_<sub>_t_<sub>_i_+1</sub></sub> to reach _H_<sub>_i_+1</sub>. Further more, Proposition 6.50 gives that \(d_{w_{i+1},H_{i+1}}(v)\ge 1-\left(\frac{c_{H_i,v}}{\delta_{H_i,v}}+2.2\mathrm{log}^{3l_3+7}(n)t_i^{-\epsilon_1}\right)\) for all _i_-reachable \(v\in V(H_{i+1})\). Supposing that _v_ is not _i_-reachable, then none

