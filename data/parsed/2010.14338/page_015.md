## A BST and Manhattan Problems

**MinASS problem.** Let \(p,q\in\mathbb{R}^2\) be points that are not horizontally or vertically aligned. Denote by \(\square_{p,q}\) the closed rectangle with two of its corners being _p_ and _q_. We say that this rectangle is _P_-empty if \(P\cap\square_{p,q}=\{p,q\}\); otherwise, we say that it is _P_-satisfied. We say that a collection of points \(P\subseteq\mathbb{R}^2\) is _arboreally satisfied_ if, for any pair \(p,q\in P\), the rectangle \(\square_{p,q}\) is _P_-satisfied. In the MinASS problem, we are given a collection of points \(P\subseteq\mathbb{R}^2\) such that no two points are horizontally or vertically aligned, and our goal is to compute a set \(Q\supseteq P\) such that _Q_ is arboreally satisfied.

**Theorem 13.** _Any set_ \(Q\subseteq\mathbb{R}^2\) _is arboreally satisfied if and only if there is a Manhattan path connecting every pair_ \(p,q\in Q\).

_Proof._ The "if" direction is quite obvious: Suppose there is a Manhattan path connecting every pair. Then, consider any \(p,q\in Q\) that is not aligned and \(\square_{p,q}\). Consider any point \(v\unknown\in\{p,q\}\) on the Manhattan path _Z_ connecting _p_ to _q_. Clearly, \(v\in\square_{p,q}\).

For the "only if" direction, assume that the set _Q_ is arboreally satisfied but (for contradiction) not Manhattan-connected. Consider points \(p,q\in Q\) that are not _M_-connected (if there are many such pairs, choose one that minimizes the \(\ell_1\)-distance ||_p-q_||<sub>1</sub>.) \(\square_{p,q}\) contains some point \(q'\unknown\in\{p,q\}\) and point \(q'\) is not at a corner of \(\square_{p,q}\) (otherwise, there would be a Manhattan path \(p\rightarrow q'\rightarrow q\).) Therefore, _p_ is not aligned with \(q'\) or _q_ is not aligned with \(q'\). Assume it is the former (the other case is similar). Then _p_ and \(q'\) is not connected, thus contradicting the choice of (_p,q_) since \(||p-q'||_1<||p-q||_1\).

## B Proof of Lemma 6

We repeat the proof from \[9\] and first show that \(\mathsf{IR}(P,D)\le\mathsf{VS}(P,D)\). Consider a set of independent monotone demands _R<sub>j</sub>=R(p<sub>j</sub>,q<sub>j</sub>_), for _j_=1_,...,k_, ordered decreasingly by width. Consider the rectangle _R<sub>j</sub>_, _j\>_1, which, among all rectangles intersecting the interior of _R_<sub>1</sub>, has minimal _x(p<sub>j</sub>_). Without loss of generality, we may assume that such a rectangle exists (otherwise _R_<sub>1</sub> can be separated trivially), and if there are several such rectangles, choose _j_ as small as possible.

