\(\text{maximize}\nu\text{subject to}\nu\le 1/2-\eta\nu\le 1/2-\delta/2\nu\le 1/2-1/37+(221/37)\delta+(10/37)\eta 0\le\delta\le 1-0.5\le\eta\le 0.5\text{(5.2)}\)

which is maximized for \(\nu\simeq 0.497956\), \(\delta\simeq 0.004090\), and \(\eta\simeq 0.002045\). This gives us the main contribution of our work.

Theorem 5.1. _There exists a linear time algorithm that approximates LCS within a factor O(n_<sup>0.497956</sup>) _(in expectation)._

**Proof.** The details are shown in Figure 4. Here we just mention that 0.497956 is strictly more than the optimal solution of LP 5.2 and therefore we can ignore all the polylogarithmic factors in the approximation factor. In addition to this, a polylogarithmic factor in the running time can be handled by sampling each character of the input by a polylogarithmic rate and reducing the input size by any polylogarithmic factor. This only hurts the solution size by a polylogarithmic factor.

## 6 Algorithm 1: Lower Bound on the Solution Size

In the first step, we show that the instances with small solution sizes can be approximated well in linear time. Consider two strings _s_ and <o>_s_</o> such that \(|\mathsf{lcs}(s,\overline{s})|\le n^{1-\delta}\) for a constant \(\delta>0\). We argue that for such instances, Algorithm 1 returns an \(O(n^{(1-\delta)/2})\)-approximate solution. Algorithm 1 is essentially a modified variant of Algorithm 0 which is tuned to work well for instances with low solution size. The precondition and guarantee of Algorithm 1 are given below.

Let _s_ and <o>_s_</o> be the inputs to Algorithm 1, with the assumption that \(|\mathsf{lcs}(s,\overline{s})|\le n^{1-\delta}\). Algorithm 1 constructs a string _s_<sup>∗</sup> from _s_ by sampling each character of _s_ with probability \(n^{-(1-\delta)/2}\). More precisely, _s_<sup>∗</sup> is a substring of _s_, where each character of _s_ is removed from _s_<sup>∗</sup> with probability \(1-n^{-(1-\delta)/2}\). After sampling _s_<sup>∗</sup>, Algorithm 1 returns lcs(_s_<sup>∗</sup>_,<o>s</o>_) as an approximation of lcs(_s,<o>s</o>_). In this section, we analyze Algorithm 1 in details.

First, let us determine the expected size of _s_<sup>∗</sup> and lcs(_s_<sup>∗</sup>_,<o>s</o>_). Since each character of _s_ appears in _s_<sup>∗</sup> with probability \(n^{-(1-\delta)/2}\), and |_s_|=_n_, we have<tbc>

\(\mathbb{E}(|s^*|)=n\cdot n^{-(1-\delta)/2}=n^{(1+\delta)/2}.\)

<tbc>Furthermore, for each character in lcs(_s,<o>s</o>_), its corresponding character in _s_ is also appeared in _s_<sup>∗</sup> with probability \(n^{-(1-\delta)/2}\). Therefore, we have<tbc>

\(\mathbb{E}(|\mathsf{lcs}(s^*,\overline{s})|)\ge|\mathsf{lcs}(s,\overline{s})|n^{-(1-\delta)/2}.\)

Inputs: s and <o>s</o>.
Precondition:
Approximation factor: O(n 1/2- /

