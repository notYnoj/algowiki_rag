respectively. The larger saving at _N_=4 reflects both the higher order and the smaller local dimension; the correction-free _N_=2 families have much smaller savings at _n_=126. Most remaining families require corrections whose costs offset much of the reduction from dimension _n_+2 to _n_+1. These bars compare the same support with and without weighting; they do not establish the lowest count per product, since families with corrections can accommodate more products.

For the second comparison, Figure 3 shows how many independent products one weighted aggregate can accommodate at fixed _N_, with multiplication count (_n_+2)<sup>3_N_</sup>. Without parameter scaling its support must be conflict-free. Allowing a border-rank grading can admit more products, subject to the requested limiting retained fraction. The capacity search therefore maximizes _p_, independently of _n_, rather than minimizing the correction-based count per product. Only mixed triples surviving weighting constrain this grading. These weighted constructions need not use the same tripartitions or exponents as the centered constructions in Section 8.2;  9 identifies the complete data for every level in Figure 3.

For _N_=4, Figure 3 shows 105 exact products, increasing to 125, 133, and 141 at limiting retained fractions at least 1/2, 1/3, and 1/4, and to 150 without an accuracy requirement. These gains come from allowing parameter scaling to suppress mixed products that an exact weighted construction must exclude. All stronger-accuracy candidates remain eligible at weaker requirements, so the cumulative capacities cannot decrease. Supports at successive levels need not be nested. Search and verification use the procedures and budgets in Section 8.1.

## 8.4 Comparison with prior matrix multiplication algorithms

We now compare our finite constructions with selected prior single-product algorithms. The baseline algorithms first reduce the multiplication count of a single product and are then applied separately to each of the _p_ products. Strassen replaces eight \(2\times 2\) block products by seven \[36\]; the exact Smirnov square base combines three cyclic rectangular rank-40 constructions \[34\]. Pan’s methods aggregate trilinear terms and cancel the unwanted products \[26\]. Schwartz-Zwecher and LITA refine this approach for a single square product \[31, 22\]. LITA has the lowest exact exponent among the bases in  4. Comparing against<tbc>

61.7
60
Fewer multiplications (%)
50
40
28.8
30
20
10
4.6
4.6
1.6
0.8
0.1
0.8
1.6
0.4
1.3
1.3
1.3
1.1
1.4
3.2
2.7
3.0
2.7
3.0
0
6
6
7
8
9
9
10
14
28
32
35
36
37
39
38
105
125
133
141
150
exact
1/4
1/16
1/2
1/3
3/11
1/8
exact
1/2
1/3
1/4
1/4
1/13
exact
1/2
1/3
1/4
1/12
N= = 2, n = 126, q = 15876
N= 3, n = 25, q = 15625
N= = 4, n = 11, q = 14641
Products p (first line); limiting retained fraction (second line)

Figure 2: Percentage fewer multiplications than centering, padding, and weighting the identical support with the identical grading. Each bar is 100 times (165); zero means no saving. The first line below a bar gives _p_, and the second gives exactness or the attained limiting retained fraction. Within each order, _n_ is the largest integer with \(q=n^N\le 16000\). The comparison changes neither the requested products nor the matrix dimension, and involves no composition of different constructions. These are multiplication counts, not execution times.

