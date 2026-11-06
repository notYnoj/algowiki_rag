<tbc>TimSort is 4. We now compare each in-place algorithm as its stack size increases from _k_ to 5, to 10, against the standard version (which can be thought of as having stacks of size up to \(\Theta(logn)\)).

As expected, all the in-place versions of our stack-based natural mergesorts perform better as their stack size increases, performing the best when the stack size is not bounded. The walkable mergesorts in particular perform very well, performing within a very small constant factor of the standard version. Even for the smallest stack size of just 3, the in-place versions of PowerSort and _c_- Adaptive ShiversSort perform within a factor of 1.7 and 1.6, respectively, of the standard version. This further confirms that not only is our simple walk-back algorithm effective, but that it is likely benefiting from being very cache-friendly. In contrast, despite the cache-friendliness of our walk-back algorithm, the in- place version of TimSort clearly does not keep up with the standard version. Even when allowed to store the top 10 runs, it is only able to keep up with the standard version for so long before diverging. See Figure 14. This directly aligns with our results from Section B.

### F.2 Stack Height Variability

In Figure 15, we plot TimSort’s stack height (_h_) during each iteration of the main loop, right after a new run is pushed onto the stack _S_ for arrays of size _n_=2<sup>20</sup> for both our bad TimSort example (left) and uniformly random inputs (right), and compare it to the stack size of the in-place version of _c_-Adaptive ShiversSort. It is clear to see from both plots how TimSort’s stack size often significantly fluctuates in hard-to-predict ways, while the in-place version of _c_-Adaptive ShiversSort has a very consistent stack size, bounded by 3. These simple figures demonstrate the predictability of our in-place versions, which may lead to their implementations being less error-prone.

20.0
TimSort
12
17.5
10
15.0
Stack Height (h)
8
Stack Height (h)
12.5
6
10.0
7.5
4
5.0
2
TimSort
2.5
WalkBackAdaptiveShiversSort<3>
0
200
600
600
800
1000
1200
1400
0
10000
20000
30000
400000
Main Loop Iteration
Main Loop Iteration

Fig.15: Here we track TimSort’s stack height (_h_) during each iteration of the main loop, right after a new run is pushed onto the stack _S_ for arrays of size _n_=2<sup>20</sup>. On the left, we use our TimSort counterexample input as described in Section B while on the right we use uniformly random inputs.

