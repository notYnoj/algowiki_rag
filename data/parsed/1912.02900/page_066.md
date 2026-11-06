## C.4 Proof of Observation 2.5

Let _C_ and \(C'\) be any pair of consecutive active columns for _X_, such that some point of _Y_ lies strictly between _C_ and \(C'\). Let C be the set of all columns that lie between _C_ and \(C'\), including _C_ but excluding \(C'\), that contain points of \(X\cup Y\) . We collapse the columns in C into the column _C_, obtaining a new feasible solution for instance _X_ (we use Observation 2.4). We continue this process until every point of the resulting solution _Y_ lies on an active column, and we perform the same procedure for the rows.

## C.5 Proof of Claim 2.6

Let _X_ be a given semi-permutation. We will construct a solution _Y_ for _X_, with |_Y_|=_O(r(X_)log_c(X_)). In order to do so, we consider a _balanced_ partitioning tree _T_ of _X_ with depth _O_(log_c(X_)): in other words, if _v_ is an inner vertex of _T_, and \(u,u'\) are its two children, then \(\mathrm{width}(u),\mathrm{width}(u')\ge 3\mathrm{width}(v)/4\). Let _v_ be the root vertex of _T_ and \(L(v)\in\mathcal{L}\) be vertical line that _v_ owns. Let _T_<sub>1</sub> and _T_<sub>2</sub> be the subtrees of _T_ rooted at the two children of _v_. Notice that _L(v_) partitions the input set _X_ of points into two subsets, _X_<sub>1</sub> and _X_<sub>2</sub>.

We start by adding, for every point \(p\in X\), the point \(p'\), whose _y_-coordinate is _p.y_, and that lies on _L(v_), to the solution _Y_ . We then recursively compute a solution _Y_<sub>1</sub> for _X_<sub>1</sub>, using the partitioning tree _T_<sub>1</sub>, and similarly a solution _Y_<sub>2</sub> for _X_<sub>2</sub>, using the partitioning tree _T_<sub>2</sub>. The final solution is obtained by adding the points of \(Y_1\cup Y_2\) to the set _Y_ . It is easy to verify that _Y_ is indeed a feasible solution. Moreover, each active row of _X_ may contain at most _O_(log_c(X_)) points of _Y_ , and so \(|Y|\le O(r(X)\mathrm{log}c(X))\).

## C.6 Proof of Claim 2.9

It is sufficient to prove that, if _X_ is a semi-permutation, and _T_ is any partitioning tree for _X_, then \(\mathsf{WB}_T(X)\le 2\mathsf{OPT}(X)\).

We prove this claim by induction on the height of _T_. The base case, when the height of _T_ is 0, is obvious: there is only one active column, and so WB_<sub>T</sub>(X_)=OPT(_X_)=0.

We now consider the inductive step. Let _X_ be any point set that is a semi-permutation, and let _T_ be any partitioning tree for _X_, such that the height of _T_ is at least 1. Let _v_ be the root vertex of _T_, _L=L(v_) the line that _v_ owns, and let _v<sub>L</sub>,v<sub>R</sub>_ be the two children of _v_. We assume w.l.o.g. that the strip _S(v<sub>L</sub>_) lies to the left of _S(v<sub>R</sub>_). We denote _S(v_)=_B_ - the bounding box of the instance, _S(v<sub>L</sub>_)=_S<sup>L</sup>,S(v<sub>R</sub>_)=_S<sup>R</sup>_, and we also denote \(X^L=X\cap S^L,X^R=X\cap S^R\). Lastly, we let _T<sup>L</sup>_ and _T<sup>R</sup>_ be the sub-trees of _T_ rooted at _v<sub>L</sub>_ and _v<sub>R</sub>_, respectively. We prove the following claim.

## Claim C.1

\(\mathsf{OPT}(X)\ge\mathsf{OPT}(X^L)+\mathsf{OPT}(X^R)+\mathsf{cost}(v)/2.\)

Notice that, if the claim is correct, then we can use the induction hypothesis on _X<sup>L</sup>_ and _X<sup>R</sup>_ with the trees _T<sup>L</sup>_ and _T<sup>R</sup>_ respectively, to conclude that:

\(\mathsf{OPT}(X)\ge\frac{1}{2}\left(\mathsf{WB}_{T^L}(X_L)+\mathsf{WB}_{T^R}(X_R)+\mathsf{cost}(v)\right)=\frac{1}{2}\mathsf{WB}_T(X).\)

