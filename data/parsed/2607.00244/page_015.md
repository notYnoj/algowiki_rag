that \(dist_{F_3}(x,y)\ge 2r\). Therefore, for any \(v\in V(G)\), the set \(\mathrm{Ball}_{F_3}^{r-1}(v)\) intersects at most one layer from each border block. Since each layer of a border block and each interior block is in one part of P<sub>2</sub>, it follows that for any \(v\in V(G)\), we have \(|\mathrm{Ball}_{F_3}^{r-1}(v)/\mathcal{P}_2|\le 4r-3\).

Finally, for (P<sub>3</sub>_,F_<sub>4</sub>), the edges of _G_ are only between consecutive blocks inside a cell gadget, or between adjacent border blocks. Since any block of _G_ is in one part of P<sub>3</sub>, for any \(v\in V(G)\), we have \(|\mathrm{Ball}_{F_4}^{r-1}(v)/\mathcal{P}_3|\le 4r-3\). This concludes the proof.

These claims readily give that _k_-IS is W[1]-hard on graphs of bounded radius-_r_ merge- width, where _r_ is a fixed constant. However, we can extract more. Fix two computable functions _f(x_)=_o(x_) and \(g(x)\ge 4x\). Then we say that _G_ has (_f,g,k)-merge-width_ if \(\mathrm{mw}_{f(k)}(G)\le g(k)\).

\(\vartriangleright\) Claim 17. _k_-Independent Set on graphs with (_f,g,k_)-merge-width is W[1]-hard.

Proof. We design an FPT reduction from Grid Tiling with parameter _q_ to _k_-Independent Set with _k_:=(2_r_-1)_q_<sup>2</sup>, where _r_:=_r(q_) is the smallest odd integer at least equal to 3 such that

\(f((2r-1)q^2)\le r-1.\)

This integer exists since _f(x_)=_o(x_), and is computable since _f_ is computable.

Let (S_,q,n_) be an instance of Grid Tiling. Computing \(G:=G_\mathcal{S}^r\) can be done in time \(\mathcal{O}(\|G\|)=\mathcal{O}(r^2q^4\cdot n^4)\). This is an FPT reduction in parameter _q_ since _r_ depends only on _q_. Besides, _G_ has (_f,g,k_)-merge-width, since

\(\mathrm{mw}_{f(k)}(G)=\mathrm{mw}_{f((2r-1)q^2)}(G)\le\mathrm{mw}_{r-1}(G)\le 4r-3\le 4(2r-1)q^2\le g((2r-1)q^2)=g(k).\)

Where the first inequality comes from monotonicity of merge-width with respect to the radius, the second is due to Claim 16, and the last, by the assumption on _g_. We conclude by Claim 15.

In particular, for every _r=o(k_), _k_-IS is W[1]-hard on graphs of bounded mw_<sub>r</sub>_.

## 6 _k_-Dominating Set in graphs of bounded low-radius merge-width

In this section, we adapt the reduction from the previous section to show the W[1]-hardness of _k_-Dominating Set in graphs of low-radius merge-width. The main difference is how the selection of copies of the same tile in a cell gadget is enforced. First, instead of cliques, the blocks will be independent sets. Then, we will achieve the vertex selection by inserting between every pair of consecutive blocks _B_ and \(B'\), an additional block _A_ such that there is a co-matching between _B_ and _A_, and a matching between _A_ and \(B'\). The only way to dominate this new block _A_ with two vertices will be to pick copies of the same tile in _B_ and \(B'\). A similar construction can be done to enforce that selected tiles in adjacent cells agree on their corresponding component (see Figure 2).

\(\blacktriangleright\) **Theorem 4.** _k-Dominating Set is W[1]-hard in graphs of bounded mw_<sub>_o(k_)</sub>.

**Proof.** Let _r\>_3 be an odd integer, for a Grid Tiling instance (S_,k,n_) we will construct a graph \(G_\mathcal{S}^r\) with \(\mathrm{mw}_{2r-2}(G_\mathcal{S}^r)=\mathcal{O}(r)\). For each grid cell \(\pi\in[k]^2\), we construct a cell gadget \(C_\pi^r\). The cell gadget \(C_\pi^r\) consists of a horizontal path and a vertical path of 2_r_-1 edgeless graphs:

\(B_\pi^{h_1},B_\pi^{h_2},\dots,B_\pi^{h_{2r-1}}\) where \(B_\pi^{h_i}\) have vertex set \(\{b(\tau,h_i,\pi)|\tau\in S_\pi\}\); and

