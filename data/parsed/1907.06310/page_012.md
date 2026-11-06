nodes then their keys comprise a rooted hull in _B<sub>i</sub>_ which is isomorphic to _L<sub>i</sub>_, and \(P'_i\) is isomorphic to a subgraph of the rooted hull in _B<sub>i</sub>_ comprising the keys in _A<sub>i</sub>_. Thus, \(\mathrm{cost}(X,S)\le\mathrm{cost}\mathcal{R}(\chi,S)\).

It remains to bound the cost of an optimal execution for the new instance. Let _Q_<sub>1</sub>_,...,Q<sub>m</sub>_ be the rooted hulls and \(Q'_1,\dots,Q'_m\) be the transition trees for an optimal execution of \(\chi\) starting from _T_, and let _G_<sub>0</sub>=_S<sub>m</sub>_. For \(1\le i\le m\), if \(r_i\neq\mathtt{delete}\) or \(\infty\in\{-u_i,w_i\}\) then let _C<sub>i</sub>_ be the rooted hull of _G_<sub>_i_-1</sub> that is isomorphic to _Q<sub>i</sub>_ and let \(C'_i\) be the transition tree with the same keys as _C<sub>i</sub>_ that is isomorphic to \(Q'_i\). If _r<sub>i</sub>_=`delete` and \(\infty\notin\{-u_i,w_i\}\) then form _C<sub>i</sub>_ and \(C'_i\) by respectively augmenting said isomorphic rooted hull and corresponding transition tree with _v<sub>i</sub>_. The first in the transition tree sequence \(D'_i\) for the requests in _Y<sub>i</sub>_ is the tree that results from splaying the first requested key of _Y<sub>i</sub>_ in \(C'_i\). The remaining transition trees in \(D'_i\) are the transition trees of Splay’s execution of the remaining requests in _Y<sub>i</sub>_ starting from the first tree in \(D'_i\). Finally, let _G<sub>i</sub>_ be the final after-tree in the execution of _Y<sub>i</sub>_ starting from _G_<sub>_i_-1</sub> whose transition trees are \(D'_i\). The first tree in \(D'_i\) has size at most \(|Q'_i|+1\), and _Y<sub>i</sub>_ has at most six remaining requests, each served by a transition tree from \(D'_i\) with size at most four, meaning \(\sum_{H\in D_i^\prime}|H|\le 26|Q'_i|\). The transition tree sequence \(\oplus_{i=1}^mD'_i\) executes \(\mathcal{R}(\chi,T)\). Thus, \(\mathrm{OPT}\mathcal{R}(\chi,T)\le 26\mathrm{OPT}_\mathrm{mut}(\chi,T)\), and R is a reduction. Apply Theorems 5.1 and 4.3.

Theorem 5.2 has an interesting consequence. A _deque instance_ is an initial tree together with a request sequence entirely comprising `push`, `pop`, `inject` and `eject` operations which respectively correspond to inserting a new maximum, deleting the maximum, inserting a new minimum and deleting the minimum. A binary search tree algorithm A supports deque operations if there is some _c\>_0 so that \(\mathrm{cost}_\mathcal{A}(D,T)\le c(|D|+|T|)\) for all deque instances (_D,T_). The _deque conjecture_ states that Splay supports deque operations. Tarjan proved that Splay supports a limited subset of deque operations \[65\]. Sundar placed an inverse-Ackermann upper bound on the cost of performing general deque operations \[63\]. Pettie later tightened this bound \[55\]. Similar bounds are known for Greedy \[11\]. We add a new result:

**Theorem 5.3.** _If Splay is eventually monotone without mutation then it supports deque operations._

_Proof._ Let _D_=(_r_<sub>1</sub>_,...,r<sub>m</sub>_) and _T_ be the request sequence and initial tree for a deque instance, and assume without loss of generality that the starting tree’s keys are integers. We construct after-trees _T_<sub>1</sub>_,...,T<sub>m</sub>_ for an execution of this instance, as follows. If \(r_i\in\{\mathtt{inject},\mathtt{eject}\}\) then the root of _T<sub>i</sub>_ is its minimum, assuming \(T_i\neq\varnothing\). Otherwise, if \(r_i\in\{\mathtt{push},\mathtt{pop}\}\) then the root of _T<sub>i</sub>_ is its maximum, and if _r<sub>i</sub>_=`pop` and \(\mathrm{min}T_i\neq\mathrm{max}T_i\) then the root’s left child is the minimum key in the tree. The remaining keys _K<sub>i</sub>_ in _T<sub>i</sub>_ are in a subtree at the appropriate location in symmetric order with the following structure. The root _v<sub>i</sub>_ of _K<sub>i</sub>_ is the largest key less than or equal to the median key in _K<sub>i</sub>_, assuming \(K_i\neq\varnothing\). The left and right subtrees of _v<sub>i</sub>_ are respectively right and left spines comprising the keys in _K<sub>i</sub>_\\{_v<sub>i</sub>_} that are less than and greater than _v<sub>i</sub>_. The initial transition tree of this execution has at most |_T_|+1 nodes and the remainder of the execution can<tbc>

So
S1
2
S2
2
2
1
3
1
3
2.5
2.5

Figure 4: After-trees in the construction of \(\mathcal{R}(\chi,T)\) where \(\chi=((\mathtt{delete},12),(\mathtt{insert},15))\) and postorder(_T_)=(2,16,12). The request sequence for the reduced instance is (1,2,3,5/2,3,1,3,2).

