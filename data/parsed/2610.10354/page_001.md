# Min-Plus Convolution Lower Bounds via a Higher-Order BSG Theorem

Nick Fischer<sup>∗</sup>

Ce Jin<sup>†</sup>

Yinzhan Xu<sup>‡</sup>

**Abstract**

_Min-Plus Convolution_ is a central problem in fine-grained complexity, and the associated Min- Plus Convolution Hypothesis forms the basis for a wide range of conditional lower bounds for fundamental problems. It is closely connected to the APSP and 3SUM Hypotheses, and in fact implies both, making it a unifying hypothesis for two of the main pillars of the area. In this work we establish several strong results related to Min-Plus Convolution. We design a _universe reduction_, showing, under a plausible additive combinatorics assumption, that the Min-Plus Convolution Hypothesis is _equivalent_ to the _Strong_ Min-Plus Convolution Hypothesis. We also obtain tight conditional lower bounds for multiple long-standing problems, including Min-Max Convolution and Bounded Monotone Min-Plus Convolution.

Our approach is inspired by Fischer’s recent equivalence between several variants of APSP [S ’26], but extending that technique to the arithmetic setting requires overcoming deep obstacles. To this end, we develop a novel additive structure theorem that can be viewed as a higher-order substitute of the Balog–Szemerédi–Gowers (BSG) theorem, allowing us to extract strong additive structure even from weakly structured sets. Building on this structural result, we show that certain structured 3SUM instances (namely, sets with low _rank_) can be solved in truly subquadratic time. This algorithm forms the main algorithmic ingredient in our reductions. Besides, it generalizes _all_ previously known truly subquadratic-time special cases of 3SUM, and is therefore of independent interest.

<sup>∗</sup>Max Planck Institute for Informatics. E-Mail: `nfischer@mpi-inf.mpg.de` †University of California, Berkeley. E-Mail: `cejin@berkeley.edu` ‡University of California, San Diego. E-Mail: `xyzhan@ucsd.edu`

