<tbc>techniques [GT85]. If the ranks of all inserted elements are known, the algorithm of Gabow and Tarjan [GT85, §4] can also solve the "offline" heap evaluation problem of Theorem 1.1 in linear time, even identifying the element removed by each individual deletion. However, finding the ranks amounts to sorting; what makes our heap evaluation problem interesting is exactly the fact that the ranks are unknown.

**Note on independent work.** After our paper was made public, we became aware that a linear-time algorithm for unit-time scheduling was also described by Matthias Görgens in a Computer Science Stack Exchange answer cs.stackexchange.com/a/171695/50292, based on ideas similar to those in the proof of Theorem 1.1. Our work was developed independently.

## 2 Heap Evaluation

In this section, we prove the following theorem.

**Theorem 1.1** (Heap evaluation)**.** _There is a deterministic comparison-based algorithm that, given a sequence_ S _of_ `insert` _and_ `delete-min` _operations on an initially empty heap, computes the (unordered) list of elements remaining in the heap after the execution of_ S _in_ O(|S|) _total time._<sup>4</sup>

We introduce some basic notation. For a nonempty set _X_ of elements with distinct keys, let min(_X_) be the element of _X_ with the smallest key and max(_X_) be the element of _X_ with the largest key. If _H_ is a data structure storing a set of elements, let E(_H_) denote the contents of _H_. Given a set _X_ of elements and a sequence S of heap operations, let D(_X,_S) be the set of elements removed by all the `delete-min` operations while executing S on a heap _H_ initially satisfying E(_H_)=_X_. Finally, let R(_X,_S) be E(_H_) at the end of that execution. (Here, E stands for **e**elements, D stands for **d**eleted elements, and R stands for **r** remaining elements.) In particular, Theorem 1.1 asks to compute \(\mathcal{R}(\varnothing,\mathcal{S})\).

As a baseline, executing S with an ordinary heap takes O(_n_log_n_) time, where _n_ is the total number of insertions in S.<sup>5</sup> Call this algorithm `TrivialHeapEval`.

The main tool in our improved algorithm is the soft heap of Chazelle [Cha00b]. Soft heaps achieve constant amortized time for both `insert` and `delete-min` operations by allowing some of the keys to be _corrupted_.

**Lemma 2.1** (Soft heap [Cha00b, KTZ13, Bro21])**.** _For every parameter_ \(\varepsilon\in(0,1/2]\)_, there is a deterministic data structure that maintains a set of elements with comparable keys, supports the operations_ `insert` _and_ `delete-min`_, and satisfies the following properties. After every operation, the data structure may increase the keys of some elements. The_ `delete-min` _operation deletes an element whose current key is the smallest. Call an element_ corrupted _if its key was ever increased. The data structure guarantees that after every operation, the number of corrupted elements in the heap is bounded by_ \(\varepsilon\cdot I\)_, where I is the total number of insertions so far. Each operation takes amortized_ \(\mathcal{O}(log\frac{1}{\varepsilon})\) _time._

<sup>4</sup> Note that if distinct elements are allowed to have equal keys, the solution to the heap evaluation problem is not well-defined. For this reason, throughout the paper we assume that the keys of all elements are distinct. This limitation can be circumvented by a standard trick of comparing equal-key elements according to their insertion times. <sup>5</sup> We may assume that \(n\le|\mathcal{S}|\le 2n\) holds. To achieve this, we initially identify all unsuccessful `delete-min` operations in S and remove them from S in linear time.

