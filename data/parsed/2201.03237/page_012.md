<tbc>In NSSG[20], Fu et al. propose a new edge selection strategy. For a point _s_, the NSSG’s strategy will select the neighbor set _V_ from the candidate set _E_ with threshold \(\alpha_t\) (\(\alpha_t\le 60^\circ\)) following two steps:

1. Sort \(e\in E\) in the ascending order of \(\delta(s,e)\);<tbc>

2. For each point \(e\in E\), only if all the point \(v\in V\) satisfies \(\angle vse>\alpha_t\), _e_ will be added to _V_ , otherwise not.

That is to say, point _A_ will not connect _B_ if \(\alpha\le\alpha_t\). If \(\alpha_t=60^\circ\), according to inequation (2), the lower bound is also only 50%. If \(\alpha_t<60^\circ\), it will cause the over large out-degree of nodes, which lead to decline in search efficiency. We illustrate this by a toy example in Figure 1.

## 2.3. A new edge selection strategy

In order to construct a (_r,p_)-MSNET, we expect the edge selection strategy to guarantee the probability for any given value. Therefore, the key of the edge selection strategy is the calculation of the probability.

C
r
a
B
A
D
E

Figure 3: point _A_ is the current node, where point _C_ is one of existing neighbors, point _B_ is the candidate of point _A_. Point _B_ is the nearest neighbor of the point _Q_.

