Recall that, by the definition of \(S'\), each _v<sub>j</sub>_ is either a sink or a source in _T_. The argument above guarantees that their types must alternate: i.e., if _v<sub>j</sub>_ is a sink, then _v_<sub>_j_+1</sub> must be a source, and vice versa. Since Reduction Rule 2 is not applicable, for each _j_ with \(0\le j\le p_i-3\) there must be a profitable edge on the subsegment of _P<sub>i</sub>_ between _v<sub>j</sub>_ and _v_<sub>_j_+3</sub>. Otherwise, the four vertices _v<sub>j</sub>,v_<sub>_j_+1</sub>_,v_<sub>_j_+2</sub>_,v_<sub>_j_+3</sub> (or the reverse order _v_<sub>_j_+3</sub>_,v_<sub>_j_+2</sub>_,v_<sub>_j_+1</sub>_,v<sub>j</sub>_) would satisfy the conditions of this reduction rule. Applying this argument to each block of four vertices of the form _v_<sub>4_x_+1</sub>_,v_<sub>4_x_+2</sub>_,v_<sub>4_x_+3</sub>_,v_<sub>4_x_+4</sub>, we obtain \(\lfloor p_i/4\rfloor\) profitable edges on the path _P<sub>i</sub>_. Moreover, each pair _v<sub>j</sub>_, _v_<sub>_j_+1</sub> satisfies the conditions of Claim 5. Hence, an edge \(e\in P_{i,j}\) cannot share an inverse edge with any \(e'\in(E(T)\backslash P_{i,j})\).

Consequently, we can construct a set of profitable tree edges _R_:={_e_<sub>1</sub>_,...,e<sub>q</sub>_} such that \(q=\sum_{i=1}^t\lfloor p_i/4\rfloor\) and \(\mathrm{Inv}(e_i)\cap\mathrm{Inv}(e_j)=\emptyset\). Note that if \(q\ge k\), then _X_:=_T-R_+Inv(_R_) is a solution for I: indeed, it is acyclic by Lemma 1, and by Observation 4, we have

\(\mathbf{w}(X)=\mathbf{w}(T)+\mathbf{p}(R)=\mathbf{w}(T)+\sum_{i=1}^q\mathbf{p}(e_i)\ge\mathbf{w}(T)+q\ge\mathbf{w}(T)+k\)

If, on the other hand, _q\<k_, then we can conclude that \(|S'|=\sum_{i=1}^tp_i\le\sum_{i=1}^t(4\lfloor p_i/4\rfloor+3)=3t+4q\le 3\cdot 4(|A|+k)+4k=12|A|+16k\). \(\lrcorner\)

Let \(\mathcal{I}':=(G',\mathbf{w}',k)\) be the equivalent instance obtained by exhaustive applications of Reduction Rule 1 and Reduction Rule 2. Recall that all vertices outside both _S_ and \(S'\) have one incoming tree edge and one outgoing tree edge. Together with Claim 4 and Claim 7, this implies that either \(\mathcal{I}'\) is a yes-instance or all but at most O(_k_+|_A_|) vertices in \(\mathrm{MaxST}(G',\mathbf{w}')\) have in-degree one and out-degree one. Moreover, Claim 1, provide a way to transform a solution for \(\mathcal{I}'\) into a solution for I.

Lemma 3 does not provide any upper bound on the size of \(G'\) in \(\mathcal{I}'\). Nevertheless, the MaxST of \((G',\mathbf{w}')\) exhibits a simple structure, since it consists of O(_k_+|_A_|) pivotal vertices connected by pairwise-disjoint directed paths.

## 4.3 Greedy-like approach to remaining profits

Our third building block relies fundamentally on remaining profits and directed paths in MaxST. Somewhat surprisingly, there is a strategy that provides a limited number of choices of removing a single edge from _E(T_) iteratively, depending on its current remaining profit, given that _T_ is partitioned into a limited number of directed paths (guaranteed by Lemma 3).

This strategy works even if _A_ is not empty, and it highly relies on that _E(T_) is ordered in a topological manner. To describe it, we have to introduce the notion of _proper path covers_.

**Definition 6** (Proper path cover)**.** A _proper path cover_ P of _T_=MaxST(_G,_**w**) is a sequence _P_<sub>1</sub>_,P_<sub>2</sub>_,...,P<sub>t</sub>_ of directed paths of _T_, such that

• each edge \(e\in E(T)\) belongs to exactly one path in _T_, and<tbc>

• each internal vertex of each _P<sub>i</sub>_ has in-degree and out-degree one in _T_, and<tbc>

• if \(v\in V(G)\) is incident to an allowed edge \(a\in A\), then _v_ is not an internal vertex in any _P<sub>i</sub>_, and<tbc>

