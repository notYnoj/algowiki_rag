_Proof._ All comparisons are performed within _Q_ or heapifications. The number of `insert` operations is precisely |_S_<sup>∗</sup>|, using O(|_S_<sup>∗</sup>|) comparisons. By definition, deleting a node _x_ from _Q_ takes O(_w(x_)) comparisons, for a total of _W(D_). We further do only _k_-1 `find-min` operations, for a total of \(\mathcal{O}(k)=\mathcal{O}(|D|)\le\mathcal{O}(W(D))\) comparisons, and `increase-weight` performs zero amortized comparisons. Thus, the number of comparisons within _Q_ is O(_W(D_)+|_S_<sup>∗</sup>|).

Consider now a heapification due to the deletion of a node \(v\in C\cup D\) (line 17). Fix _G_ and \(G'\) in the moment directly before that deletion. The set _U_ that gets heapified is the set of _unmarked_ newly created sources when removing _v_ from _G_. That is, _U_ is the set of unmarked exclusive out-neighbors of _v_ in _G_. It is not hard to see that this is precisely the set of exclusive out-neighbors of _v_ in \(G'\) (as \(G'\) is exactly _G_ without the additional edges due to previous heapifications). By definition, this is \(w(v)-1\le w(v)\). Thus, the total cost of heapifications is \(\mathcal{O}(W(C\cup D))\).

**Lemma 32.** _We have_ \(W(C)+|S^*|\le\mathcal{O}(W(D))\).

_Proof._ As WSHTreeSelect, WSHPosetSelect performs up to three new insertions per deletion or corruption. The proof of the lemma is thus analogous to the proof of lemma 26.

**Lemma 33.** _We have_ \(W(D)\le 2|D|+c(G,D)\).

_Proof._ We define a subgraph _F_ of _G_ as follows. Consider an element \(v\in D\), and let \(D_v\subseteq D\) be the set of elements deleted before _v_. In _F_, connect _v_ to each of its exclusive out-neighbors in _G-D<sub>v</sub>_. Observe that _w(v_)=deg<sub>+</sub>(_G-D<sub>v</sub>,v_)+1, so _v_ has out-degree _w(v_)-1 in _F_. This implies that

\(|E(F)|=W(D)-|D|\) (2)

Further observe that each node in _F_ has in-degree at most one, that is, _F_ is a forest. More precisely, a node _u_ has in-degree zero if it has an in-neighbor in _G_ that is not contained in _D_. Otherwise, the unique in-neighbor of _u_ in _F_ is the last in-neighbor of _u_ in _G_ to be deleted.

We now show that \(|E(F)|\le|D|+c(G,D)\). Let _u_ be the endpoint of some edge in _F_. By the discussion above, this means that _u_ has no in-neighbors outside of _D_, implying that \(u\in D\cup\text{Sources}(G-D)\). Since each _u_ is the endpoint of at most one edge in _F_, we have (using lemma 30):

\(|E(F)|\le|D\cup\text{Sources}(G-D)|\le|D|+c(G,D).\) (3)

Equations (2) and (3) yield the lemma.

Lemmas 31 to 33 imply that WSHPosetSelect performs \(\mathcal{O}(k+c(G,D))\le\mathcal{O}(k+c(G,k-1))\) comparisons. Since \(\text{OPT}(G,k)\le c(G,k-1)\) by lemma 4, we have shown our main theorem 1.

