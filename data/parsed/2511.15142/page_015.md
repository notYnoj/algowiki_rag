<tbc>all candidate sets consist of simple _s-v_ paths. The minimum weight path among them can be identified by comparing the cycles formed by adding the edge (_v,s_) to each candidate path.

Finally, if the DP completes without identifying any negative cycles during the filtering steps, it correctly computes the shortest paths from _s_ to every vertex \(v\neq s\). Verifying that none of the cycles \(DP_s(v,n-1)\cdot(v,s)\) have negative weight confirms that _D_ contains no negative cycles, thereby certifying the optimality of _y_<sub>1</sub>.

## 4 Global Subspace Learning

In this section, we develop our second general algorithmic framework, tailored to cases where the weight vector _w_<sup>∗</sup> in the objective function uses integers bounded by _B_, i.e., \(w^*\in\mathbb{Z}^n\) and \(\|w^*\|_\infty\le B\). The resulting algorithm has a clean linear-algebraic structure which we can use to obtain efficient algorithms for several natural set systems F.

Recall that the iterative sieving algorithm from Section 2 was based on iteratively sampling and sorting to filter out dominated solutions, while the Dual Ellipsoid algorithm in Section 3 maintained a geometric region of plausible weights to either certify optimality or shrink the dual space. Our new _Global Subspace Learning (GSL)_ algorithm takes a more direct algebraic approach. It iteratively learns the linear subspace of directions orthogonal to _w_<sup>∗</sup>. This algorithm is highly intuitive and demonstrates the idea of inference naturally. It also achieves a stronger global guarantee: it actually sorts _all_ feasible sets by their weight, using only poly(_nB_) comparisons--a task which is feasible in the bounded weights case, because there are at most _O(nB_) possible distinct weight classes.

### 4.1 The Algorithm

As in the previous section, we work with a set P of points, which are indicator vectors \(\unknown_S\) of the feasible sets in \(S\in\mathcal{F}\). For brevity, we will use \(x,y\in\mathcal{P}\) to refer both to points in R_<sup>n</sup>_, and also the corresponding sets in F. The weight of a point _x_ is \(w^*(x):=\langle w^*,x\rangle\).

The technical core of the algorithm is the following observation: if two points \(x,y\in\mathcal{P}\) have the same weight, they imply the linear equality \(\langle w^*,x-y\rangle=0\). Concretely, the _Global Subspace Learning_ algorithm does the following:

#### 4.1.1 Global Subspace Learning Algorithm

1. **Buckets:** At the end of step _t_, the algorithm has considered _t_ points _y_<sub>1</sub>_,...,y<sub>t</sub>_ from P which are divided into some number of buckets \(B_1,B_2,\dots,B_\ell\). These buckets are indexed in increasing order of weight, and each bucket contains points of the same weight. For each bucket _B<sub>i</sub>_, we have chosen an arbitrary _representative r<sub>i</sub>_, say the first point in that bucket.<tbc>

<tbc>Moreover, the algorithm also maintains a subspace<tbc>

<tbc>\(\mathcal{A}=span\left(\cup_{i\in[\ell]}\{x-y|x,y\in B_i\}\right)\)<tbc>

<tbc>that is spanned by directions _x-y_ known to be orthogonal to _w_<sup>∗</sup>. By construction, if a pair \(x',y'\in\mathcal{F}\) satisfies \(x'-y'\in\mathcal{A}\), we can infer that \(\langle w^*,x'-y'\rangle=0\) and hence \(w^*(x')=w^*(y')\) . Hence, each bucket _B<sub>i</sub>_ has a corresponding affine subspace \(\mathcal{A}_i=\{r_i+v|v\in\mathcal{A}\}\) defined using the representative \(r_i\in B_i\), and \(\mathcal{P}\cap\mathcal{A}_i\) is precisely the set of points which can be inferred to have the same weight as the points in _B<sub>i</sub>_ at this time.<tbc>

<tbc>To begin, at time _t_=1, we choose _y_<sub>1</sub> as an arbitrary point in P, have a single bucket _B_<sub>1</sub>={_y_<sub>1</sub>} and _r_<sub>1</sub>=_y_<sub>1</sub>, and the subspace A is the trivial subspace of dimension zero.

