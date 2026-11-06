Therefore, in order to complete the proof of Claim 2.9, it is enough to prove Claim C.1.

**Proof of Claim C.1.** Let _Y_ be an optimal solution to instance _X_. We can assume w.l.o.g. that _Y_ is a canonical solution, so no point of _Y_ lies on the line _L_. Let _Y<sup>L</sup>,Y<sup>R</sup>_ be the subsets of points of _Y_ that lie to the left and to the right of the line _L_, respectively.

Let R_<sup>L</sup>_ be the set of all rows _R_, such that (i) no point of _X<sup>L</sup>_ lies on _R_, and (ii) some point of _Y<sup>L</sup>_ lies on _R_. We define a set R_<sup>R</sup>_ of rows similarly for instance _X<sup>R</sup>_. The crux of the proof is the following observation.

**Observation C.2**

\(|\mathcal{R}^L|+|\mathcal{R}^R|\ge\mathsf{cost}(v)/2.\)

Before we prove Observation C.2, we show that Claim C.1 follows from it. In order to do so, we will define a new feasible solution \(\hat{Y}^L\) for instance _X<sup>L</sup>_, containing at most |_Y<sup>L</sup>_|-|R_<sup>L</sup>_| points, and similarly, we will define a new feasible solution \(\hat{Y}^R\) for instance _X<sup>R</sup>_, containing at most |_Y<sup>R</sup>_|-|R_<sup>R</sup>_| points. This will prove that \(\mathsf{OPT}(X^L)\le|Y^L|-|\mathcal{R}^L|\) and \(\mathsf{OPT}(X^R)\le|Y^R|-|\mathcal{R}^L|\), so altogether, \(\mathsf{OPT}(X^L)+\mathsf{OPT}(X^R)\le|Y|-|\mathcal{R}^L|-|\mathcal{R}^R|\le\mathsf{OPT}(X)-\mathsf{cost}(v)/2\), thus proving Claim C.1.

We now show how to construct the solution \(\hat{Y}^L\) for instance _X<sup>L</sup>_. The solution \(\hat{Y}^R\) for instance _X<sup>R</sup>_ is constructed similarly.

In order to construct the solution \(\hat{Y}^L\), we start with the solution _Y<sup>L</sup>_, and then gradually modify it over the course of |R_<sup>L</sup>_| iterations, where in each iteration we reduce the number of points in the solution _Y<sup>L</sup>_ by at least 1, and we eliminate at most one row from R_<sup>L</sup>_. In order to execute an iteration, we select two rows \(R,R'\), with the following properties:

• Row _R_ contains a point of _X<sup>L</sup>_;<tbc>

• Row \(R'\) contains a point of _Y<sup>L</sup>_ and it contains no points of _X<sup>L</sup>_; and<tbc>

• No point of \(X^L\cup Y^L\) lies strictly between rows _R_ and \(R'\).

Note that, if \(\mathcal{R}^L\neq\emptyset\), such a pair of rows must exist. We then collapse the row \(R'\) into the row _R_, obtaining a new modified solution to instance _X<sup>L</sup>_ (we use Observation 2.4). We claim that the number of points in the new solution decreases by at least 1. In order to show this, it is sufficient to show that there must be two points \(p\in R\), \(p'\in R'\) with the same _x_-coordinates; after the two rows are collapsed, these two points are mapped to the same point. Assume for contradiction that no such two points exist. Let \(p\in R\), \(p'\in R'\) be two points with smallest horizontal distance. Then it is easy to see that no point of \(X^L\cup Y^L\) lies in the rectangle \(\square_{p,p^\prime}\), contradicting the fact that _Y<sup>L</sup>_ is a feasible solution for _X<sup>L</sup>_.

In order to complete the proof of Claim C.1, it is now enough to prove Observation C.2.

**Proof of Observation C.2.** We denote _X_={_p_<sub>1</sub>_,...,p<sub>m</sub>_}, where the points are indexed in the increasing order of their _y_-coordinates. Recall that a pair (_p<sub>i</sub>,p_<sub>_i_+1</sub>) of points is a crossing, if the two points lie on opposite sides of the line _L_. We say that it is a _left-to-right_ crossing if _p<sub>i</sub>_ lies to the left of _L_, and we say that it is a _right-to-left_ crossing otherwise. Clearly, either at least half the crossings of _L_ are left-to-right crossings, or at least half the crossings of _L_ are right-to-left crossings. We assume w.l.o.g. that it is the former. Let \(\Pi\) denote the set of all left-to-right crossings of _L_, so \(|\Pi|\ge\mathsf{cost}(v)/2\). Notice that every point of _X_ participates in at most one crossing in \(\Pi\). We<tbc>

