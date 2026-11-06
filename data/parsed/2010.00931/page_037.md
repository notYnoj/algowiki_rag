## B. Improvement of Lemma 3

We describe a modification of Algorithm 1, slightly improving the depth-approximation factor. The idea is to execute the root replacement of Line 10 only when necessary. Suppose we call Fix(_T,x_). Let _A=V(T<sub>x</sub>_) and suppose \(|\delta(A)|=k\), and _x_ is a _k_-admissible root of _A_ (see §3.2). Then, we can simply recurse on the children, as in Lines 5-6. From the discussion in §3.2 it is clear that the result is still a _k_-cut tree.

Now suppose that _x_ is not a _k_-admissible root, i.e. \(x\notin\mathsf{ch}(\delta(A))\). Then, in Line 8, we choose _v_ to be the leaf centroid of the tree \(\mathsf{ch}(\{x\}\cup\delta(A))\) instead of \(\mathsf{ch}(\delta(A))\). Observe that the maximum boundary size of components of _S_\[_A_\]\\_v_ is \(\lfloor\frac{k+1}{2}\rfloor+1=\lceil\frac{k}{2}\rceil+1\le k\), so the algorithm is still correct.

We consider how the depth of each node changes by this modified transformation. Let _C_ be the component of _S_\[_A_\]\\_v_ that contains _x_. When changing _T<sub>x</sub>_ to \(T'_v\), a node _u_ in _C_ may either gain _v_ as an ancestor, or otherwise only some nodes on the search path of _u_ are permuted. The depth of _u_ thus increases by at most one. All other nodes in _A_\\_V(C_) lose _x_ as an ancestor and may, at worst, gain _v_ as an ancestor, their depth thus does not increase.

We now argue that, while following the search path from the root to some node _u_ in the final tree _T_<sup>∗</sup> (which corresponds to the recursion tree of Fix), the depth of a node can only increase every \(\lfloor k/2\rfloor+1\) steps. We already observed that an increase in depth can only happen in the following situation: _x_ is not a _k_-admissible root of _A=V(T<sub>x</sub>_) and _u_ is in the same connected component _C_ of _S_\[_A_\]\\_v_ as _x_. We know that \(v\in\delta(C)\). As \(x\in V(C)\), and because of our choice of _v_, there are at most \(\lfloor\frac{k+1}{2}\rfloor-1=\lceil k/2\rceil-1\) other nodes in \(\delta(C)\). This means that after executing the non-recursive portions of Fix(_T,x_) (which replaced _x_ with _v_) and then \(\mathsf{Fix}(T',x)\) (which cannot change the tree), the depth cannot increase for the next \(\lfloor k/2\rfloor\) calls on the path to _u_.

Thus, the depth of each node increases by a factor of at most \(1+1/\lfloor k/2\rfloor\). We obtain the following.

**Lemma 19** (Strengthening of Lemma 3)**.** _Given an STT T on S and_ \(k\ge 2\)_, we can find a k-cut STT T_<sup>∗</sup> _on S, so that_ \(\mathtt{depth}_{T^*}(x)\le(1+\epsilon_k)\cdot\mathtt{depth}_T(x)\) _for all_ \(x\in V(S)\)_, where_<tbc>

\(\varepsilon_k=\frac{1}{\lfloor\frac{k}{2}\rfloor}.\)

