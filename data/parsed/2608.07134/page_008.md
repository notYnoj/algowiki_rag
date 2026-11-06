the heaps are identical or _F<sub>x</sub>_ contains all the elements from \(F_\emptyset\) together with one extra element _y_, where initially _y=x_. Insertions preserve this property. If \(F_\emptyset\) deletes _z_, then _F<sub>x</sub>_ deletes min{_y,z_}, leaving max{_y,z_} as its new extra element. If \(F_\emptyset\) encounters an unsuccessful deletion, _F<sub>x</sub>_ deletes its extra element, and after that the two executions are identical.

Consider the state of _H_ in `ReverseHeapEval` after processing T , before processing \(\sigma\), and recall that \(\EuScript{E}(H)=\EuScript{D}(\emptyset,\mathcal{T})\) by the induction hypothesis. If \(|H|<\delta\), then an unsuccessful deletion occurs in the forward execution of T (since \(\delta\) counts all deletions while |_H_| only counts the successful ones). Therefore, both \(F_\emptyset\) and _F<sub>x</sub>_ end in the same state. Consequently, \(\EuScript{E}(H)\cup\{x\}=\EuScript{D}(\emptyset,\sigma\mathcal{T})\). Note that the check \(|H|>\delta\) in Algorithm 1, line 7 fails in this case, so _x_ gets correctly inserted into _H_.

Otherwise, if \(|H|=\delta\), every deletion in \(F_\emptyset\) is successful, and the extra element of _F<sub>x</sub>_ at the end of execution is \(max(\EuScript{E}(H)\cup\{x\})\) because every deletion replaces the current extra element _y_ with max{_y,z_}. Thus, the deleted set is \((\EuScript{E}(H)\cup\{x\})\backslash\{max(\EuScript{E}(H)\cup\{x\})\}\). Observe that the check in Algorithm 1, line 7 succeeds in this case, so the algorithm is again correct.

The invariant therefore holds for every suffix. Taking T =S, `ReverseHeapEval` returns \(\EuScript{D}(\emptyset,\mathcal{S})\) as claimed.

Adapting Lemma 2.2, after running `ReverseHeapEval` with a soft max-heap \(\tilde{H}\) instead of an exact heap, the set \(\tilde{X}\) of uncorrupted elements in \(\tilde{H}\) is a subset of \(\EuScript{D}(\emptyset,\mathcal{S})\).<sup>6</sup> We can use this information to reduce the problem size. Simply removing all insertions of elements \(x\in\tilde{X}\) would not work; we also need to remove the corresponding `delete-min` operations. Identifying the precise deletion that removes each element, however, would reintroduce the sorting barrier. The following lemma shows that it is sufficient to remove the first `delete-min` after the insertion of _x_.

**Lemma 2.4.** _Let x be an element of_ \(\EuScript{D}(\emptyset,\mathcal{S})\)_, and let_ \(\sigma\) _be the first_ `delete-min` _operation of_ S _after the insertion of x. Let_ \(\mathcal{S}'\) _be the sequence of operations obtained by removing_ `insert`(_x_) _and_ \(\sigma\) _from_ S_. Then_ \(\mathcal{R}(\emptyset,\mathcal{S})=\mathcal{R}(\emptyset,\mathcal{S}')\).

**Proof.** Consider two initially empty exact heaps _H_ and \(H'\). Run the first heap on S and the second one on \(\mathcal{S}'\) in parallel. (When one of the two omitted operations occurs, the second heap does nothing while the first one executes the operation.) Let _y_ be the element that \(\sigma\) deletes in _H_. Since _x_ has not been deleted yet, we have \(key(y)\le key(x)\).

If _y=x_, the claim is immediate. Otherwise, we prove that until _H_ deletes _x_, the two heaps differ only in that _H_ contains _x_ while \(H'\) contains some element _z_ with \(key(z)\le key(x)\).

Recall that \(key(y)\le key(x)\), so the property indeed holds immediately after \(\sigma\). Insertions clearly preserve this property, as do deletions in which both heaps delete the same element. The only other case is where \(H'\) deletes _z_ while _H_ deletes some \(z'\neq x\) with \(key(z')<key(x)\), in which case \(z'\) becomes the new _z_.

Finally, when the first heap deletes _x_, the second heap must delete _z_ (since all other elements are common), and from this moment on the heaps remain identical. Hence, at the end of the execution we have \(\EuScript{E}(H)=\EuScript{E}(H')\).

Lemma 2.4 allows us to remove a single element of \(\EuScript{D}(\emptyset,\mathcal{S})\). If a subset _Z_ of \(\EuScript{D}(\emptyset,\mathcal{S})\) needs to be removed, the argument can be applied repeatedly. Algorithmically, this can be implemented in O(|S|) time by running a linear scan with a stack over S and matching each deletion with the last unmatched insertion from _Z_.

<sup>6</sup> In a soft max-heap, keys of corrupted elements decrease rather than increase.

