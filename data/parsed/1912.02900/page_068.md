will associate, to each crossing \((p_i,p_{i+1})\in\Pi\), a unique row in \(\mathcal{R}^L\cup\mathcal{R}^R\). This will prove that \(|\mathcal{R}^L|+|\mathcal{R}^R|\ge|\Pi|\ge\mathsf{cost}(v)/2\).

Consider now some crossing (_p<sub>i</sub>,p_<sub>_i_+1</sub>). Assume that _p<sub>i</sub>_ lies in row _R_, and that _p_<sub>_i_+1</sub> lies in row \(R'\). Let R_<sub>i</sub>_ be a set of all rows lying between _R_ and \(R'\), including these two rows. We will show that at least one row of R_<sub>i</sub>_ lies in \(\mathcal{R}^L\cup\mathcal{R}^R\). In order to do so, let _H_ be the closed horizontal strip whose bottom and top boundaries are _R_ and \(R'\), respectively. Let _H<sup>L</sup>_ be the area of _H_ that lies to the left of the line _L_, and that excludes the row _R_ - the row containing the point _p<sub>i</sub>_, that also lies to the left of _L_. Similarly, let _H<sup>R</sup>_ be the area of _H_ that lies to the right of the line _L_, and that excludes the row \(R'\). Notice that, if any point \(y\in Y^L\) lies in _H<sup>L</sup>_, that the row containing _y_ must belong to R_<sup>L</sup>_. Similarly, if any point \(y'\in Y^R\) lies in _H<sup>R</sup>_, then the row containing \(y'\) belongs to R_<sup>R</sup>_. Therefore, it is now sufficient to show that either _H<sup>L</sup>_ contains a point of _Y<sup>L</sup>_, or _H<sup>R</sup>_ contains a point of _Y<sup>R</sup>_. Assume for contradiction that this is false. Let \(p\in X^L\cup Y^L\) be the point lying on the row _R_ furthest to the right (such a point must exist because we can choose _p=p<sub>i</sub>_). Similarly, let \(p'\in X^R\cup Y^R\) be the point lying on the row \(R'\) furthest to the left (again, such a point must exist because we can choose \(p'=p_{i+1}\).) But if _H<sup>L</sup>_ contains no points of _Y<sup>L</sup>_, and _H<sup>R</sup>_ contains no points of _Y<sup>R</sup>_, then no points of \(X\cup Y\) lie in the rectangle \(\square_{p,p^\prime}\), and so the pair \((p,p')\) of points is not satisfied in \(X\cup Y\) , a contradiction.

## D Proof of Lemma 5.3

In this section we prove Lemma 5.3, by showing that for any point set _X_ that is a permutation, \(\mathsf{GB}(X)\le 2\mathsf{OPT}(X)\). In order to do so, it is enough to prove that, for any point set _X_ that is a permutation, for any partitioning tree _T_ for _X_, \(\mathsf{GB}_T(X)\le 2\mathsf{OPT}(X)\). The proof is by induction on the height of _T_, and it is almost identical to the proof of Claim 2.9 for the standard Wilber Bound. When the height of the tree _T_ is 1, then |_X_|=1, so GB(_X_)=0 and OPT(_X_)=0.

Consider now a partitioning tree _T_ whose height is greater than 1. Let _T_<sub>1</sub>_,T_<sub>2</sub> be the two sub-trees of _T_, obtained by deleting the root vertex _r_ from _T_. Let (_X_<sub>1</sub>_,X_<sub>2</sub>) be the partition of _X_ into two subsets given by the line _L(r_), such that _T_<sub>1</sub> is a partitioning tree for _X_<sub>1</sub> and _T_<sub>2</sub> is a partitioning tree for _X_<sub>2</sub>. Notice that, from the definition of the GB bound:

\(\mathsf{GB}_T(X)=\mathsf{GB}_{T_1}(X_1)+\mathsf{GB}_{T_2}(X_2)+\mathsf{cost}(r).\)

Moreover, from the induction hypothesis, \(\mathsf{GB}_{T_1}(X_1)\le 2\mathsf{OPT}(X_1)\) and \(\mathsf{GB}_{T_2}(X_2)\le 2\mathsf{OPT}(X_2)\).

Using Claim C.1 (that can be easily adapted to horizontal partitioning lines), we get that:

\(\mathsf{OPT}(X)\ge\mathsf{OPT}(X_1)+\mathsf{OPT}(X_2)+\mathsf{cost}(r)/2.\)

Therefore, altogether we get that:

\(\mathsf{GB}_T(X)\le 2\mathsf{OPT}(X_1)+2\mathsf{OPT}(X_2)+\mathsf{cost}(r)\le 2\mathsf{OPT}(X).\)

