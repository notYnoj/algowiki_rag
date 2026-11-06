_O_(1) time whether a given parent _p_ can be activated. Whenever we do activate _p_, the size of the linked list shrinks by one, so this happens _O(N_) times. We also spend _O(N_) time scanning through the linked list, moving the pointer to _t_, and unsuccessfully activating nodes. Building a balanced binary tree takes linear time in its size. Thus, rebuilding _L_<sub>0</sub>_,...,L<sub>i</sub>_ takes _O(N_) time.

**Theorem 24.** Cleanup _maintains all invariants, has an amortized running time of O_(1)_, and restores the stronger bound in invariant (6)._

_Proof._ Cleanup only modifies the data structure via cleanupStep. By Lemma 22, cleanupStep maintains all invariants. And cleanup only terminates once the stronger bound in invariant (6) holds for all index trees. Thus, all invariants are maintained.

Cleanup spends _O_(1) time checking whether there are any index trees that are too big, in which case it performs a cleanupStep. This is repeated until no cleanupStep happens. If cleanup performs at least one cleanupStep, then the _O_(1) overhead of cleanup is dominated by the time spent in cleanupStep, so the amortized running time of cleanup is zero by Lemma 23. If no cleanupStep happens, then the running time of cleanup is _O_(1).

### 5.8 Putting things together

After every addLeaf or access operation, we run cleanup. We show that our construction achieves Theorem 12:

**Theorem 12.** _There is a data structure that maintains a rooted binary tree on top of n leaves numbered_ 1_,...,n that each store an item, such that each node in the tree stores its subtree minimum and every leaf i has depth O(d(i_))_. The data structure supports the operations:_

• addLeaf(_x): In amortized O_(1) _time, increment n and add a new leaf with index n, value x, and_ \(s(n)=-\infty\).<tbc>

• access(_i): In amortized O(d(i_)) _time (computed before the operation), set s(i_)=_t and then increment t. For the very first access operation, d(i_) _is ill-defined, so we require a bound of amortized O_(1) _time instead._<tbc>

• changeKey(_i,x): In O(d(i_)) _time, replace the item stored at leaf i with x._

_The data structure may remodel the internal tree nodes arbitrarily (within the allowed time bounds). The leaves do not need to be stored in order._

_Proof._ By Lemmas 14 and 15 every leaf _i_ has depth _O(d(i_)). By Theorem 20, addLeaf runs in amortized _O_(1) time. By Lemma 19, access runs in amortized _O(d(i_)) time. By Theorem 24, running cleanup after these operations does not increase the amortized running time. Since the values of items have no effect on the structure of our heap, we only need to update the subtree minima during changeKey. This takes worst case _O(d(i_)) time. Since we run cleanup after every addLeaf or access operation, Lemma 18 and Theorems 20 and 24 show that we maintain all invariants.

## 6 A Slightly Stronger Unified Bound

There are multiple slightly different ways of defining the working set property of heaps \[9, 14, 17\]. The simplest one is that \(x\leftarrow\text{extractMin}()\) takes _O_(log_k_) time where _k_ is the number insert operations while _x_ is in the heap. In the stronger, but more complicated definition, of Elmasry \[9\],<tbc>

