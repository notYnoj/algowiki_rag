# FPT-Approximability of Stable Matching Problems

**Abstract**

We study parameterized approximability of three optimization problems related to stable matching: (1) Min-BP-SMI: Given a stable marriage instance and a number _k_, find a size-at-least-_k_ matching that minimizes the number \(\beta\) of blocking pairs; (2) Min-BP-SRI: Given a stable roommates instance, find a matching that minimizes the number \(\beta\) of blocking pairs; (3) Max-SMTI: Given a stable marriage instance with preferences containing ties, find a maximum-size stable matching.

The first two problems are known to be NP-hard to approximate to any constant factor and W[1]- hard with respect to \(\beta\), making the existence of an EPTAS or FPT-algorithms unlikely. We show that they are W[1]-hard with respect to \(\beta\) to approximate to any function of \(\beta\). This means that unless FPT=W[1], there is no FPT-algorithm with respect to \(\beta\) that can decide whether a given instance has a matching with at most \(\beta\) or at least \(F(\beta)\) blocking pairs for every function _F_ depending only on \(\beta\). The last problem (Max-SMTI) is known to be NP-hard to approximate to factor-\(\frac{29}{33}\) and W[1]-hard with respect to the number of ties. We complement this and present an FPT-approximation scheme for the parameter "number of agents with ties".

### 1 Introduction

Stable matchings play a fundamental role in various applications ranging from job markets (e.g., the National Resident Matching Program), over education (e.g., school choice or college admission), to health (e.g., kidney exchange programs). The general idea is to match the agents into pairs so no two agents can form a blocking pair. A blocking pair is a pair of two agents that are not matched with each other but prefer each other over the status under the matching.

In the classical Stable Marriage (SM) problem introduced by Gale and Shapley [11], we are given two disjoint sets of agents, each having a complete and strict preference list (aka. ranking) over the agents of the other set, and we aim to match every agent from one set to an agent of the other set so that no blocking pairs are induced. Gale and Shapley show that every instance of the SM problem admits a stable matching and provide a linear-time algorithm to find one.

SM has many relevant extensions. First, the preference lists of the agents may be _incomplete_, allowing them to express unacceptability towards other agents. This results in the setting of Stable Marriage with Incomplete Preferences (SMI). A stable matching still always exists for each SMI instance, albeit not every agent is matched; the same set of agents are matched in all stable matchings though. A key challenge in SMI is the trade-off between the size and stability: Requiring more agents to be matched will induce blocking pairs, destroying stability [26, Rural Hospital Theorem]. This motivates the problem of Minimum Blocking Pairs SMI which aims to find a matching of size at least a given number _k_ such that the number of blocking pairs is minimized. Prior work has considered both exact and approximation algorithms [3, 14, 12], showing that the problem remains computationally challenging. For instance, Min- BP-SMI is already NP-hard when the preference lists are of length at most three [3]. Moreover, it is NP-hard to approximate to some constant factor [3, 14].

Another extension of SM is to have just one set of agents, allowing each agent to rank any other agent. In this case, we obtain the setting of Stable Roommates (SR). Unlike in SM and SMI, stable matchings are not guaranteed to exist. Irving [17] designs a linear-time algorithm to decide whether a given

Jiehua Chen<sup>1</sup>, Sanjukta Roy<sup>2</sup>, and Sofia Simola<sup>1</sup>

<sup>1</sup>TU Wien, Austria

<sup>2</sup>Indian Statistical Institute, India

arXiv:2508.10129v1 [cs.GT] 13 Aug 2025

