## Proximity.

For any optimal exchange solution (_A,B_), a simple exchange argument shows that the weights of items in _A_ and in _B_ do not share any non-zero common subset sum, i.e.,

\(\mathcal{S}^*(\text{weights}(A))\cap\mathcal{S}^*(\text{weights}(B))=\varnothing.\) (6)

Indeed, for an optimal knapsack solution \(X=(G\backslash B)\cup A\), if non-empty item sets \(A'\subseteq A\) and \(B'\subseteq B\) have the same total weight, then \((X\cup B')\backslash A'\) is a set of items with the same total weight as _X_ but _strictly_ higher total profit (since efficiencies of items in \(B'\subseteq G\) are strictly higher than efficiencies of items in \(A'\subseteq\overline{G}\) due to Eqs. (3) and (4)), contradicting the optimality of _X_.

The following proximity bound Eq. (7) is consequence of Eq. (5) and Eq. (6), and was used in previous works such as \[PRW21, CLMZ24\] (see e.g., \[PRW21, Lemma 2.1\] for a short proof): for any optimal exchange solution (_A,B_), it holds that

\(|A|+|B|\le 2w_\mathrm{max}.\) (7)

In other words, any optimal knapsack solution _X_ differs from the greedy solution _G_ by at most 2_w_<sub>max</sub> items. The bound of Eq. (7) immediately implies

\(W(A)+W(B)\le 2w_\mathrm{max}^2\) (8)

for any optimal exchange solution (_A,B_).

## Weight classes and ranks.

We rank items of the same weight _w_ according to their profits, as follows:

**Definition 2.3** (Rank of items)**.** For each \(w\in\mathcal{W}\), consider the weight-_w_ items outside the greedy solution, \(\overline{G}\cap I_{\{w\}}=\{i_1,i_2,\dots,i_m\}\), where \(p_{i_1}>p_{i_2}>\cdots>p_{i_m}\). We define \(\mathrm{rank}(i_1)=1,\mathrm{rank}(i_2)=2,\dots,\mathrm{rank}(i_m)=m\). Similarly, consider the weight-_w_ items in the greedy solution, \(G\cap I_{\{w\}}=\{i'_1,i'_2,\dots,i'_{m^\prime}\}\), where \(p_{i_1^\prime}<p_{i_2^\prime}<\cdots<p_{i_{m^\prime}^\prime}\). We define \(\mathrm{rank}(i'_1)=1,\mathrm{rank}(i'_2)=2,\dots,\mathrm{rank}(i'_{m^\prime})=m'\). In this way, every item \(i\in[n]\) receives a rank(_i_).

Then, a standard observation is that an optimal solution should always take a prefix from each weight class:

**Lemma 2.4** (Prefix property)**.** _Consider any optimal exchange solution_ (_A,B). If_ \(i\in A\)_, then_ \(\{i'\in\overline{G}\cap I_{w_i}:\mathrm{rank}(i')\le\mathrm{rank}(i)\}\subseteq A\)_, and_ \(\mathrm{rank}(i)\le 2w_\mathrm{max}\).

_Similarly, if_ \(i\in B\)_, then_ \(\{i'\in G\cap I_{w_i}:\mathrm{rank}(i')\le\mathrm{rank}(i)\}\subseteq B\)_, and_ \(\mathrm{rank}(i)\le 2w_\mathrm{max}\).

_Proof._ We only prove the \(i\in A\) case. The \(i\in B\) case is symmetric. Consider two weight-_w_ items \(i,i'\in\overline{G}\cap I_w\) with \(\mathrm{rank}(i')<\mathrm{rank}(i)\) and \(i\in A\). Suppose for contradiction that \(i'\notin A\). Then, \(p_{i^\prime}>p_i\), and hence \(((A\backslash\{i\})\cup\{i'\},B)\) is an exchange solution with the same weight as (_A,B_) but achieving strictly higher profit, contradicting the optimality of (_A,B_). Hence, _A_ contains all \(i'\in\overline{G}\cap I_w\) with \(\mathrm{rank}(i')\le\mathrm{rank}(i)\). Since \(|A|\le 2w_\mathrm{max}\) by Eq. (7), we must have \(\mathrm{rank}(i)\le 2w_\mathrm{max}\) for \(i\in A\).

We remark that all items \(i\in[n]\) with \(\mathrm{rank}(i)\le 2w_\mathrm{max}\) can be deterministically selected and sorted in \(O(n+w_\mathrm{max}^2\mathrm{log}w_\mathrm{max})\) time using linear-time median selection algorithms \[BFP<sup>+</sup>73\].

