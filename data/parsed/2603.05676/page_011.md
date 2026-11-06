# Entropy-Sensitive Strictly In-Place Sorting

11

We have shown that, over all merges, the walk-back cost is bounded by _O(m+n_). We conclude with the following.

**Theorem 1.** _PowerSort is walkable._

**Corollary 1.** _We can implement PowerSort with the walk-back algorithm to produce an in-place, stable sorting algorithm with running time_ \(\Theta(n(1+\mathcal{H}(A)))\).

_Proof._ Follows from properties of PowerSort, stable in-place merge algorithms, and the walk-back algorithm. \(\sqcap\sqcup\)

### 4 The Jump-Back Algorithm

In this section, we describe our jump-back algorithm, which is a general method for implementing all the known stack-based natural mergesort algorithms to be in-place without a stack, albeit while sacrificing stability. The only assumption required is that a stack-based mergesort algorithm, S, be almost-_k_-aware. Importantly, if the running time of S is _O(n_(1+H(_A_))), then the running time of our in-place jump-back implementation of S will also run in time _O(n_(1+H(_A_))).

Suppose we are given an input array, _A_, of size _n_, and let \(\lambda=\lceil logn\rceil+1\) (\(\lambda\) is a parameter we that we use throughout our jump-back algorithm). We begin by moving the elements in **_short_** runs, those of size at most \(3\lambda\), to the end of _A_. We then sort them via a standard in-place mergesort algorithm; e.g., see \[6-10,15\]. Our method for performing this move in-place can be done in linear time using a partitioning algorithm described in Section D. See Figure 5.

We then apply the given stack-based natural mergesort algorithm S to the remaining, **_long_**, runs, with one change--rather than using a complete stack to store run sizes, as in the original way S was defined, we use a shallow stack of size _k_ and we use bit-encoding to encode the size of each run _in the run itself_.

**Lemma 6.** _The size of any **long** run can be encoded in the run itself using a reversible in-place encoding scheme that can be encoded, decoded, and reversed in_ \(O(\lambda)=O(logn)\) _time._

m

Fig.5: The result of performing partitioning to move all short runs to the end of the array. All runs to the left of the gray block are of size \(>3\lambda\). The elements in the gray block belonged to runs of size \(\le 3\lambda\). Their ordering may not be preserved.

