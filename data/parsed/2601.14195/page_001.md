# A Minimax Perspective on Almost-Stable Matchings<sup>∗</sup>

**Abstract**

Stability is crucial in matching markets, yet in many real-world settings - from hospital residency allocations to roommate assignments - full stability is either impossible to achieve or can come at the cost of leaving many agents unmatched. When stability cannot be achieved, algorithmicists and market designers face a critical question: how should instability be measured and distributed among participants? Existing approaches to "almost-stable" matchings focus on aggregate measures, minimising either the number of blocking pairs or the count of agents involved in blocking pairs. However, such aggregate objectives can result in concentrated instability on a few individual agents, raising concerns about fairness and incentives to deviate. We introduce a fairness-oriented approach to approximate stability based on the minimax principle: we seek matchings that minimise the maximum number of blocking pairs any agent finds themselves in. Equivalently, we minimise the maximum number of agents that anyone has justified envy towards. This distributional objective protects the worst-off agents from bearing a disproportionate amount of instability.

We characterise the computational complexity of this notion across fundamental matching settings. Surprisingly, even very modest guarantees with respect to the distribution of instability prove computationally intractable: we show that it is NP-complete to decide whether a matching exists in which no agent is in more than one blocking pair, even when preference lists have constant-bounded length. This hardness applies to both Stable Roommates and maximum cardinality Stable Marriage problems. On the positive side, we provide polynomial-time algorithms when agents rank at most two others, and present approximation algorithms and integer programs for general settings. Our results map the algorithmic landscape and reveal fundamental trade-offs between distributional guarantees on justified envy and computational feasibility in matching market design.

**Keywords** Stable Marriage, Stable Roommates, Almost-Stable Matching, Fairness, Approximation Algorithm, Computational Complexity

## 1 Introduction

### 1.1 Motivation

Stability in matching markets ensures that no pair of agents would prefer to deviate from their assigned matches by becoming assigned to one another instead. This property underpins trusted real-world mechanisms from medical residency allocations to school and campus housing assignments. Yet, in many real-world settings, stability is either impossible to achieve or comes at a significant trade-off with respect to the number of matched agents. Thus, a central question for economists and computer scientists alike is whether instability can be eliminated, and how it should be measured and distributed among participants if it cannot be avoided.

<sup>∗</sup>The statements of Theorems 4.1, 4.2, 4.4, 5.1 and 5.2 appeared in Section 2 of "Minimax and Preferential Almost-Stable Matchings" in the Proceedings of AAMAS 2026 [26].

Frederik Glitzner<br> and David Manlove<br> School of Computing Science, University of Glasgow, Glasgow G12 8QQ, UK<br> `f.glitzner.1@research.gla.ac.uk, david.manlove@glasgow.ac.uk`

