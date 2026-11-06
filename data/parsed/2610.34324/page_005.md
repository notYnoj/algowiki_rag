<tbc>because each \(c\notin\{a,b\}\) lies in _m_-3 pairs disjoint from {_a,b_}. So _Ax_=-(_m_-3)_x_ on _E_. The space \(\mathrm{span}(\mathbf{1})\oplus E\) is the range of _N_, since \(\mathbf{1}=N(\frac{1}{2}\mathbf{1})\); its orthogonal complement is \(\mathrm{ker}N^\top=\{x:\sum_{b\neq a}x_{ab}=0\text{for all}a\}\). For such _x_ also \(\sum_ex_e=\frac{1}{2}\sum_a\sum_{b\neq a}x_{ab}=0\), so

\((Ax)_{ab}=\sum_ex_e-\sum_{b^\prime\neq a}x_{ab^\prime}-\sum_{a^\prime\neq b}x_{a^\prime b}+x_{ab}=x_{ab},\)

the last term correcting for the pair {_a,b_}, which is subtracted twice. Finally _A_**1**=_d_**1**. Hence _L=dI-A_ has the stated eigenvalues, and _d+m_-3_\>d_-1. □

_Proof of Theorem 1.1._ Let \(\pi=I-\frac{1}{m}J\) be the orthogonal projector of R_<sup>m</sup>_ onto \(\mathbf{1}^\perp\). By Lemma 3.1 and the identity \(N^\top N=(m-2)I\) on \(\mathbf{1}^\perp\), the orthogonal projector onto _E_ is \(P_E=\frac{1}{m-2}N\pi N^\top\), with entries

\((P_E)_{ef}=\frac{1}{m-2}\big(\mathbf{1}_e-\frac{2}{m}\mathbf{1}\big)^\top\big(\mathbf{1}_f-\frac{2}{m}\mathbf{1}\big)=\frac{|e\cap f|-\frac{4}{m}}{m-2},\)

where **1**_<sub>e</sub>=e<sub>a</sub>+e<sub>b</sub>_ is the indicator vector of _e_={_a,b_}. The matrix \(X^*=\frac{n}{m-1}P_E=\frac{m}{2}P_E\) has entries \(\frac{m|e\cap f|-4}{2(m-2)}\) ; its diagonal entries \((|e\cap f|=2)\) are 1, it is positive semidefinite, and its range is _E_. By Lemma 2.1, _X_<sup>∗</sup> is optimal and \(F(G)=\{X\in\mathcal{E}_n:\mathrm{range}X\subseteq E\}\).

It remains to show that every optimum equals _X_<sup>∗</sup>. By Lemma 2.3, it suffices to prove that the matrices \((\pi\mathbf{1}_e)(\pi\mathbf{1}_e)^\top\) span the symmetric operators on \(\mathbf{1}^\perp\). Indeed, the rows of _N_ restricted to this subspace are represented by \(\pi\mathbf{1}_e\), and the positive definite scalar operator \(M_0=\frac{m}{2(m-2)}I\) gives _X_<sup>∗</sup>.

Suppose a symmetric operator _M_ on \(\mathbf{1}^\perp\) is orthogonal to all these rank-one matrices. Extend it to a symmetric matrix \(\widetilde{M}\) on R_<sup>m</sup>_ by setting \(\widetilde{M}\mathbf{1}=0\). Orthogonality then reads

\(\widetilde{M}_{aa}+2\widetilde{M}_{ab}+\widetilde{M}_{bb}=0(a\neq b).\)

Let \(\delta_a=\widetilde{M}_{aa}\) and \(T=\sum_a\delta_a\). Summing over \(b\neq a\) and using \(\sum_{b\neq a}\widetilde{M}_{ab}=-\delta_a\) gives \((m-1)\delta_a-2\delta_a+(T-\delta_a)=0\), that is \((m-4)\delta_a+T=0\) for every _a_. Summing over _a_ gives (2_m_-4)_T_=0, so _T_=0, and then \(\delta_a=0\) for every _a_ because \(m\neq 4\). The displayed relation now gives \(\widetilde{M}_{ab}=0\) for \(a\neq b\), so _M_=0. By Lemma 2.3, _F(G_)={_X_<sup>∗</sup>} and \(\rho(G)=m-1\).

Finally 8_n_+1=4_m_<sup>2</sup>-4_m_+1=(2_m_-1)<sup>2</sup>, so _r_<sub>BP</sub>(_n_)=_m_-1 by (1). □

**Remark 3.2.** An alternative proof of the required nonsingularity follows from the entrywise square of _X_<sup>∗</sup>. The Kneser construction uses exactly \(\genfrac(){pt}{2}{m}{2}=\mathrm{dimSym}(\mathbf{1}^\perp)\) vectors, so the diagonal system is square. Indeed, \((X_{ef}^*)^2=\langle u_eu_e^\top,u_fu_f^\top\rangle\) for its unit Gram vectors _u<sub>e</sub>_. Thus \(X^*\circ X^*\) is the Gram matrix of the coefficient matrices in the diagonal equations. With _B=J-I-A_, the adjacency matrix of the triangular graph, it equals \(I+\frac{(m-4)^2}{4(m-2)^2}B+\frac{4}{(m-2)^2}A\). On the three subspaces in Lemma 3.1, its eigenvalues are, respectively,

\(\frac{m}{2},\frac{m(m-4)^2}{4(m-2)^2},\frac{m^2}{2(m-2)^2}.\)

All are positive for \(m\ge 5\). At _m_=4 the middle eigenvalue vanishes: _K_(4,2) is a perfect matching and has \(\rho=1\), explaining the missing rank in the Kneser family.

**Remark 3.3.** The optimal value is \(\mathrm{sdp}(K(m,2))=\frac{n}{4}(d+m-3)=\frac{m^2(m-1)(m-3)}{16}\) .

## 4. Rank three

The Kneser family leaves one rank to account for. The triangle supplies rank two, but _K_(4,2) is a perfect matching and has an integral optimum. For rank three we turn to a familiar graph: the wheel consisting of a five-cycle and a hub adjacent to every cycle vertex. It has six vertices, the smallest order allowed by the Barvinok-Pataki bound for rank three.

