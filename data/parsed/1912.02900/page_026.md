## 4.1 Upper-Bounding WB costs

Recall that for an input set _X_ of points, a partitioning tree _T_ of _X_, and a vertex \(v\in V(T)\), we denoted by _N(v_) the number of points of _X_ that lie in the strip _S(X_). We use the following claim for bounding the WB cost of subsets of vertices of _T_.

**Claim 4.1** _Consider a set X of points that is a semi-permutation, an ordering_ \(\sigma\) _of the auxiliary columns in_ L _and the corresponding partitioning tree_ \(T=T(\sigma)\)_. Let_ \(v\in V(T)\) _be any vertex of the tree. Then the following hold:_

• _Let T<sub>v</sub> be the sub-tree of T rooted at v. Then_ \(\sum_{u\in V(T_v)}\mathsf{cost}(u)=\mathsf{WB}_{T_v}(X\cap S(v))\le O(N(v)log(N(v)))\).<tbc>

• _Let u be any descendant vertex of v, and let P be the unique path in T connecting u to v. Then_ \(\sum_{z\in V(P)}\mathsf{cost}(z)\le 2N(v)\).

**Proof:** The first assertion follows from the definition of the weak WB-1 bound and Corollary 2.10. We now prove the second assertion. Denote _P_=(_v=v_<sub>1</sub>_,v_<sub>2</sub>_,...,v<sub>k</sub>=u_). For all \(1<i\le k\), we let \(v'_i\) be the unique sibling of the vertex _v<sub>i</sub>_ in the tree _T_. We also let _X<sub>i</sub>_ be the set of points of _X_ that lie in the strip \(S(v'_i)\), and we let \(X'\) be the set of all points of _X_ that lie in the strip _S(v<sub>k</sub>_). It is easy to verify that \(X_2,\dots,X_k,X'\) are all mutually disjoint (since the strips \(\{S(v'_i)\}_{i=2}^q\) and _S(v<sub>k</sub>_) are disjoint), and that they are contained in \(X\cap S(v)\). Therefore, \(\sum_{i=2}^q|X_i|+|X'|\le N(v)\).

From Observation 2.7, for all \(1\le i<k\), \(\mathsf{cost}(v_i)\le 2N(v'_i)=2|X_i|\), and \(\mathsf{cost}(v_k)\le 2N(v_k)=2|X'|\). Therefore, \(\sum_{z\in V(P)}\mathsf{cost}(z)\le 2\sum_{i=2}^q|X_i|+2|X'|\le 2N(v)\). □

## 4.2 Some Important Instances

### Monotonically Increasing Sequence.

We say that an input set _X_ of points is _monotonically increasing_ iff _X_ is a permutation, and moreover for every pair \(p,p'\in X\) of points, if \(p.x<p'.x\), then \(p.y<p'.y\) must hold. It is well known that the value of the optimal solution of monotonically increasing sequences is low, and we exploit this fact in our negative results.

**Observation 4.2** _If X is a monotonically increasing set of points, then_ \(\mathsf{OPT}(X)\le|X|-1\).

**Proof:** We order points in _X_ based on their _x_-coordinates as _X_={_p_<sub>1</sub>_,...,p<sub>m</sub>_} such that _p_<sub>1</sub>_.x\<p_<sub>2</sub>_.x\<...\<p<sub>m</sub>.x_. For each _i_=1_,...,m_-1 we define _q<sub>i</sub>_=((_p<sub>i</sub>).x,(p_<sub>_i_+1</sub>)_.y_) and the set _Y_={_q_<sub>1</sub>_,...,q_<sub>_m_-1</sub>}. It is easy to verify that _Y_ is a feasible solution for _X_. □

### Bit Reversal Sequence (BRS).

We use the geometric variant of BRS, which is more intuitive and easier to argue about. Let \(\mathcal{R}\subseteq\mathbb{N}\) and \(\mathcal{C}\subseteq\mathbb{N}\) be sets of integers (which are supposed to represent sets of active rows and columns.) The instance BRS(_i,_R,C) is only defined when |R|=|C|=2_<sup>i</sup>_. It contains 2_<sup>i</sup>_ points, and it is a permutation, whose sets of active rows and columns are exactly R and C respectively; so |R|=|C|=2_<sup>i</sup>_. We define the instance recursively. The base of the recursion is instance BRS(0,{_C},{R_}), containing a single point at the intersection of row _R_ and column _C_. Assume now that we have defined, for all \(1\le i'\le i\), and any sets \(\mathcal{R}',\mathcal{C}'\) of \(2^{i^\prime}\) integers, the corresponding instance \(\mathsf{BRS}(i,\mathcal{R}',\mathcal{C}')\). We define instance BRS(_i_+1,R,C), where |R|=|C|=2<sup>_i_+1</sup>, as follows.

