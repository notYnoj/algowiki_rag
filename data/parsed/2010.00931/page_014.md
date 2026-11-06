_Proof._ Let \(c_i=|\delta(T'_{u_i})|\) for \(i\in[t]\). As _u<sub>i<sub>j</sub></sub>_ is not in _P_, at some point, Algorithm 1 must have rotated _u<sub>i<sub>j</sub></sub>_ up. This means that in some recursive call, _u<sub>i<sub>j</sub></sub>_ is the leaf centroid _v_ that is rotated up in Line 10 and, in particular, _c<sub>i<sub>j</sub></sub>=k_. Similarly, _c_<sub>_i<sub>j</sub>_+1</sub>=_k_. Let \(\ell=i_{j+1}-i_j\).

As _u_<sub>_i<sub>j</sub>_+1</sub> is a child of _u<sub>i<sub>j</sub></sub>_ in _T_<sup>∗</sup>, we have \(c_{i_j+1}\le\lfloor k/2\rfloor+1\) by Lemma 5. By Lemma 4, we generally have \(c_{i+1}\le c_i+1\) for each \(i\in[t-1]\). This means that \(k=c_{i_{j+1}}=c_{i_j+\ell}\le\lfloor k/2\rfloor+\ell\), which implies that \(\ell\ge\lceil k/2\rceil\).

As _c_<sub>1</sub>=0, we also have \(i_1\ge k+1\ge\lceil k/2\rceil\). As such, we can uniquely assign \(\lceil k/2\rceil-1\) "direct predecessor" nodes in _P_ to each node in \(P'\backslash P\). This proves the upper bound for _s_.

### Running time.

In each recursive call we compute the boundary size of _V(T<sub>x</sub>_) in linear time, e.g. by finding the ancestors of _x_ in _T_ and then traversing _V(T<sub>x</sub>_) from _x_. Furthermore, we may rotate one node to the root (of _T<sub>x</sub>_), which requires linear time. As each node _v_ corresponds to exactly one recursive call (which returns a subtree rooted at _v_), the total running time is O(_n_<sup>2</sup>). This concludes the proof of Lemma 3.

### Remark.

When _k_ is even, Lemma 3 can be slightly strengthened to obtain \(\varepsilon_k=\frac{1}{\lceil k/2\rceil}\), at the cost of a slightly more involved procedure. In particular, this extends the statement to the _k_=2 case. Without the improvement, the running time stated in Theorem 1 would be O(_n_<sup>2_t_+2</sup>) instead of O(_n_<sup>2_t_+1</sup>).

Intuitively, the improvement comes from the observation that the root-replacement of Line 10 in Algorithm 1 is too "proactive". When _T<sub>x</sub>_ matches the boundary size condition with equality, it may be too early to rotate the replacement-root _v_ to the top, as the boundary size may recover as we go further down, if _x_ happens to split the tree in a reasonably balanced way. We defer the details of this small improvement to Lemma 19, Appendix B. With the improved bound and the observation that 2-cut trees are exactly the Steiner-closed trees (§4.2), the result of this subsection directly generalizes Lemma 1.

## 3.2. Finding an optimal _k_-cut tree

Let \(T'\) be a _k_-cut STT on _S_ that serves the search sequence _X_ of length _m_ with minimal cost among all _k_-cut STTs. Let _r_ be the root of \(T'\), let \(T'_1,\dots,T'_t\) be the subtrees rooted at children of _r_, and let _X<sub>i</sub>_ be the subsequence of _X_ consisting of searches to nodes of \(T'_i\). Then, \(\mathtt{cost}_{T^\prime}(X)=m+c_1+\cdots+c_t\), where \(c_i=\mathtt{cost}_{T_i^\prime}(X_i)\), for all _i_.

By definition, the trees \(T'_i\) are _k_-cut trees. Our strategy is to find _r_ and to recursively compute _k_-cut STTs _T_<sub>1</sub>_,...,T<sub>t</sub>_ on the components of _S_\\_r_ that achieve cost at most _c<sub>i</sub>_ for their respective sequences _X<sub>i</sub>_, i.e. for the relevant frequencies \(p:V(T'_i)\rightarrow\mathbb{N}\), for all _i_. We then return the tree _T_ obtained by letting the roots of _T_<sub>1</sub>_,...,T<sub>t</sub>_ be children of the root _r_.

The cost equation translates into the straightforward dynamic program Algorithm 2. We call those sets of nodes \(A\subseteq V(S)k\) _-admissible_ for which _S_\[_A_\] is connected and has boundary size at most _k_. We call a node \(x\in A\) a _k-admissible root_ of _A_ if the node sets of all connected components of _S_\[_A_\]\\_x_ are _k_-admissible.

Procedure OPT-STT in Algorithm 2 computes an optimal _k_-cut tree for a _k_-admissible set \(A\subseteq V(S)\) and the relevant frequencies \(p:A\rightarrow\mathbb{N}\). The initial call is OPT-STT(_V(S_)).<tbc>

