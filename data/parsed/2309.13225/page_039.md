**Algorithm 6** `AdditiveAPASP`\((G,\beta)\)

**Input :** Unweighted, undirected Graph _G_=(_V,E_) with _n_ vertices; approximation parameter \(\beta\)

**Output:** Distance estimate \(\hat{\delta}:U\times V\rightarrow\mathbb{Z}\) such that \(\delta(u,v)\le\hat{\delta}(u,v)\le\delta(u,v)+\beta\) for all \(u,v\in V\)

71 Phase 0: Set up and Decompose Graph

72 \(\hat{\delta}(u,v)\leftarrow\left\{\begin{array}{ c c }
1 & (u,v)\in E \\
\infty & \text{o/w}
\end{array}\right.\)

73 \(k\leftarrow\frac{3\beta-2}{2}\)

74 \(x\leftarrow\) solution to \(\omega\left(1-\frac{\beta-2}{\beta+2}x,1-x,1-\frac{\beta-4}{\beta+2}x\right)=1+\frac{4+2\beta}{\beta+2}x\)

75 \(s_{k-i}\leftarrow n^{i\cdot\frac{x}{\lfloor k/3\rfloor+2}}\) for all \(1\le i\le\lfloor k/3\rfloor+2\)

76 \(k_0\leftarrow k-(\lfloor k/3\rfloor+2)=k-\lfloor k/3\rfloor-2\)

77 \((D_{k_0},D_{k_0+1},\dots,D_k),(E_{k_0},E_{k_0+1},\dots,E_k),E^*\leftarrow\text{\textbf{Decompose}}(G,(s_{k_0},s_{k_0+1},\dots,s_{k-1}))\)

78 Phase 1: Estimate Distances on High-Degree Paths

79 \(t_i\leftarrow\frac{n}{2i}\) for all \(1\le i\le l-1=\lceil(1-x)\mathrm{log}n\rceil\)

80 \((C_1,C_2,\dots,C_l),(F_1,F_2,\dots,F_l),F^*\leftarrow\text{\textbf{Decompose}}(G,(t_1,t_2,\dots,t_{l-1}))\)

81 for \(0\le i\le l\) do

82 **for** \(w\in C_i\) **do**

83 \(X_i(w)\leftarrow\text{\textbf{BFS}}(w)\) on _G<sub>i</sub>_=(_V,F<sub>i</sub>_)

84 \(\hat{\delta}(w,v)\leftarrow\mathrm{min}(\hat{\delta},X_i(w,v))\) for all \(v\in V\)

85 Construct \(|D_{k_0+2}|\times|C_i|\) matrix _A<sub>i</sub>_ where _A<sub>i</sub>(v,w_)=_X<sub>i</sub>(w,v_)

86 Construct \(|C_i|\times(2n-1)\) Euler tour distance matrix \(B'_i\) of _C<sub>i</sub>_ on _G<sub>i</sub>_

87 \(B_i\leftarrow\text{\textbf{BDtoMonotone}}(B'_i)[C_i,D_{k_0+3}]\)

88 \(\hat{\delta}\leftarrow\mathrm{min}(\hat{\delta}(w,v),\text{\textbf{MonotoneMinPlus}}(A_i,B_i))\)

89 Phase 2: Estimate Distances on Low-Degree Paths

90 for \(k_0+1\le j\le k\) do

91 **for** \(w\in D_j\) **do**

92 \(G_{j,w}\leftarrow(V,E_j\cup(u\times V)\cup E^*)\)

93 \(\hat{\delta}\leftarrow\text{\textbf{Dijkstra}}(G_{j,w},w,\hat{\delta})\)

**Warm-Up:** \(\beta=4\)

We begin by showing a proof of correctness for the case of \(\beta=4\). The somewhat simplified argument in this case will be generalized to arbitrary \(\beta\ge 6\) below.

**Lemma 5.9.** _Algorithm `AdditiveAPASP`_(_G,_4) _returns an estimate_ \(\hat{\delta}\) _such that_ \(\delta(u,v)\le\hat{\delta}(u,v)\le\delta(u,v)+4\) _for all u,v._

_Proof._ Let _P_ be a shortest path between _u,v_. Note that _k_=5_,k_<sub>0</sub>=2.

Suppose \(P\subset E_3=E_{k_0+1}\). Then, \(L(P,5)\subset\{3,4\}\) and \(|L(P,5)|\le 2\). By Lemma A.3, since _D_<sub>5</sub>=_D<sub>k</sub>=V_ , we obtain a +4 approximation in Phase 2.

Thus, _P_ has some vertex with degree at least _s_<sub>2</sub>=_n<sup>x</sup>_. Let _y_ denote the vertex in _P_ with degree at least _s_<sub>4</sub> closest to _v_. Let _z_ be a vertex of maximum degree on _P_ and _i_<sup>∗</sup> be the integer \(1\le i\le l\) such that \(\frac{n}{2^{i^*}}\le\mathrm{deg}(z)<\frac{n}{2^{i^*-1}}\). Since \(P\subset F_{i^*}\), we have in the _i_<sup>∗</sup>-th iteration of Phase 1 that \(X_{i^*}(z^*,u)\le\delta(z,u)+1\) and \(X_{i^*}(z^*,y^*)\le\delta(z,y)+2\) where _z_<sup>∗</sup>=_r(z,C_<sub>_i_<sup>∗</sup></sub>), _y_<sup>∗</sup>=_r(y,D_<sub>4</sub>). Therefore, after Line 88,<tbc>

\(\hat{\delta}_{i^*}(u,y^*)\le X_{i^*}(u,z^*)+X_{i^*}(z^*,y^*)\le\delta(u,z)+\delta(z,y)+3=\delta(u,y)+3\)

