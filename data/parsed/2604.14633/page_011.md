time limit of \((m+n|f|)\cdot n^{o(1)}\) where |_f_| is the current flow value, and terminate the algorithm if the limit is exceeded. This completes the proof of our main result (Theorem 1).

To obtain Corollary 2, we use the fact that \(\sqrt{n}\) rounds of Dinic’s blocking flow algorithm \[Din70\] reduces the maximum flow of the residual graph to at most \(m/\sqrt{n}\) \[Kar73, ET75\]. Computing the blocking flows takes time \(O(m\sqrt{n})\), and applying Theorem 1 with \(F\le m/\sqrt{n}\) on the residual graph takes time _mn_<sup>1/2+_o_(1)</sup>.

## 4 Dynamic Sparsification

In this section, we present our dynamic sparsifier data structure to establish Theorem 10, restated below together with the definition.

**Definition 9** (Dynamic sparsifier with quality _q_)**.** _For a weighted directed graph H_=(_V,E,_**u**) _where_ \(\mathbf{u}\in\mathbb{R}^E\) _and_ \(\mathbf{u}(e)\in[1/U,U]\) _for_ \(\mathrm{log}U=\widetilde{O}(1)\)_, a dynamic sparsifier with quality q supports the following operations:_

• InsertArc(_e),_DeleteArc(_e): inserts/deletes the arc e with weight_ **u**(_e)._<tbc>

• Sparsifier\((\beta)\)_: given_ \(\beta\ge 1\)_, returns a subgraph_ \(\widetilde{H}\subseteq H\) _on at most_ \(q\cdot\beta n\) _arcs such that with high probability, any cut_ \(S\subseteq V\) _with_ \(\mathbf{u}(\partial_H^+S)\ge\frac{1}{\beta}\mathbf{u}(\partial_HS)\) _has at least one sampled out-arc, i.e.,_ \(\partial_\widetilde{H}^+S\neq\emptyset\).

**Theorem 10.** _There is a randomized dynamic sparsifier data structure with quality q=n_<sup>_o_(1)</sup>log_U such that each call to_ InsertArc(_e),_DeleteArc(_e_) _is processed in amortized time n_<sup>_o_(1)</sup>log_U, and each call to_ Sparsifier\((\beta)\) _takes time_ \(O(q\beta n\mathrm{log}U)\).

### 4.1 Reduction to Unweighted Graphs

The dynamic algorithm first reduces to the case of unweighted graphs by bucketing the arcs and running an unweighted dynamic sparsifier with quality _n_<sup>_o_(1)</sup> on each bucket. More precisely, for each integer _i_, let \(H_i\subseteq H\) be the subgraph of all arcs with weight in the range \[2_<sup>i</sup>,_2<sup>_i_+1</sup>). Since \(\mathbf{u}(e)\in[1/U,U]\), there are only _O_(log_U_) non-empty subgraphs _H<sub>i</sub>_. For each _H<sub>i</sub>_, treated as a dynamic _unweighted_ graph, initialize a dynamic sparsifier data structure where all arcs have weight 1. Finally, on each query to Sparsifier\((\beta)\), the algorithm calls Sparsifier\((2\beta)\) on the data structure for each _H<sub>i</sub>_, obtaining a subgraph \(\widetilde{H}_i\subseteq H_i\). The algorithm outputs the union of the subgraphs \(\widetilde{H}_i\) as the final sparsifier \(\widetilde{H}\), which has \(q\cdot\beta n\cdot O(\mathrm{log}U)\) arcs.

To prove correctness of this reduction, consider a cut \(S\subseteq V\) with \(\mathbf{u}(\partial_H^+S)\ge\frac{1}{\beta}\mathbf{u}(\partial_HS)\), rewritten as \(\beta\cdot\mathbf{u}(\partial_H^+S)-\mathbf{u}(\partial_HS)\ge 0\). By our bucketing scheme, we can bound \(\mathbf{u}(\partial_H^+S)\) and \(\mathbf{u}(\partial_HS)\) by<tbc>

\(\mathbf{u}(\partial_H^+S)\le\sum_i2^{i+1}\cdot|\partial_{H_i}^+S|\text{and}\mathbf{u}(\partial_HS)\ge\sum_i2^i\cdot|\partial_{H_i}S|,\)

<tbc>so

\(\sum_i2^i\cdot(2\beta\cdot|\partial_{H_i}^+S|-|\partial_{H_i}S|)=\beta\cdot\sum_i2^{i+1}\cdot|\partial_{H_i}^+S|-\sum_i2^i\cdot|\partial_{H_i}S|\ge\beta\cdot\mathbf{u}(\partial_H^+S)-\mathbf{u}(\partial_HS)\ge 0.\)

In particular, there exists an _i_ with \(2\beta\cdot|\partial_{H_i}^+S|-|\partial_{H_i}S|\ge 0\), or equivalently \(|\partial_{H_i}^+S|\ge\frac{1}{2\beta}|\partial_{H_i}S|\). Assuming that the guarantee of Sparsifier\((2\beta)\) on _H<sub>i</sub>_ holds, we conclude that \(\partial_{\widetilde{H}_i}^+S\neq\emptyset\) as well as \(\partial_\widetilde{H}^+S\neq\emptyset\), completing the reduction.

