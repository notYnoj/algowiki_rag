The definitions of Wilber’s Alternation and Funnel bounds (Alt(_X),_Funnel(_X_)) are standard in the literature.

We now give precise definitions of Wilber’s two bounds.<sup>6</sup>

\(\blacktriangleright\) **Definition 13** (alternation bound)**.** _Let P be a point set with distinct y-coordinates, and let_ T _be a binary search tree over the values P.x. We define_ Alt<sub>T</sub>(_P_) _using the recursive structure of_ T_. If_ T _is a single node, let_ Alt<sub>T</sub>(_P_):=0_. Otherwise, let_ T<sub>L</sub> _and_ T<sub>R</sub> _be the left and right subtrees at the root. Partition P into two sets_ \(P_\mathrm{L}:=\{p\in P|p.x\in\mathcal{T}_\mathrm{L}\}\) _and_ \(P_\mathrm{R}:=\{p\in P|p.x\in\mathcal{T}_\mathrm{R}\}\) _and consider the quantity_ mixValue(_P_<sub>L</sub>_.y,P_<sub>R</sub>_.y), which describes how much P_<sub>L</sub> _and P_<sub>R</sub> _are interleaved with time (we call each switch between P_<sub>L</sub> _and P_<sub>R</sub> _a “preferred child alternation”). Then_

\(\mathsf{Alt}_\mathcal{T}(P):=\mathrm{mixValue}(P_\mathrm{L}.y,P_\mathrm{R}.y)+\mathsf{Alt}_{\mathcal{T}_\mathrm{L}}(P_\mathrm{L})+\mathsf{Alt}_{\mathcal{T}_\mathrm{R}}(P_\mathrm{R}).\) (4)

_The alternation bound is then defined as the maximum over all trees:_

\(\mathsf{Alt}(P):=\mathrm{max}_\mathcal{T}\mathsf{Alt}_\mathcal{T}(P).\)

_In addition, for an access sequence X, let_ Alt<sub>T</sub>(_X_):=Alt<sub>T</sub>(_G<sub>X</sub>_) _and_ Alt(_X_):=Alt(_G<sub>X</sub>)._

For the next few definitions, it is helpful to refer back to Figure 4. In particular, _F_<sub>L</sub>(_P,p_) and _F_<sub>R</sub>(_P,p_) (the left and right funnel) correspond to the points marked with L and R.

\(\blacktriangleright\) **Definition 14** (left and right funnel)**.** _Let P be a point set. For each_ \(p\in P\)_, we say that access_ \(q\in P\) _is in the left (resp. right) funnel of p within P if q is to the lower left (resp. lower right) of p and_ \(\square pq\) _is empty. Formally, let_

\(F_\mathrm{L}(P,p):=\{q\in P|q.y<p.y\wedge q.x<p.x\wedge P\cap\square pq=\{p,q\}\}\)

_and_

\(F_\mathrm{R}(P,p):=\{q\in P|q.y<p.y\wedge q.x>p.x\wedge P\cap\square pq=\{p,q\}\}.\)

_We will collectively call_ \(F_\mathrm{L}(P,p)\cup F_\mathrm{R}(P,p)\) _the funnel of p within P._

<sup>6</sup> These definitions may differ by a constant factor or an additive \(\pm O(m)\) from the definitions the reader has seen before. We will ignore such differences, because the cost of a BST also varies by \(\pm O(m)\) depending on the definition, and the interesting regime is when \(\mathsf{OPT}(X)=\omega(m)\).

\begin{tabular}{cccc}
Node & Link used by each access & Group by letter & # \\ _u_ & R, L, L, R, R, L & [R], [L, L], [R, R], [L] & 3 \\ _v_ & L, R, R & [L], [R, R] & 1 \\ _w_ & L, R, L & [L], [R], [L] & 2 \\ _x_ & R, L & [R], [L] & 1 \\ Total & & & 7 \\ \end{tabular}

u L
R v
w L
R L
R 1
x 4
5 L
R 2
3 reference tree T

**Figure 3** For access sequence _X_=(4,1,3,5,4,2) and reference tree T , Alt<sub>T</sub>(_X_)=7.

