where \(1\le d\le k\) and \(0\le a<q\). Let _G_=(_V,E_) be a finite simple undirected graph with _V_={1_,...,k_}. Order _E_ lexicographically and define<tbc>

\(\mathsf{GT}_q(G)=\otimes_{(i,j)\in E}E_{i,j}^{(q)},\)

<tbc>where the empty product is l_<sub>k</sub>_(1). For \(1\le v\le k\), let _d<sub>v</sub>_ be the degree of vertex _v_, and list its incident edges in the induced order as _e_<sub>_v,_1</sub>_,...,e<sub>v,d<sub>v</sub></sub>_. For each labeling \(\lambda:E\rightarrow[q]_0\), put<tbc>

\(I_v(\lambda)=\sum_{t=1}^{d_v}\lambda(e_{v,t})q^{d_v-t}(1\le v\le k).\)

<tbc>Equivalently, the graph tensor is

\(\mathsf{GT}_q(G)=\sum_{\lambda:E\rightarrow[q]_0}\otimes_{v=1}^ke_{I_v(\lambda)}^{(q^{d_v})}.\)

Thus dim(GT_<sub>q</sub>(G_))=(_q_<sup>_d_<sub>1</sub></sup>_,...,q<sup>d<sub>k</sub></sup>_); an isolated vertex has a leg of dimension 1.

**Lemma 2.21** (pairing edge labels \[CVZ19, Definition 1.1.1 and the following observation\])**.** _For every finite simple undirected graph G with at least two vertices and all positive integers p,q,_

\(\mathsf{GT}_p(G)\otimes_K\mathsf{GT}_q(G)\cong\mathsf{GT}_{pq}(G).\)

_Consequently,_ \(\mathsf{GT}_q(G)^{\otimes_KN}\cong\mathsf{GT}_{q^N}(G)\) _for every positive integer N._

_Proof._ A supported term on the left is specified by two edge labelings \(\lambda:E\rightarrow[p]_0\) and \(\mu:E\rightarrow[q]_0\). Associate with them the labeling \(\nu:E\rightarrow[pq]_0\) given by \(\nu(e)=q\lambda(e)+\mu(e)\) for every \(e\in E\). This is a bijection, since division by _q_ recovers \(\lambda(e)\) and \(\mu(e)\) from \(\nu(e)\). At each vertex _v_, its coordinate on the left records the two lists of labels on the edges incident with _v_. Pairing these labels edge by edge gives the coordinate \(I_v(\nu)\) on the right. This is a permutation of that vertex’s _p<sup>d<sub>v</sub></sup>q<sup>d<sub>v</sub></sup>_=(_pq)<sup>d<sub>v</sub></sup>_ coordinates. Applying these permutations independently at every vertex sends each supported term to its corresponding term with the same coefficient 1. This proves the isomorphism. The assertion about powers follows by induction on _N_.

For _G=K_<sub>3</sub>, a choice of coordinates gives

\(\mathsf{GT}_q(K_3)\cong\sum_{0\le a,b,c\le q-1}e_{aq+b}^{(q^2)}\otimes_Ce_{bq+c}^{(q^2)}\otimes_Ce_{cq+a}^{(q^2)}.\)

Its contraction with three \(q\times q\) matrices _A,B,C_ is \(\sum_{0\le a,b,c\le q-1}A_{a,b}B_{b,c}C_{c,a}=\mathrm{tr}(ABC)\). Hence it is the matrix multiplication tensor. The standard relation between arithmetic complexity and asymptotic tensor rank gives \(\omega=\mathrm{log}\widetilde{\mathsf{R}}(\mathsf{GT}_2(K_3))\) \[BCS97\].

**Definition 2.22** (edge exponent)**.** Let _G_=(_V,E_) be a finite simple undirected graph with \(|V|\ge 2\) and \(|E|\ge 1\). Its _edge exponent_ is

\(\tau(G)=\frac{\mathrm{log}_2\widetilde{\mathsf{R}}(\mathsf{GT}_2(G))}{|E|}.\)

In particular, \(\tau(K_n)=\mathrm{log}_2\widetilde{\mathsf{R}}(\mathsf{GT}_2(K_n))/\genfrac(){pt}{2}{n}{2}\) for every integer \(n\ge 2\).

