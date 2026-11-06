<tbc>dates. Then the RNG’s strategy is used to select the neighbors from candidates, trying to ensure the existence of monotonous paths from the navigating node to all other nodes. Compared with NSG, the edge selection strategy adopted by NSSG\[20\] is that if the angles between the candidate edge and all existing edges are greater than \(\alpha(\alpha\le 60^\circ)\), the candidate edge will be selected, which effectively reduces the sparsity. Meanwhile, the NSSG directly uses approximate k nearest neighbors as the candidate set reducing the index complexity.

KNNG based graphs. The KGraph\[15\] directly uses the approximate K Nearest Neighbor Graph (KNNG) as the index. The DPG\[16\] selects a fixed number of edges based on the approximate k nearest neighbors which maximizes the average pairwise angle. Then the reverse edges are added to enhance the connectivity. The Efanna\[33\] uses Kd-tree as navigation and continue search on approximate KNNG.

## 2. Algorithm and Analysis

### 2.1. Motivation

Almost all the graph-based algorithms adopt algorithm like Algorithm 1 for ANNS query. The algorithm can be simply summarized as: starting from a specific point, take it as the expanding point, calculate the distances between its neighbors and the query point then select the closest one as the next expanding point. Repeat it until the local optimum is met where no neighbor is closer to query than the expanding point. To approach the global optimum, we use a priority queue to store visited points for backtracking. The query time cost can be roughly estimated as the product of length of search path and average out-degree of the graph. In order to improve accuracy and efficiency, we put forward the definition of monotonic search.

**Definition 2.** _(Monotonic Search). For a given query point q, a graph defined on_ D _achieves monotonic search if for each node_ \(v_i\in G\) _there are at least one edge_ \(\overrightarrow{v_iv'_j}\in G\) _makes_ \(\delta(q,v_j)<\delta(q,v_i)\) _unless v<sub>i</sub> is the nearest neighbor of q._

