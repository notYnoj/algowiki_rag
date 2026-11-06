Both types of operations have the same unit cost. An additional unit cost is charged for performing each search. The cost of an algorithm A for executing _X_, denoted `cost`<sub>A</sub>(_X_), is thus the total number of pointer moves and rotations plus an additive term _m_. An algorithm is _offline_ if it knows the entire sequence _X_ in advance, and _online_ if it receives _x<sub>i</sub>_ only after the (_i_-1)-th search has finished.

In both the static and the dynamic case we only account for operations _in the model_. Algorithms that are to be considered efficient should, however, also spend polynomial time _outside the model_ (i.e. for deciding which rotations and pointer moves to perform).<sup>1</sup> In case of our generalization of Splay, the time spent outside the model is _linear_ in the model cost.

## 3. Almost optimal search trees on trees

Let _S_ be a tree on _n_ nodes and consider a search sequence \(X=(x_1,\dots,x_m)\in V(S)^m\) with the function \(p:V(S)\rightarrow\mathbb{N}\) denoting the frequencies of searches, so that each node \(x\in V(S)\) appears _p(x_) times in _X_. We want to find a search tree _T_ on _S_ in which _X_ is served with the smallest possible cost, i.e. to minimize

\(\mathtt{cost}_T(X)=\sum_{i=1}^m\mathtt{depth}_T(x_i)=\sum_{x\in V(S)}p(x)\cdot\mathtt{depth}_T(x).\)

In this section we show how to find, in polynomial time, a search tree \(T'\) on _S_, whose cost is \(\mathtt{cost}_{T^\prime}(X)\le(1+\varepsilon)\cdot\mathtt{cost}_T(X)\), for arbitrarily small \(\varepsilon>0\), i.e. we give a polynomial-time approximation scheme (PTAS) for the optimal STT problem. The result is based on _k_-cut trees, a generalization of Steiner-closed trees that we introduce (Steiner-closed trees are the special case _k_=2). Before presenting the algorithm, we need some definitions.

### Cuts and boundaries.

The _cut_ in _S_ of a nonempty set of nodes \(A\subseteq V(S)\), denoted `cut`_<sub>S</sub>(A_) or simply `cut`(_A_) is the set of (directed) pairs of nodes (_u,v_), where \(u\in V(S)\backslash A\), and \(v\in A\), and {_u,v_} is an edge of _S_. In words, the cut is the set of edges connecting the remainder of the tree _S_ to _A_, indicating the direction. Observe that \(\mathtt{cut}(A)=\emptyset\) if and only if _A=V(S_). Moreover, `cut`(_A_) uniquely determines the set _A_, and given `cut`(_A_), we can find _A_ through a linear time traversal of _S_.

The _boundary_ \(\delta_S(A)\) or simply \(\delta(A)\) is the set of nodes outside _A_ that define the cut. More precisely, \(u\in\delta_S(A)\) if and only if \((u,v)\in\mathtt{cut}_S(A)\), for some \(v\in A\). Observe that if _S_\[_A_\] is connected (i.e. a subtree), then \(|\delta_S(A)|=|\mathtt{cut}_S(A)|\). We call this quantity the _boundary size_ of _A_. To simplify notation, for subtrees _H_ of _S_ we let \(\delta(H)\) denote \(\delta(V(H))\).

**Definition 5** (_k_-cut tree)**.** For \(k\ge 1\), an STT _T_ on _S_ is a _k_-cut tree, if the boundary size \(|\delta_S(T_x)|\) is at most _k_ for all nodes \(x\in V(S)\).

It is easy to verify that 1-cut STTs are exactly those obtained by rooting _S_ at some vertex (as in Observation 4). A more involved argument (§4.2) shows that 2-cut trees are<tbc>

<sup>1</sup>Whether unbounded computation outside the model can improve the competitiveness of online algorithms is an intriguing theoretical question for both BSTs and STTs.

