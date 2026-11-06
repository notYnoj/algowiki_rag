Finally, let us introduce you to Figure 14 and Figure 15 as two complete examples of how a target _a_-nice PMC \(\Omega\) can be reached starting from a non _a_-nice one. On successive PMCs, the connected component containing _a_ (_i.e._ set \(C_G(a,\Omega)\)) is highlighted in green: we can see it melting step by step. In Figure 14, the reader can notice the reasoning-based reading path from top left (target PMC \(\Omega\)) to bottom right (some not _a_-nice PMC) and the algorithm- based reading path - representing a possible traversal for PMC-BFS - from the bottom right to the top left. The reasoning-based reading path follows the preimage search until a non _a_-nice PMC is found. Conversely, the algorithm-based reading path provide an overview of the functioning of PMC-BFS which leads to discover the target PMC \(\Omega\). Figure 15 provides an alternative smaller path to reach the target PMC \(\Omega\).

## 4.4 Analysis of the algorithm

We are now ready to provide the analysis of our enumeration algorithm PMC-Traversal (Algorithm 3). We show that no PMC of _G_ is forgotten in the enumeration process. Also, we prove that it is executed in overall output-linear time.

**Theorem 1.** _Given a graph G with n_=|_V(G_)|_, one can compute the list of all PMCs of G in output-linear time_ \(\tilde{O}(|\Pi_G|)=O(n^4m|\Pi_G|)\).

_Proof._ Remember that PMC-Traversal follows the principle of BT-Enum with a modification of the fourth step. The goal of this fourth step is to list all the _a_-nice PMCs. By Corollary 3, PMC-BFS (Algorithm 2) finds all the _a_-nice PMCs if the starting queue of the BFS contains all PMCs which are not _a_-nice, already computed in the three first steps. According to Lemma 17, its time complexity is \(O(n^3m|\Pi_G|)\).

Since we use the same three first steps from BT-Enum (lines 8, 9 and 11 of Algorithm 3), all PMCs which are not _a_-nice (which contain _a_ or are PMCs of _G_\\{_a_}) are indeed found before executing PMC-BFS. We denote by _T(G_) the time complexity of PMC-Traversal for _G_. Combining the running time needed for each step, we obtain:

\(T(G)=T(G\backslash\{a\})+O(nm|\Pi_{G\backslash\{a\}}|)+O(nm|\Delta_G|)+O(n^3m|\Pi_G|))\)<br>
\(=T(G\backslash\{a\})+O(n^3m|\Pi_G|).\)

Indeed, there are less PMCs in _G_\\{_a_} than in _G_ (Lemma 11), and \(\Delta_G\le n|\Pi_G|\) from Section 1. Hence, there exists some positive constant \(K\ge 1\) such that \(T(G)\le T(G\backslash\{a\})+Kn^3m|\Pi_G|\).

We show by induction on _n_ that \(T(G)\le Kn^4m|\Pi_G|\). The base case (_G_ is a clique, line 4 of Algorithm 3) takes _O_(1) time and satisfies the previous inequality (if no, then _K_ could adjusted to a larger value but still constant). Assume, by induction hypothesis, that any subgraph _H_ of _G_ satisfies \(T(H)\le K\cdot|V(H)|^4\cdot|E(H)|\cdot|\Pi_H|\). As _G_\\{_a_} is a subgraph of _G_ and admits less PMCs, we get \(T(G\backslash\{a\})\le K(n-1)^4m|\Pi_G|\). Consequently,

\(T(G)\le K(n-1)^4m|\Pi_G|+Kn^3m|\Pi_G|=Km\left((n-1)^4+n^3\right)|\Pi_G|\le Kn^4m|\Pi_G|.\)

This concludes the proof since all the PMCs of the input graph are found by Algorithm 3 and its execution time is \(O(n^4m|\Pi_G|)\).

