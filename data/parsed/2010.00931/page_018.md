Consider the tree after rotating at _x_<sub>_i_-1</sub>. By the inductive claim, _x_<sub>_i_-1</sub> is the root, and since {_x_<sub>_i_-1</sub>_,x<sub>i</sub>_} is an edge of _S_, node _x<sub>i</sub>_ is the child of the root. The next rotation brings _x<sub>i</sub>_ to the root, making it the parent of _x_<sub>_i_-1</sub>. All other nodes whose parent changes must be in the subtree of _S_ delimited by _x<sub>i</sub>_ and _x_<sub>_i_-1</sub>, but since _x_<sub>_i_-1</sub> and _x<sub>i</sub>_ are connected by an edge in _S_, there are no such nodes. Thus, the edge-set of the tree remains the same and equals the edge set of _S_. Since all intermediate trees are of the form _S<sup>x<sub>i</sub></sup>_, they are 1-cut.

We continue with the transformation of _k_-cut STTs into (_k_-1)-cut STTs. The following lemma shows that certain rotations strictly "improve" the tree, by reducing the boundary size of some subtree and not affecting the boundary sizes of other subtrees.

**Lemma 9.** _Let T be a k-cut STT on S, where_ \(k\ge 2\)_. Let q be a node of T with parent p such that_ \(|\delta(T_q)|=k\) _and_ \(|\delta(T_p)|=k-1\)_. Then, rotating at q produces a k-cut STT_ \(T'\)_, where_ \(|\delta(T'_q)|\le k-1\) _and for each node_ \(x\in V(T)\backslash\{q\}\)_, we have_ \(|\delta(T'_x)|\le|\delta(T_x)|\).

_Proof._ Let _A=V(T<sub>p</sub>_) and let \(B=\delta(T_p)\). The nodes _p_ and _q_ split _B_ into three parts:

• _B<sub>p</sub>_ contains all nodes in _B_ that _p_ separates from _q_,<tbc>

• _B<sub>q</sub>_ contains all nodes in _B_ that that _q_ separates from _p_,<tbc>

• \(B'\) contains all other nodes in _B_.

Clearly, _B_ is the disjoint union of _B<sub>p</sub>_, _B<sub>q</sub>_, \(B'\). Observe that \(\delta(T_q)=B'\cup B_q\cup\{p\}\).

We first claim that \(B_q\neq\emptyset\). Suppose otherwise. Since _T_ is a _k_-cut STT, _q_ is a _k_-admissible root of _V(T<sub>q</sub>_). Thus, by Lemma 7, we have \(q\in V(\mathsf{ch}(\delta(T_q)))=V(\mathsf{ch}(B'\cup B_q\cup\{p\}))=V(\mathsf{ch}(B'\cup\{p\}))\). But _q_ does not separate any two vertices in \(B'\cup\{p\}\), nor is it contained in \(B'\cup\{p\}\), a contradiction.

We conclude the proof by showing \(|\delta(T'_p)|,|\delta(T'_q)|\le k-1\). For all other nodes _x_, we have \(|\delta(T'_x)|\le|\delta(T_x)|\) by Observation 7. (See Figure 4.)

• For _p_, we have \(\delta(T'_p)=B_p\cup B'\cup\{q\}\). Since \(B_q\neq\emptyset\), we have \(|B_p\cup B'|\le|B|-1=k-2\). Thus, \(|\delta(T'_p)|\le k-1\).<tbc>

• For _q_, we have \(|\delta(T'_q)|=|B|=|\delta(T_p)|=k-1\).

It is easy to see that in a _k_-cut STT that is not a (_k_-1)-cut STT, we always have a node _q_ that satisfies the requirements of Lemma 9. Thus, we can repeatedly apply Lemma 9 and finish after at most _n_ steps. In fact, we can do slightly better:

