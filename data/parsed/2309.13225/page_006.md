(Corollary 2.6 of Roditty \[Rod23\]).

1 illustrates the comparison in running time between our algorithms and the previous results of Roditty \[Rod23\] and Dor et al. \[DHZ00\] for dense graphs.

## 1.1.3 Additive Approximation (Section 5)

We show it is possible to get better additive approximations \((1,\beta)\) for all \(\beta>0\). Previously such a result was known only for \(\beta=2\) \[DKR<sup>+</sup>22\].

**Theorem 5.6.** _Let_ \(\beta\ge 4\) _be an even integer. Let G be an undirected, unweighted graph with n vertices. Algorithm 6 computes_ \(\hat{\delta}\) _such that_ \(\delta(u,v)\le\hat{\delta}(u,v)\le\delta(u,v)+\beta\) _for all_ \(u,v\in V\) _in time,_ \(\tilde{O}\left(n^{2+\frac{2x}{\beta+2}}\right)\) _where x is the solution to,_ \(\omega\left(1-\frac{\beta-2}{\beta+2}x,1-x,1-\frac{\beta-4}{\beta+2}x\right)=1+\frac{4+2\beta}{\beta+2}x\).<sup>1</sup>

2 shows the improvement in running time for various \((1,\beta)\)-approximation errors beyond the work of Dor, Halperin, and Zwick \[DHZ00\]. The concurrent work \[DFK<sup>+</sup>23\] obtains a \((1+\varepsilon,\beta)\)- approximation faster than \[DHZ00\] for \(\beta\le 9\). We obtain \((1,\beta)\)-approximation improving upon \[DHZ00\] for all \(\beta\) and do so without incurring any multiplicative error. Our algorithm is also faster than the \((1+\varepsilon,\beta)\)-approximation of \[DFK<sup>+</sup>23\] for \(\beta\ge 8\). Due to the additional multiplicative error, we instead compare \[DFK<sup>+</sup>23\] with Algorithm 9 in  4.

## 1.1.4 Weighted Graphs & \((\alpha,\beta)\)-approximations (Section 6 & Section 7)

We show new results that allow for \((1+\epsilon)\)-multiplicative approximation of APSP, and some additive errors to go significantly below \(n^\omega\) for weighted graphs. We also show interesting new trade-offs between \(\alpha<2\), and \(\beta\) for both unweighted and weighted graphs (see Theorem 7.1 and Theorem 7.4).

<sup>1</sup>\(\omega(a,b,c)\) is the minimum value such that the product of a \(\left\lceil n^a\right\rceil\times\left\lceil n^b\right\rceil\) matrix by a \(\left\lceil n^b\right\rceil\times\left\lceil n^c\right\rceil\) matrix can be computed in \(O(n^{\omega(a,b,c)+\varepsilon})\) arithmetic operations for any constant \(\varepsilon>0\). Note \(\omega=\omega(1,1,1)\).

\begin{tabular}{ccc}
\multicolumn{3}{c}{\(+\beta\)-Additive Approximation} \\
\(\beta\) & \[DHZ00\] & Algorithm 6 \\
4 & _n_<sup>11/5</sup>=_n_<sup>2.2</sup> & _n_<sup>2.15506251</sup> \\
6 & _n_<sup>17/8</sup>=_n_<sup>2.125</sup> & _n_<sup>2.10300405</sup> \\
8 & _n_<sup>23/11</sup>=_n_<sup>2.0909</sup> & _n_<sup>2.07733373</sup> \\
10 & _n_<sup>29/14</sup>=_n_<sup>2.0715</sup> & _n_<sup>2.06196791</sup> \\
\end{tabular}

2: Improvements in computing \(+\beta\) approximation on undirected, unweighted graphs with _n_ vertices. While a few examples are shown above, we obtain improvements for all \(\beta\ge 4\). All running times are computed with \[Bra\].

