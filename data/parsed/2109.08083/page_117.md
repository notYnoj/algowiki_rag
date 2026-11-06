<tbc>\(f_S^\mathrm{min}:=\mathrm{min}_{v\in V(H_{i.1}[S])}f_S(v)\). Then \(|Y_j^{f,S}-Y_{j-1}^{f,S}|\le|X_j^{f,S}-\mathbb{E}'(X_j^{f,S})|\le 3f_S^\mathrm{max}\), since the edge _e<sub>j</sub>_ chosen for _v<sub>j</sub>_ contains at most 3 vertices in _S_. Thus, by the Azuma-Hoeffding Inequality (Lemma 2.6), we have that<tbc>

\(\mathbb{P}(|Y_\chi^{f,S}|>f_S^\mathrm{min}t_i^{0.51})\le 2\mathrm{exp}\left(-\frac{(f_S^\mathrm{min})^2t_i^{1.02}}{2\sum_{i=1}^\chi(3f_S^\mathrm{max})^2}\right).\)

<tbc>Then since \(\chi\le 2.1c_2\mathrm{log}^{l_4}(n)t_i^{1-\epsilon_1}p_\mathrm{gr}\le 2.1c_2\mathrm{log}^{l_4}(n)t_i^{1-\epsilon_1}\), and \(\frac{f_S^\mathrm{max}}{f_S^\mathrm{min}}\le\mathrm{log}^{500}(n)\) we have that whp<tbc>

\(X^{f,S}=\left(\sum_{j\in[\chi]}\mathbb{E}'(X_j^{f,S})\right)\pm f_S^\mathrm{min}t_i^{0.51}.\)

<tbc>Claim 6.45. _For each_ \(j\in[\chi]\)_, we have that_

\(\mathbb{E}'(X_j^{f,S})\le\mathbb{E}(X_j^{f,S})\left(1+\frac{15c_2\mathrm{log}^{4l_3+l_4+6}(n)}{c_1^3t_i^{\epsilon_1}p_\mathrm{gr}^2}\right),\text{\textit{and}}\)<br>
\(\mathbb{E}'(X_j^{f,S})\ge\mathbb{E}(X_j^{f,S})-\frac{6.3f_S^\mathrm{max}c_2\mathrm{log}^{4l_3+l_4+6}(n)}{0.9c_1^3t_i^{\epsilon_1}p_\mathrm{gr}^2}.\)

Proof. Let _E<sub>j</sub>_ be the set of edges that could be chosen for _e<sub>j</sub>_ and let \(E'_j\) be the set of edges that could be chosen for _e<sub>j</sub>_ given the choices for _e_<sub>1</sub>_,...,e_<sub>_j_-1</sub>. First note that \(\mathbb{E}(X_j^{f,S})=\sum_{e\in E_j}\frac{\sum_{v\in(e\cap S)}f_S(v)}{|E_j|}\) and that \(\mathbb{E}'(X_j^{f,S})=\sum_{e\in E'_j}\frac{\sum_{v\in(e\cap S)}f_S(v)}{|E'_j|}\) . Then \(\mathbb{E}'(X_j^{f,S})\ge\frac{(\sum_{e\in E_j}\sum_{v\in(e\cap S)}f_S(v))-3f_S^\mathrm{max}\chi}{|E_j|}=\mathbb{E}(X_j^{f,S})-\frac{3f_S^\mathrm{max}\chi}{|E_j|}\) . Now by (G1) we have that \(\chi\le 2.1c_2\mathrm{log}^{l_4}(n)t_i^{1-\epsilon_1}p_\mathrm{gr}\) and by (G2) \(|E_j|\ge\frac{0.9c_1^3t_ip_\mathrm{gr}^3}{\mathrm{log}^{4l_3+6}(n)}\) so that

\(\frac{3f_S^\mathrm{max}\chi}{|E_j|}\le\frac{6.3f_S^\mathrm{max}c_2\mathrm{log}^{4l_3+l_4+6}(n)}{0.9c_1^3t_i^{\epsilon_1}p_\mathrm{gr}^2},\)

and the lower bound claim holds.

For the upper bound note that \(\mathbb{E}'(X_j^{f,S})\le\sum_{e\in E_j}\frac{\sum_{v\in(e\cap S)}f_S(v)}{|E'_j|}=\frac{|E_j|}{|E'_j|}\mathbb{E}(X_j^{f,S})\). Now \(|E'_j|\ge|E_j|-3\chi\) and \(|E_j|\gg\chi\). Thus \(\mathbb{E}'(X_j^{f,S})\le\mathbb{E}(X_j^{f,S})(1+\frac{6.1\chi}{|E_j|})\le\mathbb{E}(X_j^{f,S})\left(1+\frac{15c_2\mathrm{log}^{4l_3+l_4+6}(n)}{c_1^3t_i^{\epsilon_1}p_\mathrm{gr}^2}\right)\), as stated. □

By this claim we have that<tbc>

\(X^{f,S}\ge\mathbb{E}(X^{f,S})-\left(\frac{15c_2^2f_S^\mathrm{max}\mathrm{log}^{4l_3+2l_4+6}(n)t_i^{1-2\epsilon_1}}{c_1^3p_\mathrm{gr}}+f_S^\mathrm{min}t_i^{0.51}\right),\)

<tbc>and<tbc>

\(X^{f,S}\le\mathbb{E}(X^{f,S})+\frac{600c_2^2c_3f_S^\mathrm{max}\mathrm{log}^{8l_3+2l_4+12}(n)t_i^{1-2\epsilon_1}}{c_1^6p_\mathrm{gr}}+f_S^\mathrm{min}t_i^{0.51},\)

<tbc>where

\(\mathbb{E}(X^{f,S})=\sum_{v\in V(H_{i.1}[S])}f_S(v)p_v^i\le f_S^\mathrm{max}p_v^i|V(H_{i.1}[S])|\)<br>
\(\le\frac{40f_S^\mathrm{max}c_2c_3\mathrm{log}^{4l_3+l_4+6}(n)t_i^{1-\epsilon_1}p_\mathrm{gr}}{c_1^3}\)

