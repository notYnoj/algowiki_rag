# Tight Energy Lower Bounds for Distributed Graph Algorithms

**Abstract**

There has been a significant recent interest in designing distributed algorithms in the SLEEPING model that minimize the _energy (a.k.a awake)_ complexity, which measures the number of rounds a node is _awake_ during the algorithm. A node spends non-trivial resources (messages, energy, etc.) only when it is awake and not while _sleeping_. Energy complexity has been studied for various fundamental problems with respect to minimizing the _maximum (worst-case)_ or the _average_ number of rounds a node is awake.

It has been shown that the energy complexities of several fundamental problems such as leader election (LE), broadcast, Minimum Spanning Tree (MST), Maximal Independent Set (MIS) is _exponentially_ smaller compared to their respective best-possible round complexities in the standard CONGEST model (where nodes can only send messages of small size). This raises a fundamental question of whether such significant energy gains are possible for many other fundamental problems.

Our main contribution is a general and powerful technique for showing energy lower bounds using information theory. It gives almost a "plug-in" way to show energy lower bounds for various problems in the standard CONGEST model. Our information-theoretic technique allows us to leverage known lower bounds on _communication complexity_ to obtain new, _almost optimal_ (up to logarithmic factors) _polynomial (in n)_ lower bounds on energy complexity -- for _both_ worst-case and average-case -- for fundamental graph problems such as triangle enumeration, All-Pairs Shortest Paths (APSP), diameter computation, minimum weight cycle, Maximum Independent Set (MaxIS), Minimum Dominating Set (MinDS), Minimum Vertex Cover (MinVC). The energy lower bounds of these problems _match_ their respective round lower bounds, implying that one _cannot_ obtain any significant gains in energy complexity.

**2012 ACM Subject Classification** Theory of computation \(\rightarrow\) Distributed algorithms

**Keywords and phrases** distributed graph algorithm, energy complexity, information-theoretic lower bound

**Digital Object Identifier** 10.4230/LIPIcs.DISC.2026.13

Funding Gopal Pandurangan was supported in part by Army Research Office (ARO) grant W911NF- 231-0191 and National Science Foundation (NSF) grant CCF-2402837. Peter Robinson was supported in part by National Science Foundation (NSF) Grant No. CCF-2402836.

**Fabien Dufoulon**<br> Lancaster University, UK<br> **Gopal Pandurangan**<br> University of Houston, Texas, USA<br> **Peter Robinson**<br> Augusta University, Augusta, Georgia, USA

arXiv:2608.18992v1 [cs.DC] 19 Aug 2026

