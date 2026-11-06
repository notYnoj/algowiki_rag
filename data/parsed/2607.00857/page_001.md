# Warm-Starting All-Pairs Shortest Paths with Predictions

**Abstract**

One of the three key hypotheses of fine-grained complexity asserts that computing All-Pairs Shortest Paths (APSP) requires cubic time, up to subpolynomial factors, in the worst case. We initiate the study of APSP in the paradigm of algorithms with predictions, also known as learning-augmented algorithms. We propose an APSP algorithm that takes as additional input a _prediction_ (e.g., given by a model learned from similar instances seen in the past) consisting of sets of vertices causing the shortest _detour_ for each pair of vertices. The algorithm runs in time \(\mathcal{O}(n^{2.83}+\eta n)\), where \(\eta\) denotes the _prediction error_ defined as the number of pairs of vertices for which, informally speaking, the prediction was not sufficient to compute and certify optimality of the shortest path length. This is already subcubic when the prediction error is (polynomially) smaller than its maximum possible values _n_<sup>2</sup>, i.e., whenever the prediction is at least slightly better than terrible.

We build on the co-nondeterministic algorithm for the Exact Triangle problem by Chan, Vassilevska Williams, and Xu (S 2023), essentially enabling this algorithm to detect mistakes in the nondeterministic certificate and recover from them.

Our result constitutes the first necessary step towards designing learning-augmented algorithms for problems with known fine-grained lower bounds conditioned on the APSP Hypothesis.

**Supplementary Material https://github.com/adampolak/warm-starting-apsp**

Funding Funded by the Italian Ministry of University and Research (MUR) under Ministerial Decree No. 18169 of 17 November 2025 – FIS 3 Call CUP: J53C25002160001

**Acknowledgements** We thank Antonios Antoniadis and Yasamin Nazari for helpful discussion.

### 1 Introduction

Given a directed edge-weighted graph _G_=(_V,E,w_), the All-Pairs Shortest Paths (APSP) problem asks to compute for each pair of vertices \(u,v\in V\) the distance from _u_ to _v_, i.e., the minimum total weight of edges on a path from _u_ to _v_. In _n_-vertex graphs, APSP can be easily solved in time O(_n_<sup>3</sup>), e.g., using the Floyd-Warshall algorithm [37, 23, 44], or, when the edge weights are non-negative, by running Dijkstra’s algorithm [18] from each vertex. The fastest known APSP algorithm [45] shaves off only a factor of \(2^{\mathcal{O}(\sqrt{logn})}\), and the APSP Hypothesis [41] asserts that the cubic running time is optimal up to subpolynomial factors. It is one of the three main hypotheses of fine-grained complexity [40], alongside the 3SUM Hypothesis and Strong Exponential Time Hypothesis (SETH).

Imagine we solve many instances of APSP that are in some sense _similar_ to each other, e.g., many snapshots of a road network taken over time with edge weights representing estimated travel times that get updated between the snapshots.

_Can we use a common structure shared by similar APSP instances in order to solve them faster?_

This question fits into the recent line of research on learning-augmented algorithms, also known as algorithms with predictions, see, e.g., [35, 32]. In particular, it is the kind

Adam Polak <sup>∗</sup>

Bocconi University, Milan, Italy

**Jonas Schmidt** <sup>∗</sup>

Bocconi University, Milan, Italy

