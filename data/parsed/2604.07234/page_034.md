<tbc>**Theorem 4.8** (Variational formula for <o>_Z_</o>)**.** _Fix_ \(\alpha\in(0,1)\) _and define_<tbc>

\(\mathsf{R}(\alpha):=sup_{\rho\in(0,1)}\alpha\rho\Phi(\rho).\)

<tbc>_Then we have_

(4.20) \(lim_{M\rightarrow\infty}\frac{1}{N}log\overline{Z}=\mathsf{R}(\alpha).\)

_Proof._ We prove matching lower and upper bounds.

_Lower bound._ Fix \(\rho\in(0,1)\) and \(\eta>0\), and choose \(\nu\) with finite support such that \(\mathbb{E}_\nu[a]=1/(\alpha\rho)\), \(\mathbb{E}_\nu[b]=1/\rho\) and \(H(\nu)+\mathbb{E}_\nu[logw]\ge\Phi(\rho)-\eta\). Let \(D=\mathsf{supp}(\nu)\). For each large _M_, set \(L:=\lfloor\rho M\rfloor\) and choose integers \(n_x\ge 0\) for \(x\in D\) with \(\sum_{x\in D}n_x=L\) and

(4.21) \(|n_x/L-\nu(x)|\le|D|/L.\)

Let \(\mu_M^{(0)}\in\mathcal{M}_L\) be the corresponding empirical measure. Then as \(M\rightarrow\infty\),<tbc>

\(H(\mu_M^{(0)})\rightarrow H(\nu);\mathbb{E}_{\mu_M^{(0)}}[logw]\rightarrow\mathbb{E}_\nu[logw].\)

<tbc>The mean constraints for \(\overline{Z^{\le M}}\) require \(\mathbb{E}_\mu[a]=\frac{N+1}{L}\) and \(\mathbb{E}_\mu[b]=\frac{M+1}{L}\) , whereas \(\mathbb{E}_{\mu_M^{(0)}}[a]=\frac{A_0}{L}\) and \(\mathbb{E}_{\mu_M^{(0)}}[b]=\frac{B_0}{L}\) with

\(A_0=\sum_{x\in D}n_xa(x);B_0=\sum_{x\in D}n_xb(x).\)

Since \(\mu_M^{(0)}\rightarrow\nu\), we have _A_<sub>0</sub>=_N+O_(1) and _B_<sub>0</sub>=_M+O_(1). Here, the _O_(1) terms follow from (4.21).

We now adjust \(\mu_M^{(0)}\) into a new empirical measure \(\mu_M^{(1)}\in\mathcal{M}_L\) satisfying the _exact_ constraints by chang ing only _O_(1) atoms. We reserve a bounded buffer of the three symbols<tbc>

\(x_0:=(1,1),x_1:=(2,1),x_2:=(2,2),\text{for which}logw(x_i)=0.\)

<tbc>More precisely, choose a fixed constant _C_ large enough that \(C>|\Delta a|+|\Delta b|\) for all sufficiently large _M_, where<tbc>

\((\Delta a,\Delta b):=(N+1-A_0,M+1-B_0)\in\mathbb{Z}^2.\)

<tbc>When constructing the counts _n<sub>x</sub>_ above, we instead require \(\sum_{x\in D}n_x=L-3C\), and then adjoin _C_ copies each of _x_<sub>0</sub>_,x_<sub>1</sub>_,x_<sub>2</sub>. This changes only _O_(1) atoms, so still \(\mu_M^{(0)}\rightarrow\nu\), and hence still _A_<sub>0</sub>=_N+O_(1) and _B_<sub>0</sub>=_M+O_(1). Now we can increase (_A_<sub>0</sub>_,B_<sub>0</sub>) by (1,0) (resp. (1,1)) by replacing one copy of _x_<sub>0</sub> by _x_<sub>1</sub> (resp. _x_<sub>2</sub>), and decrease them by reversing these moves; performing _O_(1) such moves yields exact means. Since only _O_(1) atoms are changed and log_w(x<sub>i</sub>_)=0, we still have<tbc>

\(H(\mu_M^{(1)})=H(\mu_M^{(0)})+o(1);\mathbb{E}_{\mu_M^{(1)}}[logw]=\mathbb{E}_{\mu_M^{(0)}}[logw]+o(1).\)

<tbc>Therefore,<tbc>

\(H(\mu_M^{(1)})+\mathbb{E}_{\mu_M^{(1)}}[logw]\ge\Phi(\rho)-\eta+o(1).\)

<tbc>Applying (4.14) to the admissible pair \((L,\mu_M^{(1)})\) gives<tbc>

\(liminf_{M\rightarrow\infty}\frac{1}{N}log\overline{Z^{\le M}}\ge liminf_{M\rightarrow\infty}\frac{L}{N}\big(H(\mu_M^{(1)})+\mathbb{E}_{\mu_M^{(1)}}[logw]\big)\ge\alpha\rho(\Phi(\rho)-\eta).\)

<tbc>Since \(\overline{Z}\ge\overline{Z^{\le M}}\), it follows that

\(liminf_{M\rightarrow\infty}\frac{1}{N}log\overline{Z}\ge\alpha\rho(\Phi(\rho)-\eta).\)

