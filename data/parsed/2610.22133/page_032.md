## 32 Asteroidal Triples and Friends in (Likely Necessary) Matrix Multiplication Time

\(\blacksquare\) **13** The nodes of \(C'\) are not dominated by nodes outside of \(C'\) since \(C'\) is a clique and only nodes of \(C'\) have neighbors to all nodes of \(C'\) since _V_ does not contain the all 0s vector. However, two nodes in \(C'\) also cannot dominate each other because of the matching to \(C''\) and hence no node of \(C'\) can be dominated.

\(\blacksquare\) **14** Consider a node \(x\in X\). As _x_ has neighbors in all the sets \(X',Y,C'\), any node that dominates it must have neighbors in each of these sets. Only the nodes of \(X\cup Y\) have this property, and we have already established that _x_ cannot be dominated by another node of _X_. Thus the only possible nodes to be dominated are the nodes of _X_ and they can only be dominated by nodes of _Y_.

Hence, _G_ has a dominated vertex iff there is some \(x\in X\) dominated by some \(y\in Y\) which holds iff for every \(c\in C'\) for which _x_ has an edge to, _y_ also has an edge to. This is if and only if the vector of _U_ corresponding to _x_ is orthogonal to the vector of _V_ corresponding to _y_.

In the above construction, the dominated vertex can only be dominated by one of its neighbors. This also means that dominated vertex can be reduced to the problem \(\exists x\in V,\exists y\in N(x)\forall z\in N(x),(y,z)\in E\).

This latter problem can be reduced back to OV on 2_n_ dimensions pretty easily: We are given **G**=(_V,E_) in which we want to solve \(\exists x\in V,\exists y\in N(v)\forall z\in N(v),(y,z)\in E\). Let _A_ be the adjacency matrix and let _C_ be its complement. Let _I_ be the \(n\times n\) identity matrix. Let _X_ be the \(n\times 2n\) matrix obtained by concatenating _A_ and _C+I_ (with _C+I_ to the right of _A_). Now let _Y_ be the \(2n\times n\) matrix obtained by concatenating _C_ on top of _I_. Note that (_XY_)[_i,j_]=0 if and only if

(1) for every _k_ such that \((i,k)\in E\), either _k=j_ or \((k,j)\in E\) (i.e. if _A[i,k_]=1, then _C[k,j_]=0), and

(2) (_C+I_)[_i,j_]=0, so \(i\neq j\) and \((i,j)\in E\).

\(\blacksquare\) **Theorem B.3.** _The following three problems are equivalent (using_ O(_n_<sup>2</sup>) _time reductions):_

Dominated Vertex in a \(\Theta(n)\)_-node graph,_

_OV on_ \(\Theta(n)\) _vectors in_ \(\Theta(n)\) _dimensions,_

_The problem of deciding_ \(\exists x\in V,\exists y\in N(v)\forall z\in N(v),(y,z)\in E\) _in a_ \(\Theta(n)\)_-node graph._

