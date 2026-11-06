## 8.2 Construction parameters

For each family below, let _r<sub>p</sub>(n_) denote its multiplication budget for all _p_ products of dimension _q=n<sup>N</sup>_. For an exact construction this is an upper bound on \(R(\langle q,q,q\rangle^{\oplus p})\); for a parameter-dependent construction it bounds the border rank and counts the bilinear products at each nonzero parameter value. In (101), (_n_+1)<sup>3_N_</sup> counts the main aggregate and \(\kappa_s(n+1)^{3N-s}\) counts the corrections omitting _s_ coordinates. Thus singleton, pair, triple, and quadruple corrections have _s_=1,2,3,4, respectively (Definition 14). The correction counts, normalized heights, and limiting fractions of retained accuracy are summarized in  3. Appendix F indexes the complete construction data and identifies the figures in which each construction appears; the identifiers below are the file stems in that index.

### Fourteen exact products.

The _N_=3, _p_=14 family has fourteen distinct labels in each variable space. Centering annihilates every non-diagonal choice, so one aggregate on nine indices suffices:

\(r_{14}(n)=(n+1)^9.\) (155)

There are no corrections or parameter exponents. This gives fourteen independent matrix-matrix products with the lowest embedding overhead among the principal _N_=3 families, which explains its advantage at intermediate dimensions. Construction data: Appendix F, `ex14`.

### Twenty-eight exact products.

A second _N_=3 family doubles the number of independent matrix- matrix products by admitting replicated mixed terms. Nine singleton, thirty-five pair, and four triple corrections remove these terms, giving

\(r_{28}(n)=(n+1)^9+9(n+1)^8+35(n+1)^7+4(n+1)^6.\) (156)

No compatible non-diagonal product remains. The correction terms grow more slowly than the main aggregate, so the larger support eventually costs less than two fourteen-product aggregates. In fact, _r_<sub>28</sub>(_n)\<_<tbc>

\begin{tabular}{cccccc}
_N_ & _p_ & type & \((\kappa_1,\kappa_2,\dots)\) & _h_ & \(\theta\) \\
2 & 6 & exact & (4) & 0 & 1 \\
2 & 6 & border rank & \(\emptyset\) & 3 & \(\frac{1}{4}\) \\
2 & 7 & border rank & \(\emptyset\) & 15 & \(\frac{1}{16}\) \\
2 & 8 & border rank & (5) & 1 & \(\frac{1}{2}\) \\
2 & 9 & border rank & (6) & 2 & \(\frac{1}{3}\) \\
2 & 9 & border rank & (5) & \(\frac{8}{3}\) & \(\frac{3}{3}\) \\
2 & 10 & border rank & (4) & 7 & \(\frac{1}{8}\) \\
3 & 14 & exact & \(\emptyset\) & 0 & 1 \\
3 & 28 & exact & (9,35,4) & 0 & 1 \\
3 & 32 & border rank & (9,27) & 1 & \(\frac{1}{2}\) \\
3 & 35 & border rank & (9,27) & 2 & \(\frac{1}{3}\) \\
3 & 36 & border rank & (9,27) & 3 & \(\frac{1}{4}\) \\
3 & 37 & border rank & (9,29) & 3 & \(\frac{1}{4}\) \\
3 & 39 & border rank & (9,26) & 12 & \(\frac{1}{13}\) \\
4 & 38 & exact & \(\emptyset\) & 0 & 1 \\
4 & 105 & exact & (12,66,124,3) & 0 & 1 \\
4 & 125 & border rank & (12,66,143,5) & 1 & \(\frac{1}{2}\) \\
4 & 133 & border rank & (12,66,130,6) & 2 & \(\frac{1}{3}\) \\
4 & 141 & border rank & (12,66,144,6) & 3 & \(\frac{1}{4}\) \\
4 & 150 & border rank & (12,66,131,6) & 11 & \(\frac{1}{12}\) \\
\end{tabular}

3: Parameters of the square-product constructions used in the comparisons. Each computes _p_ products of dimension _q=n<sup>N</sup>_. The entry \(\kappa_s\) counts correction aggregates that omit _s_ coordinates; \(\emptyset\) means that no corrections are used. The normalized height _h_ and limiting retained fraction \(\theta=1/(1+h)\) are defined in Section 7. The two _N_=2_,p_=9 rows trade one singleton correction for a weaker accuracy requirement. The data files and figure appearances for every row are indexed in Appendix F.

