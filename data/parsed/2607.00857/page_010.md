**Algorithm 3** The algorithm for Stage 2, as in Lemma 4, adapted from [12]

**Input:** Distance estimate matrix _D_, certificate _C_, and a parameter _p_ **Output:** Set of unverified pairs _U_ **fn VerifyEstimates(D, C, p):** **foreach** \((i,j)\in V^2\) **do** **foreach** \(k\in C[i,j]\) **do** detour\(_{D,i,j}(k)\leftarrow D[i,k]+D[k,j]-D[i,j]\) \(C'[i,j]\leftarrow\) the _p_ vertices \(k\in C[i,j]\) with the smallest detour<sub>_D,i,j_</sub>(_k_) \(R\leftarrow\) greedy hitting set for all \(C'[i,j]\) **foreach** \((i,j)\in V^2\) **do** \(r_{i,j}\leftarrow argmin_{r\in R\cap C^\prime[i,j]} detour_{D,i,j}(r)\) \(count_1[i,j]\leftarrow\big|\big\{k\in C[i,j]:D[i,k]+D[k,j]<D[i,r_{i,j}]+D[r_{i,j},j]\big\}\big|\) **foreach** \(r\in R\) **do // Compute # of better witnesses than r for all i,j** \(A[i,j]\leftarrow D[i,j]-D[i,r]\) \(B[i,j]\leftarrow D[r,j]-D[i,j]\) \(Dom\leftarrow A\otimes B\) **// Yuster’s dominance product algorithm** **foreach** \(i,j\in V\) such that _r=r<sub>i,j</sub>_ **do** \(count_2[i,j]\leftarrow Dom[i,j]\) **return** \(\{(i,j):count_1[i,j]\neq count_2[i,j]\}\)

## 3 Stage 2: Verification of the distance estimates

In the next step, we give a verification algorithm that verifies for each \((u,v)\in V^2\backslash\mathrm{U}(G,C,p)\) that it cannot be further relaxed in the matrix _D_, obtained from Lemma 3. The algorithm might coincidentally verify more pairs, so formally, it outputs a set \(U\subseteq\mathrm{U}(G,C,p)\) and guarantees \(D[u,v]=min_{w\in V}D[u,w]+D[w,v]\) for all \((u,v)\in V^2\backslash U\). To achieve this, we follow the co-nondeterministic algorithm for Exact Triangle from [12, Theorem 9.7]. They introduce a technique called "Fredman’s trick meets dominance product". In this case, it allows us to speed up counting the number of smaller detour vertices with fast matrix multiplication. We adapt the exact distances in their algorithm to minimum distances for shortest paths. Furthermore, we replace their non-deterministic hitting set and non-deterministic dominance product computation with efficient deterministic counterparts.

\(\blacktriangleright\) **Lemma 4.** _There is an algorithm that is given a graph G, a certificate C of size_ |_C[u,v_]|=_q for all_ \(u,v\in V\)_, and a parameter p. It computes_ \(U\subseteq\mathrm{U}(G,C,p)\) _such that for all_ \((u,v)\in V^2\backslash U\) _we have_ \(D[u,v]=min_{w\in V}D[u,w]+D[w,v]\). _The algorithm runs in time_ \(\tilde{\mathcal{O}}\left(n^2q+n^{3.66}/p\right)\)_, or_ \(\mathcal{O}\left(n^{2.83}\right)\) _for p_<sup>∗</sup>=_n_<sup>0.83</sup> _and q_=O(_p)._

**Proof.** The algorithm is adapted from [12] and works as follows (see Algorithm 3).

For every \(u,v\in V\), \(w\in C[u,v]\), compute detour<sub>_D,u,v_</sub>(_w_). Let \(C'[u,v]\) be the _p_ vertices in _C[u,v_] with the smallest detour.

Compute a set \(R\subseteq V\) such that for all \(u,v\in V\) the intersection \(R\cap C'[u,v]\) is non-empty, that is, a hitting set for all \(C'[u,v]\). To do so, run the greedy algorithm from Chapter 2 in [43]. We will show that _R_ has size O(_n_log<sup>2</sup>_n/p_).

For all _u,v_, fix an arbitrary representative \(r_{u,v}\in R\) that appears in \(C'[u,v]\). Any such choice works but choosing an _r_ with minimum detour<sub>_D,u,v_</sub>(_r_) minimizes the size of _U_ and hence verifies more distances.

For all \(u,v\in V\) , count the number of \(w\in C[u,v]\) such that _D[u,w_]+_D[w,v_]_\<D[u,r<sub>u,v</sub>_]+_D[r<sub>u,v</sub>,v_] using brute force.

