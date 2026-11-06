## 3.3 Correctness Analysis

To present the correctness more accurately and compactly, we introduce several notations on the "shortest path tree". Due to the uniqueness of shortest paths, the shortest path tree _T_ rooted at the source _s_ can be constructed unambiguously. Define _T(u_) as the subtree rooted at _u_ according to \(d(\cdot)\). An immediate observation is that _the shortest path to v passes through u if and only if v is in the subtree rooted at u_.

For a vertex set _S_, define \(T(S)=\bigcup_{v\in S}T(v)\), namely the union of the subtrees of _T(s_) rooted at vertices in _S_, or equivalently, the set of vertices whose shortest paths pass through some vertex in _S_. For a set of vertices \(S\subseteq V\) , denote \(S^*=\{v\in S:v\text{is complete}\}\). Then \(T(S^*)=\bigcup_{v\in S^*}T(v)\) is the union of subtrees of _T(s_) rooted at _S_<sup>∗</sup>, or the set of vertices whose shortest paths pass through some complete vertex in _S_. Obviously, \(T(S^*)\subseteq T(S)\). Note that _T(S_<sup>∗</sup>) is sensitive to the progress of the algorithm while _T(S_) is a fixed set. Another observation is that, a complete vertex would remain complete, so _S_<sup>∗</sup> and _T(S_<sup>∗</sup>) never lose a member.

For a bound _B_, denote \(T_{<B}(S)=\{v\in T(S):d(v)<B\}\). Also note that _T<sub>\<B</sub>(S_) coincides with \(\widetilde{U}\) mentioned above. For an interval \[_b,B_), denote \(T_{[b,B)}(S)=\{v\in T(S):d(v)\in[b,B)\}\).

**Lemma 3.6** (Pull Minimum)**.** _Suppose every incomplete vertex v with d(v)\<B is in T(S_<sup>∗</sup>)_. Suppose we split S into_ \(X=\{x\in S:\widehat{d}[x]<\mathcal{B}\}\) _and_ \(Y=\{x\in S:\widehat{d}[x]\ge\mathcal{B}\}\) _for some_ B_\<B. Then every incomplete vertex v with d(v)\<_B _is in T(X_<sup>∗</sup>)_. Moreover, for any_ \(\mathcal{B}'<\mathcal{B}\), \(T_{<\mathcal{B}^\prime}(S)=T_{<\mathcal{B}^\prime}(X)\).

_Proof._ For any incomplete vertex _v_ with _d(v)\<_B, as B_\<B_, by definition, \(v\in T(u)\) for some complete vertex \(u\in S\). Therefore \(\widehat{d}[u]=d(u)\le d(v)<\mathcal{B}\), so \(u\in X\) and thus \(v\in T(X^*)\).

For the second statement, it is clear that \(T_{<\mathcal{B}^\prime}(X)\subseteq T_{<\mathcal{B}^\prime}(S)\). For any \(v\in T_{<\mathcal{B}^\prime}(S)\), since \(d(v)<\mathcal{B}'<\mathcal{B}<B\), the shortest path to _v_ passes through some vertex \(x\in S^*\). Now that \(\widehat{d}[x]=d(x)\le d(v)<\mathcal{B}'\), we have \(x\in X\) and \(v\in T_{<\mathcal{B}^\prime}(X)\).

Now we are ready to prove the correctness part of Lemma 3.1.

**Lemma 3.7.** _We prove the correctness of Algorithm 3 by proving the following statement (the size of U is dealt with in Lemma 3.9), restated from Lemma 3.1: Given a level_ \(l\in[0,\lceil(logn)/t\rceil]\)_, a bound B and a set of vertices S of size_ \(\le 2^{lt}\)_, suppose that every incomplete vertex v with d(v)\<B is in T(S_<sup>∗</sup>).

_Then, after running Algorithm 3, we have:_ \(U=T_{<B^\prime}(S)\)_, and U is complete._

_Proof._ We prove by induction on _l_. When _l_=0, since _S_={_x_} is a singleton, _x_ must be complete. Then clearly the classical Dijkstra’s algorithm (Algorithm 2) finds the desired \(U=T_{<B^\prime}(S)\) as required. Suppose correctness holds for _l_-1, we prove that it holds for _l_. Denote D_<sub>i</sub>_ as the set of vertices (keys) in D just before the _i_-th iteration (at the end of the (_i_-1)-th iteration), and \(\mathcal{D}_i^*\) as the set of complete vertices in D_<sub>i</sub>_ at that time. Next, we prove the following two propositions by induction on increasing order of _i_:

Immediately before the _i_-th iteration,

(a) Every incomplete vertex _v_ with _d(v)\<B_ is in \(T_{[B_{i-1}^\prime,B)}(P)\).<tbc>

(b) \(T_{[B_{i-1}^\prime,B)}(P)=T_{<B}(\mathcal{D}_i)=T_{<B}(\mathcal{D}_i^*)\);

In the base case _i_=1, by Lemma 3.2, for every incomplete vertex _v_ with _d(v)\<B_ (including \(v\in P\)), \(v\in T_{<B}(P^*)\). Then \(d(v)\ge min_{x\in P^*}d(x)=min_{x\in P^*}\widehat{d}[x]\ge B'_0\). Thus every such _v_ is in \(T_{[B_0^\prime,B)}(P)\) (actually \(T_{<B_0^\prime}(P)\) is an empty set) and \(T_{[B_0^\prime,B)}(P)=T_{<B}(P)=T_{<B}(P^*)\). Because D<sub>1</sub>=_P_, the base case is proved.

Suppose both propositions hold for _i_. Then each incomplete vertex _v_ with _d(v)\<B_ is in \(T_{[B_{i-1}^\prime,B)}(P)\subseteq T(\mathcal{D}_i^*)\). By Lemma 3.3, the suppositions of Lemma 3.6 are met for _X_:=_S<sub>i</sub>_, _Y_:=D_<sub>i</sub>_\\_S<sub>i</sub>_, and B:=_B<sub>i</sub>_, so every incomplete vertex _v_ with _d(v)\<B<sub>i</sub>_ is in \(T(S_i^*)\); also note \(|S_i|\le 2^{(l-1)t}\). By induction hypothesis<tbc>

