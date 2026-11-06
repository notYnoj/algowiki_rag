By pigeonhole principle, we can imply that at least one of the four terms on the left hand side of Inequality (7.4), approximates lcs(_s,<o>s</o>_) within a factor of 4. As we show in Section 7.1, the first three instances can be \(O(n^{1/2-\eta})\) approximated in time \(\tilde{O}(n)\). Using the method we describe in Section 7.1, Algorithm 2 finds an \(O(n^{1/2-\eta})\) approximation solution for each of the first three subproblems and selects the largest one. Let _t_ be the selected solution. The output of Algorithm 2 consists of three strings _t,s_<sub>H</sub>_,<o>s</o>_<sub>H</sub>. If

\(\mathrm{max}\left\{\begin{array}{ c }
|\mathsf{lcs}(s_\mathsf{L},\overline{s_\mathsf{L}})|, \\
|\mathsf{lcs}(s_\mathsf{L},\overline{s_\mathsf{H}})|, \\
|\mathsf{lcs}(s_\mathsf{H},\overline{s_\mathsf{L}})|, \\
|\mathsf{lcs}(s_\mathsf{H},\overline{s_\mathsf{H}})|
\end{array}\right\}\ge|\mathsf{lcs}(s,\overline{s})|/4\)

holds, then _t_ is an \(O(n^{1/2-\eta})\) approximation of lcs(_s,<o>s</o>_). Otherwise, due to Inequality (7.4), we have \(|\mathsf{lcs}(s_\mathsf{H},\overline{s_\mathsf{H}})|\ge|\mathsf{lcs}(s,\overline{s})|/4\). In addition, since each symbol in _s_<sub>H</sub> and <o>_s_</o><sub>H</sub> has a frequency of at least \(\tau=n^{1/2-\eta}\), the total number of different symbols in _s_<sub>H</sub>_,<o>s</o>_<sub>H</sub> is at most \(n/n^{1/2-\eta}=n^{1/2+\eta}\).

The result of this section is formally stated in Lemma 7.1.

Lemma 7.1. _Let t,s_<sub>H</sub>_,<o>s</o>_<sub>H</sub> _be the output of Algorithm 2 for input strings s and <o>s</o> and_ \(0\le\eta\le 1/2\) _be a fixed number. Then, either_ \(|\mathsf{lcs}(s_\mathsf{H},\overline{s_\mathsf{H}})|\ge|\mathsf{lcs}(s,\overline{s})|/4\) _holds, or t is an_ \(O(n^{1/2-\eta})\) _approximation solution. Also, s_<sub>H</sub> _and <o>s</o>_<sub>H</sub> _have at most_ \(n^{1/2+\eta}\) _symbols._

In the next section, we propose a random procedure to provide an \(O(n^{1/2-\eta})\) approximation solution for the first three subinstances.

## 7.1 Instances with Low Frequency Symbols.

We claim that for the first three subinstances on the left-hand side of Inequality (7.4), we can find an \(O(n^{1/2-\eta})\) approximation solution for LCS in near linear time. A character _s<sub>i</sub>_ matches a character <o>_s_</o><sub>j</sub>, if they have the same symbols. The key property of these subinstances is that the number of pairs that match in these subinstances is small, as we prove in Lemma 7.2.

Lemma 7.2. _Let r and <o>r</o> be two strings of size n, with the property that for every symbol c, we have_ \(\mathsf{fr}_c(r)\le\tau\) _and let_

\(R:=|\{(i,j)|r_i=\overline{r}_j\}|\)

_be the number of matching pairs of r and <o>r</o>. Then, we have_ \(R\le\tau n\).

**Proof.** Let _f<sub>i</sub>_ be the frequency of the _i_’th character of <o>_r_</o> in _r_. The total number of the matching pairs of _r_ and <o>_r_</o> is<tbc>

\(\sum_{1\le i\le|\overline{r}|}f_i.\)

<tbc>Since _r_ contains only symbols with frequency at most \(\tau\), \(f_i\le\tau\) holds for every \(1\le i\le|r|\). Furthermore, we have \(|\overline{r}|=n\), which implies

\(\sum_{i\le|r|}f_i\le\tau n.\)

