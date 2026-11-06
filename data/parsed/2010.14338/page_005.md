### 1.3 Outlook and Open Problems

Inspired by the study of structural properties of Manhattan connected sets and potential applications in BSTs, we initiate the study of MinGMConn by proving NP-hardness and giving several algorithmic results.

There are multiple interesting open problems. First, can we show that the BST problem is NP-hard? We hope that our construction and analysis using the new VS bound would be useful for this purpose. Another interesting open problem is to obtain a _o_(log_n_)-approximation for the edge-cost variant of the generalized Manhattan network problem.

Finally, it can be shown that our VS bound is sandwiched between OPT and IR. It is an interesting question to study the tightness of the VS bound when estimating the value of an optimal solution. Can we show that VS is within a constant factor from the optimal cost of BST? Can we approximate the value of VS efficiently within a constant factor?

## 2 Model & Preliminaries

Let \(P\subseteq\mathbb{R}^2\) be a set of points on the plane. We say that points \(p,q\in P\) are _Manhattan-connected (M-connected)_ in _P_ if there is a sequence of points _p=x_<sub>0</sub>_,x_<sub>1</sub>_,...,x<sub>k</sub>=q_ such that (i) the points _x<sub>i</sub>_ and _x_<sub>_i_+1</sub> are horizontally or vertically aligned for _i_=0_,...,k_-1, and (ii) the total length satis fies \(\sum_{i=0}^{k-1}||x_i-x_{i+1}||_1=||p-q||_1\).

In the _minimum generalized Manhattan connections_ (MinGMConn) _problem_, we are given a set of _input points P_ and their placement in a rectangular grid with integer coordinates such that there are no two points in the same row or in the same column. Additionally, we are given a set \(D\subseteq\{(p,q)|p,q\in P\}\) of _demands_. The goal is to find a set of points _Q_ of minimum cardinality such that _p_ and _q_ are M-connected with respect to \(P\cup Q\) for all \((p,q)\in D\). Denote by OPT(_P,D_) the size of such a point set. We differentiate between the points of _P_ and _Q_ by calling them _input points_ and _auxiliary points_, respectively. Since being M-connected is a symmetrical relation, we typically assume _x(p)\<x(q_) for all \((p,q)\in D\). Here, _x(p_) and _y(p_) denote the _x_- and _y_-coordinate of a point _p_, respectively. In our analysis, we sometimes use the notations \[_n_\]:={1,2_,...,n_} and \([n]_0:=[n]\cup\{0\}\), where \(n\in\mathbb{N}\).

#### Connection to Binary Search Trees.

In the _uniform_ case where all pairs of input points are connected by a demand, i.e. \(D=\{(p,q)|p,q\in P\}\), this problem is intimately connected to the Binary Search Tree (BST) problem in the geometric model \[9\]. Here, we are given a point set _P_ and the goal is to compute a minimum set _Q_ such that _every pair_ in \(P\cup Q\) is M-connected in \(P\cup Q\). Denote by BST(_P_) the optimal value of the BST problem.

#### Independent Rectangles and Vertically Separable Demands.

Following Demaine et al. \[9\], we define the independent rectangle number which is a lower bound on OPT(_P,D_). For a demand \((p,q)\in D\), denote by _R(p,q_) the (unique) axis-aligned closed rectangle that has _p_ and _q_ as two of its corners. We call it the _demand rectangle_ corresponding to (_p,q_). Two rectangles \(R(p,q),R(p',q')\) are called _non-conflicting_ if none contains a corner of the other in its interior. We say a subset of demands \(D'\subseteq D\) is _independent_, if all pairs of rectangles in \(D'\) are non-conflicting. Denote by IR(_P,D_) the maximum integer _k_ such that there is an independent subset \(D'\) of size _k_. We refer to _k_ as the _independent rectangle number_.

For uniform demands, the problem admits a 2-approximation. Here, the independent rectangle number plays a crucial role. Specifically, it was argued in Harmon’s PhD thesis \[16\] that a natural greedy algorithm costs at most the independent rectangle number and thus yields a 2-approximation.<tbc>

