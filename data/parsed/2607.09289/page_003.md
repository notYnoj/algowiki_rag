<tbc>which gives _T=O_<sup>∗</sup>(3_<sup>n</sup>/S_<sup>2</sup>) for any space bound \(S\le O^*(3^{n/4})\) \[25, Appendix D, full version\], has remained the only general time-space tradeoff known for the problem. As our third result, we give an improved time-space tradeoff curve for ESS, improving the running time under a broad range of exponential-space bounds.

**Theorem 1.5.** _For every constant_ \(\alpha\) _satisfying_ \(0\le\alpha\le 1\)_, there is a Monte Carlo algorithm for ESS that runs in_ \(O^*(2^{\mathcal{T}(\alpha)n})\) _time and uses_ \(O^*(2^{\alpha n})\) _space, where_ \(\mathcal{T}(\alpha)\) _is defined in_ (8) _of Section 5.1._

In Fig. 1, we compare \(\mathcal{T}(\alpha)\) with the best bound previously obtainable for each space exponent \(\alpha\). This previous bound is obtained by taking the best among the Schroeppel–Shamir-type tradeoff, the polynomial-space \(O^*(2^{1.42312n})\le O^*(2.6817^n)\)-time algorithm of \[25\], and the \(O^*(2^{0.77117n})\le O^*(1.7067^n)\)-time and space algorithm of \[28\].

## 1.2 Our Main Techniques

The algorithms of \[25\] focus on the solution size \(\ell=|A|+|B|\), where _A_ and _B_ form a disjoint solution of ESS. They gave an algorithm that runs in \(O^*(2^\ell)\) time and space for \(\ell>n/2\), which is fast when \(\ell\) is small. In our algorithm, we introduce a simple random modification to the input instance; see Algorithm 1 in Section 3. This modification reduces the solution size \(\ell\) with inverse-exponential probability. Although we need to pay an additional exponential cost to successfully reduce \(\ell\), the exponential speedup obtained from the reduction in \(\ell\) dominates this cost in the bottleneck case \(\ell\approx 0.773n\) of \[25\]. Thus, by combining this input modification with the \(O^*(2^\ell)\)-time and space<tbc>

Comparison of time-space tradeoff curves
1.5
Our bound T(a) Previous best
1.42312
1.34651
1.25429
1.13083
time exponent
1
0.5log2 3 0.76502
0.7
0
a4
a3
0.25
0.25log2 3
0.5
a1
0.77117
1
space exponent a

Figure 1: For each constant \(\alpha\in[0,1]\), the figure plots the time exponent \(f(\alpha)\) of the running time \(O^*(2^{f(\alpha)n})\) achievable under the space bound \(O^*(2^{\alpha n})\). We compare our tradeoff curve \(\mathcal{T}(\alpha)\) with the previous best tradeoff curve. The blue solid curve represents our bound \(\mathcal{T}(\alpha)\), and the orange dotted curve represents the previous best bound. Here, \(\alpha_1\approx 0.64738\) is defined in (7), and \(\alpha_3\approx 0.18687\) and \(\alpha_4\approx 0.12286\) are defined in Section 5.1.

