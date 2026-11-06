In the remainder, we find it convenient to work with logarithms of size of search spaces. For this purpose, we will use the term "bit". The learning of one "bit" by the algorithm corresponds to the halving of the search space of some large element.

**Mechanics of the adversary’s strategy:** Our adversary will try to maintain the following invariant at all times during the execution of the algorithm.

**Invariant:** The search intervals of large elements in main memory are disjoint.

We denote by \(\{\ell_i^{p-1}\}_{i=1}^{M/w}\) the set of at most _M/w_ large elements in memory before the _p_th I/O. By hypothesis, the nodes in T belonging to the set \(\{v(\ell_i^{p-1})\}_{i=1}^{M/w}\) have no ancestor-descendant relationships between them. We write \(S_i^{p-1}\) to denote \(I(v(\ell_i^{p-1}))\), the search interval of large element \(\ell_i^{p-1}\) at step _p_-1.

**Small-block input.** Consider the incoming block. We denote _n<sub>p,i</sub>_ as the number of incoming small elements that belong to \(S_i^{p-1}\). These elements divide \(S_i^{p-1}\) into _n<sub>p,i</sub>_+1 parts {_P_<sub>1</sub>_,...,P<sub>n<sub>pi</sub></sub>_+1}, some of them possibly empty. The largest of these parts (say _P<sub>j</sub>_) is of size at least 1/(_n<sub>p,i</sub>_+1) times the size of \(S_i^{p-1}\). The new search interval of \(\ell_i^p\) is defined to be the highest node in T such that \(I(v)\subset P_j\).

**Large element input.** On an input of a large element \(\ell_\text{new}^p\) (with search interval \(S_\text{new}^{p-1}\)), the adversary uses a strategy similar to that one on a small- block input to compare \(\ell_\text{new}^p\) with the (at most) _M_ small elements present in memory. These _M_ small elements divide \(S_\text{new}^{p-1}\) into at most _M_ parts, and the new search interval of \(\ell_\text{new}^p\) corresponds to the highest node in T that contains the largest part.

This is the temporary search interval _S_new, with the corresponding node _v_new.

_S_new can be related to the search intervals of large elements in memory in three ways:

**Case 1.** The element \(\ell_\text{new}^p\) shares a node with another large element \(\ell_i^p\). The conflict is resolved by sending \(\ell_\text{new}^p\) and \(\ell_i^p\) to the left and right children of _v_new, respectively.

**Case 2.** The element \(\ell_\text{new}^p\) has an ancestor in memory. The ancestor is sent one level down, to the child that does not contain _v_new in its subtree. Thus the conflict is resolved while giving at most _O_(1) bit.

**Case 3.** The element \(\ell_{new}^p\) has descendants in memory.

