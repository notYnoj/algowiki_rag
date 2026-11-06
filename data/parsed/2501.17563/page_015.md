<tbc>worst-case rounding of the optimum shown in Figure 3 (for Theorem 2.2), that gives an approximation ratio of \(\frac{62}{53}\approx 1.170\). Then we explain how to find directions in which the root rounding is sub-optimal and where the directions in  3 come from.

**Theorem 2.9.** The approximation ratio of root rounding (Definition 1.6) is at least \(\frac{62}{53}\). (As shown in  3, other (numerical) examples show that it is can be even worse.)

_Proof._ Consider the case of Theorem 2.2, of weights _w_=(3,2,0,2,3,3,10) and the non-integer solution described in Figure 3. We show a set of choices that round this solution to an STT with depths-vector _D_=(4,3,2,3,4,1,0). Then its LP value is \(w\cdot D=12+6+0+6+12+3=39\), compared to the best STT whose value is 30. By Remark 1.5, the approximation ratio is \(\frac{39+\sum w_i}{30+\sum w_i}=\frac{62}{53}\approx 1.170\).

We now round step by step, for each connected component _C_ throughout the process.

1. Initially, _C_={1_,...,_7} (whole tree): since \(X_{7i}=\frac{1}{2}\) for each _i_=1_,...,_6, we can choose the root _r_=7. _C_\\{_r_} remains a single connected component.<tbc>

2. _C_={1_,...,_6}: since \(X_{6i}\ge\frac{1}{2}\) for each _i_=1_,...,_5, we can choose the root _r_=6. _C_\\{_r_} remains a single connected component, now it is a path.<tbc>

3. _C_={1_,...,_5}: while _X_<sub>3_i_</sub>=0 for _i_=1,2,4,5, choosing _r_=3 as the root satisfies the condition because \(X_{24}=X_{25}=X_{41}=X_{42}=\frac{1}{2}\). _C_\\{_r_} now has two connected components.<tbc>

4. _C_={1,2}: since \(X_{21}=\frac{1}{2}\) we can root at 2. This leaves a singleton subtree _C_\\{2}={1}.<tbc>

5. _C_={4,5}: since \(X_{45}=\frac{1}{2}\) we can root at 4. This leaves a singleton subtree _C_\\{4}={5}.

Combining all of the above yields an STT whose depths-vector (4,3,2,3,4,1,0).

We could refine root rounding by solving the LP recursively for each connected component after picking the root, instead of rounding always based on the same one-time solution. In the example of Theorem 2.9 it does help, because 7 is a root of some optimal STT with respect to _w_, and we know that when the topology has size \(n\le 6\) the LP approach is optimal. However, this refined rounding does not generally circumvent the problem, since we show next that we might pick the root sub-optimally. When this happens, the resulting STT is suboptimal even if we can improve our choices and the overall approximation ratio by constructing the subtrees better.

In the remainder of this section, we discuss how to find directions for which root rounding has a relatively large approximation ratio. First let us discuss the best-case rounding. As noted, to ensure a gap, even under the refined (iterated) root rounding, it is sufficient to ensure an empty intersection between the set of candidate roots, which we denote by _R_, and the set of roots of optimal STTs, which we denote by _O_.<sup>8</sup> It requires to solve an LP _O(n_) times instead of once, but the running time will remain polynomial.

As a first step, we can look for a primary direction for which \(O\backslash R\neq\emptyset\). Then we can variate slightly the primary direction to ensure that all the optimal STTs have a root from _O_\\_R_. This naive approach does not always work, and by checking the sets _O_ and _R_ for each primary direction, we find multiple such directions only for the topologies _U_<sub>(8,4)</sub> and _U_<sub>(8,13)</sub>. Moreover, primary directions are only special because they let us find a non-STT vertex, but they do not necessarily maximize<tbc>

<sup>8</sup>Note that if we could guarantee a rounding that shares a root with an optimal solution, the refined (iterated) root rounding would give an optimal STT.

