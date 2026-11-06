**Algorithm 1** `Random2ApproxAPSP`(_G_)

**Input :** Unweighted, undirected Graph _G_=(_V,E_) with _n_ vertices

**Output:** Distance estimate \(\hat{\delta}:U\times V\rightarrow\mathbb{Z}\) such that \(\delta(u,v)\le\hat{\delta}(u,v)\le 2\delta(u,v)\) for all \(u,v\in V\)

1 Fix parameters \(x\leftarrow 0.53184039\) and \(C\leftarrow 22\)

2 \(\hat{\delta}(u,v)\leftarrow\left\{\begin{array}{ c c }
1 & (u,v)\in E \\
\infty & \text{o/w}
\end{array}\right.\)

3 Phase 1: Compute +2 Approximate Distances of High Max Degree Paths

4 for _t_=2_<sup>j</sup> for_ \(0\le j\le\lceil(1-x)\mathrm{log}n\rceil\) **do**

5 \(C_t\leftarrow\text{\textbf{Dominate}}\left(G,\frac{n}{t}\right)\) and \(G_t=\left(V,E_\frac{2n}{t}\right)\)

6 \(\hat{\delta}\leftarrow\mathrm{min}(\hat{\delta},\text{\textbf{DominatingSetAPASP}}(G_t,V,V,C_t,C+1))\)

7 Phase 2: Compute Approximate Distances of Low Degree Paths

8 \(\hat{\delta}\leftarrow\mathrm{min}(\hat{\delta},\text{\textbf{BK2APASP}}(G_x))\) where _G<sub>x</sub>_=(_V,E<sub>n<sup>x</sup></sub>_)

9 Phase 3: Compute Approximate Distances of Long Paths

10 \(\hat{\delta}\leftarrow\mathrm{min}(\hat{\delta},\text{\textbf{DenseAPASP}}(G,C))\)

**Algorithm 2** `DominatingSetAPSP`(_G,V_<sub>1</sub>_,V_<sub>2</sub>_,W,C_)

**Input :** Unweighted, undirected Graph _G_=(_V,E_), source and target subsets \(V_1,V_2\subset V\) and dominating subset \(W\subset V\) , and distance bound _C_

**Output:** Distance estimate \(\hat{\delta}:U\times V\rightarrow\mathbb{Z}\) such that \(\delta(u,v)\le\hat{\delta}(u,v)\le\mathrm{min}_{w\in W}\delta(u,w)+\delta(w,v)\) for all _u,v_

11 for \(w\in W\) **do**

12 \(\hat{\delta}(w)\leftarrow\text{\textbf{BFS}}(G,w)\)

13 Construct \(V_1\times W\) matrix _A_ where \(A(v,w)=\left\{\begin{array}{ c c }
\hat{\delta}(w,v) & \hat{\delta}(w,v)\le C \\
\infty & \text{o/w}
\end{array}\right.\)

14 Construct \(W\times V_2\) matrix _B_ where \(B(w,v)=\left\{\begin{array}{ c c }
\hat{\delta}(w,v) & \hat{\delta}(w,v)\le C \\
\infty & \text{o/w}
\end{array}\right.\)

15 \(\hat{\delta}\leftarrow\text{\textbf{boundedMinPlus}}(A,B,C)\)

**Case 1:** \(\delta(u,v)\ge C\) In this case, `DenseAPASP` computes a +_C_ approximation so that,

\(\hat{\delta}(u,v)\le\delta(u,v)+C\le 2\delta(u,v)\)

**Case 2:** deg(_P)\<n<sup>x</sup>_ In this case, \(P\subset G_x=(V,E_{n^x})\) so that `BK2APASP` computes,

\(\hat{\delta}(u,v)\le 2\delta(u,v)\)

**Case 3:** \(\mathrm{deg}(P)\ge n^x\) **and** \(\delta(u,v)\le C\) We handle this case with Phase 1 and obtain a +2 approximation. Note that if \(\delta(u,v)=1\), then we already computed an exact distance when initializing \(\hat{\delta}\).

Let _w_ be the vertex of maximum degree in _P_. Let _j_ be the integer such that \(\frac{n}{2^j}\le\mathrm{deg}(w)<\frac{n}{2^{j-1}}\), noting that \(j\le\lceil(1-x)\mathrm{log}n\rceil\) since deg(_w)\>n<sup>x</sup>_. Consider the iteration where _t_=2_<sup>j</sup>_ of `DominatingSetAPASP` (Algorithm 2). Then, \(P\subset G_t=(V,E_\frac{2n}{t})\). Then, since \(\mathrm{deg}(w)\ge\frac{n}{t}\) we<tbc>

