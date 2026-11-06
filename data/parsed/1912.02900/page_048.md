<tbc>If \(\sigma\) is any ordering of the auxiliary columns in L, and \(T=T_\sigma\) is the corresponding partitioning tree, then any point set _Y_ that is a special solution for _X_ is also called a _T-special solution_ (although the notion of the solution _Y_ being special does not depend on the tree _T_, this notion will be useful for us later; in particular, a convenient way of thinking of a _T_-special solution is that every point of _Y_ must lie on an active row of _X_, and on a column that serves as a boundary for some strip _S(v_), where \(v\in V(T)\).)

## 6.2 Redundant Points and Reduced Point Sets

Consider a semi-permutation _X_, that we think of as a potential input to the Min-Sat problem. We denote _X_={_p_<sub>1</sub>_,...,p<sub>m</sub>_}, where the points are indexed in their natural bottom-to-top order, so (_p_<sub>1</sub>)_.y\<(p_<sub>2</sub>)_.y\<...\<(p<sub>m</sub>).y_. A point _p<sub>i</sub>_ is said to be _redundant_, iff (_p<sub>i</sub>).x_=(_p_<sub>_i_+1</sub>)_.x_=(_p_<sub>_i_-1</sub>)_.x_. We say that a semi-permutation _X_ is in the _reduced form_ if there are no redundant points in _X_; in other words, if _p_<sub>_i_-1</sub>_,p<sub>i</sub>,p_<sub>_i_+1</sub> are three points lying on three consecutive active rows, then their _x_-coordinates are not all equal. We use the following observation and lemma.

**Observation 6.2** _Let X be a semi-permutation, and let_ \(X'\subseteq X\) _be any point set, that is obtained from X by repeatedly removing redundant points. Then_ \(\mathsf{OPT}(X')\le\mathsf{OPT}(X)\).

**Proof:** It is sufficient to show that, if \(X''\) is a set of points obtained from _X_ by deleting a single redundant point _p<sub>i</sub>_, then \(\mathsf{OPT}(X'')\le\mathsf{OPT}(X)\). Let _R_ denote the row on which point _p<sub>i</sub>_ lies, and let \(R'\) be the row containing _p_<sub>_i_-1</sub>. Let _Y_ be the optimal solution to instance _X_. We assume w.l.o.g. that _Y_ is a canonical solution. Consider the set \(Z=X\cup Y\) of point, and let \(Z'\) be obtained from _Z_ by collapsing the rows \(R,R'\) into the row \(R'\) (since _Y_ is a canonical solution for _X_, no points of \(X\cup Y\) lie strictly between the rows \(R,R'\)). From Observation 2.4, \(Z'\) remains a satisfied point set. Setting \(Y'=Z'\backslash X''\), it is easy to verify that \(Y'\) is a feasible solution to instance \(X''\), and moreover, \(|Y'|\le|Y|\). Therefore, \(\mathsf{OPT}(X'')\le|Y'|\le|Y|\le\mathsf{OPT}(X)\). □

**Lemma 6.3** _Let X be a semi-permutation, and let_ \(X'\subseteq X\) _be any point set, that is obtained from X by repeatedly removing redundant points. Let Y be any feasible solution for_ \(X'\) _such that every point of Y lies on a row that is active for_ \(X'\)_. Then Y is also a feasible solution for X._

**Proof:** It is sufficient to show that, if \(X''\) is a set of points obtained from _X_ by deleting a single redundant point _p<sub>i</sub>_, and _Y_ is any canonical solution for \(X''\), then _Y_ is also a feasible solution for<tbc>





(a) Canonical Solution

(b) Special Solution

Figure 7: Canonical and _T_-special solutions of _X_. The input points are shown as circles; the points that belong to the solution _Y_ are shown as squares.

