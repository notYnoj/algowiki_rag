**Theorem 2.5.** _The mputs problem with n jobs can be solved in_ O(_n_) _time._

The problem appears in many classical textbooks on algorithms and scheduling with O(_n_log_n_)- time solutions; see [CLRS09, §16.5], [Bru07, §4.4.2], [HSR08, §4.4]. The following algorithm, originally due to Lawler [Law76], correctly solves the problem in O(_n_log_n_) time:

Cap all due dates by _n_ and process the jobs in nondecreasing order of their due dates. Maintain a min-heap _H_, initially empty. When job _j_ is processed, insert _j_ into _H_. If the number of jobs stored in _H_ is greater than _d<sub>j</sub>_, remove the minimum-profit job from _H_. At the end of the algorithm, the jobs remaining in _H_ are a maximum-profit feasible set of jobs. Furthermore, ordering the jobs in _H_ by nondecreasing due date gives a valid execution schedule.

Note that processing the jobs by their due dates does not imply a sorting bottleneck, as these values are integers between 1 and _n_; the superlinear running time is only due to the operations on heap _H_, which stores jobs with their profit as the key. Lawler’s algorithm is, in fact, similar to `ReverseHeapEval` (Algorithm 1) when implemented with an exact heap, and can be seen to solve an instance of the heap evaluation problem.

We use this observation to speed up the algorithm, as follows. Simulate the steps of the algorithm, but instead of carrying out the heap operations `insert` and `delete-min` on _H_ in real time, record them as a sequence S. Notice that the operations do not depend on the outcomes of past operations, only on the job due dates and on the number of elements currently in the heap, which we can simulate with a counter. Running the simulation clearly takes O(_n_) time. Finally, after obtaining the heap operation sequence S of length at most 2_n_, we use Theorem 1.1 to evaluate the final state of the heap in O(_n_) time. This implies Theorem 2.5.

To the best of our knowledge, this is the first linear-time algorithm in the literature for mputs with arbitrary comparable profits and integer due dates, without assuming that the profits are given in sorted order. We observe that the single-machine assumption is without loss of generality: the variant with _m_ machines is equivalent to the problem with one machine and processing time 1_/m_ for each job.

## 3 The Sync Heap

In this section, we turn the offline algorithm of §2 into an online data structure we call the _sync heap_. We support operations `insert`, silent `delete-min`, `find-min`, and `reveal-deletions`. As before, we call the first two operations _modifications_ and the other two _observations_. The silent `delete-min` removes the current minimum without revealing it. The operation `reveal-deletions` returns, in arbitrary order, all elements deleted by `delete-min` operations since the last `reveal-deletions` (or since the beginning of the execution if this is the first call of `reveal-deletions`). We analyze the optimal time complexity in terms of the total number _n_ of operations and the number _k_ of observations (`find-min` and `reveal-deletions`). Building on the results of §2, we prove the following theorem.

**Theorem 3.1.** _There is a deterministic data structure, the sync heap, that supports the operations_ `insert`, `find-min`, and `reveal-deletions` in constant amortized time and silent `delete-min` operations in_ O(log_k_) _amortized time, where k is the number of_ `find-min` and `reveal-deletions` _operations up to the current moment._

Before we prove Theorem 3.1, we review an important data structure called the _selectable heap_ that we use as a component. Selectable heaps augment regular heaps with batched deletions which are executed more efficiently than individual ones.

