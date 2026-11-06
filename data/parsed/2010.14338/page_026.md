_Observation 2._ \(\mathsf{OPT}(P,D)\ge\sum_{C\in\mathcal{C}}\mathsf{OPT}(P_C,D_C)\).

Next, we define our solution points which consist of the _inner points S_<sub>1</sub> connecting the demands _D<sub>C</sub>_ in the same cell _C_, and the _outer points S_<sub>2</sub> connecting the demands \((p,p')\in D\), \(p\in C\) and \(p'\in C'\) where _C_ and \(C'\) are two different grid cells. The inner points _S_<sub>1</sub> are defined as follows. For each cell \(C\in\mathcal{C}\), we take the solution _S_<sub>1</sub>(_C_) that results from Theorem 27, and then \(S_1=\bigcup_{C\in\mathcal{C}}S_1(C)\). The outer points _S_<sub>2</sub> is also a union of _S_<sub>2</sub>(_C_). For each grid cell \(C\in\mathcal{C}\), for each point \(p\in C\) that has some demand with some other point in different cell, if a vertical grid line _L_ (a line drawn at the _x_-coordinate _x(L_)) is within distance _r_ from _p_, we create a point (_x(L),y(p_)) on line _L_ (in other words, this is a projection of point _p_ onto line _L_.) We do the same for each point \(p\in P_C\) and each horizontal grid line _L_: If _L_ is within distance _r_ from _p_, create a projected point (_x(p),y(L_)). The set _S_<sub>2</sub>(_C_) contains, for each \(p\in P_C\), all such projected points from _p_.

**Lemma 31** (Feasibility)**.** _The solution_ \(S_1\cup S_2\) _is feasible for_ (_P,D)._

_Proof._ Consider any point \((p,q)\in D\). If _p_ and _q_ are in the same cell, we are done since _S_<sub>1</sub> would connect them. If \(p\in C\) and \(q\in C'\) for \(C,C'\in\mathcal{C}\), then consider any grid line _L_ that separates them, so we have that the distance between _L_ and _p_ is at most _r_ and so is the distance between _L_ and _q_. Let \(p'\) and \(q'\) be projections of _p_ and _q_ on _L_. We have a Manhattan path \(p\rightarrow p'\rightarrow q'\rightarrow q\).

**Lemma 32** (Cost)**.** \(|S_1|+|S_2|\le O(\mathsf{OPT}(P,D))\)

_Proof._ From Theorem 27, we have that \(|S_1|\le 2\sum_{C\in\mathcal{C}}\mathsf{OPT}(P_C,D_C)\le 2\mathsf{OPT}(P,D)\). Next, for points in _S_<sub>2</sub>, notice that each point \(p\in P\) creates at most 8 projected points, so we have:

\(|S_2|=\sum_{C\in\mathcal{C}}|S_2(C)|\le 8\sum_{C\in\mathcal{C}}|P_C|\le 8|P|\le 8\mathsf{OPT}(P,D)+8\)

The last inequality follows from Lemma 30.

## G.2 General Disks

Now we show that any instance with disc demand admits an \(O(log\Delta)\)-approximation where each \(r_p\in[1,\Delta]\). As in the proof of the unit disk case, we may assume that _G_ is connected and every input-point in _P_ is part of some demand.

Let _h,k_ be minimal and maximal integers respectively such that \(2^h\le r_p\le 2^{k-1}\) for all \(p\in P\). Fix grids \(\Gamma_h\subseteq\Gamma_{h+1}\subseteq\dots\subseteq\Gamma_k\) of sizes 2<sup>_h_-1</sup>,2_<sup>h</sup>,...,_2<sup>_k_-1</sup> respectively. For every input point, we place 8 points by projecting a point to the two closest grid lines in each direction. We do this for each of the grids adding in total \(8n(k-h+1)=O(nlog\Delta)\) many points.

Additionally, we satisfy the demands within a cell of \(\Gamma_h\) as before by applying the greedy algorithm for each cell separately, using at most \(2\cdot\mathsf{OPT}\) points. The statement follows, as \(\mathsf{OPT}\ge\frac{n}{2}\) by Lemma 30.

## G.3 Demands with Two Radii

In this section, we study the disk demands where there are only two different radii _r<sub>A</sub>\<r<sub>B</sub>_.

**Definition 33.** Let (_P,D_) be an input to MinGMConn. The input demand _D_ is called _two-disk demand_ if the point set _P_ is partitioned into two subsets \(A\cup B\), such that every point \(p\in A\) has _r<sub>p</sub>=r<sub>A</sub>_; otherwise, _r<sub>p</sub>=r<sub>B</sub>_ for each \(p\in B\).

