<tbc>Let \(\eta\downarrow 0\) and take the supremum over \(\rho\in(0,1)\) to obtain

(4.22) \(\mathrm{liminf}_{M\rightarrow\infty}\frac{1}{N}\mathrm{log}\overline{Z}\ge\mathsf{R}(\alpha).\)

_Upper bound._ Write<tbc>

\(\overline{Z}=\overline{Z^{\le M}}+\overline{Z^{(M+1)}},\)

<tbc>where<tbc>

\(\overline{Z^{(M+1)}}:=\sum_{(X_1,\dots,X_{M+1})\in\mathcal{S}_M(N,M)}\prod_{k=1}^{M+1}w(X_k).\)

<tbc>By (4.14), there exists \((L,\mu)\in\mathcal{I}_M\) such that<tbc>

\(\frac{1}{N}\mathrm{log}\overline{Z^{\le M}}\le\frac{L}{N}\big(H(\mu)+\mathbb{E}_\mu[\mathrm{log}w]\big)+o(1).\)

<tbc>Set \(\rho:=L/M\in(0,1]\). Since \(L\le M\) and \(\sum_{k=1}^Lb_k=M+1\), there exists an atom with \(b\ge 2\), so Lemma 4.7 applies. Thus there is \(\widehat{\mu}\in\mathcal{M}_L\) with<tbc>

\(\mathbb{E}_\widehat{\mu}[a]=\frac{N}{L}=\frac{1}{\alpha\rho},\mathbb{E}_\widehat{\mu}[b]=\frac{M}{L}=\frac{1}{\rho},\)

<tbc>and, by (4.19),<tbc>

\(\frac{L}{N}\big(H(\widehat{\mu})+\mathbb{E}_\widehat{\mu}[\mathrm{log}w]\big)=\frac{L}{N}\big(H(\mu)+\mathbb{E}_\mu[\mathrm{log}w]\big)+o(1).\)

<tbc>Since \(\widehat{\mu}\) is finitely supported, it is admissible in the definition of \(\Phi(\rho)\), hence<tbc>

\(\frac{L}{N}\big(H(\mu)+\mathbb{E}_\mu[\mathrm{log}w]\big)\le\alpha\rho\Phi(\rho)+o(1)\le\mathsf{R}(\alpha)+o(1).\)

<tbc>Therefore

(4.23) \(\mathrm{limsup}_{M\rightarrow\infty}\frac{1}{N}\mathrm{log}\overline{Z^{\le M}}\le\mathsf{R}(\alpha).\)

It remains to control <o>_Z_</o><sup>(_M_+1)</sup>. If \((X_1,\dots,X_{M+1})\in\mathcal{S}_M(N,M)\), then necessarily _b<sub>k</sub>_=1 for every _k_, since each \(b_k\ge 1\) and \(\sum_{k=1}^{M+1}b_k=M+1\). Hence _w(X<sub>k</sub>_)=_w(a<sub>k</sub>,_1)=1 for all _k_, and<tbc>

\(\overline{Z^{(M+1)}}=\big|\{(a_1,\dots,a_{M+1})\in\mathbb{N}_{>0}^{M+1}:a_1+\cdots+a_{M+1}=N+1\}\big|=\genfrac(){pt}{2}{N}{M}.\)

<tbc>Therefore

(4.24) \(\mathrm{lim}_{M\rightarrow\infty}\frac{1}{N}\mathrm{log}\overline{Z^{(M+1)}}=h(\alpha).\)

To compare this with \(\mathsf{R}(\alpha)\), fix \(\rho\in(1/2,1)\) and set \(\delta_\rho:=\rho^{-1}-1\). Let \(B_\rho\in\{1,2\}\) satisfy

\(\mathbb{P}(B_\rho=2)=\delta_\rho;\)<br>
\(\mathbb{P}(B_\rho=1)=1-\delta_\rho,\)

so that \(\mathbb{E}[B_\rho]=1/\rho\). Let \(C_\rho\) be a geometric random variable on {0,1,2_,..._} with mean<tbc>

\(m_\rho:=\frac{1-\alpha}{\alpha\rho},\)

<tbc>and independent of \(B_\rho\), and define \(A_\rho:=B_\rho+C_\rho\). Then \(A_\rho\ge B_\rho\) almost surely and

\(\mathbb{E}[A_\rho]=\mathbb{E}[B_\rho]+\mathbb{E}[C_\rho]=\frac{1}{\rho}+\frac{1-\alpha}{\alpha\rho}=\frac{1}{\alpha\rho};\)

