_T_ in the classical BST view.

This completes the proof of Theorem 1.3, except for an _O_(loglog_n_)-competitive online algorithm. We show that our _O_(loglog_n_)-approximation algorithm can be adapted to the online setting in Section 7.

## 7 An _O_(loglog_n_)-Competitive Online Algorithm

In this section we extend the _O_(loglog_n_)-approximation algorithm from the previous section to the online setting, obtaining an _O_(loglog_n_)-competitive algorithm and completing the proof of Theorem 1.3. The recursive description of the algorithm from the previous section is however not very convenient for the online setting. In subsection 7.1, we present an equivalent iterative description of the algorithm. In subsection 7.2, we slightly modify the solution _Y_ that the algorithm returns to obtain another solution \(\hat{Y}\) that is more friendly for the online setting, before presenting the final online algorithm in subsection 7.3.

### 7.1 Unfolding the recursion

Let _X_ be an input set of points that is semi-permutation, with |_X_|=_m_, and _c(r_)=_n_. Let _T_ be a balanced partitioning tree of height _H=O_(log_n_) for _X_.

We now construct another tree _R_, that is called a _recursion tree_, and which is unrelated to the tree _T_. Every vertex _q_ of the tree _R_ is associated with an instance I(_q_) of Min-Sat that arose during the recursive execution of Algorithm RecursiveBST\((X,T,\rho)\), with \(\rho=1\). Specifically, for the root _r_ of the tree _R_, we let I(_r_)=_X_. For every vertex _q_ of the tree _R_, if Algorithm RecursiveBST\((X,T,\rho)\), when called for instance I(_q_), constructed instances I<sub>1</sub>_,...,_I_<sub>z</sub>_ (recall that one of these instances is a compressed instance, and the remaining instances are strip instances), then vertex _q_ has _z_ children in tree _R_, each of which is associated with one of these instances.

For a vertex \(q\in V(R)\), let _n(q_) be the number active columns in the instance I(_q_). Recall that<tbc>

q

Figure 9: An illustration of the algorithm. Point _q_ is projected to the boundaries of every strip _S(v_) that contains _q_.

