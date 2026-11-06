## 1 Introduction

In a (linear) combinatorial optimization problem, we are given a family \(\mathcal{F}\subseteq 2^U\) of _feasible subsets_ of a ground set _U_ of _n_ elements, and our goal is to find \(S^*=argmin_{S\in\mathcal{F}}\langle w,\unknown_S\rangle\). Traditionally, we are either given the weight vector _w_ explicitly, or else we are given a _value oracle_ which allows us to evaluate \(w(S):=\langle w,\unknown_S\rangle\) for any \(S\in\mathcal{F}\). In this work, we pose the question:

Which combinatorial optimization problems can we efficiently solve if we are only allowed

_pairwise comparisons between feasible solutions?_

That is, we are given access to a comparison oracle that takes two <u>feasible</u> sets \(S,T\in\mathcal{F}\), and outputs whether _w(S_) is less than/equal to/greater than _w(T_). This comparison query model is perhaps the weakest feedback model where we can hope to optimize efficiently.<sup>1</sup> As a concrete question, consider the min-cut problem in this model. Specifically:

We are given an undirected simple graph _G_=(_V,E_). In each query, we can compare any two (edge) cuts to each other. _Can we efficiently find a minimum cut in this graph?_

The min-cut problem has been intensively studied in the value-query model in recent years, leading to new insights and algorithms: can we replicate this success in the comparison-query model?

More generally, our high-level motivation for the model comes from recent interest in applications (e.g., from crowdsourcing, recommendation systems, and most recently, RLHF) which solicit feedback from users only via comparison queries. In these settings, users’ notions of quality/utility is often difficult to quantify, or noisy, or only partially consistent, and hence they are asked to give _relative preferences_--choosing one alternative over another--rather than assigning precise numerical values. While these practical settings do not seek to solve precise optimization problems (like min-cuts or spanning trees), they do motivate the particularly clean query model we investigate in this work.

### 1.1 Our Results

#### 1.1.1 Query Complexity

We first focus on the _query complexity_ of the problem: how many comparison queries give us enough information to solve the problem, without worrying about computation? Recall that we can only query pairs of feasible solutions, so it is completely unclear whether we can identify the optimal solution using much less than |F| queries.

For this query complexity question, we show a surprisingly general _positive_ result: _we can optimize over <u>allBooleanfamilies</u> with a small number of queries!_

**Theorem 1.1** (Boolean Linear Optimization)**.** _For any family_ \(\mathcal{F}\subseteq 2^U\) _and unknown weight function_ \(w^*:U\rightarrow\mathbb{R}\)_, we can solve_ \(argmin_{S\in\mathcal{F}}\sum_{e\in S}w_e^*\) _using_ \(O(nlog^2n\cdot log|\mathcal{F}|)=\widetilde{O}(n^2)\) _comparison queries, where n_=|_U|._

We find Theorem 1.1 remarkable: it shows that the number of comparison queries required to find the optimal solution is only \(\widetilde{O}(n^2)\), _regardless of the complexity of_ the set system F. Indeed, we<tbc>

<sup>1</sup>One can consider more general objective functions, such as XOS, submodular, subadditive, etc., where the function \(w(\cdot)\) is typically exponential-sized, and hence we can only access it via value or demand oracles. Our question--what can you do with just comparison queries--is interesting in these settings as well, but we focus on linear optimization for now.

