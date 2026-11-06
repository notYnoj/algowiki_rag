## 4. Absorbers

In this section we analyze Algorithm 2.2. We wish to show that it is unlikely to abort. The next lemma provides a sufficient condition.

**Definition 4.1.** Let \(\ell>0\). A partial _n_-queens configuration _Q_ is \(\ell\)**-absorbing** if for every \((r,c)\in[n]^2\), it holds that \(|\mathcal{B}_Q(r,c)|\ge\ell\).

**Lemma 4.2.** _Suppose_ |_Q(T_)|=_T and Q(T_) _is_ 10(_n-T)-absorbing. Then Algorithm 2.2 does not abort._

_Proof._ Let _k=n-T_. Algorithm 2.2 aborts only if for some _t_ we have \(\left|\mathcal{B}_{R(t)}(r_t,c_t)\right|=0\). Thus, if for every \(0\le t<k\) it holds that \(\left|\mathcal{B}_{R(t)}(r_t,c_t)\right|\ge 10k-9t\), then the algorithm does not abort.

We prove this inductively. Let \((r,c)\in[n]^2\). By assumption, \(|\mathcal{B}_{R(0)}(r,c)|\ge 10k\). Now assume that for \(0\le t<k-1\) it holds that \(|\mathcal{B}_{R(t)}|\ge 10k-9t\). We wish to show that \(|\mathcal{B}_{R(t+1)}|\ge 10k-9t-9\). We note that _R(t_+1) is obtained from _R(t_) by removing one queen and adding two queens. Thus, the conclusion follows from the following two observations regarding partial _n_-queens configurations \(P_1,P_2\subseteq[n]^2\):

\(\bullet\) If _P_<sub>2</sub> is obtained from _P_<sub>1</sub> by removing a queen then \(|\mathcal{B}_{P_2}(r,c)|\ge|\mathcal{B}_{P_1}(r,c)|-1\). Indeed, if \((x,y)\in\mathcal{B}_{P_1}(r,c)\) then it does not share a diagonal with (_r,c_) and the four diagonals passing through (_r,y),(x,c_) are unoccupied. Since \(P_2\subseteq P_1\), these facts hold in _P_<sub>2</sub> as well. Thus, if \((x,y)\in P_2\) then \((x,y)\in\mathcal{B}_{P_2}(r,c)\). Since |_P_<sub>1</sub>\\_P_<sub>2</sub>|=1, the conclusion follows.<tbc>

\(\bullet\) If _P_<sub>2</sub> is obtained from _P_<sub>1</sub> by adding a queen then \(|\mathcal{B}_{P_2}(r,c)|\ge|\mathcal{B}_{P_1}(r,c)|-4\). Indeed, suppose \((x,y)\in\mathcal{B}_{P_1}(r,c)\backslash\mathcal{B}_{P_2}(r,c)\). Let (_q<sub>r</sub>,q<sub>c</sub>_) be the additional queen that is present in _P_<sub>2</sub>. By assumption, (_x,y_) does not share a diagonal with (_r,c_) and \((x,y)\in P_2\). Since \((x,y)\notin\mathcal{B}_{P_2}(r,c)\), this means that one of the diagonals containing (_r,y_) or (_x,c_) is occupied by (_q<sub>r</sub>,q<sub>c</sub>_). Therefore, one of the following holds:<tbc>

<tbc>\(q_r+q_c=r+y,q_r+q_c=x+c,q_r-q_c=r-y,q_r-q_c=x-c.\)<tbc>

<tbc>Since _r,c,q<sub>r</sub>,q<sub>c</sub>_ are fixed, each equality has at most one solution in \[_n_\]. Now, for each _x_ that solves one of the equations, there is at most one _y_ such that \((x,y)\in P_1\) (since _P_<sub>1</sub> contains at most one queen in each column). Similarly, for each _y_ solving one of the equations there is at most one _x_ such that \((x,y)\in P_1\). Therefore there are at most 4 absorbers \((x,y)\in\mathcal{B}_{P_1}(r,c)\) for which one of the equalities holds.

□

The next lemma asserts that w.h.p. _Q(T_) contains \(\Omega(n)\) absorbers for every position. By Proposition 3.1, w.h.p. _n_-|_Q(T_)|=_n-T=o(n_). Thus, it then follows from Lemma 4.2 that Algorithm 2.2 succeeds in constructing an _n_-queens configuration.

**Lemma 4.3.** _There exists a constant_ \(\beta>0\) _such that w.h.p. Q(T_) _is_ \((\beta n)\)_-absorbing._

The intuition is that _Q(T_) contains approximately _n_ queens, each occupying a single diagonal of each type (that is, one diagonal from upper-left to lower-right and one from upper-right to lower-left). However, the grid \[_n_\]<sup>2</sup> contains approximately 2_n_ diagonals<tbc>

