Because

\(\frac{A}{\sqrt{A(1+logA)}}\rightarrow\infty\text{and}\frac{A}{1+logA}\rightarrow\infty\text{as}A\rightarrow\infty,\)

we can increase _A_<sub>inv</sub> so that the bracket is strictly positive. Thus _F_(0)_\>_0. Since _F_ is nondecreasing, \(F(L)\ge F(0)>0\) for every \(L\ge 0\), which is exactly the desired inequality.

## F.5 Proof of Theorem 5.2

_Proof of Theorem 5.2._ Fix \(\delta\in(0,1/2]\) and \(\eta\in(0,1/4]\). Define

\(\widetilde{H}_t(\eta):=log\frac{K}{\eta}+log(et).\)

Let \(\mathcal{E}_\mathrm{env}(\eta)\) be the event from Proposition 5.1; it has probability at least \(1-2\eta\). Let \(\mathcal{A}_\eta\) be the event from Proposition F.1; it has probability at least \(1-\eta\). We work on

\(\mathcal{E}:=\mathcal{E}_\mathrm{env}(\eta)\cap\mathcal{A}_\eta,\mathbb{P}_\mu(\mathcal{E})\ge 1-3\eta.\)

For all \(t\ge t_U\), entry into the stabilized regime gives _B_<sub>_t_+1</sub>=_i<sup>⋆</sup>_ and \(\alpha_t\in U\). Hence the stopping condition is met at time _t_ as soon as

\(\mathrm{min}_{j\neq i^\star} W_t(i^\star,j)>c(t,\delta).\)

On \(\mathcal{E}_\mathrm{env}(\eta)\), Proposition 5.1 gives, for all \(t\ge t_U\),

\(\mathrm{min}_{j\neq i^\star} W_t(i^\star,j)\ge\frac{t}{T_{\alpha_t}^\star(\mu)}-B_0(U)t_U-B_1(U)\sqrt{t\widetilde{H}_t(\eta)}-B_2(U)\widetilde{H}_t(\eta)-B_3(U)\)

for finite instance-dependent constants \(B_\ell(U)\).

By Lemma C.4, for all \(\alpha\in U\),

\(\frac{1}{T_\alpha^\star(\mu)}\ge\frac{1}{T_\beta^\star(\mu)}-L_\mu(U)|\alpha-\beta|.\)

On \(\mathcal{A}_\eta\), Proposition F.1 with start time _m=t<sub>U</sub>_ implies, uniformly for \(t\ge t_U\),

\(t|\alpha_t-\beta|\le C_\beta t_U+C_\beta\sqrt{t\widetilde{H}_t(\eta)}+G_t^\mathrm{tot}(t_U).\)

For the unguarded rule the last term is zero. With the guard enabled, Lemma E.3 gives \(G_t^\mathrm{tot}(t_U)\le\sqrt{K}t+K\le C_K\sqrt{t\widetilde{H}_t(\eta)}\). Thus

\(\frac{t}{T_{\alpha_t}^\star(\mu)}\ge\frac{t}{T_\beta^\star(\mu)}-A_0(U)t_U-A_1(U)\sqrt{t\widetilde{H}_t(\eta)}.\)

Combining the preceding displays, there are constants \(a_\mu(U),b_\mu(U),d_\mu(U)\) and \(C_{\mu,0}(U)\ge 0\) such that, for all \(t\ge t_U\),

\(\mathrm{min}_{j\neq i^\star} W_t(i^\star,j)\ge\frac{t}{T_\beta^\star(\mu)}-\frac{C_{\mu,0}(U)}{T_\beta^\star(\mu)}t_U-a_\mu(U)\sqrt{t\widetilde{H}_t(\eta)}-b_\mu(U)\widetilde{H}_t(\eta)-d_\mu(U).\) (F.3)

Apply Theorem F.6 with

\(T=T_\beta^\star(\mu),C_0=C_{\mu,0}(U),a=a_\mu(U),b=b_\mu(U),d=d_\mu(U).\)

Let \(s_{\delta,\eta}\) be the resulting quantity and set

\(t^\star:=(1+C_{\mu,0}(U))t_U+s_{\delta,\eta}.\)

Evaluating (F.3) at _t=t<sup>⋆</sup>_ gives

\(\mathrm{min}_{j\neq i^\star} W_{t^\star}(i^\star,j)\ge\frac{t_U+s_{\delta,\eta}}{T_\beta^\star(\mu)}-a_\mu(U)\sqrt{t^\star\widetilde{H}_{t^\star}(\eta)}-b_\mu(U)\widetilde{H}_{t^\star}(\eta)-d_\mu(U).\)

