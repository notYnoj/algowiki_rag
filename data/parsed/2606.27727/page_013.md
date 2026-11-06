output should be correct with high probability. To do this, we need to circumvent the reduction to All-Edges Equality Inner Product.

## 4.2 Solving All-Edges Sparse Triangle in \(O(n^{1+2\delta} logw/w)\) Time

We begin by formally defining the All-Edges Sparse Triangle problem. We note that the instances that arise in the literature from the APSP and 3SUM reductions have _m=O(n_<sup>1.5</sup>) and maximum degree \(\Delta=O(\sqrt{n})\). We give a slight generalization, allowing for graphs of any sufficiently small sparsity. However, our techniques do require that the maximum degree \(\Delta=O(m/n)\). We also assume without loss of generality that the graph is tripartite; if this is not the case, generate two more copies of the vertex set, and add the original edges of the graph between each of the pairs of parts.

\(\blacktriangleright\) **Definition 22** (All-Edges Sparse Triangle)**.** _Let G be a tripartite graph whose vertex set is_ \(I\cup J\cup K\) _such that_ |_I_|=|_J_|=|_K_|=_n. Let the number of edges be_ \(m=n^{1+\delta}\) _for some_ \(\delta\in(0,0.5]\)_, and let the maximum degree be_ \(\Delta:=O(n^\delta)\)_. For every edge_ \(e\in E\cap(I\times J)\)_, decide whether e participates in a triangle._

**Reminder of Theorem 1.** There is a Las Vegas algorithm for All-Edges Sparse Triangle on graphs with maximum degree \(n^\delta\) running in \(O(n^{1+2\delta} logw)/w\) expected time.

**Proof of Theorem 1.** Let the word size \(w\ge clog(n)\) for a constant _c\>_0. As in Section 4.1, we can think of solving All-Edges Sparse Triangle as responding to \(O(n^{1+\delta})\) edge queries, each in \(o(n^\delta)\) time. Our algorithm is loosely inspired by a communication complexity protocol for set disjointness due to Dasgupta, Kumar, and Sivakumar [18]. We do the following:

**1.** Randomly partition _K_ into \(n^\delta/w\) color classes. **2.** Compress the name of each vertex in _K_ using a random hash function: \(h:[n]\rightarrow[\mathsf{poly}(\ell)]\) **3.** For each vertex _i_ in \(I\cup J\), for every color class _v_ in \([n^\delta/w]\), write down a compressed list that stores the hashes of their neighbors in that color class in sorted order. **4.** To respond to an edge query (_i,j_), for every color class, compute the set intersection of the compressed lists associated with _i_ and _j_’s neighbors with that color. If it is non-empty, (_i,j_) participates in a triangle.

We will now discuss each step in more detail. We begin by color-coding the vertex set, randomly partitioning [_n_] into \(n^\delta/w\) color classes \(S_1,\dots,S_{n^\delta/w}\). We need to draw _h_ from an _O_(log_n_)-wise independent hash family, as follows.

Fix an arbitrary vertex \(i\in(I\cup J)\) and color class \(v\in[n^\delta/w]\). We define the random variable \(X_{i,v}:=|N(i)\cap S_v|\) to be the number of neighbors that _u_ has in the _v_th color class. Clearly, \(\mathbb{E}[X_{i,v}]=w\ge clog(n)\). By the \(k'\)-wise independent Chernoff bound (Theorem 11), we know that for \(\delta'\ge 1\) and \(k'\le\delta'\lfloor\mu/e^{1/3}\rfloor\) we have \(Pr[X\ge(1+\delta')\mu]\le e^{-k^\prime/2}\). Setting \(k'=6ln(n)\) and setting \(\delta'=6e^{1/3}/c\le O(1)\), we have

\(Pr[X_{i,v}\ge(1+\delta')w]\le 1/n^3.\)

We can union bound over all the color classes and all the vertices, which tells us that each vertex’s neighborhood in each color class has size at most \(k:=(1+\delta')w\) with probability 1-1_/n_. If this does not hold for all vertices, we can just rerun the color coding.

We will now run a second level of hashing. We pick a random hash function \(h:[n]\rightarrow[k^3]\) such that each element in the image can be expressed in \(\ell:=3logw+O(1)\) bits. We use \(\ell\) copies of the linear hash function \(h_r(x):=\langle r,x\rangle mod2\). One might (rightly) worry that

