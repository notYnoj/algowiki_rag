**PLE-DFS:** PLE-DFS builds a static B-tree _T_ on _S_, and searches for large elements in _T_ one by one. This approach is preferred in the case of really large elements, and it is better to input them fewer times.

We dynamically maintain a smaller B-tree \(T'\) that contains only _border elements_ (the two small elements sandwiching each large element in the final sorted order) and has depth at most log_<sub>B</sub>k_. All large elements first travel down \(T'\) to locate their stripe. Only those elements for which their stripe has not yet been discovered need to travel down _T_. After a new stripe is discovered in _T_, it is then added to \(T'\). The total cost becomes

\(O\left(\frac{L}{w}log_Bk+klog_BS+\frac{L}{B}+\frac{S}{B}\right).\) (1)

**PLE-BFS:** Our second algorithm for PLE uses a batch-searching tree with fanout \(\Theta(M)\). When a node of the tree is brought into memory, we route all large elements via the node to the next level. We process the nodes of the _M_-tree level by level so all large elements proceed at an equal pace from the root to leaves. This technique is helpful when large elements are sufficiently small so that bringing them many times into memory does not hurt while they benefit from a large fanout.

The analysis is as follows: at each level of M-tree, the algorithm spends \(\Theta(L/B)\) I/Os in large-element inputs. Every node of the tree is brought in at most once, which results in total _O(S/B_) I/Os in small-element inputs. The total number of memory transfers for PLE-BFS then becomes

\(O\left(\frac{L}{B}log_MS+\frac{S}{B}\right).\) (2)

Our final upper bound is the better of the two algorithms:

**Theorem 18** (**PLE Upper Bound**)**.**

\(\text{PLE}\left(S,L\right)=O\left(min\left\{\frac{L}{B}log_MS+\frac{S}{B},\frac{L}{w}log_Bk+klog_BS+\frac{L}{B}+\frac{S}{B}\right\}\right).\)

Substituting the lower and upper bounds of the batched predecessor problem (PLE(_S,L_)) derived in Theorems 3 and 4 into the complexity of sorting in Theorem 2 gives us lower and upper bounds on the sorting problem Sort(_S,L_).

**Remark 1:** One observes that in Theorem 4 (PLE(_S,L_) lower bound), the transition between the two terms in the minimum happens at _w=B_log_M_. This is because when large elements are very large, the bound obtained<tbc>

