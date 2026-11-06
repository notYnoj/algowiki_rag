with Tarjan’s algorithm [12], and selecting a sink SCC all take linear time, namely _O(n+m_).

Since _G_ is connected, \(m\ge n-1\). Consequently, the overall running time is _O(m_<sup>2</sup>).

## 6. Conclusions and future work

We studied the detection and construction of small blocking sets in connected simple graphs. A maximum-cardinality critical independent set provides a case classification, and, in the balanced boundary case, the projection theorem reduces the search over the entire graph to the detection of a tight subset within the selected independent set. Matching contraction then reduces this problem to a strong-connectivity test in an auxiliary digraph, and a sink SCC yields a small blocking set. The resulting algorithm runs in _O(m_<sup>2</sup>) time. Future work may investigate base-graph repair by adding the minimum number of edges needed to eliminate all small blocking sets, providing low-cost structural modifications that guarantee universal restless explorability for sufficiently long lifetimes. Another direction is to decide the feasibility of restless exploration and construct exploration schedules for a given permutation sequence, allowing base graphs that do not satisfy the universal explorability condition to be explored under suitable temporal arrangements.

## References

