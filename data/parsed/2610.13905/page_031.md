<tbc>can get a decent approximation to the true product without executing the full interpolation procedure of Algorithm 4.

We test Algorithm 5 on three APA routines: Schönhage’s \(\langle 3,3,3;21\rangle\) algorithm (which has highest degree two in its base-case remainder), Smirnov’s \(\langle 3,3,3;20\rangle\) algorithm (which has highest degree ten), and our \(\langle 2,2,3;10\rangle\) algorithm (which has highest degree six). Input matrices _A_ and _B_ are chosen to be \(m_0^4\times k_0^4\) and \(k_0^4\times n_0^4\) with entries sampled independently from N(0,1). Figure 6 shows accuracy results for each algorithm under varying choices of _r_ and \(\beta\). In each case, we see the anticipated tradeoff. If \(\beta\) is too small, even evaluating enough times to get an "exact" product (i.e., running Algorithm 4) gives poor results. On the other hand, if \(\beta\) is close to one - and in particular if only a modestly-accurate product is desired - we can get away with a constant factor reduction in the number of evaluations.

We also observe in these plots the phenomenon discussed in Theorem 1.1. That is, while the highest degree in the base-case remainder of our \(\langle 2,2,3;10\rangle\) algorithm is six (and recalling that we’re testing with inputs that require four recursive steps) we do not need 25 evaluations to get the exact product. This is a result of the fact that the remainder for this algorithm has the special form

\(AB+\varepsilon^3R_3+\varepsilon^6R_6.\) (5.2)

Hence, when we apply the algorithm recursively with _L_=4, only degrees 3, 6, 9, 12, 15, 18, 21, and 24 appear in the remainder. Since we are using scaled _r_-th roots of unity as evaluation points, we obtain the exact product whenever _r_ does not divide any degree in the remainder; this happens here when _r_=25 but also occurs at much lower values of _r_ since only specific exponents are present. This corresponds to the bands of blue in the \(\langle 2,2,3;10\rangle\) panel of Figure 6. We see similar (though less pronounced) behavior for Smirnov’s \(\langle 3,3,3;20\rangle\) algorithm since its base-case remainder omits the exponent nine.

## 6 Conclusion

This paper presented a deep dive into arbitrary precision approximate (APA) matrix multiplication. We provided both a new search algorithm for APA schemes and numerical analysis results aimed at understanding the practical performance of an APA algorithm. As mentioned in the introduction, the goal of this work was to renew interest in APA matrix multiplication, both from the theory and implementation perspectives.

In future work, we plan to pursue high-performance implementations of APA matrix multiplication algorithms with the goal of demonstrating results competitive with fast exact matrix multiplication (possibly in applications where lower precision is required). We have already identified several tools for accelerating APA algorithms - e.g., sparsification, truncation, etc. - but these have not yet been tested in a high- performance environment. It also remains to examine other kinds of approximate matrix multiplication. In<tbc>

\begin{tabular}{cccccc}
 & \multicolumn{4}{c}{Inner Dimension (_k_)} \\
 & 3 & 9 & 27 & 81 & 243 \\
Bound & 2.32 & 4.98 & 10.6 & 22.6 & 48.1 \\
Empirical & 0.98 & 1.12 & 1.01 & 1.05 & 1.04 \\
\end{tabular}

\begin{tabular}{cccccc}
 & \multicolumn{4}{c}{Inner Dimension (_k_)} \\
 & 2 & 4 & 8 & 16 & 32 & 64 \\
Bound & 3.22 & 10.1 & 31.7 & 99.2 & 311 & 974 \\
Empirical & 0.90 & 0.90 & 0.90 & 0.83 & 0.93 & 0.85 \\
\end{tabular}

\begin{tabular}{cccccc}
 & \multicolumn{4}{c}{Inner Dimension (_k_)} \\
 & 2 & 4 & 8 & 16 & 32 \\
Bound & 88.0 & 6.6\(\times\)10<sup>3</sup> & 5.0\(\times\)10<sup>5</sup> & 3.8\(\times\)10<sup>7</sup> & 2.8\(\times\)10<sup>9</sup> \\
Empirical & 1.52 & 0.93 & 1.56 & 1.38 & 1.39 \\
\end{tabular}

(a) \(\langle 3,3,3;21\rangle\)

(b) \(\langle 2,2,3;10\rangle\)

(c) \(\langle 2,2,5;17\rangle\)

4: Error ratios (either empirical or predicted by Theorem 4.6) for the APA algorithms shown in Figure 5, obtained by dividing the error with alternative bases by the error in the standard basis. A value of one indicates the algorithm is equally accurate with/without alternative bases.

