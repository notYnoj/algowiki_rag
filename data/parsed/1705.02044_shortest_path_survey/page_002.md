<tbc>to produce fast answers even in the presence of a large input graph. A special sub-graph, called a _spanner_, can also be created from the main graph that approximates the distances so that a shortest-path can be computed over that sub-graph.

Given the large body of literature on algorithms for computing the shortest-path, the objective of this survey is to present a breakdown of these shortest-path algorithms through an appropriate taxonomy. The taxonomy aims to help researchers, practitioners, and application developers understand how each shortest-path algorithm works and to help them decide which type or category of shortest-path algorithms to use given a specific scenario or application domain. Figure 1 illustrates the proposed taxonomy where each branch describes a specific category of shortest-path problem.

## 2 Taxonomy

As in Figure 1, the proposed taxonomy classifies the various shortest-path algorithms into multiple high- level branches.

The static branch in Figure 1 lists algorithms that operate over graphs with fixed weights for each edge. The weights can denote distance, travel time, cost, or any other weighting criteria. Given that the weights are fixed, some static algorithms perform precomputations over the graph. The algorithms<tbc>

Static
Alternative Path
Single Source
All Pairs
Replacement Path
Distance Oracle
Weighted Region
Exact
Approximate
Dynamic
Goal Directed
All-Pairs
Simple
Single Source
Advanced
Stochastic
Hierarchical
Adaptive
Highway Hierarchies
Non-Adaptive
Contraction Hierarchies
Parametric
Shortest Path
Multi-Level Graphs
Time-Dependant
Transit Node Routing
Discrete Time
Hub Labeling
Continuous Time
Highway Node Routing

Figure 1: Taxonomy of Shortest-Path Algorithms

