<tbc>We begin with a theorem that completely determines the permutational Ramsey numbers in which one argument is a monotone path with a trivial permutation group, while the other is any connected graph with an arbitrary permutation group. The upper bound was implicitly shown by Károlyi, Pach and Tóth \[16\], as remarked by Balko, Cibulka, Král and Kynčl \[3, Lemma 18\], while the lower bound can be established similarly to \[4, Theorem 4.1\]. For completeness, we provide the full proof.

**Theorem 4.1.** _For_ \(a,b\in\mathbb{N}\)_, let H be any connected graph of order a,_ \(\Gamma\) _any permutation group on V(H), and_ \(\Lambda\) _the trivial permutation group on_ \(V(P_b^\mathrm{mon})\)_. Then_ \(R\left(H^\Gamma,(P_b^\mathrm{mon})^\Lambda\right)=1+(a-1)(b-1)\).

_Proof._ The theorem trivially holds if min{_a,b_}=1, so we assume that \(a,b\ge 2\). First, we establish the upper bound by showing that every 2-edge-coloring of _K<sub>n</sub>_ with _n_=1+(_a_-1)(_b_-1) contains a forbidden embedding. We carry out the proof by induction on _b_. To begin, the statement trivially holds for _b_=2, so we assume that \(b\ge 3\). Consider a 2-edge-coloring of _K<sub>n</sub>_, and let _G<sub>j</sub>_ denote the spanning subgraph of _K<sub>n</sub>_ comprising the edges of color _j_, for \(j\in\{1,2\}\). Suppose that _H_ is not \(\Gamma\)-embeddable in _G_<sub>1</sub>. Then, since (1+(_a_-1)(_b_-1))-(1+(_a_-1)(_b_-2))=_a_-1, by induction, there exist _a_ increasing injective homomorphisms \(\varphi_1,\varphi_2,\dots,\varphi_a\) from \(P_{b-1}^\mathrm{mon}\) to _G_<sub>2</sub> such that the numbers \(\varphi_1(b-2),\varphi_2(b-2),\dots,\varphi_a(b-2)\) are all mutually distinct. If none of the edges between the vertices \(\varphi_1(b-2),\varphi_2(b-2),\dots,\varphi_a(b-2)\) is colored in color 2, then there exists an increasing injective homomorphism from _H_ to _G_<sub>1</sub>, yielding a contradiction. Thus, at least one of these edges is colored in color 2, implying the existence of an increasing injective homomorphism from \(P_b^\mathrm{mon}\) to _G_<sub>2</sub>. Therefore, \(P_b^\mathrm{mon}\) is \(\Lambda\)-embeddable in _G_<sub>2</sub>, and hence \(R\left(H^\Gamma,(P_b^\mathrm{mon})^\Lambda\right)\le 1+(a-1)(b-1)\).

\begin{tabular}{ccccc}
Argument 1 & Argument 2 & Type & Status & \\
\multirow{4}{*}{alternating path} & \multirow{4}{*}{alternating path} & ordered & -- & -- \\
 & & reflective & -- & -- \\
 & & cyclic & conjectured \[4, Conjecture 4.8\] & _a+b_-2-(_ab_mod2) for \(a,b\ge 2\) \\
 & & dihedral & conjectured (Conjecture 4.4) & _a+b_-2-(_ab_mod2) for \(a,b\ge 2\) \\
\multirow{4}{*}{alternating path} & \multirow{4}{*}{start-central star} & ordered & -- & -- \\
 & & reflective & -- & -- \\
 & & cyclic & conjectured \[4, Conjecture 4.17\] & _a+b_-2-(_ab_mod2) for \(a,b\ge 2\) \\
 & & dihedral & conjectured (Conjecture 4.5) & _a+b_-2-(_ab_mod2) for \(a,b\ge 2\) \\
\multirow{4}{*}{alternating path} & \multirow{4}{*}{monotone path} & ordered & solved \[4, Corollary 4.2\] & 1+(_a_-1)(_b_-1) for \(a,b\in\mathbb{N}\) \\
 & & reflective & solved (Corollary 4.2) & 1+(_a_-1)(_b_-1) for \(a,b\in\mathbb{N}\) \\
 & & cyclic & conjectured \[4, Conjecture 4.9\] & 1+(_a_-1)(_b_-2) for \(a\ge 3\), \(b\ge 4\) \\
 & & dihedral & conjectured (Conjecture 4.6) & 1+(_a_-1)(_b_-2) for \(a\ge 3\), \(b\ge 4\) \\
