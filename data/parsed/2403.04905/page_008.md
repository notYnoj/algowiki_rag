**Step 3: Applying the separator theorem for string graphs.** Lee’s separator theorem for string graphs [18] states that any string graph on _m_ edges admits a balanced separator of size \(O(\sqrt{m})\). It is well known (and easy to show) that any intersection graph of path-connected sets in the plane is a string graph. Hence, we can apply Lee’s result to \(\mathcal{G}^\times(\mathcal{D}_1)\) which, as we have just shown, has \(O(n^\frac{3+\alpha}{2})\) edges. Thus, \(\mathcal{G}^\times(\mathcal{D}_1)\) has a separator of size \(O(n^\frac{3+\alpha}{4})\). If we add the vertices of this separator as singletons to our clique-based separator S then, together with the cliques added in Step 1, we obtain a separator consisting of \(O(n^\frac{3+\alpha}{4}+n^{1-\alpha})\) cliques. Picking \(\alpha=1/5\), and anticipating the extension to the case where \(\Pi(\mathcal{D}_1)\) is not a proper path set, we obtain the following result.

\(\blacktriangleright\) **Proposition 2.3.** _Let d be a well-behaved shortest-path metric on a closed and path- connected subset_ \(F\subset\mathbb{R}^2\) _and let_ D _be a set of n geodesic disks with respect to the metric d. Then_ \(\mathcal{G}^\times(\mathcal{D})\) _has a balanced clique-based separator consisting of O(n_<sup>4/5</sup>) _cliques._

## 2.2 Bootstrapping

We now describe a bootstrapping mechanism to improve the size of our clique-based separator. We first explain how to apply the mechanism once, to obtain a clique-based separator consisting of _O(n_<sup>10/13</sup>) cliques. Then we apply the method repeatedly to obtain a separator consisting of \(O(n^{3/4+\varepsilon})\) cliques.

**The basic bootstrapping mechanism.** The idea of our bootstrapping mechanism is as follows. After reducing the ply in Step 1, we argued that the number of remaining edges is subquadratic. We can actually reduce the number of edges and crossings even further, by reducing the maximum degree of the graph \(\mathcal{G}^\times(\mathcal{D}_1)\). To this end, after reducing the ply, we remove from \(\mathcal{G}^\times(\mathcal{D}_1)\) all vertices _D<sub>i</sub>_ such that \(deg(D_i)\unknown n^\beta\), for some constant \(0<\beta<1\) whose value will be determined later. All these high degree vertices are placed in our clique-based separator as singletons. If _h_ is the number of these vertices, then \(h\cdot n^\beta\unknown 2|E_1|\) and so \(h=O(n^\frac{3+\alpha}{2}-\beta)\). We denote the resulting graph by \(\mathcal{G}^\times(\mathcal{D}_2)=(\mathcal{D}_2,E_2)\) and let E<sub>2</sub> be the half-edges corresponding to the edges in _E_<sub>2</sub>.

To minimize the number of cliques in our separator, the constants \(\alpha\) and \(\beta\) should be chosen to satisfy the equation

\(\frac{3+\alpha}{2}-\beta=1-\alpha.\) (2)

Next, we show that after reducing the maximum degree, the number of edges has also decreased.

\(\blacktriangleright\) **Lemma 2.4.** _For the graph_ \(\mathcal{G}^\times(\mathcal{D}_2)\) _defined as above, it holds that_ \(|E_2|\unknown\sqrt{\frac{4}{c}}n^{1+\frac{\alpha+\beta}{2}}\) _, where c is the constant appearing in the Crossing Lemma._

**Proof.** The proof is essentially the same as the proof of Lemma 2.2, so we only mention the key differences. We assume for a contradiction that \(|E_2|>\sqrt{\frac{4}{c}}n^{1+\frac{\alpha+\beta}{2}}\) . Then, we lower bound the number of crossings (denoted now by X<sub>2</sub>) as

\(|\mathcal{X}_2|\unknown c\frac{|E_2|^3}{n^2}>2|\mathcal{E}_2|n^{\alpha+\beta}.\)

We then proceed with the same labeling procedure as in Step 2 in order to lower bound the total ply _K_<sub>2</sub> of all crossings. A key difference is that now we only need to divide by \(2n^\beta\),

