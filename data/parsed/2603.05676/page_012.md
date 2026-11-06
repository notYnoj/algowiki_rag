This lemma is proved by the introduction of two new encoding schemes which we call **_pivot-encoding_**, which works when there are a sufficient number of distinct elements in the run, and **_marker-encoding_**, which works in general. Under either scheme, we encode the size of a run within the last \(\lambda+1\) elements of the run. We discuss these encoding schemes in Section 5. See Figure 6.

Recall that we have already moved all short runs to the end of the array. Using Lemma 6, we can implement the almost-_k_-aware algorithm, S, in-place on the remaining long runs using our jump-back algorithm with only two changes.

1. Whenever a new run, _q_, is added and the bottommost run, _s_, in the shallow stack no longer fits, we _encode s_’s size using the algorithm of Lemma 6. This step takes \(O(\lambda)\) time, and can be charged to the run, _q_, that was just added to the stack, since its size must have been at least \(3\lambda+1\).

2. Symmetrically, whenever a run is merged and the shallow stack is no longer full, we add the run deeper in the array to the shallow stack by _decoding_ its size and by _reversing_ the encoding such that the original run is restored. This step also takes \(O(\lambda)\) time, and can be charged to the merge operation.

Using these two changes, we can maintain all the information of our shallow stack efficiently, without asymptotically increasing the running time of our algorithm, S. All that is left is to sort all the remaining _short_ runs.

All short runs, of size at most \(3\lambda\), were initially moved to the end of the array. Let us denote this portion of the array as \(A'\). By the definition of the Shannon entropy of an array, \(n\mathcal{H}(A)=\sum_{i=1}^{\rho(A)}r_ilog(n/r_i)\), and we see that

\(\sum_{i=1}^{\rho(A^\prime)}r_ilog(n/r_i)\ge\sum_{i=1}^{\rho(A^\prime)}r_ilog(n/3\lambda).\)

But \(\lambda=\lceil logn\rceil+1\); hence, if we let \(m=\sum_{i=1}^{\rho(A^\prime)}r_i\), then the sum of their entropy is \(\Omega(mlogn)\). As a result, the cost of sorting all runs of size at most \(3\lambda\) in time _O(mlogm_) is "paid" for by their contribution to the entropy of the original array. We spend an additional _O(n_) time moving all such runs to the end of the array. (see Section D). As noted above, the time to sort the long runs in _A_ is asymptotically the same as S. Thus, we have the following:

\(\lambda+1\lambda+1\lambda+1\)<br>
\(\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\)

Fig. 6: We encode run lengths within the last \(\lambda+1\) elements of each run, indicated with shading, allowing us to compute the run’s length in _O_(log_n_) time. This eliminates the need for walking back via the walk-back algorithm albeit at the loss of stability.

