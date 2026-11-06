_Proof._ For fixed _j_, let \(y_k=\frac{\varepsilon_k}{\varepsilon_k-\varepsilon_j}\). If \(\widehat{y}_k\) is the value of this quantity in floating-point arithmetic, then<tbc>

\(\hat{y}_k=\frac{\varepsilon_k(1+\delta')}{(\varepsilon_k-\varepsilon_j)(1+\delta)}\text{for some}|\delta|,|\delta'|\le\mathbf{u}.\) (A.3)

<tbc>Equivalently, \(\widehat{y}_k=y_k\left(1+\mu_k\right)\) where \(|\mu_k|=\left|\frac{\delta'-\delta}{1+\delta}\right|\le\frac{2\mathbf{u}}{1-\mathbf{u}}\). Now \(\widehat{\alpha}_j\) is just a floating-point product of the \(\widehat{y}_k\). Assuming without loss of generality that this product can be computed from left to right without encountering over/underflow (the argument is the same for any ordering), the corresponding floating-point partial products \(\widehat{\Pi}_i\) satisfy

\(\widehat{\Pi}_1=\widehat{y}_1=y_1(1+\mu_1)\widehat{\Pi}_2=\widehat{y}_1\widehat{y}_2(1+\delta_1)=y_1y_2(1+\mu_1)(1+\mu_2)(1+\delta_1)\widehat{\Pi}_3=\widehat{\Pi}_2\widehat{y}_3(1+\delta_2)=y_1y_2y_3(1+\mu_1)(1+\mu_2)(1+\mu_3)(1+\delta_1)(1+\delta_2)\text{(A.4)}\)

\(\vdots\)

and therefore<tbc>

\(\widehat{\alpha}_j=\widehat{\Pi}_{p-1}=\alpha_j\cdot\prod_{k\neq j}(1+\mu_k)\cdot\prod_{k=1}^{p-2}(1+\delta_k),\) (A.5)

<tbc>where each \(\delta_k\) satisfies \(|\delta_k|\le\mathbf{u}\). Since \(\frac{2(p-1)\mathbf{u}}{1-\mathbf{u}}<1\), standard bounds - e.g., \[31, Lemma 3.1\] - imply \(\prod_{k\neq j}(1+\mu_k)=1+\theta_1\) and \(\prod_{k=1}^{p-2}(1+\delta_i)=1+\theta_2\) for

\(|\theta_1|\le 2p\mathbf{u}+O(\mathbf{u}^2)\text{and}|\theta_2|\le p\mathbf{u}+O(\mathbf{u}^2).\) (A.6)

Hence,

\(\frac{|\widehat{\alpha}_j-\alpha_j|}{|\alpha_j|}=|\theta_1+\theta_2+\theta_1\theta_2|\le|\theta_1|+|\theta_2|+|\theta_1||\theta_2|.\) (A.7)

The result now follows by applying (A.6).

We next prove a perturbation bound for (A.1).

**Proposition A.2.** _Let_ \(\varepsilon_1,\dots,\varepsilon_p\in\mathbb{C}\) _be distinct and nonzero and define_<tbc>

\(gap_\varepsilon=min_{i\neq j}|\varepsilon_i-\varepsilon_j|\text{\textit{and}}M_\varepsilon=max_j|\varepsilon_j|.\)

<tbc>_Suppose that_ \(\tilde{\varepsilon}_1,\dots\) , \(\tilde{\varepsilon}_p\) _satisfy_<tbc>

\(\tilde{\varepsilon}_j=\varepsilon_j(1+\delta_j)\text{\textit{for}}|\delta_j|\le\delta,\)

<tbc>_where_ \(\delta>0\) _is the "size" of the relative perturbation. Let_ \((\alpha_1,\dots,\alpha_p)\) _and_ \((\tilde{\alpha}_1,\dots,\tilde{\alpha}_p)\) _be the exact- arithmetic solutions to the Vandermonde system_ (A.1) _at the points_ \(\varepsilon_1,\dots,\varepsilon_p\) _and_ \(\tilde{\varepsilon}_1,\dots,\tilde{\varepsilon}_p\)_, respectively. If_ \(2(p-1)M_\varepsilon\delta<gap_\varepsilon-2M_\varepsilon\delta\)_, then_<tbc>

\(\frac{|\tilde{\alpha}_j-\alpha_j|}{|\alpha_j|}\le\frac{2(p-1)M_\varepsilon\delta}{gap_\varepsilon-2pM_\varepsilon\delta}.\)

<tbc>_Proof._ Let \(y_k=\frac{\varepsilon_k}{\varepsilon_k-\varepsilon_j}\) and \(\tilde{y}_k=\frac{\tilde{\varepsilon}_k}{\tilde{\varepsilon}_k-\tilde{\varepsilon}_j}\). We have

\(\tilde{y}_k=\frac{\varepsilon_k(1+\delta_k)}{\varepsilon_k(1+\delta_k)-\varepsilon_j(1+\delta_j)}=\frac{\varepsilon_k}{\varepsilon_k-\varepsilon_j}\cdot\frac{1+\delta_k}{1+\frac{\varepsilon_k\delta_k-\varepsilon_j\delta_j}{\varepsilon_k-\varepsilon_j}}=y_k\left(1+\frac{\varepsilon_j(\delta_j-\delta_k)}{\varepsilon_k-\varepsilon_j+\varepsilon_k\delta_k-\varepsilon_j\delta_j}\right),\) (A.8)

where \(\mu_k=\frac{\varepsilon_j(\delta_j-\delta_k)}{\varepsilon_k-\varepsilon_j+\varepsilon_k\delta_k-\varepsilon_j\delta_j}\) satisfies \(|\mu_k|\le\frac{2M_\varepsilon\delta}{gap_\varepsilon-2M_\varepsilon\delta}\). Hence,

\(\tilde{\alpha}_j=\prod_{k\neq j}\tilde{y}_k=\prod_{k\neq j}y_k(1+\mu_k)=\alpha_j\prod_{k\neq j}(1+\mu_k).\) (A.9)

