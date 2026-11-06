Altogether, the bound is \(\tilde{O}\left(\alpha(V)^{3/2}\right)\), as required.

In order to obtain data structure 2 of Theorem 3.1, we do not store the separators from step 6 as they were only used as witnesses. However, we do maintain the list of \(\tilde{O}(\alpha(V))\) node pairs we directly called Max-Flow for in step 6, together with the corresponding answers. We further give up storing the separators from step 2, notwithstanding the immediate consequence that for a cut \(\left(S_{p,f(u)},C_{p,f(u)},S_{f(u),p}\right)\) and a node pair _u,v_ we cannot anymore immediately distinguish between the case where _u_ and _v_ are separated in the cut, i.e., \(v\in S_{p,f(u)}\), and the case where \(v\in C_{p,f(u)}\). However, we may assume that a direct Max-Flow(_u,v_) call was not made in step 6b (as we store the list of direct Max-Flow queries), and so it must be that this \(v\in C_{p,f(u)}\) case covered by step 6b, and also the case where \(v\in S_{f(u),p}\) in final instances covered by step 6a, happened in at most _k_-1 repetitions each. As established in the correctness proof, at least 20_k_log<sup>3</sup>_n_ repetitions are not invalid for _u,v_ at the end of the recursion, and so at least \(20k\mathrm{log}^3n-2(k-1)\ge 18k\mathrm{log}^3n\) recursion trees must have the optimal answer for _u,v_. To find the optimal answer, simply take the majority among the smallest 19_k_log<sup>3</sup>_n_ answers, i.e., in repetitions where _u_ and _v_ do not belong together in final instances, concluding a query time of \(\tilde{O}(k)\) (as discussed before, node pairs in \[_k,_2_k_\] stages with \(k\ge\tilde{\Omega}\left(\sqrt{\alpha(V)}\right)\) can be answered faster, in \(\tilde{O}(1)\) time). The total space for data structure 2 is thus at most \(\tilde{O}\left(\alpha(V)\right)\), as required.

## 4 Conditional Lower Bound for Undirected Graphs with Unit Node- Capacities

Here, we show that the _n_<sup>3-_o_(1)</sup> conditional lower bound \[AKT20b\] for All-Pairs Max-Flow on undirected graphs with general node-capacities can be extended, using the source-sink isolating gadget presented in \[HLSW23\], to prove a conditional lower bound for undirected graphs with unit node- capacities.

**Lemma 4.1.** _3OV over vector sets of size n and dimension d can be reduced to All-Pairs Max-Flow on undirected graphs with_ \(\Theta(nd)\) _nodes,_ \(\Theta(n^2d^2)\) _edges, and unit node-capacities._

To see how Theorem 1.4 follows from Lemma 4.1, one can simply add isolated nodes and recall that the output is always of size \(\Theta(n^2)\).

_Proof of Lemma 4.1._ We generally follow the reduction from 3OV presented in \[AKT20b\], with minor modifications. As an intermediate construction in this reduction, a layered graph with undirected edges and a few directed edges was created. The following lemma describes the properties of this reduction, where ST-Max-Flow is a restricted version of All-Pairs Max-Flow focusing only on Max-Flow(_s,t_) with \(s\in S\) and \(t\in T\), used here for convenience.

**Lemma 4.2** (From the proof of Lemma 4.2 in \[AKT20b\])**.** _3OV over vector sets of size n and dimension d can be reduced to ST-Max-Flow with_ |_S_|=|_T_|=_n in graphs G with_ \(\Theta(n\cdot d)\) _nodes,_ \(\Theta(n\cdot d)\) _edges, and with the following properties._

• _all nodes in_ \(S\cup T\) _have capacity_ 1_, and also_ \(\sum_{u\in V(G)}c(u)=O(nd)\).<tbc>

• _each edge_ \(uv\in E(G)\) _satisfies_ \(c(u)\cdot c(v)\le nd^2\).<tbc>

• _the edges adjacent to S are all directed away from S, and the edges adjacent to T are all directed towards T. The rest of the edges in G are undirected._<tbc>

