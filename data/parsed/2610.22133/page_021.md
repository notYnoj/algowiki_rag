Proof. We proceed by rewriting each of the three terms in Equation (8). For the first term, we use the fact that if \((N(w)\cap N(v))\backslash N(u)=\varnothing\) for every \(w\in C\backslash N[u]\), then:<tbc>

\(\sum_{w\in C\backslash N[u]}|N(w)\cap N(v)|=\sum_{w\in C\backslash N[u]}|N(w)\cap N(v)\cap N(u)|.\)

<tbc>For the second and third terms, basic set rewriting yields:

\(\sum_{w\in C\backslash N[u]}|N(w)\cap N(u)|=\sum_{w\in C\backslash N[u]}|N(w)\cap N(u)\cap N(v)|+\underbrace{\sum_{w\in C\backslash N[u]}|(N(w)\cap N(u))\backslash N(v)|}_{(\dagger)},\)<br> \(\sum_{w\in C\cap N(u)}|N(w)\backslash N[u]|=\sum_{w\in C\cap N(u)}|(N(w)\cap N(v))\backslash N[u]|+\underbrace{\sum_{w\in C\cap N(u)}|N(w)\backslash(N(v)\cup N[u])|}_{(\dagger)}.\)

Summing and subtracting the terms as they appear in the definition of \(\Delta_v(C)\), we get that the right-hand side simplifies to our target expression, \(\sum_{w\in C\cap N(u)}|(N(w)\cap N(v))\backslash N(u)|\), since \((N(w)\cap N(v))\backslash N[u]=(N(w)\cap N(v))\backslash N(u)\), and provided that Term (†) and Term (‡) are equal. To verify this equality, we note that:

Term (‡) counts all pairs (_x,y_) such that \(x\in C\cap N(u)\), \(\{x,y\}\in E\), and \(y\notin N(v)\cup N[u]\).

Term (†) counts all pairs (_x,y_) such that \(y\in C\backslash N[u]\), \(\{x,y\}\in E\), and \(x\in N(u)\backslash N(v)\).

Because every neighbor of _u_ is either in _C_ or in _N(v_), the condition \(x\in C\cap N(u)\) is equivalent to \(x\in N(u)\backslash N(v)\). Moreover, for any node \(y\in N(x)\) where \(x\in C\), we have \(y\notin N(v)\) if and only if \(y\in C\). Thus, we have that Term (†) and Term (‡) are indeed equal.

**Runtime.** Step (i) takes time \(\tilde{\mathcal{O}}(n^\omega)\). All other steps take time \(\mathcal{O}(\sum_v\sum_{C\in C_v}|C|)=\mathcal{O}(\sum_vn)=\mathcal{O}(n^2)\).

## 4.5 Recognizing Quasi-Triangulated Graphs Faster

As explained in Section 2, it suffices to give an algorithm for the decremental simplicial vertex problem, where each update corresponds to a vertex deletion and we need to maintain whether there is a simplicial vertex in the graph. In the following theorem, we present an algorithm that solves this problem in subcubic (amortized) time.

**Theorem 4.14.** _There is an algorithm for Decremental Simplicial Vertex that on an n-node graph runs in time_

\(\mathcal{O}\left(min_{\Delta\in[1..n]}\{n/\Delta\cdot\mathsf{MM}(n,\Delta,n)+m\cdot\Delta\}\right).\)

_In particular, with the current bounds on rectangular matrix multiplication_<sup>12</sup> _this gives a running time of_ O(_n_<sup>2.5275</sup>) _on dense graphs. For sparse graphs, bounding the rectangular product naively by dividing it into_ \(\Delta\times\Delta\) _blocks yields a running time of_ \(\mathcal{O}\left(m^{(3-\omega)/(4-\omega)}n^{3/(4-\omega)}\right)\).

**Proof.** Let \(\Delta\in[1..n]\) be a parameter. First, we set up some notation and make some remarks:

For \(i\in[0..n]\), let the _i_-th _time step_ be the point in time before the _i_-th removal (zero-indexed) in the overall process. Further partition the _n_ time steps into \(\lceil n/\Delta\rceil\) _phases_ of size at most \(\Delta\). Let [_t<sub>j</sub>..t_<sub>_j_+1</sub> ] denote the time steps in the _j_-th phase, where _t_<sub>0</sub>=0 and \(t_{\lceil n/\Delta\rceil}=n\).

Let **G**_<sub>i</sub>_=(_V<sub>i</sub>,E<sub>i</sub>_) be the graph at the _i_-th time step (in particular **G**<sub>0</sub> is the input graph), write _N<sub>i</sub>(v_) for _N_<sub>**G**_<sub>i</sub>_</sub>(_v_) and _N<sub>i</sub>_\[_v_\] for \(N_i(v)\cup\{v\}\), and let _A<sub>i</sub>_ and \(\bar{A}_i\) denote the adjacency matrix of **G**_<sub>i</sub>_ and the complement of **G**_<sub>i</sub>_, respectively. Note that during the entire process it is easy to maintain _A<sub>i</sub>_ and the neighborhood of the vertices in total time O(_n_<sup>2</sup>).

The algorithm maintains a count \(\delta_i(v)\) for each vertex \(v\in V_i\), defined as the number of induced _P_<sub>3</sub>’s where _v_ is the middle vertex. Formally, \(\delta_i(v):=|\{\{x,y\}\subseteq N_i(v):\{x,y\}\notin E_i\}|\) is the number of missing edges in the neighborhood of _v_. Clearly, \(\delta_i(v)=0\) if and only if _v_ is a simplicial vertex in **G**_<sub>i</sub>_. This means that for each query, it suffices to return any node for which \(\delta_i(v)=0\), or report that no such node exists.

<sup>12</sup> We used the bounds from \[ADV<sup>+</sup>25\] plugged into van den Brand’s optimization tool \[Bra\].

