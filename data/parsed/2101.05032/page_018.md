**(4)** _d_ intervals \([\ell_j,u_j]\) with \(\ell_j>\ell_{j_1}\) and \(u_j\ge u_{j_2}\); they intersect the target area on the **right**. We propose the following algorithm for rounds with _k_ queries: Each round is filled with as many non-trivial intervals as possible, using the following order: first all intervals of category (1); then intervals of category (2); then picking intervals alternatingly from categories (3) and (4), starting with category (3). If one of the two categories (3) and (4) is exhausted, the rest of the _k_ queries is chosen from the other category. Intervals of categories (3) and (4) are picked in order of non-increasing length of overlap with the target area, i.e., intervals of category (3) are chosen in non-increasing order of right endpoint, and intervals of category (4) in non-decreasing order of left endpoint. When a round is filled, it is queried, and the algorithm restarts, with a new target area and the intervals redistributed into the categories.

\(\blacktriangleright\) **Proposition 5.4.** _At the start of any round,_ \(a\ge 1\) _and_ \(b\le a-1\).

**Proof.** Lemma 5.3 shows \(a\ge 1\). If the target area is trivial, we have _b_=0 and hence \(b\le a-1\). From now on assume that the target area is non-trivial.

Let _L_ be the set of intervals in I that lie to the left of the target area, i.e., intervals _I<sub>j</sub>_ with \(u_j<\ell_{j_1}\). Similarly, let _R_ be the set of intervals that lie to the right of the target area. Observe that _a+b+c+d_+|_L_|+|_R_|=_n_.

The intervals in _L_ and the intervals of type (1) and (3) include all intervals with left endpoint at most \(\ell_{j_1}\). As \(\ell_{j_1}\) is the _i_-th smallest left endpoint, we have \(|L|+a+c\ge i\).

Similarly, the intervals in _R_ and the intervals of type (1) and (4) include all intervals with right endpoint at least _u_<sub>_j_<sub>2</sub></sub>. As _u_<sub>_j_<sub>2</sub></sub> is the _i_-th smallest right endpoint, or equivalently the (_n-i_+1)-th largest right endpoint, we have \(|R|+a+d\ge n-i+1\).

Adding the two inequalities derived in the previous two paragraphs, we get \(2a+c+d+|L|+|R|\ge n+1\). Combined with _a+b+c+d_+|_L_|+|_R_|=_n_, this yields \(b\le a-1\). \(\blacktriangleleft\)

\(\blacktriangleright\) **Lemma 5.5.** _If the current round of the algorithm is not the last one, then the following holds: If the algorithm queries at least one interval of categories (3) or (4), then the algorithm does not query all intervals of category (3) that contain v_<sup>∗</sup>_, or it does not query all intervals of category (4) that contain v_<sup>∗</sup>.

**Proof.** Assume for a contradiction that the algorithm queries at least one interval of categories (3) or (4), and that it queries all intervals of categories (3) and (4) that contain _v_<sup>∗</sup>. Observe that the algorithm also queries all intervals in categories (1) and (2), as otherwise it would not have started to query intervals of categories (3) and (4). Thus, the algorithm has queried all intervals that contain _v_<sup>∗</sup> and, hence, solved the problem, a contradiction to the current round not being the last one. \(\blacktriangleleft\)

\(\blacktriangleright\) **Theorem 5.6.** _There is a_ 2_-round-competitive algorithm for Selection._

**Proof.** Consider any round of the algorithm that is not the last one. Let _A_, _B_, _C_ and _D_ be the sets of intervals of categories (1), (2), (3) and (4) that are queried in this round, respectively. Let _A_<sup>∗</sup>, _B_<sup>∗</sup>, _C_<sup>∗</sup> and _D_<sup>∗</sup> be the subsets of _A_, _B_, _C_ and _D_ that are in OPT<sub>1</sub>, respectively. By Lemmas 5.2 and 5.3, \(|A|=|A^*|\ge 1\). Since the algorithm prioritizes category (1), by Proposition 5.4 we have \(|B|\le|A|-1\), and thus \(|A\cup B|\le 2\cdot|A|-1=2\cdot|A^*|-1\le 2(|A^*|+|B^*|)-1\).

For bounding the size of \(C\cup D\), first note that the order in which the algorithm selects the elements of categories (3) and (4) ensures that, within each category, the intervals that contain _v_<sup>∗</sup> are selected first. By Lemma 5.5, there exists a category in which the algorithm does not query all intervals that contain _v_<sup>∗</sup> in the current round. If that category is (3), we have |_C_|=|_C_<sup>∗</sup>| and, by the alternating choice of intervals from (3) and (4) starting with (3),

