### The instance _f_=1-_x_<sub>1</sub>, _n_=2.

With the minimizers ordered first, \(\mathcal{X}_\star=\{\mathrm{diag}(\alpha,4-\alpha,0,0):0\le\alpha\le 4\}\), \(\mathcal{S}_\star=\{\mathrm{diag}(0,0,\frac{1}{2},\frac{1}{2})+s(e_3e_4^\top+e_4e_3^\top):|s|\le\frac{1}{2}\}\) (the only elements of R supported on _V_ are the off-diagonal _VV_ matrices), M=span{diag(1,-1,0,0)}, \(\mathcal{L}=\mathrm{span}\{e_3e_4^\top+e_4e_3^\top\}\).

### The endpoint and the direction.

Take the primal optimum \(\bar{X}:=Ne_ae_a^\top\) (the moment matrix of the point mass at _a_), the slack \(\bar{S}\) above, the endpoint \(\bar{Z}:=\bar{X}-\sigma\bar{S}\), and the direction \(H:=e_be_c^\top+e_ce_b^\top\). Then \(H\in\mathcal{R}\), and \(H\perp\mathcal{D}\) because _H_ is a cross term between \(U\unknown e_b\) and \(V\unknown e_c\) while \(\mathcal{M}\subseteq\mathbb{S}(U)\) and \(\mathcal{L}\subseteq\mathbb{S}(V)\). Hence the nearest point of aff Z_<sub>⋆</sub>_ to \(\bar{Z}+tH\) is \(\bar{Z}\), and \(\mathrm{dist}_F(\bar{Z}+tH,\mathcal{Z}_\star)=\|tH\|_F=\sqrt{2}t\). The only spectral block of \(\bar{Z}\) changed by _tH_ is the {_b,c_} block \(\genfrac(){pt}{2}{0}{t-\sigma\gamma}\), \(\gamma:=(f(c)-f_\star)/N>0\), whose single positive eigenvalue is

\(\lambda_+(t)=\frac{\sqrt{\sigma^2\gamma^2+4t^2}-\sigma\gamma}{2}=\frac{t^2}{\sigma\gamma}+O(t^4),\) (E.4)

so \(B(t):=\Pi_+(\bar{Z}+tH)-\bar{X}\) is rank one with \(\|B(t)\|_F=\lambda_+(t)\).

### The residual.

Since \(\mathsf{P}\bar{X}=(\mathrm{tr}\bar{X}/N)I_N=I_N=X_b\), \(\mathsf{P}^\perp(\sigma\widehat{C}-\sigma\bar{S})=\mathsf{P}^\perp(\sigma f_\star I_N/N)=0\), and \(\mathsf{P}^\perp H=0\),<tbc>

\(\delta_\sigma(\bar{Z}+tH)=-\mathsf{P}B(t)-\mathsf{P}^\perp\big(tH-B(t)\big)=(\mathrm{Id}-2\mathsf{P})B(t),\)

<tbc>and Id-2P is an orthogonal reflection, so \(\|\delta_\sigma(\bar{Z}+tH)\|_F=\lambda_+(t)\) exactly. Therefore

\(\frac{\|\delta_\sigma(\bar{Z}+tH)\|_F}{\mathrm{dist}_F(\bar{Z}+tH,\mathcal{Z}_\star)}=\frac{\lambda_+(t)}{\sqrt{2}t}\longrightarrow 0,\) (E.5)

and no local error bound (3.9) holds at \(\bar{Z}\). For _f_=1-_x_<sub>1</sub> one has \(\gamma=\frac{1}{2}\), which is the instance quoted in Theorem 4.4.

### Which condition fails.

The direction _H_ lies in R, has _H<sub>UU</sub>_=0, and satisfies \(\bar{X}H=0\) (its rows avoid _a_), but \(H\notin\mathcal{L}\). So the dual identity (the second identity in (3.8), which tests dual directions at a primal boundary point) fails at \(\bar{X}\), which is a relative-boundary point of X_<sub>⋆</sub>_. Consistently, let \(X_\varepsilon\in\mathrm{ri}\mathcal{X}_\star\) be the diagonal optimum with entry \(\varepsilon\) at every minimizer other than _a_ (for _f_=1-_x_<sub>1</sub>, \(X_\varepsilon=\mathrm{diag}(N-\varepsilon,\varepsilon,0,0))\). Along the interior endpoints \(X_\varepsilon-\sigma\bar{S}\), the unit direction \(H/\sqrt{2}\in\mathcal{D}^\perp\) has \(\|\delta'_\sigma(X_\varepsilon-\sigma\bar{S};H/\sqrt{2})\|_F=\varepsilon/(\varepsilon+\sigma\gamma)\rightarrow 0\). Hence \(\mu_\mathrm{ri}=0\), although each interior derivative has kernel exactly D. Moreover \(\Pi'_+(\bar{Z};H)=0\), so \(\delta'_\sigma(\bar{Z};H)=-\mathsf{P}^\perp H=0\) and \(H\in\mathcal{C}(\bar{Z})\backslash T_{\mathcal{Z}_\star}(\bar{Z})\). This is a second-order-dominant direction in the sense of \[KY26b\]: along it the residual is quadratic in the distance to the optimal set.

## F Algorithmic Transfer

### F.1 Error bound plus averagedness: the rate lemma

**Lemma F.1** (Setwise error bound plus averagedness)**.** _Let T be_ \(\alpha\)_-averaged,_ \(0<\alpha<1\)_, in a norm_ \(\|\cdot\|_G\) _with_ \(g_\mathrm{min}\|\cdot\|^2\le\|\cdot\|_G^2\le g_\mathrm{max}\|\cdot\|^2\), \(0<g_\mathrm{min}\le g_\mathrm{max}\)_, on a finite-dimensional space, suppose_ \(\mathrm{Fix}T\neq\emptyset\)_, and suppose_ \(\|Tz-z\|\ge c\mathrm{dist}(z,\mathrm{Fix}T)\) _whenever_ \(\mathrm{dist}(z,\mathrm{Fix}T)\le t_0\)_. Then every orbit converges to a point of_ Fix_T; it eventually enters the error-bound neighborhood, after which_ dist_<sub>G</sub>(z<sup>k</sup>,_Fix_T_) _contracts Q-linearly and the iterates converge R-linearly._

