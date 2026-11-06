1. _Given a hinted-_\((J_{\le j-1}^+\cup J_{\le j-1}^-)\)_-optimal DP table of size L_<sub>_j_-1</sub> _with positive and negative hint size b<sub>j</sub>, we can compute a hinted-_\((J_{\le j}^+\cup J_{\le j-1}^-)\)_-optimal DP table of size L<sub>j</sub> with positive hint size b_<sub>_j_+1</sub> _and negative hint size b<sub>j</sub>, in_ \(O(L_jb_j\cdot\mathrm{log}^2(L_jb_j)+|J_j^+|)\) _time._<tbc>

_2._ _Given a hinted-_\((J_{\le j}^+\cup J_{\le j-1}^-)\)_-optimal DP table of size L<sub>j</sub> with positive hint size b_<sub>_j_+1</sub> _and negative hint size b<sub>j</sub>, we can compute a hinted-_\((J_{\le j}^+\cup J_{\le j}^-)\)_-optimal DP table of size L<sub>j</sub> with positive and negative hint size b_<sub>_j_+1</sub>_, in_ \(O(L_jb_j\cdot\mathrm{log}^2(L_jb_j)+|J_j^-|)\) _time._

Lemma 3.9 immediately implies our overall first-stage algorithm:

_Proof of Lemma 3.3 assuming Lemma 3.9._ We start with the trivial hinted DP table with _q_\[0\]=0 and _S_<sup>+</sup>\[0\]=_S_<sup>-</sup>\[0\]=W<sub>1</sub> (padded with \(q[z]=-\infty\) for \(z\in\{-L_0,\dots,L_0\}\backslash\{0\}\)). By definition, _q_\[\] is hinted-\(\varnothing\)-optimal, and has positive and negative hint size \(|\mathcal{W}_1|\le b_1\). Then, we iteratively perform phases _j_=1,2_,...,k_, where in phase _j_ we first apply Item 1 of Lemma 3.9, and then apply Item 2 of Lemma 3.9. In the end of phase _k_, we have obtained a hinted-\((J_{\le k}^+\cup J_{\le k}^-)\)-optimal DP table. By Item 1 of Lemma 3.7, it is an _I_<sub>W<sub>1</sub></sub>-optimal DP table as desired.

The total time of applying Lemma 3.9 is (up to a constant factor)

\(\sum_{j=1}^k\left(L_jb_j\cdot\mathrm{log}^2(L_jb_j)+|J_j^+|+|J_j^-|\right)\)<br>
\(\le\sum_{j=1}^km_jw_\mathrm{max}b_j\mathrm{log}^2(m_jw_\mathrm{max}b_j)+n\)<br>
\(=\sum_{j=1}^kC^2w_\mathrm{max}^2\mathrm{log}(2w_\mathrm{max})\mathrm{log}^2\left(C^2w_\mathrm{max}^2\mathrm{log}(2w_\mathrm{max})\right)+n\text{(by Eqs. (12) and (13))}\)<br>
\(\le O(w_\mathrm{max}^2\mathrm{log}^4w_\mathrm{max}+n).\text{(by}k=\lceil\mathrm{log}_2(2w_\mathrm{max}+1)\rceil\text{)}\)

It remains to prove Lemma 3.9. In the following, we will reduce it to a core subproblem called HintedKnapsackExtend<sup>+</sup>, which captures the task of updating a hinted size-_L_ DP table with positive hint size _b_ using "positive items" whose weights come from some positive integer set _U_ (here we can think of _U_=W<sub>1</sub>). Similarly to the proof of the batch-update lemma (Lemma 2.7) based on SMAWK, here we also use a function \(Q_w:\mathbb{Z}_{\ge 0}\rightarrow\mathbb{Z}\) to represent the total profit of taking the top-_x_ items of weight _w_.

**Problem 1** (HintedKnapsackExtend<sup>+</sup>)**.** _Let_ \(U\subseteq\mathcal{W}_1\)_. For every_ \(w\in U\)_, suppose_ \(Q_w:\mathbb{Z}_{\ge 0}\rightarrow\mathbb{Z}\) _is a concave function with Q<sub>w</sub>_(0)=0 _that can be evaluated in constant time. We are given a DP table q_\[-_L...L_\] _(where_ \(q[i]\in\mathbb{Z}\cup\{-\infty\}\)_), annotated with S_\[-_L...L_\] _where_ \(S[i]\subseteq U\).

_Consider the following optimization problem for each_ \(-L\le i\le L\)_: find a solution vector_ \(x[i]\in\mathbb{Z}_{\ge 0}^U\) _that maximizes the total profit_

\(r[i]:=q\big[z[i]\big]+\sum_{w\in U}Q_w(x[i]_w),\) (15)

