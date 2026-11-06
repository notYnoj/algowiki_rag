<tbc>rerouting operations, _f<sub>st</sub>_ remains valid after this operation, meaning that it (1) respects the edge directions, and (2) adheres to the node capacities and flow conservation constraints. This is because while \(u_{j+1}\in P_{out}\) receives additional flow of _f<sub>st</sub>(e<sub>min</sub>_) from its predecessor \(u_j\in P_{in}\), it also receives less flow by the exact same amount from its successor \(u_{j+2}\in P_{in}\). Furthermore, after the operation, the flow shipped through _e<sub>min</sub>_ in _f<sub>st</sub>_ becomes zero, and therefore _e<sub>min</sub>_ does not exist in _f<sub>st</sub>_ anymore, and _C_ is no longer an anti-directed closed walk there.

Finally, we demonstrate that when the operation can no longer be performed in _f<sub>st</sub>_, i.e., no more anti-directed closed walks exist in _f<sub>st</sub>_, then the resulting _st_-flow \(f'_{st}\) satisfies \(\text{\textbf{volume}}(f'_{st})\le 2n\). Since each operation reduces **volume**(_f<sub>st</sub>_) by at least 1, this must occur at some point. To begin with, we consider the standard reduction of \(f'_{st}\) to a bipartite graph \(G_{1,2}=(V_1\cup V_2,E_{1,2})\). _V_<sub>1</sub> and _V_<sub>2</sub> are two copies of \(V(f'_{st})\), and there is an edge in _E_<sub>1,2</sub> from \(u_1\in V_1\) to \(v_2\in V_2\) iff the edge (_u,v_) exists in \(f'_{st}\). Note that any cycle in the undirected graph underlying _G_<sub>1,2</sub> corresponds to an anti-directed closed walk in \(f'_{st}\). Since no more anti-directed closed walks exist in \(f'_{st}\), we conclude that the undirected graph underlying _G_<sub>1,2</sub> is a forest, and therefore, \(\text{\textbf{volume}}(f'_{st})\le|E_{1,2}|\le 2|V(f'_{st})|\le 2n\), as required by Lemma 2.5.

Below, we sketch an alternative proof that uses linear programming \[Che24\]. First, we write Max-Flow as a linear program, as usual, but adjusted to vertex capacities.

\(\text{maximize}\sum_{e\in\delta^+(s)}f(e)-\sum_{e\in\delta^-(s)}f(e)\text{subject to}\sum_{e\in\delta^-(v)}f(e)=\sum_{e\in\delta^+(v)}f(e),\forall v\in V\backslash\{s,t\}\sum_{e\in\delta^-(v)}f(e)\le c(v),\forall v\in V\backslash\{s,t\}f(e)\ge 0,\forall e\in E\)

In the above, \(\delta^-(v)\) is the set of incoming edges to _v_, and \(\delta^+(v)\) is the set of outgoing edges from _v_. Note that there are _m_ variables, _n_-2 flow conservation constraints and _n_-2 node-capacity constraints (since _s_ and _t_ do not have capacity constraints), and _m_ non-negativity constraints. From standard polyhedral theory (see the proof of Proposition 2.4 in \[CK04\], as well as \[Raj90\]), the linear program above admits an optimal solution with as many tight-constraints as variables, namely _m_. Since the total number of nontrivial constraints is 2_n_-4, there exists an optimal solution with at most this many non-zero variables.

## 2.2 Nondeterministic Algorithms in Various Settings

Finally, we will use Theorem 2.1 to show nondeterministic algorithms with time tailored to each setting; Theorems 1.3, 1.5, 1.6 will immediately follow from Lemmas 2.7, 2.8, 2.9, respectively, by applying Theorem 1.10.

**Lemma 2.7.** (Undirected graphs with unit node-capacities.) _The nondeterministic time complexity of Min-Cut data structure on undirected graphs with unit node-capacities is_ \(\tilde{t}_p(m)=O\left(n^{\omega(\mathrm{log}_nm,1,1)}\right)\) _with_ \(\tilde{t}_{mc}=O(1)\).

Assuming \(\omega=2\), the time becomes \(\tilde{t}_p(m)=\tilde{O}(mn)\).

_Proof of Lemma 2.7._ By combining Theorem 2.1 with the flow bound in Lemma 2.3 and our Las Vegas algorithm in Theorem 1.1 which has \(t_{pq}(m)=\tilde{O}(m),t_{po}=\tilde{O}(mn)\), and \(t_{mc}=\tilde{O}(1)\), we get a nondeterministic time of \(\tilde{t}_p(m)=O\left(n^{\omega(\mathrm{log}_nm,1,1)}\right)\) with \(\tilde{t}_{mc}=\tilde{O}(1)\), as required by lemma 2.7.

