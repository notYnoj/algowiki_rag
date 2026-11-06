<tbc>\(x\in C(a,S')\). Since \(x\in C(a,S')\) and \(S'\) is an (_a,b_)-separator, path _P_ necessarily intersects \(S'\). Let _y_ be the first vertex of _P_ intersecting \(S'\): we fix _P<sub>x</sub>_ as the subpath of _P_ starting at _x_ and arriving at _y_. As the only vertex of _P_ intersecting _S_ is _x_ and since _y_ is the first vertex of \(S'\) in _P_, the internal vertices of _P<sub>x</sub>_ do not belong to \(S\cup S'\). Moreover, as _P<sub>x</sub>_ is a subpath of some (_a,b_)-path, its internal vertices cannot contain _a_ or _b_.

## 2.2.3 Close separators

A well-known concept on minimal separators is recalled here: the unicity of a minimal (_a,b_)- separator contained in _N<sub>G</sub>(a_), for two vertices _a,b_ not adjacent. Such unique separator was called the _close separator_ by Takata in \[28\] and comes from a more general definition. An example is illustrated in Figure 2.

**Lemma 4** (Close separator \[28\])**.** _Let_ \(A\unknown V\) _be a connected set (_i.e. _such that G_\[_A_\] _is connected) where_ \(a\in A\), \(b\notin N[A]\)_. The close separator S of_ (_A,b_) _is the unique minimal_ (_a,b)-separator included in N(A), denoted_ S_<sub>G</sub>(A,b). Formally,_

\(\mathcal{S}_G(A,b)=N\left(C(b,N(A))\right).\)

_The close separator_ S_<sub>G</sub>(A,b_) _can be computed in linear time O(m). When G is clear from the context, we might use notation_ S(_A,b_) _instead of_ S_<sub>G</sub>(A,b)._

Given a pair (_a,b_) of nonadjacent vertices, one close separator is particularly interesting: the one for which _A_={_a_}.

**Definition 10** (Close (_a,b_)-separator \[28\])**.** _Given a graph G with two vertices a,b such that_ \((a,b)\notin E(G)\)_, the_ close (_a,b_)-separator _is exactly_ S_<sub>G</sub>_({_a},b)._

The close (_a,b_)-separator is thus the unique minimal (_a,b_)-separator included into _N(a_). We need a property dealing with the close (_a,b_)-separator and its relationship with other minimal (_a,b_)-separators.

**Lemma 5** (Close (_a,b_)-separators and parallelism)**.** _Let_ \((a,b)\notin E(G)\)_, S_<sup>∗</sup> _the close_ (_a,b)- separator, and S be any other minimal_ (_a,b)-separator:_ \(S\neq S^*\)_. Then, S_<sup>∗</sup> _and S are parallel and_ \(C(a,S^*)\unknown C(a,S)\).

_Proof._ Our first goal is to show that any vertex of _S_<sup>∗</sup> belongs to either _S_ or _C(a,S_). Assume by way of contradiction that some \(v\in S^*\) belongs to _C(b,S_). As \(S^*\subseteq N(a)\), then \((a,v)\in E(G)\): this yields a contradiction as \(v\in C(b,S)\) and _a_ must be separated from _C(b,S_) by _S_.

A
a
b
S(A, b) ( N(A)

Figure 2: Schema of a close separator S(_A,b_) in blue. The red area highlights _N(A_).

