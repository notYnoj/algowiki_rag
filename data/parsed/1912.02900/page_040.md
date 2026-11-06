When _L(v_) is a horizontal line, cost(_v_) is defined analogously: we index the points of \(X\cap S(v)\) in the increasing order of their _x_-coordinates. We then say that a consecutive pair of such points is a crossing iff they lie on opposite sides of _L(v_). We let cost(_v_) be the number of such crossings.

For a fixed ordering \(\sigma\) of the lines in \(\mathcal{L}^V\cup\mathcal{L}^H\), and the corresponding partition tree \(T=T(\sigma)\), we define \(\mathsf{cGB}_\sigma(X)=\sum_{v\in V(T)}\mathsf{cost}(v)\).

Lastly, we define the consistent Guillotine Bound for a point set _X_ that is a permutation to be the maximum, over all orderings \(\sigma\) of the lines in \(\mathcal{L}^V\cup\mathcal{L}^H\), of \(\mathsf{cGB}_\sigma(X)\).

In the following subsection we define an even stronger bound, that we call the _Guillotine bound_, and we show that for every point set _X_ that is a permutation, \(\mathsf{cGB}(X)\le\mathsf{GB}(X)\), and moreover that \(\mathsf{GB}(X)\le O(\mathsf{OPT}(X))\). It then follows that for every point set _X_ that is a permutation, \(\mathsf{cGB}(X)\le O(\mathsf{OPT}(X))\).

In subsequent subsections, we prove the following negative result for cGB, which extends the results of Theorem 1.1.

**Theorem 5.1** _For every integer_ \(n'\)_, there is an integer_ \(n\ge n'\)_, and a set X of points that is a permutation with_ |_X_|=_n, such that_ \(\mathsf{OPT}(X)\ge\Omega(nloglogn)\) _but_ \(\mathsf{cGB}(X)\le O(nlogloglogn)\).

The following lemma will be helpful in the proof of Theorem 5.1; recall that \(\mathsf{WB}'(X)\) is the basic Wilber Bound, where we cut via horizontal lines only.

**Lemma 5.2** _For every instance X that is a permutation,_ \(\mathsf{cGB}(X)\le\mathsf{WB}(X)+\mathsf{WB}'(X)\).

**Proof:** Let \(\sigma\) be a permutation of \(\mathcal{L}^V\cup\mathcal{L}^H\), such that \(\mathsf{cGB}(X)=\mathsf{cGB}_\sigma(X)\). Notice that \(\sigma\) naturally induces a permutation \(\sigma'\) of L_<sup>V</sup>_ and a permutation \(\sigma''\) of L_<sup>H</sup>_. We show that \(\mathsf{cGB}_\sigma(X)\le\mathsf{WB}_{\sigma^\prime}(X)+\mathsf{WB}'_{\sigma^{\prime\prime}}(X)\). In order to do so, it is enough to show that for every vertical line \(L\in\mathcal{L}^V\), the cost that is charged to _L_ in the bound \(\mathsf{cGB}_\sigma(X)\) is less than or equal to the cost that is charged to _L_ in the bound \(\mathsf{WB}_{\sigma^\prime}(X)\), and similarly, for every horizontal line \(L'\in\mathcal{L}^H\), the cost that is charged to \(L'\) in the bound \(\mathsf{cGB}_\sigma(X)\) is less than or equal to the cost that is charged to \(L'\) in the bound \(\mathsf{WB}'_{\sigma^{\prime\prime}}(X)\). We show the former; the proof of the latter is similar.

Consider any line \(L\in\mathcal{L}^V\). We let _T_ be the partitioning tree associated with \(\mathsf{cGB}_\sigma(X)\), just before line _L_ is processed, and we let \(T'\) be defined similarly for \(\mathsf{WB}_{\sigma^\prime}(X)\). Let \(v\in V(T')\) be the leaf vertex with \(L\subseteq S(v)\), and let _U_ be the set of all leaf vertices _u_ of the tree _T_ with \(S(u)\cap L\neq\emptyset\). Observe that the set of vertical lines that appear before _L_ in \(\sigma\) and \(\sigma'\) is identical. Therefore, \(S(v)=\bigcup_{u\in U}S(u)\). It is easy to verify that, for every vertex \(u\in U\), every crossing that contributes to cost(_u_) is also a crossing that is charged to the line _L_ in the strip _S(v_). Therefore, the total number of crossings of line _L_ in tree \(T'\) that contribute to \(\mathsf{WB}_{\sigma^\prime}(X)\) is greater than or equal to the number of crossings of the line _L_ that contribute to \(\mathsf{cGB}_\sigma(X)\).

To conclude, we get that \(\mathsf{cGB}(X)=\mathsf{cGB}_\sigma(X)\le\mathsf{WB}_{\sigma^\prime}(X)+\mathsf{WB}'_{\sigma^{\prime\prime}}(X)\le\mathsf{WB}(X)+\mathsf{WB}'(X)\). \(\square\)

## 5.1.2 Guillotine Bound

In this section, we define a second extension of Wilber Bound, that we call Guillotine Bound, and denote by GB. The bound is more convenient to define using a partitioning tree instead of a sequence of lines. Let _X_ be a point set which is a permutation.

