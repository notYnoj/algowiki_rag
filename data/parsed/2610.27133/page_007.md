Therefore, if \(\alpha(H)=4\), we need an additional analysis. For a given hypergraph _H_=(_V,_E), define a simple graph _G<sub>H</sub>_=(_V,E_), where

\(E=\{uv:u,v\in V,\{u,v\}\cap e\neq\emptyset\text{for all}e\in\mathcal{E}\}.\)

**Proposition 9** (Matching reduction)**.** _Let H be a hypergraph with_ \(\alpha(H)=4\) _and let_ \(\nu\) _be the size of a maximum matching of G<sub>H</sub>. Then_ \(\chi_B=\beta\) _if and only if_ \(|V|+\nu\le 3\chi_P-4\).

_Proof._ Since \(\alpha=4\) and \(\beta=\chi_P-2\), then \(\chi_B\in\{\chi_P-2,\chi_P-1\}\). Consider any bipanchromatic _k_-coloring. Each color occurring exactly twice determines an edge of _G<sub>H</sub>_. These edges are vertex-disjoint, so they form a matching in _G<sub>H</sub>_. Therefore, we have at most \(\nu\) colors used exactly two times. Consequently, \(|V|\ge 2\nu+3(k-\nu)\), so \(k\le\chi_B\le\lfloor(|V|+\nu)/3\rfloor\).

If \(|V|+\nu\le 3\chi_P-4\), then \(\chi_B\le\chi_P-2=\beta\), and therefore \(\epsilon=0\).

For the converse, assume \(\epsilon=0\) and choose a panchromatic \(\chi_P\)-coloring attaining \(\alpha=4\).

If some color _C_ occurs at least four times, we can recolor all vertices of color _C_ with the four colors that are used only once. This produces a bipanchromatic coloring with \(\chi_P-1\) colors, contradicting \(\epsilon=0\).

Therefore, every color is used at most three times. Let C_<sub>k</sub>_ denote the number of colors used exactly _k_ times. Then, \(\chi_P=4+\mathcal{C}_2+\mathcal{C}_3\), and |_V_|=4+2C<sub>2</sub>+3C<sub>3</sub>.

The pairs corresponding to the C<sub>2</sub> color classes must form a maximum matching in _G<sub>H</sub>_\[_V_\\_S_\], where _S_ is the set of vertices receiving the four unique colors. Otherwise, an augmenting path would yield a larger matching, whose pairs could be assigned distinct colors in a panchromatic coloring of _H_ (the pairs intersect every hyperedge). The endpoints _u_ and _v_ of such an augmenting path belong to three-vertex color classes C<sub>3</sub>. Reassign the colors so that each matching pair forms its own color class. If _u_ and _v_ belong to the same three-vertex color class, assign the color of one of the four uniquely colored vertices to the third vertex of that class. This produces a \(\chi_P\)-coloring with three uniquely colored vertices, a contradiction. If _u_ and _v_ belong to different three-vertex color classes, assign the four unique colors to their other four vertices. This produces a bipanchromatic coloring with \(\chi_P-1\) colors, again a contradiction, since \(\chi_B=\beta=\chi_P-2\). Thus, \(\nu\le\mathcal{C}_2+4\), and thus \(|V|+\nu\le(4+2\mathcal{C}_2+3\mathcal{C}_3)+(\mathcal{C}_2+4)=3\chi_P-4\).

Given _H_ and promises \(\chi_P\) and \(\alpha\), \(\epsilon=0\) (or \(\chi_B=\beta\)) is decidable in polynomial time.

## 7 Order-aware improved bounds

In this section, we introduce another lower bound _L_ for the bipanchromatic number, based on our construction, and show that \(\beta\le L\le\chi_B\). Thus, _L_ improves the lower bound \(\beta\).

Consider a hypergraph _H_=(_V,_E) with \(|V|\ge 2\) and \(\alpha>0\). If \(\alpha\ge|V|/2\), then \(\chi_B=\lfloor|V|/2\rfloor\). Indeed, the unique vertices can be paired with the non-unique vertices, and any remaining vertices can be assigned colors so that every color used occurs at least twice. For the sunflower S_<sub>n</sub>_ (see Theorem 1), where \(n\ge 3\), we have \(\alpha=|V|/2\) and \(\chi_B=|V|/2\), while \(\chi_B/\beta\rightarrow 2\) as \(n\rightarrow\infty\).

We now consider the case \(0<\alpha<|V|/2\) and choose a panchromatic \(\chi_P\)-coloring of _H_ with \(\alpha\) unique colors. Let \(m=\chi_P-\alpha\) denote the number of colors used more than once. Suppose that color _i_ is used on _c<sub>i</sub>_ vertices, where

\(c_1\ge c_2\ge\cdots\ge c_m>1.\)

Observe that \(c_1+c_2+\cdots+c_m=|V|-\alpha\).

Let \(d\in[m]\) be the smallest index such that \(c_1+c_2+\cdots+c_d\ge\alpha\). Such an integer exists because \(|V|-\alpha>\alpha\).

