\(r_{j,n,S}:=\Phi_j^{-1}(n,\gamma_{n,S})\) give the equalizer. This equalizer maximizes the real-valued max-min problem: if \(\gamma\) is feasible, then each coordinate must satisfy \(m_j\ge\Phi_j^{-1}(n,\gamma)\), so feasibility requires \(\sum_{j\in\mathcal{J}}\Phi_j^{-1}(n,\gamma)\le S\); the largest such \(\gamma\) is exactly \(\gamma_{n,S}\).

Let \(\lambda_\alpha=T_\alpha^\star(\mu)^{-1}\) and let \(w^\alpha\) be the unique continuous optimizer from Proposition C.3. Writing _q<sub>j</sub>=r<sub>j,n,S</sub>/t_, the equalizer identity gives<tbc>

\(\gamma_{n,S}=tI_j^\alpha(q_j)+\mathrm{log}t+\mathrm{log}q_j\forall j\in\mathcal{J}.\)

<tbc>For the upper bound, choose _j_ minimizing \(I_j^\alpha(q_j)\). Since \(\sum_jq_j=1-\alpha\), Proposition C.3 gives \(\mathrm{min}_jI_j^\alpha(q_j)\le\lambda_\alpha\), and \(\mathrm{log}q_j\le 0\). Hence \(\gamma_{n,S}\le t\lambda_\alpha+\mathrm{log}t\). For the lower bound, use the real feasible allocation \(m_j=tw_j^\alpha\). Because \(\mathrm{inf}_{\alpha\in U,j}w_j^\alpha>0\), all these coordinates are at least one for all large _t_, and the finitely many remaining cases are absorbed into the constant. Thus

\(\gamma_{n,S}\ge\mathrm{min}_j\left\{tI_j^\alpha(w_j^\alpha)+\mathrm{log}t+\mathrm{log}w_j^\alpha\right\}\ge t\lambda_\alpha+\mathrm{log}t-C_\mu(U).\)

This proves the estimate for \(\gamma_{n,S}\).

We next control _r<sub>j,n,S</sub>_. Let \(c_U:=\mathrm{inf}_{\alpha\in U,j}w_j^\alpha>0\). If _q<sub>j</sub>\<c<sub>U</sub>/_2, then uniformly in \(\alpha\in U\) the strict monotonicity of \(I_j^\alpha\) gives \(I_j^\alpha(q_j)\le\lambda_\alpha-\rho_U\) for some \(\rho_U>0\). For large _t_, this contradicts the lower bound on \(\gamma_{n,S}\); the finitely many small values of _t_ are absorbed into constants. Hence \(q_j\ge c_U/2\). Since log_q<sub>j</sub>=O<sub>U</sub>_(1), the equalizer identity and the estimate for \(\gamma_{n,S}\) imply

\(I_j^\alpha(q_j)=\lambda_\alpha+O_\mu(1/t).\)

On \[_c<sub>U</sub>/_2,1\], the derivative \(\partial_wI_j^\alpha(w)\) is uniformly bounded away from zero. The mean value theorem yields \(|q_j-w_j^\alpha|\le C_\mu(U)/t\), which is the asserted estimate for _r<sub>j,n,S</sub>_.

Finally assume _S_ is an integer. The continuous equalizer maximizes the real-valued max-min problem, so \(\Gamma_{n,S}^\mathrm{disc}(\mu)\le\gamma_{n,S}\). Conversely, Lemma C.5 rounds _r<sub>n,S</sub>_ to integers \(\overline{r_j}\ge 1\) with \(\sum_j\overline{r_j}=S\) and \(|\overline{r_j}-r_{j,n,S}|\le 1\). Lemma E.1 gives \(\Phi_j(n,\overline{r_j})\ge\gamma_{n,S}-C_\mu(U)\), and hence \(\Gamma_{n,S}^\mathrm{disc}(\mu)\ge\gamma_{n,S}-C_\mu(U)\).

## E.2 Guard-count control

**Lemma E.3** (Deterministic bound on the number of guard activations)**.** _Assume the guard rule is the following: at time t_+1_, if_ \(\mathrm{min}_iN_{t,i}<\sqrt{t/K}\)_, then the algorithm sets G_<sub>_t_+1</sub>=1 _and pulls a least-sampled arm. Then for all_ \(t\ge K\),<tbc>

\(G_t^\mathrm{tot}:=\sum_{u=K}^{t-1}G_{u+1}\le K\left(1+\left\lfloor\sqrt{t/K}\right\rfloor\right)\le\sqrt{K}t+K.\)

<tbc>_Proof of Lemma E.3._ For \(r\in\mathbb{N}\), define

\(\mathcal{I}_r:=\left\{u\ge K:r\le\sqrt{u/K}<r+1\right\}.\)

Fix _r_. If _G_<sub>_u_+1</sub>=1 for some \(u\in\mathcal{I}_r\), then a least-sampled arm has count at most _r_. After at most _K_ guard pulls inside I_<sub>r</sub>_, every arm has count at least _r_+1, and then the guard condition cannot hold again within the same epoch. There are at most \(1+\left\lfloor\sqrt{t/K}\right\rfloor\) epochs up to time _t_, which proves the claim.

## E.3 The uniform challenger-index lower bound

Let \(U\in(0,1)\) contain \(\beta\), and let _t<sub>U</sub>_ be a _U_-stabilization time:<tbc>

\(B_{t+1}=i^\star,\alpha_t:=\frac{N_{t,i^\star}}{t}\in U,\forall t\ge t_U.\)

<tbc>For \(s\ge t_U\), define<tbc>

\(n_s:=N_{s,i^\star},S_s:=s-n_s,m_{s,j}:=N_{s,j},j\in\mathcal{J}.\)

