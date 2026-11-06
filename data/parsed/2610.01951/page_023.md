## E.1 Continuous equalizers and slope bounds

**Lemma E.1** (Uniform slope bounds for \(\Phi_j\))**.** _Fix a compact interval_ \(U\Subset(0,1)\)_. There exist constants_ \(0<c_\mu(U)\le C_\mu(U)<\infty\) _such that, whenever_ \(\alpha=n/(n+S)\in U\), \(1\le m\le S+1\)_, and_ \(j\in\mathcal{J}\),<tbc>

\(c_\mu(U)\le\partial_m\Phi_j(n,m)\le C_\mu(U).\)

<tbc>_Proof of Lemma E.1._ By the envelope theorem,<tbc>

\(\partial_m\Phi_j(n,m)=d(\mu_j,x_j(n,m))+\frac{1}{m},x_j(n,m):=\frac{n\mu_{i^\star}+m\mu_j}{n+m}.\)

<tbc>If _a<sub>U</sub>_:=inf_U_, then for \(1\le m\le S+1\),

\(\frac{n}{n+m}\ge\frac{n}{n+S+1}=\frac{\alpha(n+S)}{n+S+1}\ge\frac{a_U}{2}\)

after enlarging constants for finitely many small values of _n+S_. Hence _x<sub>j</sub>(n,m_) stays uniformly separated from \(\mu_j\). Since \(\mu_{i^\star}>\mu_j\), the term \(d(\mu_j,x_j(n,m))\) has a positive lower bound depending only on \((\mu,U)\). The upper bound follows from \(x_j(n,m)\in[\mu_j,\mu_{i^\star}]\) and \(1/m\le 1\).

**Lemma E.2** (Continuous equalizer and small-budget cutoff)**.** _Fix_ \(U\Subset(0,1)\)_. For each_ \(n\ge 1\)_, define_<tbc>

\(\gamma_{min}(n):=max_{k\in\mathcal{J}}\Phi_k(n,1),S_0(n,\mu):=\sum_{j\in\mathcal{J}}\Phi_j^{-1}(n,\gamma_{min}(n)),\)

<tbc>_where_ \(\Phi_j^{-1}(n,\gamma)\) _is the inverse of_ \(m\mapsto\Phi_j(n,m)\) _on_ \([1,\infty)\)_. There exists_ \(\overline{S_\mu}<\infty\) _such that_ \(S_0(n,\mu)\le\overline{S_\mu}\) _for all_ \(n\ge 1\)_. For every_ \(S\ge S_0(n,\mu)\)_, there is a unique pair_ \((\gamma_{n,S},r_{n,S})\), \(r_{n,S}=(r_{j,n,S})_{j\in\mathcal{J}}\)_, satisfying_<tbc>

\(\sum_{j\in\mathcal{J}}r_{j,n,S}=S,r_{j,n,S}\ge 1,\Phi_j(n,r_{j,n,S})=\gamma_{n,S}\forall j\in\mathcal{J}.\)

<tbc>_Moreover, if t=n+S,_ \(\alpha=n/t\in U\)_, and_ \(S\ge S_0(n,\mu)\)_, then_<tbc>

\(\gamma_{n,S}=\frac{t}{T_\alpha^\star(\mu)}+logt+O_\mu(1),r_{j,n,S}=tw_j^\alpha(\mu)+O_\mu(1),\)

<tbc>_uniformly over_ \(\alpha\in U\)_, S, and_ \(j\in\mathcal{J}\)_. If S is an integer, then_<tbc>

\(|\gamma_{n,S}-\Gamma_{n,S}^\text{disc}(\mu)|\le C_\mu(U).\)

<tbc>_Proof of Lemma E.2._ For fixed _n_, the map \(m\mapsto\Phi_j(n,m)\) is continuous on \((0,\infty)\) and strictly increasing. Indeed,<tbc>

\(\partial_m\Phi_j(n,m)=d(\mu_j,x_j(n,m))+\frac{1}{m}>0,x_j(n,m)=\frac{n\mu_{i^\star}+m\mu_j}{n+m}.\)

<tbc>Moreover \(\Phi_j(n,m)\rightarrow+\infty\) as \(m\rightarrow\infty\) because \(logm\rightarrow+\infty\). Thus the inverse on \([1,\infty)\) is well defined for every \(\gamma\ge\Phi_j(n,1)\).<br>
Let<tbc>

\(D_\mu^{max}:=max_{k\in\mathcal{J}}d(\mu_k,\mu_{i^\star}).\)

<tbc>Evaluating \(\Phi_k(n,1)\) at \(x=\mu_{i^\star}\) gives \(\gamma_{min}(n)\le D_\mu^{max}\). Since \(\Phi_j(n,m)\ge logm\), any \(m\ge exp(D_\mu^{max})\) satisfies \(\Phi_j(n,m)\ge\gamma_{min}(n)\). Hence<tbc>

\(\Phi_j^{-1}(n,\gamma_{min}(n))\le exp(D_\mu^{max}),S_0(n,\mu)\le\overline{S_\mu}:=d_Kexp(D_\mu^{max}).\)

<tbc>For \(S\ge S_0(n,\mu)\), define

\(F_n(\gamma):=\sum_{j\in\mathcal{J}}\Phi_j^{-1}(n,\gamma),\gamma\ge\gamma_{min}(n).\)

Then _F<sub>n</sub>_ is continuous and strictly increasing, \(F_n(\gamma_{min}(n))=S_0(n,\mu)\), and \(F_n(\gamma)\rightarrow\infty\) as \(\gamma\rightarrow\infty\). Therefore \(F_n(\gamma)=S\) has a unique solution \(\gamma_{n,S}\), and the corresponding coordinates<tbc>

