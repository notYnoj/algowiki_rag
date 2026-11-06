Our work focuses on the weighted case. For unweighted graphs with capacity 1 on every edge, a max flow (assuming no unnecessary cycles) always uses at most _O(n_<sup>1.5</sup>) edges. Thus they can be trivially stored in that much space. It’s interesting to see that now the same upper bound holds for the weighted case, despite graph with arbitrary capacities using up to _O(n_<sup>2</sup>) edges.

**Theorem A.3.** _Given a graph G_=(_V,E_) _with_ |_V_|=_n and unit-capacity, then any size F st-max flow (after removing cycles) uses at most_ \(2n\sqrt{F}\) _edges._

_In particular, since_ \(F\le n\)_, then we get_ 2_n_<sup>1.5</sup> _edges._

_Proof._ After removing cycles from the max-flow, the edges used by the flow form a directed acyclic graph (DAG). From now, we consider the graph that consists of only the flow-edges. Since that is a DAG, consider the topological order.

Let _g_ be some parameter. We split the sequence of ordered vertices into _g_ groups of _n/g_ vertices. Let \(V_1,V_2,\cdots,V_g\) denote those _n_ groups and each |_V<sub>i</sub>_|=_n/g_ for all \(i\in[g]\).

If we consider all the max-flow edges, there are now 2 types:

• Type I: edges within a single group,<tbc>

• Type II: edges that go from one group to another group.

First we will explain how to compute the number of Type I edges. Within a single group there are at most (_n/g_)<sup>2</sup> edges, and since there are _g_ groups, we have

\((n/g)^2\cdot g=n^2/g\)

edges of that Type I in total.

For any set \(W\subset V\) , we use the \(\delta(W)\) to denote the size of cut between _W_ and _V_\\_W_.

Now, let us consider edges of type II that go across different groups. For any such edge _e_, assume it leaves some group _V<sub>k</sub>_, then the edge is cut by the cut \(W_k\subset V\) where<tbc>

\(W_k:=\bigcup_{i=1}^kV_i,\text{and}V\backslash W_k=\bigcup_{i=k+1}^gV_i,\)

<tbc>because all flow-edges are oriented left to right by topological order assumption. Thus the number of type II edges is bounded by the sum of sizes of all such cuts, i.e.,<tbc>

\(\sum_{k=1}^g\delta(W_k).\)

<tbc>Since the graph is a DAG and _W<sub>k</sub>_ contains the first _kn/g_ vertices of the topological order, the cut has only outgoing edges, in particular, \(\delta(W_k)=F\) the size of the flow. Thus

\(\sum_{k=1}^g\delta(W_k)=g\cdot F\)

So there are at most _gF_ many edges of type II.

Overall, if count two types of edges together, there are<tbc>

\(n^2/g+g\cdot F.\)

<tbc>To minimize the above quantity, we choose \(g=n/\sqrt{F}\). Thus, we obtain

\(2n\sqrt{F}\)

By unit-capacity we have \(F\le n\), implying at most 2_n_<sup>1.5</sup> edges in the max-flow.

