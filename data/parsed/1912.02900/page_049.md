<tbc>_X_. We can then apply this argument iteratively, until we obtain a set of points that is in a reduced form.

Consider any feasible canonical solution _Y_ to instance \(X''\). We claim that \(X\cup Y\) is a feasible set of points. Indeed, consider any two points \(p,q\in X\cup Y\) that are not collinear. If both points are distinct from the point _p<sub>i</sub>_, then they must be satisfied in \(X\cup Y\) , since both these points lie in \(X''\cup Y\) . Therefore, we can assume that _p=p<sub>i</sub>_. Notice that \(q\neq p_{i-1}\) and \(q\neq p_{i+1}\), since otherwise _p_ and _q_ must be collinear. Moreover, _q_ cannot lie strictly between the row of _p_<sub>_i_-1</sub> and the row of _p_<sub>_i_+1</sub>, as we have assumed that every point of _Y_ lies on a row that is active for \(X'X''\). But then it is easy to verify that either point _p_<sub>_i_-1</sub> lies in \(\square_{p,q}\) (if _q_ is below _p_), or point _p_<sub>_i_+1</sub> lies in \(\square_{p,q}\) (otherwise). In either case, the pair (_p,q_) is satisfied in \(X\cup Y\) . □

From Lemma 6.3, whenever we need to solve the Min-Sat problem on an instance _X_, it is sufficient to solve it on a sub-instance, obtained by iteratively removing redundant points from _X_. We obtain the following immediate corollary of Lemma 6.3.

**Corollary 6.4** _Let X be a semi-permutation, and let_ \(X'\subseteq X\) _be any point set, that is obtained from X by repeatedly removing redundant points. Let Y be any special feasible solution for_ \(X'\)_. Then_ \(Y'\) _is also a special feasible solution for X._

Lastly, we need the following lemma.

**Lemma 6.5** _Let X be a point set that is a semi-permutation in reduced form. Then_ \(\mathsf{OPT}(X)\ge|X|/4-1\).

**Proof:** Since _X_ is a semi-permutation, every point of _X_ lies on a distinct row; we denote |_X_|=_n_. Let _X_={_p_<sub>1</sub>_,...,p<sub>n</sub>_}, where the points are indexed in the increasing order of their _y_-coordinates. Let \(\Pi=\{(p_i,p_{i+1})|1\le i<n\}\) be the collection of all consecutive pairs of points in _X_. We say that the pair (_p<sub>i</sub>,p_<sub>_i_+1</sub>) is _bad_ iff both _p<sub>i</sub>_ and _p_<sub>_i_+1</sub> lie on the same column. From the definition of the reduced form, if (_p<sub>i</sub>,p_<sub>_i_+1</sub>) is a bad pair, then both (_p_<sub>_i_-1</sub>_,p<sub>i</sub>_) and (_p_<sub>_i_+1</sub>_,p_<sub>_i_+2</sub>) are good pairs. Let \(\Pi'\subseteq\Pi\) be the subset containing all good pairs. Then \(|\Pi'|\ge(|\Pi|-1)/2\ge n/2-1\). Next, we select a subset \(\Pi''\subseteq\Pi'\) of pairs, such that \(|\Pi''|\ge|\Pi'|/2\ge n/4-1\), and every point in _X_ belongs to at most one pair in \(\Pi''\). Since every point in _X_ belongs to at most two pairs in \(\Pi'\), it is easy to see that such a set exists. Let _Y_ be an optimal solution to instance _X_.

Consider now any pair (_p<sub>i</sub>,p_<sub>_i_+1</sub>) of points in \(\Pi''\). Then there must be a point \(y_i\in Y\) that lies in the rectangle \(\square_{p_i,p_{i+1}}\). Moreover, since all points of _X_ lie on distinct rows, and each such point belongs to at most one pair in \(\Pi''\), for \(i\neq j\), \(y_i\neq y_j\). Therefore, \(|Y|\ge|\Pi''|\ge n/4-1\). □

## 6.3 The Algorithm Description

Suppose we are given an input set _X_ of points that is a semi-permutation. Let _T_ be any partitioning tree for _X_. We say that _T_ is a _balanced_ partitioning tree for _X_ iff for every non-leaf vertex \(v\in V(T)\) the following holds. Let \(v'\) and \(v''\) be the children of _v_ in the tree _T_. Let \(X'\) be the set of all input points lying in strip _S(v_), and let \(X'',X'''\) be defined similarly for \(S(v')\) and \(S(v'')\). Let _c_ be the number of active columns in instance \(X'\), and let \(c'\) and \(c''\) be defined similarly for \(X''\) and \(X'''\). Then we require that \(c',c''\le\lceil c/2\rceil\).

Given a partitioning tree _T_, we denote by \(\Lambda_i\) the set of all vertices of _T_ that lie in the _i_th _layer_ of _T_ - that is, the vertices whose distance from the root of _T_ is _i_ (so the root belongs to \(\Lambda_0\)). The<tbc>

