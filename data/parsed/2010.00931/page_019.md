**Lemma 10.** _Let T be a k-cut STT on S, with_ \(k\ge 2\)_. Then T can be transformed into a_ (_k_-1)_-cut STT with at most n-k rotations, so that each intermediate tree is a k-cut tree._

_Proof._ Suppose _T_ is not a (_k_-1)-cut STT. Since \(|\delta(T)|=0\), there is a node _q_ with parent _p_ such that \(|\delta(T_q)|=k\) and \(|\delta(T_p)|<k\). Since \(\delta(T_q)\subseteq\delta(T_p)\cup\{p\}\), we have \(|\delta(T_p)|=k-1\). We can thus apply Lemma 9, increasing the number of nodes _x_ with \(|\delta(T_x)|\le k-1\) by at least one. Repeat this step until we have a _k_-cut STT. In the original tree _T_, every node _x_ of depth at most _k_ already satisfies \(|\delta(T_x)|\le\mathtt{depth}(x)-1\le k-1\). As such, we can ignore these nodes and need at most _n-k_ steps.

The first part of Theorem 2 now follows by induction as outlined above:

**Lemma 11.** _Let_ \(T,T'\) _be k-cut STTs. Then we can transform T into_ \(T'\) _with_ \((2k-1)n-(k+1)k+1\) _rotations._

_Proof._ If _k_=1, we need _n_-1 rotations, by Lemma 8. Otherwise, we transform the two _k_-cut STTs \(T,T'\) into (_k_-1)-cut STTs \(T'',T'''\), using 2(_n-k_) rotations, by Lemma 10. By induction, the rotation distance between \(T''\) and \(T'''\) is at most (2(_k_-1)-1)_n-k(k_-1)+1. The rotation distance between _T_ and \(T'\) is therefore at most

\(2(n-k)+(2(k-1)-1)n-k(k-1)+1\)<br>
\(=(2k-1)n-2k-k(k-1)+1\)<br>
\(=(2k-1)n-(k+1)k+1.\)

## 4.1. Implementation

We now finish the proof of Theorem 2, by showing that the constructed rotation-sequence can be carried out with O(_k_<sup>2</sup>_n_) pointer-moves and oracle calls. (This is necessary if we are to apply it in the STT model.)

Implementing Lemma 8 requires no more than the search for _r_<sub>2</sub> in _S_<sup>_r_<sub>1</sub></sup> and _n_-1 rotations, which altogether needs O(_n_) steps. It remains to show that Lemma 10 can be implemented in O(_kn_) steps, from which the _O(k_<sup>2</sup>_n_) bound of Theorem 2 will follow.

### The boundary-size data structure.

To detect nodes at which we can rotate (as in Lemma 9 and Lemma 10), we need to efficiently compute the boundary sizes of subtrees rooted at arbitrary nodes. Furthermore, these boundary sizes need to be updated during rotations. We show that a data structure that stores all boundary sizes can be obtained in an _O(k_<sup>2</sup>_n_)- time preprocessing, with _O(k_)-time updates for every rotation. As we do _O(kn_) rotations altogether, these costs can be absorbed in the _O(k_<sup>2</sup>_n_) bound of Theorem 2.

Consider a node _q_ with parent _p_ in _T_, and suppose that \(\delta(T_p)\) is known. We know that \(p\in\delta(T_q)\), since _V(T<sub>q</sub>_) is a connected component of _S_\[_V(T<sub>p</sub>_)\]\\_p_. Further, \(\delta(T_q)\backslash\{p\}\subseteq\delta(T_p)\). Each node \(x\in\delta(T_p)\) is a boundary node of _T<sub>q</sub>_ if and only if _x_ and _q_ lie on the same side of _p_ in _S_. Thus, we can compute \(\delta(T_q)\) from \(\delta(T_p)\) using \(|\delta(T_p)|\) oracle calls. It follows that, if _T_ is a _k_-cut tree, we can compute \(\delta(T_x)\) for all \(x\in V(T)\) in an _O(n_)-time traversal of _T_ starting from the root, with _O(nk_) oracle-calls.

