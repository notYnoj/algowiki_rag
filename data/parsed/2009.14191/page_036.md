<tbc>containing any of these agents, it follows that \(b_{r+1}^{i,j}\) prefers \(\{z_1^{i,j},b_r^{j,i}\}\) to \(M(b_{r+1}^{i,j})\). Every 2-set which \(b_r^{i,j}\) prefers to \(\{z_1^{i,j},b_{r+1}^{j,i}\}\) contains an agent outside _B<sup>i,j</sup>_, an agent from _X_, agent \(z_1^{i,j}\), or two agents from \(\{b_q^{i,j},b_q^{j,i},c_q^{i,j}\}\). From all these agents, \(b_r^{i,j}\) can only be matched to \(c_r^{i,j}\). It follows that \(b_r^{i,j}\) prefers \(\{z_1^{i,j},b_{r+1}^{i,j}\}\) to \(M(b_r^{i,j})\). Thus, _t_ blocks _M_, a contradiction to the stability of _M_.

If _s\<r_, then symmetric arguments show that \(\{z_1^{i,j},b_s^{i,j},b_{s+1}^{j,i}\}\) is a blocking 3-set for _M_.

It now easily follows that _G_ contains a multicolored clique.

**Lemma 4.26.** _If_ \(\mathcal{I}'\) _admits a stable matching, then G admits a clique of size k._

_Proof._ By Lemma 4.23, every vertex-selection gadget selects a vertex, and by Lemma 4.25, these _k_ vertices form a clique.

Theorem 4.27 now directly follows from Lemmas 4.16, 4.22 and 4.26.

**Theorem 4.27.** 3-DSR _parameterized by_ \(\lambda(\mathcal{I})\) _is_ W\[1\]_-hard, where_ \(\lambda(\mathcal{I})\) _denotes the minimum number of agents such that the preferences of the instance arising through the deletion of these agents are derived from a strict order._

_Proof._ The reduction clearly runs in polynomial time. By Lemmas 4.22 and 4.26 it is correct. By Lemma 4.16, we have that \(\lambda(\mathcal{I})=O(k^2)\). Thus, we have a parameterized reduction from Multicolored Clique parameterized by solution size _k_ to 3-DSR parameterized by \(\lambda(\mathcal{I})\). Since Multicolored Clique parameterized by solution size _k_ is W\[1\]-hard \[15, 42\], 3-DSR is W\[1\]-hard parameterized by \(\lambda(\mathcal{I})\).

We have shown that 3DSR-Poset parameterized by \(\lambda\) is W\[1\]-hard. A natural question is whether there is an XP-algorithm for 3DSR-Poset.

Next, we drop the assumption that preferences are complete (i.e., every agent is allowed to be matched to any set of _d_-1 other agents), but instead require that the master poset is a strict order.

## 4.4 Incomplete preferences derived from a strictly ordered master poset

Let MDSRI be the MDSR problem with incomplete preference lists, i.e., \(\succ_a\) is not a strict order of \(\genfrac(){pt}{2}{A\backslash\{a\}}{d-1}\), but a strict order of a subset \(X_a\subseteq\genfrac(){pt}{2}{A\backslash\{a\}}{d-1}\) for each \(a\in A\). In this case, we call a _d_-set _t acceptable_ if \(t\backslash\{a\}\in X_a\) for every \(a\in t\), and define a _matching M_ to be a set of disjoint, acceptable _d_-sets.

Similarly, MDSRI-ML is the MDSRI problem restricted to instances where the preferences are derived from a strict order of agents (which we call _master poset_), and \(\ell\)-DSRI is MDSRI for the special case \(d=\ell\). Here, preferences of an agent _a_ are derived from the master poset \(\succ_\text{ML}\) if they are the restriction to _X<sub>a</sub>_ of a preference list derived from \(\succ_\text{ML}\).

MDSRI
Input:
A set A of agents together with preference lists Xa over Xa for a subset Xa -
for each a A.
Task:
Decide whether a stable matching exists.

