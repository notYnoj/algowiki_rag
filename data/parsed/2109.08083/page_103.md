<tbc>Definition 6.21 (_l_<sub>1</sub>_,l_<sub>2</sub>_,l_<sub>3</sub>_,l_<sub>4</sub>_,c_<sub>1</sub>_,c_<sub>2</sub>_,c_<sub>3</sub>). Let _l_<sub>1</sub>:=10, _l_<sub>2</sub>:=3, _l_<sub>3</sub>:=7 and \(l_4:=80log\left(\frac{2}{\delta_*^-}\right)\). We use this notation for powers of logs to clarify the source of various terms in subsequent calculations. We also fix absolute constants \(c_1:=\frac{c_{1,1}^*}{2}\) , _c_<sub>2</sub>:=_c_<sub>1,4</sub> and _c_<sub>3</sub>:=max{1,2_c_<sub>1,6</sub>} (where \(c_{1,1}^*\) is an absolute constant defined in Theorem 6.12 and _c_<sub>1,4</sub> and _c_<sub>1,6</sub> are absolute constants defined in Theorem 6.1).

We now come to the key definition for the remainder of this chapter.

Definition 6.22 (Graph permmissibility). Suppose that T\[_I<sub>t<sub>i</sub></sub>_\] has depth _j_. We say that a weighted subgraph \((G,\omega)\) is _i_-permissible if the following all hold:

(P1) \(G\subseteq H_{1*}[I_{t_i}]\),<tbc>

(P2) for every \(v\in V(G)\) which is (_i_-1)-reachable<tbc>

<tbc>\(1\ge d_{\omega,G}(v)\ge 1-log^{l_4}(n)t_i^{-\epsilon_1},\)<tbc>

<tbc>and if _v_ is not (_i_-1)-reachable, then<tbc>

<tbc>\(d_{\omega,G}(v)=d_{w_{1*},H_{1*}}(v).\)<tbc>

(P3) for every edge \(e\in G\) which is (_i_-1)-reachable,<tbc>

<tbc>\(\frac{c_1}{p_\mathrm{gr}^3t_ilog^2(n)}\le\omega(e)\le\frac{log^{l_1}(n)}{p_\mathrm{gr}^3t_i},\)<tbc>

<tbc>and every edge \(e\in G\) which is not (_i_-1)-reachable satisfies \(\omega(e)=w_{1*}(e)\).<tbc>

(P4) for every _i_-valid subset _S_ which is (_i_-1)-reachable,<tbc>

<tbc>\(\frac{|S|p_\mathrm{gr}}{log^{l_2}(n)}\le|V(G[S])|\le c_2|S|p_\mathrm{gr},\)<tbc>

<tbc>and for every _i_-valid subset \(S\subseteq K_{j+1}\), |_V(G_\[_S_\])|=|_V(H_<sub>1∗</sub>\[_S_\])|.<tbc>

(P5) for every open or closed (_i_-1)-reachable tuple (_v,S_<sub>1</sub>_,S_<sub>2</sub>_,S_<sub>3</sub>) which is an _i_-permissible tuple, we have that<tbc>

<tbc>\(\frac{|S_1|p_\mathrm{gr}^3}{log^{l_3}(n)}\le|E_G(v,S_1,S_2,S_3)|\le c_3|S_1|p_\mathrm{gr}^3,\)<tbc>

<tbc>and for every open or closed _i_-permissible tuple (_v,S_<sub>1</sub>_,S_<sub>2</sub>_,S_<sub>3</sub>) such that \(\bigcup\{e\backslash\{v\}:e\in E_\mathcal{T}(v,S_1,S_2,S_3)\}\subseteq K_{j+1}\), we have that |_E<sub>G</sub>(v,S_<sub>1</sub>_,S_<sub>2</sub>_,S_<sub>3</sub>)|=|_E_<sub>_H_<sub>1∗</sub></sub>(_v,S_<sub>1</sub>_,S_<sub>2</sub>_,S_<sub>3</sub>)|.

We now show that Theorem 6.12 implies that (_H_<sub>1∗</sub>_,w_<sub>1∗</sub>) is 1-permissible.

Lemma 6.23. (_H_<sub>1∗</sub>_,w_<sub>1∗</sub>) _is_ 1_-permissible, and in particular we have that_ \(c_{H_{1*}}\le t_1^{-\epsilon_1}\)_, and there exist constants_ \(\delta_{1*}^\pm>0\) _such that_

\(\delta_{1*}^-\le w_{1*}(E_{H_{1*}}(v,I_{t_2}))\le\delta_{1*}^+.\)

Proof. We consider the properties of (_H_<sub>1∗</sub>_,w_<sub>1∗</sub>) given in the statement of Theorem 6.12 to deduce the lemma. First note that 6.12(i) tells us immediately that \(c_{H_{1*}}\le t_1^{-\epsilon_1}\), and in particular implies that (P2) holds. It is also clear that (P1) holds. (P3) by Theorem 6.12(ii) and (P4) holds by Theorem 6.12(iii) and Theorem 6.1(iii). Similarly, (P5) holds by Theorem 6.12(iv) and Theorem 6.1(iv).

