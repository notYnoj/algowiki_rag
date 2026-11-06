<tbc>experiments suggest that this does not have a significant impact on the running time of the algorithms. All our code will be made available online.

### E.2 Results

In Figure 12, we compare the algorithms on the TimSort counterexample input as described in Section B and Section B.1. This input has a constant Shannon entropy, so any algorithm that is instance-optimal with respect to Shannon entropy should run in linear time, and after scaling the running times by _n_, should appear constant. Indeed, we see that all the standard stack-based mergesorts take advantage of the natural ordering of the input and appear constant, while C++’s **std::sort** function (using introsort) and QuickXsort, which are not instance-optimal, perform poorly. Reassuringly, after applying our simple walk-back algorithm, the in-place versions of the _walkable_ mergesorts (PowerSort and _c_-Adaptive ShiversSort) appear to remain input-sensitive like their non-in-place counterparts. In contrast, the in-place version of TimSort, which as we proved in Section B is not walkable, performs poorly.

27
26
Running Time (T(n)//n logn)
25
24
13
22
25
29
213
217
221
225
229
Input Size (n)
StdSort
PowerSort
WalkBackCAAdaptiveShiversSort<3>
WalkBackTimSort<4>
CAAdaptiveShiversSort
TimSort
WalkBackPowerSort<3>
Hybrid QuickMergeSort

Fig.13: A comparison of normalized running times on uniformly random inputs. Since uniformly random inputs are expected to have a Shannon entropy of \(\Theta(logn)\), we scaled the running times by _n_log_n_, such that any algorithm that is optimal with respect to Shannon entropy should appear constant. As expected, **std::sort** (StdSort) and Hybrid QMS are optimized well for these inputs. Reassuringly, not only do all the stack-based mergesorts appear constant, but also all our in-place versions of the _walkable_ mergesorts appear constant. The only mergesort which does not appear constant is the in-place version of TimSort, which is not walkable, as shown in Section B.

