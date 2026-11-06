3. We determine the exact quantum optimum with one comparison for every number of designs and every good-enough set, with a matching upper certificate and an attaining algorithm. The value is affine in the smallest positive root of an explicit cubic, with closed forms for the best design and for the top half, and it gives the limiting success probability for a fixed good-enough fraction.<tbc>

4. For selecting the best design, the equivalent blind-pick size of one quantum comparison increases with the number of designs toward \((3+\sqrt{13})/2\approx 3.30\), compared with 2 for one classical comparison, and it exceeds that of two classical comparisons exactly when there are more than nine designs. For the top 5 percent of 1000 designs it is about 3.27. In the cases computed it decreases as the good-enough set grows, and for the top half of 1000 designs it is below that of two classical comparisons.

The one-comparison result also raises the question of how the quantum benefit changes as more comparisons are allowed. Known search bounds and the reduction in Section 8.1 show that for selecting the best design the quantum equivalent blind-pick size grows at most quadratically in the comparison budget [11, 12], and minimum finding attains this order when the number of designs is at least of the order of the square of the budget [8]. The classical size is the budget plus one, so the ratio of quantum to classical sizes grows at most in proportion to the budget and reaches that order when the designs are numerous enough. This paper determines the ratio exactly for one comparison.

Section 2 reviews related work, and Section 3 defines the model and measures. Sections 4- 6 establish the classical optimum, the quantum degree bound and the exact one-comparison value. Section 7 compares the values in OO terms, Section 8 discusses larger budgets, evaluations and computational cost, and Section 9 summarizes the findings.

## 2 Relation to prior work

The relevant literature treats selection from performance estimates, selection through comparisons and exact optimization of quantum query algorithms. We distinguish these settings because their oracles and success criteria determine which guarantees can be compared with OO alignment.

### Classical ordinal optimization.

OO uses the fact that an estimated order can converge faster than estimated values. For several common performance measures, the order converges exponentially fast in the simulation length [13]. Its selection rules include blind pick, which selects designs at random; the horse race, which selects the designs that look best under a crude model [3]; and budget allocation rules such as optimal computing budget allocation (OCBA) [14]. These rules are catalogued and compared in [2].

Classical OO compares selection rules mainly by simulation. Lau and Ho listed round-robin and pairwise comparison rules as yet to be studied [3]. These rules were later defined for noisy observations and compared numerically, and no universally best selection rule is known [2]. Apart from budget allocation rules such as OCBA, existing OO optimality results apply to the final selection given the observations. Under independent, identically distributed noise and equal allocation, choosing the observed top designs is optimal [2], and with design-dependent<tbc>

