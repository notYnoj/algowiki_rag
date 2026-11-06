## Adaptive heap data structures

A heap is a data structure that maintains a set of _n_ comparable items under two operations: insert(_x_) adds a new item to the set, and \(x\leftarrow\text{extractMin}()\) removes the smallest item _x_ from the set and returns this item. Some heaps additionally support the operation decreaseKey(_x,y_), which replaces the item _x_ by an item _y_ with _y\<x_. We require that insert runs in _O_(1) (amortized) time and then seek to minimize the running time of extractMin. We say a heap is adaptive if extractMin runs in _o_(log_n_) time for specific sequences of insert and extractMin operations. Adaptive data structures are useful since they allow us to perform \(\Theta(n)\) operations while still achieving a sorting time of _o(n_log_n_).

Iacono \[17\] shows that the pairing heap has the _working set bound_: It supports \(x\leftarrow\text{extractMin}()\) in _O_(log_k_) time where _k_ is the number of insert operations performed while _x_ is in the heap. By using this result, Haeupler, Hladík, Iacono, Rozhoň, Tarjan and Tětek \[14\] obtain their _O_(log_e(G_)+_m_) algorithm for sorting under partial information. Recently, adaptive heap data structures have led to fast algorithms for other problems: Haeupler, Hladík, Rozhoň, Tarjan and Tětek \[13\] design a heap data structure with the working set bound that also supports the decrease-key operation in _O_(1) amortized time. They show that Dijkstra’s algorithm with their heap is universally optimal.

Furthermore, Elmasry \[9\] designs a heap that supports \(x\leftarrow\text{extractMin}()\) in _O_(log_k_) time where _k_ is the number of items that get inserted after _x_ and remain in the heap until _x_ gets extracted. Elmasry, Farzan and Iacono \[10\] design a heap that supports \(x\leftarrow\text{extractMin}()\) in \(O(min(logk,log\ell))\) time where _k_ is defined the same way and \(\ell\) is the number of items that get inserted _before x_ and remain in the heap until _x_ gets extracted. Kozma and Saranurak \[22\] introduce the _smooth heap_, which is conjectured to be instance optimal, but seems difficult to analyze.

## Contribution.

We provide the first algorithm for sorting under partial information that is tight in both preprocessing and sorting time. To this end, we introduce the notion of the _unified bound_ for heaps. Consider an initially empty heap under insert and extractMin operations. We allow some items to remain in the heap at the end of the execution. Let _X_ be the set of items that get inserted into the heap. For an item \(x\in X\), let \(a(x)\in[n]\) denote the number of items that get inserted no later than _x_ gets inserted. If _x_ does not get extracted, put \(b(x)=\infty\), otherwise, let \(b(x)\in[n]\) denote the number of items that get extracted no later than _x_ gets extracted. In other words, _x_ is the _a(x_)-th item to be inserted, and the _b(x_)-th item to be extracted.

**Definition 1.** _A heap data structure has the_ unified bound _if it supports_ insert(_x_) _in amortized O_(1) _time, the very first_ extractMin _operation in amortized O_(1) _time, and subsequent_ \(x\leftarrow\text{extractMin}()\) _operations in amortized time_

\(O\big(min_{y\in Xb(y)<b(x)}\big(1+log|a(x)-a(y)|+log(b(x)-b(y)))\big)\big).\)

Intuitively, the unified bound allows us to use items _y_ that were already extracted as a "finger" to find the item _x_ that gets extracted next. The cost of using a particular item _y_ contains two terms: log|_a(x_)-_a(y_)|, and log(_b(x_)-_b(y_)). Roughly speaking, log|_a(x_)-_a(y_)| measures how "close" _x_ and _y_ are in the insertion order, while log(_b(x_)-_b(y_)) measures how "old" the finger _y_ is. Crucially, we do not need to specify _y_ ourselves; the data structure automatically selects an (asymptotically) optimal _y_. Designing a heap with the unified bound is our main technical contribution:

**Theorem 2.** _There is a heap data structure with the unified bound._

We believe that this data structure and our notion of heaps with the unified bound are of independent theoretical interest. For example, we show:

