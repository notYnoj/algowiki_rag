<tbc>Hence there exists an almost-surely finite random time _T_<sub>1</sub> such that, for every \(t\ge T_1\),

\(max_{L\in\mathcal{D}\backslash\mathcal{E}}G_t(L)>max_{L\in\mathcal{E}}G_t(L).\)

Since SA maximizes the score (D.1) over D, the direction chosen at round _t_ cannot be in E for all sufficiently large _t_. But after round _T_<sup>∗</sup>, every sampled direction lies in E. Contradiction. Therefore,

\(\mathbf{1}^\perp\subseteq span(E_\infty)\text{almost surely.}\)

**Step 6: convergence.** It remains to show that the full history identifies \(P\unknown\), after which Lemma D.8 implies the conclusion of the theorem. Fix \(\mathcal{E}\subseteq\mathcal{D}\). On \(\Omega_\mathcal{E}\), for each _i_=1_,...,I_, we have \(Pe_i\in\mathbf{1}^\perp\subseteq M\), so Lemma D.1 implies that \(\mathbb{1}_{\Omega_\mathcal{E}}(Pe_i)^\top\unknown\) is \(\mathcal{H}_\infty\)-measurable. Since \((P\unknown)_i=e_i^\top P\unknown=(Pe_i)^\top\unknown\), it follows that \(\mathbb{1}_{\Omega_\mathcal{E}}P\unknown\) is \(\mathcal{H}_\infty\)-measurable. Since \(P\unknown=\sum_{\mathcal{E}\subseteq\mathcal{D}}\mathbb{1}_{\Omega_\mathcal{E}}P\unknown\) a.s., \(P\unknown\) is \(\mathcal{H}_\infty\)-measurable.

Therefore, for each _i_=1_,...,I_,<tbc>

\((P\mu_{t-1}^*)_i=\mathbb{E}[(P\unknown)_i|\mathcal{H}_t]\rightarrow(P\unknown)_i\text{a.s. and in}L^1,\)

<tbc>by Doob’s theorem. Hence<tbc>

\(\mathbb{E}\|P\mu_{t-1}^*-P\unknown\|_\infty\le\sum_{i=1}^I\mathbb{E}\big|(P\mu_{t-1}^*-P\unknown)_i\big|\rightarrow 0.\)

<tbc>This establishes convergence for the exact posterior mean along the run without a budget constraint. We now return to the procedure with budget _R_ and show that \(\mathbb{E}\|P\mu_T-P\unknown\|_\infty\rightarrow 0\) as \(R\rightarrow\infty\). For a run with budget _R_, take \(t=\lfloor R/max(r_0,r_1)\rfloor\) so that for the first _t_ evaluations this is equivalent to the unbudgeted run considered above. Its terminal history therefore contains the history through evaluation _t_. Jensen’s inequality and the triangle inequality give

\(\mathbb{E}\|P\mu_T^*-P\unknown\|_\infty\le\mathbb{E}\|P\mu_T^*-P\mu_t^*\|_\infty+\mathbb{E}\|P\mu_t^*-P\unknown\|_\infty\)<br>
\(=\mathbb{E}\left\|\mathbb{E}\big[P\unknown-P\mu_t^*\big|\mathcal{H}_{T+1}\big]\right\|_\infty+\mathbb{E}\|P\mu_t^*-P\unknown\|_\infty\)<br>
\(\le 2\mathbb{E}\|P\mu_t^*-P\unknown\|_\infty\rightarrow 0\text{as}R\rightarrow\infty.\)

Also, for any \(z\in\mathbb{R}^I\), \(\|zz\|_\infty\le 2\|z\|_\infty\). Thus, by Assumption 2(iii),<tbc>

\(\mathbb{E}\|P\mu_T-P\unknown\|_\infty\le\mathbb{E}\|P\mu_T-P\mu_T^*\|_\infty+\mathbb{E}\|P\mu_T^*-P\unknown\|_\infty\le 2\mathbb{E}\|\mu_T-\mu_T^*\|_\infty+\mathbb{E}\|P\mu_T^*-P\unknown\|_\infty\rightarrow 0.\)

<tbc>Lemma D.8 gives

\(\mathbb{E}[OC_T]\rightarrow 0\text{as}R\rightarrow\infty.\) □

## Appendix E: Supplement to §7

The figures below are the counterparts of Figure 2, Figure 3a, and Figure 6 for all other configurations.

### E.1. Allocations over the budget

