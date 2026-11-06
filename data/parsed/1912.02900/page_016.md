**Observation 3.2** _If X is a semi-permutation, then the following properties hold for any_ (_X,T)- split at U:_

• \(\sum_{v\in U}r(X_v^s)=r(X)\)<tbc>

• \(\sum_{v\in U}c(X_v^s)=c(X)\)<tbc>

• \(c(X^c)\le|U|\)<tbc>

• \(\sum_{v\in U}\mathsf{WB}_{T_v}(X_v^s)+\mathsf{WB}_{T^c}(X^c)=\mathsf{WB}_T(X).\)

The first property holds since _X_ is a semi-permutation. In order to establish the last property, consider any vertex \(x\in V(T)\), and let \(T'\in\{T^c\}\cup\{T_v\}_{v\in U}\) be the new tree to which _v_ belongs; if \(x\in U\), then we set \(T'=T_x\). It is easy to see that the cost of _v_ in tree \(T'\) is the same as its cost in the tree _T_ (recall that the cost of a leaf vertex is 0).

The last property can be viewed as a "perfect decomposition" property of the weak WB-1 bound. In Section 3.3, we will show an (approximate) decomposition property of strong WB-1 bound.

### Splitting by Lines.

We can also define the splitting with respect to any subset \(\mathcal{L}'\subseteq\mathcal{L}\) of the auxiliary columns for _X_, analogously: Notice that the lines in \(\mathcal{L}'\) partition the bounding box _B_ into a collection of internally disjoint strips, that we denote by \(\{S'_1,\dots,S'_k\}\). We can then define the strip instances \(X_i^s\) as containing all vertices of \(X\cap S_i\) for all \(1\le i\le k\), and the compressed instance _X<sup>c</sup>_, that is obtained by collapsing, for each \(1\le i\le k\), all active columns that lie in strip _S<sub>i</sub>_, into a single column. We also call these resulting instances _a split of X by_ \(\mathcal{L}'\).

We can also consider an arbitrary ordering \(\sigma\) of the lines in L, such that the lines of \(\mathcal{L}'\) appear at the beginning of \(\sigma\), and let \(U\subseteq V(T(\sigma))\) contain all vertices _u_ for which the strip _S(u_) is in \(\{S_i\}_{1\le i\le k}\). If we perform a split of (_X,T_) at _U_, we obtain exactly the same strip instances \(X_1^s,\dots,X_k^s\), and the same compressed instance _X<sup>c</sup>_.

## 3.2 Decomposition Theorem for OPT

The following theorem gives a crucial decomposition property of OPT. The theorem is used in our algorithm for Min-Sat.

**Theorem 3.3** _Let X be a semi-permutation, let T be any partitioning tree for X, let_ \(U\subseteq V(T)\) _be a subset of vertices of T such that the strips in_ \(\{S(v)|v\in U\}\) _partition the bounding box, and let_ \(\{X^c,\{X_v^s\}_{v\in U}\}\) _be an_ (_X,T)-split at U. Then:_

\(\sum_{v\in U}\mathsf{OPT}(X_v^s)+\mathsf{OPT}(X^c)\le\mathsf{OPT}(X).\)

**Proof:** Let _Y_ be an optimal canonical solution for _X_, so that every point of _Y_ lies on an active row and an active column for _X_. For each vertex \(v\in U\), let _Y<sub>v</sub>_ denote the set of points of _Y_ that lie in the strip _S(v_); recall that these points must lie in the interior of the strip. Therefore, \(Y=\bigcup_{v\in U}Y_v\).

For every vertex \(v\in U\), let R(_v_) denote the set of all rows _R_, such that: (i) _R_ contains a point of _X_; (ii) _R_ contains no point of \(X_v^s\); and (iii) at least one point of _Y<sub>v</sub>_ lies on _R_. We let _m<sub>v</sub>_=|R(_v_)|. We need the following claim.

