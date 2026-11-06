## A Additive Approximation Algorithms of \[DHZ00\] with a Different Analysis

In this appendix, we state the approximation algorithms of Dor, Halperin and Zwick \[DHZ00\], proving some useful properties about the algorithms that we require in our algorithm design.

**Lemma 3.2.** _(\[DHZ00\]) Let_ \(\beta\ge 2\) _be even. Let G be an undirected, unweighted graph with n vertices and m edges. There is an algorithm computing a_ \(+\beta\)_-approximate APSP solution in time_

\(\tilde{O}(min(n^{2-\frac{2}{\beta+2}}m^\frac{2}{\beta+2},n^{2+\frac{2}{3\beta-2}}))\)

_Denote **SparseAPASP** the algorithm running in time_ \(\tilde{O}(n^{2-\frac{2}{\beta+2}}m^\frac{2}{\beta+2})\) _and **DenseAPASP** the algorithm running in time_ \(\tilde{O}(n^{2+\frac{2}{3\beta-2}})\).

The pseudocode for **DenseAPASP** and **SparseAPASP** are provided in Algorithms 11 and 12 respectively. Although we never explicitly call **SparseAPASP**, we implicitly run it as a sub-routine in many of our algorithms.

**Algorithm 11** \(\text{\textbf{DenseAPASP}}(G,\beta)\)

**Input :** Unweighted, undirected Graph _G_=(_V,E_) with _n_ vertices and even integer \(\beta\)

**Output:** \(\hat{\delta}:U\times V\rightarrow\mathbb{Z}\) such that \(\delta(u,v)\le\hat{\delta}(u,v)\le\delta(u,v)+\beta\) for all \(u,v\in V\)

164 \(\hat{\delta}\leftarrow\left\{\begin{array}{ c c }
1 & (u,v)\in E \\
\infty & \text{o/w}
\end{array}\right.\)<br>
165 \(k\leftarrow\frac{3\beta-2}{2}\)<br>
166 \(s_i\leftarrow n^{1-\frac{i}{k}}\) for all \(1\le i\le k-1\)<br>
167 \((D_1,D_2,\dots,D_k),(E_1,E_2,\dots,E_k),E^*\leftarrow\text{\textbf{Decompose}}(G,(s_1,s_2,\dots,s_{k-1}))\)<br>
168 for \(1\le i\le k\) do<br>
   for \(w\in D_i\) do<br>
   \(G_{i,w}\leftarrow\left(V,E_i\cup(u\times V)\cup E^*\cup\left(\bigcup_{i+j_1+j_2\le 2k+1}D_{j_1}\times D_{j_2}\right)\right)\)<br>
  \(\hat{\delta}\leftarrow\text{\textbf{Dijkstra}}(G_{i,w},w,\hat{\delta})\)

**Algorithm 12** \(\text{\textbf{SparseAPASP}}(G,\beta)\)

**Input :** Unweighted, undirected Graph _G_=(_V,E_) with _n_ vertices, _m_ edges, and even integer \(\beta\)

**Output:** \(\hat{\delta}:U\times V\rightarrow\mathbb{Z}\) such that \(\delta(u,v)\le\hat{\delta}(u,v)\le\delta(u,v)+\beta\) for all \(u,v\in V\)

172 \(\hat{\delta}\leftarrow\left\{\begin{array}{ c c }
1 & (u,v)\in E \\
\infty & \text{o/w}
\end{array}\right.\)<br>
173 \(k\leftarrow\frac{\beta+2}{2}\)<br>
174 \(s_i\leftarrow(m/n)^{1-\frac{i}{k}}\) for all \(1\le i\le k-1\)<br>
175 \((D_1,D_2,\dots,D_k),(E_1,E_2,\dots,E_k),E^*\leftarrow\text{\textbf{Decompose}}(G,(s_1,s_2,\dots,s_{k-1}))\)<br>
176 for \(1\le i\le k\) do<br>
177 for \(w\in D_i\) do<br>
\(\hat{\delta}\leftarrow\text{\textbf{Dijkstra}}(G_{i,w},w,\hat{\delta})\) where \(G_{i,w}\leftarrow(V,E_i\cup(u\times V)\cup E^*)\)

