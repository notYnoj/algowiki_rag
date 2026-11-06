• Deleting an element _x_ corresponds to no more than _x._`weight` deletions in _H_, so \(d'\le W_\text{deleted}\).<tbc>

<tbc>Now let _c_<sup>∗</sup> be the total number of corruptions that ever happened in _H_. We clearly have \(c^*\le c'+d'\). Moreover, the number of extra copies ever inserted in to _H_, which is precisely \(m'-m\), is at most _c_<sup>∗</sup>. Overall, we have<tbc>

\(m'-m\le c^*\le c'+d'\le\varepsilon'm'+W_\text{deleted}.\)

<tbc>This solves to<tbc>

\(m'\le\frac{1}{1-\varepsilon'}(m+W_\text{deleted}),\)

<tbc>which proves the second part of the lemma and implies that

\(W_\text{corrupted}\le c'\le\varepsilon'm'\le\frac{\varepsilon'}{1-\varepsilon'}(m+W_\text{deleted})=\varepsilon(m+W_\text{deleted}).\)

The following lemma concludes the proof of theorem 14.

**Lemma 18.** _The amortized running time of_ `insert`, `find-min`, and `increase-weight` is_ O(1)_. The amortized number of comparisons performed by_ `increase-weight` is zero. The amortized running time of_ `delete` _is_ \(\mathcal{O}(wlog\frac{1}{\varepsilon})\)_, where w is the weight of the deleted element._

_Proof._ It is easy to see that `insert`, `find-min`, and `increase-weight` do constant work in addition to up to one call to _H._`insert` or _H._`find-min`.

For `delete`(_x_), observe that we call _H._`delete` once for _x_ and one more time for each copy of _x_. By observation 15, this makes up to _x._`weight` total deletions. The running time for this is \(\mathcal{O}(x.\text{\texttt{weight}}\cdot log\frac{1}{\varepsilon'})=\mathcal{O}(x.\text{\texttt{weight}}\cdot log\frac{1}{\varepsilon})\).

The WSH then performs up to one insertion into _H_ for each element corrupted by these deletions. By lemma 17, the total number of insertions into _H_ is O(_m+W_`deleted`), where _m_ is the number of insertions into the WSH, and _W_`deleted` is the total final weight of elements deleted from the WSH. Thus, all insertions into _H_ can be charged to `insert` and `delete` operations of the WSH. This also implies that `increase-weight` performs zero amortized comparisons, since it only performs comparisons due to a possible call _H._`insert`.

## 5 An O(_k_+OPT) algorithm for trees

In this section, we formally describe and analyze a version of our weighted-soft-heap based algorithm restricted to _trees_. We show:

**Theorem 19.** _There is an algorithm for poset selection that takes_ O(_k_+OPT(_T,k_)) _time on each input_ (_T,k,L_) _when T is a tree._

Observe that from theorem 19, an algorithm for _forests_ is easily obtained as follows: Given a forest _G_ and _k_, define the tree _T_ by adding a node _r_ to _G_ and making each root of _G_ a child of _r_. Clearly, _T_ is a tree. Run the algorithm on (_T,k_+1), and resolve each comparison with _r_ in such a way that _r_ is the minimal element in _V(T_). It is easy to see that this correctly<tbc>

