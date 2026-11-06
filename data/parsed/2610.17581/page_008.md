_p_3OPT/5 implies \(g(\mathcal{S})-pf(\mathcal{S})\ge 2p\mathrm{OPT}/5\). We finish the proof with an application of the Chernoff bound eq. (1b), as well as taking \((1+\varepsilon^2)/2\le 1\) for the second inequality.

\(\mathrm{Pr}\left[g(\mathcal{S})\ge\frac{3p\mathrm{OPT}}{5}\right]\le\mathrm{Pr}\left[g(\mathcal{S})-pf(\mathcal{S})\ge\frac{2p\mathrm{OPT}}{5}\right]\le\mathrm{Pr}\left[\hat{w}(\mathcal{S})-pw(\mathcal{S})\ge\frac{1+\varepsilon^2}{2}\frac{2p\mathrm{OPT}}{5f_k}\right]\)<br>
\(\le\mathrm{exp}\left(-\frac{(1+\varepsilon^2)p\mathrm{OPT}}{5f_k\mathbb{E}[\hat{w}(\mathcal{S})]}\frac{\mathbb{E}[\hat{w}(\mathcal{S})]}{3}\right)\le\mathrm{exp}\left(-\frac{p\varepsilon^2\mathrm{OPT}}{15f_k}\right)\le\epsilon_k.\)

Defining _X_<sub>S</sub> to be the event that the applicable line of Lemma 3.2 is ‘violated’ for some solution S, we can take a union bound over all \(\mathcal{S}\in\mathbb{S}_k\) to bound the probability of \(\bigcup_{\mathcal{S}\in\mathbb{S}_k}X_\mathcal{S}\). We can then perform a similar union bound over all solution sets \(k\in[\ell]\); letting _k_ denote the set achieving the worst bound, we bound the probability of \(\bigcup_{\mathcal{S}\in\mathbb{S}}X_\mathcal{S}\) by

\(\ell\cdot|\mathbb{S}_k|\cdot\epsilon_k=2\ell|\mathbb{S}_k|\mathrm{exp}\left(-\frac{C}{m}\frac{\varepsilon^2\mathrm{OPT}}{240f_k}\right)\)<br>
\(\le 2\ell|\mathbb{S}_k|\mathrm{exp}\left(-\frac{240n(1+\delta+\mathrm{log}\ell+\gamma^{-1})}{\varepsilon^2m}\frac{\varepsilon^2f_k\frac{m}{n}\mathrm{max}\{\gamma\mathrm{log}|\mathbb{S}_k|,1\}}{240f_k}\right)\)<br>
\(=2\ell|\mathbb{S}_k|\mathrm{exp}\left(-(1+\delta+\mathrm{log}\ell+\gamma^{-1})\mathrm{max}\{\gamma\mathrm{log}|\mathbb{S}_k|,1\}\right)\) (3)

\(\le\mathrm{exp}\left(1+\mathrm{log}\ell+\mathrm{log}|\mathbb{S}_k|-(1+\delta+\mathrm{log}\ell+\gamma^{-1})\gamma\mathrm{log}|\mathbb{S}_k|\right)\le\mathrm{exp}\left(-\delta\right).\)

The first inequality uses the \(\gamma\) bound, and the second inequality makes the assumption that \(\gamma\mathrm{log}|\mathbb{S}_k|\ge 1\). We now finish the argument in the case that \(\gamma\mathrm{log}|\mathbb{S}_k|<1\), upper bounding eq. (3) by<tbc>

\(\mathrm{exp}\left(1+\mathrm{log}\ell+\mathrm{log}|\mathbb{S}_k|-(1+\delta+\mathrm{log}\ell+\gamma^{-1})\right)\le\mathrm{exp}\left(-\delta\right),\)

<tbc>using \(\gamma^{-1}>\mathrm{log}|\mathbb{S}_k|\). Thus, with probability \(1-e^{-\delta}\), we have \(\overline{\bigcup_{\mathcal{S}\in\mathbb{S}}X_\mathcal{S}}\), meaning that for every S,

\(f(\mathcal{S})>\mathrm{OPT}/5\Longrightarrow\left|g(\mathcal{S})-pf(\mathcal{S})\right|\le\varepsilon pf(\mathcal{S})/4,\text{and}\) (4a)

\(f(\mathcal{S})\le\mathrm{OPT}/5\Longrightarrow g(\mathcal{S})\le 3p\mathrm{OPT}/5.\) (4b)

Recalling that \(\mathcal{S}^*=\mathrm{argmax}_{\mathcal{S}\in\mathbb{S}}f(\mathcal{S})\) and \(\hat{\mathcal{S}}^*=\mathrm{argmax}_{\mathcal{S}\in\mathbb{S}}g(\mathcal{S})\), eq. (4a) along with \(\varepsilon\le 1\) gives \(g(\mathcal{S}^*)\ge(1-\varepsilon/4)p\mathrm{OPT}>3p\mathrm{OPT}/5\). By definition, \(\hat{\mathcal{S}}^*\) satisfies \(g(\hat{\mathcal{S}}^*)>g(\mathcal{S}^*)\), and so we have \(f(\hat{\mathcal{S}}^*)>\mathrm{OPT}/5\) by the contrapositive of eq. (4b). Finally, we use eq. (4a) again to get \(g(\hat{\mathcal{S}}^*)-pf(\hat{\mathcal{S}}^*)\le\varepsilon pf(\hat{\mathcal{S}}^*)/4\le\varepsilon p\mathrm{OPT}/4\), yielding

\(f(\hat{\mathcal{S}}^*)\ge p^{-1}g(\hat{\mathcal{S}}^*)-\varepsilon\mathrm{OPT}/4\ge(1-\varepsilon/2)\mathrm{OPT}\ge\mathrm{OPT}/(1+\varepsilon),\)

where the last inequality follows by \(\varepsilon\in(0,1)\). This completes the proof.

## 3.1 \((1+\varepsilon)\)-Approximations for Heavy Subgraph Problems in Weighted Graphs

In weighted graphs, a cut meta-algorithm for heavy subgraph problems follows immediately from Theorem 3.1, as the primitive Rand_<sub>G</sub>_ satisfies Pr\[Rand_<sub>G</sub>=e_\]=_w(e)/w(G_).

**Theorem 3.3.** Let _G_=(_V,E_) be a weighted graph, and let P be a \((\gamma,\ell)\)-heavy subgraph problem. With probability \(1-e^{-\delta}\), Algorithm 1 makes \(O(n\mathrm{log}n(1+\delta+\mathrm{log}\ell+\gamma^{-1})/\varepsilon^2)\) cut queries and returns a \((1+\varepsilon)\)-approximation for P.

Since DSG is a \((\frac{1}{\mathrm{log}n},n)\)-heavy subgraph problem, Theorem 3.3 yields our main result for Densest Subgraph on weighted graphs in the cut query model.

**Theorem 3.4.** Let _G_=(_V,E_) be a weighted graph. There is a randomized algorithm that makes \(O(n\mathrm{log}^2n/\varepsilon^2)\) cut queries and returns a \((1+\varepsilon)\)-approximation to the densest subgraph of _G_.

