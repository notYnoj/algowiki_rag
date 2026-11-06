# A Survey of Shortest-Path Algorithms

**Abstract**

A shortest-path algorithm finds a path containing the minimal cost between two vertices in a graph. A plethora of shortest-path algorithms is studied in the literature that span across multiple disciplines. This paper presents a survey of shortest-path algorithms based on a taxonomy that is introduced in the paper. One dimension of this taxonomy is the various flavors of the shortest-path problem. There is no one general algorithm that is capable of solving all variants of the shortest-path problem due to the space and time complexities associated with each algorithm. Other important dimensions of the taxonomy include whether the shortest-path algorithm operates over a static or a dynamic graph, whether the shortest-path algorithm produces exact or approximate answers, and whether the objective of the shortest-path algorithm is to achieve time-dependence or is to only be goal directed. This survey studies and classifies shortest-path algorithms according to the proposed taxonomy. The survey also presents the challenges and proposed solutions associated with each category in the taxonomy.

### 1 Introduction

The shortest-path problem is one of the well-studied topics in computer science, specifically in graph theory. An optimal shortest-path is one with the minimum length criteria from a source to a destination. There has been a surge of research in shortest-path algorithms due to the problem’s numerous and diverse applications. These applications include network routing protocols, route planning, traffic control, path finding in social networks, computer games, and transportation systems, to count a few.

There are various graph types that shortest-path algorithms consider. A _general graph_ is a mathematical object consisting of vertices and edges. An _aspatial graph_ contains vertices where their positions are not interpreted as locations in space. On the other hand, a _spatial graph_ contains vertices that have locations through the edge’s end-points. A _planar graph_ is plotted in two dimensions with no edges crossing and with continuous edges that need not be straight.

There are also various settings in which a shortest-path can be identified. For example, the graph can be _static_, where the vertices and the edges do not change over time. In contrast, a graph can be _dynamic_, where vertices and edges can be introduced, updated or deleted over time. The graph contains either _directed_ or _undirected_ edges. The weights over the edges can either be _negative_ or _non-negative_ weights. The values can be real or integer numbers. This relies on the type of problem being issued.

The majority of shortest-path algorithms fall into two broad categories. The first category is _single- source shortest-path_ (SSSP), where the objective is to find the shortest-paths from a single-source vertex to all other vertices. The second category is _all-pairs shortest-path_ (APSP), where the objective is to find the shortest-paths between all pairs of vertices in a graph. The computation of shortest-path can generate either _exact_ or _approximate_ solutions. The choice of which algorithm to use depends on the characteristics of the graph and the required application. For example, approximate shortest-path algorithms objective is<tbc>

Amgad Madkour<sup>1</sup>, Walid G. Aref<sup>1</sup>, Faizan Ur Rehman<sup>2</sup>, Mohamed Abdur Rahman<sup>2</sup>, Saleh Basalamah<sup>2</sup>

<sup>1</sup> _Purdue University, West Lafayette, USA_

<sup>2</sup> _Umm Al-Qura University, Makkah, KSA_

May 8, 2017

