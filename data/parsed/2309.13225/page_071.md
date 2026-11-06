### _k_=6

We minimize,

\(max\left(\omega\left(1-\frac{2x}{l-4},1-x,1-\frac{x}{l-4}\right),2+\frac{x}{l-4},1.5+x\right)\)

Using \[Bra\], we set _l_=51_,x_=0.50980335 and obtain the running time \(\tilde{O}(n^{2.01084688})\).

### _k_=8

We minimize,

\(max\left(\omega\left(1-\frac{3x}{l-6},1-x,1-\frac{2x}{l-6}\right),2+\frac{x}{l-6},1.5+x\right)\)

Using \[Bra\], we set _l_=74_,x_=0.50716126 and obtain the running time \(\tilde{O}(n^{2.00745825})\).

### _k_=10

We minimize,

\(max\left(\omega\left(1-\frac{4x}{l-8},1-x,1-\frac{3x}{l-8}\right),2+\frac{x}{l-8},1.5+x\right)\)

Using \[Bra\], we set _l_=96_,x_=0.50496404 and obtain the running time \(\tilde{O}(n^{2.00573823})\).

### _k_=12

We minimize,

\(max\left(\omega\left(1-\frac{5x}{l-10},1-x,1-\frac{4x}{l-10}\right),2+\frac{x}{l-10},1.5+x\right)\)

Using \[Bra\], we set _l_=119_,x_=0.50432041 and obtain the running time \(\tilde{O}(n^{2.00462679})\).

## D A Quadratic \((\frac{7}{3},0)\)-Approximate APSP on Unweighted Graphs

In the section, we briefly observe that a \(\frac{7}{3}\)-approximate APSP solution can be obtained in \(\tilde{O}(n^2)\)- time. This follows simply from a \(\tilde{O}(n^2)\)-time (2,1)-approximate APSP algorithm due to Baswana and Kavitha \[BK10\] and Berman and Kasiviswanathan \[BK07\] along with the result of \[DHZ00\]

**Lemma D.1.** _Given an undirected, unweighted graph, Algorithm 14 outputs a_ (2,0) _approximation for paths of length_ \(\delta(u,v)\le 2\)_. in_ \(\tilde{O}(n^2)\)_-time._

**Algorithm 14** `distance2APASP`(_G_)

**Input :** Unweighted, undirected Graph _G_=(_V,E_) with _n_ vertices

**Output:** Distance estimate \(\hat{\delta}:U\times V\rightarrow\mathbb{Z}\) such that \(\delta(u,v)\le\hat{\delta}(u,v)\) for all _u,v_ and \(\hat{\delta}(u,v)\le 4\) for all \(\delta(u,v)=2\)

\(\hat{d}(u,v)\leftarrow\left\{\begin{array}{ c c }
1 & (u,v)\in E \\
\infty & \text{o/w}
\end{array}\right.\) **186**

\(s_i\leftarrow\frac{n}{2^i}\text{for all}1\le i\le k-1=\lfloor logn\rfloor\) **187**

\((D_1,D_2,\dots,D_k),(E_1,E_2,\dots,E_k),E^*\leftarrow\text{\textbf{Decompose}}(G,(s_1,s_2,\dots,s_{k-1}))\) **188**

**for** \(1\le i\le k=\lfloor logn\rfloor+1\) **do**

**190** **for** \(w\in D_i\) **do**

**191** \(X_i(w)\leftarrow\text{\textbf{Dijkstra}}(w)\text{on graph}\left(V,E_i\cup(w\times V)\cup E^*,\hat{\delta}\right)\) **192** \(\hat{\delta}(w,v)\leftarrow min(\hat{\delta}(w,v),X_i(w,v))\)

**193** \(\hat{\delta}(u,v)\leftarrow min(\hat{\delta}(u,v),\hat{\delta}(v,u))\)

