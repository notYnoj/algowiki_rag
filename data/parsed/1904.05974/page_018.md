\(\text{minimize}\sum_{u\in A\cup B}\alpha_u\) (LP4)

subject to

\(\alpha_a+\alpha_b\ge g_M(a,b)\forall(a,b)\in E\)<br>
\(\alpha_u\ge g_M(u,u)\forall u\in A\cup B.\)

Given a matching _M_, if we can show a a feasible solution \(\alpha\in\mathbb{R}^n\) to (LP4) such that \(\sum_{u\in A\cup B}\alpha_u=0\), then the optimal value of (LP3) is at most 0, so we have \(\phi(N,M)-2\phi(M,N)\le 0\) for all _N_, i.e., \(u(M)\le 2\). Let us call such a vector \(\alpha\) a _witness_ for quasi-popularity. Interestingly, every quasi-popular matching admits a simple witness as shown below.

**Lemma 4.** _If M is a quasi-popular matching in G then M has a witness_ \(\alpha\in\{0,\pm 1,\pm 2\}^n\).

_Proof._ Since _M_ is quasi-popular, the optimal value of (LP3) is at most 0 and so \(\tilde{M}\) is an optimal solution to (LP3) (because \(g_M(\tilde{M})=0\)). The graph _G_ is bipartite, hence the constraint matrix of (LP4) is totally unimodular (note that adding self-loops does not change this fact). Thus (LP4) has an integral optimal solution \(\alpha\).

We have \(\alpha_u\ge g_M(u,u)\ge-2\) for all _u_. Complementary slackness implies \(\alpha_u+\alpha_v=g_M(u,v)=0\) for each edge \((u,v)\in M\). Thus \(\alpha_u=-\alpha_v\le 2\) for every vertex _u_ matched in _M_. Regarding any vertex _u_ that is left unmatched in _M_, we have \((u,u)\in\tilde{M}\), so \(\alpha_u=g_M(u,u)=0\) (by complementary slackness). Hence \(\alpha\in\{0,\pm 1,\pm 2\}^n\). \(\square\)

## 4.2 A Min-Cost Popular Fractional Matching

The popular fractional matching polytope L_<sub>G</sub>_ was briefly discussed in Section 2.1. The polytope L_<sub>G</sub>_ is the set of all perfect fractional matchings **_x_** in \(\tilde{G}\) that satisfy \(\mathsf{wt}_x(N)\le 0\) for all perfect matchings _N_ in \(\tilde{G}\).

The function wt_<sub>x</sub>(N_) defined below is linear in **_x_**: (recall the function vote_<sub>u</sub>(v,**x**_) defined in Section 2.1)

\(\mathsf{wt}_x(N)=\sum_{e\in N}\mathsf{wt}_x(e)=\sum_{u\in A\cup B}\mathsf{vote}_u(N(u),\mathbf{x})=\sum_{u\in A\cup B}\left(\sum_{v^\prime:v^\prime\prec_uN(u)}x_{(u,v^\prime)}-\sum_{v^\prime:v^\prime\succ_uN(u)}x_{(u,v^\prime)}\right).\)

A compact extended formulation E_<sub>G</sub>_ of the polytope L_<sub>G</sub>_ was given in Section 2.1. Thus we can find a min- cost popular fractional matching **_q_** in _G_ in polynomial time by optimizing over E_<sub>G</sub>_. We can, in fact, assume that **_q_** is a vertex of L_<sub>G</sub>_, hence half-integral (recall that L_<sub>G</sub>_ is a half-integral polytope \[27, Theorem 1\]). We will now show how we can use **_q_** to obtain a quasi-popular matching of cost at most cost(**_q_**).

We will show that **_q_**=(_I_<sub>_N_<sub>1</sub></sub>+_I_<sub>_N_<sub>2</sub></sub>)/2 where _N_<sub>1</sub>_,N_<sub>2</sub> are quasi-popular matchings in _G_ and _I<sub>N</sub>_ is the edge incidence vector of matching _N_. Since \(\mathsf{cost}(N_1)+\mathsf{cost}(N_2)=2\cdot\mathsf{cost}(\mathbf{q})\), one of _N_<sub>1</sub>_,N_<sub>2</sub> has cost at most cost(**_q_**). Thus the matching in {_N_<sub>1</sub>_,N_<sub>2</sub>} with lower cost is our desired matching.

### A New Graph \(G'\).

The following useful property on the min-cost popular fractional matching **_q_** follows from the proof of half-integrality of L_<sub>G</sub>_ given in \[27\]: for every \(u\in A\cup B\) we have \(\sum_{e\in\delta(u)}q_e\in\{0,1\}\). In other words, every vertex _u_ is either "completely matched" or "completely unmatched" in **_q_** (so _q_<sub>(_u,u_)</sub>=1 in the latter case), i.e., no vertex is _half-matched_ in **_q_**.

Let _U<sub>A</sub>_ be the set of vertices in _A_ that are left unmatched in **_q_** and let _U<sub>B</sub>_ be the set of vertices in _B_ that are left unmatched in **_q_**. We now augment the graph _G_ with new vertices and new edges as follows.

Corresponding to each \(u\in U_A\cup U_B\), there will be a new vertex \(u'\). Thus the vertex set of the augmented graph (call it \(G'\)) is \(A'\cup B'\) where \(A'=A\cup U'_B\) and \(B'=B\cup U'_A\). Here \(U'_A=\{u':u\in U_A\}\), i.e., \(U'_A\) is a copy of _U<sub>A</sub>_, and \(U'_B=\{u':u\in U_B\}\) is a copy of _U<sub>B</sub>_.

The edge set \(E'\) of \(G'\) is \(E\cup\{(u,u'):u\in U_A\cup U_B\}\). The vertex \(u'\) is the least preferred neighbor of _u_ for every \(u\in U_A\cup U_B\) and _u_ is \(u'\)’s only neighbor. Fig. 5 will be helpful.

