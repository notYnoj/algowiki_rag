## A Probability, combinatorial, and Graph Tools

In this section, we restate probability and graph tools that we use throughout this paper. All these theorems are proven in previous work.

**Theorem A.1** (Chernoff Bounds \[Che52\])**.** _Let_ \(X=\sum_{i=1}^nX_i\)_, where X<sub>i</sub>_=1 _with probability p<sub>i</sub> and X<sub>i</sub>_=0 _with probability_ 1-_p<sub>i</sub>, and all X<sub>i</sub> are independent. Let_ \(\mu=\mathbf{E}[X]=\sum_{i=1}^np_i\)_. Then<br>
1._ \(Pr[X\ge(1+\delta)\mu]\le exp(-\delta^2\mu/3)\), \(\forall\delta>0\) _;<br>
2._ \(Pr[X\le(1-\delta)\mu]\le exp(-\delta^2\mu/2)\), \(\forall 0<\delta<1\).

**Theorem A.2** (Hoeffding bound \[Hoe63\])**.** _Let_ \(X_1,\cdots,X_n\) _denote n independent bounded variables in_ \[_a<sub>i</sub>,b<sub>i</sub>_\]_. Let_ \(X=\sum_{i=1}^nX_i\)_, then we have_

\(Pr[|X-\mathbf{E}[X]|\ge t]\le 2exp\left(-\frac{2t^2}{\sum_{i=1}^n(b_i-a_i)^2}\right)\)

**Theorem A.3** (Blakley-Roy inequality, \[BR65\], see also Proposition 3.1 in \[KSV13\])**.** _Let G denote a graph that has n vertices and average degree d. The number of walks of length k in graph G is at least nd<sup>k</sup>._

**Theorem A.4** (Turán theorem for bipartite graphs, \[KST54\], see also \[BBK13\])**.** _For a graph G the Turán number_ ex(_G,n_) _is the maximum number of edges that a graph on n vertices can have without containing a copy of G. For any_ \(s\le t\), \(ex(K_{s,t},n)\le\frac{1}{2}(t-1)^{1/s}n^{2-1/s}+o(n^{2-1/s})\)

In particular, when _s=t_, Theorem A.5 implies that for large enough _n_ we have \(ex(K_{s,s},n)\le n^{2-1/s}\).

**Theorem A.5** (Turán theorem for cliques \[Tur41\])**.** _Let G be any graph with n vertices, such that G is K_<sub>_r_+1</sub>_-free. Then the number of edges in G is at most_

\((1-\frac{1}{r})\cdot\frac{n^2}{2}.\)

**Corollary A.6** (of Theorem A.5)**.** _Let G be any graph with n vertices, such that G has no independent set of size r_+1_. Then the number of edges in G is at least_

\(\genfrac(){pt}{2}{n}{2}-(1-\frac{1}{r})\cdot\frac{n^2}{2}=\frac{nr+n^2}{2r}.\)

**Lemma A.7** (application of Jensen’s inequality)**.** _Let n_<sub>1</sub>_,n_<sub>2</sub>_,...,n<sub>k</sub> be a sequence of integer numbers of size k and_ \(\lambda_1,\lambda_2,\dots,\lambda_k\) _be k real numbers in the interval_ \[0,1\]_. Define_ \(\lambda=(\sum n_i\lambda_i)/(\sum n_i)\)_. Then for any_ \(y\ge 0\) _we have_<tbc>

\(\sum n_i\lambda_i^{1+y}\ge\sum n_i\lambda^{1+y}.\)

<tbc>_Proof._ Let \(\psi(x)=x^{1+y}\). Since \(\psi\) is real convex function, by Jensen’s inequality, we have<tbc>

\(\psi(\frac{\sum_in_i\lambda_i}{\sum_in_i})\le\frac{\sum n_i\psi(\lambda_i)}{\sum n_i}\)

<tbc>Applying definition \(\psi\), we have<tbc>

\((\frac{\sum_in_i\lambda_i}{\sum_in_i})^{1+y}\le\frac{\sum n_i\lambda_i^{1+y}}{\sum n_i}.\)

