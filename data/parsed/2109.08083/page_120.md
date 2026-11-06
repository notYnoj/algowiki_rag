<tbc>where, letting \(p_*^i:=\mathrm{max}_ep_e^i\),

\(\mathbb{E}(X^f)=\sum_{e\in E_{H_{i.1}}(v,S_1,S_2,S_3)}f(e)p_e^i\)<br>
\(\le f^\mathrm{max}p_*^i|E_{H_i}(v,S_1,S_2,S_3)|\le\frac{160f^\mathrm{max}c_3^2\mathrm{log}^{4l_3+l_4+6}(n)t_i^{1-\epsilon_1}p_\mathrm{gr}^3}{c_1^3}\)

using (P5) and that \(|E_{H_{i.1}}(v,S_1,S_2,S_3)|\le|E_{H_i}(v,S_1,S_2,S_3)|\) with \(|S_1|\le|I_{t_{i+1}}|\) and Corollary 6.43. This gives that

\(X^f=\mathbb{E}(X^f)\pm O\left(f^{max}p_\mathrm{gr}^{-1}\mathrm{log}^{8l_3+2l_4+12}(n)t_i^{1-2\epsilon_1}\right).\)

Furthermore, \(\sum_{e\in E_{H_{i.1}}(v,S_1,S_2,S_3)}f(e)\ge f^\mathrm{min}|E_{H_{i.1}}(v,S_1,S_2,S_3)|\ge\frac{0.9c_1^3f^\mathrm{min}t_ip_\mathrm{gr}^3}{\mathrm{log}^{4l_3+8}(n)}\) by Corollary 6.33. Thus,

\(\sum_{E_{H_{i+1}}(v,S_1,S_2,S_3)}f(e)=\sum_{e\in E_{H_{i.1}}(v,S_1,S_2,S_3)}f(e)-X^f\)<br>
\(=\left(\sum_{e\in E_{H_{i.1}}(v,S_1,S_2,S_3)}f(e)(1-p_e^i)\right)\pm O\left(f^{max}p_\mathrm{gr}^{-1}\mathrm{log}^{8l_3+2l_4+12}(n)t_i^{1-2\epsilon_1}\right)\)<br>
\(=\left(1\pm O\left(\frac{f^\mathrm{max}\mathrm{log}^{12l_3+2l_4+20}(n)t_i^{-2\epsilon_1}}{c_1^3f^\mathrm{min}p_\mathrm{gr}^4}\right)\right)\sum_{e\in E_{H_{i.1}}(v,S_1,S_2,S_3)}f(e)(1-p_e^i).\)

Since \(t_i^{-\epsilon_1/2}p_\mathrm{gr}^{-4}\checkmark 1\) and \(\frac{f^\mathrm{max}}{f^\mathrm{min}}\le\mathrm{log}^{500}(n)\), we have that

\(O\left(\frac{f^\mathrm{max}\mathrm{log}^{12l_3+2l_4+20}(n)t_i^{-2\epsilon_1}}{c_1^3f^\mathrm{min}p_\mathrm{gr}^4}\right)\le t_i^{-1.5\epsilon_1}\)

as required to complete the proof. □

## 6.4.1.4. _Step 4._

We fix \(M_i^c\) such that Lemmas 6.44 and 6.46 both hold for all _i_-reachable _S_ and open and closed _i_-reachable tuples (_v,S_<sub>1</sub>_,S_<sub>2</sub>_,S_<sub>3</sub>). (It is clear this is possible by union bounds.)

Define \(w_{i,2}:E(H_i)\rightarrow\mathbb{R}_{\ge 0}\) such that

\(w_{i,2}(e):=\left\{\begin{array}{ c c }
\frac{w_{i,1}(e)}{1-p_e^i} & \text{if}e\in H_i[I_{t_{i+1}}]\text{is}i\text{-reachable} \\
w_{i,1}(e) & \text{otherwise.}
\end{array}\right..\)

Since (_H<sub>i</sub>,w<sub>i</sub>_) is _i_-permissible, we have from Corollary 6.43 that \(\frac{1}{1-p_e^i}=1-o(1)\), for every \(e\in H_{i.1}[I_{t_{i+1}}]\).

Proposition 6.48. _For every edge_ \(e\in H_i[I_{t_{i+1}}]\) _that is i-reachable, we have that_<tbc>

\(\frac{c_1}{t_ip_\mathrm{gr}^3\mathrm{log}^2(n)}\le w_{i,2}(e)\le\frac{1.2\mathrm{log}^{l_1+4l_3+8}(n)}{c_1^4t_ip_\mathrm{gr}^3}.\)

<tbc>Proof. Since (_H<sub>i</sub>,w<sub>i</sub>_) is _i_-permissible we have by (P3) that

\(\frac{c_1}{t_ip_\mathrm{gr}^3\mathrm{log}^2(n)}\le w_i(e)\le\frac{\mathrm{log}^{l_1}(n)}{t_ip_\mathrm{gr}^3},\)

