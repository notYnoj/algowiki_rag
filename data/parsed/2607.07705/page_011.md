**Lemma 2.** _Let_ I=(_G,_**w**_,k_) _be an instance of_ \(MAS/MaxST(\mathbb{Q}_{\ge 1})\)_. If_ \(\mathbf{w}(A)\ge 3k\)_, then_ I _is a yes-instance. The solution to_ I _can be constructed in polynomial time._

_Proof._ We first apply Proposition 1 to the maximum spanning tree _T_ of (_G,_**w**). Let \(\mathcal{P}=(V(T),\unknown)\) be the poset defined as in the proposition statement, that is, \(u\unknown v\) if and only if there is a directed path in _T_ from _u_ to _v_. Then, in polynomial time, we can construct linear extensions \(\unknown_1\), \(\unknown_2\) and \(\unknown_3\) of P such that for each \(x,y\in V(T)\), \(x\unknown y\) if and only if \(x\unknown_iy\) for each \(i\in\{1,2,3\}\).

We now provide a partition \(A_1\sqcup A_2\sqcup A_3\) of _A_ such that _T+A<sub>i</sub>_ is acyclic for each \(i\in\{1,2,3\}\). For each edge \(uv\in A\), we determine its part as follows. By the definition of allowed edges, _T+uv_ does not contain directed cycles. In particular, this means that there is no directed path from _v_ to _u_ in _T_. Hence, \(v\unknown u\) does not hold. Then, by the definition of \((\unknown_1,\unknown_2,\unknown_3)\), we know that _u_ must precede _v_ in one of these total orders. We choose an arbitrary \(\unknown_i\) with this property and add _uv_ to the set _A<sub>i</sub>_. Note that the construction of _A_<sub>1</sub>, _A_<sub>2</sub> and _A_<sub>3</sub> also takes polynomial time.

We claim that for each \(i\in\{1,2,3\}\), all edges from \(E(T)\cup A_i\) go from smaller to larger elements with respect to \(\unknown_i\). For the edges from _A<sub>i</sub>_, this property is ensured by the definition of _A<sub>i</sub>_. Now consider an edge \(uv\in E(T)\). This edge gives a trivial path from _u_ to _v_ in _T_, and thus we have \(u\unknown v\), implying \(u\unknown_iv\). Because _uv_ is a tree edge, it cannot be a loop, and hence _u_ strictly precedes _v_ in \(\unknown_i\).

It follows that for each \(i\in\{1,2,3\}\), the graph _T+A<sub>i</sub>_ is acyclic. Let _A<sub>j</sub>_ be a set of maximum weight among _A_<sub>1</sub>, _A_<sub>2</sub> and _A_<sub>3</sub>. If \(\mathbf{w}(A)\ge 3k\), then \(\mathbf{w}(A_j)\ge k\), and hence \(\mathbf{w}(T+A_j)\ge\mathbf{w}(T)+k\). Therefore, _T+A<sub>j</sub>_ is a solution to I, and it can be constructed in polynomial time.

It is an interesting open problem to determine whether the bound in Lemma 2 is tight or can be improved.

## 4.2 Decomposing MST into paths

Our next block is a polynomial-time algorithm that either constructs a solution, or obtains an equivalent instance of \(MAS/MaxST(\mathbb{Z}_{\ge 1})\) via edge contractions. In the resulting instance, all but at most O(_k_+|_A_|) vertices have exactly one ingoing and exactly one outgoing edge.

**Lemma 3.** _There an algorithm that, given an instance_ I=(_G,_**w**_,k_) _of_ \(MAS/MaxST(\mathbb{Z}_{\ge 1})\)_, works in polynomial time and either_

• _outputs a solution to_ I_, or_<tbc>

• _outputs an equivalent instance_ \(\mathcal{I}'=(G',\mathbf{w}',k)\) _of_ \(MAS/MaxST(\mathbb{Z}_{\ge 1})\) _such that in_ \(MaxST(G',\mathbf{w}')\) _all but at most_ \(\mathcal{O}(k+|A'|)\) _vertices have both in- and out-degree one, where_ \(A'=A(G',\mathbf{w}')\).

_Additionally, a solution to_ \(\mathcal{I}'\) _can be transformed into a solution to_ I _in polynomial time._

_Proof._ We call a tree edge \(e\in E(T)\) _profitable_ if **p**(_e)\>_0. Otherwise we say that it’s _unprofitable_. A leaf vertex in _T_ inherits this classification from its unique incident _tree_ edge. We provide two reduction rules which contract unprofitable edges. These rules are designed in such a way that if they are not applicable, but _T_ has too many vertices whose in-degree or out-degree differs from one, then I is a yes-instance. We start with a couple of claims that are used in both reduction rules.

**Claim 1.** _Consider the graph G/e, where_ \(e\in E(T)\) _is a tree edge. Then:_

1. _Weight of_ MaxST _in G/e is_ **w**(_T_)-**w**(_e)._<tbc>

