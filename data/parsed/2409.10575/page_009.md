where _bigM_ is a large enough number to be fixed later, |_L<sub>v</sub>_| represents the length of agent _v_’s preference list, and _b(v_)-|_M(v_)| indicates the number of unassigned positions of agent _v_.

To ensure that the evaluation scores of matchings with larger matching sizes consistently exceed those of matchings with smaller matching sizes, the parameter _bigM_ is defined as follows:

\(bigM=\big(max_{u\in U}|L_u|+max_{w\in W}|L_w|\big)\times(N-e_M)\)

where _e<sub>M</sub>_ denotes the estimated minimum size of the matching throughout the entire search process. To simplify parameter settings, we define \(e_M=c\cdot|M_{init}|\), where _c_ represents a ratio varying between 0 and 1, and _M<sub>init</sub>_ denotes the matching obtained from the random tie-breaking strategy at the beginning.

## 4.2 Refining the tie-breaking strategy

A tie-breaking strategy, denoted as _S_, converts the original preference lists _L_, which contain ties, into tie-free (i.e., strictly ordered) preference lists _L_<sup>∗</sup>. Let \(r_v^*(x)\) represent the rank of _x_ in _v_’s tie-free preference list. In the subroutine `RefineTieBreakingStrategy`, outlined in Algorithm 2, the tie-breaking strategy is updated as follows:

1. Obtain a set of candidate adjustments \(R_M^b\) via the subroutine `ObtainAdjustments` (line 3).<tbc>

2. If no adjustments are available, i.e. \(R_M^b\) is an empty set, or with a small probability _p<sub>d</sub>_, then a disruption is implemented to escape local optima. The disruption involves randomly selecting _k<sub>u</sub>_ agents from set _U_ and _k<sub>w</sub>_ agents from set _W_, and then arbitrarily breaking all ties in their respective preference lists (lines 4-11).<tbc>

3. Otherwise, if at least one adjustment is available, i.e. \(R_M^b\) is non-empty, and with a probability 1-_p<sub>d</sub>_, then an adjustment is randomly selected to refine the tie- breaking strategy. This adjustment improves a specific free agent _f_’s rank in its candidate _x_’s tie-free preference list by positioning _f_ at the highest rank among the agents who share the same rank as _f_ in _x_’s preference list, i.e., the agents in \(\phi_f(x)\) (lines 12-16).

Additionally, a set _Q<sub>a</sub>_ is maintained to record the agents whose preference lists have been altered during the refinement process. This set will subsequently be used in the BP removal process within the subroutine `ObtainStableMatching`, which is discussed in Section 4.3.

Next, we detail the process of identifying adjustments that can increase the likelihood of matching free agents and the construction of \(R_M^b\). In the subroutine `ObtainAdjustments`, as illustrated in Algorithm 3, \(R_M^b\) is generated through the following two steps:

1. Identify a set _R<sub>M</sub>_ of all potential adjustments (lines 4-11). Given a stable matching _M_, consider each free agent \(f\in F_M\). For every agent \(x\in\xi_f^M\), if the set<tbc>

