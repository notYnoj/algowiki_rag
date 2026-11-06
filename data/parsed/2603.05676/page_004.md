## 2 Preliminaries

Let us begin with some preliminaries for stack-based mergesort algorithms. Let _A_ be an input array of _n_ elements. We define a run as either a non-decreasing or strictly decreasing subsequence of elements in _A_. All decreasing runs can easily be flipped in-place to be increasing runs in an initial linear-time sweep of _A_ without affecting stability, so, without loss of generality, we only consider non-decreasing runs.

We can separate all stack-based mergesort algorithms into two phases. First is the **_main loop_**, in which we sweep _A_ from left-to-right, pushing new runs into our stack. Each algorithm defines and is distinguished by a merge policy, P. Whenever we push a new run into our stack and P’s invariant is violated, we perform a sequence of merges of adjacent runs in our stack determined by P until the invariant is restored. We call this a **_merge sequence_**. After processing all runs in _A_, the main loop exits and we perform a **_collapse_** phase on the remaining runs in the stack, where we repeatedly merge the top two runs in the stack until only one run remains, our final sorted list. We use the convention that runs closer to the top of the stack are labeled with lower indices, such that the run at the top of the stack takes label _R_<sub>1</sub>. We use _r<sub>i</sub>_ to denote the length of run _R<sub>i</sub>_, i.e., _r<sub>i</sub>_=|_R<sub>i</sub>_|. We present pseudocode of a generic stack-based mergesort in Algorithm 1. See Figure 1.

**Algorithm 1** A Generic Stack-Based Mergesort Algorithm with Merge Policy, P

1: **Input:** array _A_ of size _n_. Merge policy P.<br>
2: **Output:** sorted array \(A'\).<br>
3: \(\mathcal{R}\leftarrow\) run decomposition of _A_<br>
4: \(S\leftarrow\emptyset\triangleright\) the stack of runs<br>
5: while R is not empty do \(\triangleright\) main loop<br>
6: Push next run from R onto S<br>
7: while S violates P’s invariant do \(\triangleright\) algorithm-specific merge policy<br>
8: Merge a pair of adjacent runs in S according to P<br>
9: while |S|\>1 do \(\triangleright\) collapse phase<br>
10: Pop R<sub>1</sub> and R<sub>2</sub> from S and push Merge(R<sub>1</sub>,R<sub>2</sub>) onto S<br>
11: return pop(S)

For ease of expression, we may still use the term "stack" when referring to a given stack-based mergesort, even though our algorithms do not explicitly maintain all of _S_. We review the merge policies of specific stack-based mergesorts as needed throughout the paper.

### 2.1 Shallow Mergesorts

Interestingly, most instance-optimal mergesorts have merge policies that only consider a constant number, _k_, of runs from the top of the stack. Buss and

