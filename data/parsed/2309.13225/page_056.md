We will briefly remark that Algorithm **(2,1)-APASP** in fact returns a (2,0)-approximation for paths of even length, only returning a (2,1)-approximation for paths of odd length.

**Algorithm 10** `MulAddAPASP`\((G,\alpha,\beta)\)

**Input :** Unweighted, undirected Graph _G_=(_V,E_) with _n_ vertices; approximation parameters \(\alpha,\beta\)

**Output:** Distance estimate \(\hat{\delta}:U\times V\rightarrow\mathbb{Z}\) such that \(\delta(u,v)\le\hat{\delta}(u,v)\le\alpha\delta(u,v)+\beta\) for all \(u,v\in V\)

157 \(\gamma\leftarrow\) maximum even \(\gamma\) such that \(\gamma\le 1+\frac{\beta-1}{2-\alpha}\)

158 \(k\leftarrow\) minimum _k_ such that `AdditiveAPASP`(_G,k_) requires \(O(T(\gamma))\) time

159 \(C\leftarrow\frac{k-\beta}{\alpha-1}\)

160 \(\hat{\delta}(u,v)\leftarrow\left\{\begin{array}{ c c }
1 & (u,v)\in E \\
\infty & \text{o/w}
\end{array}\right.\)

161 \(\hat{\delta}\leftarrow min(\hat{\delta},\text{\textbf{(2,1)-APASP}}(G))\)

162 \(\hat{\delta}\leftarrow min(\hat{\delta},\text{\textbf{BoundedAdditiveAPASP}}(G,\gamma,C))\)

163 \(\hat{\delta}\leftarrow min(\hat{\delta},\text{\textbf{AdditiveAPASP}}(G,k))\)

_Proof._ (Correctness) Let \(u,v\in V\) .

**Case 1:** \(\delta(u,v)\ge C\) Then, from `AdditiveAPASP`,

\(\hat{\delta}(u,v)\le\delta(u,v)+k=(\alpha-1)C+\beta\le\alpha\delta(u,v)+\beta\)

**Case 2:** \(\gamma\le\delta(u,v)\le C\) Then, from `BoundedAdditiveAPASP`\((G,\gamma,C)\),

\(\hat{\delta}(u,v)\le\delta(u,v)+\gamma\)

Note that if \(\beta\ge\gamma\), we have in fact already obtained a \((1,\beta)\) approximation. Thus, in the following, assume \(\beta<\gamma\).

For now, assume \(\delta(u,v)=\gamma\). Then,

\(\hat{\delta}(u,v)\le 2\delta(u,v)\)<br>
\(=(2\delta(u,v)-\beta)+\beta\)<br>
\(=\frac{2\delta(u,v)-\beta}{\delta(u,v)}\delta(u,v)+\beta\)<br>
\(=\left(2-\frac{\beta}{\gamma}\right)\delta(u,v)+\beta\)

noting that \(2-\frac{\beta}{\gamma}\le 2-\frac{\beta-1}{\gamma-1}\le\alpha\) as \(\beta<\gamma\). We conclude the proof by noting that for all larger paths, an additive error of \(\gamma\) implies an \((\alpha,\beta)\) approximation, as desired.

**Case 3:** \(\delta(u,v)\le\gamma-1\) From **(2,1)-APASP**,

\(\hat{\delta}(u,v)\le 2\delta(u,v)+1=2\delta(u,v)-(\beta-1)+\beta\le\left(2-\frac{\beta-1}{\gamma-1}\right)\delta(u,v)+\beta\)

By our choice of \(\gamma\),

\(2-\frac{\beta-1}{\gamma-1}\le\alpha\)

