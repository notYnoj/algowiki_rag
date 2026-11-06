**Algorithm 8** `Weighted2AdditiveAPASP`(_G_)

**Input :** Weighted, undirected Graph _G_=(_V,E_) with _n_ vertices

**Output:** Distance estimate \(\hat{\delta}:U\times V\rightarrow\mathbb{Z}\) such that \(\delta(u,v)\le\hat{\delta}(u,v)\le\delta(u,v)+2w_{u,v}\) for all \(u,v\in V\)

116 Phase 0: Set up and Decompose Graph

117 \(\hat{\delta}(u,v)\leftarrow\left\{\begin{array}{ c c }
1 & (u,v)\in E \\
\infty & \text{o/w}
\end{array}\right.\)

118 \(x\leftarrow\) solution to \(\omega\left(1,1-x,1\right)=2+\frac{x}{2}\)

119 \(s_1,s_2\leftarrow n^x,n^\frac{x}{2}\)

120 \((D_1,D_2,D_3),(E_1,E_2,E_3),E^*\leftarrow\text{\texttt{WeightedDecompose}}(G,(s_1,s_2))\)

121 Phase 1: Estimate Distances on High-Degree Paths

122 \(t_i\leftarrow\frac{n}{2^i}\) for all \(1\le i\le l-1=\lceil(1-x)\mathrm{log}n\rceil\)

123 (_C_<sub>1</sub>_,C_<sub>2</sub>_,...,C<sub>l</sub>),(F_<sub>1</sub>_,F_<sub>2</sub>_,...,F<sub>l</sub>),_\(F^*\leftarrow\text{\texttt{WeightedDecompose}}(G,(t_1,t_2,\dots,t_{l-1}))\)

124 **for** \(0\le i\le l\) **do**

125 **for** \(w\in C_i\) **do**

126 \(X_i(w)\leftarrow\text{\texttt{Dijkstra}}(w)\) on _G<sub>i</sub>_=(_V,F<sub>i</sub>_)

127 \(\hat{\delta}(w,v)\leftarrow\mathrm{min}(\hat{\delta},X_i(w,v))\) for all \(v\in V\)

128 Construct \(V\times C_i\) matrix _A<sub>i</sub>_ where _A<sub>i</sub>(v,w_)=_X<sub>i</sub>(w,v_)

129 \(\hat{\delta}\leftarrow\mathrm{min}\left(\hat{\delta},\text{\texttt{ApproximateMinPlus}}\left(A_i,A_i^T,1+\frac{\varepsilon}{3}\right)\right)\)

130 Phase 2: Estimate Distances on Low-Degree Paths

131 **for** \(2\le j\le 3\) **do**

132 **for** \(w\in D_j\) **do**

133 \(G_{j,w}=(V,E_j\cup(u\times V)\cup E^*)\)

134 \(\hat{\delta}\leftarrow\text{\texttt{Dijkstra}}(G_{j,w},w,\hat{\delta})\)

_Proof._ (Correctness) We follow a similar proof to that of Cohen and Zwick \[CZ01\]. Fix a pair of vertices _u,v_ and let _P_ be a shortest path between _u,v_.

**Case 1:** \(P\unknown\subset E_2\) Let \(e_0\in P\) be edge such that \(e_0\notin E_2\). Let \(1\le j\le l-1\) such that \(P\subset F_j\) but \(P\cap(F_j\backslash F_{j+1})=\emptyset\). Such a _j_ must exist as _F_<sub>1</sub>=_E_ and _F<sub>l</sub>_ contains edges with rank at most \(t_{l-1}=\frac{n}{2^{l-1}}\le n^x\) so \(e_0\notin F_l\).

In particular, we now choose a specific _e_=(_a,b_) such that \(e\in F_j\backslash F_{j+1}\). By the correctness of `WeightedDecompose`, \(\mathrm{rank}_a(e),\mathrm{rank}_b(e)\ge t_j\). Since both _a,b_ have degree at least _t<sub>j</sub>_, let \(x\in D_j\) such that \((x,a)\in E_j^*\) so that \(\mathrm{rank}_a(x,a)<t_j\le\mathrm{rank}_a(e)\). Now, since \((x,a),P\subset F_j\), when we execute `Dijkstra` from _x_, we have

\(\hat{\delta}(x,u)\le\delta(a,u)+\mathfrak{wt}(x,a)\le\delta(a,u)+\mathfrak{wt}(a,b)\)<br>
\(\hat{\delta}(x,v)\le\delta(a,v)+\mathfrak{wt}(x,a)\le\delta(a,v)+\mathfrak{wt}(a,b)\)

Then, from the `ApproximateMinPlus` product,

\(\hat{\delta}(u,v)\le\left(1+\frac{\varepsilon}{3}\right)\left(\hat{\delta}(x,u)+\hat{\delta}(x,v)+2h(P)\right)\le(1+\varepsilon)\delta(u,v)+2h(P)\)

where the second inequality follows as \(\frac{2}{3}w_{u,v}\le\frac{2}{3}\delta(u,v)\).

