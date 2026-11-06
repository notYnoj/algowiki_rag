### Other accuracy requirements.

At quarter retained precision, a 37-product family improves the count per product of the 36-product family for \(n\ge 3\). Without the quarter-accuracy requirement, 39 products are possible with fewer pair corrections. Their budgets are

\(r_{37}(n)=(n+1)^9+9(n+1)^8+29(n+1)^7,\theta=\frac{1}{4},\) (162)

\(r_{39}(n)=(n+1)^9+9(n+1)^8+26(n+1)^7,\theta=\frac{1}{13}.\) (163)

A twelfth-order construction without an accuracy requirement gives

\(r_{150}(n)=(n+1)^{12}+12(n+1)^{11}+66(n+1)^{10}+131(n+1)^9+6(n+1)^8,\theta=\frac{1}{12}.\) (164)

At order six, the selected unrestricted ten-product construction uses only four singleton corrections, with _h_=7 and \(\theta=1/8\). A nine-product variant uses five singleton corrections and attains \(\theta=3/11>1/4\); the version attaining 1/3 uses six. These choices target small multiplication counts at the stated limiting accuracy requirements, not the full finite-precision error bound. Construction data: Appendix F, `br37`, `ub9`, `ub12`, `br10`, `br9q`, and `br9`.

### Accuracy at fixed precision.

The normalized height _h_ determines the growth \(\lambda^{-h}\) of \(\sigma\), while the leading approximation coefficient \(\beta'(0)\) of Definition 23 includes only mixed products of smallest positive degree, weighted by |_c_<sub>Q</sub>(R_<sub>ijk</sub>_)|(_n_+1)<sup>|R_<sub>ijk</sub>_|</sup>.  5 gives these quantities and the normalized leading coefficient \(\sigma_0/\sigma_c\) (Definition 25) for the approximate families. The correction sets also enter the factor norms, so both \(\sigma_0\) and \(\beta'(0)\) are recomputed for each selected family. The limiting fraction is determined by _h_; the remaining mixed products and factor norms additionally affect the parameter choice and accuracy at fixed working precision. Reducing the count at a prescribed limiting fraction does not minimize the error bound at fixed precision: omitting replicated corrections can substantially increase \(\beta'(0)\). Full-correction variants therefore remain relevant when these constants are decisive. For exact families, the common bound (136) shows that the extra amplification decreases to one as _n_ increases.

The parameter rule balances the first approximation term against the leading intermediate-rounding term. This minimizes their sum when _h_=1, but need not do so for other heights. The higher-order approximation terms can be included by minimizing the full bound (145) with respect to \(\lambda\). This changes the finite-precision parameter choice while retaining the same limiting fractions displayed in the count comparisons.

Neither the limiting retained fraction nor balancing, or even minimizing, these error bounds necessarily selects the most stable or fastest construction at a fixed working precision. The bounds are conservative, and multiplication counts omit encoding, decoding, and data movement. Searches intended for an implementation should therefore account for error constants and higher-order approximation terms, the evaluation order, and measured execution costs at the precision and dimensions of interest.

## 8.3 Centering, corrections, and weighting

We separate the cost of evaluating a fixed support from the number of products that a weighted aggregate can accommodate. For the first comparison, the centered, padded, and weighted embedding of Section 5.4 uses (_n_+2)<sup>3_N_</sup> multiplications. The construction with selected corrections uses \(\rho_{\mathcal{S},\mathcal{Q}}(n)\) on the _same support_, with the _same grading_. Figure 2 shows the fractional saving, normalized to the weighted count:

\(1-\frac{\rho_{\mathcal{S},\mathcal{Q}}(n)}{(n+2)^{3N}}.\) (165)

For a graded support, weighting eliminates all replicated terms, whereas explicit corrections need eliminate only those required by the prescribed accuracy. The weighted version therefore meets at least the same limiting accuracy requirement; equality of finite-precision errors is not assumed. Appendix C.1 gives the weighted specialization.

The exact _p_=14 and _p_=38 families are outliers in Figure 2: centering alone suffices, with no corrections. Their savings are 1-((_n_+1)/(_n_+2))<sup>3_N_</sup>, approximately 28.8% at (_N,n_)=(3,25) and 61.7% at (4,11),<tbc>

