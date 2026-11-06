## Conclusion.

Lemmas 11-13 establish correctness of the 2-lane structure. Together with Lemmas 9-10, they justify the expansion-based accounting used in Theorem 6. The CNF policy is target-independent and scheduler-agnostic, and, combined with compensatory merging, preserves both decision and construction correctness.

## Complexity and Target Independence (Summary)

The Controlled Aliasing transform is purely structural (fixed alias pairs per half), independent of the target _t_ and any randomness. Under CNF, each base pattern contributes to at most three expanded states, yielding the worst-case factor 3/4 per half and the _O_<sup>∗</sup>(2<sup>_n/_2-log<sub>2</sub>(4/3)</sup>) bound when integrated into the interleaved double-meet-in-the-middle solver.

