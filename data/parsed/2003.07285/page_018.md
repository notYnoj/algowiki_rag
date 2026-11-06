where rem(_j_) is the number of indices \(j'>j\) with \(\overline{s_{j^\prime}}=\overline{s_j}\), which can be computed using \(\overline{F_{\overline{s_j}}}\):

\(\mathsf{rem}(\mathsf{j})=|\overline{F_{\overline{s_j}}}|-l\)

where _l_ is the index of \(\overline{F_{\overline{s_j}}}\) that \(\overline{F_{\overline{s_j}}}=j\). After finding \(i'\), using \(\overline{F_{s_{i^\prime}}}\) we can find the pair \((i',j')\) which is the \(k'\)’th pair.

Lemma 7.3. _Let r and <o>r</o> be two strings of size n, with the property that the number of matching pairs of s and <o>s</o> is_ \(O(n^{3/2-\eta})\)_. Then, by setting_ \(\alpha=R/n\) _Algorithm 5 returns an_ \(O(n^{1/2-\eta})\) _approximation of lcs(s,<o>s</o>_) _in time O(n)._

**Proof.** The expected length of the longest increasing subsequence of _M_<sup>∗</sup> is at least \(|\mathsf{lcs}(s,\overline{s})|/2\alpha\ge|\mathsf{lcs}(s,\overline{s})|/2n^{1/2-\eta}\). Hence, Algorithm 5 outputs an \(O(n^{1/2-\eta})\) approximation of lcs(_s,<o>s</o>_) in linear time.

## 8 Algorithms 3 and 4: Decomposition into Blocks and Permutations

The last step of our algorithm is technically more involved as we perform two separate algorithms and argue that the better of the two algorithms gives us a desirable solution for a class of inputs.

Formally, during this section, we analyze Algorithm 6, which takes _s_ and <o>_s_</o> as input and runs both Algorithms 3 and 4 on the input and returns the better solution. Algorithm 6 assumes that the input satisfies two conditions: first, the solution size is at least \(n^{1-\delta}\), and second, the number of different symbols in _s_ and <o>_s_</o> is at most \(n^{1/2+\eta}\), i.e., \(|\Sigma|\le n^{1/2+\eta}\). In this section, we first analyze Algorithm 3, and characterize the conditions under which Algorithm 3 provides the desirable approximation guarantee. Next, we show that the inputs that do not satisfy these conditions can be approximated well by Algorithm 4. The main argument of this section is formally stated in Lemma 8.1.

Lemma 8.1. _For two strings s and <o>s</o> with the properties that_ \(|\mathsf{lcs}(s,\overline{s})|\ge n^{1-\delta}\) _and_ \(|\Sigma|\le n^{1/2+\eta}\)_, Algorithm 6 returns an_ \(\tilde{O}(n^{1/2-1/37+(221/37)\delta+(10/37)\eta})\) _approximation solution for lcs(s,<o>s</o>)._

Throughout this section, we use Observation 8.1 several times. Observation 8.1 is a simple consequence of Pigeonhole principle.

Algorithm 3:
Algorithm 4:
Inputs: s and <o>s</o>.
Inputs: s and <o>s</o>.
Precondition
Precondition
• |lcs(s, <o>s</o>)| 2 n 1-δ
• |lcs(s, <o>s</o>)| 2 n 1-δ
• m < n 1/2+η
• m < n 1/2+η
The approximation factor of the better solution returned by Algorithms 3 and 4:
O(n 1/2-1/37+(221/37)δ+(10/37)η).

