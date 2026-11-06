In both phases together, observing that \(k\le\mathtt{depth}_T(x)/2\), we have:

\(z=z_1+z_2\ge\frac{\mathtt{depth}_T(x)-k}{2}-1\ge\frac{\mathtt{depth}_T(x)}{4}-1.\)

The total increase in potential is \(6d\cdot\mathtt{depth}_R(x)-d/4\cdot\mathtt{depth}_T(x)-O(1)\).

Choosing _d_=4, we obtain \(\mathtt{depth}_T(x)+\phi(T')-\phi(T)\le 24\cdot\mathtt{depth}_R(x)+O(1)\le\mathcal{O}(\mathtt{depth}_R(x))\).

## Remark.

The additive term _O(n_<sup>2</sup>) is an artifact of the proof technique, arising as an upper bound on the total potential \(|\phi(T)|\). A finer bound of \(|\phi(T)|\le d\cdot\sum_{x\in V(S)}\mathtt{depth}_R(x)\) is immediate from Lemma 17(i)(ii). This shows that (1) the _O(n_<sup>2</sup>) upper bound is rather loose, unless the optimal tree _R_ is very unbalanced, and (2) if every node is searched _at least once_ in _X_, then \(|\phi(T)|\le d\cdot\mathtt{OPT}(X)\), and the additive term can be absorbed into O(`OPT`).

a
a
a
b
C
C
C
b
A
e
d
d
d
e
e
b

Figure 6.: Example showing that naïvely splaying in a Steiner-closed tree may destroy the property. (_left_) Underlying tree _S_. (_right_) Splaying node _e_. After the first (ZIG-ZIG) step, the search tree is no longer Steiner-closed.

