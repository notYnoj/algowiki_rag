<tbc>Azuma-Hoeffding Inequality (Lemma 2.6), we have that<tbc>

\(\mathbb{P}(|Y_\chi^f|>f^\mathrm{min}t_i^{0.51})\le 2\mathrm{exp}\left(-\frac{(f^\mathrm{min})^2t_i^{1.02}}{2\sum_{i=1}^\chi(3f^\mathrm{max})^2}\right).\)

<tbc>Then since \(\chi\le 2.1c_2\mathrm{log}^{l_4}(n)t_i^{1-\epsilon_1}p_\mathrm{gr}\le 2.1c_2\mathrm{log}^{l_4}(n)t_i^{1-\epsilon_1}\), and \(\frac{f^\mathrm{max}}{f^\mathrm{min}}\le\mathrm{log}^{500}(n)\) we have that whp<tbc>

\(X^f=\left(\sum_{j\in[\chi]}\mathbb{E}'(X_j^f)\right)\pm f^\mathrm{min}t_i^{0.51}.\)

<tbc>Claim 6.47. _For each_ \(j\in[\chi]\)_, we have that_<tbc>

\(\mathbb{E}(X_j^f)\left(1+\frac{15c_2\mathrm{log}^{4l_3+l_4+6}(n)}{c_1^3t_i^{\epsilon_1}p_\mathrm{gr}^2}\right)\ge\mathbb{E}'(X_j^f)\ge\mathbb{E}(X_j^f)-\frac{6.3f^\mathrm{max}c_2\mathrm{log}^{4l_3+l_4+6}(n)}{0.9c_1^3t_i^{\epsilon_1}p_\mathrm{gr}^2}.\)

<tbc>Proof. Let _E<sub>j</sub>_ be the set of edges that could be chosen for _e<sub>j</sub>_ and let \(E'_j\) be the set f edges that could be chosen for _e<sub>j</sub>_ given the choices for _e_<sub>1</sub>_,...,e_<sub>_j_-1</sub>. First note that<tbc>

\(\mathbb{E}(X_j^f)=\sum_{e\in E_j}\frac{\sum_{e^\prime\in E_{H_{i,1}}(v,S_1,S_2,S_3):e\cap e^\prime\neq\emptyset} f(e')}{|E_j|},\)

<tbc>and that<tbc>

\(\mathbb{E}'(X_j^f)=\sum_{e\in E_j^\prime}\frac{\sum_{e^\prime\in E_{H_{i,1}}(v,S_1,S_2,S_3):e\cap e^\prime\neq\emptyset} f(e')}{|E'_j|}.\)

<tbc>Then \(\mathbb{E}'(X_j^f)\ge\frac{(\sum_{e\in E_j}\sum_{e^\prime\in E_{H_{i,1}}(v,S_1,S_2,S_3):e\cap e^\prime\neq\emptyset} f(e^\prime))-3f^\mathrm{max}\chi}{|E_j|}=\mathbb{E}(X_j^f)-\frac{3f^\mathrm{max}\chi}{|E_j|}\). Now by (G1) and (G2) we have that \(\chi\le 2.1c_2\mathrm{log}^{l_4}(n)t_i^{1-\epsilon_1}p_\mathrm{gr}\) and \(|E_j|\ge\frac{0.9c_1^3t_ip_\mathrm{gr}^3}{\mathrm{log}^{4l_3+6}(n)}\) so that

\(\frac{3f^\mathrm{max}\chi}{|E_j|}\le\frac{6.3f^\mathrm{max}c_2\mathrm{log}^{4l_3+l_4+6}(n)}{0.9c_1^3t_i^{\epsilon_1}p_\mathrm{gr}^2},\)

and the lower bound claim holds.

For the upper bound note that \(\mathbb{E}'(X_j^f)\le\sum_{e\in E_j}\frac{\sum_{e^\prime\in E_{H_{i,1}}(v,S_1,S_2,S_3):e\cap e^\prime\neq\emptyset} f(e^\prime)}{|E'_j|}=\frac{|E_j|}{|E'_j|}\mathbb{E}(X_j^f)\). Now \(|E'_j|\ge|E_j|-3\chi\) and \(|E_j|\gg\chi\). Thus \(\mathbb{E}'(X_j^f)\le\mathbb{E}(X_j^f)(1+\frac{6.1\chi}{|E_j|})\le\mathbb{E}(X_j^f)\left(1+\frac{15c_2\mathrm{log}^{4l_3+l_4+6}(n)}{c_1^3t_i^{\epsilon_1}p_\mathrm{gr}^2}\right)\), as stated. □

From the claim and the preceding statement it follows that<tbc>

\(X^f\ge\mathbb{E}(X^f)-\left(\frac{15c_2^2f^\mathrm{max}\mathrm{log}^{4l_3+2l_4+6}(n)t_i^{1-2\epsilon_1}}{c_1^3p_\mathrm{gr}}+f^\mathrm{min}t_i^{0.51}\right),\)

<tbc>and

\(X^f\le\mathbb{E}(X^f)+\frac{2400c_2c_3^2f^{max}\mathrm{log}^{8l_3+2l_4+12}(n)t_i^{1-2\epsilon_1}p_\mathrm{gr}}{c_1^6}+f^\mathrm{min}t_i^{0.51},\)

