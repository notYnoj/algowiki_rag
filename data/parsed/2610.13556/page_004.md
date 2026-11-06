<tbc>**Definition 2.1** (Words and profiles)**.** A _word_ on _G_ is a map \(w:V(G)\rightarrow\mathcal{C}\), with no properness assumption. Its _profile_ is the vector \(\mathbf{m}(w)=(m_X(w))_{X\in\mathcal{C}}\), where _m<sub>X</sub>(w_)=|_w_<sup>-1</sup>(_X_)|. Bold letters denote vectors. Inequalities between vectors are coordinatewise, **e**_<sub>X</sub>_ is a coordinate unit vector, and **1** is an all-one vector of the required dimension.

Write P(_G_) for the proper colorings with palette C. Since \(|\mathcal{C}|=\chi(G)\), each such coloring uses every color. A profile **m** is _feasible_ if it occurs in P(_G_).

For a feasible profile, put<tbc>

\(\mathcal{W}_\mathbf{m}(G)=\{w:V(G)\rightarrow\mathcal{C}:\mathbf{m}(w)=\mathbf{m}\},\mathcal{P}_\mathbf{m}(G)=\mathcal{W}_\mathbf{m}(G)\cap\mathcal{P}(G).\)

<tbc>We omit _G_ from W**<sub>m</sub>**(_G_) when the vertex set is clear. Every word in W**<sub>m</sub>**(_G_) is a rearrangement of every proper coloring with that profile. We call such a word an _admissible disturbance_; equivalently, its profile is feasible. The Hamming distance and the number of agreements are

\(d_\mathrm{H}(w,y)=|\{v:w(v)\neq y(v)\}|,\mathrm{agr}(w,y)=n-d_\mathrm{H}(w,y).\)

The cost therefore counts changed vertices; exchanging two different colors on two vertices has cost two.

**Definition 2.2** (Repair radii and villainy)**.** The repair radius of a profile and its weak counterpart are

\(R_G(\mathbf{m})=\mathrm{max}_{w\in\mathcal{W}_\mathbf{m}(G)}\mathrm{min}_{y\in\mathcal{P}_\mathbf{m}(G)}d_\mathrm{H}(w,y),\)<br>
\(R_G^\mathrm{w}(\mathbf{m})=\mathrm{max}_{w\in\mathcal{W}_\mathbf{m}(G)}\mathrm{min}_{y\in\mathcal{P}(G)}d_\mathrm{H}(w,y).\)

With the terminology of Clark et al. \[2\],

\(B(G)=\mathrm{max}_{\mathbf{m}\text{feasible}}R_G(\mathbf{m}),B_\mathrm{w}(G)=\mathrm{max}_{\mathbf{m}\text{feasible}}R_G^\mathrm{w}(\mathbf{m}).\)

Both parameters are zero on the empty graph by convention.

The inclusion of the two target sets gives \(B_\mathrm{w}(G)\le B(G)\). In particular, the weak target may change the profile, but it still uses the same palette of \(\chi(G)\) colors. A simultaneous permutation of the color labels in the source and target preserves distances and all profile conditions.

We write \[_k_\]={1_,...,k_}. For sets of vectors _A,B_, their sum is \(A+B=\{\mathbf{a}+\mathbf{b}:\mathbf{a}\in A,\mathbf{b}\in B\}\). The graph _mG_ is the disjoint union of _m_ vertex-disjoint copies of _G_.

## 3. Counterexamples to superadditivity

Clark et al. \[2, Propositions 3.7 and 3.8\] proved

\(B_\mathrm{w}(G\sqcup H)\ge B_\mathrm{w}(G)+B_\mathrm{w}(H)\text{when}\chi(G)=\chi(H),\) (3.1)

and its ordinary analogue when, in addition, every optimal coloring of one summand has equal-sized color classes. We show that the unrestricted inequalities fail by an arbitrarily large amount, even for connected summands.

**Theorem 3.1.** _For every real C\>_0_, there exists a connected graph G such that_<tbc>

\(B_\mathrm{w}(G\sqcup K_3)<B_\mathrm{w}(G)+B_\mathrm{w}(K_3)-C.\)

<tbc>_Proof._ For a positive integer _s_, let _T<sub>s</sub>_ consist of an edge _uv_ with 3_s_ leaves adjoined to each endpoint. Both bipartition classes have size 3_s_+1. The connected bipartite formula \[2, Proposition 3.3\] gives

\(B_\mathrm{w}(T_s)=2\left\lfloor\frac{3s+1}{2}\right\rfloor,B_\mathrm{w}(K_3)=0.\)

We show that \(B_\mathrm{w}(T_s\sqcup K_3)\le 2s+3\).

