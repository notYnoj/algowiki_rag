The first sum is _d_<sub>0</sub>, and the second satisfies

\(\sum_{d=d_0}^\infty\frac{A}{B^d}\le\sum_{d=d_0}^\infty B^{d_0-d}=\sum_{k=0}^\infty B^{-k}=\frac{1}{1-B^{-1}}=\frac{B}{B-1}.\)

Thus

\(\mathbb{E}[D]\le d_0+\frac{B}{B-1}.\)

Substituting the definition of _d_<sub>0</sub>, we obtain

\(\mathbb{E}[D]\le max\left\{0,\left\lceil log_B\left(\frac{nM}{T}\right)\right\rceil\right\}+\frac{B}{B-1}.\)

Since _M_, _T_, and _B_ are fixed constants independent of _n_, this implies

\(\mathbb{E}[D]=\mathcal{O}(logn).\)

□

We now apply the theorem to several typical input distributions. These examples are meant to illustrate the scale of the bound, rather than to precisely model every possible input.

Assume that the input values lie in the interval

\[_a,b_\]=[0,10000],

and suppose that each recursive distribution step uses

\(B=2000\)

buckets. We stop recursion once a bucket contains at most

\(T=10\)

elements, and we consider an input size of

\(n=1,000,000.\)

The theorem gives

\(\mathbb{E}[D]\le max\left\{0,\left\lceil log_{2000}\left(\frac{nM}{T}\right)\right\rceil\right\}+\frac{2000}{1999},\)

where

\(M=(b-a)\|f\|_\infty.\)

Since _n/T_=100,000, this becomes

\(\mathbb{E}[D]\le\left\lceil log_{2000}(100,000M)\right\rceil+\frac{2000}{1999}.\)

For a uniform distribution on [0,10000], we have

\(f(x)=\frac{1}{10000},\)

so

\(M=10000\cdot\frac{1}{10000}=1.\)

Therefore,

\(\mathbb{E}[D]\le\left\lceil log_{2000}(100,000)\right\rceil+\frac{2000}{1999}=2+\frac{2000}{1999}\approx 3.00.\)

Thus, for a uniform input of one million elements, the theorem predicts that only a small number of recursive levels are needed on average.

Next consider a normal distribution centered at 5000, with most values lying within roughly 500 units of the mean. For example, we may take

\(X\sim\mathcal{N}(5000,250^2),\)

so that about 95% of the mass lies within 500 units of the mean. The maximum density occurs at the mean, so

\(\|f\|_\infty=\frac{1}{250\sqrt{2\pi}}.\)

Hence

\(M=10000\cdot\frac{1}{250\sqrt{2\pi}}\approx 15.96.\)

The theorem gives

\(\mathbb{E}[D]\le\left\lceil log_{2000}(100,000\cdot 15.96)\right\rceil+\frac{2000}{1999}=2+\frac{2000}{1999}\approx 3.00.\)

Even though the distribution is much more concentrated than the uniform distribution, the expected depth bound remains very small.

As another example, consider an exponential distribution on [0,10000]. If we use a truncated exponential distribution with rate

\(\lambda=\frac{1}{1000},\)

then its density is

\(f(x)=\frac{\lambda e^{-\lambda x}}{1-e^{-10000\lambda}},0\le x\le 10000.\)

The maximum occurs at _x_=0, so

\(\|f\|_\infty=\frac{\lambda}{1-e^{-10000\lambda}}.\)

Therefore,

\(M=10000\cdot\frac{1/1000}{1-e^{-10}}\approx 10.00.\)

The theorem gives

\(\mathbb{E}[D]\le\left\lceil log_{2000}(100,000\cdot 10.00)\right\rceil+\frac{2000}{1999}=2+\frac{2000}{1999}\approx 3.00.\)

We also consider a more concentrated mixture distribution. This example is useful because it is less favorable to distribution sorting than the previous smooth distributions: most of the input lies in a narrow interval, while a small fraction of values are spread across the full range.

Suppose that each element is drawn from the following mixture:

\(X\sim\left\{\begin{array}{ c c }
Unif([4999,5001]), & \text{with probability}0.99, \\
Unif([0,10000]), & \text{with probability}0.01.
\end{array}\right.\)

The density is therefore

\(f(x)=0.99\cdot\frac{1}{2}\mathbf{1}_{[4999,5001]}(x)+0.01\cdot\frac{1}{10000}\mathbf{1}_{[0,10000]}(x).\)

The maximum density occurs inside the narrow interval [4999, 5001], where both mixture components contribute. Hence

\(\|f\|_\infty=\frac{0.99}{2}+\frac{0.01}{10000}=0.495001.\)

Thus

\(M=10000\|f\|_\infty=4950.01.\)

The theorem gives

\(\mathbb{E}[D]\le\left\lceil log_{2000}(100,000\cdot 4950.01)\right\rceil+\frac{2000}{1999}=3+\frac{2000}{1999}\approx 4.00.\)

This is larger than in the uniform, normal, and exponential examples, but still quite small. The increase is expected: the high-density interval contains many more elements per unit length, so the cardinalities of buckets intersecting that interval shrink more slowly across recursive levels. Nevertheless, because each recursive step

