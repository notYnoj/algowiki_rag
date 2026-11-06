**Algorithm 15** `shortAdditiveAPASP`\((G,\beta)\)

**Input :** Unweighted, undirected graph _G_=(_V,E_) with _n_ vertices; approximation parameter \(\beta\)<br>
**Output:** Distance estimate \(\hat{\delta}:U\times V\rightarrow\mathbb{Z}\) such that \(\delta(u,v)\le\hat{\delta}(u,v)\) for all \(u,v\in V\) and \(\hat{\delta}(u,v)\le\delta(u,v)+\beta\) whenever \(\delta(u,v)\le\beta+1\)<br>
194 Phase 0: Set up and Decompose Graph<br>
195 \(\hat{\delta}(u,v)\leftarrow\left\{\begin{array}{ c c }
1 & (u,v)\in E \\
\infty & \text{o/w}
\end{array}\right.\)<br>
196 \(k\leftarrow\frac{3\beta+2}{2}\) and \(k_0\leftarrow\beta-2\).<br>
197 \(s_i\leftarrow n^{1-\frac{i}{k}}\) for all \(1\le i\le k-1\)<br>
198 \((D_1,D_2,\dots,D_k),(E_1,E_2,\dots,E_k),E^*\leftarrow\mathtt{rDecompose}(G,(s_1,s_2,\dots,s_{k-1}))\)<br>
199 for \(1\le i\le k\) do<br>
   if D<sub>i</sub> does not dominate all neighborhoods \(|N(v)|\ge s_i\) or \(|D_i|\ge\frac{12nlogn}{s_i}\) then<br>
**return**<br>
`APSP`<br>
(<br>
_G_<br>
)<br>
Phase<br>
1<br>
:<br>
Compute<br>
_X_<br>
(<br>
_u_<br>)<br>
,<br>
_C_<br>
(<br>
_u_<br>)<br>
for<br>
\(u\in V\)<br>
   for \(u\in V\) do<br>
   for \(k_0+1\le i\le k_0+\frac{\beta}{2}-1\) do<br>
   \(r_i\leftarrow\frac{\beta}{2}-(i-(k_0+1))\)<br>
   if \(|N(u,r_i)|\ge s_i\) then compute X(u,i) (see Lemma E.3);<br>
   else if \(|N(u,r_i)\cap D_{i+1}|\le 12s_{k-1}logn\) then compute \(C(u,i)\leftarrow N(u,r_i)\cap D_{i+1}\);<br>
   else return `APSP`(<br>
_G_<br>
)<br>
;<br>
   if \(\mathrm{deg}(u)\le s_{k_0+2}\) then \(\hat{\delta}(u,v)\leftarrow\mathrm{min}(\hat{\delta}(u,v),\mathtt{BFS}(G_{k_0+1},u,2))\) where G<sub>k<sub>0</sub>+1</sub>=(_V,E_<sub>k<sub>0</sub>+1</sub>);<br>
   for \(k_0+1\le i\le k_0+\frac{\beta}{2}-1\) do \(D_i\leftarrow D_i\cup\mathtt{HittingSet}(\{X(u,i)\})\) for all _u_ such that \(|X(u,i)|\ge s_i\);<br>
Phase<br>
2<br>
:<br>
Compute<br>
Distance<br>
Estimates<br>
   for \(1\le j\le k\) do<br>
   for \(w\in D_j\) do<br>
   \(G_{j,w}\leftarrow\left(V,E_j\cup\left(\bigcup_{j+j_1+j_2\le 2k+1}D_{j_1}\times D_{j_2}\right)\cup E^*\cup(w\times V)\right)\)<br>
   \(\hat{\delta}(w,v)\leftarrow\mathrm{min}(\hat{\delta}(w,v),\mathrm{min}_{u\in q(w,D_j)}1+\hat{\delta}(u,v))\) for all \(v\in V\)<br>
   \(\hat{\delta}\leftarrow\mathtt{Dijkstra}(G_{j,w},w,\hat{\delta})\)<br>
   for \(u,v\in V\) do<br>
   for \(k_0+1\le i\le k_0+\frac{\beta}{2}-1\) do<br>
   if \(\delta(u,p(u,D_i))\le r_i\) then \(\hat{\delta}(u,v)\leftarrow\mathrm{min}(\hat{\delta}(u,v),r_i+\hat{\delta}(p(u,D_i),v))\);<br>
   if \(|C(u,i)|\le 12s_{k-1}logn\) then \(\hat{\delta}(u,v)\leftarrow\mathrm{min}(\hat{\delta}(u,v),\mathrm{min}_{w\in C(u,i)}r_i+\hat{\delta}(w,v))\);

The following lemma bounds the probability that we must compute an exact `APSP` solution.

**Lemma E.4.** _Let_ \(u\in V\) _and_ \(k_0+1\le i\le k_0+\frac{\beta}{2}-1\) _Define the following events for each u,i._

\(A(u,i)=\{|N(u,r_i)|\ge s_i\}\)<br>
\(B(u,i)=\{|N(u,r_i)\cap D_{i+1}|\ge 12s_{k-1}logn\}\)

_For all u, let E(u,i_) _denote the error event_ \(E(u,i)=\neg A(u,i)\wedge B(u,i)\).

_For each_ \(1\le i\le k\)_, let E(i_) _denote the event that either D<sub>i</sub> fails to dominate some neighborhood of size at least s<sub>i</sub> or_ \(|D_i|\ge\frac{12nlogn}{s_i}\).

_Let_ \(E=(\bigcup_{i=1}^kE(i))\cup(\bigcup_{i,u}E(u,i))\) _denote the event that any error event occurs._

_Then,_ \(\mathrm{Pr}(E)=O\left(\frac{1}{n^2}\right)\)

