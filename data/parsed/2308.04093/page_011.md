• Let \(\mathcal{W}=\mathrm{supp}(\{w_1,w_2,\dots,w_n\})\subseteq[w_\mathrm{max}]\) be the set of input item weights.<tbc>

• For \(\mathcal{W}'\subseteq\mathcal{W}\), let \(I_{\mathcal{W}^\prime}:=\{i\in[n]:w_i\in\mathcal{W}'\}\) denote the set of items with weights in \(\mathcal{W}'\).<tbc>

• For \(I=\{i_1,\dots,i_{|I|}\}\subseteq[n]\), let weights(_I_)={_w_<sub>_i_<sub>1</sub></sub>_,...,w_<sub>_i_<sub>_|I_|</sub></sub>} be the _multiset_ of weights of items in _I_.

We assume \(w_\mathrm{max}\le t\) by ignoring items that are too large to fit into the knapsack. We assume \(w_1+\cdots+w_n>t\), since otherwise the trivial optimal solution is to include all the items. We assume \(w_\mathrm{max}\le n^2\), because when _w_<sub>max</sub>_\>n_<sup>2</sup> it is faster to run the textbook dynamic programming algorithm \[Bel57\] in \(O(nt)\le O(n\cdot nw_\mathrm{max})\le O(w_\mathrm{max}^2)\) time. We use the standard word-RAM computation model with \(\Theta(\mathrm{log}n)\)-bit words, and we assume \(p_i\le p_\mathrm{max}\) fits into a single machine word.<sup>6</sup>

The _efficiency_ of item _i_ is _p<sub>i</sub>/w<sub>i</sub>_. We always assume the input items have _distinct_ efficiencies _p<sub>i</sub>/w<sub>i</sub>_. This assumption is justified by the following tie-breaking lemma proved in Appendix B.1.

**Lemma 2.1** (Break ties)**.** _Given a 0-1 Knapsack instance I, in O(n_) _time we can deterministically reduce it to another 0-1 Knapsack instance_ \(I'\) _with n,w_<sub>max</sub> _and t unchanged, and_ \(p'_\mathrm{max}\le\mathrm{poly}(p_\mathrm{max},w_\mathrm{max},n)\)_, such that the items in_ \(I'\) _have_ distinct efficiencies _and distinct profits._

## 2.2 Greedy solution and proximity

### Greedy solution.

Sort the _n_ input items in decreasing order of efficiency,<tbc>

\(p_1/w_1>p_2/w_2>\cdots>p_n/w_n.\) (3)

<tbc>The _greedy solution_ (or _maximal prefix solution_) is the item subset

\(G=\{1,2,\dots,i^*\},\text{where}i^*=\mathrm{max}\{i^*:w_1+w_2+\cdots+w_{i^*}\le t\},\) (4)

i.e., we greedily take the most efficient items one by one, until the next item cannot be added without exceeding the knapsack capacity. Since the input instance is nontrivial, we have \(1\le i^*\le n-1\), and \(W(G)\in(t-w_\mathrm{max},t]\). Denote the remaining items as <o>_G_</o>=\[_n_\]\\_G_={_i_<sup>∗</sup>+1_,i_<sup>∗</sup>+2_,...,n_}.

**Remark 2.2.** As noted by \[PRW21\], the greedy solution _G_ can be found in deterministic _O(n_) time using linear-time median finding algorithms \[BFP<sup>+</sup>73\] (if we only need the set _G_ rather than the order of their elements), as opposed to a straightforward _O(n_log_n_)-time sorting according to Eq. (3).

Every item subset \(X\subseteq[n]\) can be written as \(X=(G\backslash B)\cup A\) where \(A\subseteq\overline{G}\) and \(B\subseteq G\). Finding an optimal knapsack solution _X_ is equivalent to finding an _optimal exchange solution_, defined as a pair of subsets \((A,B)(A\subseteq\overline{G},B\subseteq G)\) that maximizes _P(A_)-_P(B_) subject to \(W(A)-W(B)\le t-W(G)\). Since any optimal knapsack solution _X_ satisfies \(W(X)\in(t-w_\mathrm{max},t]\), we have

\(0\le W(A)-W(B)=W(X)-W(G)<w_\mathrm{max}\) (5)

for any optimal exchange solution (_A,B_).

<sup>6</sup>If this assumption is dropped, we simply pay an extra _O_(log_p_<sub>max</sub>) factor in the running time for adding integers of magnitude (_np_<sub>max</sub>)<sup>_O_(1)</sup>.

