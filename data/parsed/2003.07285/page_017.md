Since each of the instances (_s_<sub>L</sub>,<o>s</o><sub>L</sub>),(_s_<sub>L</sub>,<o>s</o><sub>H</sub>), and (_s_<sub>H</sub>,<o>s</o><sub>L</sub>) contains at least one string with low frequency characters, the total number of the matching pairs in each instance is upper bounded by \(n^{3/2-\eta}\). Now, we show that we can find an \(O(n^{1/2-\eta})\) approximation solution for these instances in time \(\tilde{O}(n)\). First, we start by stating that a near-linear time algorithm can exactly compute LCS in time \(\tilde{O}(n+R)\).

Theorem 7.1. (Apostolico and Guerra \[6\]) _Let r and_ \(\overline{r}\) _be two strings of size n, and let_

\(R:=|\{(i,j)|r_i=\overline{r}_j\}|\)

_be the number of matching pairs in r and_ \(\overline{r}\)_. Then, we can compute_ \(\mathsf{lcs}(r,\overline{r})\) _in time_ \(\tilde{O}(n+R)\).

**Proof.** Let _M_ be an array of size _R_, where each element of _M_ is a pair of indices that corresponds to a matching pair. In addition, suppose that the elements in _M_ are sorted according to the following rule:

\((i,j)<(i',j')\Longleftrightarrow i<i'\text{or}(i=i'\text{and}j<j').\) (7.5)

It can be easily observed that finding the longest common subsequence of _s_ and <o>_s_</o> is equivalent to finding the longest subsequence of _M_ that is increasing in terms of both the elements of each pair, which can be found in time \(O(n+RlogR)=\tilde{O}(n+R)\) \[22\].

Based on the method proposed in Theorem 7.1, we present Algorithm 5 which is an \(\widetilde{O}(n+R/\alpha)\) time algorithm with an approximation factor of \(\alpha\). Suppose that the input to Algorithm 5 are two strings \(r,\overline{r}\) of sizes _n_ and let _R_ be the number of matches in \((r,\overline{r})\). Recall the definition of _M_ in the proof of Theorem 7.1. Algorithm 5 constructs an array _M_<sup>∗</sup> where every pair of _M_ is in _M_<sup>∗</sup> with probability \(1/\alpha\). The expected size of _M_<sup>∗</sup> is \(R/\alpha\) and since each pair appears in _M_<sup>∗</sup> with probability \(1/\alpha\), the expected size of the longest increasing subsequence of _M_<sup>∗</sup> is at least \(|\mathsf{lcs}(r,\overline{r})|/\alpha\) which approximates\(\mathsf{lcs}(r,\overline{r})\) with a factor of \(\alpha\). Notice that, when \(R=O(n^{3/2-\eta})\), choosing \(\alpha=n^{1/2-\eta}\) results in expected running time \(\tilde{O}(n)\) and expected approximation factor \(n^{1/2-\eta}\).

The only challenge here is that the size of _M_ is large, and we cannot construct _M_ before constructing _M_<sup>∗</sup>. We argue that we can construct _M_<sup>∗</sup> in time \(\tilde{O}(R/\alpha)\) from _r_ and \(\overline{r}\). To do so, we use Observation 7.1.

Observation 7.1. _Let P be a probability distribution over_ {0,1}_, with_ \(P(0)=\alpha\) _and_ \(P(1)=1-\alpha\)_, and let x_<sub>1</sub>_,x_<sub>2</sub>_,...,x<sub>n</sub> be n random variables sampled independently from P. For every i, define next(i_) _as the minimum index j, such that j\>i and x<sub>j</sub>_=1_. Then, the distribution of next(i_) _for every i is a geometric distribution with parameter_ \(\alpha\).

Based on Observation 7.1, we iteratively sample the index of the next element of _M_<sup>∗</sup> in _M_ using a geometric distribution with parameter \(\alpha\) which determines its distance to the currently selected index. Next, for every sampled number _i_, we find the _i_’th matching pair of _M_. Note that to find the _i_’th matching pair of _M_, we do not need to explicitly access _M_; we can find it in amortized time _O_(1) using a data structure of size _O(n_), which for every symbol _c_ stores an array <o>_F_</o><sub>c</sub> of size \(\mathsf{fr}_c(\overline{r})\) containing the occurrence indices of _c_ in <o>_s_</o>. More precisely, suppose that the last selected pair is (_i,j_) which is the _k_’th matching pair in _M_ and \(next(k)=k'\). Then, we find the least index \(i'\ge i\), such that<tbc>

\(\mathsf{rem}(j)+\sum_{i<l\le i^\prime}\mathsf{fr}_{s_l}(\overline{r})\ge k'-k\)

