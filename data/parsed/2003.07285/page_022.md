Since \(|\mathsf{lcs}(s,\overline{s})|\le n\), the approximation factor of Algorithm 4 is<tbc>

\(\tilde{\Omega}(n^{1/6+221/3\delta+34/3\zeta+10/3\eta}).\)

<tbc>Finally, we know that the approximation factor of Algorithm 3 is \(O(n^{1/2-\zeta})\). To optimize the better solution of Algorithms 3 and 4, we set<tbc>

\(1/6+221/3\delta+34/3\zeta+10/3\eta=1/2-\zeta\)<br>
\(1/2+221\delta+34\zeta+10\eta=3/2-3\zeta\)

<tbc>which implies<tbc>

\(\zeta=1/37-(221/37)\delta-(10/37)\eta.\)

<tbc>Therefore, the better solution returned by these two algorithms is an

\(\tilde{O}(n^{1/2-1/37+(221/37)\delta+(10/37)\eta})\)

approximation.

The remaining challenge is to prove the existence of _U_ and <o>_U_</o>, which we prove in the next section.

## 8.2.1 Rarus Blocks and Semi-permutations

We call a block rarus, if it belongs to a pair in \(\widetilde{U}_2\). Recall the property of the block pairs in \(\widetilde{U}_2\): for each pair \((b_i,\overline{b_j})\in\widetilde{U}_2\), the total number of the crebris characters <sup>4</sup> (i.e., a character that its corresponding symbol has frequency at least \(n^{4\delta+\zeta}\) in both _b<sub>i</sub>_ and <o>_b_</o><sub>j</sub>) in _b<sub>i</sub>_ is at most \(n^{1/2-2\delta}/4\). The rest of the characters in _b<sub>i</sub>_ are rarus. Since \(|\mathsf{lcs}(b_i,\overline{b_j})|\ge n^{1/2-\delta}/2\), at least

\(n^{1/2-\delta}/2-n^{1/2-2\delta}/4\ge n^{1/2-\delta}/4\) (8.8)

of the characters in lcs(_b<sub>i</sub>,<o>b</o><sub>j</sub>_) are rarus. By definition, rarus characters either have a frequency at most \(n^{4\delta+\zeta}\) in both the blocks, or have a frequency less than \(n^{4\delta+\zeta}\) in one block and at least \(n^{4\delta+\zeta}\) in the other one. We argue that at least half of the rarus characters have a frequency at most \(\tau=16n^{5\delta+\zeta}\) in both _b<sub>i</sub>_ and <o>_b_</o><sub>j</sub>. To prove this, consider the symbols with frequency more than \(\tau\) in _b<sub>i</sub>_ and <o>_b_</o><sub>j</sub>. Since \(|b_i|,|\overline{b_j}|\le n^{1/2}\), there are at most \(2n^{1/2}/(16n^{5\delta+\zeta})\) different symbols of this type in _b<sub>i</sub>_ and <o>_b_</o><sub>j</sub>. The contribution of each of these symbols to lcs(_b<sub>i</sub>,<o>b</o><sub>j</sub>_) is at most \(n^{4\delta+\zeta}\). Thus, the total contribution of these symbols to lcs(_b<sub>i</sub>,<o>b</o><sub>j</sub>_) is at most \(n^{1/2-\delta}/8\). By Inequality (8.8), the total contribution of rarus characters to lcs(_b<sub>i</sub>,<o>b</o><sub>j</sub>_) is at least \(n^{1/2-\delta}/4\). Therefore, at least

\(n^{1/2-\delta}/4-n^{1/2-\delta}/8=n^{1/2-\delta}/8\)

of the characters in lcs(_b<sub>i</sub>,<o>b</o><sub>j</sub>_) correspond to the rarus characters with frequency at most \(\tau\) in both _b<sub>i</sub>_ and <o>_b_</o><sub>j</sub>.

Consider a character _c_ in lcs(_b<sub>i</sub>,<o>b</o><sub>j</sub>_) where its corresponding characters in _s_ and <o>_s_</o> are rarus and have frequency at most \(\tau\). In the first step of Algorithm 4, we select one instance of each<tbc>

<sup>4</sup>We use rarus and crebris for both symbols and characters. Rarus (crib) characters are those whose corresponding symbols are rarus (crebris).

