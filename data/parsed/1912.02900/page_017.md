**Claim 3.4** _There is a feasible solution_ \(\hat{Y}\) _to instance X<sup>c</sup>, containing at most_ \(\sum_{v\in U}m_v\) _points._

**Proof:** We construct the solution \(\hat{Y}\) for _X<sup>c</sup>_ as follows. Consider a vertex \(v\in U\). Let _C<sub>v</sub>_ be the unique column into which the columns lying in the strip _S(v_) were collapsed. For every point \(p\in Y_v\) that lies on a row \(R\in\mathcal{R}(v)\), we add a new point \(\varphi(p)\) on the intersection of row _R_ and column _C<sub>v</sub>_ to the solution \(\hat{Y}\). Once we process all vertices \(v\in U\), we obtain a final set of points \(\hat{Y}\). It is easy to verify that \(|\hat{Y}|=\sum_vm_v\). In order to see that \(\hat{Y}\) is a feasible solution to instance _X<sup>c</sup>_, it is enough to show that the set \(X^c\cup\hat{Y}\) of points is satisfied. Notice that set \(X\cup Y\) of points is satisfied, and set \(X^c\cup\hat{Y}\) is obtained from \(X\cup Y\) by collapsing sets of active columns lying in each strip _S(v_) for \(v\in U\). From Observation 2.4, the point set \(X^c\cup\hat{Y}\) is satisfied. \(\square\)

We now consider the strip instances \(X_v^s\) and prove the following claim, that will complete the proof of the lemma.

**Claim 3.5** _For each vertex_ \(v\in U\), \(\mathsf{OPT}(X_v^s)\le|Y_v|-m_v\).

**Proof:** Notice first that the point set \(X_v^s\cup Y_v\) must be satisfied. We will modify point set _Y<sub>v</sub>_, to obtain another set \(Y'_v\), so that \(Y'_v\) remains a feasible solution for \(X_v^s\), and \(|Y'_v|\le|Y_v|-m_v\).

In order to do so, we perform _m<sub>v</sub>_ iterations. In each iteration, we will decrease the size of _Y<sub>v</sub>_ by at least one, while also decreasing the cardinality of the set R(_v_) of rows by exactly 1, and maintaining the feasibility of the solution _Y<sub>v</sub>_ for \(X_v^s\).

In every iteration, we select two arbitrary rows _R_ and \(R'\), such that: (i) \(R\in\mathcal{R}(v)\); (ii) \(R'\) is an active row for instance \(X_v^s\), and (iii) no point of \(Y_v\cup X_v^s\) lies strictly between rows _R_ and \(R'\). We collapse the rows _R_ and \(R'\) into the row \(R'\). From Observation 2.4, the resulting new set _Y<sub>v</sub>_ of points remains a feasible solution for instance \(X_v^s\). We claim that |_Y<sub>v</sub>_| decreases by at least 1. In order to show this, it is enough to show that there are two points \(p,p'\in X_v^s\cup Y_v\), with \(p\in R\), \(p'\in R'\), such that the _x_-coordinates of _p_ and \(p'\) are the same; in this case, after we collapse the rows, _x_ and \(x'\) are mapped to the same point. Assume for contradiction that no such two points exist. Let \(p\in R\cap(X_v^s\cup Y_v)\), \(p'\in R'\cap Y_v\) be a pair of points with smallest horizontal distance. Such points must exist since _R_ contains a point of \(X_v^s\) and \(R'\) contains a point of _Y<sub>v</sub>_. But then no other point of \(X_v^s\cup Y_v\) lies in \(\square_{p,p^\prime}\), so the pair \((p,p')\) is not satisfied in \(X_v^s\cup Y_v\), a contradiction. \(\square\)

\(\square\)

## 3.3 Decomposition Theorem for the Strong WB-1 bound

In this section we prove the following theorem about the strong WB-1 bound, that we use several times in our negative result.

**Theorem 3.6** _Let X be a semi-permutation and T be a partitioning tree for X. Let_ \(U\subseteq V(T)\) _be a set of vertices of T such that the strips in_ \(\{S(v)|v\in U\}\) _partition the bounding box. Let_ \(\{X^c,\{X_v^s\}_{v\in U}\}\) _be the split of_ (_X,T_) _at U. Then:_

\(\mathsf{WB}(X)\le 4\mathsf{WB}(X^c)+8\sum_{v\in U}\mathsf{WB}(X_v^s)+O(|X|).\)

This result is somewhat surprising. One can think of the expression \(\mathsf{WB}(X^c)+\sum_{v\in U}\mathsf{WB}(X_v^s)\) as a WB-1 bound obtained by first cutting along the lines that serve as boundaries of the strips _S(v_)<tbc>

