<tbc>gap between accurate probability and min\_prob tends to increase, so min\_prob is a loose lower bound. Also, both probabilities and the min\_prob decrease monotonically with the increase of \(\varphi\), we can adjust the probability through min\_prob.

Our edge selection strategy is based on min\_prob . For a node _s_, with _E_ as candidate set and _mp_ as threshold of min\_prob, we perform the following steps to select neighbor set _V_ :

1) Sort \(e\in E\) in the ascending order of \(\delta(s,e)\);<tbc>

2) For each node \(e\in E\) we list all existing neighbor \(v\in V\) with \(\delta(v,e)<\delta(s,e)\) and calculate the min\_prob of monotonic search with edge \(\overrightarrow{s}\). If all are lower than _mp_, _e_ is added to _V_ , otherwise not.

There is a simple example showing the difference between three popular edge selection strategies in Figure 5. To further improve the search efficiency, we expect to achieve monotonic search with guaranteed probability meanwhile keeping smallest out-degree.

## 2.4. TBSG

To build a (_r,p_)-MSNET, for each node its candidate neighbor set should include all other nodes. Therefore, the time complexity is at least _O(n_<sup>2</sup>_m_), where _n_ is the cardinality of the dataset and _m_ is the maximum of neighbor size. An effective way to reduce the complexity is that for each node its candidate<tbc>

1.0
2-d prob
3-d prob
4-d prob min_prob
0.9
0.8
probability
0.7
0.6
0.5
0.0
0.5
1.0
1.5
2.0
2.5
3.0
V

Figure 4: Comparison between probabilities in 2, 3, 4 dimensional space and min\_prob

