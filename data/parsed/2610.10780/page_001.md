<tbc>Deterministic Distance Selection in _O(n_<sup>4/3</sup>) Time

Haitao Wang<sup>∗</sup>

**Abstract**

Let _P_ be a set of _n_ points in the plane. Given an integer _K_ with \(1\le K\le\genfrac(){pt}{2}{n}{2}\), the distance selection problem asks for the _K_-th smallest distance among all pairwise distances of the points of _P_. The problem has been studied extensively over the past four decades. Recently, Chan and Zheng (2023) gave a randomized algorithm with _O(n_<sup>4/3</sup>) expected running time, while the best known deterministic algorithm runs in _O(n_<sup>4/3</sup>log_n_) time. In this paper, we present a deterministic _O(n_<sup>4/3</sup>)-time algorithm for the problem, matching the best known randomized complexity.

We also consider the more general bichromatic version of the problem, where two point sets _A_ and _B_ are given, with _m_=|_A_| and _n_=|_B_|, and the goal is to find the _K_-th smallest distance among the _mn_ distances between points of _A_ and points of _B_. For this problem, the best previously known algorithm runs in _O_((_m_log_n+n_log_m+m_<sup>2/3</sup>_n_<sup>2/3</sup>)log(_m+n_)) time. We present a new deterministic algorithm with running time _O(m_log<sup>2</sup>_n+n_log<sup>2</sup>_m+m_<sup>2/3</sup>_n_<sup>2/3</sup>).

_Keywords:_ Distance selection, geometric optimization, distance counting, hierarchical cuttings, biclique partitions, range searching

## 1 Introduction

Let _P_ be a set of _n_ points in the plane. Given an integer _K_ with \(1\le K\le\genfrac(){pt}{2}{n}{2}\), the _distance selection problem_ asks for the _K_-th smallest distance among all pairwise distances of the points of _P_.

Distance selection is a fundamental problem in computational geometry. Besides its intrinsic interest, it serves as a prototype for a broad class of geometric optimization problems whose optimal objective values are realized by interpoint distances [3, 5, 9, 18, 19, 27]. One may even regard it as a geometric analogue of the classical selection problem [7]. The problem can be solved trivially in _O(n_<sup>2</sup>) time. The first subquadratic algorithm was given by Chazelle [11]. Later, Agarwal, Aronov, Sharir, and Suri [2] obtained an _O(n_<sup>3/2</sup>log<sup>5/2</sup>_n_)-time algorithm, which was subsequently improved by Goodrich [17] to _O(n_<sup>4/3</sup>log<sup>8/3</sup>_n_) time. Katz and Sharir [20] further improved the running time to _O(n_<sup>4/3</sup>log<sup>2</sup>_n_). Wang and Zhao recently reduced it to _O(n_<sup>4/3</sup>log_n_) in ESA 2023 [28].

All of the above algorithms are deterministic. Several randomized algorithms are also known. The randomized algorithm of Agarwal, Aronov, Sharir, and Suri [2] runs in _O(n_<sup>4/3</sup>log<sup>8/3</sup>_n_) expected time. Matoušek [22] later improved the bound to _O(n_<sup>4/3</sup>log<sup>2/3</sup>_n_) expected time. Most recently, Chan and Zheng [10] obtained a randomized algorithm of _O(n_<sup>4/3</sup>) expected time. Their algorithm uses random sampling and is reminiscent of the randomized linear-time selection algorithm of Floyd and Rivest [16]. The complexity can also be expressed as a function of _K_. In particular, combining Chan’s randomized optimization framework [8] with the result of Wang [24] yields an _O(n_log_n+n_<sup>2/3</sup>_K_<sup>1/3</sup>log<sup>5/3</sup>_n_)-time randomized algorithm, which is particularly attractive when _K_ is relatively small.

Like Hopcroft’s problem and several related geometric range searching problems [10, 15], it is possible that distance selection has complexity \(\Theta(n^{4/3})\), although no matching lower bound is currently known. In particular, many problems whose best known upper bounds are _O(n_<sup>4/3</sup>) admit \(\Omega(n^{4/3})\) lower bounds, at least in a restricted partition-based computational model [15], such as Hopcroft’s<tbc>

<sup>∗</sup>Kahlert School of Computing, University of Utah, Salt Lake City, UT 84112, USA. `haitao.wang@utah.edu`

