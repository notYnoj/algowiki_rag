Summing over \(j\neq i^\star\) gives<tbc>

\(1-\alpha=\sum_{j\neq i^\star} w_j\ge\sum_{j\neq i^\star} G_j(\alpha,m(w)).\)

<tbc>By the defining property of \(\lambda_\alpha\), this implies \(m(w)\le\lambda_\alpha\). Hence

\(max_{w\in\Delta_{1-\alpha}}min_{j\neq i^\star} I_j^\alpha(w_j)=\lambda_\alpha,\)

and therefore \(\lambda_\alpha=T_\alpha^\star(\mu)^{-1}\). If _w_ is any maximizer, then \(m(w)=\lambda_\alpha\), so \(w_j\ge G_j(\alpha,\lambda_\alpha)=w_j^\alpha(\mu)\) for every \(j\neq i^\star\). Because both vectors sum to \(1-\alpha\), equality must hold coordinatewise, proving uniqueness.

For regularity, define<tbc>

\(\Psi_j(\alpha,w,\lambda):=I_j^\alpha(w)-\lambda.\)

<tbc>Since \(\Psi_j\) is _C_<sup>1</sup> and \(\partial_w\Psi_j(\alpha,w,\lambda)=\partial_wI_j^\alpha(w)>0\), the inverse function theorem implies that _G<sub>j</sub>_ is _C_<sup>1</sup> on its domain. Hence _F_ is _C_<sup>1</sup>, with

\(\partial_\lambda F(\alpha,\lambda)=\sum_{j\neq i^\star}\partial_\lambda G_j(\alpha,\lambda)>0.\)

The implicit function theorem applied to \(F(\alpha,\lambda_\alpha)=0\) shows that \(\alpha\mapsto\lambda_\alpha\) is _C_<sup>1</sup> on compact subsets of (0,1). Each coordinate \(\alpha\mapsto w_j^\alpha(\mu)=G_j(\alpha,\lambda_\alpha)\) is therefore _C_<sup>1</sup> as well.

**Lemma C.4** (Lipschitz control of \(T_\alpha^\star(\mu)^{-1}\) on compacts)**.** _Let_ \(U\Subset(0,1)\) _be compact. Then there exists a finite constant_ \(L_\mu(U)\) _such that for all_ \(\alpha,\alpha'\in U\),

\(\left|\frac{1}{T_\alpha^\star(\mu)}-\frac{1}{T_{\alpha^\prime}^\star(\mu)}\right|\le L_\mu(U)|\alpha-\alpha'|.\)

_Proof of Lemma C.4._ By Proposition C.3, the map \(\alpha\mapsto T_\alpha^\star(\mu)^{-1}\) is _C_<sup>1</sup> on an open neighborhood of _U_. Its derivative is continuous and therefore bounded on the compact set _U_. The mean value theorem yields the displayed Lipschitz bound.

## C.3 Discrete rounding and proof of Proposition 4.1

**Lemma C.5** (Integer rounding with a fixed sum)**.** _Let_ \(a_1,\dots,a_{K-1}\ge 1\) _satisfy_ \(\sum_{j=1}^{K-1}a_j=s\in\mathbb{N}\)_. Then there exist integers_ \(m_1,\dots,m_{K-1}\ge 1\) _such that_

\(\sum_{j=1}^{K-1}m_j=s,|m_j-a_j|\le 1\forall j.\)

_Proof of Lemma C.5._ Let \(\widetilde{m}_j:=\lfloor a_j\rfloor\), so \(\widetilde{m}_j\ge 1\) for all _j_, and define \(r:=s-\sum_{j=1}^{K-1}\widetilde{m}_j\). Because \(\sum_ja_j=s\) and each fractional part satisfies \(a_j-\lfloor a_j\rfloor<1\), one has \(r\in\{0,1,\dots,K-2\}\). Add 1 to the _r_ coordinates with largest fractional parts. The resulting integers satisfy the required properties.

_Proof of Proposition 4.1._ Fix \(U\Subset(0,1)\). We show that there exists \(C_\mu(U)<\infty\) such that for every \(n\ge 1\) and \(s\ge K-1\) with<tbc>

\(\alpha:=\frac{n}{n+s}\in U,t:=n+s,\)

<tbc>one has<tbc>

\(\left|\Gamma_{n,s}^\mathrm{disc}(\mu)-\left(\frac{t}{T_\alpha^\star(\mu)}+\mathrm{log}t\right)\right|\le C_\mu(U).\)

<tbc>Let \(m=(m_j)_{j\neq i^\star}\) be any feasible integer allocation and define _w<sub>j</sub>_:=_m<sub>j</sub>/t_. Then \(w\in\Delta_{1-\alpha}\) and<tbc>

\(\Phi_j(n,m_j)=tI_j^\alpha(w_j)+\mathrm{log}t+\mathrm{log}w_j.\)

