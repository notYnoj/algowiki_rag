## 6 The Sync Heap: Delete First, Ask Questions Later

To clearly distinguish an ordinary heap from a soft heap, we sometimes refer to the former as an _exact heap_. Our algorithm for Theorem 1.1 repeatedly executes one of two reduction steps. The first works when at most half of the inserted elements are deleted (i.e., \(|\mathcal{D}(\varnothing,\mathcal{S})|\le|\mathcal{R}(\varnothing,\mathcal{S})|\)); the second works when more than half of the inserted elements are deleted (i.e., \(|\mathcal{D}(\varnothing,\mathcal{S})|>|\mathcal{R}(\varnothing,\mathcal{S})|\)). One of the two steps is always applicable and reduces the problem size by a constant factor in linear time.

### Handling few deletions.

Our first algorithm replaces the exact heap in `TrivialHeapEval` with a soft heap with parameter \(\varepsilon=1/4\). We claim that if an uncorrupted element _x_ belongs to the soft heap \(\tilde{H}\) at the end of the execution, then _x_ would also belong to the exact heap after the same execution. Intuitively, increasing keys may postpone deletions of corrupted elements but cannot make uncorrupted elements survive for longer.

**Lemma 2.2.** _Suppose that a sequence_ S _of heap operations is executed on an initially empty soft heap_ \(\tilde{H}\)_. Let_ \(\tilde{X}\) _be the set of uncorrupted elements in_ \(\tilde{H}\) _at the end of the execution. Then_ \(\tilde{X}\) _is a subset of_ \(\mathcal{R}(\varnothing,\mathcal{S})\).

**Proof.** Fix some \(x\in\tilde{X}\) and let _a_:=key(_x_). Execute S in parallel on a soft heap \(\tilde{H}\) and an exact heap _H_. For an element \(y\in\EuScript{E}(\tilde{H})\), let \(\widetilde{key}(y)\) denote the current key of _y_ in \(\tilde{H}\). At every point in time, let _N<sub>a</sub>_ be the current rank of _a_ in _H_, and let \(\tilde{N}_a\) be the current rank of _a_ in \(\tilde{H}\). Formally, let

\(N_a:=|\{y\in\EuScript{E}(H):key(y)\le a\}|\text{and}\tilde{N}_a:=|\{y\in\EuScript{E}(\tilde{H}):\widetilde{key}(y)\le a\}|.\)

We claim that \(\tilde{N}_a\le N_a\) holds at all times. Initially, both values are equal to zero. Upon an insertion, both change by the same amount. Key corruptions can only reduce \(\tilde{N}_a\). Upon a deletion, each of the two values is decremented by 1 if and only if the respective value is strictly positive. Thus, \(\tilde{N}_a\le N_a\) is maintained.

Now suppose that \(x\notin\mathcal{R}(\varnothing,\mathcal{S})\). Consider the operation that deletes _x_ from _H_. Right after this operation, _N<sub>a</sub>_=0 since _x_ was the element with the smallest key in _H_ and all keys in _H_ are distinct. Consequently, \(\tilde{N}_a=0\), so either \(x\notin\EuScript{E}(\tilde{H})\) or _x_ is corrupted. This contradicts the fact that _x_ belongs to \(\tilde{X}\), finishing the proof.

We now use Lemma 2.2 to reduce the problem size if there are _few deletions_. Indeed, after executing S on a soft heap \(\tilde{H}\), we may add the set _U_ of uncorrupted elements in \(\tilde{H}\) to the answer (i.e., the set of remaining elements), remove the insertions of these elements from S, and recursively solve the problem for the new sequence \(\mathcal{S}'\). Since clearly \(\mathcal{D}(\varnothing,\mathcal{S})=\mathcal{D}(\varnothing,\mathcal{S}')\), we have \(\mathcal{R}(\varnothing,\mathcal{S})=\mathcal{R}(\varnothing,\mathcal{S}')\cup U\), and we have reduced the problem from S to \(\mathcal{S}'\). Note that removing the insertions corresponding to the set _U_ can be done with simple bookkeeping in linear time.

Let _n_ be the number of insertions. With the error parameter \(\varepsilon=1/4\), at most _n/_4 elements remaining in the soft heap at the end are corrupted. If the number of deletions is at most _n/_2, then at least _n/_2 elements are still present in \(\tilde{H}\) at the end of S, and at least _n/_4 of them are uncorrupted. Recall that \(n\le|\mathcal{S}|\le 2n\), so we have reduced the problem size by a constant factor. Next, we discuss how to handle the case with more than _n/_2 deletions.

### Handling many deletions.

The above algorithm works by maintaining an approximation of \(\mathcal{R}(\varnothing,\mathcal{S})\) in a soft heap. The idea for the remaining case is simple and in a sense "dual" to the first case: maintain an approximation of \(\mathcal{D}(\varnothing,\mathcal{S})\). We do so by scanning S backwards, using a max-heap instead of a min-heap. Intuitively, every `delete-min` creates a deletion "slot", while every `insert` provides a candidate for one of the currently open slots. If there are more candidates than slots, the largest<tbc>

