<tbc>its associated left side the witness of this point.

For any point added to _Q_ in line 5 in one of the last \(\lceil logs\rceil\) recursion levels, pick the first (left or right) side of a demand rectangle that led to including this point. More precisely, if, in line 5, we add point (_x(p),m_) to _Q_ for the first time (which means that this point has not yet been added to _Q_ via a different demand) then associate \(\lambda(p,q)\) as a witness. Analogously, if we add (_x(q),m_) for the first time then associate \(\rho(p,q)\) as a witness.

Overall, we have associated to each point in the final solution a uniquely determined witness, which is a left or a right side of some demand rectangle. Note that any (left or right) side of a rectangle may be assigned as a witness to two solution points (once in the top recursion levels and once in the bottom levels). In such a case we create a duplicate of the respective side and consider them to be distinct witnesses.

Two witnesses added in the last \(\lceil logs\rceil\) recursion levels can intersect only if the recursive calls lie on the same root-to-leaf path in the recursion tree. Otherwise, they are separated by the median row of the lowest common ancestor in the recursion tree and cannot intersect. With this observation and the fact that the witnesses in _L_ form an independent set, we can bound the maximum clique size in the intersection graph of all witnesses by \(1+\lceil logs\rceil\).

This graph is an interval graph. Since interval graphs are perfect \[13\], there exists a \((1+\lceil logs\rceil)\)- coloring in this graph. Hence, there exists an independent set of witnesses of size \(1/(\lceil logs\rceil+1)\) times the size of the Manhattan solution. Taking all left or all right sides of demands in this independent set (whichever is larger) gives a _boundary_ independent set of size at least \(1/(2(1+\lceil logs\rceil))\) times the cost of the Manhattan solution.

We conclude the section by noting that the proof of Theorem 2 directly follows by combining Lemmata 6, 9 and 11. As mentioned in the introduction, the factor _O_(log_s_) in Lemma 11 is tight in the strong sense that there is an MinGMConn instance (_P,D_) with _s_ distinct _x_-coordinates such that \(\mathsf{OPT}(P,D)=\Omega(\mathsf{IS}(P,D)logs)\). See Appendix C.

## 5 A Sublogarithmic Approximation Algorithm

In this section, we give an overview of how to leverage the _O_(log_s_)-approximation for _s_-thin instances to design an \(O(\sqrt{logn})\)-approximation algorithm for general instances.

### Sub-instances.

Let (_P,D_) be an instance of MinGMConn and let _B_ be a bounding box for _P_, that is, \(P\subseteq B\). Let S={_S_<sub>1</sub>_,...,S<sub>s</sub>_} be a collection of _s_ vertical strips, ordered from left to right, that are obtained by drawing _s_-1 vertical lines that partition _B_. We naturally create _s_+1 sub-instances as follows. (See also Figure 4.) First, we have _s intra-strip instances_ \(\{(P_i,D_i)\}_{i\in[s]}\) such that \(P_i=P\cap S_i\) and \(D_i=D\cap(S_i\times S_i)\). Next, we have the _inter-strip instance_ \(\pi_\mathcal{S}(D)=(P',D')\) where \(P'\) is obtained by collapsing each strip in S into a single column and \(D'\) is obtained from collapsing demands accordingly. For each point \(p\in P\), denote by \(\pi_\mathcal{S}(p)\) a copy of _p_ in \(P'\) after collapsing. Note that this is a simplified description of the instances that avoids some technicalities. For a precise definition, see Appendix E.

### Sub-additivity of VS.

The following is our sub-additivity property that we use crucially in our divide-and-conquer algorithm.

**Lemma 12.** _If_ (_P,D_) _is an instance of_ MinGMConn _with strip subdivision_ S_, then_<tbc>

\(\mathsf{VS}(P,D)\ge\mathsf{VS}(\pi_\mathcal{S}(P,D))+\sum_{S\in\mathcal{S}}\mathsf{VS}(P\cap S,D\cap(S\times S)).\)

