## 8 Algorithms for new types of fair stable matchings

**Algorithm 2** REDI-COL(_I,M,Q,M<sub>opt</sub>_), subroutine for Algorithm 1. Column operation for the current column _d<sub>U</sub>(M_). Returns _M<sub>opt</sub>_, the best stable matching found so far (according to the regret-equality score).

**Require:** An instance _I_ of smi, stable matching _M_, the closure of _M_, _Q_ and _M<sub>opt</sub>_ the best stable matching found so far (according to the regret-equality score).

**Ensure:** Finds the best stable matching (according to the regret-equality score) found when incrementally eliminating women of worst rank from the current matching, without increasing the men’s degree. If an improvement is made then _M<sub>opt</sub>_ is updated. _M<sub>opt</sub>_ is returned. All variables used within Algorithm 2 are understood to be local.

1: \(a\leftarrow d_U(M)\)

2: **while true do**

3: **if** _r(M)\<r(M<sub>opt</sub>_) **then**

4: \(M_{opt}\leftarrow M\)

5: **end if**

6: **if** \(d_U(M)\ge d_W(M)\) **then** \(\triangleright\) Further rotations for this column would only increase the difference in degree of men and women.

7: **return** _M<sub>opt</sub>_

8: **end if**

9: \(b\leftarrow d_W(M)\)

10: \(Q'\leftarrow c(R_b(M))\backslash Q\)

11: **if** \(d_U(M/Q')>a\vee d_W(M/Q')=b\) **then**

12: **return** _M<sub>opt</sub>_

13: **else**

14: \(M\leftarrow M/Q'\triangleright\) Rotations in \(Q'\) are eliminated in order defined by the rotation poset of _I_.

15: \(Q\leftarrow Q\cup Q'\)

16: **end if**

17: **end while**

where \(1\le t\le n\), is then the process of deleting pair (_m<sub>i</sub>,w<sub>j</sub>_) for each (_m<sub>i</sub>,w<sub>j</sub>_) such that rank(_m<sub>i</sub>,w<sub>j</sub>)\>t_. An analogous definition holds for women. For a given SMI instance _I_, first find the regret-equality score _r_ of the regret-equal stable matching using Algorithm REDI in _O(d_<sub>0</sub>_nm_) time. Then, iterate over all possible man-woman degree pairs (_a,b_) such that |_a-b_|=_r_ (there are _O(n_) such pairs). For each such degree pair (_a,b_), truncate men at _a_ and women at _b_, creating instance \(I'\). Then, for each of the _O(m_) man-woman pairs (_m<sub>i</sub>,w<sub>j</sub>_) in \(I'\), fix _m<sub>i</sub>_ with his _a_th-choice partner and _w<sub>j</sub>_ with her _b_th-choice partner (where ranks are taken with respect to instance _I_), if possible. If this is not possible then continue to the next degree pair. Assume that \(w'_j\) is _m<sub>i</sub>_’s _a_th-choice partner, and \(m'_i\) is _w<sub>j</sub>_’s _b_th-choice partner. In \(I'\), we now delete pairs \((m''_i,w''_j)\) for any \(w''_j\) such that _m<sub>i</sub>_ prefers \(w''_j\) to \(w'_j\) and \(w''_j\) prefers _m<sub>i</sub>_ to \(m''_i\). Also delete the pair \((m''_i,w''_j)\) for any \(m''_i\) such that _w<sub>j</sub>_ prefers \(m''_i\) to \(m'_i\) and \(m''_i\) prefers _w<sub>j</sub>_ to \(w''_j\). Next we delete all remaining preference list elements of _m<sub>i</sub>_ except \(w'_j\) and all remaining preference list elements of _w<sub>j</sub>_ except \(m'_i\). The Gale-Shapley Algorithm is run to check that a stable matching of size _n_ exists in \(I'\). If no such stable matching exists then we move on to the next degree pair. Feder’s Algorithm may then be used to find an egalitarian stable matching in the reduced smi instance \(I'\) in _O(m_<sup>1.5</sup>) time (using the original ranks in _I_ as costs). This makes a total of _O(nm_<sup>2.5</sup>) time to find a regret-equal stable matching with minimum cost.

