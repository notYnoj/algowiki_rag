**_Q2:_** _What is the time complexity of All-Pairs Max-Flow when restricted to combinatorial algorithms?_

A typical hope is that this restriction would facilitate better conditional lower bounds. Indeed, at least for dense graphs, **_Q2_** is settled. By a reduction from the problem of detecting a 4-clique in a graph, it was shown \[AGI<sup>+</sup>19\] that all directed variants are unlikely to admit \(O(n^{4-\varepsilon})\) time combinatorial algorithms. Later, this technique was extended to undirected graphs with unit node- capacities \[HLSW23\], implying an _n_<sup>4-_o_(1)</sup> conditional lower bound against combinatorial algorithms for them as well. This result finally established that _no_ hard variant can be solved faster than the naive approach by a combinatorial algorithm, at least when the input graph is dense. Notably, all these _n_<sup>4-_o_(1)</sup> conditional lower bounds can also be expressed as _m_<sup>2-_o_(1)</sup> conditional lower bounds for all _m_ (accomplished by simply adding isolated nodes). This still leaves a gap for less dense graphs in various settings, including undirected graphs with unit node-capacities, for which the current upper bound is \(min\{\hat{O}(n^2\cdot m),\hat{O}(m^{11/5})\}\) (see Figure 1).

## 1.1 A New Algorithm for Graphs with Unit Node-Capacities

In our main result we resolve **_Q2_** for this setting across all densities by closing the gap with the known conditional lower bound against combinatorial algorithms (see also Figure 1), settling the time complexity of All-Pairs Max-Flow in these settings.

**Theorem 1.1.** _There is a randomized Las Vegas algorithm that given an undirected graph G_=(_V,E_) _with unit node-capacities, makes_ \(\tilde{O}(m)\) _calls to Max-Flow in G and spends_ \(\tilde{O}(mn)\) _time outside of these calls, and can:_

• _construct a data structure of size_ \(\tilde{O}\left(m^{3/2}\right)\) _that stores a set_ C _of_ \(\tilde{O}(m)\) _vertex-cut separators_<sup>7</sup>_, such that given a queried pair_ \(u,v\in V\) _outputs in_ \(\tilde{O}(1)\) _time a pointer to an optimal uv- separator in_ C.<tbc>

• _construct a data structure of size_ \(\tilde{O}(m)\) _that given a queried pair_ \(u,v\in V\) _outputs in_ \(\tilde{O}(Max-Flow(u,v))\) _time_<sup>8</sup> _the value Max-Flow(u,v_) _(or simply in_ \(\tilde{O}(1)\) _time in an alternative Monte Carlo version)._

To obtain this bound, we depart from the recent practice of using element-connectivity<sup>9</sup> for constructing vertex-connectivity data structures \[PSY22, HLSW23\], and adapt an algorithm previously employed for \((1+\varepsilon)\)-approximate All-Pairs Max-Flow on undirected, edge-capacitated graphs \[AKT20a\]. Note that our algorithm is Las Vegas, unlike many of the recent algorithms for All-Pairs Max-Flow which are Monte Carlo \[PSY22, AKL<sup>+</sup>22, HLSW23, ALPS23\]. This algorithm is also combinatorial, and runs in \(\hat{O}(m^2)\) time using the recent near linear \(\hat{O}(m)\) time Max-Flow algorithm \[CKL<sup>+</sup>22, vdBCP<sup>+</sup>23\], improving on the recent \(\hat{O}(m^{11/5})\) \[HLSW23\] time algorithm for the problem.

## 1.2 Other Results

Following our resolution of **_Q2_** for unit node-capacities, the main open question remains: can we answer **_Q1_** by proving _n_<sup>4-_o_(1)</sup> conditional lower bounds for general algorithms too? Perhaps surprisingly, we establish a strong barrier to the possibility of such a result. We address **_Q1_** by<tbc>

<sup>7</sup>For a pair \(u,v\in V\) , a vertex-cut _uv_-separator is a set of nodes separating _u_ and _v_. <sup>8</sup>Max-Flow values greater than \(\sqrt{m}\) can be output in \(\tilde{O}(1)\) time using high-degree considerations. <sup>9</sup>Given a graph _G_=(_V,E_) and a terminal subset \(T\subseteq V\) , the element-connectivity between \(u,v\in T\) is the maximum number of paths between _u_ and _v_ in _G_ that are disjoint with respect to _E_ and also to _V_\\_T_.

