As in Section 3.1, every certified biclique produced by Recurrence (4) is added to \(\Gamma\), while the bicliques corresponding to the remaining recursive subproblems form \(\Pi\).

For _i_=1, we apply Lemma 1 once with _r=n_<sup>1/3</sup>/log<sup>2</sup>_n_. The running time is _O(n_<sup>4/3</sup>/log_n_), and \(\sum_t(|A_t|+|B_t|)=O(n^{4/3}/\mathrm{log}n)\). The total number of uncertain pairs recorded in \(\Pi\) is _O(n_<sup>4/3</sup>log<sup>4</sup>_n_).

Let \(N(\Pi)\) denote the number of uncertain pairs recorded in \(\Pi\). Since all certified pairs are represented in \(\Gamma\), we have<tbc>

\(\sum_{A_t\times B_t\in\Gamma}|A_t||B_t|=|S\cap I|-N(\Pi).\)

<tbc>Since \(N(\Pi)\le cn^{4/3}\mathrm{log}^4n\) for some constant _c\>_0, and Theorem 3 assumes \(|S\cap I|\ge c_1n^{4/3}\mathrm{log}^4n\), we obtain<tbc>

\(\sum_{A_t\times B_t\in\Gamma}|A_t||B_t|\ge(1-\frac{c}{c_1})|S\cap I|.\)

<tbc>Therefore, by choosing _c_<sub>1</sub> sufficiently large, we have

\(\sum_{A_t\times B_t\in\Gamma}|A_t||B_t|\ge 0.4|S\cap I|.\)

This proves the theorem for _i_=1.

For _i_=2, we apply Recurrence (4) twice. As shown in Section 3.1, the running time becomes _O(n_<sup>4/3</sup>/loglog_n_), while the total number of uncertain pairs is _O(n_<sup>4/3</sup>log<sup>4</sup>log_n_). Again, all certified pairs are recorded in \(\Gamma\), and therefore \(\sum_{A_t\times B_t\in\Gamma}|A_t||B_t|=|S\cap I|-N(\Pi)\). Using the assumption \(|S\cap I|\ge c_1n^{4/3}(\mathrm{loglog}n)^4\) and choosing _c_<sub>1</sub> sufficiently large yields \(\sum_{A_t\times B_t\in\Gamma}|A_t||B_t|\ge 0.4|S\cap I|\).

The size bound \(\sum_t(|A_t|+|B_t|)=O(n^{4/3}/\mathrm{loglog}n)\) follows directly from the recurrence. This proves the theorem for _i_=2.

## 4.2 The case \(i\ge 3\)

For \(i\ge 3\), one might try to continue applying Recurrence (4). As discussed in Section 3.2, this approach incurs a constant-factor loss at every recursive level and therefore does not yield the bounds of Theorem 3 for general _i_. Consequently, a different approach is required.

The high-level framework remains the same as in Section 3.2. We again apply the recurrence twice and reduce the problem to a collection of tiny subproblems _T(q,q_), where _q_=log<sup>6</sup>log_n_. However, the way we solve these subproblems is fundamentally different.

For approximate counting, it suffices to know, for each cell of the last cutting, how many annuli completely contain the cell. This allows us to count certified pairs without explicitly constructing bicliques. For distance representation, however, this information is no longer sufficient. We must explicitly organize the target pairs into bicliques, and therefore a new idea is needed.

We follow the same notation as in Section 3.2 and obtain Recurrence (5). We add all certified bicliques produced during the first two recursive levels to \(\Gamma\). This takes _O(n_<sup>4/3</sup>/loglog_n_) time, and the total contribution to \(\sum_t(|A_t|+|B_t|)\) is bounded by the same bound.

Next, for every subproblem _T(q,q_), we apply Recurrence (6) and again add all certified bicliques to \(\Gamma\). This contributes _O(q_<sup>4/3</sup>_/g_<sup>2</sup>) time and the same asymptotic amount to the total representation size.

We now solve the subproblem _T(q_<sup>1/3</sup>_g_<sup>4</sup>_,q_<sup>2/3</sup>_g_<sup>2</sup>) in Recurrence (6), which corresponds to an unresolved biclique \(A'\times B'\) with \(A'\subseteq A\), \(B'\subseteq B\), \(|A'|\le q^{1/3}g^4\), and \(|B'|\le q^{2/3}g^2\). Let \(m'=|A'|\) and \(n'=|B'|\).

Let \(\mathcal{D}'\) be the set of annuli defined by the points of \(A'\) with respect to the interval _I_. We compute a hierarchical \((1/r')\)-cutting \(\{\Xi_0,\Xi_1,\dots,\Xi_k\}\) for \(\mathcal{D}'\), where \(r'=m'/g^6\). This takes \(O(m'r')\) time. Let \(\Xi\) denote the set of all cutting cells.

