candidate will survive the processed suffix. Therefore, such a maximum candidate can be discarded. The pseudocode for this algorithm, `ReverseHeapEval`, is given in Algorithm 1. Since the algorithm is slightly more complex than the previous one, we first analyze it with an exact heap.

`ReverseHeapEval(S) begin` `2` \(H\leftarrow\mathtt{MaxHeap}()\) `3` \(\delta\leftarrow 0\) _// Number of deletion slots in the processed suffix_ `4` **for** \(\sigma\in\mathtt{reversed}(\mathcal{S})\) **do** `5` **if** \(\sigma=\mathtt{insert}(x)\) **then** `6` _H._`insert`(_x_) `7` **if** \(|H|>\delta\) **then** `8` _H._`delete-max`() `9` **else if** \(\sigma=\mathtt{delete-min}\) **then** `10` \(\delta\leftarrow\delta+1\) `11 return E(_H_)` `Algorithm 1` A heap-based algorithm for computing \(\mathcal{D}(\varnothing,\mathcal{S})\). The algorithm reverses the timeline and maintains the set of deleted elements.

`Example.` Consider the sequence \(\mathcal{S}=\big(\mathtt{insert}(a_2),\mathtt{insert}(a_4),\mathtt{delete-min},\mathtt{insert}(a_3),\mathtt{insert}(a_5),\mathtt{delete-min},\mathtt{delete-min},\mathtt{insert}(a_1)\big)\) from §1, where key(_a<sub>i</sub>_)=_i_. Starting with an empty max- heap _H_ and \(\delta=0\), `ReverseHeapEval` scans the sequence from right to left. The following table shows the state after each step; the last column records the element discarded when \(|H|>\delta\).

Thus, `ReverseHeapEval` returns \(\mathcal{D}(\varnothing,\mathcal{S})=\{a_2,a_3,a_4\}\), while _a_<sub>1</sub> and _a_<sub>5</sub> survive the original sequence.

**Lemma 2.3. `ReverseHeapEval`**, _when implemented with an exact max-heap, computes_ \(\mathcal{D}(\varnothing,\mathcal{S})\).

**Proof.** We prove by induction over the suffixes T of S that after `ReverseHeapEval` processes T , the invariant \(\mathcal{E}(H)=\mathcal{D}(\varnothing,\mathcal{T})\) holds. Observe that \(\delta\) is the number of `delete-min` operations in T . The invariant is trivial for an empty suffix. Now suppose that the invariant holds for a suffix T , and let \(\sigma\) be the operation immediately preceding T in the original order. If \(\sigma=\mathtt{delete-min}\), then \(\sigma\) is unsuccessful in a forward execution of \(\sigma\mathcal{T}\) from an empty heap. Thus, prepending \(\sigma\) to T does not change the deleted set.

Now suppose that \(\sigma=\mathtt{insert}(x)\). A forward execution of \(\sigma\mathcal{T}\) from an empty heap is equivalent to a forward execution of T from a heap initially containing only _x_. Compare forward executions of T starting from \(\varnothing\) (heap \(F_\varnothing\)) and from {_x_} (heap _F<sub>x</sub>_) in parallel. Observe that at all times either

\begin{tabular}{cccc}
Operation & \(\delta\) & E(_H_) & Discarded element \\ `insert(a<sub>1</sub>)` & 0 & \(\varnothing\) & _a_<sub>1</sub> \\ `delete-min` & 1 & \(\varnothing\) & - \\ `delete-min` & 2 & \(\varnothing\) & - \\ `insert(a<sub>5</sub>)` & 2 & {_a_<sub>5</sub>} & - \\ `insert(a<sub>3</sub>)` & 2 & {_a_<sub>3</sub>_,a_<sub>5</sub>} & - \\ `delete-min` & 3 & {_a_<sub>3</sub>_,a_<sub>5</sub>} & - \\ `insert(a<sub>4</sub>)` & 3 & {_a_<sub>3</sub>_,a_<sub>4</sub>_,a_<sub>5</sub>} & - \\ `insert(a<sub>2</sub>)` & 3 & {_a_<sub>2</sub>_,a_<sub>3</sub>_,a_<sub>4</sub>} & _a_<sub>5</sub> \\ \end{tabular}

