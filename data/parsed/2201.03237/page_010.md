## 2.2. Edge selection strategy

The key to build (_r,p_)-MSNET is the 3_<sup>rd</sup>_ step, which is called as edge selection strategy. In NSG, they define another type of MSNET which ensures from any point _A_ to another point _B_, there are at least one path on which the distance from the points to point _B_ decrease monotonically. It is worth noting that points _A_, _B_ must be in the point set D. Therefore, the MSNET defined in NSG achieves monotonic search only if the query point is in the D. However, in high dimensional space, this condition is difficult to guarantee, because the probability that the query point is not in D is much higher. The only difference between (_r,p_)-MSNET and MSNET defined in [14] is the edge selection strategy.

The edge selection strategy adopted by NSG is the RNG’s strategy, which is also adopted by HNSW and FANNG. For a point _s_, the RNG’s strategy will select the neighbor set _V_ from the candidate set _E_, which can be summarized as the following two steps:

1. Sort \(e\in E\) in the ascending order of \(\delta(s,e)\);<tbc>

2. For each point \(e\in E\), only if all the point \(v\in V\) satisfies \(\delta(s,e)<\delta(v,e)\), _e_ will be added to _V_ , otherwise not.

In other words, the point _s_ will not connect a candidate point if there is<tbc>

C
A
n
B
O

Figure 2: point _A_ is the current node, where point _C_ is one of existing neighbors, point _B_ is the candidate neighbor and point _Q_ is the query point. Also, point _B_ is the nearest neighbor of _Q_.

