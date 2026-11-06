pairs **z** with _F<sub>i,a</sub>_(**z**). When \(\mathbf{z}-a\mathbf{e}_i\in\mathcal{S}\), this is precisely the error-space transition in (25); the remaining pairs give

\(M_{i,a}:=\{(F_{i,a}(\mathbf{z}),\mathbf{z}):\mathbf{z}\in\mathcal{S}_{i,a}^c\},\) (32)

\(\mathcal{A}_\mathbf{C}:=\sum_{i,a}\kappa_i(a)\sum_{(\mathbf{y},\mathbf{z})\in M_{i,a}}\overline{\phi_\mathbf{C}(\mathbf{y})}\phi_\mathbf{C}(\mathbf{z}),\) (33)

\(\mathbb{E}[s(\mathbf{X})]=\langle\Gamma_\mathcal{S}|\widetilde{\mathsf{S}}_\mathrm{err}|\Gamma_\mathcal{S}\rangle+\frac{\mathcal{A}_\mathbf{C}}{Z_\mathbf{C}}.\) (34)

The real quantity A**<sub>C</sub>** accounts for interference between distinct error-space transitions with the same syndrome, which we call _aliasing_.

For \(a\neq 0\), the centered Fourier coefficients satisfy

\(\kappa_i(a)=\sqrt{\rho(1-\rho)}\overline{\widetilde{g}_i(a)}.\) (35)

Define the boundary masses

\(\mu_{i,a}:=\sum_{\mathbf{y}\in\mathcal{S}_{i,a}^c}|\phi_\mathbf{C}(\mathbf{y})|^2.\) (36)

Cauchy-Schwarz and the boundary bijection imply

\(|\mathcal{A}_\mathbf{C}|\le\Delta_\mathbf{C}:=\sqrt{\rho(1-\rho)}\sum_{i,a\neq 0}|\widetilde{g}_i(a)|\sqrt{\mu_{i,a}\mu_{i,-a}}.\) (37)

We will use the bounds

\(\sum_{a\neq 0}|\widetilde{g}_i(a)|\le\sqrt{q-1},\sum_{a\neq 0}|\kappa_i(a)|\le\sqrt{(q-1)\rho(1-\rho)}.\) (38)

Let \(\epsilon_k\) be the decoder’s ordinary failure probability under _P<sub>k</sub>_. The hypothesis gives \(\epsilon_k\le\varepsilon\) for \(k\le\ell\). Moreover, every boundary event \(\mathbf{y}\in\mathcal{S}_{i,a}^c\) implies failure of the hypothesis’s one- coordinate recovery condition. For every \(k\le\ell\), the one-coordinate recovery hypothesis implies \(P_k(\mathcal{S}_{i,a}^c)\le\varepsilon\). The prepared error has weight _k_ with probability |_w<sub>k</sub>_|<sup>2</sup> and, conditional on that weight, has distribution _P<sub>k</sub>_. Therefore, for every normalized amplitude vector supported on weights \(0,\dots,\ell\),

\(\mu_{i,a}=\sum_{k=0}^\ell|w_k|^2P_k(\mathcal{S}_{i,a}^c)\le\varepsilon\sum_{k=0}^\ell|w_k|^2=\varepsilon.\) (39)

Substituting this bound into (37) and using (38) gives

\(|\mathcal{A}_\mathbf{C}|\le\varepsilon\sum_{i,a\neq 0}|\kappa_i(a)|\le m\sqrt{(q-1)\rho(1-\rho)}\varepsilon.\) (40)

Let \(T_{\rho,\ell}\) be the principal block of \(T_\rho\) on weights \(0,\dots,\ell\), and let \(\lambda_\ell\) be its largest eigenvalue. Success projection has the diagonal compression

\(Q_\mathcal{S}:=\mathsf{V}^\dagger\Pi_\mathcal{S}\mathsf{V}=\mathrm{diag}(1-\epsilon_0,\dots,1-\epsilon_m).\) (41)

For normalized **w** supported through \(\ell\), decompose

\(\Pi_\mathcal{S}\mathsf{V}\mathbf{w}=\mathsf{V}Q_\mathcal{S}\mathbf{w}+|\eta\rangle,|\eta\rangle\perp\mathrm{ranV},\|\eta\|^2=Z_\mathbf{C}-\|Q_\mathcal{S}\mathbf{w}\|^2.\) (42)

