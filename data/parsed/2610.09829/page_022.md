• _s-t_ **longitudinal path.** Let _s,t_ be a pole pair. A shortest _s-t_ path in _G_ is an _s-t longitudinal path_ (or simply a _longitudinal path_ when the pole pair is clear from context).<tbc>

• _s-t_ **longitudinal cycle.** Let _s,t_ be a pole pair. A shortest cycle \(C=P_1\cup P_2\), where _P_<sub>1</sub> and _P_<sub>2</sub> are _s-t_ longitudinal paths satisfying \(V(P_1)\cap V(P_2)=\{s,t\}\), is an _s-t longitudinal cycle_ (or simply a _longitudinal cycle_). We call _P_<sub>1</sub> and _P_<sub>2</sub> the _longitudinal paths of C_.<tbc>

• _s-t_ **splittable cycle.** An _s-t_ longitudinal cycle _C_ is _s-t splittable_ (or simply _splittable_, when the context is clear) if the bounded region enclosed by _C_ contains a shortest _s-t_ path that is internally vertex-disjoint from _V(C_).<tbc>

• **Unsplittable cycle.** A shortest cycle that is not splittable is _unsplittable_.<tbc>

• **Consecutive** _s-t_ **longitudinal paths.** Let _P_ and \(P'\) be _s-t_ longitudinal paths, where \(V(P)\cap V(P')=\{s,t\}\). The paths _P_ and \(P'\) are _consecutive_ if the bounded region enclosed by the cycle \(P\cup P'\) contains no other _s-t_ longitudinal path.

Let _G_ be a weighted plane graph. We introduce the following partial order on the family of all shortest cycles of _G_. For two shortest cycles _C_<sub>1</sub> and _C_<sub>2</sub>, we write \(C_1\le C_2\) if every vertex and edge of _C_<sub>1</sub> is a vertex or an edge of _C_<sub>2</sub> or is embedded in the internal face Int(_C_<sub>2</sub>) of _C_<sub>2</sub>.

Consider a pole {_s,t_} in _G_. Following \[4\], we introduce specific families of paths and cycles as follows. Let \(C=P\cup P'\) be an _s-t_ splittable cycle where \(P,P'\) are _s-t_ longitudinal paths with \(V(P)\cap V(P')=\{s,t\}\). Recall that for a shortest cycle _C_ of a plane graph _G_, we denote by _G<sub>C</sub>_ the subgraph of _G_ induced by the vertices lying on _C_ or in Int(_C_). Let P_<sub>s</sub>(C_)={_P_<sub>0</sub>_,P_<sub>1</sub>_,...,P<sub>q</sub>_} be the inclusion-wise maximal family of distinct shortest _s-t_ paths in _G<sub>C</sub>_, ordered so that \(P_0\cup P_q=C\), and for each \(i\in[q]\) the paths _P_<sub>_i_-1</sub> and _P<sub>i</sub>_ are consecutive, i.e., no path of P_<sub>s</sub>(C_) is embedded in the interior of the cycle \(P_{i-1}\cup P_i\) (see Figure 13a). By \[4, Lemma 5.4\] the paths in P_<sub>s</sub>(C_) are pairwise internally vertex-disjoint and this ordering is unique. For paths in P_<sub>s</sub>(C_), we will always follow the ordering described here. Let C_<sub>s</sub>(C_) be the set of cycles obtained by taking consecutive pairs of paths in P_<sub>s</sub>(C_). By \[4, Lemma 5.5\], any shortest cycle \(C'\) contained in _G<sub>C</sub>_ is either the union of two paths from P_<sub>s</sub>(C_), or is embedded inside one of the cycles in C_<sub>s</sub>(C_), i.e., \(C'\le\widehat{C}\) for some \(\widehat{C}\in\mathscr{C}_s(C)\).

t
P1
P2
P3
P4
S

t
C
P1
P*
P3
S

t
P
P'
S

(a)

(b)

(c)

Figure 12: Illustration of Definition 5.3. (a) A pole {_s,t_} with four longitudinal paths _P_<sub>1</sub>_,P_<sub>2</sub>_,P_<sub>3</sub>_,P_<sub>4</sub>. (b) A splittable cycle \(C=P_1\cup P_3\) (blue and orange): the dashed green path _P_<sup>∗</sup> lies strictly inside _C_, witnessing splittability. (c) Two consecutive longitudinal paths _P_ and \(P'\): the bounded region of \(P\cup P'\) contains no other longitudinal path.

