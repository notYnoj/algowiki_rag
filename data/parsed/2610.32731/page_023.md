### Running time.

As for WSHTreeSelect, the running time of operations in _Q_ (except `increase-weight`) and the heapifications is bounded in the same way the comparisons are. Otherwise, we spend constant time per element inserted into _Q_ (so \(\mathcal{O}(|S^*|)\le\mathcal{O}(k+\mathrm{OPT})\) in total), with the exception of the parts listed below. Let _e_<sup>∗</sup> denote the number of edges in _G_<sub>0</sub> with one or both endpoints in \(C\cup D\).

• Deleting a node from _G_ or \(G'\) takes time linear in the out-degree of that node. Finding newly created sources can be done in the same time. For \(G'\), the overall time is thus clearly O(_e_<sup>∗</sup>). For _G_, observe that we add at most one three new out-edges per node, so we can bound the time to delete from \(G'\) by \(\mathcal{O}(e^*+|C\cup D|)\le\mathcal{O}(e^*+|S^*|)\).<tbc>

• An `increase-weight` call in line 26 is performed if the second-to-last in-neighbor of some node is removed. Thus, there are O(|_S_<sup>∗</sup>|) such calls. To perform these calls at the right time, we need to check the in-degree of a node whenever an edge is removed, in O(_e_<sup>∗</sup>) time overall.<tbc>

• Line 10 may take \(\Theta(k^2)\) time in total. This can be reduced to O(_k+e_<sup>∗</sup>) in a similar way as for WSHTreeSelect (see the end of section 5), although we need to account for the fact that nodes may have multiple in-neighbors.<tbc>

<tbc>Maintain a set _R_ of "ready" nodes. When traversing a node with line 11, put it into _R_, unless it is deleted in the same iteration. At the start of each iteration, check if _R_ contains a node _v_ with in-degree zero. If so, set \(x\leftarrow v\) and skip lines 9 to 11. Maintaining the in-degrees of nodes in _R_ takes O(_e_<sup>∗</sup>) time in total.

We have shown:

**Theorem 34.** _There exists an algorithm for poset selection that takes_ O(_k_+OPT(_P,k_)) _comparisons and_ O(_k_+OPT(_P,k_)+_e_<sup>∗</sup>) _time for each instance_ (_P,k), where e_<sup>∗</sup> _is the number of edges incident to some prefix of P of size_ O(_k_+OPT(_P,k_)).

## 7 Almost-optimal algorithms for trees

In this section, we present improved algorithms for trees for the case OPT(_G,k)\<o(k_) (theorems 2 and 3). Throughout this section, we make the technical assumption that \(k\ge 2\) (otherwise, the problem is trivial).

### 7.1 Contracting the tree

Let _T_ be a tree. The \(\ell\)_-contraction_ of _T_, written \(T^\ell\), is a tree obtained as follows (see fig. 5). Starting at the root _v=r_, perform the following recursive procedure. Determine the maximum-depth node _u_ such that _u_ is a descendant of _v_ or _v_ itself and the path between _u_ and _v_ is an induced path _P_ in _T_ of length at most \(\ell\). Replace _P_ by _u_. That is, delete all nodes in _P_\\{_u_}, and make _u_ a child of the parent of _v_ (unless _v_ is the root). We write _P(u_) for the set of nodes replaces by _u_ (including _u_) itself. Further, we write size(_u_)=|_P(u_)|.

