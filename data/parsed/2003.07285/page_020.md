**Proof.** Let \(\alpha_i\) and \(\beta_i\) be the block numbers that the _i_’th character of lcs(_s,<o>s</o>_) belongs to in _s_ and <o>_s_</o>, respectively, and let _U_ be a multi-set containing pairs \((\alpha_i,\beta_i)\). We know both the sequences \(\alpha_1,\alpha_2,\dots,\alpha_{|\text{lcs}(s,\overline{s})|}\) and \(\beta_1,\beta_2,\dots,\beta_{|\text{lcs}(s,\overline{s})|}\) are non-decreasing. Thus, if for some _j_, \((\alpha_j,\beta_j)\neq(\alpha_{j+1},\beta_{j+1})\), at least one of the following two inequalities holds:

\(\alpha_{j+1}>\alpha_j\text{or}\beta_{j+1}>\beta_j.\)

As a result, the total number of different pairs in _U_ is at most \(2\sqrt{n}\), and since the size of a block is \(\sqrt{n}\), each pair appears no more than \(\sqrt{n}\) times in _U_. Since \(|U|\ge n^{1-\delta}\), by Observation 8.1 we can find at least \(n^{1/2-\delta}\) different pairs which appear at least \(n^{1/2-\delta}/2\) times in _U_. Let \(\widetilde{U}\) be the set of these pairs. A pair \((\alpha_i,\beta_i)\) collides with a pair \((\alpha_j,\beta_j)\), if \(\alpha_i=\alpha_j\) or \(\beta_i=\beta_j\). Since the size of each block in _s_ and <o>_s_</o> is \(\sqrt{n}\) and each pair of \(\widetilde{U}\) appears at least \(n^{1/2-\delta}/2\) times in _U_, no pair \((\alpha_i,\beta_i)\) in \(\widetilde{U}\) can collide with more than \(4n^\delta\) other pairs in \(\widetilde{U}\). Otherwise, at least one of \(b_{\alpha_i}\) or \(\overline{b_{\beta_i}}\) must have a size more than _n_<sup>1/2</sup>. Hence, \(\widetilde{U}\) contains at least \(n^{1/2-2\delta}/8\) collision-free pairs. Each one of these pairs corresponds to a pair of blocks in _s_ and <o>_s_</o> with the desired property.

Let \(\widetilde{U}\) be the set of _l_ block pairs mentioned in Lemma 8.2. Now, we partition these block pairs into two types. A symbol _c_ is crebris in block pair \((b_i,\overline{b_j})\), if<tbc>

\(min\{\text{fr}_c(b_i),\text{fr}_c(\overline{b_j})\}\ge n^{4\delta+\zeta},\)

<tbc>and is rarus, otherwise. A pair \((b_i,\overline{b_j})\in\widetilde{U}\) approximately consists of crebris symbols, if<tbc>

\(\sum_{c\in C}\text{fr}_c(b_i)\ge n^{1/2-2\delta}/4,\)

<tbc>where, _C_ is the set of crebris symbols of \((b_i,\overline{b_j})\). The intuition behind this definition is as follows: if a pair \((b_i,\overline{b_j})\) approximately consists of crebris characters, when we select a random positions of _b<sub>i</sub>_ to fill _T_\[_i_\]\[_j_\], with probability at least

\(n^{1/2-2\delta}/4n^{1/2}=n^{-2\delta}/4,\)

we have \(T[i][j]\ge n^{4\delta+\zeta}\). Now, let \(\widetilde{U}_1\) be the set of pairs in \(\widetilde{U}\) which are approximately consisted of crebris characters and \(\widetilde{U}_2=\widetilde{U}\backslash\widetilde{U}_1\).

Lemma 8.3. _If_ \(|\widetilde{U}_1|\ge|\widetilde{U}|/2\)_, then the expected length of the solution returned by Algorithm 3 is_ \(\Omega(n^{1/2+\zeta})\).

**Proof.** As mentioned above, for every block pair \((b_i,\overline{b_j})\in\widetilde{U}_1\), with probability at least \(n^{-2\delta}/4\) we have \(T[i][j]\ge n^{4\delta+\zeta}\), which means that the expected value of _T_\[_i_\]\[_j_\] is at least \(n^{2\delta+\zeta}/4\). Let _t_ be the solution returned by Algorithm 3. Since Algorithm 3 selects the best constrained solution, we have

\(\mathbb{E}(t)\ge\sum_{(b_i,\overline{b_j})\in B}\mathbb{E}(T[i][j])\)<br>
\(\ge\sum_{(b_i,\overline{b_j})\in\widetilde{U}_1}\mathbb{E}(T[i][j])\)<br>
\(\ge n^{1/2-2\delta}/16\cdot n^{2\delta+\zeta}/4\)<br>
\(=n^{1/2+\zeta}/64\)<br>
\(=\Omega(n^{1/2+\zeta}).\)

