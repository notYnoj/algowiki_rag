2_r_<sub>14</sub>(_n_) for integer \(n\ge 11\). Thus permitting replicated terms can reduce the count per output even when the algorithm is required to be exact. Construction data: Appendix F, `ex28`.

## Thirty-two products with half retained precision.

The _N_=3, _p_=32 family has budget

\(r_{32}(n)=(n+1)^9+9(n+1)^8+27(n+1)^7.\) (157)

Its twenty-seven remaining mixed products, including three replicated products, are suppressed by a grading with _h_=1, giving \(\theta=1/2\). Compared with the exact twenty-eight-product family, it needs eight fewer pair corrections and no triple corrections. Relaxing exactness therefore has two benefits here: more products are aggregated, and the total multiplication budget is smaller. Construction data: Appendix F, `br32`.

## Thirty-five products with one-third retained precision.

The _N_=3, _p_=35 family has the same correction budget as the half-accuracy construction:

\(r_{35}(n)=(n+1)^9+9(n+1)^8+27(n+1)^7.\) (158)

Its eighty-three remaining mixed products, including thirty-six replicated products, admit normalized exponents of height 2, giving \(\theta=1/3\). The three additional outputs therefore require no increase in the multiplication budget. A full-correction variant attains the slightly larger fraction 8/23 with thirty-one pair corrections; its tripartitions and exponents are supplied for that stronger requirement. Construction data: Appendix F, `br35` and `br35full`, respectively.

## Thirty-six products with quarter retained precision.

A further _N_=3 family adds one more product at the same cost:

\(r_{36}(n)=(n+1)^9+9(n+1)^8+27(n+1)^7.\) (159)

Here _h_=3 gives \(\theta=1/4\). Of its 171 remaining mixed products, 116 are replicated. Thus the half-, third-, and quarter-accuracy choices have distinct supports and gradings but identical rank polynomials, aggregating 32, 35, and 36 products, respectively. Construction data: Appendix F, `br36`.

## One hundred and five exact products.

For _N_=4, the corrected exact family has

\(r_{105}(n)=(n+1)^{12}+12(n+1)^{11}+66(n+1)^{10}+124(n+1)^9+3(n+1)^8.\) (160)

All singleton and pair corrections occur, but only 124 of the 220 triples and three of the 495 quadruples are needed. The correction-free family at the same order aggregates 38 products with budget (_n_+1)<sup>12</sup>. Thus the corrected family provides almost three times as many outputs, but must first overcome a substantial correction cost. At a fixed matrix dimension, increasing _N_ also reduces the local dimension _n_; this delays the advantage over the _N_=3 families. Construction data: Appendix F, `ex105` and `ex38`.

## One hundred and forty-one products with quarter retained precision.

The largest graded family at quarter retained precision has _N_=4, _p_=141, and budget

\(r_{141}(n)=(n+1)^{12}+12(n+1)^{11}+66(n+1)^{10}+144(n+1)^9+6(n+1)^8.\) (161)

A grading of height three suppresses its 497 remaining mixed products, of which 109 are replicated, giving \(\theta=1/4\). The 125- and 133-product families satisfy the stronger bounds \(h\le 1\) and \(h\le 2\), respectively. All four large families share the leading aggregate and all singleton and pair corrections. Their budgets differ only in the (_n_+1)<sup>9</sup> and (_n_+1)<sup>8</sup> terms, while their output counts range from 105 to 141. Consequently, relaxing the retained-precision requirement increases the number of products at nearly the same total multiplication cost. Construction data: Appendix F, `br125`, `br133`, and `br141`.

