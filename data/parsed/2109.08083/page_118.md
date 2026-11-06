<tbc>using (P4) with that \(|V(H_{i.1}[S])|\le|V(H_i[S])|\) and Corollary 6.41. This gives that<tbc>

\(X^{f,S}=\mathbb{E}(X^{f,S})\pm O\left(f_S^{max}p_\mathrm{gr}^{-1}\mathrm{log}^{8l_3+2l_4+12}(n)t_i^{1-2\epsilon_1}\right).\)

<tbc>Furthermore, \(\sum_{v\in V(H_{i.1}[S])}f_S(v)\ge f_S^\mathrm{min}|V(H_{i.1}[S])|\ge\frac{0.9c_1f_S^\mathrm{min}t_ip_\mathrm{gr}}{\mathrm{log}^{l_2+l_3+4}(n)}\) by Corollary 6.33. Thus

\(\sum_{v\in V(H_{i+1}[S])}f_S(v)=\sum_{v\in V(H_{i.1}[S])}f_S(v)-X^{f,S}\)<br>
\(=\left(\sum_{v\in V(H_{i.1}[S])}f_S(v)(1-p_v^i)\right)\pm O\left(f_S^{max}p_\mathrm{gr}^{-1}\mathrm{log}^{8l_3+2l_4+12}(n)t_i^{1-2\epsilon_1}\right)\)<br>
\(=\left(1\pm O\left(\frac{f_S^\mathrm{max}\mathrm{log}^{l_2+9l_3+2l_4+16}(n)t_i^{-2\epsilon_1}}{c_1f_S^\mathrm{min}p_\mathrm{gr}^2}\right)\right)\sum_{v\in V(H_{i.1}[S])}f_S(v)(1-p_v^i).\)

Since \(t_i^{-\epsilon_1/2}p_\mathrm{gr}^{-2}\checkmark 1\) for all _i_ and \(\frac{f_S^\mathrm{max}}{f_S^\mathrm{min}}\le\mathrm{log}^{500}(n)\), we have that

\(O\left(\frac{f_S^\mathrm{max}\mathrm{log}^{l_2+9l_3+2l_4+16}(n)t_i^{-2\epsilon_1}}{c_1f_S^\mathrm{min}p_\mathrm{gr}^2}\right)\le t_i^{-1.5\epsilon_1}\)

as required to complete the proof. □

Lemma 6.46. _Let v be a vertex that survives the greedy cover. Let_ (_v,S_<sub>1</sub>_,S_<sub>2</sub>_,S_<sub>3</sub>) _be an open or closed i-reachable tuple such that_ \(S_1,S_2,S_3\subseteq I_{t_{i+1}}\)_. Let f be edge allowable for_ \((H_i,w_i,t_i,\eta_1)\) _such that over all edges e that are i-reachable_ \(\frac{\mathrm{max}_ef(e)}{\mathrm{min}_ef(e)}\le\mathrm{log}^{500}(n)\)_. Then_<tbc>

\(f(E_{H_{i+1}}(v,S_1,S_2,S_3))=(1\pm t_i^{-1.5\epsilon_1})\sum_{e\in E_{H_{i.1}}(v,S_1,S_2,S_3)}f(e)(1-p_e^i).\)

<tbc>_In particular,_

\(|E_{H_{i+1}}(v,S_1,S_2,S_3)|=(1\pm t_i^{-1.5\epsilon_1})\sum_{e\in E_{H_{i.1}}(v,S_1,S_2,S_3)}(1-p_e^i).\)

Proof. The proof follows precisely the same strategy as that of Lemma 6.44 with many details exactly the same.

Let _X<sup>f</sup>_ be the total weight removed from _f(E_<sub>_H<sub>i.1</sub>_</sub>(_v,S_<sub>1</sub>_,S_<sub>2</sub>_,S_<sub>3</sub>)) as a result of the random greedy cover for some fixed _i_-reachable tuple (_v,S_<sub>1</sub>_,S_<sub>2</sub>_,S_<sub>3</sub>). Then we have that \(\mathbb{E}(X^f)=\sum_{e\in E_{H_{i.1}}(v,S_1,S_2,S_3)}f(e)p_e^i\). Furthermore, we may write \(X^f=\sum_jX_j^f\) where \(X_j^f\) is the weight removed from _f(E_<sub>_H<sub>i.1</sub>_</sub>(_v,S_<sub>1</sub>_,S_<sub>2</sub>_,S_<sub>3</sub>)) as a result of the choice of edge _e<sub>j</sub>_ for vertex _v<sub>j</sub>_ in the random greedy algorithm. Let \(\mathbb{E}'(X_j^f)\) be the conditional expectation of \(X_j^f\) given that _e_<sub>1</sub>_,...,e_<sub>_j_-1</sub> have been revealed, and let \(Y_j^f:=\sum_{k\le j}(X_k^f-\mathbb{E}'(X_k^f))\). Write _f_<sup>max</sup>:=max<sub>_e\in E_<sub>_H<sub>i.1</sub>_</sub>(_v,S_<sub>1</sub>_,S_<sub>2</sub>_,S_<sub>3</sub>)</sub>_f(e_) and \(f^\mathrm{min}:=\mathrm{min}_{e\in E_{H_{i.1}}(v,S_1,S_2,S_3)}f(e)\). Then \(|Y_j^f-Y_{j-1}^f|\le|X_j^f-\mathbb{E}'(X_j^f)|\le 3f^\mathrm{max}\), since the edge _e<sub>j</sub>_ chosen for _v<sub>j</sub>_ contains at most 3 vertices in _I_<sub>_t<sub>i</sub>_+1</sub> and each of these vertices can be in at most one edge that lies in _E_<sub>_H<sub>i.1</sub>_</sub>(_v,S_<sub>1</sub>_,S_<sub>2</sub>_,S_<sub>3</sub>). Thus, by

