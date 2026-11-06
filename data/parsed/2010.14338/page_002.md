<tbc>computational geometry. Below, we briefly discuss them, as well as the implications of our results in those contexts.

**Binary Search Trees (BSTs).**

The _Dynamic Optimality Conjecture_ \[18\] is one of the most fundamental open problems in dynamic data structures, postulating the existence of an _O_(1)- competitive binary search tree. Despite continuing efforts and important progress for several decades (see, e.g., \[10, 6, 9, 17, 2\] and references therein), the conjecture has so far remained elusive, with the best known competitive ratio of _O_(loglog_n_) obtained by Tango trees \[10\]. Even in the offline setting, the best known algorithm is also a _O_(loglog_n_)-approximation; the problem is not even known to be NP-hard. Demaine, Harmon, Iacono, Kane, and Pătraşcu \[9\] showed that approximating BST is equivalent (up to a constant in the approximation factor) to approximating the node-cost Manhattan problem with "evolving demand" (that is, points added to the solution create demands to all existing points).<sup>1</sup>

The long-standing nature of the _O_(loglog_n_) upper bound could suggest the lower bound answer. However, the understanding of lower bound techniques for BSTs has been completely lacking: It is not even known whether the problem is NP-hard! Our work is inspired by the following question.

Is it NP-hard to (exactly) compute a minimum cost binary search tree?

We are, unfortunately, unable to answer this question. In this paper, we instead present a proof that a natural generalization of the problem in the geometric view (which is exactly our MinGMConn) is NP-hard<sup>2</sup>. We believe that our construction and its analysis could be useful in further study of the BST problem from the perspective of lower bounds.

**Edge-Cost Manhattan Problem.**

Closely related to MinGMConn is the edge-cost variant of Manhattan Network \[14\]: Given \(P\subseteq\mathbb{R}^2\), our goal is to compute \(Q\subseteq\mathbb{R}^2\) such that every pair in _P_ is _M_-connected in \(G_{P\cup Q}\), while minimizing the total lengths of the edges used for the connections. The problem is motivated by various applications in city planning, network layouts, distributed algorithms and VLSI circuit design, and has received attention in the computational geometry community. Since the edge-cost variant is NP-hard \[5\], the focus has been on approximation algorithms. Several groups of researchers presented 2-approximation algorithms \[15, 4\], and this has remained the best known approximation ratio. Generalizations of the edge-cost variant have been proposed<tbc>

<sup>1</sup>In fact, the problem stated in \[9\] is called MinASS which appears different from Manhattan problem, but they can be shown to be equivalent. Please see Appendix A for a detailed discussion on the equivalence. <sup>2</sup>Demaine et al. \[9\] proves an NP-hardness result for MinGMConn with uniform demands but allowing the input to contain multiple points on the same row. Their result is incomparable to ours.

P4
P4
P3
P3
P1
P1
q2
P2
P2
q1

Figure 1: Left: A Manhattan instance with input points _P_={_p_<sub>1</sub>_,p_<sub>2</sub>_,p_<sub>3</sub>_,p_<sub>4</sub>}, drawn as black disks, and demands \(D=\{(p_1,p_2),(p_1,p_4),(p_2,p_3),(p_3,p_4)\}\), drawn as orange rectangles. Right: The Manhattan Graph \(G_{P\cup Q}\) of a feasible solution _Q_, with points in _Q_ drawn as crosses. Points _p_<sub>2</sub> and _p_<sub>4</sub> are Manhattan-connected via the red path _p_<sub>2</sub> - _q_<sub>1</sub> - _p_<sub>3</sub> - _q_<sub>2</sub> - _p_<sub>4</sub>. Points _p_<sub>1</sub> and _p_<sub>3</sub> are not Manhattan-connected but also not a demand pair in _D_.

