<tbc>_where_ \(z[i]\in\mathbb{Z}\) _is uniquely determined by_

\(z[i]+\sum_{w\in U}w\cdot x[i]_w=i.\) (16)

_The task is to solve this optimization problem for each_ \(-L\le i\le L\) with the following relaxation:

• _If_ all _maximizers_ (**_x_**\[_i_\]_,z_\[_i_\]) _of Eq._ (15) _(subject to Eq._ (16)_) satisfy_

\(\mathrm{supp}(x[i])\subseteq S\big[z[i]\big],\) (17)

_then we are required to correctly output a maximizer for i._

• _Otherwise, we are allowed to output a suboptimal solution for i._

**Remark 3.10.** We give a few remarks to help get a better understanding of Problem 1:

1. In Eq. (16), \(z[i]\le i\) must hold, since \(w\in U\subseteq[w_\mathrm{max}]\) is always positive and **_x_**\[_i_\] is a nonnegative vector.<tbc>

2. If we do not have the relaxation based on hints _S_\[_i_\], then Problem 1 becomes a standard problem solvable in _O_(|_U|L_) time using SMAWK algorithm (basically, repeat the proof of Lemma 2.7 for every \(w\in U\); see also \[PRW21, CLMZ24, AT19, KP04\]).<tbc>

3. Under this relaxation, without loss of generality, we can assume the output of Problem 1 always satisfies \(\mathrm{supp}(x[i])\subseteq S\big[z[i]\big]\) (Eq. (17)) for all \(-L\le i\le L\). (If we had to output an **_x_**\[_i_\] that violates Eq. (17), then we must be in the "otherwise" case for _i_, and should be allowed to output anything). In particular, if \(|S[i]|\le b\) for all \(-L\le i\le L\), then we can assume the output **_x_**\[-_L...L_\] of Problem 1 has description size _O(bL_) words.<tbc>

4. Note that Problem 1 is different from (and easier than) the task of maximizing Eq. (15) for every _i_ subject to Eq. (17). The latter version would make a cleaner definition, but it is a harder problem which we do not know how to solve.

The following Theorem 3.11 summarizes our algorithm for Problem 1, which will be given in Section 4.

**Theorem 3.11.** _HintedKnapsackExtend_<sup>+</sup> _(Problem 1) with_ \(|S[i]|\le b\) _for all_ \(-L\le i\le L\) _can be solved deterministically in O(Lb_log<sup>2</sup>(_Lb_)) _time._

Finally, we show how to prove Lemma 3.9 using Theorem 3.11.

_Proof of Lemma 3.9 assuming Theorem 3.11._ Here we only prove Item 1 of Lemma 3.9 (Item 2 can be proved similarly in the reverse direction). Given a hinted-\((J_{\le j-1}^+\cup J_{\le j-1}^-)\)-optimal DP table _q_\[-_L_<sub>_j_-1</sub>_...L_<sub>_j_-1</sub>\] with positive hint size \(|S^+[i]|\le b_j\) and negative hint size \(|S^-[i]|\le b_j\), our task is to compute a hinted-\((J_{\le j}^+\cup J_{\le j-1}^-)\)-optimal DP table _r_\[\], by updating _q_\[\] with items from \(J_j^+\).

As usual, partition \(J_j^+\) into weight classes: for each \(w\in\mathcal{W}_1\), let the weight-_w_ items \(J_j^+\cap I_{\{w\}}=\{i_1,i_2,\dots,i_m\}\) be sorted so that \(p_{i_1}>p_{i_2}>\cdots>p_{i_m}\), and define their top-_x_ total profit \(Q_w(x):=p_{i_1}+p_{i_2}+\cdots+p_{i_x}\), which is a concave function in _x_. After preprocessing in \(O(|J_j^+|+|\mathcal{W}_1|w_\mathrm{max}\mathrm{log}w_\mathrm{max})\) total time, \(Q_w(\cdot)\) can be evaluated in constant time for all \(w\in\mathcal{W}_1\).

