In Figure 13, we compare the algorithms on uniformly random inputs, which are expected to have a Shannon entropy of \(\Theta(logn)\), so we scale the running times by _n_log_n_, such that any _O(n_log_n_) algorithm should appear constant. And indeed, all the algorithms (notably except the version of TimSort implemented with the walk-back algorithm) appear constant, as expected. The fact that walk-back TimSort appears to perform worse than _O(n_log_n_) on such inputs is interesting.

## F Supplemental Experiments

### F.1 Impact of Different Stack Sizes

In the previous section, we gave each in-place variant their minimal stack size required, _k_, which for PowerSort and _c_-Adaptive ShiversSort is 3, and for

1.7
1.6
1.6
1.5
1.5
1.4
1.4
Running Time Degradation
1.3
Running Time Degradation
1.3
1.2
1.2
1.1
1.1
1.0
1.0
20
20
215
217
217
215
215
210
20
20
215
217
217
215
210
Input Size (n)
Input Size (n)
WalkBackActiveShiversSort<3>
WalkBackActiveShiversSort<10>
WalkBackPowerSort<3>
WalkBackPowerSort<10>
WalkBackActiveShiversSort<5>
CAdaptiveShiversSort
WalkBackPowerSort<5>
PowerSort
20
15
Running Time Degradation
10
5
0
20
20
215
217
217
215
215
210
Input Size (n)
WalkBackTimSort<4>
WalkBackTimSort<10>
WalkBackTimSort<5>
TimSort

Fig.14: A comparison of the different in-place versions of each algorithm against their standard version on uniformly random inputs. Each algorithm is measured with respect to the standard version, which is normalized to 1. While the in-place versions of _c_-Adaptive ShiversSort and PowerSort are within a small constant factor of the standard version, the in-place versions of TimSort clearly perform asymptotically worse.

