<tbc>at the ancestor of _x_ in _T_ whose depth is _d<sub>T</sub>(x_)-2(_k_-1). Since the first _k_-1 splay steps each decrease the depth of _x_ by two, splay(_T,x_)=splay(_S,x_) where _S_=splay(_Q,x_). Denote by splay\('\) the procedure described in the theorem. Let _z_=root(_S_), let _y_ be the left child of _z_ in _S_ and assume without loss of generality that _x\<z_. (The other case is symmetric.) If _x=y_ then \(splay'(S,x)\) only enacts a single rotation at _x_, which is equivalent to the zig enacted by splay. If _x\>y_ then _y_ and _z_ are on opposite sides of _x_ in symmetric order and \(splay'(S,x)\) rotates twice at _x_, making it identical to the zig-zag step performed by splay. Finally, if _x\<y_ then \(splay'(S,x)\) rotates twice at _x_ and then once at _y_, which is equivalent the rotation at _y_ followed by _x_ in the zig-zig performed by splay. In all three cases, \(splay'(S,x)=splay(S,x)\). Form \(S'\) by replacing _Q_ with \(splay'(Q,x)\) in _T_. The edges rotated by \(splay'\) subsequent to the move-to-root operation are disjoint, and \(d_{S^\prime}(x)-d_{S^\prime}(w)\) and _d<sub>T</sub>(x_)-_d<sub>T</sub>(w_) have the same parity for every ancestor _w_ of _x_ in \(S'\). Therefore, \(splay'(T,x)=splay'(S',x)\). By the inductive hypothesis \(S'=S\), thus \(splay'(T,x)=splay(T,x)\).

Each zig-zig can create a violation of the max-heap ordering with respect to the standard priorities of an instance. As the executions of both Splay and Move-to-Root proceed, these zig-zigs will sometimes create further heap order violations. At other times, splay steps will remove some of the heap order violations. The correct potential for analyzing Splay’s crossing cost should in some way bound the rate at which splay operations generate heap order violations with respect to the standard priorities. We speculate on two possible forms. The first simply counts the number of edges in the tree being splayed that violate the heap-order condition with respect to most recent access time. This potential may be too "coarse," in that it fails to capture heap order violations between nodes not immediately connected by an edge. If so, the likely way to address this shortcoming is weighting each node by some function of the difference between its crossing depth in the splayed tree and in the max-heap order maintained by Move-to-Root. While honing the details of the potential’s construction falls outside this work’s scope, we can infer something important up front.

A potential function’s design is closely tied to the extent to which its value can increase or decrease. By Theorem 4.3, if Splay is dynamically optimal then its startup overhead is no more than linear in initial tree size. Hence, any potential for proving Conjecture 8.1 should also have maximum value at most linear in the size of the starting tree. This considerably narrows the design space that we might otherwise need to explore.

To prove optimality we must also address Splay’s bookkeeping cost. Here again, we can glean insight from Splay’s progenitor. Move-to-Root is not dynamically optimal. For example, if _T_ is a left spine with keys {1_,...,n_}, _X_=(_n,n_-1_,...,_2,1,2_,...,n_-1_,n_) and _Y_=(1,2_,...,n_) then<tbc>

10
9
X
8
10
9
X
9
7
8
4
10
7
3
6
7
3
5
4
6
2
8
5
3
2
4
2
5
6
1
1
1
X

Figure 7: The transformation from the left to the middle illustrates Move-to-Root. The transformation from the left to the right illustrates Splay. (Illustration from \[14\].)

