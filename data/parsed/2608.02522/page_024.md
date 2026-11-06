_Proof of Lemma 4.5._ Let _G_ be any given graph, and let us set \(z:=\overline{\vartheta}(G)\ge 1\). By Defini tion 4.3, there exists a matrix \(M\in\mathcal{M}_G\) such that \(\lambda_\mathrm{max}(M)=z\). Since \(M\in\mathrm{Sym}_{V(G)}\) is positive semidefinite, we have that \(\|M\|=\lambda_\mathrm{max}(M)=z\). Let \(q:=\lceil z\rceil\). Note that since \(M\in\mathcal{M}_G\), we may now apply Lemma 4.7 to _M_ and _q_. We thus find that there exists a partition \(V(G)=V_1\sqcup\cdots\sqcup V_q\) of the vertex-set of _G_ such that

\(\|M_{V_i}\|\le\left(\sqrt{\frac{\|M\|}{q}}+1\right)^2=\left(\sqrt{\frac{z}{\lceil z\rceil}}+1\right)^2\le 4\)

for every \(i\in[q]\). Let now \(G'\) be the spanning subgraph of _G_, obtained from _G_ by deleting, for every \(i\in[q]\), the edges of _G_ which have both their endpoints in _V<sub>i</sub>_. Clearly, each _V<sub>i</sub>_ is an independent set in \(G'\), and hence we have \(\chi(G')\le q\).

In the following we will define a matrix \(M'\), of which we will then show that it belongs to \(\mathcal{M}_{G^\prime}\) and has a suitably large operator norm, so that we obtain a good lower bound on \(\overline{\vartheta}(G')\) using Definition 4.3. Concretely, we define

\(M':=I_{V(G)}+\frac{1}{4}\left(M-\sum_{i=1}^qM_{V_i}\right).\)

As a linear combination of symmetric matrices, \(M'\) is still symmetric. Furthermore, note that since _V_<sub>1</sub>_,...,V<sub>q</sub>_ partition _V(G_), we have that the diagonal entries of _M_ and \(\sum_{i=1}^qM_{V_i}\) agree. Thus, every diagonal entry of \(M'\) equals 1.

Note that with _M_ also each of the matrices _M<sub>V<sub>i</sub></sub>_, _i_=1_,...,q_ is positive semi-definite: For every vector \(\mathbf{y}\in\mathbb{R}^{V(G)}\), we have \(\mathbf{y}^\top M_{V_i}\mathbf{y}=\mathbf{w}^\top M\mathbf{w}\ge 0\), where **w** is obtained from **y** by replacing all entries with index outside of _V<sub>i</sub>_ by zeros. This in particular implies that \(\lambda_\mathrm{max}(M_{V_i})=\|M_{V_i}\|\le 4\) for every _i_.

We next claim that \(M'\) is positive semidefinite. So consider any non-zero vector \(\mathbf{x}\in\mathbb{R}^{V(G)}\). For each \(i\in[q]\), let **x**_<sub>i</sub>_ denote the vector obtained from **x** by replacing all entries of **x** with index outside _V<sub>i</sub>_ by zeroes. We then have:

\(\mathbf{x}^\top M'\mathbf{x}=\mathbf{x}^\top\mathbf{x}+\frac{1}{4}\mathbf{x}^\top M\mathbf{x}-\frac{1}{4}\sum_{i=1}^q\mathbf{x}^\top M_{V_i}\mathbf{x}\)<br>
\(\ge\mathbf{x}^\top\mathbf{x}\left(1-\frac{1}{4}\sum_{i=1}^q\frac{\mathbf{x}^\top M_{V_i}\mathbf{x}}{\mathbf{x}^\top\mathbf{x}}\right)+\frac{1}{4}\mathbf{x}^\top M\mathbf{x}\)<br>
\(=\mathbf{x}^\top\mathbf{x}\left(1-\frac{1}{4}\sum_{i=1}^q\frac{\mathbf{x}_i^\top M_{V_i}\mathbf{x}_i}{\mathbf{x}^\top\mathbf{x}}\right)+\frac{1}{4}\mathbf{x}^\top M\mathbf{x}\)<br>
\(\ge\mathbf{x}^\top\mathbf{x}\left(1-\frac{1}{4}\sum_{i=1}^q\frac{4\mathbf{x}_i^\top\mathbf{x}_i}{\mathbf{x}^\top\mathbf{x}}\right)+\frac{1}{4}\mathbf{x}^\top M\mathbf{x}\)<br>
\(=\mathbf{x}^\top\mathbf{x}\left(1-\frac{\sum_{i=1}^q\mathbf{x}_i^\top\mathbf{x}_i}{\mathbf{x}^\top\mathbf{x}}\right)+\frac{1}{4}\mathbf{x}^\top M\mathbf{x}=\frac{1}{4}\mathbf{x}^\top M\mathbf{x}\ge 0.\) (7)

Here we used that \(\mathbf{x}_i^\top M_{V_i}\mathbf{x}_i\le\lambda_\mathrm{max}(M_{V_i})\mathbf{x}_i^\top\mathbf{x}_i\le 4\mathbf{x}_i^\top\mathbf{x}_i\) for every \(i\in[q]\) as well as the fact that \(\sum_{i=1}^q\mathbf{x}_i^\top\mathbf{x}_i=\mathbf{x}^\top\mathbf{x}\) which follows directly from the definition of the vectors<tbc>

