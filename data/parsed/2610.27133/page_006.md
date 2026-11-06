For \(3\le\alpha<\chi_P\), the construction in Proposition 7 has exactly \(max\{2\chi_P-\alpha,2\chi_B\}\) vertices. In the remaining cases, Lemma 4(i) gives \(\chi_B=\beta\). Take two sets of size \(\chi_P\) intersecting in \(\alpha\) vertices, use them as hyperedges, and take their union as the vertex set. When \(\alpha=\chi_P\), this gives just one hyperedge. The panchromatic number is \(\chi_P\), and every maximum panchromatic coloring has unique colors precisely on the \(\alpha\) common vertices. The same lemma therefore gives bipanchromatic number \(\beta\). This construction has \(2\chi_P-\alpha=max\{2\chi_P-\alpha,2\beta\}\) vertices, attaining the lower bound.

## 6 Characterization of equality

Here we discuss conditions characterizing \(\chi_B=\beta\) (equivalently \(\epsilon=0\)) for an arbitrary hypergraph.

**Proposition 8** (Zero excess characterization)**.** _Assume that H is a hypergraph with_ \(\alpha\in\mathbb{N}\backslash\{1,2,4\}\)_. Then_ \(\chi_B=\beta\) _if and only if_ \(\beta=\left\lfloor\frac{|V|}{2}\right\rfloor\).

_Proof._ Assume that \(\chi_B=\beta\) and consider a \((\chi_P,\alpha)\)-coloring of _H_. Let _n_=3 if \(\alpha\) is odd and _n_=4 otherwise. If a color _C_ occurs at least _n_ times, recolor all vertices of color _C_ with _n_ existing unique colors, using each at least once. Merge the remaining \(\alpha-n\) uniquely colored vertices in pairs. This yields a \(\beta+1\) bipanchromatic coloring of _H_, contradicting \(\chi_B=\beta\). Therefore, if \(\alpha\) is odd, then every color occurs at most twice, and if \(\alpha\) is even, every color occurs at most thrice. If two distinct colors each occur three times, recolor their six vertices with six colors that are used only once (since \(\alpha\ge 6\)), and then merge the remaining uniquely colored vertices in pairs, again obtaining a coloring with \(\beta+1\) colors. Thus, at most one color occurs thrice, so \(|V|\in\{2\chi_P-\alpha,2\chi_P-\alpha+1\}\), and \(\lfloor|V|/2\rfloor=\beta\).

The converse follows from the definition.

For a hypergraph _H_ with \(\alpha=4\), the equality \(\chi_B=\beta\) requires further consideration. Consider mutually disjoint sets |_S_|=4, {_v,a,b,x_<sub>0</sub>_,x_<sub>1</sub>_,x_<sub>2</sub>} and |_P<sub>i</sub>_|=2 for _i_=1,2,3. We define two hypergraphs _H_<sub>-</sub> and _H_<sub>+</sub> whose hyperedge sets are, respectively

\(\mathcal{E}_-=\{S\sqcup P_i:i\in[3]\}\text{and}\mathcal{E}_+=\{S\sqcup\{v,x_0\},S\sqcup\{v,x_1\},S\sqcup\{v,x_2\},S\sqcup\{a,b\}\}.\)

Notice that |_V(H_<sub>-</sub>)|=|_V(H_<sub>+</sub>)|=10, \(\chi_P(H_-)=\chi_P(H_+)=6\), and \(\alpha(H_-)=\alpha(H_+)=4\). However, \(\beta=\chi_B(H_-)=4<|V|/2\) and \(\beta<\chi_B(H_+)=5=|V|/2\).

u
x0
e0
u
x0
e0
u
x0
e0
S1
S2
S1
S2
X1
e1
S1
S2
X1
e1
S
S3
S4
S
S3
S4
S
S3
S4
S5
S6
S5
S6
X2
e2
X2
e2
S5
S6
w
X3
e3
w
X3
e3
w
X3
e3
w
X3
e3
10 vertices, 2 hyperedges
12 vertices, 4 hyperedges
6 pairs, each with its own color

(a) Starting hypergraph

(b) Panchromatic 8-coloring

(c) Bipanchromatic 6-coloring

Figure 2: Proposition 7 at (_p,a,b_)=(8,6,6) and _n_=2. _S_={_s_<sub>1</sub>_,...,s_<sub>6</sub>}, _U_={_u_} and _W_={_w_}. The contours represent the hyperedges \(e_i=S\sqcup\{u,x_i\}\), \(e_3=S\sqcup\{w,x_3\}\). (a) The initial construction. (b) Adding new vertices and hyperedges, and 8-coloring. (c) Bipanchromatic coloring by pairing.

