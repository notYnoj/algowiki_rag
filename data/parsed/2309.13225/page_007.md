**Theorem 6.3.** _Let_ \(\beta\ge 2\) _be an integer and_ \(\varepsilon>0\)_. Let G be an undirected, unweighted graph with n vertices. Algorithm 9 computes_ \(\hat{\delta}\) _such that_ \(\delta(u,v)\le\hat{\delta}(u,v)\le(1+\varepsilon)\delta(u,v)+2w_{u,v}(\beta)\) _in time_ \(\tilde{O}\left(\frac{n^{2+}\frac{x}{\beta+1}}{\varepsilon}\right)\) _where x is the solution to,_ \(\omega\left(1-\frac{\beta-1}{\beta+1}x,1-x,1-\frac{\beta-2}{\beta+1}x\right)=2+\frac{x}{\beta+1}\)_. Here,_ \(w_{u,v}(\beta)\) _denotes the total weight of the_ \(\beta\) _heaviest edges of a shortest path P._

We compare Algorithm 9 with concurrent work \[DFK<sup>+</sup>23\]. In addition to handling weighted graphs, our algorithm is faster than both \[DHZ00\] and \[DFK<sup>+</sup>23\] for all \(\beta\ge 4\).

## 1.2 Other Related Work

Dor, Halperin and Zwick’s results to additively approximate APSP \[DHZ00\] improves upon an earlier work of Aingworth et al. \[ACIM99\] where a +2 additive approximation was obtained in _O(n_<sup>2.5</sup>) time. Cohen and Zwick \[CZ01\] observed that the algorithm of Dor et al. \[DHZ00\] obtain \(2w_{u,v}(\beta)\) additive approximations for weighted graphs where \(w_{u,v}(\beta)\) denote the weights of the \(\beta\) heaviest edges on the shortest path. Cohen and Zwick \[CZ01\] obtain a variety of multiplicative approximation algorithms for weighted graphs with stretch factors 2, 7/3, 3, which are later improved upon by Baswana and Kavitha \[BK10\]. For directed graphs with real weights in \[0_,M_\], Yuster \[Yus12\] obtained an additive approximation with error \(\varepsilon M\) in time \(O(n^{(3+\omega)/2})\). Building upon this work, Chan \[Cha21\] improved the running time on undirected graphs to \(O(n^{(3+\omega^2)/(\omega+1)})\).

There is a long line of work investigating approximate distance oracles, where the goal is to trade- off the pre-processing time with query time along with further considerations such as space complexity. Thorup and Zwick gave a stretch 2_k_-1 distance oracle with _O(k_) query time, _O(kn_<sup>1+1_/k_</sup>) space,<tbc>

\begin{tabular}{ccc}
\multicolumn{3}{c}{Approximation Algorithms on Weighted Graphs} \\
Work & Approximation Factor & Time \\
\[Zwi02\] & \((1+\varepsilon,0)\) & \(n^\omega\) \\
\[Elk05\] & \((1+\varepsilon,M\beta(\zeta,\rho,\varepsilon))\) & \(mn^\rho+n^{2+\zeta}\) \\
\[BK07\] & \((1+\varepsilon,2w_{u,v})\) & _n_<sup>2.24</sup> \\
Algorithm 8 & \((1+\varepsilon,2w_{u,v})\) & _n_<sup>2.1519</sup> \\
Algorithm 9 & \((1+\varepsilon,2w_{u,v}(\beta))\) & \(n^{2+x/(\beta+1)}\) \\
\end{tabular}

\begin{tabular}{cccc}
\multicolumn{4}{c}{\((1+\varepsilon,\beta)\)-Additive Approximation} \\
\(\beta\) & \[DHZ00\] (Weighted) & \[DFK<sup>+</sup>23\] (Unweighted) & Algorithm 9 (Weighted) \\
2 & _n_<sup>7/3</sup>=_n_<sup>2.34</sup> & _n_<sup>2.152</sup> & _n_<sup>2.152</sup> \\
4 & _n_<sup>11/5</sup>=_n_<sup>2.200</sup> & _n_<sup>2.119</sup> & _n_<sup>2.094</sup> \\
6 & _n_<sup>17/8</sup>=_n_<sup>2.125</sup> & _n_<sup>2.098</sup> & _n_<sup>2.058</sup> \\
8 & _n_<sup>23/11</sup>=_n_<sup>2.0909</sup> & _n_<sup>2.084</sup> & _n_<sup>2.043</sup> \\
10 & _n_<sup>29/14</sup>=_n_<sup>2.0715</sup> & \[DHZ00\] & _n_<sup>2.034</sup> \\
\end{tabular}

3: Comparison with previous results for \((\alpha,\beta)\)-approximations on weighted graphs. _M_ denotes the ratio between the heaviest and lightest edge in the graph _G_. \(w_{u,v}(\beta)\) denotes the weight of the \(\beta\) heaviest edges on the shortest path between _u,v_ and _w<sub>u,v</sub>=w<sub>u,v</sub>_(1).

4: Comparison with \[DFK<sup>+</sup>23\] of computing \((1+\varepsilon,\beta)\) approximation on undirected, unweighted graphs with _n_ vertices. While a few examples are shown above, we obtain improvements for all \(\beta\ge 4\). \[DHZ00\] (with adaptions from \[CZ01\]) and Algorithm 9 additionally handle weighted graphs.

