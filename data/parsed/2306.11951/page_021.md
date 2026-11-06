## B. Upper Bounds

Now it suffices to prove the upper bounds. For OR and MAX, we already know from Theorem I.1 that \(\mathcal{O}(K\mathrm{log}(1/\delta)/(1-H(p)))\) is an upper bound for fixed-length setting when comparing two elements with error probability at most \(\delta\) requires \(\lceil C\mathrm{log}(1/\delta)/(1-H(p))\rceil\) samples for some constant _C_. Now for variable-length setting, we know that comparing two elements with error probability at most \(\delta\) only requires \(\mathrm{log}(1/\delta)/D_\mathrm{KL}(p\|1-p)+1/(1-2p)\) queries in expectation via the variable-length comparison algorithm in Lemma 13 of Gu and Xu (2023). Thus in Algorithm 1, we replace the repetition-based comparisons in Algorithm 2 with the new variable- length comparison algorithm. This gives the query complexity \(\mathcal{O}(K/(1-H(p))+K\mathrm{log}(1/\delta)/D_\mathrm{KL}(p\|1-p))\). Similar algorithm can also be applied to compute MAX . The main difference is that in MAX, we directly compare two elements instead of finding the number of \(1'\)s of the first element.

**Theorem J.1.** _The expected number of total queries made by Algorithm 1 is upper bounded by_ \(C\cdot\big(\frac{K}{1-H(p)}+\frac{K\mathrm{log}(1/\delta)}{D_\mathrm{KL}(p\|1-p)}\big)\)_. Furthermore, the algorithm outputs the correct value of_ \(\mathsf{OR}(X_1,\cdots,X_K)\) _with probability at least_ \(1-2\delta\) _when_ \(\delta<1/2\).

_Proof._ First, we compute the total number of queries of the algorithm. Without loss of generality, we may assume that _K_ can be written as 2_<sup>m</sup>_ for some integer _m_. If not we may add no more than _K_ extra dummy 0’s to the original list X to make sure _K_=2_<sup>m</sup>_. In each of the outer iteration _i_, the size of X is decreased half. We know that after \(\lceil\mathrm{log}_2(K)\rceil\) iterations, the set X will only contain one element. From Lemma 27 in Gu and Xu (2023), the expected number of queries we make is \(\mathcal{O}(\mathrm{log}(1/\tilde{\delta}_i)/D_\mathrm{KL}(p\|1-p)+1/(1-2p))\) at round _i_. Thus the total number of queries we make is

\(\frac{\mathrm{log}(1/\delta)}{D_\mathrm{KL}(p\|1-p)}+\frac{1}{1-2p}+C\cdot\sum_{i=1}^{\lceil\mathrm{log}_2(K)\rceil}\left(\frac{\mathrm{log}(1/\tilde{\delta}_i)}{D_\mathrm{KL}(p\|1-p)}+\frac{1}{1-2p}\right)\cdot\frac{K}{2^{i-1}}\)<br>
\(\le C\cdot\sum_{i=1}^{\lceil\mathrm{log}_2(K)\rceil}\left(\frac{(4i-2)\mathrm{log}(1/\delta)}{D_\mathrm{KL}(p\|1-p)}+\frac{1}{1-2p}\right)\cdot\frac{K}{2^{i-1}}\)<br>
\(\le C\cdot\left(\frac{K}{1-2p}+\frac{K\mathrm{log}(1/\delta)}{D_\mathrm{KL}(p\|1-p)}\cdot\sum_{i=1}^{\lceil\mathrm{log}_2(K)\rceil}\frac{4(2i-1)}{2^{i-1}}\right)\)<br>
\(\le C\cdot\left(\frac{K}{1-2p}+\frac{K\mathrm{log}(1/\delta)}{D_\mathrm{KL}(p\|1-p)}\right)\)<br>
\(\le C\cdot\left(\frac{K}{1-H(p)}+\frac{K\mathrm{log}(1/\delta)}{D_\mathrm{KL}(p\|1-p)}\right).\)

Here in last inequality we use the fact below, which can be verified numerically:

\(\forall p\in[0,1],\frac{(1/2-p)^2}{1-H(p)}\in[1/4,1/2].\) (5)

Now we show that the failure probability of the algorithm is at most \(\delta\). Consider the first case where all the elements are 0. Then no matter which element is left in X, the probability that the algorithm fails is the probability that the last while loop gives wrong output. From Lemma 27 in Gu and Xu (2023), we know that such probability is less than \(\delta\).

Consider the second case where there exists at least a 1 in the original elements \(X_1,\cdots,X_K\). Without loss of generality, we assume that _X_<sub>1</sub>=1. Let X_<sup>i</sup>_ be the remaining list of elements at the beginning of _i_-th iteration. We let E_<sub>i</sub>_ be the event that the first element in X_<sup>i</sup>_ is 1 while the first element in X<sup>_i_+1</sup> is 0. This event only happens when the while loop ends with \(a<\tilde{\delta}_i\) for the first element at the _i_-th round. Let A denote the event

