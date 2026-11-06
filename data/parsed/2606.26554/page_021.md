_Proof of Lemma 5.9._ Consider the matrix \(X':=X-min_{i,j}X[i,j]\) with integer entries between \[0_,B_\], which can be computed in _O(n_<sub>1</sub>_n_<sub>2</sub>) time. Then, \(X'\star Y\) can be computed in \(O\left(B\cdot\mathsf{T}_\mathrm{MUL}(n_1,n_2,n_3)\right)\) time \[AGM97\]. To recover _X⋆Y_ , observe that \(X\star Y=(X'\star Y)+min_{i,j}X[i,j]\), which can be computed in _O(n_<sub>1</sub>_n_<sub>3</sub>) time.

We are now ready to prove Theorem 1.3. Consider the following procedure which for presentation we break into an initialization phase and a computation phase. In the initialization phase, we decompose the graph and initialize various useful data structures.

In the computation phase, we use the computed decompositions and data structures to compute shortest paths.

Input: Graph G=(V,E,wt), weight bound B, and sources Sin V .
1. For t=0...logB and b=2t:
(a) Let Gb=(V,Eb) be the graph with Eb= {e ∈ E s.t. b (b) Let d, 2 (d, 2 (sqrtlogn).
(c) Let Cb be a (d, )-LDSND of Gb as an unweighted graph. Denote Cb = {V1 (b), ..., Vkb (b)
2. Let S S in.
3. For all s S:
(a) Let L(s, 0) {s}, L(s, r) = 0 for 1 r (n, and (s, s) = 0, (d(s, v) = 0 for all v = s.
(b) Let A(s, b) {s} and level(s, b) = 0 for all s S and b=2t. Let level(s) = 0.
4. Let score(i, b) = | {s S s.t. level(s) = level(s, b) and A(s, b) = 0} for all Vi (b)
Output: Cb, A(s, b), level(s, b), level(s), L(s, r), (d(s, v), and score(i, b) for all s, b, r,i.

Input: Graph G, weight bound B, sources Sin. Outputs of initialization phase.
1. While S = :
(a) If exists S with A(s, b) = 0 for all b=2t:
i. Run increaseLevel (s, {level(s, b)}, level(s), {L(s, r)}, {Cb})
(b) Otherwise, there exists (b) with score(i, b) > |S|N (V(b)) 2 (nlogB
i. Run extendPaths (G, S, V(b), {A(s, b)}, {level(s, b)}, {level(s)}, {level(s)}, {L(s, r)}).
Output: (s, v) for all S in and v V.
extendPaths (G, S, V(b), {A(s, b)}, {level(s, b)}, {level(s)}, {level(s)}, {L(s, r)}):
1. Let S' = {s S s.t. A(s, b) = 0}.
2. If |N(V(b))| = |Sin
(a) For all S', u = A(s, b) (b), ,v N(b): update (s, v) -min (s, u) + wt(u, v).