\multirow{4}{*}{alternating path} & \multirow{4}{*}{monotone cycle} & ordered & conjectured \[4, Conjecture 4.13\] & \(\lceil(a-1)(b-\frac{1}{2})\rceil\) for \(a\ge 2\), \(b\ge 3\) \\
 & & reflective & conjectured (Conjecture 4.7) & \(\lfloor(a-1)(b-\frac{1}{2})\rfloor\) for \(a,b\ge 3\) \\
 & & cyclic & conjectured \[4, Conjecture 4.14\] & 1+(_a_-1)(_b_-1) for \(a\in\mathbb{N}\), \(b\ge 2\) \\
 & & dihedral & conjectured (Conjecture 4.8) & 1+(_a_-1)(_b_-1) for \(a\in\mathbb{N}\), \(b\ge 2\) \\
\multirow{4}{*}{alternating path} & \multirow{4}{*}{complete graph} & ordered & conjectured \[4, Conjecture 4.22\] & \(\lceil\frac{3ab-5b}{2}\rceil-2a+5\) for \(a\ge 3\), \(b\ge 2\) \\
 & & reflective & -- & -- \\
 & & cyclic & conjectured \[4, Conjecture 4.23\] & 1+(_a_-1)(_b_-1) for \(a,b\in\mathbb{N}\) \\
 & & dihedral & conjectured (Conjecture 4.9) & 1+(_a_-1)(_b_-1) for \(a,b\in\mathbb{N}\) \\
\multirow{4}{*}{alternating path} & \multirow{4}{*}{nested matching} & ordered & -- & -- \\
 & & reflective & -- & -- \\
 & & cyclic & -- & -- \\
 & & dihedral & -- & -- \\
\multirow{4}{*}{start-central star} & \multirow{4}{*}{start-central star} & ordered & solved \[3, Observation 12\] & _a+b_-2 for \(a,b\ge 2\) \\
 & & reflective & solved (Proposition 4.10) & _a+b_-2 for \(a,b\ge 2\) \\
 & & cyclic & solved \[8\] & _a+b_-2-(_ab_mod2) for \(a,b\ge 2\) \\
\multirow{4}{*}{start-central star} & \multirow{4}{*}{monotone path} & ordered & solved \[4, Corollary 4.4\] & 1+(_a_-1)(_b_-1) for \(a,b\in\mathbb{N}\) \\
 & & reflective & solved (Corollary 4.3) & 1+(_a_-1)(_b_-1) for \(a,b\in\mathbb{N}\) \\
 & & cyclic & conjectured \[4, Conjecture 4.16\] & 1+(_a_-1)(_b_-2) for \(a\ge 3\), \(b\ge 4\) \\
\multirow{4}{*}{start-central star} & \multirow{4}{*}{monotone cycle} & ordered & solved \[4, Theorem 4.18\] & 1+(_a_-1)(_b_-1) for \(a\in\mathbb{N}\), \(b\ge 2\) \\
 & & reflective & solved (Proposition 4.12) & 1+(_a_-1)(_b_-1) for \(a\in\mathbb{N}\), \(b\ge 2\) \\
 & & cyclic & solved \[4, Corollary 4.19\] & 1+(_a_-1)(_b_-1) for \(a\in\mathbb{N}\), \(b\ge 2\) \\
\multirow{4}{*}{start-central star} & \multirow{4}{*}{complete graph} & ordered & solved \[4, Theorem 4.24\] & 1+(_a_-1)(_b_-1) for \(a,b\in\mathbb{N}\) \\
 & & reflective & solved (Corollary 4.16) & 1+(_a_-1)(_b_-1) for \(a,b\in\mathbb{N}\) \\
 & & cyclic & solved \[9\] & 1+(_a_-1)(_b_-1) for \(a,b\in\mathbb{N}\) \\
\multirow{4}{*}{start-central star} & \multirow{4}{*}{nested matching} & ordered & -- & -- \\
 & & reflective & -- & -- \\
 & & cyclic & conjectured \[4, Conjecture 4.33\] & \(\left\{\begin{array}{ c c }
a+b-3, & \text{if}2\nmid a\text{and}4|b, \\
a+b-2, & \text{otherwise}
\end{array}\right.\text{for}a\ge 2\text{and even}b\ge 2\text{} \\
a+b-3, & \text{otherwise}
\end{array}\right.\) \\
\end{tabular}

2: The known and conjectured formulas for the ordered, reflective, cyclic and dihedral Ramsey numbers of alternating paths and start-central stars versus alternating paths, start-central stars, monotone paths, monotone cycles, complete graphs and nested matchings. The dihedral Ramsey numbers of start-central stars versus start- central stars, monotone paths, monotone cycles, complete graphs and nested matchings are omitted, since they coincide with the corresponding cyclic Ramsey numbers. In the  column, _a_ and _b_ denote the orders of the first and second graph arguments, respectively. Entries marked "--" indicate that no general formula is currently known or conjectured.

