(ii) there is \(e'\in E(C')\) such that every interior point of the curve of \(e'\) lies in Int(_C_).

If _C_ and \(C'\) do not cross, we say they are _non-crossing_.

**Definition 5.2** (Laminar family of cycles)**.** Let _G_ be a plane graph. A family C of cycles in _G_ is _laminar_ if no two distinct cycles in C cross. Equivalently, for any two distinct cycles \(C_1,C_2\in\mathcal{C}\), exactly one of the following holds: \(\mathrm{Int}(C_1)\subseteq\mathrm{Int}(C_2)\), \(\mathrm{Int}(C_2)\subseteq\mathrm{Int}(C_1)\), or \(\mathrm{Int}(C_1)\cap\mathrm{Int}(C_2)=\emptyset\).

We will next see how the shortest cycles in a weighted plane graph can be categorized into two types, _splittable_ and _unsplittable_--we state their definitions as implied by Lemma 5.4 of \[4\], as opposed to the original definitions given in \[4\]. We rephrase some of these definitions in terms of notions we call _longitudinal_ paths and cycles.

**Definition 5.3.** Consider a weighted plane graph _G_ (see Figure 12 for illustration).

• **Pole pair.** A pair of distinct vertices \(s,t\in V(G)\) is a _pole pair_(or simply poles) if there exist at least three pairwise internally vertex-disjoint shortest _s-t_ paths in _G_, each of length exactly _g(G)/_2.<tbc>

S
C1
C2
t

S
C1
C2
t

C
C'
C
C'
C'
C
S
t
S
t
C'
C'
(a) Crossing (shortest cycles do not cross this way)
(b) Non- crossing (nested)
(c) Non-crossing (touching)
(d) Crossing (two common vertices, no common edge)

(a)

(b)

Figure 10: Interactions between shortest cycles in a planar graph: (a) two cycles that share a common path (shown in red color); (b) two cycles intersecting exactly at two vertices _s_ and _t_.

(a) Crossing (shortest cycles do not cross this way)

(b) Non- crossing (nested)

(c) Non-crossing (touching)

(d) Crossing (two common vertices, no common edge)

Figure 11: Illustration of (some) crossing and non-crossing cycles in a plane graph. Two shortest cycles can cross exactly one way as illustrated in (d).

