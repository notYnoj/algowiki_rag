Balancing Weights, Directed Sparsification, and Augmenting Paths

**Abstract**

We present a randomized augmenting paths-based algorithm to compute the maximum flow in a directed, uncapacitated graph in almost _m+nF_ time, matching the algorithm of Karger and Levine for undirected graphs (SICOMP 2015). Combined with an initial \(\sqrt{n}\) rounds of blocking flow to reduce the value of _F_, we obtain a maximum flow algorithm with running time _mn_<sup>1/2+_o_(1)</sup>. For combinatorial, augmenting paths-based algorithms, this is the first improvement over Dinic’s algorithm for moderately sparse graphs.

To obtain our algorithm, we introduce a new technique to re-weight the edges of a strongly connected directed graph so that each cut is approximately balanced: the total weight of edges in one direction is within a constant factor of the total weight in the other direction. We then adapt Karger and Levine’s technique of sampling edges from the newly weighted residual graph, ensuring that an augmenting path exists in the sampled graph with high probability. One technical difficulty is that our balancing weights have to be dynamically maintained upon changes to the residual graph. Surprisingly, we can black box the dynamic data structure from the recent interior point method-based flow algorithm of van den Brand et al. (FOCS 2024).

## 1 Introduction

In the (uncapacitated) maximum flow problem, we are given a directed graph and two vertices _s_ and _t_, and the goal is to find the maximum number of edge-disjoint paths from _s_ to _t_. It is one of the oldest problems in combinatorial optimization [Dan51], and many influential techniques have been developed to tackle the problem, including augmenting paths [FF56], blocking flows [Din70], push-relabel [GT88], and random sampling [KL15]. More recently, techniques based on continuous optimization have become widely successful, culminating in the first almost-linear time algorithm for maximum flow and its generalizations [CKL<sup>+</sup>25]. However, it remains an open question whether a more traditional approach based on augmenting paths can match this recent breakthrough. Two very recent lines of work have obtained almost quadratic-time algorithms for maximum flow [BBST24, BBL<sup>+</sup>25] and bipartite matching [CK24a, CK24b], showing that combinatorial techniques still have room for future development.

In this work, we present a new approach based on sampling edges from an appropriately weighted residual graph. Our main result is the following:

**Theorem 1.** _There is a randomized, augmenting paths-based algorithm that computes the maximum flow on a directed, uncapacitated graph in time_ \((m+nF)\cdot n^{o(1)}\)_, where F is the value of the maximum flow._

<sup>∗</sup>Carnegie Mellon University. `jmli@cs.cmu.edu`

Jason Li<sup>∗</sup>

April 17, 2026

arXiv:2604.1463v1 [cs.DS] 16 Apr 2026

