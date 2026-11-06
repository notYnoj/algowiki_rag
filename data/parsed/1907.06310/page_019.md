**Theorem 7.5.** _The crossing bound is approximately monotone._

_Proof._ Let _T_<sub>1</sub>_,...,T<sub>m</sub>_ be the after-trees of Move-to-Root’s execution of _X_=(_x_<sub>1</sub>_,...,x<sub>m</sub>_) starting from _T_, and let \(m\ge e_1>e_2>\cdots>e_p\ge 1\) be a sequence of request times. Set _X_<sub>0</sub>=_X_ and for \(1\le i\le p\) form _X<sub>i</sub>_ by removing request _e<sub>i</sub>_ from _X_<sub>_i_-1</sub>. We induct on _p_ to show that \(\Lambda(X_p,T)\le\Lambda(X,T)+3\sum_{i=1}^p\ell_{T_{e_i-1}}(x_{e_i})\) where _T_<sub>0</sub>=_T_, which suffices to establish that the crossing bound has subsequence overhead at most four. The statement is trivial when _p_=0. Now suppose \(\Lambda(X_{p-1},T)\le\Lambda(X,T)+3\sum_{i=1}^{p-1}\ell_{T_{e_i-1}}(x_{e_i})\). Let _y=x<sub>e<sub>p</sub></sub>_ and let _W_ and _Z_ respectively be the first _e<sub>p</sub>_-1 and final _m-e<sub>p</sub>_-(_p_-1) requests in _X_<sub>_p_-1</sub>, so that \(X_{p-1}=W\oplus(y)\oplus Z\) and \(X_p=W\oplus Z\). Let _S=T_<sub>_e<sub>p</sub>_-1</sub>, so that \(\Lambda(X_{p-1},T)=\Lambda(W,T)+\Lambda((y)\oplus Z,S)\) and \(\Lambda(X_p,T)=\Lambda(W,T)+\Lambda(Z,S)\). Note that \(\Lambda((y)\oplus Z,S)=\ell_S(y)+\Lambda(Z,\text{move-to-root}(S,y))\). Thus, \(\Lambda(X_p,T)-\Lambda(X_{p-1},T)=\Lambda(Z,S)-\Lambda(Z,\text{move-to-root}(S,y))-\ell_S(y)\), which by Theorem 7.4 is at most \(3\ell_S(y)\). Therefore, \(\Lambda(X_p,T)\le\Lambda(X_{p-1},T)+3\ell_{T_{e_p-1}}(x_{e_p})\), and the hypothesis holds for _p_ request removals.

Our presentation of the crossing bound is based on Iacono’s work \[37, 38\]. Move-to-Root, introduced by Allen and Munro \[3\], is the earliest example of a self-adjusting binary search tree algorithm. The crossing bound is not strictly monotone. For example, \(\Lambda(Y,T)>\Lambda(X,T)\) when _X_=(4,5,3), _Y_=(5,3) and postorder(_T_)=(3,2,5,6,4,7,1). We had not realized this when writing our SODA paper, whose treatment of the crossing bound contains several mistakes \[46\].

## 8 The Way Forward

Our numerical experiments indicate that Splay’s cost never exceeds four times the sum of an instance’s crossing bound and initial tree size, which would imply dynamic optimality. Moreover, the crossing costs of Splay and Move-to-Root are so tightly coupled that the difference between them may well be at most linear in initial tree size. Additionally, the keys in the crossing nodes of these algorithms’ executions are quite similar, albeit sometimes offset from each other in symmetric order by a small amount. We have tried to prove these statements, to no avail. We believe our failures are not incidental, and that there are structural obstacles in the way of establishing dynamic optimality in this manner. The difficulty arises from temporal spread. Typically, about half of<tbc>

J
K
W1
O
Y
W2
W1
W2
W3
W4
W3
W4
Y

Figure 6: Schematic of the window subtrees _J_ and _K_. If _z_ is a horizontally striped node then _A_=1. If _z_ is a vertically striped node then _B_=1, and if _z_ is a cross-hatched node then _AB_=1.

