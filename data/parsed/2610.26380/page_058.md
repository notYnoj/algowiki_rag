<tbc>**Step 1: learning on the recurrent space.** Lemma D.1 applies on \(\Omega_\mathcal{E}\). Hence for every \(\nu\in M\),

\(\nu^\top\mu_{t-1}^*\rightarrow\nu^\top\theta,\nu^\top\Sigma_{t-1}^*\nu\rightarrow 0\text{a.s. on}\Omega_\mathcal{E}.\)

Choose a basis \(L_1,\dots,L_d\in\mathcal{E}\) of _M_ and let \(A=[L_1\cdots L_d]\). By Cauchy-Schwarz,

\(|L_r^\top\Sigma_{t-1}^*L_s|\le\sqrt{L_r^\top\Sigma_{t-1}^*L_r}\sqrt{L_s^\top\Sigma_{t-1}^*L_s}\rightarrow 0,\)

so \(A^\top\Sigma_{t-1}^*A\rightarrow 0\) entrywise and hence in operator norm. It follows that

\(\|R_M\Sigma_{t-1}^*R_M\|_\mathrm{op}\rightarrow 0,R_M\mu_{t-1}^*\rightarrow R_M\theta\text{a.s. on}\Omega_\mathcal{E}.\)

**Step 2: approximate variance stays positive off the recurrent span.** Lemma D.2 applies with the conclusions of Step 1. Thus, almost surely on \(\Omega_\mathcal{E}\), there exists \(\eta>0\) such that \(Q\Sigma_{t-1}^*Q\unknown\eta Q\) for all sufficiently large _t_. By Lemmas D.3 and D.4,

\(\|R_M\Sigma_{t-1}R_M\|_\mathrm{op}\rightarrow 0,\|R_M\Sigma_{t-1}Q\|_\mathrm{op}+\|Q\Sigma_{t-1}R_M\|_\mathrm{op}\rightarrow 0,Q\Sigma_{t-1}Q\unknown\chi_-\eta Q\) (D.2)

almost surely on \(\Omega_\mathcal{E}\), where the last inequality holds for all sufficiently large _t_.

**Step 3: the sum of scores stays bounded away from zero.** The conditions of Lemma D.7 follow from (D.2), Assumption 2(ii), and Lemma D.3. Therefore,

\(\mathrm{liminf}_{t\rightarrow\infty}\sum_{L\in\mathcal{D}}G_t(L)>0\text{a.s. on}\Omega_\mathcal{E}.\) (D.3)

**Step 4: every recurrent direction’s score goes to 0.** Fix \(L\in\mathcal{E}\). Since \(L\in M\), Step 1 gives \(L^\top\Sigma_{t-1}^*L\rightarrow 0\). Assumption 2(i) then yields<tbc>

\(L^\top\Sigma_{t-1}L\le\chi_+L^\top\Sigma_{t-1}^*L\rightarrow 0.\)

<tbc>Lemma D.6 therefore implies<tbc>

\(G_t(L)\rightarrow 0\text{a.s. on}\Omega_\mathcal{E}.\)

<tbc>Thus<tbc>

\(\sum_{L\in\mathcal{E}}G_t(L)\rightarrow 0\text{a.s. on}\Omega_\mathcal{E}.\) (D.4)

<tbc>**Step 5: contradiction with the chosen evaluation.** By (D.3), (D.4),

\(\mathrm{liminf}_{t\rightarrow\infty}\sum_{L\in\mathcal{D}\backslash\mathcal{E}}G_t(L)>0\text{a.s. on}\Omega_\mathcal{E}.\)

<tbc>Therefore,

\(\mathrm{liminf}_{t\rightarrow\infty}\mathrm{max}_{L\in\mathcal{D}\backslash\mathcal{E}}G_t(L)>0,\mathrm{max}_{L\in\mathcal{E}}G_t(L)\rightarrow 0.\)

