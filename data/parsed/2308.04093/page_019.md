## 3.3 The first-stage algorithm via hinted dynamic programming

Based on our rank partitioning \(J_1^+\unknown J_1^-\unknown\cdots\unknown J_k^+\unknown J_k^-\subseteq I_{\mathcal{W}_1}\), \(k=\lceil\mathrm{log}_2(2w_\mathrm{max}+1)\rceil\) (Definition 3.5) and its structural lemma (Lemma 3.7), our first-stage algorithm uses dynamic programming and runs in _k_ phases. At the beginning of the _j_-th phase \((1\le j\le k)\), we have a \((J_{\le j-1}^+\cup J_{\le j-1}^-)\)-optimal DP table, and we first update it with the "positive items" \(J_j^+\) to obtain a \((J_{\le j}^+\cup J_{\le j-1}^-)\)-optimal DP table, and then update it with the "negative items" \(J_j^-\) to obtain a \((J_{\le j}^+\cup J_{\le j}^-)\)-optimal DP table. We will adjust the size of the DP table throughout the _k_ phases based on Item 2 of Lemma 3.7. This is similar to the second-stage algorithm from Section 3.1, except that in Section 3.1 the DP table is shrinking whereas here it will be expanding.

To implement the DP efficiently, we crucially rely on Item 3 of Lemma 3.7, which gives an upper bound on the "active support" of the weights of items in every partial solution in the current DP table. More specifically, consider an _I_<sub>W<sub>1</sub></sub>-optimal partial solution \((A',B')\) and its restriction \((A'',B'')\) where \(A''=A'\cap J_{\le j-1}^+,B''=B'\cap J_{\le j-1}^-\). Then Item 3 of Lemma 3.7 implies that the items in \(A'\backslash A''\) (or \(B'\backslash B''\)) can only have at most _b<sub>j</sub>_ distinct weights. This means that, for any partial solution \((A'',B'')\) in the DP table at the end of phase _j_-1, in order to extend it to an _I_<sub>W<sub>1</sub></sub>-optimal partial solution \((A',B')\) in future phases, we only need to update it with items from these _b<sub>j</sub>_ weight classes determined by Item 3 of Lemma 3.7. This idea is called _witness propagation_, and was originally introduced by Deng, Mao, and Zhong \[DMZ23\] in the context of unbounded knapsack-type problems. Implementing this idea in the more difficult 0-1 setting is a main technical contribution of this paper.

In the rest of this section, we will introduce a few more definitions to help use formally describe our algorithm, and we will abstract out a core subproblem called HintedKnapsackExtend<sup>+</sup> which captures the aforementioned idea of witness propagation. Then we will show how to implement our first-stage algorithm and prove Lemma 3.3, assuming HintedKnapsackExtend<sup>+</sup> can be solved efficiently.

In the following definition, we augment each entry of the DP table with hints, which contain the weight classes from which we need to add items when we update this entry, as we just discussed.

**Definition 3.8** (Hinted DP tables)**.** A _hinted DP table_ is a DP table \(q[\unknown]\) where each entry \(q[z]\neq-\infty\) is annotated with two sets \(S^+[z],S^-[z]\subseteq\mathcal{W}_1\). We say the table has _positive hint size b_ if \(|S^+[z]|\le b\) for all _z_, and has _negative hint size b_ if \(|S^-[z]|\le b\) for all _z_.

For an item subset \(J\subseteq I_{\mathcal{W}_1}\), we say a hinted DP table \(q[\unknown]\) is _hinted-J-optimal_, if \(q[\unknown]\) is _J_-valid (see Definition 2.6), and it has an entry \(q[z]\) such that both of the following hold:

1. There exists an _I_<sub>W<sub>1</sub></sub>-optimal partial solution \((A',B')\) such that \(W(A'\cap J)-W(B'\cap J)=z\) and \(P(A'\cap J)-P(B'\cap J)=q[z]\).<tbc>

2. Every _I_<sub>W<sub>1</sub></sub>-optimal partial solution \((A',B')\) with \(W(A'\cap J)-W(B'\cap J)=z\) should satisfy \(A'\backslash J\subseteq I_{S^+[z]}\) and \(B'\backslash J\subseteq I_{S^-[z]}\).

Note that if a hinted DP table is hinted-_J_-optimal, then in particular it is _J_-optimal in the sense of Definition 2.6 (due to Item 1 of Definition 3.8).

The following lemma summarizes each of the \(k=\lceil\mathrm{log}_2(2w_\mathrm{max}+1)\rceil\) phases in our first-stage algorithm.

**Lemma 3.9.** _Let k,m<sub>j</sub>,b<sub>j</sub> be defined as in Lemma 3.7. Let_ \(L_j:=m_j\cdot w_\mathrm{max}\)_. For every_ \(1\le j\le k\)_, the following hold:_

