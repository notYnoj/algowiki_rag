queries is chosen from the other category. Intervals of categories (3) and (4) are picked in order of non-increasing length of overlap with the target area. More precisely, intervals of category (3) are chosen according to the reverse of the order \(\unknown_U\) of their right endpoints, and intervals of category (4) are chosen according to the order \(\unknown_L\) of their left endpoints. When a round is filled, it is queried, and the algorithm restarts, calculating a new target area and redistributing the intervals into the categories.

\(\blacktriangleright\) **Proposition B.2** (Version of Proposition 5.4 for arbitrary intervals)**.** _At the start of any round,_ \(a\ge 1\) _and_ \(b\le a-1\).

**Proof.** Lemma B.1 shows \(a\ge 1\). If the target area is trivial, we have _b_=0 and hence \(b\le a-1\). From now on assume that the target area is non-trivial.

Let _L_ be the set of intervals in I that lie to the left of _I_<sub>ta</sub> (and have empty intersection with _I_<sub>ta</sub>). Similarly, let _R_ be the set of intervals that lie to the right of _I_<sub>ta</sub> (and have empty intersection with _I_<sub>ta</sub>). Observe that _a+b+c+d_+|_L_|+|_R_|=_n_.

The intervals in _L_ and the intervals of type (1) and (3) include all intervals with left endpoint not after \(\ell_{j_1}\) in the order \(\unknown_L\). As \(\ell_{j_1}\) is the _i_-th left endpoint in that order, we have \(|L|+a+c\ge i\).

Similarly, the intervals in _R_ and the intervals of type (1) and (4) include all intervals with right endpoint not before _u_<sub>_j_<sub>2</sub></sub> in the order \(\unknown_U\). As _u_<sub>_j_<sub>2</sub></sub> is the _i_-th smallest right endpoint in that order, or equivalently the (_n-i_+1)-th largest right endpoint in that order, we have \(|R|+a+d\ge n-i+1\).

Adding the two inequalities derived in the previous two paragraphs, we get \(2a+c+d+|L|+|R|\ge n+1\). Combined with _a+b+c+d_+|_L_|+|_R_|=_n_, this yields \(b\le a-1\). \(\blacktriangleleft\)

Lemma 5.5 and its proof hold for arbitrary intervals without any changes.

\(\blacktriangleright\) **Theorem B.3.** _There is a_ 2_-round-competitive algorithm for Selection even if arbitrary intervals are allowed as input._

**Proof.** The proof is identical to the proof of Theorem 5.6, except that Lemma B.1 and Proposition B.2 are used in place of Lemma 5.3 and Proposition 5.4, respectively. \(\blacktriangleleft\)

