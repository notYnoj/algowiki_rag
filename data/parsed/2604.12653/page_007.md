<tbc>stronger bound. This terminology is also used in \[2,3\]. Elmasry, Farzan and Iacono \[10\] attempt to define a unified bound for Heaps, based on Iacono’s \[18\] unified bound for binary search trees. They use the term "unified conjecture" for this bound. Their "unified conjecture" bound, using our notation from Definition 1, is \(min_{y\in X:b(y)<b(x)}\big(1+log|\text{rank}(x)-\text{rank}(y)|+log(b(x)-b(y)))\), where rank(_x_) is the number of items currently in the heap that are smaller than _x_. Unfortunately, they show that, if a heap supports insert in amortized _O_(1) time, the running time of \(x\leftarrow\text{extractMin}()\) cannot be within the "unified conjecture".

Definition 1 avoids this obstruction, since it uses the insert time _a(x_) instead of the rank, and has an additional nice property: If you use a binary search tree that has the unified bound (in the sense of Iacono \[18\]) as a heap, the resulting heap has the unified bound (in the sense of Definition 1)<sup>1</sup>.

## Existing heaps fall short of the unified bound.

None of the existing heap data structures \[9, 10,17\] mentioned in the introduction are known to have the unified bound. It is conceivable that the smooth heap or (some variant of) the pairing heap has the unified bound - we see this as an interesting but difficult open problem.

As discussed above, transforming a binary search tree with the unified bound into a heap would yield a heap with the unified bound. Unfortunately, there are no known binary search tree data structures with the unified bound. The splay tree is conjectured to have the unified bound \[18\], but this conjecture remains open. Resolving the dynamic finger conjecture for the splay tree took considerable effort \[5\], and the unified bound would imply this conjecture. The binary search tree data structure of Derryberry and Sleator \[7\] has an additive _O_(loglog_n_) overhead on top of the unified bound. This would raise the running time of `UniTopSort` to _O(n_loglog_n_+log_e(G_)). The dictionaries without this overhead \[2,3,18\] cannot be transformed into a heap, as they are not binary search trees. Thus, there is no easy way of obtaining a heap with the unified bound.

## Comparing the unified bound and the working set bound for heaps.

For some sequences of insert and extractMin operations, the unified bound is strictly stronger than the working set bound: Consider inserting the items 1_,n_+1,2_,n_+2_,...,n,_2_n_ into a heap, and then repeatedly calling extractMin until the heap is empty. A heap with the unified bound can perform these operations in _O(n_) total time, while the working set bound is only _O(n_log_n_). Conversely, we now prove Lemma 3: if a heap has the unified bound, then it automatically has the working set property.

**Lemma 8.** _If a heap has the unified bound, then the_ insert _operation runs in amortized constant time, and the_ \(x\leftarrow\text{extractMin}()\) _operation runs in amortized O_(1+log(1+_t-a(x_))) _time, where t is the number of_ insert _operations performed so far and a(x_) _is as in Definition 1._

Note that _t-a(x_) is the number of insert operations that were performed while _x_ is in the heap, so _O_(1+log(1+_t-a(x_))) is indeed the working set bound.

_Proof._ Consider an arbitrary sequence _S_ of _t_ insert operations and _k_ extractMin operations. Let _x_<sub>1</sub>_,...,x<sub>k</sub>_ be the elements returned by the extractMin operations in order, and let _t<sub>i</sub>_ be the value of _t_ at the time of the \(x_i\leftarrow\text{extractMin}()\) operation. For all real numbers \(\alpha,\beta>0\), we have \(log(1+\alpha+\beta)\le log(1+\alpha)+log(1+\beta)\) and \(log(1+\alpha)\le\alpha\). Therefore,

<sup>1</sup>Curiously, from this viewpoint, the working set property for heaps \[14\] does not correspond to the working set property for binary search trees, but rather to a static finger search property for binary search trees where the finger is the most recently inserted item.

