then vertex _v_ will never be queried by any optimal strategy in _v_, since a query to _v_ can then be replaced by a sequence of queries to all neighbors of _v_, obtaining not less information at strictly smaller cost. In general, given an instance which does not satisfy the star condition, we enforce it by performing all necessary weight replacements \(w(v)\leftarrow min\{w(v),\sum_{u\in N(v)}w(u)\}\), for \(v\in V\) .

For \(a,\omega\in\mathbb{R}_{\ge 0}\), we denote the rounding of _a_ down (up) to the nearest multiple of \(\omega\) as \(\lfloor a\rfloor_\omega=\omega\lfloor a/\omega\rfloor\) and \(\lceil a\rceil_\omega=\omega\lceil a/\omega\rceil\), respectively.

## 2.2 Definition of a Search Strategy

_A search strategy_ A for a rooted tree _T_=(_V,E,w_) is an adaptive algorithm which defines successive queries to the tree, based on responses to previous queries, with the objective of locating the target vertex in a finite number of steps. Note that search strategies can be seen as decision trees in which each node represents a subset of vertices of _T_ that contains _x_, with leaves representing singletons consisting of _x_.

Let Q<sub>A</sub>(_T,x_) be the time-ordering (sequence) of queries performed by strategy A on tree _T_ to find a target vertex _x_, with Q<sub>A_,i_</sub>(_T,x_) denoting the _i_-th queried vertex in this time ordering, \(1\le i\le|\mathsf{Q}_\mathcal{A}(T,x)|\).

We denote by<tbc>

\(\mathsf{COST}_\mathcal{A}(T,x)=\sum_{i=1}^{|\mathsf{Q}_\mathcal{A}(T,x)|}w(\mathsf{Q}_{\mathcal{A},i}(T,x))\)

<tbc>the sum of weights of all vertices queried by A with _x_ being the target node, i.e., the time after which A finishes. Let<tbc>

\(\mathsf{COST}_\mathcal{A}(T)=max_{x\in V}\mathsf{COST}_\mathcal{A}(T,x)\)

<tbc>be the _cost of_ A. We define the _cost of T_ to be

\(\mathsf{OPT}(T)=min\{\mathsf{COST}_\mathcal{A}(T)\big|\mathcal{A}\text{is a search strategy for}T\}.\)

We say that a search strategy is _optimal_ for _T_ if its cost equals `OPT`(_T_).

As a consequence of normalization and the star condition, we have the following bound.

**Observation 2.1.** _For any tree T, we have_ \(1\le\mathsf{OPT}(T)\le\lceil log_2n\rceil\).

_Proof._ By the star condition, considering any vertex \(v\in V\) as the target, we trivially have

\(\mathsf{OPT}(T)\ge inf_\mathcal{A}\mathsf{COST}_\mathcal{A}(T,v)\ge inf_\mathcal{A}\mathsf{COST}_\mathcal{A}(T[\{v\}\cup N(v)],v)\ge w(v).\)

Thus, \(\mathsf{OPT}(T)\ge max_{v\in V}w(v)=1\), which gives the first inequality.

For the second inequality, we observe that applying to tree _T_ the optimal search strategy for unweighted trees, we can locate the target in at most \(\lceil log_2n\rceil\) queries (cf. e.g. \[19, 30\]). Since the cost of each query is at most 1, the claim follows.

We also introduce the following notation. If the first |_U_| queried vertices by a search strategy A are exactly the vertices in _U_, \(U=\{\mathsf{Q}_{\mathcal{A},i}(T,x):1\le i\le|U|\}\), then we say that A _reaches_ \(T\langle U,x\rangle\) _through U_, and _w(U_) is the _cost of reaching_ \(T\langle U,x\rangle\) _by_ A. We also say that we receive an ‘up’ reply to a query to a vertex _v_ if the root of the tree remaining to be searched remains unchanged by the query, i.e., \(r(T\langle U,x\rangle)=r(T\langle U\cup\{v\},x\rangle)\), and we call the reply a ‘down’ reply when the root of the remaining tree changes, i.e., \(r(T\langle U,x\rangle)\neq r(T\langle U\cup\{v\},x\rangle)\). Without loss of generality, after having performed a sequence of queries _U_, we can assume that the tree \(T\langle U,x\rangle\) is known to the strategy.

