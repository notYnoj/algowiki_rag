## Appendix A Proof of Lemma 1

**Proof:** When \(\alpha=0\), \(\mathcal{C}_\alpha=\mathcal{T}\) . In such case, \(\sigma(\mathcal{C}_\alpha)=\sigma(\mathcal{T})=\sigma(L)\subset(1,+\infty)\subset\mathbb{C}\backslash(-\infty,0]\). Hence, \(\mathcal{C}_0\in\mathcal{Q}(mn)\).

It remains to focus on the case \(\alpha\in(0,1)\). We recall from (1.7) that<tbc>

\(\sigma(\mathcal{C}_\alpha)=\sigma(\Lambda_{\alpha,1}\otimes L+\Lambda_{\alpha,2}\otimes I_m).\)

<tbc>Hence, for any \(\mu\in\sigma(\mathcal{C}_\alpha)(\alpha\in(0,1))\), there exists \(k\in\{1,2,\dots,n\}\) and \(\lambda\in\sigma(L)\subset(1,+\infty)\) such that

\(\mu=\lambda\lambda_{1,k}^{(\alpha)}+\lambda_{2,k}^{(\alpha)}\)<br>
\(=\lambda-2\alpha^\frac{1}{n}\theta_n^{(k-1)}+\lambda\alpha^\frac{2}{n}\theta_n^{2(k-1)}\)<br>
\(=\lambda-2\alpha^\frac{1}{n}\mathrm{cos}(\omega_k)+\lambda\alpha^\frac{2}{n}\mathrm{cos}(2\omega_k)-2\alpha^\frac{1}{n}\mathbf{i}\mathrm{sin}(\omega_k)+\lambda\alpha^\frac{2}{n}\mathbf{i}\mathrm{sin}(2\omega_k)\)<br>
\(=\lambda-2\alpha^\frac{1}{n}\mathrm{cos}(\omega_k)+\lambda\alpha^\frac{2}{n}(2\mathrm{cos}^2(\omega_k)-1)+\mathbf{i}2\alpha^\frac{1}{n}\mathrm{sin}(\omega_k)[\lambda\alpha^\frac{1}{n}\mathrm{cos}(\omega_k)-1]\)<br>
\(=\lambda(1-\alpha^\frac{2}{n})+2\alpha^\frac{1}{n}\mathrm{cos}(\omega_k)[\lambda\alpha^\frac{1}{n}\mathrm{cos}(\omega_k)-1]+\mathbf{i}2\alpha^\frac{1}{n}\mathrm{sin}(\omega_k)[\lambda\alpha^\frac{1}{n}\mathrm{cos}(\omega_k)-1],\)

where \(\omega_k=\frac{2\pi(k-1)}{n}\) . We now show \(\mu\in\mathbb{C}\backslash(-\infty,0]\) case by case.

If \(\mathrm{cos}(\omega_k)<0\), then

\(\Re(\mu)=\lambda(1-\alpha^\frac{2}{n})+2\alpha^\frac{1}{n}\mathrm{cos}(\omega_k)[\lambda\alpha^\frac{1}{n}\mathrm{cos}(\omega_k)-1]>\lambda(1-\alpha^\frac{2}{n})>0,\)

which implies \(\mu\in\mathbb{C}\backslash(-\infty,0]\).

If \(\mathrm{cos}(\omega_k)=0\), then

\(\Re(\mu)=\lambda(1-\alpha^\frac{2}{n})>0,\)

which implies \(\mu\in\mathbb{C}\backslash(-\infty,0]\).

If \(\frac{1}{\lambda\alpha^\frac{1}{n}}>\mathrm{cos}(\omega_k)>0\) and \(\mathrm{cos}(\omega_k)\neq 1\), then \(\unknown(\mu)\neq 0\). If \(\mathrm{cos}(\omega_k)=1\), then \(\Re(\mu)=\lambda(1-\alpha^\frac{2}{n})+2\alpha^\frac{1}{n}(\lambda\alpha^\frac{1}{n}-1)=(\alpha^\frac{1}{n}-1)^2+(\lambda-1)(\alpha^\frac{2}{n}+1)>0\). That means \(\mu\in\mathbb{C}\backslash(-\infty,0]\) when \(\frac{1}{\lambda\alpha^\frac{1}{n}}>\mathrm{cos}(\omega_k)>0\).

If \(\mathrm{cos}(\omega_k)=\frac{1}{\lambda\alpha^\frac{1}{n}}\), then \(\mu=\lambda(1-\alpha^\frac{2}{n})>0\), which implies \(\mu\in\mathbb{C}\backslash(-\infty,0]\).

