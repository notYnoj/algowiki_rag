**Lemma 3** (Informal Lemma 8)**.** _If a heap has the unified bound, then it also has the working set property._

Next, we use this heap to design a fast algorithm for sorting under partial information. Let `UniTopSort` be the following two-phase algorithm: In the preprocessing phase, `UniTopSort` computes a topological ordering of _G_. This is the only preprocessing step, and takes _O(n+m_) time. In the sorting phase, `UniTopSort` considers all items of _X_ in topological order and inserts them into a heap with the unified bound. Then, it repeatedly extracts the minimum from the heap. This yields _X_ in sorted order. Note that, to perform the insert and extractMin operations, the heap has to compare items. But this is fine, since we have access to the linear order _L_ in the sorting phase. _A priori_, it seems unlikely that `UniTopSort` achieves _O_(log_e(G_)+_n_) sorting time. Indeed, the only information about the graph _G_ that `UniTopSort` retains is a topological ordering. Surprisingly, we show:

**Theorem 4.** _`UniTopSort` has O(n+m_) _preprocessing time and O_(log_e(G_)+_n_) _sorting time._

From Theorem 4, we apply existing reductions to reduce the preprocessing time to _O(m_) and the sorting time to _O_(log_e(G_)). The sorting time bounds the number of comparisons. This yields:

**Theorem 5.** _We can preprocess a DAG G on X in O(m_) _time, so that, given an unknown linear order L on X and the guarantee that all edges in G go from smaller items to larger items with respect to L, we can sort X in O_(log_e(G_)) _time and comparisons._

### Comparison to existing algorithms for DAG sorting

Both `UniTopSort` and the algorithm of Haeupler, Hladík, Iacono, Rozhoň, Tarjan and Tětek \[14\] are variants of Heapsort that use an adaptive heap data structure guided by a topological ordering of _G_. Thus, at a surface level, these algorithms might look similar. However, the two algorithms operate very differently. Let us illustrate three key differences:

(1) The algorithm of \[14\] tries to keep the heap as small as possible, by inserting items on the fly once they become relevant (i.e. become sources in _G_). Thus, the algorithm interleaves insert and extractMin operations. `UniTopSort` inserts all _n_ items into the heap immediately.

(2) The algorithm of \[14\] is closely tied to the graph _G_: Whenever an item is extracted from the heap, the algorithm looks at all outgoing edges from that item. This yields the _O(m_) term in the sorting time. `UniTopSort` does not care about the individual edges of _G_ beyond using them to find a topological ordering of _G_.

(3) The heap used by \[14\] is much simpler than the one we use: You can obtain a heap with the working set via a simple bucket-based construction with heaps of exponentially increasing sizes \[31\]. Our construction of a heap with the unified bound is involved. We have reasons to believe that an involved construction is necessary, as the cost function in the unified bound contains two separate terms (log|_a(x_)-_a(y_)| and log(_b(x_)-_b(y_))). We discuss prior attempts at this in Section 2.2.

The other existing algorithms for DAG sorting do not use heaps: \[30\] use a variant of insertion sort with a finger search tree, where they look at all outgoing edges of an item to determine the optimal finger. \[4\] and \[19\] decompose the graph into paths and use a variant of merge sort based on Huffman trees.

## 2 Preliminaries

We denote \[_n_\]={1,2_,...,n_} and we use log for the base-2 logarithm. Let _X_ be the set of items and let _G_ be a DAG with vertex set _X_. We say a linear order _L_ on _X_ is _compatible with G_ if all edges in _G_ go from a smaller item to a larger item under _L_, that is, _x\<<sub>L</sub>y_ for every edge \(x\rightarrow y\).

