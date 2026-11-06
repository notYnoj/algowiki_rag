With this, the running time of _i_ such loops is O(_i_+|_S_|): The last time the loop is executed may take \(\mathcal{O}(|Q|)\le\mathcal{O}(|S|)\) time, but all other instances are amortized over their _i_-1 outer loop iterations.

It remains to show that the modified algorithm is still correct. Let _R<sub>i</sub>_ be the set of nodes that have been deleted from _Q_ or corrupted in _Q_ in the first _i_ outer loop iterations. Let _x_ be the result of _Q.find-min_() in the (_i_+1)th iteration, and let _x_<sub>1</sub>_,x_<sub>2</sub>_,...,x<sub>t</sub>=x_ be the nodes traversed by lines 8 and 9.

By lemma 22, all other nodes in _V(T_)\\_R<sub>i</sub>_ are larger than _x_. As noted in the proof of corollary 23, this is also true for each _x<sub>j</sub>_, \(j\in[t-1]\), since _x<sub>j</sub>_ is an ancestor of _x<sub>t</sub>=x_ in _T_.

Consider now the next iteration _i_+2, where we choose \(x\leftarrow x_2\). Observe that \(R_{i+1}\supseteq R_i\), so we still have that _x_<sub>2</sub> than all other nodes in \(V(T)\backslash R_{i+1}\subseteq V(T)\backslash R_i\). This means corollary 23 holds in iteration _i_+2, and similarly in all iterations until we use _Q.find-min_ again.

Finally, observe that we always delete a child of a previously deleted node; this ensures lemma 21 and thereby the rest of the correctness proof still holds. We have shown the following lemma, and thus theorem 19.

**Lemma 28.** WSHTreeSelect _can be modified to so that the running time matches the number of comparisons up to a constant factor, even when only performing the first i iterations for any_ \(i\in[k-1]\).

## 6 An O(_k_+OPT) algorithm for arbitrary posets

We now generalize WSHTreeSelect to posets. There are two main changes. The first one is of a technical nature: When a node is removed from or corrupted in _Q_, we _delete_ it from the DAG _G_. This simplifies the algorithm description and analysis, but note that we could have formulated WSHTreeSelect in this way, too.

The second change is concerns the _weights_ of nodes in _Q_. Recall that for trees, we defined the weight of a node as its degree (plus one). This worked because removing or corrupting a node adds all of its children as candidates for the next-largest element.

A naive generalization would take the _out-degree_ of a DAG node instead. However, deleting a DAG node with high out-degree does not necessarily make any nodes available, since these nodes need all of their in-neighbors be removed (or corrupted) first. The total weight of nodes<tbc>

deleted
corrupted

Figure 4: An example where line 8 of algorithm 1 is inefficient. After deleting ≈_k/_2 nodes (blue), a chain of ≈_k/_2 nodes is corrupted (red), which may cause total running time \(\Theta(k)\) for the next _k/_2 iterations.

