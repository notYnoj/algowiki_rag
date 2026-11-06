We use the observation that if two non-conflicting rectangles intersect, then one of them crosses the other on two of its sides, either top and bottom, or left and right. If \(p_1\neq p_j\), then _x(p<sub>j</sub>)\>x(p_<sub>1</sub>). Otherwise, _R<sub>j</sub>_ must cross the left and right side of _R_<sub>1</sub>, a contradiction to _R_<sub>1</sub> being the widest rectangle. Hence, we can place a line \(\ell_1\) connecting top and bottom boundaries of _R_<sub>1</sub> just right of _p_<sub>1</sub>. If _p_<sub>1</sub>=_p<sub>j</sub>_ on the other hand, then, by monotonicity and the previous observation, _x(q<sub>j</sub>)\<x(q_<sub>1</sub>) and _y(q<sub>j</sub>)\>y(q_<sub>1</sub>). We show that there cannot be another rectangle whose interior intersects both _R_<sub>1</sub> and the right border of _R<sub>j</sub>_. Suppose there was such a rectangle _R<sub>k</sub>_. If _R<sub>k</sub>_ crosses the left and right sides of _R<sub>j</sub>_ this contradicts the minimality of _x(p<sub>j</sub>_) for _R<sub>j</sub>_. Therefore, the interior of _R<sub>k</sub>_ could not have intersected the right border of _R<sub>j</sub>_. Hence, we may place \(\ell_1\) just right of _q<sub>j</sub>_. Repeating the argument for the remaining rectangles, we obtain the statement.

To show the second inequality, \(\mathsf{VS}(P,D)\le\mathsf{OPT}(P,D)\), consider a vertically separable set of monotone demands, the corresponding demand rectangles _R_<sub>1</sub>_,R_<sub>2</sub>_,...,R<sub>k</sub>_ and their respective separating lines \(\ell_1,\ell_2,\dots,\ell_k\). Consider an optimal solution _Q_ that satisfies these demands as well as the Manhattan path it uses to satisfy _R<sub>i</sub>_, that is the Manhattan-path connecting _p<sub>i</sub>_ and _q<sub>i</sub>_. This path must cross \(\ell_i\) at some point horizontally. We associate with _R<sub>i</sub>_ the pair \(a_i,b_i\in P\cup Q\) of points directly right and left of \(\ell_1\) on that path respectively. By the definition of separable demands, for two such point pairs (_a<sub>i</sub>,b<sub>i</sub>_), (_a<sub>j</sub>,b<sub>j</sub>_) that lie on the same horizontal line, either \(x(a_i)<x(b_i)\le x(a_j)<x(b_j)\), or \(x(a_j)<x(b_j)\le x(a_i)<x(b_i)\). This requires the monotonicity of the demands since it is otherwise possible that the top of some rectangle touches the bottom of another and the same point-pair is considered twice. We conclude that _k_ point-pairs on the same horizontal line consist of at least _k_+1 distinct points. Moreover, since input-points lie on distinct rows, at most one of these is an input point. We can thus charge each demand _R<sub>i</sub>_ to a distinct auxiliary point in the optimal solution. In fact, we can choose this to be either _a<sub>i</sub>_ or _b<sub>i</sub>_.

## C Tightness of Theorem 2

Let \(s\in\mathbb{N}\) be any integer. We show that there exists an _n_-point instance (_P,D_) on _s_ columns such that \(\mathsf{IS}(P,D)=\Theta(n)\) while \(\mathsf{OPT}(P,D)=\Omega(nlogs)\). We remark that this tightness holds even when _D_ is uniform.

There are many ways to prove this result, for instance, we can use the analysis of Wilber \[20\] adapted to the case with only _s_ columns. We sketch the proof here.

Let W(_P_) denote Wilber’s first bound on _P_. It was proved in \[9\] that \(\mathcal{W}(P)\le O(\mathsf{OPT}(P,D))\), where \(D=P\times P\) represents complete demands.

**Theorem 14.** _Let P be a random sequence of size n on s columns. Then_ \(\mathcal{W}(P)=\Omega(nlogs)\) _with high probability._

In particular, there exists an input _P_ with \(\mathcal{W}(P)=\Omega(nlogs)\). Since \(\mathsf{IS}(P,D)\le n\), we have our desired result.

## D NP-Hardness Proof for MinGMConn

We first observe that \(\alpha\) - the number of non-_SC_ demands _D<sub><o>SC</o></sub>_ - has polynomial size, namely

\(\alpha=3m\cdot 4+n\cdot 4=12m+4n.\) (2)

To see this, note that each of the _m_ clause gadgets _GC<sub>j</sub>_ contains 3 literal points \(\ell_{jk}\). Such an \(\ell_{jk}\) "connects" its corresponding positive or negative variable literal point \((x_i^+\) or \(x_i^-)\) to the clause<tbc>

