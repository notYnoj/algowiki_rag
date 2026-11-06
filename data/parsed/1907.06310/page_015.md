<tbc>of the parent of _z_ with the left subtree of _z_ in _V_ , otherwise _W=V_ . The tree _H(S_) is the binary search tree whose left spine comprises {_a,b,z_} such that _W_ is the right subtree of _b_ in _H(S_).

Let _E_ be an execution for _X_=(_x_<sub>1</sub>_,...,x<sub>m</sub>_) starting from _T_ with rooted hulls _Q_<sub>1</sub>_,...,Q<sub>m</sub>_, transition trees \(Q'_1,\dots,Q'_m\) and after-trees _T_<sub>1</sub>_,...,T<sub>m</sub>_ and let _T_<sub>0</sub>=_T_. Let _A_=(_z,b,a,z_), let \(\hat{T}_{-1}\) be the final tree in Top-Down Splay’s execution of let _A_ starting from \(\hat{T}_{-1}\), let \(Q_0=\hat{T}_{-1}\), let \(Q'_0=T\), let _T_<sub>0</sub>=_T_ and let _x_<sub>0</sub>=_z_. For \(0\le i\le m\) let \(\hat{T}_i=H(T_i)\), let \(\hat{Q}_i\) and \(\hat{Q}'_i\) respectively be the smallest rooted hulls in \(\hat{T}_{i-1}\) and \(\hat{T}_i\) containing the keys in \(Q_i\cup\{a\}\), and let _Y<sub>i</sub>_ be the sequence of keys determined by the restricted rotation algorithm for transforming the right subtree of _b_ in \(\hat{Q}_i\) into its right subtree in \(\hat{Q}'_i\). Form _Z<sub>i</sub>_ by replacing each key in _Y<sub>i</sub>_ with the corresponding keys determined by Figure 5, and then appending the requests (_x<sub>i</sub>,a,z_). Top-Down Splay’s execution of _A_ has cost proportional to at most |_T_|, which can be absorbed into the cost of _E_. The sequence _Z<sub>i</sub>_ induces Top-Down Splay to transform \(\hat{Q}_i\) into \(\hat{Q}'_i\). Since \(|\hat{Q}'_i|\le|Q'_i|+3\), the transformation’s cost is proportional to \(|Q'_i|\). Thus, the map \(\mathcal{S}(E)=A\oplus\oplus_{i=0}^mZ_i\) is a simulation embedding for Top-Down Splay. Apply Theorem 3.2.

While the rooted hulls of Greedy’s executions are access paths, its transition trees are determined by which keys are in surrounding requests, meaning Greedy is not a natural algorithm. Lucas conjectured that restricting executions’ rooted hulls to the access path does not increase optimal cost by more than a fixed multiple \[49\]. This conjecture remains open. Kozma catalogues related open questions about the relative power of classes of binary search tree algorithms subject to various restrictions \[42\]. Splay is in the most restrictive of these classes, meaning dynamic optimality would imply they are all equivalent up to constant factors.

## 7 Crossing Cost

Binary search trees facilitate efficient search by arranging keys into many short access paths comprising children of alternating direction, and an algorithm’s efficiency depends critically on how it utilizes these arrangements. Consider the subtree _P_ of a binary search tree _T_ comprising the access path for a node _x_ in _T_. The _crossing nodes_ for _x_ in _T_ comprise _x_, the root of _T_, and the nodes in _P_ that are either left children with a right child on _P_ or right children with a left child on _P_. We refer to the number of crossing nodes for _x_ as its _crossing depth_ in _T_, denoted \(\ell_T(x)\). The _bookkeeping nodes_ are the non-crossing nodes on _P_. The _crossing cost_ of execution _E_ with after-trees _T_<sub>1</sub>_,...,T<sub>m</sub>_ for _X_=(_x_<sub>1</sub>_,...,x<sub>m</sub>_) starting from _T_ is \(\sum_{i=1}^m\ell_{T_{i-1}}(x_i)\) where _T_<sub>0</sub>=_T_, and the execution’s _bookkeeping cost_ is \(\sum_{i=1}^m(d_{T_{i-1}}(x_i)-\ell_{T_{i-1}}(x_i))\).

z
b
a
X
v
y
u
w

Figure 5: Schematic of the top portion of some \(\hat{T}_i\). To induce a rotation at _u_, perform top-down splays at (_a,u,a,z_). To induce a rotation at _v_, top-down splay the sequence (_v,a,z_). To induce a rotation at _w_, top-down splay at (_a,w,a,z_). To induce a rotation at _y_, top-down splay at (_y,a,z_).

