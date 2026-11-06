which is the other conclusion of our lemma.

It remains to show Eq. (8). Since the number of edges in the character-based bipartite graph is at least \(\lambda|T|d\), we have

\(\sum_{\ell=1}^dD_\ell\ge\lambda|T|d\)<br>
\(\ge\lambda(2/\lambda)d>d.(|T|\ge 2/\lambda\text{by lemma premise})\) (6)

We also require the following simple fact:

\(\forall x\ge y\ge z\ge 0,x(x-z)\ge y(y-z).\) (7)

Combining the last two inequalities, we finally have:

\(\frac{1}{d}(\sum_{\ell=1}^dD_\ell)^2-\sum_{\ell=1}^dD_\ell=\frac{\sum_{\ell=1}^dD_\ell}{d}(\sum_{\ell=1}^dD_\ell-d)\)<br>
\(\ge\frac{1}{d}(\lambda|T|d)^2-(\lambda|T|d)\text{(Ineq. (6) and (7)).}\) (8)

Now, we are ready to prove that the remaining graph is sparse.

**Lemma 3.19** (upper bound on \(|E(\mathsf{NG}_\lambda)|\))**.**

\(|E(\mathsf{NG}_\lambda)|\le\frac{2k^{2-\gamma}}{\lambda}\)

_holds with probability at least_ 1-1_/k_<sup>3</sup>.

In the proof of this lemma we will construct an auxiliary graph \(\mathsf{NF}_\lambda\) in the following way:

**Definition 3.20** (\(\mathsf{NF}_\lambda\))**.** Let _a_ denote the node in \(V(\mathsf{NG}_\lambda)\) that has the highest degree. The vertices of \(\mathsf{NF}_\lambda\) would be the set of neighbors of _a_ in \(\mathsf{NG}_\lambda\).We add an edge between vertices (_i,j_) in \(\mathsf{NF}_\lambda\) if both \(||\mathsf{lc}_{w_a}(w_i,w_j)||\ge\lambda^2/2\) and \(||\mathsf{lc}_{w_a}(w_j,w_i)||\ge\lambda^2/2\) hold.

_Proof of Lemma 3.19._ We prove the lemma by contradiction. Suppose<tbc>

\(|E(\mathsf{NG}_\lambda)|>\frac{2k^{2-\gamma}}{\lambda}.\)

<tbc>Since the number of vertices in \(\mathsf{NF}_\lambda\) is equal to the maximum degree of \(\mathsf{NG}_\lambda\) we have

\(|V(\mathsf{NF}_\lambda)|>\frac{2k^{1-\gamma}}{\lambda}.\) (9)

Using Lemma 3.18, we have for each set \(T\subseteq V(\mathsf{NF}_\lambda)\) with \(|T|\ge 2/\lambda\), there exist two nodes _u_ and _v_ in _T_ such that (_u,v_) is an edge of \(\mathsf{NF}_\lambda\).

If we look at the complement of graph \(\mathsf{NF}_\lambda\), we know there is no clique _K<sub>r</sub>_ where \(r=2/\lambda\). Using Turan’s theorem (Lemma A.5) we know that the complement of graph \(\mathsf{NF}_\lambda\) has at most \((1-\frac{1}{r-1})\frac{q^2}{2}<(1-\frac{1}{r})\frac{q^2}{2}\) edges, where \(q:=|V(\mathsf{NF}_\lambda)|\). Then we have<tbc>

\(|E(\mathsf{NF}_\lambda)|>\frac{q(q-1)}{2}-(1-\frac{1}{r})\frac{q^2}{2}=\frac{q^2}{2r}-\frac{q}{2}.\)

