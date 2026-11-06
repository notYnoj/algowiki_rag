• _reports that_ I _is a no-instance, if_ I _is a no-instance, or_<tbc>

• _outputs a solution to_ I_, if there is a solution_ \(G'\) _to_ I _such that_ \(E(T)\backslash E(G')=S\)_, or_<tbc>

• _outputs any of the two outcomes above, otherwise._

When solving an instance (_G,_**w**_,k_) of MAS/MaxST, we can always look at the problem from a different perspective. Instead of finding an acyclic subgraph of _G_ of weight at least **w**(_T_)+_k_, we can equivalently seek an edge set of weight at most **w**(_G_)-**w**(_T_)-_k_ whose removal makes _G_ acyclic. This dual problem is called Weighted Directed Feedback Arc Set.

Formally, an instance of WDFAS is described by a tuple (_G,_**w**_,k,W_), where _G_ is a directed graph with positive integer weights on edges given by the function \(\mathbf{w}:E(G)\rightarrow\mathbb{Z}_{\ge 1}\), and our goal is to find a set \(S\subseteq E(G)\) of cardinality at most _k_ and weight at most _W_ such that _G-S_ is acyclic. In their recent work on flow augmentation in directed graphs \[KKPW25\], Kim, Kratsch, Pilipczuk and Wahlström have shown that WDFAS admits an FPT algorithm when parameterized by _k_.

**Proposition 2** (\[KKPW25\], Theorem 4.3)**.** _WDFAS can be solved in time_ 2<sup>O(_k_<sup>8</sup>log_k_)</sup>_n_<sup>O(1)</sup>.

We employ this result in our proof of Lemma 5. The core idea is that given a fixed set of removed tree edges _S_, we can reduce our problem to a WDFAS on the graph _T-S_+Inv(_S_)+_A_. Moreover, we can bound _W_ and _k_ by **w**(_A_) as otherwise the subgraph _T-S_+Inv(_S_) already has a sufficiently large weight. We now move on to the formal proof of the lemma.

_Proof of Lemma 5._ Consider a tree edge set _S_. Denote _X_:=_T-S+A_+Inv(_S_) and let \(k':=\mathbf{w}(X)-\mathbf{w}(T)-k\). Note that if there exists a solution \(G'\) to I such that \(E(T)\backslash E(G')=S\), then we can remove a set of edges from _X_ of total weight and cardinality at most \(k'\) to obtain an acyclic graph: since \(G'\) is a solution, it is acyclic, and Observation 2 guarantees that \(G'\subseteq X\). Moreover, \(\mathbf{w}(G')\ge\mathbf{w}(T)+k\). Consequently, \(\mathbf{w}(X)-\mathbf{w}(G')\le\mathbf{w}(X)-\mathbf{w}(T)-k=k'\). Additionally, observe that since all weights are at least one, from \(\mathbf{w}(X)-\mathbf{w}(G')\le k'\) it also follows that \(|E(X\backslash G')|\le k'\).

Conversely, if \(X'\) is an acyclic subgraph of _X_ obtained by removing edges of total weight at most \(k'\), then \(X'\) is also a valid solution for I, because \(\mathbf{w}(X')\ge\mathbf{w}(X)-k'=\mathbf{w}(X)-(\mathbf{w}(X)-\mathbf{w}(T)-k)=\mathbf{w}(T)+k\).

Therefore, we obtain the algorithm required in the lemma statement as follows: solve the WDFAS problem for the instance \(\mathcal{I}':=(X,\mathbf{w}',k',k')\), where the weight bound and the cardinality bound are both set to \(k'\), and \(\mathbf{w}'\) is the restriction of **w** to _X_. If \(X'\) is a solution for \(\mathcal{I}'\), then it is also a valid solution for I, and we can output \(X'\). Otherwise, we report that I is a no-instance.

From the discussion above, if I is a no-instance, we correctly report it as such, because any solution produced by the algorithm would be feasible by construction. Moreover, if there exists a solution \(G'\) for I such that \(E(T)\backslash E(G')=S\), then there exists a solution for \(\mathcal{I}'\), and our algorithm will output it as a solution for I. Thus, the described algorithm satisfies all the required properties.

A potential concern is that the value of \(k'\) may be very large. To address this, we distinguish two cases. If \(k'\ge\mathbf{w}(A)\), then we can immediately produce a solution for \(\mathcal{I}'\): consider the subgraph \(X':=T-S+Inv(S)\). It is acyclic by Lemma 1 and \(\mathbf{w}(X')\ge\mathbf{w}(X)-\mathbf{w}(A)\ge\mathbf{w}(X)-k'\). Otherwise, we have \(k'<\mathbf{w}(A)\). By Proposition 2, in this case the instance \(\mathcal{I}'\) can be solved in time

\(2^{(k^\prime)^8logk^\prime}\cdot n^{\mathcal{O}(1)}\subseteq 2^{\mathbf{w}(A)^8log\mathbf{w}(A)}\cdot n^{\mathcal{O}(1)}\)

This completes the proof.

