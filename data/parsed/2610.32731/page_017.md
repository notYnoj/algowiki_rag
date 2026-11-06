## Correctness.

We start with two simple facts.

**Lemma 22.** _Let x be the result of Q._`find-min`() _(line 7) in some iteration. Then all smaller nodes have been either deleted or corrupted in a previous iteration._

_Proof._ Suppose for the sake of contradiction that there exists a node \(u\prec x\) that has not been deleted or corrupted in a previous iteration. Choose _u_ to have minimum depth, and observe that _u_ cannot be the root, which is always deleted in the first iteration.

At the start of the current iteration, the parent of _u_ must have been deleted or corrupted in a previous iteration. This means that _u_ has been inserted into _Q_ at some point. By assumption, _u_ is not currently corrupted. Since \(u\prec x\), _Q._`find-min`() will not return _x_, a contradiction.

**Corollary 23.** _Let x be the node deleted in some iteration. Then all smaller nodes have been either deleted or corrupted in a previous iteration._

_Proof._ Use lemma 22, and observe that line 9 can only replace _x_ by a smaller node.

Observe that WSHTreeSelect is correct if _S_ contains the smallest _k_ nodes at the end, since then the final Select(_S,k_) returns the desired result. We now show that this is true.

**Lemma 24.** _At the end of a call to_ WSHTreeSelect_, all nodes with rank at most k are contained in S._

_Proof._ Corollary 23 implies that after the _k_-1 iterations, all nodes with rank at most _k_-1 must have been deleted or corrupted, and thus are contained in _S_. Now let _v_ be the node of rank _k_. The parent _p_ of _v_ has rank less than _k_, and as such must have been deleted or corrupted at some point. This also caused _v_ to be inserted into _S_.

## Number of comparisons.

We now show that WSHTreeSelect performs O(OPT+_k_) comparisons. To achieve the same bound on the running time, we need a small modification that we discuss later.

**Lemma 25.** _Directly before and after each iteration of the main loop in_ WSHTreeSelect_, each node_ \(v\in V(T)\) _has at most three marked children, and at most_ deg(_T_<sub>0</sub>_,v_) _many unmarked children._

_Proof._ At the start, the invariant is clearly true since _T=T_<sub>0</sub>. The children of a node _v_ are changed at most twice: Once when its parent _p_ is corrupted or deleted and _v_ is part of a Heapify call, and once when _v_ itself is corrupted or deleted and its unmarked children are heapified. The former gives _v_ up to two new marked children. The latter removes all unmarked children besides one, which is immediately marked. This clearly implies the statement.

Fix some input _T_<sub>0</sub>_,k_ to WSHTreeSelect. In the following, write _w(v_)=deg(_T_<sub>0</sub>_,v_)+1 for each node _v_. Observe that _w(v_) is the weight of _v_ as long as it is contained in _Q_. Moreover, for a node set _U_ define \(W(U)=\sum_{u\in U}w(u)\). Observe that \(W(U)\ge|U|\).

