Besides, \((loglogn)^2\ge log^2k\). Thus,

\(logr\le\frac{\gamma\cdot 2klog(12(\Delta+1)N)}{log^2k}\le\frac{\gamma\cdot 24(\Delta+1)klogN}{log^2k}<\gamma\cdot 48(\Delta+1)\cdot\frac{N}{log^{c+1}N\cdot log^2k}\)<br>
\(\le\gamma\cdot 48(\Delta+1)\cdot\frac{N}{log^{c+1}N\cdot 0.25log^2N}=\gamma\cdot 192(\Delta+1)\cdot\frac{N}{log^{c+3}N},\)

where the penultimate inequality holds because of Item 5, the last inequality uses Item 3, whereas the other inequalities always hold.

On the other hand,

\(klog\left(1+\frac{1-\beta}{\beta+3(\Delta+1)\lceil log(3N)\rceil}\right)\ge\frac{k\cdot 0.8(1-\beta)}{\beta+3(\Delta+1)\lceil log(3N)\rceil}\ge\frac{k\cdot 0.8(1-\beta)}{4(\beta+3(\Delta+1))logN}\)<br>
\(\ge\frac{0.8(1-\beta)}{4(\beta+3(\Delta+1))}\cdot\frac{N}{log^{c+3}N},\)

where the first inequality holds because of Item 2, and the second uses Item 1.

And we conclude since \(\gamma=\frac{0.8(1-\beta)}{4(\beta+3(\Delta+1))}\cdot\frac{1}{192(\Delta+1)}\). \(\triangleleft\)

This concludes the proof since, under the promise, _H_ is 3-colorable if and only if A uses at most \(r\cdot 3^k\) colors. \(\blacktriangleleft\)

## 5 _k_-Independent Set in graphs of bounded low-radius merge-width

In this section, we reduce Grid Tiling to _k_-Independent Set, to show the W\[1\]-hardness of the latter problem in graphs of bounded low-radius merge-width. The reduction is inspired by the one of Dreier, Mählmann, and Siebertz. \[16, Thm. 2\] and we use their notations. The Grid Tiling problem was introduced in \[24\]. Given some integers \(k,n\in\mathbb{N}\) and a collection S of _tile_ subsets \(S_\pi\subseteq[n]^2\) for each _grid cell_ \(\pi\in[k]^2\), the goal is to decide whether there exists a selection of tiles \(s(\pi)\in S_\pi\) for all \(\pi\in[k]^2\) such that:

The tiles \(s(\pi)\) and \(s(\pi_\blacktriangleright)\) have the same first component for all cells \(\pi=(i,j)\in[k-1]\times[k]\) and \(\pi_\blacktriangleright:=(i+1,j)\); and

The tiles \(s(\pi)\) and \(s(\pi_\triangledown)\) have the same second component for all cells \(\pi=(i,j)\in[k]\times[k-1]\) and \(\pi_\triangledown:=(i,j+1)\).

It is known that Grid Tiling is W\[1\]-hard parameterized by the grid size _k_ and unless the ETH fails it has no _f(k)m_<sup>_o(k_)</sup>-time algorithm for any computable function _f_ \[13, Thm. 14.28\].

\(\blacktriangleright\) **Theorem 3.** _k-Independent Set is W\[1\]-hard in graphs of bounded mw_<sub>_o(k_)</sub>.

**Proof.** Let \(r\ge 3\) be an odd integer. For a Grid Tiling instance (S_,k,n_), we will construct a graph \(G_\mathcal{S}^r\) with \(mw_{r-1}(G_\mathcal{S}^r)\le 4r-3\). For each grid cell \(\pi\in[k]^2\), we construct a cell gadget \(C_\pi^r\), illustrated in Figure 1. The cell gadget \(C_\pi^r\) consists of a horizontal path and a vertical path of _r_ cliques:

\(B_\pi^{h_1},B_\pi^{h_2},\dots,B_\pi^{h_r}\) where \(B_\pi^{h_i}\) has vertex set \(\{b(\tau,h_i,\pi)|\tau\in S_\pi\}\); and

\(B_\pi^{v_1},B_\pi^{v_2}\dots,B_\pi^{v_r}\) where \(B_\pi^{v_i}\) has vertex set \(\{b(\tau,v_i,\pi)|\tau\in S_\pi\}\).

They cross in the middle, i.e., \(B_\pi^{h_m}=B_\pi^{v_m}\) for \(m=\frac{r+1}{2}\) .

We then add a co-matching between any two consecutive blocks. Formally, for every \(\tau,\tau'\in S_\pi\) with \(\tau\neq\tau'\), and every \(i\in[r-1]\), we add an edge

\(\text{between}b(\tau,h_i,\pi)\text{and}b(\tau',h_{i+1},\pi)\text{; and}\)

