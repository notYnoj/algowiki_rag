\(\sum_{e\in\tilde{\delta}(u)}x_e=1\forall u\in A\cup B\)<br>
\(x_e\ge 0\forall e\in\tilde{E}.\)

\(\text{minimize}\sum_{u\in A\cup B}\alpha_u\) (LP2)

subject to<tbc>

\(\begin{array}{ c c c c }
\alpha_a+\alpha_b & \ge & \mathsf{wt}_M(a,b) & \forall(a,b)\in E \\
\alpha_u & \ge & \mathsf{wt}_M(u,u) & \forall u\in A\cup B.
\end{array}\)

Any popular matching in _G_ is an optimal solution to (LP1) and any witness of _M_ is an optimal solution to (LP2). So if (_a,b_) is a popular edge, then complementary slackness implies that \(\alpha_a+\alpha_b=\mathsf{wt}_M(a,b)\), where \(\alpha\in\{0,\pm 1\}^n\) is a witness of _M_. Since \(\mathsf{wt}_M(a,b)\in\{0,\pm 2\}\), \(\alpha_a\) and \(\alpha_b\) have the same parity. So either \(\alpha_a=\alpha_b=0\) or \(\alpha_a,\alpha_b\in\{\pm 1\}\).

Let _u_ be an unstable vertex in _G_. Let _S_ be a stable matching in _G_. The perfect matching \(\tilde{S}\) contains therefore the self-loop (_u,u_). Since \(\tilde{S}\) is an optimal solution to (LP1) (recall that every stable matching is popular), we have \(\alpha_u=\mathsf{wt}_M(u,u)\) by complementary slackness. Thus \(\alpha_u=0\) if and only if _u_ is left unmatched in _M_ (otherwise \(\alpha_u=-1\)).

For every connected component _C<sub>i</sub>_ in _G_<sub>0</sub>, it follows from our first observation above that either (i) \(\alpha_u=0\) for all vertices \(u\in C_i\) or (ii) \(\alpha_u=\pm 1\) for all vertices \(u\in C_i\). For every unstable vertex _u_, we have \(\alpha_u=\mathsf{wt}_M(u,u)\) (by our second observation above). Hence in case (i), all unstable vertices in _C<sub>i</sub>_ are left unmatched in _M_ and in case (ii), all unstable vertices in _C<sub>i</sub>_ are matched in _M_. \(\sqcap\sqcup\)

Let _C_<sub>1</sub>_,...,C<sub>k</sub>_ be the non-trivial connected components in _G_<sub>0</sub>. Consider _C<sub>i</sub>_ where \(i\in\{1,\dots,k\}\). We know from Observation 1 that the number of unstable vertices in \(A\cap C_i\) is the same as the number of unstable vertices in \(B\cap C_i\). Let _a_<sub>1</sub>_,...,a<sub>t</sub>_ be the unstable vertices in \(A\cap C_i\) and let _b_<sub>1</sub>_,...,b<sub>t</sub>_ be the unstable vertices in \(B\cap C_i\). Compute an arbitrary pairing of _a_<sub>1</sub>_,...,a<sub>t</sub>_ with _b_<sub>1</sub>_,...,b<sub>t</sub>_ -- this partitions unstable vertices of _C<sub>i</sub>_ into disjoint pairs, say \((a_j,b_j):1\le j\le t\). Let _S<sub>i</sub>_ be the set of these _t_ pairs.

We also consider the trivial or singleton components in _G_<sub>0</sub>: each such component consists of a single _unpopular_ vertex, i.e., a vertex that is left unmatched in every popular matching. Since \(|A\cap C_i|=|B\cap C_i|\) for every non-trivial component _C<sub>i</sub>_ and \(|A|\ge|B|\), there are at least as many unpopular vertices in _A_ as in _B_. We compute an arbitrary pairing _S_<sub>0</sub> between unpopular vertices in _A_ and in _B_. If |_A|\>|B_| then some unpopular vertices in _A_ are left out of _S_<sub>0</sub>.

The instance \(G^*=(A\cup B,E^*)\) is defined as follows: \(E^*=\cup_{i=0}^kS_i\cup E\). So _G_<sup>∗</sup> is the graph _G_ augmented with new edges (_a,b_) in \(\cup_{i=0}^kS_i\). Preference lists of vertices in _G_<sup>∗</sup> are the same as in _G_, except for unstable vertices in _G_, some of whom have acquired a new neighbor in _G_<sup>∗</sup>. For any unstable vertex _u_ with a new neighbor _v_ in _G_<sup>∗</sup>, the vertex _v_ is at the tail of _u_’s preference list, i.e., _v_ is _u_’s least preferred neighbor in _G_<sup>∗</sup>.

**The Matching** _M_<sup>∗</sup>**.** Let _M_ be any popular matching in _G_. Lemma 1 tells us that for any edge \((a,b)\in\cup_{i=1}^kS_i\), either both _a_ and _b_ are matched in _M_ or neither is matched in _M_. This is also true for \((a,b)\in S_0\), since in this case both _a_ and _b_ are left unmatched in _M_. Define _M_<sup>∗</sup> as follows:

\(M^*=M\cup\{(a,b)\in\cup_{i=0}^kS_i\text{such that}a\text{and}b\text{are unmatched in}M\}.\)

It is easy to see that _M_<sup>∗</sup> is a _B_-perfect matching in _G_<sup>∗</sup>. Let _U_<sup>∗</sup> be the set of unstable vertices in _G_<sup>∗</sup>. So \(U^*\subseteq A\), in fact, \(U^*\subseteq U_A\), where _U<sub>A</sub>_ is the set of unstable vertices in _G_ that are in _A_.

