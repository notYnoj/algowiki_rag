## APPENDIX I<br>
UPPER BOUNDS FOR ADAPTIVE SAMPLING

Here we present the tournament algorithm for computing OR introduced in (Feige et al., 1994). Similar algorithm can also be applied to compute MAX. The main difference is that in MAX, we directly compare two elements \(\lceil\frac{4(2i-1)\mathrm{log}(1/\delta)}{(1-H(p))}\rceil\) times instead of comparing their number of \(1'\)s.

**Algorithm 2** Tournament for computing OR with noise

1: **Input**: Target confidence level \(\delta\).

2: Set \(\mathcal{X}=(X_1,X_2,\cdots,X_K)\) as the list of all bits with unknown value.

3: **for** iteration \(i=1:\lceil\mathrm{log}_2(K)\rceil\) **do**

4: Query \(\lceil\frac{4(2i-1)\mathrm{log}(1/\delta)}{(1-H(p))}\rceil\) times each of the element in X.

5: **for** iteration \(j=1:\lceil\mathcal{X}|/2\rceil\) **do**

6: Compare the number of 1’s in the queries from the (2_j_-1)-th element and (2_j_)-th element, remove the element with smaller number of 1’s from the list X. Ties are broken arbitrarily. (If the (2_j_)-th element does not exist, we will not remove the (2_j_-1)-th element.)

7: Break when X only has one element left.

8: Query \(\lceil\frac{6\mathrm{log}(1/\delta)}{(1-H(p))}\rceil\) times the only left element in X. Return 1 if there is more than half 1’s, and 0 otherwise.

The following theorem is due to (Feige et al., 1994). We include it here for completeness.

**Theorem I.1.** _Algorithm 2 finishes within_ \(C\cdot K\mathrm{log}(1/\delta)/(1-H(p))\) _queries, and outputs the correct value of_ \(\mathrm{OR}(X_1,\cdots,X_K)\) _with probability at least_ \(1-2\delta\) _when_ \(\delta<1/2\).

_Proof._ First, we compute the total number of queries of the algorithm. Without loss of generality, we may assume that _K_ can be written as 2_<sup>m</sup>_ for some integer _m_. If not we may add no more than _K_ extra dummy 0’s to the original list X to make sure _K_=2_<sup>m</sup>_. In each of the outer iteration _i_, the size of X is decreased half. We know that after \(\lceil\mathrm{log}_2(K)\rceil\) round, the set X will only contain one element. In round _i_, the number of queries we make for each element is \(\lceil\frac{4(2i-1)\mathrm{log}(1/\delta)}{(1-2p)^2}\rceil\). The total number of queries we make is

\(\left\lceil\frac{4\mathrm{log}(1/\delta)}{(1-2p)^2}\right\rceil+\sum_{i=1}^{\lceil\mathrm{log}_2(K)\rceil}\left\lceil\frac{4(2i-1)\mathrm{log}(1/\delta)}{(1-2p)^2}\right\rceil\cdot\frac{K}{2^{i-1}}\)<br>
\(\le\left\lceil\frac{4\mathrm{log}(1/\delta)}{(1-2p)^2}\right\rceil+\sum_{i=1}^{\lceil\mathrm{log}_2(K)\rceil}\left(\frac{4(2i-1)\mathrm{log}(1/\delta)}{(1-2p)^2}+1\right)\cdot\frac{K}{2^{i-1}}\)<br>
\(\le\left\lceil\frac{4\mathrm{log}(1/\delta)}{(1-2p)^2}\right\rceil+2K+\frac{K\mathrm{log}(1/\delta)}{(1-2p)^2}\sum_{i=1}^{\lceil\mathrm{log}_2(K)\rceil}\frac{4(2i-1)}{2^{i-1}}\)<br>
\(\le\left\lceil\frac{4\mathrm{log}(1/\delta)}{(1-2p)^2}\right\rceil+2K+\frac{28K\mathrm{log}(1/\delta)}{(1-2p)^2}\)<br>
\(\le\frac{CK\mathrm{log}(1/\delta)}{1-H(p)}\)

Here in last inequality we use the fact below, which can be verified numerically:

\(\forall p\in[0,1],\frac{(1/2-p)^2}{1-H(p)}\in[1/4,1/2].\) (4)

Now we show that the failure probability of the algorithm is at most \(\delta\). Consider the first case where all the elements are 0. Then no matter which element is left in X, the probability that the algorithm fails is the probability that a Binomial random variable _X∼B(n,np_) has value larger or equal to _n/_2 with \(n=\left\lceil\frac{4\mathrm{log}(1/\delta)}{(1-2p)^2}\right\rceil\).

