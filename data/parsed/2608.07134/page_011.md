**Lemma 3.2** (Selectable heap \[SZ22\])**.** _There is a deterministic heap that supports_ `insert` _and_ `find-min` _operations in constant amortized time and can delete and return the_ \(\ell\) _smallest elements from the heap in_ \(\mathcal{O}(\ell log\frac{m}{\ell})\) _amortized time for an arbitrary_ \(\ell\le m\)_. Here m denotes the current size of the heap._

As will be clear from the proof below, sync heaps can be seen as a generalization of selectable heaps: while selectable heaps allow multiple deletions to be processed in one batch, sync heaps allow batching an arbitrary sequence of interleaved insertions and deletions in the same time complexity.<sup>8</sup>

**Proof of Theorem 3.1.** Maintain a selectable heap \(\hat{H}\), initially empty. Between consecutive observations, we do not execute `insert` and silent `delete-min` operations on \(\hat{H}\) explicitly but rather buffer them and process them in a batch when the next observation occurs. (To simplify presentation, we regard initialization as an initial dummy observation.) Thus, throughout the execution, \(\hat{H}\) represents the state of the heap at the last observation.

Suppose an observation occurs, and let S be the buffered sequence of operations since the last observation. Let \(X:=\EuScript{E}(\hat{H})\) be the state at the previous observation. First, in O(|S|) time we remove from S all deletions that would be unsuccessful if S were executed from state _X_. Let \(\delta\) be the number of deletions that remain. By construction, all of them are successful when S is executed from _X_.

Now run the heap evaluation algorithm of Theorem 1.1 on S to compute \(\mathcal{D}(\varnothing,\mathcal{S})\) and \(\mathcal{R}(\varnothing,\mathcal{S})\). As we show later, the elements deleted when S is executed from _X_ are precisely the \(\delta\) smallest elements of \(X\cup\mathcal{D}(\varnothing,\mathcal{S})\). Accordingly, to synchronize \(\hat{H}\), we perform three steps: (1) insert all elements of \(\mathcal{D}(\varnothing,\mathcal{S})\) into \(\hat{H}\); (2) delete the \(\delta\) smallest elements from \(\hat{H}\) (denote the returned set by \(\Delta\)); (3) insert all elements of \(\mathcal{R}(\varnothing,\mathcal{S})\) into \(\hat{H}\). The second step is executed using the selectable heap’s batch-deletion operations.

After synchronization, if the current observation is a `find-min`, simply query \(\hat{H}\) for the minimum element. If instead the current observation is a `reveal-deletions`, return the union of all computed sets \(\Delta\) since the last `reveal-deletions` operation.

## Correctness.

For the analysis, consider an exact heap _H<sup>⋆</sup>_ that executes every modification immediately rather than buffering it until the next observation. We prove by induction that after every observation, \(\EuScript{E}(\hat{H})=\EuScript{E}(H^\star)\). At initialization, the claim is trivial. For the inductive step, assume that \(X=\EuScript{E}(\hat{H})\) is the state of _H<sup>⋆</sup>_ immediately after the previous observation. Since the preprocessing removed all unsuccessful deletions, all remaining \(\delta\) deletions in S succeed when executed from _X_, and hence \(|\mathcal{D}(X,\mathcal{S})|=\delta\).

It remains to prove the key fact used in the synchronization step: \(\Delta=\mathcal{D}(X,\mathcal{S})\). Let S_<sub>X</sub>_ be a sequence of operations obtained by prepending insertions of all elements of _X_ to S. Executing S_<sub>X</sub>_ from an empty heap is equivalent to executing S from _X_, so \(\mathcal{D}(\varnothing,\mathcal{S}_X)=\mathcal{D}(X,\mathcal{S})\).

Consider an execution of `ReverseHeapEval` (Algorithm 1) on S_<sub>X</sub>_ and denote its internal max- heap by _M_. By Lemma 2.3, the final state of _M_ is \(\mathcal{D}(\varnothing,\mathcal{S}_X)=\mathcal{D}(X,\mathcal{S})\) and therefore has size \(\delta\). Now consider how this run proceeds. After processing the suffix S of S_<sub>X</sub>_, we have \(\EuScript{E}(M)=\mathcal{D}(\varnothing,\mathcal{S})\) by Lemma 2.3, and the deletion-slot counter is equal to \(\delta\).

The algorithm then processes the prepended insertions of elements of _X_. Each element of _X_ is inserted into _M_, and whenever the number of elements in _M_ exceeds \(\delta\), the maximum element is removed from _M_. Thus, after processing all elements of _X_, the heap _M_ contains the \(\delta\) smallest<tbc>

<sup>8</sup> This is true for our formulation of selectable heaps, but it is worth noting that Sandlund and Zhang’s data structure \[SZ22\] also allows `decrease-key` operations, which we do not support.

