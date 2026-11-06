From Lemma 13 it follows, in particular, that neither the root _r_ of _T_, nor the searched node _x_ can be branching (since \(|\delta(T_r)|=0\), and _x_ has no child on _P_). The following lemma shows that we can only lose the Steiner-closed property by rotating the edge between a branching node and its relevant child.

**Lemma 14.** _Let T be a Steiner-closed STT, let_ \(q\in V(T)\) _with parent_ \(p\in V(T)\)_. Let_ \(T'\) _be the tree obtained by rotating the edge_ {_q,p}. Then_ \(T'\) _is Steiner-closed if and only if_ \(|\delta(T_p)|\neq 2\) _or_ \(|\delta(T_q)|\neq 1\).

_Proof._ Suppose that \(|\delta(T_p)|=2\) and \(|\delta(T_q)|=1\), i.e. _p_ is a branching node of the search path of _q_. Then _p_ has two ancestors _y_<sub>1</sub>_,y_<sub>2</sub> such that _p_ has degree 3 in ch({_y_<sub>1</sub>_,y_<sub>2</sub>_,q_}). The search path \(P'_q\) of _q_ in \(T'\) contains _y_<sub>1</sub>_,y_<sub>2</sub>_,q_, but not _p_, so \(P'_q\) is not Steiner-closed.

Conversely, suppose that \(T'\) is not Steiner-closed, so \(|\delta(T'_p)|>2\) by Observation 7. Since \(\delta(T'_p)\subseteq\delta(T'_q)\cup\{q\}\), and \(|\delta(T'_q)|\le 2\) by Observation 7, we have \(|\delta(T'_q)|=2\), say \(\delta(T'_q)=\{y_1,y_2\}\) and \(\delta(T'_p)=\{y_1,y_2,q\}\). We already have \(|\delta(T_p)|=|\delta(T'_q)|=2\). It remains to show that \(|\delta(T_q)|=1\). We claim that \(\delta(T_q)=\{p\}\).

Suppose, to the contrary, that \(y_i\in\delta(T_q)\) for some \(i\in\{1,2\}\). Then _q_ cannot separate _y<sub>i</sub>_ from _p_, since \(y_1\in\delta(T_p)\). Moreover, no ancestor of _p,q_ is in ch({_p,q_}). In particular, ch({_p,q,y<sub>i</sub>_}) has a node _z_ of degree 3, which is not an ancestor of _p,q_. As such, the search path of _q_ in _T_ is not Steiner-closed, a contradiction.

Our goal is to remove all branching nodes from the search path _P<sub>x</sub>_ before splaying _x_ to the root. Note that by Lemma 13, a branching node can never be the child of another branching node. Our strategy is to splay up a branching node _b_ to become the child of its lowest branching ancestor \(b'\), or to become the root, if _b_ has no branching ancestors. In both cases _b_ loses the branching property. It is crucial that during this process no new branching nodes are created on _P<sub>x</sub>_ and \(b'\) (if exists) stays a branching node. We show this in the following.

**Lemma 15.** _Let T be an STT, let P<sub>x</sub> be the search path of x in T, and let_ \(q\in P\) _be a node with non-branching parent_ \(p\in P\)_. Let_ \(T'\) _be the tree obtained by rotating the edge_ {_q,p}, and let_ \(P'_x\) _be the search path of x in T. Then_

(_i)_ _Every branching node of_ \(P'_x\) _is a branching node of P<sub>x</sub>;_<tbc>

_(ii)_ _Every branching node of P<sub>x</sub>, except possibly q, is a branching node of_ \(P'_x\).

_Proof._ (i) Since \(V(P'_x)\subseteq V(P_x)\), no non-branching node on the search path becomes branching and no new branching node enters the search path of _x_.

(ii) Let \(b\neq q\) be a branching node of _P<sub>x</sub>_, with child _c_ on _P<sub>x</sub>_. The branching node _b_ is not affected by the rotation, so \(|\delta(T'_q)|=|\delta(T_q)|=2\) by Observation 7. If \(c\neq q\), then _c_ is not affected by the rotation either, so \(|\delta(T'_c)|=|\delta(T_c)|=1\). Otherwise, if _c=q_, then \(|\delta(T'_c)|=|\delta(T_q)|=1\). Either way, _b_ stays a branching node.

We are now ready to describe the search operation in our generalized SplayTT structure (Algorithm 4). Like Splay, it starts with a normal search to the target node _x_ in the (Steiner-closed) search tree _T_, identifying the search path of _x_ (Line 2). Then, in a first phase of splaying (Lines 3-6), it transforms the search path, such as to remove all branching<tbc>

