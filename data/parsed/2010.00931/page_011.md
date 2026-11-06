exactly the _Steiner-closed trees_. Note that these equivalences directly imply Observation 4, since, by definition, every 2-cut tree is also a 1-cut tree.

As the number of possible cut edges in a tree is O(_n_), the following observation is immediate, implying that the number of possible subtrees of a _k_-cut tree is polynomial, rather than exponential.

**Observation 5.** _The number of subsets_ \(A\subseteq V(S)\) _with boundary size at most k is_ O(_n<sup>k</sup>)._

The following technical lemma relates the boundary sets before and after the removal of a node, and will be useful in the remainder of the section.

**Lemma 2.** _Let S be a tree, let S_\[_A_\] _be a subtree of S, and let_ \(r\in A\subseteq S\)_. Let N(r_) _be the set of neighbors of r in S, and let C_<sub>1</sub>_,C_<sub>2</sub>_,...,C<sub>t</sub> be the connected components of S_\[_A_\]\\_r. Then:_

\(\bigcup_{i=1}^t\delta(C_i)=\delta(A)\cup\{r\}\backslash N(r).\)

_Proof._ Let \(v\in\delta(C_i)\) for some \(i\in[t]\). Then there is an edge {_v,u_} with \(u\in V(C_i)\). Either _v=r_, or the unique path from _v_ to _r_ in _S_ contains _u_, and therefore \(v\notin N(r)\). If \(v\neq r\), then \(v\notin C_j\) for all \(j\neq i\), as otherwise _C<sub>i</sub>_ and _C<sub>j</sub>_ were connected in _S_\[_A_\]\\_r_. It follows that \((v,u)\in\mathtt{cut}(A)\), so \(v\in\delta(A)\).

Conversely, let \(v\in\delta(A)\cup\{r\}\backslash N(r)\). If _v=r_, then \(v\in\delta(C_i)\) for all _i_. Otherwise, let \(v\in\delta(A)\backslash N(r)\), and let \(v'\in A\) such that \((v,v')\in\mathtt{cut}(A)\). By assumption, \(v'\neq r\). Let _C<sub>i</sub>_ be the connected component of _S_\[_A_\]\\_r_ that contains \(v'\). Then \(v\in\delta(C_i)\).

Observe that Lemma 2 directly implies that if _x_ is a child of _p_ in _T_, then \(\delta(T_x)\subseteq\delta(T_p)\cup\{p\}\). Consequently, the boundary \(\delta(T_x)\) of a node _x_ consists entirely of ancestors of _x_ in _T_.

The rest of this section is dedicated to the proof of Theorem 1 and is organized as follows. In §3.1 we show that an optimal _k_-cut STT approximates an optimal general STT by a factor of roughly \(1+\frac{2}{k}\). In §3.2 we generalize the dynamic programming algorithm for BSTs and show that an optimal _k_-cut STT can be found in polynomial time.

## 3.1. _k_-cut trees approximate depth

In this subsection we show that an arbitrary STT _T_ can be transformed into a _a k-cut STT_ \(T'\), so that the depth of every node increases by a factor of no more than (roughly) \(1+\frac{2}{k}\). The proof is based on a similar idea as the proof of Lemma 1 by Bose et al. \[BCI<sup>+</sup>20\]: problematic nodes are fixed one-by-one, carefully controlling the depth-increase of every node. The cases _k\>_2 require however some further ideas, in particular, we make use of the _leaf centroid_ of a tree, defined next.

**Definition 6** (Leaf centroid)**.** Let _S_ be a tree on \(n\ge 3\) nodes, having \(\ell\) leaves. A non-leaf node \(v\in V(S)\) is a _leaf centroid_ of _S_ if every connected component of _S_\\_v_ has at most \(\lfloor\frac{\ell}{2}\rfloor+1\) leaves, at most \(\lfloor\frac{\ell}{2}\rfloor\) of which are leaves of _S_.

