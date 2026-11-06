<tbc>**Runtime.** Clearly, Step (i) and Step (ii) run in time \(\tilde{\mathcal{O}}(n^\omega)\).

On the other hand, in Step (iii), we first find _x<sub>C</sub>_ for each \(C\in\mathcal{C}\) and verify whether to list all witnessed pairs in _C_. It is not difficult to see that this can be implemented in time \(\mathcal{O}(\sum_{v\in V}|\mathcal{C}_v|)\le\mathcal{O}(\sum_{v\in V}|V\backslash N[v]|)\le\mathcal{O}(n^2)\). Let \(S\subseteq\mathcal{C}\) be the set of all \(C\in\mathcal{C}\) for which we list all pairs \(u,v\in C\). For each \(C\in S\) we spend time O(|_C_|<sup>2</sup>). Over all elements \(C\in S\) this becomes:

\(\sum_{C\in S}|C|^2\le\sum_{C\in S}|C|\cdot|V\backslash N[x_C]|(C\in\mathcal{C}_{x_C})\)<br>
\(\le 2\sum_{C\in S}|C|\cdot|\{w\in V:C\in\mathcal{C}_w\}|(|\{w\in V:C\in\mathcal{C}_w\}|\ge|V\backslash N[x_C]|/2\text{holds for all}C\in S)\)<br>
\(\le 2\sum_{C\in\mathcal{C}}|C|\cdot|\{w\in V:C\in\mathcal{C}_w\}|(S\subseteq\mathcal{C})\)<br>
\(=2\sum_{v\in V}|V\backslash N[v]|\text{(double counting argument)}\)<br>
\(\le 2n^2,\)

which concludes the proof.

## 4.4 Listing Two-Pairs in Matrix Multiplication Time

We begin with the observation by Arikati and Pandu Rangan \[AR91\], which characterizes two-pairs based on neighborhood-deleted components. For the sake of completeness, we also include a proof of it.

**Proposition 4.11** (Lemma 2 of \[AR91\])**.** _Let_ **G**=(_V,E_) _be a graph. Then, for any two distinct non-neighboring vertices u,v the following holds: u,v is a two-pair if and only if_ \(N(u)\cap N(v)=N(C_v(u))\).

**Proof.** Let us abbreviate _C_:=_C<sub>v</sub>(u_). By definition of _C_, we always have that \(N(u)\cap N(v)\subseteq N(C)\) and \(N(C)\subseteq N(v)\).

Suppose first that \(N(u)\cap N(v)\neq N(C)\), or equivalently that \(N(C)\backslash N(u)\neq\emptyset\). Let _w_ be any vertex in _N(C_)\\_N(u_). Consider a shortest path \(\pi\) from _u_ to _w_ in \(\mathbf{G}[C\cup\{w\}]\). Then, extending the path \(\pi\) with the edge {_w,v_} gives a chordless path from _u_ to _v_, which has length at least three, as illustrated in Figure 4. Thus, _u,v_ are not a two-pair.

Conversely, suppose that _u,v_ are not a two-pair, which means that there is a chordless path of length at least three between _u_ and _v_. Then, the neighbor _w_ of _v_ on this path is in _N(C_) but not in _N(u_). Thus, we have that \(N(u)\cap N(v)\neq N(C)\).

In other words, a two-pair is characterized by the property that the entire out-neighborhood of _C<sub>v</sub>(u_) (which must be a subset of _N(v_)) coincides exactly with the neighbors of _u_ outside of _C<sub>v</sub>(u_) (which must also be a subset of _N(v_)). This allows us to give the following algorithm to list all two-pairs in matrix multiplication time.

N[v]
N(C)
C
w
u
v
N(u)

**Figure 4.** Criterion for two vertices to form a two-pair

