**Algorithm 5** `FMMLongMultiplicativeAPASP`(_G,k_)

**Input :** Unweighted, undirected graph _G_=(_V,E_) with _n_ vertices; approximation parameter _k_

**Output:** Distance estimate \(\hat{\delta}:U\times V\rightarrow\mathbb{Z}\) such that \(\delta(u,v)\le\hat{\delta}(u,v)\) for all \(u,v\in V\) and \(\hat{\delta}(u,v)\le 2\delta(u,v)\) whenever \(\delta(u,v)\ge k\)

52 Phase 0: Set up and Decompose Graph

53 \(\hat{\delta}(u,v)\leftarrow\left\{\begin{array}{ c c }
1 & (u,v)\in E \\
\infty & \mathrm{o}/\mathrm{w}
\end{array}\right.\)

54 Parameters _x,l_ chosen to minimize

\(t_\mathrm{max}=\mathrm{max}\left(\omega\left(1-\frac{k-2}{2(l-k+2)}x,1-x,1-\frac{k-4}{2(l-k+2)}x\right),2+\frac{x}{l-k+2},1.5+x\right)\)

55 _M_ chosen so that \(2+\frac{2}{3M-2}\le t_\mathrm{max}\)

56 \(l_0\leftarrow k-2\)

57 \(s_{l-i}\leftarrow n^\frac{i}{l-l_0}x\) for all \(1\le i\le l-l_0\)

58 \((D_{l_0},D_{l_0+1},\dots,D_l),(E_{l_0},E_{l_0+1},\dots,E_l),E^*\leftarrow\text{\textbf{Decompose}}(G,(s_{l_0+1},s_{l_0+2},\dots,s_{l-1}))\)

59 Phase 1: Compute Intermediate Distance Estimates on High Degree Paths

60 \(t_i\leftarrow\frac{n}{2^i}\) for all \(1\le i\le b-1=\lceil(1-x)\mathrm{log}n\rceil\)

61 (_C_<sub>1</sub>_,C_<sub>2</sub>_,...,C<sub>b</sub>),(F_<sub>1</sub>_,F_<sub>2</sub>_,...,F<sub>b</sub>),F_<sup>∗</sup>\(\leftarrow\text{\textbf{Decompose}}(G,(t_1,t_2,\dots,t_{b-1}))\)

62 for \(1\le i\le b\) do

63 \(\hat{\delta}\leftarrow\mathrm{min}\left(\hat{\delta},\text{\textbf{DominatingSetAPASP}}\left(G_i,D_{l-\frac{l_0}{2}},D_{l-\frac{l_0}{2}+1},C_i,M+2\right)\right)\) where _G<sub>i</sub>_=(_V,F<sub>i</sub>_).

64 Phase 2: Compute Distance Estimates

65 for \(l_0+1\le j\le l\) do

66 for \(w\in D_j\) do

67 \(G_{j,w}\leftarrow(V,E_j\cup E^*\cup(w\times V))\)

68 \(\hat{\delta}\leftarrow\text{\textbf{Dijkstra}}(G_{j,w},w,\hat{\delta})\)

69 \(\hat{\delta}\leftarrow\mathrm{min}\left(\hat{\delta},\text{\textbf{BK2APASP}}(G_{l_0+1})\right)\) where \(G_{l_0+1}\leftarrow(V,E_{l_0+1})\)

70 \(\hat{\delta}\leftarrow\mathrm{min}\left(\hat{\delta},\text{\textbf{DenseAPASP}}(G,M)\right)\)

as \(v\in V,z^*\in D_{28},w^*\in C_i\). Finally, the path \((v,z^*,z)\circ P_{z,u}\) exists in _G_<sub>6_,v_</sub> and Dijkstra computes a +4 approximation.

The computation of every invocation of Dijkstra requires time \(\tilde{O}(n^{2+x/27})\), since _l-l_<sub>0</sub>=27. The computation of **BK2APASP** requires time \(\tilde{O}(n^{1.5+x})\). The overall complexity of **DominatingSetAPASP** is dominated by the computation of bounded (min,+) products, which requires time,

\(\tilde{O}\left(n^{\omega\left(1-\frac{x}{27},1-x,1\right)}\right)\)

where we have again plugged in _l_=29_,l_<sub>0</sub>=2. Plugging in _x_=0.51973523 yields the desired complexity.

## Correctness

We prove Theorem 4.1 for general \(k\ge 6\).

_Proof._ Let _u,v_ be vertices and _P_ a shortest path of length \(\delta(u,v)\).

