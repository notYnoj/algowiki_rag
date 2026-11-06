It was shown that if an ST-Max-Flow algorithm could distinguish between the following two cases, then the input 3OV instance can be solved. In the first case, all pairs of nodes \(s\in S\) and \(t\in T\) satisfy Max-Flow_<sub>G</sub>(s,t_)=_nd_, implying that there exists no orthogonal triple in the 3OV instance, i.e. it is a "NO" instance. In the second case, there exists at least one pair of nodes \(s'\in S\) and \(t'\in T\) such that \(\text{Max-Flow}_G(s',t')=nd-1\), indicating the presence of an orthogonal triple in the 3OV instance, i.e. it is a "YES" instance. In the final construction, all edges must become undirected. To prevent flows from zigzagging through _S_, and similarly through _T_, all node- capacities are multiplied by 2_n_, except for nodes in _S_ and _T_. It was then proved that the number of zigzagging flow paths in every _st_-flow is at most \(|(S\cup T)\backslash\{s,t\}|\le 2(n-1)\). Therefore, these paths can be disregarded after the node-capacities are multiplied by 2_n_.

We will show that an alternative way to increasing the capacities in _G_ is to use the source-sink gadget. However, before doing so, we need to modify the graph so that it only has unit node- capacities. This can be easily done by replacing each node _u_ with _c(u_) copies of itself, and by then adding a complete biclique between the new copies of _u_ and the new copies of _v_ for each edge \(uv\in G\). The resulting graph is denoted by \(G'\).

The number of nodes in \(G'\) is clearly \(\sum_{u\in V(G)}c(u)=O(nd)\), and the number of edges in \(G'\) is \(\sum_{uv\in E(G)}c(u)\cdot c(v)\le O(nd\cdot nd^2)=O(n^2d^3)\) (in fact, a more careful analysis leads to a bound of _O(n_<sup>2</sup>_d_<sup>2</sup>)). Importantly, for every \(s\in S\) and \(t\in T\), every _st_-flow in _G_ naturally corresponds to an _st_-flow of the same value in \(G'\), and vice versa; to transform an _st_-flow in \(G'\) to an _st_-flow in _G_, simply contract nodes that correspond to the same node in _G_. Although the resulting flow may contain cycles, they can be disregarded.

Below is the source-sink isolating lemma, adapted to our notations.

**Lemma 4.3** (Lemma 3.2 in \[HLSW23\])**.** _Given an undirected graph R and two disjoint groups of vertices_ \(X,Y\subseteq V(R)\)_, there is a graph Q with_ \(V(Q)\cap V(R)=X\cup Y\) _such that for any_ \(x\in X,y\in Y\) _with_ \((x,y)\notin E(R)\),

\(\text{\textit{Max-Flow}}_{R\cup Q}(x,y)=\text{\textit{Max-Flow}}_{R_{xy}}(x,y)+|X|+|Y|,\)

_where_ \(R_{xy}=R\backslash((X\cup Y)\backslash\{x,y\})\)_. Such a graph P is called a source-sink isolating gadget and there is an algorithm that constructs Q with_ |_V(Q_)|=_O_(|_X_|+|_Y_|).

Constructing _Q_ can be easily done in linear time with respect to its size. We use Lemma 4.3, taking \(R=G'\), _X=S_ and _Y=T_. The lemma guarantees that \(\text{Max-Flow}_{G^\prime\cup Q}(s,t)=\text{Max-Flow}_{R_{st}}(s,t)+|S|+|T|\) for any \(s\in S\) and \(t\in T\). Therefore, we can determine whether there exists an orthogonal triple by checking whether \(\text{Max-Flow}_{G^\prime}(s,t)=nd+2n\) for all \(s\in S\) and \(t\in T\), or if there exists \(s'\in S\) and \(t'\in T\) such that \(\text{Max-Flow}_{G^\prime}(s',t')=nd-1+2n\).

The size of the graph remains asymptotically the same after adding the source-sink isolating gadget. Since All-Pairs Max-Flow is a more general problem than ST-Max-Flow, we can conclude Lemma 4.1.

## 5 Open Problems

After our work, many open problems on the fine-grained complexity of All-Pairs Max-Flow remain. Here are a few:

1. Can we break the _O(n_<sup>4</sup>) bound for any hard setting? With our new non-reducibility results, (non-combinatorial) subquartic algorithms seem more attainable.<tbc>

