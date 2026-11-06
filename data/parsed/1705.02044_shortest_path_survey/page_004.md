<tbc>a time-dependent network. In essence, they investigate which networks can existing techniques be adopted to. Bast [11] illustrates speed-up techniques for fast routing between road networks and transportation networks. Bast’s survey argues that the algorithms for both networks are different and require specialized speed-up techniques for each. Also, the survey presents how the speed-up technique performs against Dijkstra’s algorithm. Moreover, the survey presents two open questions, namely, (1) how to achieve speed-up despite the lack of a hierarchy in transportation networks, and (2) how to efficiently compute local searches, e.g., as in neighborhoods.

Demetrescu and Italiano [39] survey algorithms that investigate fully dynamic directed graphs with emphasis on dynamic shortest-paths and dynamic transitive closures. The survey focuses on defining the algebraic and combinatorial properties as well as tools for dynamic techniques. The survey tackles two important questions, namely whether dynamic shortest-paths achieve a space complexity of _O(n_<sup>2</sup>), and whether single-source shortest path algorithms in a fully-dynamic setting be solved efficiently over general graphs. Nannicini and Liberti [105] survey techniques for dynamic graph weights and dynamic graph topology. They list classical and recent techniques for finding trees and shortest-paths in large graphs with dynamic weights. They target two versions of the problem, namely, time-dependence, and what they refer to as cost updates of the weights. Dean’s survey [35] focuses on time-dependent techniques in a dynamic setting. It surveys one special case, namely, the First-In-First-Out (FIFO) network as it exposes structural properties that allow for the development of efficient polynomial-time algorithms.

This survey presents these aspects that are different from all its predecessors. First, it presents a taxonomy that can aid in identifying the appropriate algorithm to use given a specific setting. Second, for each branch of the taxonomy, the algorithms are presented in chronological order that captures the evolution of the specific ideas and algorithms over time. Moreover, our survey is more comprehensive. We cover more recent algorithms that have been invented after the publication of the other surveys.

## 4 Problem Definition

Given a set of vertices _V_ , a source vertex _s_, a destination vertex _d_, where \(s,d\in V\) , and a set of weighted edges _E_, over the set _V_ , find the shortest-path between _s_ and _d_ that has the minimum weight. The input to the shortest-path algorithm is a graph _G_ that consists of a set of vertices _V_ and edges _E_. The graph is defined as _G_=(_V,E_). The edges can be _directed_ or _undirected_. The edges have explicit weights, where a weight is defined as _w(e_), where \(e\in E\), or unweighted, where the implicit weight is considered to be 1. When calculating the algorithm complexity, we refer to the size of the set of vertices _V_ as _n_ and the size of the set of edges _E_ as _m_.

## 5 Static Shortest-Path Algorithms

In this section, we review algorithms for both the single-source shortest-path (SSSP) and all-pairs shortest- path (APSP) problems.

### 5.1 Single-Source Shortest-Path (SSSP)

_Definition:_ Given a Graph _G_=(_V,E_) and Source \(s\in V\) , compute all distances \(\delta(s,v)\), where \(v\in V\) .

The simplest case for SSSP is when the graph is unweighted. Cormen et al. [34] suggest that breadth- first search can be simply employed by starting a scan from a root vertex and inspecting all the neighboring vertices. For each neighboring vertex, it probes the non-visited vertices until the path with the minimum number of edges from the source to the destination vertex is identified.

