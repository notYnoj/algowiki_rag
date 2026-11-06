# Approximations schemes for Edit Distance and LCS in quasi-strongly subquadratic time

**Abstract**

We present novel randomized approximation schemes for the Edit Distance (ED) problem and the Longest Common Subsequence (LCS) problem that, for any constant \(\varepsilon>0\), compute a \((1+\varepsilon)\)-approximation for ED and a \((1-\varepsilon)\)-approximation for LCS in time \(n^2/2log^{\Omega(1)}(n)\) for two strings of total length at most _n_. This running time improves upon the classical quadratic-time dynamic programming algorithms by a quasi-polynomial factor.

Our results yield significant insights into fine-grained complexity: Firstly, for ED, prior work indicates that any exact algorithm cannot be improved beyond a few logarithmic factors without refuting established complexity assumptions [Abboud, Hansen, Vassilevska Williams, Williams, 2016]; our quasi-polynomial speed-up shows a separation the complexity of approximate ED from that of exact ED, even for approximation factor arbitrarily close to 1. Secondly, for LCS, obtaining similar approximation-time tradeoffs via deterministic algorithms would imply breakthrough circuit lower bounds [Chen, Goldwasser, Lyu, Rothblum, Rubinstein, 2019]; our randomized algorithm demonstrates derandomization hardness for LCS approximation.

<sup>∗</sup>Supported by NSF CAREER Award CCF-2337901. <sup>†</sup>Supported by NSF CAREER Award CCF-2337901.

Xiao Mao<sup>∗</sup> Stanford University <u>xiaomao@stanford.edu</u>

Aviad Rubinstein<sup>†</sup> Stanford University <u>aviad@stanford.edu</u>

April 1, 2026

