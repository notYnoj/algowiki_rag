## 2.3 Merge-width

For two sets _X,Y_ , we write \(XY:=\{xy|x\in X,y\in Y,x\neq y\}\), where _xy_ denotes the unordered pair {_x,y_}. Let P be a partition of the vertices _V_ of a graph _G_. For a set \(X\subseteq V\) , we denote by _X/_P the set of parts of P intersecting _X_. Let \(R\subseteq\genfrac(){pt}{2}{V}{2}\) be a set of pairs of vertices of _G_. The distance between _x_ and _y_ in (_V,R_) is denoted by dist_<sub>R</sub>(x,y_), and we define \(\mathrm{Ball}_R^r(x):=\{y\in V|\mathrm{dist}_R(x,y)\le r\}\). The _radius-r width_ of (P_,R_) is defined as

\(max_{v\in V}|\mathrm{Ball}_R^r(v)/\mathcal{P}|.\)

We say that P is _homogeneous modulo R_ (in _G_) if for any parts \(X,Y\in\mathcal{P}\) (possibly _X=Y_ ) and pairs \(xy,x'y'\in XY\backslash R\), we have that \(xy\in E(G)\) if and only if \(x'y'\in E(G)\). A partition P is _coarser_ than a partition \(\mathcal{P}'\), denoted by \(\mathcal{P}'\unknown\mathcal{P}\), if every part of \(\mathcal{P}'\) is contained in a part of P.

\(\blacktriangleright\) **Definition 6** (Definition 3.1 in [17])**.** _A_ merge sequence _for a graph G is a sequence_ (P<sub>1</sub>_,R_<sub>1</sub>)_,...,_(P_<sub>m</sub>,R<sub>m</sub>_) _such that:_

\(\mathbf{1}.\mathcal{P}_1\unknown\mathcal{P}_2\unknown\dots\unknown\mathcal{P}_m\text{\textit{is a sequence of ever coarser partitions of}}V(G)\text{\textit{, with}}\mathcal{P}_1\text{\textit{the
partition into singletons and}}\mathcal{P}_m\text{\textit{the partition with one part,}}\)

\(\mathbf{2}.R_1\subseteq\cdots\subseteq R_m\subseteq\genfrac(){pt}{2}{V(G)}{2}\text{\textit{is a monotone sequence of sets of pairs of vertices, and}}\)

\(\mathbf{3}.\mathcal{P}_t\text{\textit{is homogeneous modulo}}R_t\text{\textit{, for}}t=1,\dots,m\text{\textit{.}}\)

_The_ radius-_r_ width _of this merge sequence is the maximum radius-r width of_ (P_<sub>t</sub>,R_<sub>_t_+1</sub>)_, for_ \(1\le t<m\)_. Finally, the_ radius-_r_ merge-width _of G, denoted by mw<sub>r</sub>(G), is the minimum radius-r width of a merge sequence for G._

The elements of _R<sub>t</sub>_ are called _resolved pairs_ (at step _t_). Note that the partition P<sub>_t_+1</sub> is obtained by merging some parts of P_<sub>t</sub>_. Note also that the index mismatch in (P_<sub>t</sub>,R_<sub>_t_+1</sub>) is intentional, and prevents one from merging many parts and adding many resolved pairs all at once when going from step _t_ to _t_+1.

A graph class C has _bounded merge-width_ if there is a function _f_ such that for every \(G\in\mathcal{C}\) and every positive integer _r_, we have \(\mathrm{mw}_r(G)\le f(r)\).

**Organization.** We prove Theorem 1 in Section 3, Theorem 2 in Section 4, Theorem 3 in Section 5, and Theorem 4 in Section 6.

## 3 Approximation Hardness of MIS in Graphs of Bounded Twin-Width

In this paper, all 3-SAT instances have only 3-clauses. Equal literals within the same clause are allowed, but we disallow opposite literals of the same variable within the same clause. A 3-SAT-_B_ formula has no variable occurring (positively or negatively) more than _B_ times. The following theorem is a consequence of Dinur’s almost-linear PCP [15] and some folklore reductions; see, for instance, [23, Thm. 7].

\(\blacktriangleright\) **Theorem 7** (consequence of Theorem 8.3 in [15])**.** _Unless the ETH fails, there are positive constants_ \(\beta<1,B,c\) _such that distinguishing n-variable m-clause 3-SAT-B satisfiable formulas from instances where at most_ \(\beta m\) _clauses can be satisfied requires_ \(2^{\Omega(n/\mathrm{log}^cn)}\) _time._

We denote by \(e(\varphi)\) the total number of unordered pairs of opposing literals appearing in \(\varphi\). For instance, if \(\varphi=x_1\vee\neg x_2\vee x_4,\neg x_1\vee\neg x_1\vee x_2,\neg x_2\vee x_3\vee\neg x_4\), we have \(e(\varphi)=2+2+0+1=5\). We denote by \(\mathrm{val}(\varphi)\) the largest number of clauses satisfied by any truth assignment. In particular, if \(\varphi\) is satisfiable, then \(\mathrm{val}(\varphi)\) is equal to its number of clauses.

