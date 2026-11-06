<tbc>Knop [4] made a similar observation, which led them to formulate the notion of _k-aware_ mergesorts. A stack-based mergesort is _k-aware_ if its merge conditions are based on the run lengths of the top _k_ runs in the stack and it only merges runs in the top _k_ entries of the stack. For our purposes, we can also allow merge conditions to operate on other metadata or properties of runs that can be recovered in constant time, such as their position in the array, as well as other global data, provided all of this fits in _O_(1) memory cells. We call this relaxed definition **_almost-k-aware_**. Any _k_-aware algorithm is trivially almost-_k_-aware.

These definitions suggests a very simple way to make almost-_k_-aware algorithms in-place: replace our stack _S_ with a "shallow stack" that only maintains the top _k_ runs. Of course, as runs are merged, other runs whose lengths we have forgotten enter the top _k_ entries of _S_. We must determine the length of these forgotten runs to test whether the merge policy’s invariant is still violated. In this paper, we propose two simple algorithms that efficiently do so, the walk- back algorithm and the jump-back algorithm. They are described respectively in Section 3 and Section 4. If we can efficiently implement some stack-based mergesort, S, in-place using a shallow stack, then we call S a **_shallow_** mergesort. We summarize our results and related properties of known algorithms in  1.

### 3 The Walk-Back Algorithm

In this section, we define the walk-back algorithm and show that a variety of stack-based mergesorts are **_walkable_**, i.e., applying the walk-back algorithm to them increases runtime by no more than a constant factor. The walk-back algorithm implements a shallow stack like so: whenever we must determine the length of a run for a comparison, we start at the beginning of the run above it in the stack and walk backwards. See Figure 2.

#### 3.1 The Walk-Back Procedure and Stopping Condition

We keep walking until either (1) we determine the length of the run in question or (2) we walk far enough to confirm whether the given comparison is false. We

R4
R3
R2
R1
Merge(R2, R1)
R3
R2
R1

Fig.1: A merge step according to a merge policy, P. The merged run takes the label of the higher run. Merging decreases the labels of all runs below the two merged runs.

