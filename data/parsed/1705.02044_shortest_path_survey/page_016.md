<tbc>It achieves a time complexity of _O(nlog_<sup>3</sup>_n_). It performs update and query operations in _O(n_<sup>4/5</sup>_log_<sup>13/5</sup>_n_) amortized time. The proposed algorithm uses Monge matrices [26] with a combination of Bellman-Ford and Dijkstra’s algorithms for searching in sub-linear time.

Bernstein and Roditty [22] propose a dynamic shortest-paths algorithm that can achieve an update time better than _O(n_) without sacrificing query time. In specific, they obtain _O(n_<sup>2+_o_(1)</sup>) total update time and constant query time. The main type of graphs that it can achieve this result on is moderately sparse graphs. Bernstein and Roditty propose two randomized decremental algorithms that operate over unweighted, undirected graph for two approximate shortest-path problems.

Henzinger et al. [76] improve the update operation time of Bernstein and Roditty [22] to _O(n_<sup>1.8+_o_(1)</sup>+_m_<sup>1+_o_(1)</sup>) while maintaining a constant query time. The algorithm utilizes the center-cover data structure where, given a parameter _h_ and a constant \(\gamma\), maintains _O(h_) vertices, referred to as _centers_. The main property of the center-cover data structure is that every vertex within a specific distance is in a tree termed Even-Shiloach tree (ES-tree). The proposed algorithm has the same property of the center-cover data structure and is fastest when _h_ is moderately small.

## 7 Time-Dependent Shortest-Path Algorithms

A time-dependent shortest-path algorithm processes graphs that have edges associated with a function, known as an _edge-delay_ function. The edge-delay function indicates how much time is needed to travel from one vertex to another vertex. The query operation probes for the the minimum-travel-time path from the source to the destination vertex over graph. The returned result represents the best departure time found in a given time interval.

### 7.1 Continuous-Time Algorithms

Kanoulas et al. [82] propose an algorithm that finds a set of all fastest paths from source to destination given a specified time interval. The specified interval is defined by the user and represents the departure or arrival time. The query algorithm finds a partitioning scheme for the time interval and creates a set of sub-intervals where each sub-interval is assigned to a set of fastest paths. Unlike the _A_<sup>∗</sup> algorithm, the proposed algorithm probes the graph only once instead of multiple times.

Ding et al. [43] propose an algorithm that finds the departure time that minimizes the travel time over a road network. Also, the traffic conditions are dynamically changing in the road network. The algorithm is capable of operating on a variety of time-dependent graphs.

George et al. [64, 65] propose a Time-Aggregated Graph (TAG) graph that changes its topology with time. In TAG, vertices and edges are modeled as time series. Apart from time dependence, it is also responsible for managing the edges and vertices that are absent during any instance in time. They propose two algorithms to compute shortest-path using time-aggregated network (SP-TAG) and best start-time shortest-path (BEST). SP-TAG finds the shortest-path at the time of given query using a greedy algorithm. On the other hand, BEST algorithm finds out the best start-time (i.e., earliest travel time) over the entire period using TAG. The time complexity of SP-TAG and BEST are _O(e(logT+logn_), and _O(n_<sup>2</sup>_eT_), respectively, where _e_ represents edges, _n_ represents vertices, and _T_ represents the time instance.

Ding et al. [43] propose an algorithm for the shortest-path problem over a large time-dependent graph GT. Each edge has a delay function that denotes the time taken from the source vertex to the destination vertex at a given time. The user queries the least travel time (LTT). The proposed algorithm achieves a space complexity of \(O((n+m)\alpha(T))\) and a time complexity of \(O((nlogn+m)\alpha(T))\).

