## 4 Fault-Tolerant Bounded Flow Preservers

\(\blacktriangleright\) **Theorem 7.** _For any_ \(\lambda,k,n\ge 1\) _satisfying_ \(k=\Omega(log(\lambda^{-1}n))\)_, the problem of computing an_ \(O(log(\lambda^{-1}n))\) _approximate_ \((\lambda,k)\)_-FT-BFP for n vertex digraphs is NP-hard._

We prove the above theorem by showing a reduction from the SET-COVER problem to the optimal FT-BFP.

\(\blacktriangleright\) **Problem 8** (\[18\], Definition 1)**.** _The input to SET-COVER consists of base set U,_ |_U_|=_n and subsets_ \(S_1,\dots,S_m\subseteq U\), \(\cup_{j=1}^mS_j=U\), \(m\le poly(n)\)_. The goal is to find as few sets S_<sub>_i_<sub>1</sub></sub>_,...,S<sub>i<sub>k</sub></sub> as possible that cover U, that is,_ \(\cup_{j=1}^kS_{i_j}=U\)

\(\blacktriangleright\) **Lemma 9** (\[18\], Theorem 2)**.** _For every_ \(0<\alpha<1\) _(exact) SAT on inputs of size n can be reduced in polynomial time to approximating SET-COVER to within_ \((1-\alpha)lnN\) _on inputs of size_ \(N=n^{O(1/\alpha)}\).

From Lemma 9, we can also deduce that it is NP-Complete to approximate SET- COVER up to a multiplicative factor of _c_<sub>1</sub>logmax(_n,m_) for some _c_<sub>1</sub>_\>_0 as \(m\le poly(n)\).

**Transformation** Given a SET-COVER instance \(\langle U,\mathfrak{F}\rangle\), we will construct a \((\lambda,k)\)-FT- BFP instance \(\langle\mathcal{G},s\rangle\). The transformation is as follows (also see Figure 1).

**1.** Round up the number for elements in _U_ to nearest power of 2 (let this be 2_<sup>u</sup>_) by adding 2_<sup>u</sup>_-|_U_| new elements to _U_ and all these new elements to every set in F.

**2.** Initialize G to be the graph with _N_+1 vertices, namely, _s,v_<sub>1</sub>_,...,v<sub>N</sub>_ where \(N=4\lambda(m+n)\).

**3.** Next construct the following subgraph G_<sub>i</sub>_, for each \(i\in[1,\lambda]\).

**a.** Construct a complete binary tree _B<sub>i</sub>_ rooted at a vertex _r<sub>i</sub>_ of height _u_ and 2_<sup>u</sup>_ leaf nodes. The leaf nodes of _B<sub>i</sub>_ will correspond to elements in the universe _U_. From each leaf node _x<sub>i</sub>_ in _B<sub>i</sub>_, add out-edges to two new vertices, namely, \(\ell(x_i)\) and _r(x<sub>i</sub>_).

**b.** For each set \(W\in\mathfrak{F}\), add a vertex _y<sub>i,W</sub>_ to graph G_<sub>i</sub>_. Let _Y<sub>i</sub>_ denote the resulting set which consists of |F| vertices. For each \(x\in U\) and \(W\in\mathfrak{F}\), add an edge from \(\ell(x_i)\) to _y<sub>i,W</sub>_ if and only if \(x\in W\).

**c.** Add a set _Z<sub>i</sub>_ of _u_+1 additional vertices. For each leaf _x<sub>i</sub>_ in _B<sub>i</sub>_, add an edge from _r(x<sub>i</sub>_) to each vertex in the set _Z<sub>i</sub>_.

**4.** Finally, we add an edge from _s_ to the roots \(r_1,\dots,r_\lambda\). Also for each \(i\in[1,\lambda]\), we add an edge from each vertex in \(Y_i\cup Z_i\) to each of the vertices _v_<sub>1</sub>_,...,v<sub>N</sub>_.

We set _k=u_+1 for this \((\lambda,k)\)-FT-BFP instance.

\(\blacktriangleright\) **Lemma 10.** _Any_ \((\lambda,k)\)_-FT-BFP_ H _of the graph instance_ \(\langle\mathcal{G},s\rangle\)_, can be used to construct a solution of the SET-COVER instance of size at most_ \(\lambda^{-1}(min_{j=1}^N|_{IN}(v_j,\mathcal{H})|)\).

**Proof.** Consider a vertex _v<sub>j</sub>_ in H that minimizes |IN(_v<sub>j</sub>,_H)|. Consider the following candidate solutions

\(S_i=\{W\in\mathfrak{F}|(y_{i,W},v_j)\in E(\mathcal{H})\}.\)

Out of the \(\lambda\) sets, namely \(S_1,\dots,S_\lambda\), let _S_<sub>_i_<sub>0</sub></sub> be the set with least cardinality. The cardinality of _S_<sub>_i_<sub>0</sub></sub> is at most \(|in(v_j,\mathcal{H})|/\lambda\) as minimum value is upper-bounded by the average value.

Now in order to prove that _S_<sub>_i_<sub>0</sub></sub> is a valid solution, consider an element \(x\in U\). Let _P_ be the unique path from _r_<sub>_i_<sub>0</sub></sub> to leaf node _x_<sub>_i_<sub>0</sub></sub> in _B_<sub>_i_<sub>0</sub></sub>, and let _F_<sub>1</sub> be the set of all those edges \((u,v)\in B_{i_0}\) such that \(u\in P\) and _v_ is the child of _u_ not lying on _P_. Observe that _x_<sub>_i_<sub>0</sub></sub> is the unique leaf in _B_<sub>_i_<sub>0</sub></sub> that is reachable from _s_ in H\\_F_<sub>1</sub>. Let _F_<sub>2</sub> be a singleton set comprising of the edge (_x_<sub>_i_<sub>0</sub></sub>_,r(x_<sub>_i_<sub>0</sub></sub>)). Consider the set \(F=F_1\cup F_2\) of size _k_. Since

