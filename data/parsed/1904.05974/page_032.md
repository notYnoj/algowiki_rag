where _c<sub>x</sub>(a,b_)=wt_<sub>x</sub>(a,b_) for \(a,b\notin U\), see (1) for the definition of wt_<sub>x</sub>(a,b_); for \(a\in U\) or \(b\in U\), _c<sub>x</sub>(a,b_)=1. For a definition of \(\tilde{G}=(A\cup B,\tilde{E})\), see Section 2.

The only difference between \(\mathcal{E}'_G\) and E_<sub>G</sub>_ is in the right side of constraints (20) for \(a\in U\) or \(b\in U\).

Let \(E_D\subseteq E\) be the set of dominant edges of _G_, i.e., \(e\in E_D\) if there is a dominant matching in _G_ containing edge _e_. Adding to (19)-(23) the following constraints: (here \(\tilde{E}_D=E_D\cup\{(u,u):u\in U\}\))

\(x_e=0\forall e\in\tilde{E}\backslash\tilde{E}_D\) (24)

gives a face, call it R_<sub>G</sub>_, of \(\mathcal{E}'_G\).

**Claim 6** _For any dominant matching M in G and any dominant witness_ \(\unknown\) _of M,_ \((I_M,\unknown)\in\mathcal{R}_G\).

As \(M\subseteq\tilde{E}_D\), constraint (24) holds. The proof of Claim 6 is identical to that of Claim 1, with the addendum that (21) is tight for all unstable vertices _u_ (see Lemma 1), thus \(\beta_u=0\) for \(u\in U\) and this implies \(\beta_v=1\) for \(v\in\mathsf{Nbr}(U)\). Here Nbr(_U_) are the neighbors in _G_ of vertices in _U_.

Now let \((x,\unknown)\in\mathcal{R}_G\). We show it is a convex combination of vectors \((I_M,\unknown_M)\), where _M_ is a popular matching and \(\beta_M\) is a witness of _M_, and that \(\beta_v\in\{\pm 1\}\) for all \(v\in(A\cup B)\backslash U\). The proof is completely analogous to the proof of Theorem 10 (\[27\]), hence omitted. We conclude the following.

**Theorem 15.** _The polytope_ R_<sub>G</sub> defined by constraints_ (19)-(24) _is an extended formulation of the dominant matching polytope of G._

## 7.2 The Dominant Matching Polytope in R_<sup>m</sup>_

In this section we describe the convex hull of incidence vectors of dominant matchings in \(G=(A\cup B,E)\). Recall that all dominant matchings in _G_ match the same subset of vertices (see Section 2). We let again \(U\subseteq A\cup B\) be the set of unpopular vertices in _G_. In particular, every vertex in _U_ is left unmatched in any dominant matching in _G_. Note that _U_ has to be an independent set in _G_. We let again \(E_D\subseteq E\) be the set of dominant edges in _G_. Suppose \(x\in\mathbb{R}^m\) is a convex combination of dominant matchings. Then we have:

\(\sum_{e\in\delta(u)}x_e=1\forall u\in(A\cup B)\backslash U,x_e=0\forall e\in E\backslash E_D,x_e\ge 0\forall e\in E_D.\text{(25)}\)

For any matching _M_ in _G_, let \(k_M\ge 0\) be the number of vertices in _U_ that are matched in _M_. Consider the following family of constraints:

\(\mathsf{wt}_x(M)\le-k_M\forall matchingsM\text{in}G,\) (26)

where \(\mathsf{wt}_x(M)=\sum_{u\in A\cup B}\mathsf{vote}_u(M(u),x)\). Note that we are in the graph _G_ (and not in \(\tilde{G}\)) - so neither **_x_** nor _M_ needs to be perfect in _G_. We define therefore vote_<sub>u</sub>(M(u),**x**_), i.e., _u_’s vote for its assignment in _M_ versus its assignment in **_x_**, as follows.

- For \(u\in U\): vote_<sub>u</sub>(M(u),**x**_)=1 if _u_ is matched in _M_, else it is 0;<tbc>

**-** For \(u\in(A\cup B)\backslash U\): if _u_ is matched in _M_ then \(\mathsf{vote}_u(M(u),x)=\sum_{v^\prime:v^\prime\prec_uv}x_{(u,v^\prime)}-\sum_{v^\prime:v^\prime\prec_uv}x_{(u,v^\prime)}\), where _v_ is _u_’s partner in _M_; else (i.e., _u_ is unmatched in _M_) it is -1.<tbc>

