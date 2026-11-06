**Algorithm 7** `BoundedAdditiveAPASP`\((G,\beta,C)\)

**Input :** Unweighted, undirected Graph _G_=(_V,E_) with _n_ vertices; approximation parameter \(\beta\); distance bound _C_

**Output:** Distance estimate \(\hat{\delta}:U\times V\rightarrow\mathbb{Z}\) such that \(\delta(u,v)\le\hat{\delta}(u,v)\) for all \(u,v\in V\) and \(\hat{\delta}(u,v)\le\delta(u,v)+\beta\) whenever \(\delta(u,v)\le C\).

94 Phase 0: Set up and Decompose Graph

95 \(\hat{\delta}(u,v)\leftarrow\left\{\begin{array}{ c c }
1 & (u,v)\in E \\
\infty & \text{o/w}
\end{array}\right.\)

96 \(k\leftarrow\frac{3\beta-2}{2}\)

97 \(x\leftarrow\) solution to \(\omega\left(1-\frac{\lfloor k/3\rfloor}{\lfloor k/3\rfloor+2}x,1-x,1-\frac{\lfloor k/3\rfloor-1}{\lfloor k/3\rfloor+2}x\right)=2+\frac{x}{\lfloor k/3\rfloor+2}\)

98 \(s_{k-i}\leftarrow n^{i\cdot\frac{x}{\lfloor k/3\rfloor+2}}\) for all \(1\le i\le\lfloor k/3\rfloor+2\)

99 \(k_0\leftarrow k-(\lfloor k/3\rfloor+2)=k-\lfloor k/3\rfloor-2\)

100 \((D_{k_0},D_{k_0+1},\dots,D_k),(E_{k_0},E_{k_0+1},\dots,E_k),E^*\leftarrow\text{\textbf{Decompose}}(G,(s_{k_0},s_{k_0+1},\dots,s_{k-1}))\)

101 Phase 1: Estimate Distances on High-Degree Paths

102 \(t_i\leftarrow\frac{n}{2^i}\) for all \(1\le i\le l-1=\lceil(1-x)\mathrm{log}n\rceil\)

103 (_C_<sub>1</sub>_,C_<sub>2</sub>_,...,C<sub>l</sub>),(F_<sub>1</sub>_,F_<sub>2</sub>_,...,F<sub>l</sub>),F_<sup>∗</sup> \(\leftarrow\text{\textbf{Decompose}}(G,(t_1,t_2,\dots,t_{l-1}))\)

104 for \(0\le i\le l\) do

105 **for** \(w\in C_i\) **do**

106 \(X_i(w)\leftarrow\text{\textbf{BFS}}(w)\) on _G<sub>i</sub>_=(_V,F<sub>i</sub>_)

107 \(\hat{\delta}(w,v)\leftarrow\mathrm{min}(\hat{\delta},X_i(w,v))\) for all \(v\in V\)

108 Construct \(|D_{k_0+2}|\times|C_i|\) matrix _A<sub>i</sub>_ where \(A_i(v,w)=\left\{\begin{array}{ c c }
X_i(w,v) & X_i(w,v)\le C+2 \\
\infty & \text{o/w}
\end{array}\right.\)

109 Construct \(|C_i|\times|D_{k_0+3}|\) matrix _B<sub>i</sub>_ where \(B_i(w,v)=\left\{\begin{array}{ c c }
X_i(w,v) & X_i(w,v)\le C+2 \\
\infty & \text{o/w}
\end{array}\right.\)

110 \(\hat{\delta}\leftarrow\mathrm{min}(\hat{\delta},\text{\textbf{BoundedMinPlus}}(A_i,B_i,C+2))\)

111 Phase 2: Estimate Distances on Low-Degree Paths

112 for \(k_0+1\le j\le k\) do

113 **for** \(w\in D_j\) **do**

114 \(G_{j,w}=(V,E_j\cup(w\times V)\cup E^*)\)

115 \(\hat{\delta}\leftarrow\text{\textbf{Dijkstra}}(G_{j,w},w,\hat{\delta})\)

**General Case:** \(\beta\ge 6\)

We now present the proof of Theorem 5.12.

_Proof._ (Correctness) We will ignore cases that are too similar to Theorem 5.6. Note by the definition of \(k\leftarrow\frac{3\beta-2}{2}\) and \(\beta\) is an even integer,

\(2\left(\lfloor k/3\rfloor+1\right)=2\left(\left\lfloor\frac{\beta}{2}-\frac{1}{3}\right\rfloor+1\right)\le\beta\)

By Lemma 5.16, it suffices to check that for \(\delta(u,v)\le C\), we have \(\hat{\delta}(u,v)\le\delta(u,v)+2(\lfloor k/3\rfloor+1)\).

Let \(u,v\in V\) be a pair of vertices such that \(\delta(u,v)\le C\). Let _P_ be a shortest path between _u,v_. Let \(\mathrm{deg}(P)=\mathrm{max}_{v\in P}\mathrm{deg}(v)\) be the maximum degree of any vertex on _P_.

