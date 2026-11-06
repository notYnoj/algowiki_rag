<tbc>new constructions instead reduce the count per product by aggregating more independent matrix-matrix products at a prescribed limiting retained fraction.

Without a precision constraint, the smaller supports in Figure 6 can use much larger parameter exponents. The seven-product family suppresses all remaining mixed products without corrections; the ten-product family permits more outputs with a small correction budget. Their improved counts at small dimensions come at the cost of a large limiting loss of accuracy. This tradeoff is less favorable at larger dimensions, where the 39- and 150-product families overtake them at their respective accuracy levels.

Smirnov’s rank-20 base gives the strongest prior unrestricted curve shown. Its direct realization has limiting fraction 1/7 for one level and 1/(1+6_k_) for _k_ levels. By comparison, the 150-product family reduces this formal multiplication-count estimate by a factor of approximately 1.516 at _q_=14641, with \(\theta=1/12\). At the stronger requirement \(\theta\ge 1/4\), the 141-product family gives a factor of approximately 1.421. Thus the new constructions appear promising in comparison with prior works in the multiplication count achieved both by exact constructions and border rank constructions under various accuracy constraints.

### Unequal shapes.

For complete and incomplete tripartitions with unequal part sizes, s 6 and 7 retain the matrix shapes and product volumes. The complete ten- and thirteen-product families have limiting retained fractions 1/2 and 1/3. A twenty-two-product family gives an asymptotic-sum bound of approximately 2.560147 with limiting retained fraction at least 1/212. The incomplete _d_=6,9 families give bounds near 2.636 and 2.639. These values follow by substituting the complete shape lists and rank budgets into the asymptotic sum theorem.

## 9 Conclusion

We provide explicit aggregation formulas for the simultaneous matrix products obtained from fixed-shape restrictions of powers of the little Coppersmith-Winograd tensor. Centering and weighting give a direct realization of the (_n_+2)<sup>3_N_</sup> multiplication budget. Explicit inclusion-exclusion corrections reduce this<tbc>

Strassen, b = 2
q = n2, p = 7
20
Bini et al., b = 12
q = n2, p = 10
Schönhage, b = 3
q = n4, p = 105
LITA, b = 32
q = n3, p = 39
Smirnov, b = 3
q = n4, p = 150
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

Figure 6: Finite-size border-rank reduction factors without a precision constraint. Prior algorithms are dashed and this paper’s constructions are solid. The _q=n_<sup>2</sup>, _p_=7,10 families have limiting retained fractions 1/16 and 1/8, respectively. The _p_=39,150 families have limiting retained fractions 1/13 and 1/12. Smirnov’s dashed curve uses the rank-20 base of dimension three at unrestricted recursive depth. The _p_=105 curve is exact. Construction parameters and multiplication-count comparisons are defined in Section 8.1, and Appendix B.2 analyzes the parameter dependence of the prior approximations.

