# The Sync Heap: Delete First, Ask Questions Later

**Abstract**

Heaps (priority queues) are among the best-studied data structures in computer science. In this paper, we critically revisit the textbook assumption that in the comparison model at least one of the two standard heap operations of inserting an element and deleting the minimum must take logarithmic time.

By decoupling the deletion itself from the act of revealing the identity of the deleted element to the user, we avoid the sorting barrier and obtain a novel trade-off between the complexities of heap operations. This shows that _the logarithmic barrier is not inherently the cost of deleting the minimum but rather the information cost of immediately learning which element was deleted_. In the special case when the user inspects the heap state only constantly many times, we show that both insertions and deletions can be supported in constant amortized time. As an application, this yields a runtime improvement from O(_n_log_n_) to the optimal O(_n_) for a textbook unit-time scheduling problem.

We obtain our results by designing a new data structure, the _sync heap_, which gains speed by rearranging and compacting its operations until queries force it to synchronize and reveal its state. As a key component, we use the soft heap introduced by Chazelle as part of his minimum spanning tree algorithm. Our data structure is simple, comparison-based, and deterministic, and our results are asymptotically optimal.

### 1 Introduction

A central principle in the study of algorithms is the information-theoretic lower bound for sorting. It implies, in particular, that no comparison-based heap<sup>1</sup> data structure can support both `insert` and `delete-min` operations in sub-logarithmic time, since doing so would imply a heapsort with _o(n_log_n_) running time for an input of size _n_, contradicting the lower bound for sorting. Implicit in this argument is the assumption that deleting the minimum also reveals its identity; this assumption is rarely given much consideration, since in most heap implementations examining the minimum comes essentially for free.

In this paper, we revisit this basic assumption and find that it is precisely the act of revealing information to the user (_observing_ the heap) that drives the complexity of deletions. That is, we show a time complexity dichotomy between an `extract-min` operation that returns the deleted element and a _silent_ `delete-min` operation that does not report anything. We design an online data structure, the _sync heap_, that executes _n_ heap operations containing _d_ silent deletions and _k_ heap observations in O(_n+d_log_k_) total time.<sup>2</sup> In particular, if the user inspects the data structure relatively rarely, we show that all heap operations can be supported in constant amortized time, circumventing the sorting barrier.

<sup>1</sup> By _heap_ we refer here to the abstract data structure, not to a particular implementation; we use the term in preference to _priority queue_ because of its brevity. <sup>2</sup> We define log_x_ as log<sub>2</sub>(max{2_,x_}).

**Benjamin Aram Berendsohn** Max Planck Institute for Informatics **Egor Gorbachev** ETH Zürich **László Kozma** Dresden University of Technology

