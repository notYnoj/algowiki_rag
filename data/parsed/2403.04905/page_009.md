<tbc>since \(n^\beta\) is the maximum degree of \(\mathcal{G}^\times(\mathcal{D}_2)\):

\(K_2\unknown\frac{1}{2n^\beta}\sum_{x\in\mathcal{X}_2}min\{\lambda_1(x),\lambda_2(x)\}.\)

To get an estimate for _K_<sub>2</sub>, we remove from every half-edge, its first \(n^{\alpha+\beta}\) crossings. In this way there are at least \(|\mathcal{X}_2|-|\mathcal{E}_2|n^{\alpha+\beta}\) crossings remaining, each having a minimum label larger than \(n^{\alpha+\beta}\). Therefore

\(K_2>\frac{\left(|\mathcal{X}_2|-|\mathcal{E}_2|n^{\alpha+\beta}\right)n^{\alpha+\beta}}{2n^\beta}>\frac{|\mathcal{X}_2|}{4}n^\alpha\)

so we again get a contradiction, since there has to exist a crossing with ply at least \(\frac{1}{4}n^\alpha\). \(\blacktriangleleft\)

Step 3 now gives us that \(\mathcal{G}^\times(\mathcal{D}_2)\) has a separator of size \(O(n^\frac{2+\alpha+\beta}{4})\), whose vertices we add to our clique-based separator as singletons. In order to minimize the number of cliques in our separator, we now have the equation

\(\frac{2+\alpha+\beta}{4}=1-\alpha.\) (3)

Solving the system of Equations (2) and (3) gives \(\alpha=3/13\) and \(\beta=11/13\). This solution corresponds to a clique-based separator of size _O(n_<sup>10/13</sup>).

**Repeated bootstrapping.** The method we just described can be applied repeatedly: After reducing the maximum degree to \(n^\beta\), we showed that \(|E_2|=O(n^{1+\frac{\alpha+\beta}{2}})\). This allows us to reduce the maximum degree even more, by placing vertices of degree at least \(n^\gamma\) in the clique-based separator, for some \(\gamma<\beta\). If we repeat this process \(O(log(1/\varepsilon))\) times, we can obtain a clique-based separator of size \(O(n^{3/4+\varepsilon})\), as is shown in the following theorem.

\(\blacktriangleright\) **Theorem 2.5.** _Let d be a well-behaved shortest-path metric on a closed and path-connected subset_ \(F\subset\mathbb{R}^2\)_, and let_ D _be a set of n geodesic disks with respect to the metric d. Then_ \(\mathcal{G}^\times(\mathcal{D})\) _has a balanced clique-based separator consisting of_ \(O(n^\frac{3}{4}+\varepsilon)\) _cliques._

**Proof.** Let S denote our clique-based separator. As before, we start by reducing the ply of the subdivision, by finding points of ply at least \(\frac{n^{\alpha_1}}{4}\) , for some constant \(0<\alpha_1<1\), and placing the corresponding cliques into S. Our separator now has a size of \(O(n^{1-\alpha_1})\). Let D<sub>1</sub> denote the remaining set of disks and let \(\mathcal{G}^\times(\mathcal{D}_1)=(\mathcal{D}_1,E_1)\) denote the resulting subgraph after this step. Next, we repeatedly apply the following procedure for _i_=2_,...,k_: we reduce the maximum degree of \(\mathcal{G}^\times(\mathcal{D}_{i-1})\) to \(n^{\alpha_i}\) (for some positive constant \(\alpha_i<\alpha_{i-1}\)) by removing from \(\mathcal{G}^\times(\mathcal{D}_{i-1})\) vertices of degree at least \(n^{\alpha_i}\) and we place them in S as singletons. We denote by D_<sub>i</sub>_ the remaining set of disks and let \(\mathcal{G}^\times(\mathcal{D}_i)=(\mathcal{D}_i,E_i)\) be the resulting subgraph.

Lemma 2.4 gives us that \(|E_2|\unknown\sqrt{\frac{4}{c}}n^{1+\frac{\alpha_1+\alpha_2}{2}}\) , for _i_=2_,...,k_. In exactly the same way we can show that \(|E_i|\unknown\sqrt{\frac{4}{c}}n^{1+\frac{\alpha_1+\alpha_i}{2}}\) , for _i_=3_,...,n_.

During the above procedure, we have introduced _k_ unknown constants \(\alpha_1,\alpha_2,\dots,\alpha_k\) and so we need _k_ equations in order to calculate their values. To this end, let _h<sub>i</sub>_ denote the number of vertices of _G<sub>i</sub>_ with degree at least \(n^{\alpha_{i+1}}\), for _i_=1_,...,k_-1. Then, due to Lemma 2.2, we have \(h_1\cdot n^{\alpha_2}\unknown 2|E_1|\), and so

\(h_1=O(n^\frac{3+\alpha_1}{2}-\alpha_2).\)

