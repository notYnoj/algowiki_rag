16
Strassen, b = 2
q = n3, p = 14
LITA, b = 32
q = n3, p = 28
Smirnov, b = 54
q = n4, p = 38
Schwartz-Zwecher, b = 1936
q = n4, p = 105
q = n2, p = 6
12
Reduction factor pq3/r
8
4
1
2
10
100
1000
16000
Matrix dimension q

Strassen, b = 2
q = n2, p = 9, 0 2 1/3
q = n3, p = 37, 0 2 1/4
LITA, b = 32
q = n2, p = 9, 0 2 1/4
20
Schönhage + exact, 0 2 1/3
q = n3, p = 32, 0 2 1/2
q = n4, p = 125, 0 2 1/2
Bini + exact, 0 2 1/4
q = n3, p = 35, 0 2 1/3
q = n4, p = 133, 0 2 1/3
q = n2, p = 6, 0 2 1/4
q = n3, p = 36, 0 2 1/4
q = n4, p = 141, 0 2 1/4
15
Reduction factor pq3/r
10
5
1
2
10
100
1000
16000
Matrix dimension q

Figure 4: Multiplication-count reduction factors for exact algorithms. Each solid curve computes _p_ independent products of dimension _q=n<sup>N</sup>_; dashed curves apply the indicated prior base of dimension _b_ recursively. Markers indicate dimensions _q=n<sup>N</sup>_ with integer _n_, with the interpolation conventions of Section 8.1. The _p_=14 and _p_=38 families use centering without corrections. The _p_=6,28,105 families include the corrections counted in  3. Larger corrected families become advantageous as their correction terms decrease relative to the leading aggregate.

Figure 5: Multiplication-count reduction factors with limiting fraction of retained precision at least 1/4. Labels distinguish the half-, third-, and quarter-precision bounds; the exact _p_=105 family has \(\theta=1\). Solid curves are the centered constructions of this paper. Dashed curves are exact prior algorithms or a single Schönhage or cyclic Bini approximation followed by exact algorithms for the remaining subproblems. These latter two constructions have \(\theta=1/3\) and 1/4, respectively, as derived in Appendix B.2. The limiting fraction is relative to the classical error reference; Section 7.4 gives the parameter rule and the finite-precision comparison, including the approximation coefficients and factor norms. All counts use the conventions of Section 8.1.

