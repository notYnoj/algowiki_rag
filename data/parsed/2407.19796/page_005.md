## 4 Algorithms for SegE

In this section, we give a matching upper bound for SegE. We do so by presenting an algorithm for the function version of the problem, MinSegE, running in _O(mn_) time, where _m_=|_P_| and _n_=|_T_|.

### 4.1 _O(mn_)-time Algorithm for general \(f\ge 1\)

Shapira and Storer considered Problem 2 in the context of _generalized edit distance problems_ with block deletions, and proposed an _O(mn_<sup>2</sup>)-time algorithm (Algorithm 2 of \[16\]). However, there is a room for improvements in their algorithm, e.g., employing a standard memorization technique in function during\_deletion appears to provide _n_ times speedup. On the other hand, Problem 2 can be seen as a special case of the global alignment with _affine gap penalty_, where the _gap open penalty_ equals 1, the _gap extension penalty_ equals 0, and any gap in _P_ is prohibited. Our algorithm below is inspired by alignment algorithms with affine gap penalties \[17, 8, 9, 3, 7\].

**Theorem 3.** _The problem MinSegE can be solved in O_(|_T_||_P_|) _time._

_Proof._ By definition of \(SubSeq^{\le f}(T)\), if \(P\in SubSeq^{\le f}(T)\) holds, then _P_ is obtained by deleting (1) a (possibly empty) prefix of _T_, (2) a (possibly empty) suffix of _T_, and (3) at most _f_-1 non-empty factors of _T_ that are neither prefix nor suffix from _T_. The smallest such number _f_ can be computed as _f=d_+1, where _d_ is the minimum number of _edit operations_ to obtain _P_ from _T_ by (i) deleting a prefix _y_ that changes _yx_ into _x_ with cost 0, (ii) deleting a suffix _y_ that changes _xy_ into _x_ with cost 0, and (iii) deleting a string _y_ that changes _xyz_ into _xz_ with cost 1, where \(x,y,z\in\Sigma^+\). Thus, the standard dynamic programming algorithm \[18\] can be applied, by designing the cost function properly as follows. Both the _substitution_ and _insertion_ operations cost \(\infty\) to be prohibited. The _block deletion_ of _y_ costs 0 if _y_ is either prefix or suffix, and costs 1 otherwise. Precisely, we can compute the smallest cost _d_ as follows. We utilize two tables _D_ and _E_ of size \(n\times m\), where _n_=|_T_| and _m_=|_P_|. The value _D_\[_i,j_\] indicates the edit distance between _T_\[1.._i_\] and _P_\[1.._j_\] such that the last operation is a character deletion of _T_, and the value _E_\[_i,j_\] gives the edit distance between _T_\[1.._i_\] and _P_\[1.._j_\], where _D_ and _E_ both assume that the deletion of a suffix of _T_ costs 1 instead of 0. These two tables are linked by the following recurrence relations.

\(D[i,0]=E[i,0]=0\text{for}0\le i\le n,\)<br>
\(D[0,j]=E[0,j]=\infty\text{for}1\le j\le m,\)<br>
\(D[i,j]=min\{D[i-1,j],E[i-1,j]+1\},\text{and}\)<br>
\(E[i,j]=\left\{\begin{array}{ c c }
min\{E[i-1,j-1],D[i,j]\} & (T[i]=P[j]) \\
D[i,j] & (T[i]\neq P[j])
\end{array}\right.\)<br>
\(\text{for}1\le i\le n\text{and}0\le j\le m.\)

Note that, in the third equation, the "+1" term indicates the cost to begin a block deletion. The smallest cost _d_ is given by \(min_{1\le i\le n}\{E[i,m]\}\), because we allow to delete a suffix of _T_ with cost 0. If \(d=\infty\), it means that \(P\notin SubSeq(T)\).

The total running time is _O_(|_T_||_P_|).

### 4.2 _O(m+n_)-time Algorithm for \(f\le 2\)

We show a faster algorithm for a special case of SegE where the segmentation number _f_ is at most two. If _f_=1, the problem is nothing more than the standard exact pattern matching, so that it can be solved in _O_(|_T_|+|_P_|) time with _O_(1) space \[6, 4\]. Here, we focus on the case where _f_=2.

