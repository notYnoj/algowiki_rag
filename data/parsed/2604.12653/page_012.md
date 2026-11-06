## 5.2 Invariants

We first describe the _main tree M_: This is a complete binary tree with \(m\in[n+1,2n]\) leaves, numbered 1,2_,...,m_ where _m_ is some power of two. The first _n_ of these leaves store items as in Theorem 12, while the remaining leaves are there for future addLeaf operations. Recall the definition of _t,s(i_) and _d(i_). We say the _height_ of a node is the height of its subtree in _M_. (Leaves have height 0.) Our goal is to maintain a set of leader nodes so that, for every _i_, the subtree of the leader of leaf _i_ has height _O(d(i_)). To this end, every node in _M_ can be _active_ or _passive_. We say a node _u_ is a _leader_ if _u_ is active and the parent of _u_ is passive. We require the following invariants:

(1) The leaves 1_,...,n_ are active, and the leaves _n_+1_,...m_ are passive.<tbc>

(2) If a node is active, then its children are active.<tbc>

(3) Consecutive leaders have a height difference of at most two. Formally: Let _u_<sub>1</sub>_,u_<sub>2</sub>_,..._ be the leaders in left to right order. Then \(|\text{height}(u_j)-\text{height}(u_{j+1})|\le 2\) for every _j_.<tbc>

(4) For every leaf _i_, the \(\lceil log_2(1+t-s(i))\rceil\)-th ancestor of _i_ is passive.<tbc>

(5) The parent of leaf _n_ is passive.

We will soon add some additional invariants to guarantee that the number of leaders stays small. Indeed, with just the invariants (1)-(5), we could make every leaf its own leader. However, we first show that these invariants already imply that the depth of each leaf is within the unified bound.

**Lemma 13.** _Every active node (and each leaf_ 1_,...,n) lies in the subtree of a unique leader._

_Proof._ We first show that the root of _M_ is passive. Indeed, since \(m\ge(n+1)\), the leaf _n_+1 exists. By invariant (1), this leaf is passive, so by invariant (2), the root of _M_ is passive too.

Let _u_ be an arbitrary active node. In particular, by invariant (1), _u_ could be any leaf of index 1_,...,n_. Let _v_ be the first active node on a root-to-_u_ path. By invariant (2), all nodes after _v_ are active. We have seen that _v_ cannot be the root of _M_. Thus, by definition, _v_ is the only leader on the root-to-_u_ path.

Invariants (3) and (4) imply that the depth of each leaf is bounded by the unified bound:

**Lemma 14.** _Let v be the leader of the i-th leaf. Then_ \(\text{height}(v)\le d(i)+3\).

_Proof._ Let _u,v,w_ be consecutive leaders, that is, in left to right order, let _u_ be the leader before _v_, and let _w_ be the leader after _v_. By invariant (3), \(\text{height}(u)\ge\text{height}(v)-2\) and \(\text{height}(w)\ge\text{height}(v)-2\). In particular, if \(|j-i|\le 2^{\text{height}(v)-2}\), then the _j_-th leaf lies in one of the subtrees of _u,v,w_, so by invariant (4), we have \(1+t-s(j)\ge 2^{\text{height}(v)-3}\). For all other _j_, we have \(|j-i|\ge 2^{\text{height}(v)-2}\). Therefore, \(d(i)=1+min_{1\le j\le n}(log(1+|i-j|)+log(1+t-s(j)))\ge\text{height}(v)-3\).

The astute reader might notice that we have not used invariant (5) so far. Indeed, (5) will only be used to support addLeaf in _O_(1) time, where it allows us to activate leaf _n_+1 without violating invariants (2) or (4).

We now describe the index trees _L_<sub>0</sub>_,L_<sub>1</sub>_,..._. Each index tree _L<sub>i</sub>_ is a balanced binary search tree. Every leader is stored in exactly one index tree, and leaders in the same index tree are ordered by their left-to-right order in the main tree _M_. These index trees have additional invariants:

(6) Before every addLeaf or access operation, the size of _L<sub>i</sub>_ is at most \(20\cdot 4^{2^{i+2}}\). After an addLeaf or access operation, the size of _L<sub>i</sub>_ is at most \(23\cdot 4^{2^{i+2}}\).<tbc>

