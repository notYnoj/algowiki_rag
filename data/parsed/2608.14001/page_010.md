## C. Non-Uniformly-Sampled Takens’ Embedding Theorem

If Conjecture 1 is true, we can establish two theorems about delay-coordinate maps consisting of non-uniformly-sampled time delays. Just as Theorem 2 establishes the _existence_ of a stable embedding for a delay-coordinate map with evenly-<tbc>

<tbc>spaced lags for linear dynamical systems, so too can we establish the _existence_ of a stable embedding for delay-coordinate maps of non-uniformly-spaced lags in the following theorem.

_Theorem 7:_ (Linear Takens’ Embedding with Non-Uniform Sampling) Consider a linear dynamical system of class A(_d_) in R_<sup>n</sup>_ in steady-state. Let \(\{\tau_k\}_{k=1}^\ell>0\) be distinct times, \(\mathbf{h}\in\mathbb{R}^n\) be the observation function, and \(\unknown\) the delay-coordinate map as in (8). Suppose that \(\ell\ge 2d\), the \(\mathcal{A}_\unknown\)-eigenvalues \(\{e^{\pm i\theta_j\tau_k}\}\) are distinct and purely imaginary, and \(\mathbf{v}_j^H\mathbf{h}\neq 0\) for all \(j\in\{1,\dots,d\}\). Then, for all distinct pairs of points \(\mathbf{x}_1,\mathbf{x}_2\in\mathcal{M}\), with probability one \(\unknown\) satisfies (4) for some constants _C_ and \(\delta<1\).

_Proof:_ If Conjecture 1 is true, then the result follows from a nearly identical approach to the proof of Theorem III.1 of \[6\]. In particular, provided \(\mathrm{rank}(\mathbf{T})=\mathrm{min}\{\ell,2d\}\), then for \(\ell\ge 2d\), rank(**T**)=2_d_, and, provided rank(**H**)=2_d_, then rank(**G**)=2_d_. This is because \(\mathrm{rank}(\mathbf{G})=\mathrm{rank}(\mathbf{H})-\mathrm{dim}(\mathcal{N}(\mathbf{T})\cap\mathcal{R}(\mathbf{H}))\), where N(**T**) denotes the null-space of **T** and R(**H**) is the range of **H**; when rank(**H**)=2_d_, R(**H**) is all of R_<sup>d</sup>_, and when rank(**T**)=2_d_, N(**T**) is empty, leading to rank(**G**)=2_d_. Thus, when \(\ell\ge 2d\), the entire attractor M is embedded into the delay-coordinate space by \(\unknown\).

Likewise, Theorem 3, which provides explicit enveloping bounds and long-term asymptotic bounds for the stability of linear delay-coordinate maps with uniformly-spaced time- delays (3), can be extended partially to the setting of delay- coordinate maps with non-uniformly-spaced delays (8). Due to the unevenly-sampled delay structure of generalized Vandermonde matrices **T**, it is unknown whether explicit enveloping upper and lower bounds on the embedding quality can be derived. What is possible is to capture the asymptotic bounds<tbc>

Regular
Uniform Dist.
100
l = 1m
l = 1m
l = 2m
l = 2m
l = 4m
l = 4m
l = 8m
50
l = 8m
l = 8m
0
Exp. Dist.
Normal Dist.
Rank of T
100
l = 1m
l = 1m
l = 2m
l = 2m
l = 4m
l = 4m
l = 8m
50
l = 8m
l = 8m
0
0
50
100
0
50
100
Number of Spatial Points [m]
Upper Bound: 1

Regular
Uniform Dist.
l = 1m
l = 1m
1.1
l = 2m
l = 2m
l = 4m
l = 4m
l = 8m
Pseudo-Finite Diameter [d m
1.0
l = 8m
0.9
Exp. Dist.
Normal Dist.
l = 1m
l = 1m
l = 1m
1.1
l = 2m
l = 2m
l = 4m
l = 4m
l = 8m
l = 8m
1.0
l = 8m
0.9
0
50
100
0
50
100
Number of Spatial Points [m]
Upper Bound: m 1/(m - 1)
Lower Bound: 1

Regular
Uniform Dist.
1.10
l = 1m
l = 1m
l = 2m
l = 2m
l = 4m
l = 4m
l = 8m
1.05
l = 8m
l = 8m
Condition Number of T [k(T)
1.00
Exp. Dist.
Normal Dist.
1.10
l = 1m
l = 1m
l = 2m
l = 2m
l = 4m
l = 4m
l = 8m
1.05
l = 8m
l = 8m
l = 8m
1.00
0
50
100
0
50
100
Number of Spatial Points [m]
Empirical Upper Bound: (1+ E 1/(m(m - 1)), E 1
Lower Bound: 1

Fig. 2. The rank of generalized Vandermonde matrix (14) in relation to number of frequencies _m_. As \(\ell\rightarrow\infty\), **T** is full rank. For small \(\ell\), the normal and exponential distributions exhibit a slight deviation from full rank, likely a numerical artifact from the severely ill-posed nature of Vandermonde matrices.

Fig. 3. The scaled determinant (19) of the generalized Vandermonde matrix (14) is shown for different ratios of the number of lags to the number of sample points. In each case when \(\ell=m\), whether the sampling is deterministic or random, the determinant is less than 1, and its value drops suddenly around _m_=60, most likely due to a numerical artifact stemming from the ill-posed nature of Vandermonde matrices. Around \(\ell=2m\), the determinant tends to oscillate around and converge towards 1 as _m_ increases, especially for the uniformly and exponentially-distributed sampling schemes. When \(\ell\gg m\), all the distributions have a scaled determinant greater than 1 that, in the limit as \(m\rightarrow\infty\), converge to 1.

Fig. 4. The scaled condition number of the generalized Vandermonde matrix (14). Increasing \(\ell/m\) correlates with the scaled condition number for generalized Vandermonde matrices converging to 1 faster in the deterministic case, and for random cases using uniform, normal, and exponential distributions. The upper bound for the condition number (40) is empirically determined by finding a suitable \(\varepsilon\), which in this case is \(\varepsilon=1-10^{-9}\). Decreasing \(\varepsilon\) by orders of magnitude generates tighter bounds for higher \(\ell/m\) ratios.

