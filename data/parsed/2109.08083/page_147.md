<tbc>**6.5.4.** _H_<sub>0</sub> **to** _H_<sub>1</sub>**.** We now repeat the process above, this time with (_H_<sub>0</sub>_,w_<sub>0</sub>) in place of (_H,w<sub>H</sub>_), and _I_<sub>_t_<sub>1</sub></sub> as the new ‘target interval’ in place of _I_<sub>_t_<sub>0</sub></sub>. We start with some useful properties to note for this process.

Proposition 6.79. _For each_ \(v\in V(H_0)\), \(w_0(E_{H_0}(v,I_{t_1}))\ge(1-O(p_\mathrm{gr}^{-2}t_0^{-\epsilon}))\frac{1}{20}\).

Proof. We have by Proposition 6.78 that for each \(v\in V(H_0)\),

\(w_0(E_{H_0}(v,I_{t_1}))=(1\pm 2.2C_0p_\mathrm{gr}^{-2}t_0^{-\epsilon})\frac{w_H(E_H(v,I_{t_1}))}{w_H(E_H(v,I_{t_0}))}.\)

Now, from properties of T , in particular Fact 3.30, and Theorem 3.28, we know that \(w_H(E_H(v,I_{t_0}))\le\frac{2}{3}+O(\alpha_G)\), and that \(w_H(E_H(v,I_{t_1}))\ge\frac{1}{30}-O(\alpha_G)\). Thus, the result follows. □

Corollary 6.80. _For each_ \(v\in V(H_0[I_{t_1}])\)_, we have that_<tbc>

\(1-d_{w_0^o}(v)=(1\pm 44.1C_0p_\mathrm{gr}^{-2}t_0^{-\epsilon})w_0(E_{H_0}(v,I_{t_1})).\)

<tbc>Proof. By Proposition 6.79, we have that \(w_0(E_{H_0}(v,I_{t_1}))\ge(1-o(1))\frac{1}{20}\). Furthermore, we have that for each \(v\in V(H_0[I_{t_1}])\) that \(d_{w_0^o}(v)+w_0(E_{H_0}(v,I_{t_1}))=1\pm 2.2C_0p_\mathrm{gr}^{-2}t_0^{-\epsilon}\). Thus,

\(1-d_{w_0^o}(v)=w_0(E_{H_0}(v,I_{t_1}))\pm 2.2C_0p_\mathrm{gr}^{-2}t_0^{-\epsilon}=(1\pm 44.1C_0p_\mathrm{gr}^{-2}t_0^{-\epsilon})w_0(E_{H_0}(v,I_{t_1})),\)

as required. □

Proposition 6.81. _There exists a matching_ \(M_0^o\) _in_ \((H_0^o,w_0^o)\) _such that letting_ \(H_0^c:=H_0[V(H_0)\backslash V(M_0^o)]\)_, we have that_

(_i)_ _every_ 0_-valid subset_ \(S\subseteq I_{t_1}\) _satisfies_<tbc>

<tbc>\(|V(H_0^c[S])|=(1\pm O(t_0^{-\epsilon}))\sum_{v\in V(H_0[S])}(1-d_{w_0^o}(v)),\)<tbc>

<tbc>_and for any vertex allowable function_ \(p_S(v):V(H_0)\rightarrow\mathbb{R}_{\ge 0}\) _for_ \((H_0,w_0,t_0,\eta)\) _such that_ \(p_S(v)=f_S(v)\unknown_{v\in V(H_0[S])}\),<tbc>

<tbc>\(\sum_{v\in V(H_0^c[S])}p_S(v)=(1\pm O(t_0^{-\epsilon}))\sum_{v\in V(H_0[S])}p_S(v)(1-d_{w_{H_0^o}}(v)),\)<tbc>

_(ii)_ _every open and closed_ T _-valid tuple_ (_v,S_<sub>1</sub>_,S_<sub>2</sub>_,S_<sub>3</sub>) _with_ \(S_1,S_2,S_3\subseteq I_{t_1}\) _satisfies_<tbc>

<tbc>\(|E_{H_0^c}(v,S_1,S_2,S_3)|=(1\pm O(t_0^{-\epsilon}))\sum_{e\in E_{H_0}(v,S_1,S_2,S_3)}\prod_{u\in e\backslash\{v\}}(1-d_{w_0^o}(u)),\)<tbc>

<tbc>_and for any v-edge allowable function_ \(f_v:E(H_0)\rightarrow\mathbb{R}_{\ge 0}\) _for_ \((H,w_H,t_0,\eta)\) _such that f<sub>v</sub>(e_)=0 _wherever_ \(v\notin e\),<tbc>

<tbc>\(f_v(E_{H_0^c}(v,S_1,S_2,S_3))=(1\pm O(t_0^{-\epsilon}))\sum_{e\in E_{H_0}(v,S_1,S_2,S_3)}f_v(e)\prod_{u\in e\backslash\{v\}}(1-d_{w_{H_0^o}}(u)),\)<tbc>

_(iii)_ _for every_ \(i\in[c_g]\),<tbc>

<tbc>\(|\mathcal{Z}_{i,e,H_0^c}^+(\alpha,\beta,\gamma)|:=\left\{\begin{array}{ c c }
(1\pm O(t_0^{-\epsilon}))\sum_{z\in\mathcal{Z}_{i,e,H_0}^+(\alpha,\beta,\gamma)}\prod_{u\in z\backslash e}(1-d_{w_0^o}(u)) & \text{\textit{if}}e\text{\textit{is a bad edge}}, \\
O\left(k_it_1p_\mathrm{gr}^{12}\right) & \text{\textit{if}}\alpha=0\text{\textit{,}}\beta=1\text{\textit{,}}\gamma=3\text{\textit{,}} \\
0 & \text{\textit{otherwise}}.
\end{array}\right.\)<tbc>

