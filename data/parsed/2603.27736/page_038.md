**Remark 5.5.** _The same proof shows that the premise,_ \(\mathrm{MinPlus}(n,n^\alpha,n|u\le n^\alpha)=O(n^{2+\alpha-\epsilon})\)_, is_ equivalent _for all_ \(\alpha\in(0,1]\)_, i.e., if the premise holds for some_ \(\alpha\in(0,1]\) _then it also holds for all_ \(\alpha'\in(0,1]\)_, provided that_ \(\omega=2\)_. Curiously, this equivalence statement was already established for all_ \(\alpha\in(0,1)\) _in previous work by Chan, Vassilevska W., and Xu \[35, Corollary 7.6\]--only the equivalence with_ \(\alpha=1\) _(i.e., the Strong APSP hardness) was missing._

Corollary 5.4 combined with the equivalence of \(\mathrm{MinPlus}(n,n^\mu,n|u\le n^{1-\mu})\) and directed unweighted APSP due to \[33\] completes the proof of Theorem 1.7.

In the following, we quickly prove the strengthening of Theorem 1.7 that Zwick’s algorithm is best-possible for arbitrary weight bounds provided that \(\omega=2\), Theorem 1.8. For the proof we rely on the following simple generalization of \[33\]:

**Lemma 5.6.** _Let_ APSP(_n|u_) _denote the running time of APSP in n-vertex graphs with weights_ {0_,...,u}. Then_ \(\mathrm{MinPlus}(n,n_2,n|u)=O(\mathrm{APSP}(n|u\le n_2u/n))\) _for all parameters_ \(n_2,u\le n\).

**Proof.** Let _A,B_ be the given matrices of sizes \(n\times n_2\) and \(n_2\times n\) with entries in \(\{0,\dots,u\}\cup\{\perp\}\). Pick the parameters \(q=\lfloor n_2u/n\rfloor\) and \(p=2\lceil n/n_2\rceil\). Since \(pq\ge u\) we can rewrite the matrices in their "(_p,q_)-ary" representations

\(A=A_1\cdot q+A_0,\)<br>
\(B=B_1\cdot q+B_0,\)

where _A_<sub>0</sub>_,B_<sub>0</sub> have entries in \(\{0,\dots,q-1\}\cup\{\perp\}\) and _A_<sub>1</sub>_,B_<sub>1</sub> have entries in \(\{0,\dots,p-1\}\cup\{\perp\}\).

Next, we construct a graph _G_ as follows. The vertices consist of three separate sets \(I\sqcup K\sqcup J\). The sets _I_ and _J_ are each copies of \[_n_\], and _K_ is \([n_2]\times\{-p,\dots,p\}\). We choose the edges as follows: For each non-\(\perp\) entry _A_\[_i,k_\] we insert an edge from \(i\in I\) to \((k,-A_1[i,k])\in K\) with weight _A_<sub>0</sub>\[_i,k_\]. For each non-\(\perp\) entry _B_\[_k,j_\] we insert an edge from \((k,B_1[k,j])\in K\) to \(j\in J\) with weight _B_<sub>0</sub>\[_k,j_\]. And finally we turn each of the vertex sequences (_k,-p),...,(k,p_) into a directed path, where each edge along the path has weight _q_.

We claim that the min-plus product _A∗B_ equals exactly the _I_-to-_J_ distances in _G_. Indeed, the only directed paths from \(i\in I\) to \(j\in J\) take the form _i,(k,-A_<sub>1</sub>\[_i,k_\])_,...,(k,B_<sub>1</sub>\[_k,j_\])_,j_. The weight of such a path is exactly _A_<sub>0</sub>\[_i,k_\] (the first edge) plus _B_<sub>0</sub>\[_k,j_\] (the last edge) plus \(q\cdot(A_1[i,k]+B_1[k,j])\) (the middle edges). In sum this is _A_\[_i,k_\]+_B_\[_k,j_\], so the claim follows.

Moreover, _G_ is a graph on \(|I|+|K|+|J|\le n+O(pn_2)+n=O(n)\) vertices, and the largest edge weight in _G_ is \(q\le n_2u/n\). Hence we can solve APSP on _G_ in time \(\mathrm{APSP}(n|u\le n_2u/n)\) and read off the desired min-plus product from the computed distances.

**Theorem 1.8** (Zwick’s Algorithm is Optimal)**.** _Let_ \(0\le\delta\le 1\) _be a constant. APSP in directed graphs with weights_ \(\{0,\dots,n^\delta\}\) _cannot be solved in time_ \(O(n^{2.5+\delta/2-\epsilon})\) _(for any constant_ \(\epsilon>0\)_), unless the Strong APSP Hypothesis fails._

**Proof.** Suppose that \(\mathrm{APSP}(n|u\le n^\delta)=O(n^{2.5+\delta/2-\epsilon})\) for some constant \(\epsilon>0\). Then by Lemma 5.6 it follows that \(\mathrm{MinPlus}(n,n^{1/2+\delta/2},n|u\le n^{1/2+\delta/2})=O(n^{2.5+\delta/2-\epsilon})\). This contradicts the Strong APSP Hypothesis by Corollary 5.4 (with \(\alpha=1/2+\delta/2\)).

Finally, we consider undirected graphs and prove that the Shoshan-Zwick algorithm is best-possible conditioned on the Strong APSP Hypothesis.

**Theorem 1.9** (Shoshan-Zwick Algorithm is Optimal)**.** _Let_ \(0\le\delta\le 1\) _be a constant. APSP in undirected graphs with weights_ \(\{0,\dots,n^\delta\}\) _cannot be solved in time_ \(O(n^{2+\delta-\epsilon})\) _(for any constant_ \(\epsilon>0\)_), unless the Strong APSP Hypothesis fails._

**Proof.** Suppose that APSP in undirected graphs with weights \(\{0,\dots,n^\delta\}\) is in time \(O(n^{2+\delta-\epsilon})\). By a standard construction it follows easily that \(\mathrm{MinPlus}(n,n,n|u<n^\delta/2)=O(n^{2+\delta-\epsilon})\). Indeed, we transform the given pair of matrices _A,B_ with entries less than \(u=n^\delta/2\) into an undirected graph with three vertex layers _I,K,J_, where we set the weight of any edge \((i,k)\in I\times K\) to _A_\[_i,k_\]+_u_ and of any edge \((k,j)\in K\times J\)<tbc>

