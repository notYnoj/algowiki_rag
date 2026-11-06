_Proof of Claim 3.4._ We need to update the DP table using items from _I_<sub>W<sub>_j_</sub></sub>. Partition them into \(I_{\mathcal{W}_j}^+=I_{\mathcal{W}_j}\cap\overline{G}\) and \(I_{\mathcal{W}_j}^-=I_{\mathcal{W}_j}\cap G\) (recall from Section 2.2 that _G_ denotes the greedy solution). We first update the DP table with the "positive items" \(I_{\mathcal{W}_j}^+\). By a similar proof to Eq. (9), we know

\(|W(B\cap I_{\mathcal{W}_{\le j-1}})-W(A\cap I_{\mathcal{W}_{\le j}})|\le L_{j-1}\)

holds for any optimal exchange solution (_A,B_). Hence, we can iterate over \(w\in\mathcal{W}_j\), and use the batch-update lemma based on SMAWK (Lemma 2.7) to update the size-_L_<sub>_j_-1</sub> DP table with the weight-_w_ items \(I_{\{w\}}\cap\overline{G}\), in \(O(L_{j-1}+|I_{\{w\}}\cap\overline{G}|+w_\mathrm{max}\mathrm{log}w_\mathrm{max})\) time. In the end we ob tain a \((I_{\mathcal{W}_{\le j-1}}\cup I_{\mathcal{W}_j}^+)\)-optimal DP table of size _L_<sub>_j_-1</sub>, in total time \(\sum_{w\in\mathcal{W}_j}O(L_{j-1}+|I_{\{w\}}\cap\overline{G}|+w_\mathrm{max}\mathrm{log}w_\mathrm{max})=O(|\mathcal{W}_j|(L_{j-1}+w_\mathrm{max}\mathrm{log}w_\mathrm{max})+|I_{\mathcal{W}_j}\cap\overline{G}|)\).

Then, we update the \((I_{\mathcal{W}_{\le j-1}}\cup I_{\mathcal{W}_j}^+)\)-optimal DP table with the "negative items" \(I_{\mathcal{W}_j}^-\), and obtain an \(I_{\mathcal{W}_{\le j}}\)-optimal DP table. This algorithm is symmetric to the positive case described above, and similarly runs in time \(O(|\mathcal{W}_j|(L_{j-1}+w_\mathrm{max}\mathrm{log}w_\mathrm{max})+|I_{\mathcal{W}_j}\cap G|)\).

In the end, we shrink the size of the obtained DP table to _L<sub>j</sub>_. By Eq. (9), this does not affect the \(I_{\mathcal{W}_{\le j}}\)-optimality of the DP table. The total running time is \(O(|\mathcal{W}_j|(L_{j-1}+w_\mathrm{max}\mathrm{log}w_\mathrm{max})+|I_{\mathcal{W}_j}|)\).

In the main algorithm, starting from the _I_<sub>W<sub>1</sub></sub>-optimal DP table, we sequentially apply Claim 3.4 for _j_=2,3_,...,s_, and in the end we can obtain an \(I_{\mathcal{W}_{\le s}}\)-optimal DP table. Note that \(I_{\mathcal{W}_{\le s}}=\lceil n\rceil\), so the final DP table contains an optimal exchange solution. The total time for applying Claim 3.4 is (up to a constant factor)

\(\sum_{j=2}^s\left(|\mathcal{W}_j|(L_{j-1}+w_\mathrm{max}\mathrm{log}w_\mathrm{max})+|I_{\mathcal{W}_j}|\right)\)<br>
\(\le\sum_{j=2}^s4C\sqrt{w_\mathrm{max}\mathrm{log}w_\mathrm{max}}\cdot 2^j\cdot(4Cw_\mathrm{max}^{3/2}/2^{j-1}+2w_\mathrm{max}\mathrm{log}w_\mathrm{max})+\sum_{j=2}^s|I_{\mathcal{W}_j}|\)<br>
\(=\sum_{j=2}^s\left(32C^2w_\mathrm{max}^2\sqrt{\mathrm{log}w_\mathrm{max}}+8C\cdot 2^j\cdot(w_\mathrm{max}\mathrm{log}w_\mathrm{max})^{3/2}\right)+\sum_{j=2}^s|I_{\mathcal{W}_j}|\)<br>
\(\le O(w_\mathrm{max}^2(\mathrm{log}w_\mathrm{max})^{3/2}+n).(\text{by}s<\mathrm{log}_2(\sqrt{w_\mathrm{max}}))\)

The time complexity of the entire algorithm is dominated by the \(O(n+w_\mathrm{max}^2\mathrm{log}^4w_\mathrm{max})\) running time of the first stage (Lemma 3.3).

## 3.2 Rank partitioning

Given \(\mathcal{W}_1\subseteq[w_\mathrm{max}]\) of size \(|\mathcal{W}_1|\le O(\sqrt{w_\mathrm{max}\mathrm{log}w_\mathrm{max}})\) from Lemma 3.2, we partition the items whose weights belong to W<sub>1</sub> into dyadic groups based on their ranks (Definition 2.3), as follows:

**Definition 3.5** (Rank partitioning)**.** Let \(k=\lceil\mathrm{log}_2(2w_\mathrm{max}+1)\rceil\). For each \(1\le j\le k\), define item subsets<tbc>

\(J_j^+:=\{i\in\overline{G}\cap I_{\mathcal{W}_1}:2^{j-1}\le\mathrm{rank}(i)\le 2^j-1\},\)

<tbc>and<tbc>

\(J_j^-:=\{i\in G\cap I_{\mathcal{W}_1}:2^{j-1}\le\mathrm{rank}(i)\le 2^j-1\}.\)

