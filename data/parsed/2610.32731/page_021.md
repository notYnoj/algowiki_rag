### Hepapification.

Let _G_ be a DAG, let _L_ be a consistent ordering, and let _U_ be a set of sources in _G_. Then Heapify(_G,U_) modifies _G_ as follows: Build a heap _B_ on _U_, and add all edges of _B_ to _G_. It returns the root of _B_. The following analog of lemma 20 holds for Heapify:

**Lemma 29.** Heapify(_G,U_) _takes_ O(|_U_|) _time and yields a DAG_ \(G'\) _such that L is consistent with_ \(G'\)_, and_ \(\mathcal{L}(G')\subseteq\mathcal{L}(G)\)_, that is, every ordering_ \(L'\) _of_ \(V(G)=V(G')\) _that is consistent with_ \(G'\) _is also consistent with G._

_Proof._ As noted before, the running time of heapification is linear. The second statement immediately follows from the fact that Heapify only _adds_ edges to _G_, and all these edges are consistent with _L_.

### Weight updates.

We now explain line 26 of algorithm 2. Deleting _v_ from \(G'\) also removes all out-edges of _v_. After that, some previous out-neighbor _u_ of _v_ may have only one in-neighbor \(u'\). This increases the exclusive out-degree of \(u'\) by one, so we call \(Q.\text{\texttt{increase-weight}}(u',1)\). Note that this may un-corrupt \(u'\), hence the check in line 16 is necessary. Note that the weight of a single node \(u'\) may be increased multiple times, but, crucially, the exclusive out-degree never _decreases_.

Since we need to check each out-neighbor of \(u'\), the running time of line 26 is \(\mathcal{O}(\mathrm{deg}_+(G,u'))\), where _G_ denotes the DAG directly before removing _v_. The number of comparisons will be analyzed later.

### Correctness.

We can proceed with the same strategy as in section 5. One complication is that nodes may be un-corrupted due to weight changes. We say a node _u_ is _properly corrupted_ in iteration _i_ if in that iteration, _u_ is corrupted without being uncorrupted in the same iteration. Note that then _u_ is removed from _G_, meaning it cannot be uncorrupted in a later iteration.

The correctness proof of WSHTreeSelect (lemmas 22 and 24 and corollary 23) carries over to WSHPoseet almost directly. The only necessary changes are to replace "corrupted" with "properly corrupted", and to consider the set of in-neighbors instead of the single parent of a node.

### Number of comparisons.

From now on, fix some input _G_<sub>0</sub>_,k_. Let _D_ be the _k_-1 elements deleted from _Q_, and let _C_ be the set of corrupted elements in _Q_ at the end. Let _S_<sup>∗</sup> be the value of _S_ in the end. For each \(v\in D\cup C\), let _w(v_) be the final weight of _v_ in _Q_, when it is either deleted or properly corrupted.

We again need the following, which can be proved analogously to lemma 21.

**Lemma 30.** _Leet D be the set of elements deleted from Q so far at any point during a run of_ WSHTreeSelect_. Then D is a prefix of G_<sub>0</sub>.

We now prove the comparison bound.

**Lemma 31.** WSHPoseetSelect _performs_ O(_W(D_)+_W(C_)+|_S_<sup>∗</sup>|) _comparisons._

