Thus \(\sum_{j\in\mathcal{J}}m_{s,j}=S_s\) and \(Q_s(j)=\Phi_j(n_s,m_{s,j})\). Let \(\mathcal{G}_\eta\) be the event from Theorem 4.2. On this event, simultaneously for all \(t\ge K\) and all \(j\in\mathcal{J}\),<tbc>

\(|P_t(j)-Q_t(j)|=|V_t(i^\star,j)-V_t^\mu(i^\star,j)|\le\varepsilon_t,\)

<tbc>where<tbc>

\(P_t(j)=V_t(i^\star,j)+logN_{t,j},Q_t(j)=V_t^\mu(i^\star,j)+logN_{t,j},\)

<tbc>and

\(\varepsilon_t:=C_\mu\left(\sqrt{tH_t(\eta)}+H_t(\eta)\right).\)

<tbc>**Lemma E.4** (Challenger-budget uniform lower bound)**.** _Fix_ \(U\Subset(0,1)\) _containing_ \(\beta\)_. There exists a finite constant_ \(C_\mu(U)<\infty\) _such that, on_ \(\mathcal{G}_\eta\)_, for every U-stabilization time t<sub>U</sub> and every_ \(s\ge t_U\),

\(min_{j\in\mathcal{J}}Q_s(j)\ge\Gamma_{n_s,S_s}^\mathrm{disc}(\mu)-C_\mu(U)\left(t_U+G_s^\mathrm{tot}+\varepsilon_s+\mathrm{sup}_{t_U\le u\le s}u|\alpha_u-\beta|+1\right).\) (E.1)

_For the unguarded rule,_ \(G_s^\mathrm{tot}\equiv 0\).

_Proof of Lemma E.4._ Let \(\overline{S_\mu}\) be the uniform cutoff from Lemma E.2 and set

\(\overline{\alpha_U}:=\mathrm{sup}U<1,s_\mathrm{eq}:=\left[\frac{\overline{S_\mu}}{1-\overline{\alpha_U}}\right].\)

If \(u\ge s_\mathrm{eq}\) and \(\alpha_u\in U\), then \(S_u=(1-\alpha_u)u\ge\overline{S_\mu}\), so the continuous equalizer \((\gamma_{n_u,S_u},r_{n_u,S_u})\) exists. If _s\<s_<sub>eq</sub>, only finitely many count configurations are possible; after enlarging \(C_\mu(U)\), the displayed bound is automatic because the factor in parentheses is at least one. We therefore assume \(s\ge s_\bullet:=\mathrm{max}\{t_U,s_\mathrm{eq}\}\). Then the equalizer exists for every \(u\in[s_\bullet,s]\).

Define the fixed-\(\beta\) challenger target<tbc>

\(p_j^\beta:=\frac{w_j^\beta}{1-\beta},j\in\mathcal{J},\)

<tbc>so that \(p_j^\beta>0\) and \(\sum_jp_j^\beta=1\). For \(u\in[s_\bullet,s]\), set<tbc>

\(D_{u,j}:=p_j^\beta S_u-N_{u,j},j\in\mathcal{J}.\)

<tbc>Then \(\sum_jD_{u,j}=0\). Lemma E.2 and the identity \(S_u=(1-\alpha_u)u\) give<tbc>

\(r_{j,n_u,S_u}-p_j^\beta S_u=u\left(w_j^{\alpha_u}-\frac{1-\alpha_u}{1-\beta}w_j^\beta\right)+O_\mu(1).\)

<tbc>The map<tbc>

\(\alpha\mapsto w_j^\alpha-\frac{1-\alpha}{1-\beta}w_j^\beta\)

<tbc>is _C_<sup>1</sup> on _U_ and vanishes at \(\alpha=\beta\). Hence, uniformly over \(u\in[s_\bullet,s]\),

\(|r_{j,n_u,S_u}-p_j^\beta S_u|\le C_\mu(U)(u|\alpha_u-\beta|+1).\) (E.2)

We next show that regular challenger pulls serve an approximately largest deficit. Let \(u+1\le s\) be a non-guard challenger-pull round with \(u\ge s_\bullet\), and let _a=C_<sub>_u_+1</sub>. Put \(M_u:=\mathrm{max}_{j\in\mathcal{J}}D_{u,j}\). We claim that, for constants \(\kappa_\mu(U)\in(0,1]\) and \(A_\mu(U)<\infty\),

\(D_{u,a}\ge\kappa_\mu(U)M_u-A_\mu(U)(\varepsilon_u+u|\alpha_u-\beta|+1).\) (E.3)

Let \(j^+\in\mathrm{argmax}_jD_{u,j}\) and define _e<sub>u,j</sub>_:=_r<sub>j,n<sub>u</sub>,S<sub>u</sub></sub>-N<sub>u,j</sub>_. By (E.2),

\(e_{u,j^+}\ge M_u-C_\mu(U)(u|\alpha_u-\beta|+1).\) (E.4)

If \(M_u\le C_\mu(U)(\varepsilon_u+u|\alpha_u-\beta|+1)\), then (E.3) follows after increasing \(A_\mu(U)\), because the zero-sum property implies \(D_{u,a}\ge-d_KM_u\). Otherwise _e_<sub>_u,j_<sup>+</sup></sub>_\>_0, and the slope lower bound in Lemma E.1 gives<tbc>

\(Q_u(j^+)\le\gamma_{n_u,S_u}-c_\mu(U)M_u+C_\mu(U)(u|\alpha_u-\beta|+1).\)

