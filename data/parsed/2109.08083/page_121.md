<tbc>for every \(e\in H_i\) which is (_i_-1)-reachable, and _w<sub>i</sub>(e_)=_w_<sub>1∗</sub>(_e_) otherwise. If \(d_{i,0}^*\le 1\) we have that \(w_{i,2}(e)=\frac{w_{i,0}(e)}{1-p_e^i}\) and if \(d_{i,0}^*>1\) we have that \(w_{i,2}(e)=\frac{w_{i,0}(e)}{d_{i,0}^*(1-p_e^i)}\). By Proposition 6.37 and Corollary 6.43 we have that \(w_{i,2}(e)=(1\pm o(1))w_{i,0}(e)\). Thus by Proposition 6.35 we have that

\(w_i(e)\le w_{i,2}(e)\le\frac{1.2w_i(e)log^{4l_3+8}(n)}{c_1^4}.\)

For those edges \(e\in H_i[I_{t_{i+1}}]\) which are (_i_-1)-reachable, the result follows immediately. This covers all _i_-reachable edges unless _H_<sub>_i_-1</sub> had depth _j_-1 and _H<sub>i</sub>_ has depth _j_ for some _j_. In this case all edges _e_ which are _i_-reachable but not (_i_-1)-reachable are of type \((\alpha,\beta,0)_{j+1}\) with \(\alpha\neq 0\). Thus by Theorem 6.12 we have \(\frac{c_{1,1}^*}{k_{j+1}p_\mathrm{gr}^3log(n)}\le w_i(e)=w_{1*}(e)\le\frac{c_{1,2}^*}{k_{j+1}p_\mathrm{gr}^3log(n)}\). Furthermore, in this case we have that _t<sub>i</sub>=k_<sub>_j_-1</sub>=_k_<sub>_j_+1</sub>log<sup>2</sup>(_n_), so in particular, \(\frac{c_{1,1}^*log(n)}{t_ip_\mathrm{gr}^3}\le w_i(e)=w_{1*}(e)\le\frac{c_{1,2}^*log(n)}{t_ip_\mathrm{gr}^3}\) and the result still holds. □

Then we have the following corollary to Lemma 6.46:

Corollary 6.49. _Let_ \(v\in V(H_{i+1})\) _and_ \(S_1,S_2,S_3\subseteq I_{t_{i+1}}\)_. Let_ (_v,S_<sub>1</sub>_,S_<sub>2</sub>_,S_<sub>3</sub>) _be an open or closed i-reachable tuple. Then_

\(w_{i,2}(E_{H_{i+1}}(v,S_1,S_2,S_3))=(1\pm t_i^{-1.5\epsilon_1})w_{i,1}(E_{H_{i,1}}(v,S_1,S_2,S_3)).\)

Proof. By Proposition 6.48, _w_<sub>_i,_2</sub> is edge allowable for \((H_i,w_i,t_i,\eta_1)\) and \(\frac{\mathrm{max}_ew_{i,2}(e)}{\mathrm{min}_ew_{i,2}(e)}\le log^{500}(n)\) over all _i_-reachable edges. Then by Lemma 6.46 we have that for (_v,S_<sub>1</sub>_,S_<sub>2</sub>_,S_<sub>3</sub>) an open or closed _i_-reachable tuple such that \(S_1,S_2,S_3\subseteq I_{t_{i+1}}\),

\(w_{i,2}(E_{H_{i+1}}(v,S_1,S_2,S_3))=(1\pm t_i^{-1.5\epsilon_1})\sum_{e\in E_{H_{i,1}}(v,S_1,S_2,S_3)}w_{i,2}(e)(1-p_e^i)\)<br>
\(=(1\pm t_i^{-1.5\epsilon_1})\sum_{e\in E_{H_{i,1}}(v,S_1,S_2,S_3)}\frac{1-p_e^i}{1-p_e^i}w_{i,1}(e)\)<br>
\(=(1\pm t_i^{-1.5\epsilon_1})\sum_{e\in E_{H_{i,1}}(v,S_1,S_2,S_3)}w_{i,1}(e)\)<br>
\(=(1\pm t_i^{-1.5\epsilon_1})w_{i,1}(E_{H_{i,1}}(v,S_1,S_2,S_3)).\)(6.19)

□

Now, since \(V(H_{i+1})\subseteq I_{t_{i+1}}\), we have that \(d_{w_{i,2},H_{i+1}}(v)=w_{i,2}(E_{H_{i+1}}(v,I_{t_{i+1}}))=(1\pm t_i^{-1.5\epsilon_1})w_{i,1}(E_{H_{i,1}}(v,I_{t_{i+1}}))\). By Corollary 6.39 \(1\ge w_{i,1}(E_{H_{i,1}}(v,I_{t_{i+1}}))\ge 1-\left(\frac{c_{H_i,v}}{\delta_{H_i,v}}+2.1log^{3l_3+7}(n)t_i^{-\epsilon_1}\right)\), so \(d_{w_{i,2},H_{i+1}}(v)\le 1+t_i^{-1.5\epsilon_1}\) for every \(v\in V(H_{i+1})\). Let

(6.20) \(d_i^*:=\mathrm{max}_{v\in V(H_{i+1})}d_{w_{i,2},H_{i+1}}(v).\)

We rescale to obtain \(w_{i+1}:E(H_i)\rightarrow\mathbb{R}_{\ge 0}\) an almost-perfect fractional matching for _H_<sub>_i_+1</sub> as follows:

\(w_{i+1}(e):=\left\{\begin{array}{ c c }
\frac{w_{i,2}(e)}{d_i^*} & \text{if}e\in H_i[I_{t_{i+1}}]\text{is}i\text{-reachable} \\
w_{i,1}(e) & \text{otherwise.}
\end{array}\right.\)

