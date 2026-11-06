\(\mathbb{E}[B_\rho]=\frac{1}{\rho}.\)

<tbc>By truncating \(C_\rho\) and adjusting the top atom, we may approximate the law of \((A_\rho,B_\rho)\) by finitely supported admissible laws with the same moments and entropy arbitrarily close to \(H(A_\rho,B_\rho)\). Since \(w(a,b)\ge 1\), it follows that<tbc>

\(\Phi(\rho)\ge H(A_\rho,B_\rho)=H(B_\rho)+H(C_\rho).\)

<tbc>Now \(H(B_\rho)\rightarrow 0\) as \(\rho\uparrow 1\), while<tbc>

\(H(C_\rho)=\big(m_\rho+1\big)h\big(\frac{1}{m_\rho+1}\big)\longrightarrow\frac{1}{\alpha}h(\alpha)\)

<tbc>as \(\rho\uparrow 1\). Therefore<tbc>

\(\mathsf{R}(\alpha)=sup_{\rho\in(0,1)}\alpha\rho\Phi(\rho)\ge limsup_{\rho\uparrow 1}\alpha\rho\big(H(B_\rho)+H(C_\rho)\big)=h(\alpha).\)

<tbc>Together with (4.24), this yields

(4.25) \(limsup_{M\rightarrow\infty}\frac{1}{N}log\overline{Z^{(M+1)}}\le\mathsf{R}(\alpha).\)

Finally, using \(\overline{Z}=\overline{Z^{\le M}}+\overline{Z^{(M+1)}}\) and combining (4.22), (4.23), and (4.25), we conclude that

\(lim_{M\rightarrow\infty}\frac{1}{N}log\overline{Z}=\mathsf{R}(\alpha),\)

which is (4.20). □

## 4.6. Solving the variational problem.

By Theorem 4.8, it remains to evaluate the supremum

\(\mathsf{R}(\alpha)=sup_{\rho\in(0,1)}\alpha\rho\Phi(\rho),\)

where \(\Phi(\rho)\) was defined in (4.15). We solve this double optimisation (over \(\nu\) and over \(\rho\)) via Lagrange multipliers in four steps: first the inner problem for fixed \(\rho\), then a closed-form evaluation of the partition function, then the outer problem in \(\rho\), and finally the resulting algebraic system.

**Lemma 4.9** (Exponential family optimizer)**.** _Fix_ \(\rho\in(0,1)\)_. The supremum defining_ \(\Phi(\rho)\) _is attained by a unique probability measure_ \(\nu^*\) _of the form_

(4.26) \(\nu^*(a,b)=\frac{w(a,b)x^ay^b}{Z(x,y)},a\ge 1,1\le b\le a,\)

_where x,y\>_0 _are the unique positive solutions of the moment equations_ \(\mathbb{E}_{\nu^*}[a]=1/(\alpha\rho)\) _and_ \(\mathbb{E}_{\nu^*}[b]=1/\rho\)_, and_<tbc>

\(Z(x,y):=\sum_{a\ge 1}\sum_{b=1}^a\genfrac(){pt}{2}{a-1}{b-1}^2x^ay^b\)

<tbc>_is the partition function. The optimal value is_

(4.27) \(\Phi(\rho)=logZ(x,y)-\frac{1}{\alpha\rho}logx-\frac{1}{\rho}logy.\)

_Proof._ We first solve the inner variational problem for fixed \(\rho\) by Lagrange multipliers over the space of probability measures satisfying the moment constraints, which identifies the optimizer \(\nu^*\) and shows that it has the exponential family form (4.26). The functional

\(\nu\mapsto H(\nu)+\mathbb{E}_\nu[logw]\)

