## 2.1 The Min-Sat Problem

For a point \(p\in\mathbb{R}^2\) in the plane, we denote by _p.x_ and _p.y_ its _x_- and _y_-coordinates, respectively. Given any pair \(p,p'\) of points, we say that they are _collinear_ if \(p.x=p'.x\) or \(p.y=p'.y\). If _p_ and \(p'\) are not collinear, then we let \(\square_{p,p^\prime}\) be the smallest closed rectangle containing both _p_ and \(p'\); note that _p_ and \(p'\) must be diagonally opposite corners of the rectangle.

**Definition 2.1** _We say that a non-collinear pair_ \(p,p'\) _of points is_ satisfied by a point \(p''\) _if_ \(p''\) _is distinct from p and_ \(p'\) _and_ \(p''\in\square_{p,p^\prime}\)_. We say that a set S of points is_ satisfied _iff for every non-collinear pair_ \(p,p'\in S\) _of points, there is some point_ \(p''\in S\) _that satisfies this pair._

We refer to horizontal and vertical lines as _rows_ and _columns_ respectively. For a collection of points _X_, the _active rows_ of _X_ are the rows that contain at least one point in _X_. We define the notion of _active columns_ analogously. We denote by _r(X_) and _c(X_) the number of active rows and active columns of the point set _X_, respectively. We say that a point set _X_ is a _semi-permutation_ if every active row contains exactly one point of _X_. Note that, if _X_ is a semi-permutation, then \(c(X)\le r(X)\). We say that _X_ is a _permutation_ if it is a semi-permutation, and additionally, every active column contains exactly one point of _X_. Clearly, if _X_ is a permutation, then _c(X_)=_r(X_)=|_X_|. We denote by _B_ the smallest closed rectangle containing all points of _X_, and call _B_ the _bounding box_.

We are now ready to define the Min-Sat problem. The input to the problem is a set _X_ of points that is a semi-permutation, and the goal is to compute a minimum-cardinality set _Y_ of points, such that \(X\cup Y\) is satisfied. We say that a set _Y_ of points is a _feasible solution_ for _X_ if \(X\cup Y\) is satisfied. We denote by OPT(_X_) the minimum value |_Y_| of any feasible solution _Y_ for _X_.<sup>1</sup> In the online version of the Min-Sat problem, at every time step _t_, we discover the unique input point from _X_ whose _y_-coordinate is _t_, and we need to decide which points with _y_-coordinate _t_ to add to the solution _Y_ . The Min-Sat problem is equivalent to the BST problem, in the following sense (see Appendix B for more details):

**Theorem 2.2 (**\[**DHI**<sup>+</sup>**09\]**)** _Any efficient_ \(\alpha\)_-approximation algorithm for_ Min-Sat _can be transformed into an efficient_ \(O(\alpha)\)_-approximation algorithm for BST’s, and similarly any online_ \(\alpha\)_- competitive algorithm for_ Min-Sat _can be transformed into an online_ \(O(\alpha)\)_-competitive algorithm for BST’s._

## 2.2 Basic Geometric Properties

The following observation is well known (see, e.g. Observation 2.1 from \[DHI<sup>+</sup>09\]). We include the proof Section C.2 of the Appendix for completeness.

**Observation 2.3** _Let Z be any satisfied point set. Then for every pair_ \(p,q\in Z\) _of distinct points, there is a point_ \(r\in\square_{p,q}\backslash\{p,q\}\) _such that r.x=p.x or r.y=p.y._

### Collapsing Sets of Columns or Rows.

Assume that we are given any set _X_ of points, and any collection C of consecutive active columns for _X_. In order to collapse the set C of columns,<tbc>

<sup>1</sup>We remark that in the original paper that introduced this problem \[DHI<sup>+</sup>09\], the value of the solution is defined as \(|X\cup Y|\), while our solution value is |_Y_|. It is easy to see that for any semi-permutation _X_ and solution _Y_ for _X_, \(|Y|\ge\Omega(|X|)\) must hold, so the two definitions are equivalent to within factor 2.

