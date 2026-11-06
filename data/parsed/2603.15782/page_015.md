The routing _f_ is represented implicitly; \(f'\) is internal to the subroutine and is a flow in \(\mathcal{N}(A,B,\mu)\). The decomposition has _O(m_) paths, but only their original endpoints and weights are needed to construct _D_. Cycle removal and endpoint decomposition can be implemented in _O(m_log_n_) time using dynamic trees \[41\], without listing path interiors. The implicit representation of _f_ also allows its edge loads \(\sum_{p:e\in p}f_p\) to be read from the edge-bottleneck arcs of the cycle-free flow in _O(m_) total time. In particular, _D_ has _O(m_) edges and total edge weight _F_; its symmetric adjacency matrix satisfies _D<sub>xy</sub>=D<sub>yx</sub>=d<sub>xy</sub>_ for \(x\in A,y\in B\).

**Lemma 13** (Gaussian direction)**.** _Under Assumption 1, there are constants_ \(c',\sigma,\zeta>0\)_, depending only on c, such that for u_∼N(0_,I<sub>d</sub>) Algorithm 3 satisfies_

\(\mathtt{Pr}\left[min_{y\in B}\langle y,u\rangle-max_{x\in A}\langle x,u\rangle\ge\sigma\right]\ge\zeta.\)

_For every direction, if_ \(F\le c'n\mu\)_, the returned cut gives a_ \(c'\)_-balanced element cut of cost at most_ \(2c'n\mu\)_. Otherwise the returned flow routes at least_ \(c'n\mu\) _units between A and B subject to the bounds of Lemma 12; on the event above every demand pair has projection gap at least_ \(\sigma\).

_Proof._ The bounded norms and spreading in Assumption 1 imply that \(\Omega(n^2)\) ordered pairs in _S_ have squared distance bounded below by a positive constant. For each such pair, \(\langle y-x,u\rangle\) is a centered Gaussian with variance \(\|y-x\|^2\), so it exceeds a suitable constant \(\sigma>0\) with constant probability. Thus the number _Z_ of ordered pairs with projection gap at least \(\sigma\) has expectation \(\Omega(n^2)\). Since \(0\le Z\le n^2\), there are constants \(\theta,\zeta>0\) such that \(Z\ge\theta n^2\) with probability at least \(\zeta\). If the gap between _A_ and _B_ were less than \(\sigma\), every pair counted by _Z_ would have its lower endpoint in _A_ or its upper endpoint in _B_. This would give \(Z\le(|A|+|B|)|S|\le 4c'n^2\), a contradiction for \(4c'<\theta\). The cut and flow conclusions follow from Lemma 12.

## 6 First approach: rectangular covers

In this section we assume that \(\beta(G)\le\beta\), or that \(w(e)=\infty\) for all \(e\in E\) and \(\beta_v(G)\le\beta\) (see Definition 2).

We start with some definitions. A set \(Q=A\times B\), where \(A,B\subseteq S\) are disjoint, is a _rectangle_. We denote \(\langle Q\rangle=\{\{x,y\}:(x,y)\in(A\times B)\cup(B\times A)\}\subseteq\genfrac(){pt}{2}{S}{2}\). Let _Q_<sup>paths</sup> consist of the simple graph paths _p_ with \(\partial p\in\langle Q\rangle\). For a set Q={_Q_<sub>1</sub>_,...,Q<sub>q</sub>_} with _q_=|Q| rectangles define \(\langle\mathcal{Q}\rangle=\bigcup_i\langle Q_i\rangle\subseteq\genfrac(){pt}{2}{S}{2}\) and \(\mathcal{Q}^\mathtt{paths}=\bigcup_iQ_i^\mathtt{paths}\).

**Definition 14.** _A set_ Q _is a_ \((\varepsilon,\Delta)\)-rectangular cover _if every pair_ \(\{x,y\}\in\langle\mathcal{Q}\rangle\) _satisfies_ \(\|x-y\|^2\ge\varepsilon\)_, and every pair_ \(\{x,y\}\in\genfrac(){pt}{2}{S}{2}\) _with_ \(\|x-y\|^2\ge\Delta\) _belongs to_ \(\langle\mathcal{Q}\rangle\)_. A nonnegative vector_ \(\nu:\mathcal{Q}^\mathtt{paths}\rightarrow\mathbb{R}_{\ge 0}\) _is a_ \(\mu\)-uniform Q-flow _if_

\(\sum_{p:x\in p}\nu(p)\le w(x)/2(x\in V)\) (7a)

\(\sum_{p:e\in p}\nu(p)\le w(e)(e\in E)\) (7b)

\(\sum_{p:x\in\partial p}\nu(p)\le\mu(x\in S)\) (7c)

_Its value is_ \(\mathtt{val}(\nu)=\sum_p\nu(p)\)_. The_ demand graph \(D_\nu\) _is an undirected weighted graph on V with positive weights where the weight of edge xy equals_ \(\sum_{p:\partial p=\{x,y\}}\nu(p)\).

Our algorithm will work as follows. First, we will generate a set of rectangles Q by sampling Gaussian directions which w.h.p. will be an \((\varepsilon,\Delta)\)-rectangular cover for \(\Delta=\Theta(1)\) (Sec. 6.1). Next,<tbc>

