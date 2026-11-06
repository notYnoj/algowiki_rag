we replace C with a single representative column _C_ (for concreteness, we use the column of C with minimum _x_-coordinate). For every point \(p\in X\) that lies on a column of C, we replace _p_ with a new point, lying on the column _C_, whose _y_-coordinate remains the same. Formally, we replace point _p_ with point (_x,p.y_), where _x_ is the _x_-coordinate of the column _C_. We denote by _X_<sub>|C</sub> the resulting new set of points. We can similarly define collapsing set of rows. The following useful observation is easy to verify; the proof appears in Section C.3 of Appendix.

**Observation 2.4** _Let S be any set of points, and let_ C _be any collection of consecutive active columns (or rows) with respect to S. If S is a satisfied set of points, then so is S_<sub>|C</sub>.

### Canonical Solutions.

We say that a solution _Y_ for input _X_ is _canonical_ iff every point \(p\in Y\) lies on an active row and an active column of _X_. It is easy to see that _any_ solution can be transformed into a canonical solution, without increasing its cost. The proof of the following observation appears in Section C.4 of Appendix.

**Observation 2.5** _There is an efficient algorithm, that, given an instance X of_ Min-Sat _and any feasible solution Y for X, computes a feasible canonical solution_ \(\hat{Y}\) _for X with_ \(|\hat{Y}|\le|Y|\).

## 2.3 Partitioning Trees

We now turn to define partitioning trees, that are central to both defining the WB-1 bound and to describing our algorithm.

Let _X_ be the a set of points that is a semi-permutation. We can assume without loss of generality that every column with an integral _x_-coordinate between 1 and _c(X_) inclusive contains at least one point of _X_. Let _B_ be the bounding box of _X_. Assume that the set of active columns is {_C_<sub>1</sub>_,...,C<sub>a</sub>_}, where _a=c(X_), and that for all \(1\le i\le a\), the _x_-coordinate of column _C<sub>i</sub>_ is _i_. Let L be the set of all vertical lines with half-integral _x_-coordinates between 1+1/2 and _a_-1/2 (inclusive). Throughout, we refer to the vertical lines in L as _auxiliary columns_. Let \(\sigma\) be an arbitrary ordering of the lines of L and denote \(\sigma=(L_1,L_2,\dots,L_{a-1})\). We define a hierarchical partition of the bounding box _B_ into vertical strips using \(\sigma\), as follows. We perform _a_-1 iterations. In the first iteration, we partition the bounding box _B_, using the line _L_<sub>1</sub>, into two vertical strips, _S<sub>L</sub>_ and _S<sub>B</sub>_. For \(1<i\le a-1\), in iteration _i_ we consider the line _L<sub>i</sub>_, and we let _S_ be the unique vertical strip in the current partition that contains the line _L<sub>i</sub>_. We then partition _S_ into two vertical sub-strips by the line _L<sub>i</sub>_. When the partitioning algorithm terminates, every vertical strip contains exactly one active column.



Figure 1: Input point set _X_ and a partitioning tree _T_.

