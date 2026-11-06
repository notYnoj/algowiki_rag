### 3.2 Mapping Between Spaces

Now we have defined a set of allowed orderings of the random variables as _S_ whose elements _s_ identify regions \(R_s\subset C\) and \(R'_s\subset C'\). Once we have our uniformly sampled point \((u_1,\cdots,u_N)\) from _C_, we use the above definition of the regions to determine which _R<sub>s</sub>_ our point falls into. Once we know this _s_, we can use the following mapping to translate the point into \(C'\) coordinates \((u'_1,\cdots,u'_N)\). For coordinate index _j_ and region index _s_=(_s<sub>A</sub>,s<sub>B</sub>_), we have the mapping

\(u'_j=g_s(u_j)=\left\{\begin{array}{ c c }
(b_j-a_j)u_j+a_j & \text{if}j\in s_A\cap s_B,j<N \\
\frac{b_j-a_j}{f_s}(u_j-\sum_{l=1}^{s-1}f_l)+a_j & \text{if}j\in s_A\cap s_B,j=N \\
(1-b_j)u_j+b_j & \text{if}j\in s_A\backslash s_B,j<N \\
\frac{1-b_j}{f_s}(u_j-\sum_{l=1}^{s-1}f_l)+b_j & \text{if}j\in s_A\backslash s_B,j=N \\
a_ju_j & \text{if}j\in s_B\backslash s_A,j<N \\
\frac{a_j}{f_s}(u_j-\sum_{l=1}^{s-1}f_l) & \text{if}j\in s_B\backslash s_A,j=N
\end{array}\right.\)

After performing this mapping on each of the _N_ coordinates in our original sampled point, we obtain \((u'_1,\cdots,u'_N)\). Using the inverse CDFs, we can use these coordinates to obtain samples from the _X<sub>i</sub>_: \((F_{X_1}^{-1}(u'_1),\cdots,F_{X_N}^{-1}(u'_N))\). Then our final answer is the _k_-th largest of these values, which due to our procedure is guaranteed to be between _A_ and _B_ without biasing the distribution.

## 4 Simulation

We can demonstrate the validity and computational speed of the above method by simulating draws in R.<sup>1</sup> For the following simulations, we choose _N_=5 and _k_=3, and we use the following probability distributions for the individual _X<sub>i</sub>_:

\(\bullet X_1\sim\text{Cauchy}(x_0=5,\gamma=1)\)

\(\bullet X_2\sim\text{Normal}(\mu=6,\sigma=2)\)

\(\bullet X_3\sim\text{Logistic}(\mu=3,s=2)\)

\(\bullet X_4\sim\text{Weibull}(\lambda=10,k=1.5)\)

<sup>1</sup>R code for performing these procedures is available upon request.

