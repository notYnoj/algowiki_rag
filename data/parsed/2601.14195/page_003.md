<tbc>_cost_. Suppose that agents rank a large number of other agents or positions and that rankings are private information. Then, following the release of the matching by the central matchmaker, agents may explore possible profitable deviations by contacting each agent they prefer to their match, which may come at a cost (e.g., the time it takes to contact other agents). However, when agents are guaranteed to be in only a few blocking pairs, or none, then the exploration cost to find a blocking pair can be high.<sup>1</sup>

In this paper, we continue research on algorithmic and complexity results related to decision and optimisation problems concerned with matchings and maximum-cardinality matchings that are "as stable as possible", which are also referred to as "almost-stable" matchings [1, 10], and resolve open questions on the complexity of such problems [12, 13, 29].

## 1.2 Our Contributions

Given the practical importance of matchings that minimise instability while maximising size, strong intractability results involving the computation of such matchings are discouraging. We therefore aim to understand the tractability frontier through a different lens. Rather than aggregate measures of instability, we adopt the classical principle of _minimax fairness_: protecting the worst-off individual from excessive injustice, and simultaneously decreasing individuals’ incentives to deviate and the risk of unravelling. Specifically, our interpretation of _minimax_ is to minimise the maximum number of blocking pairs that any agent finds themselves in, which is a new notion of almost-stability that we study in this paper. Equivalently, we minimise the maximum number of agents that any single agent has justified envy towards (under non- wastefulness). This distributional objective accepts that full stability may not be achievable, but ensures that no single agent bears a disproportionate burden of instability. Our approach aligns with fairness principles in social choice that prioritise the leximin allocation of bad outcomes, rather than maximising the utilitarian welfare.

We characterise the computational complexity of this fairness-constrained notion of almost- stability with surprisingly strong intractability results. Specifically, we show that even deciding whether a matching (respectively maximum-cardinality matching) exists in which no agent is in more than one blocking pair is NP-complete for sri (smi), even when preference lists are of short, constant-bounded length. We also give additional strong intractability results and<tbc>

<sup>1</sup>We purposefully keep this statement vague, as there are multiple factors at play here. For example, receiving a high-ranking partner leaves few better partners to block with. However, none of the discussed almost-stability criteria provide any inherent guarantees with regard to the average or maximum ranks of partners.

2
1
2
1
1
1
1
3
1
3
1
2
2
2
2
3
1
2
3
1
1
2
1
2
2
2
2
2
1
1
1
1

Figure 1: Two different perfect matchings with the same number of blocking pairs but different numbers of blocking agents and different levels of instability concentration.

