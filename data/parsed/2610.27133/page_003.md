<tbc>_Proof._ We can color each _s<sub>i</sub>_ by _i_, and all _p<sub>i</sub>_ by _n_+1. This is a panchromatic coloring (Figure 1(a)), and \(\chi_P=n+1\). Any panchromatic (_n_+1)-coloring of S_<sub>n</sub>_ uses each color only once per hyperedge \(S\sqcup\{p_i\}\). The colors on _S_ have to be unique, thus \(\alpha=|S|=n\) and every _p<sub>i</sub>_ has the same color. Merging the unique colors gives \(n+1-\left\lceil\frac{n}{2}\right\rceil\) colors (Figure 1(b)). However, we can color each {_s<sub>i</sub>,p<sub>i</sub>_} distinctly (Figure 1(c)). Each hyperedge then contains _n_ colors, none of which is unique. Notice that \(\chi_B\le|V|/2=n\), thus \(\chi_B=n\) and \(\epsilon=\left\lceil\frac{n}{2}\right\rceil-1\).

Thus, the gap between \(\chi_B\) and the quantity in \[1, Conjecture 1\] is unbounded. In particular, adding any fixed constant to the right-hand side cannot make the conjecture valid in general.

Figure 1(a) shows a \(\chi_P\)-coloring of S_<sub>n</sub>_ attaining \(\alpha\). Figure 1(b) shows a bipanchromatic coloring obtained by merging unique colors. Figure 1(c) shows a bipanchromatic coloring with more colors.

For excess _n_, the three-hyperedge construction in \[5, Proposition 1\] uses at least 12_n_ vertices. The following construction uses 12_n_-6. It is obtained by enlarging S<sub>3</sub>. Replace each vertex by a group of 2_n_-1 vertices and each hyperedge by the union of the groups corresponding to its vertices.

**Proposition 2** (Three-hyperedge counterexamples)**.** _For_ \(n\in\mathbb{N}\)_, let S,P_<sub>1</sub>_,P_<sub>2</sub>_,P_<sub>3</sub> _be pairwise disjoint sets with_ |_S_|=6_n_-3 _and_ |_P<sub>i</sub>_|=2_n_-1_. Let_ \(V=S\sqcup P_1\sqcup P_2\sqcup P_3\), \(e_i=S\sqcup P_i\)_, and_ \(\Delta_n=(V,\{e_1,e_2,e_3\})\)_. The excess_ \(\epsilon(\Delta_n)\) _is equal to n._

_Proof._ Color the vertices of _S_ with distinct colors. Using |_P<sub>i</sub>_| additional distinct colors, color the vertices of each _P<sub>i</sub>_ with distinct colors. This is panchromatic, so \(\chi_P=|e_i|=8n-4\). Any \(\chi_P\)-coloring of \(\Delta_n\) uses each color only once per hyperedge \(S\sqcup P_i\), so only the colors on _S_ are unique, thus \(\alpha_{\chi_P}=|S|\). Now color the vertices of _S_ with distinct colors and repeat each such color on exactly one vertex in \(P_1\cup P_2\cup P_3\). This gives \(\chi_B=|S|\). Thus, \(\epsilon(\Delta_n)=(6n-3)-\left(8n-4-\left\lceil\frac{6n-3}{2}\right\rceil\right)=n\).

## 4 Bounds and minimality

Consider an arbitrary hypergraph _H_ with panchromatic number \(\chi_P\). For any integer \(k\le\chi_P\), let \(\beta_k=k-\left\lceil\frac{\alpha_k}{2}\right\rceil\). In particular, let \(\beta=\beta_{\chi_P}\). \[1, Conjecture 1\] asserts that \(\chi_B=\beta\), but this does not hold in general. However, for any _k_-panchromatic coloring of _H_ attaining \(\alpha_k\), the pairing argument used in \[1\] produces a bipanchromatic coloring with \(\beta_k\) colors. Thus, for every \(k\le\chi_P\) we obtain a lower bound for \(\chi_B\), and the largest of these bounds equals \(\chi_B\).

e1
e1
e1
p1
p1
p1
S1
S2
S1
S1
Sn
S2
Sn
S2
Sn
S3
S4
p2
Pn
p2
Pn
p2
Pn
e2
e2
en
en
e2
en
XP = n + 1, a n+1 = n
1+ 2
colors
XB = n

(a) \(\chi_P\)-coloring

(b) Merging-based

(c) Bipanchromatic \(\chi_B\)-coloring

Figure 1: S_<sub>n</sub>_ colorings. Hyperedges are \(e_i=S\cup\{p_i\}\). (a) Unique colors on _S_ and one color on _P_ give _n_+1 colors. (b) Merging on _S_ gives \(1+\left\lfloor\frac{n}{2}\right\rfloor\) colors. (c) Each {_s<sub>i</sub>,p<sub>i</sub>_} has its own color, giving _n_ colors.

