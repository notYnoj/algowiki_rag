In the next section, we show that for the case that \(|\widetilde{U}_2|\ge|\widetilde{U}|/2\), Algorithm 4 provides a good approximate solution.

## 8.2 Algorithm 4: Random Shifting Algorithm.

In this section, we analyze Algorithm 4 and show that this algorithm performs well on the instances that satisfy the preconditions, and have the property that \(|\widetilde{U}_2|\ge|\widetilde{U}|/2\). Let us first give a short description of Algorithm 4. Algorithm 4 modifies each block of the strings into a special structure, which we call semi-permutation. Next, Algorithm 4 samples a random integer _r_ uniformly from \([1,\sqrt{n}]\), and for every \(1\le i\le\sqrt{n}\), finds \(q_i=\mathsf{lcs}(b_i,\bar{b}_{(i+r)\mathrm{mod}\sqrt{n}})\) <sup>3</sup> . Finally, Algorithm 4 selects one of<tbc>

\(t_1=q_1q_2\dots q_{\sqrt{n}-r}\)

<tbc>or

\(t_2=q_{\sqrt{n}-r+1}q_{\sqrt{n}-r+2}\cdots q_{\sqrt{n}}\)

which is longer, as an approximation of lcs(_s,<o>s</o>_). In what follows we describe Algorithm 4 in more details.

In the first step, Algorithm 4 updates _s_ and <o>_s_</o> by performing the following operation on each block: for every symbol which appears more than once in that block, we keep one of the instances uniformly at random and remove the rest. After this operation, each symbol appears in each block at most once. Note that, the blocks may have different sizes as some symbols might not appear in some blocks. Formally, after this operation, each block of _s_ and <o>_s_</o> is a permutation of the characters in \(\Sigma\), except that some of the symbols are missing in each block. We call such a structure _semi-permutation_.

As we show in Section 8.2.1, after this operation, there exist two sets _U_ and <o>_U_</o> of the blocks in _s_ and <o>_s_</o>, such that \(|U|=|\overline{U}|=\Omega(n^{1/2-26\delta-4\zeta-\eta})\), and for every two blocks _b<sub>i</sub>_ and \(\bar{b}_j\) that are randomly selected from _U_ and <o>_U_</o>, we have

\(\mathbb{E}(|\mathsf{lcs}(b_i,\bar{b}_j)|)=\tilde{\Omega}(n^{1/6-65/3\delta-10/3\zeta-4/3\eta}).\) (8.7)

In the second step, Algorithm 4 selects a random integer _r_ and for every _i_, finds

\(q_i=\mathsf{lcs}(b_i,\bar{b}_{(i+r)\mathrm{mod}\sqrt{n}}).\)

Since both _b<sub>i</sub>_ and \(\bar{b}_j\) are semi-permutations, they have at most \(\sqrt{n}\) matching pairs and hence, _q<sub>i</sub>_ can be computed in time \(\tilde{O}(\sqrt{n})\) \[6\]. Therefore, the running time of Algorithm 4 is \(\tilde{O}(n)\). To analyze the approximation factor of Algorithm 4, we focus on the blocks in _U_ and <o>_U_</o>. Note that since _r_ is selected uniformly at random, if for some index _i_, both \(b_i\in U\) and \(\bar{b}_{(i+r)\mathrm{mod}\sqrt{n}}\in\overline{U}\) hold, then we have

\(\mathbb{E}(|q_i|)=\tilde{\Omega}(n^{1/6-65/3\delta-10/3\zeta-4/3\eta}).\)

Furthermore, since \(|U|=|\overline{U}|=\Omega(n^{1/2-26\delta-4\zeta-\eta})\) and the total number of blocks is _n_<sup>1/2</sup>, the expected number of such indices is at least \(|U|\cdot|U|/n^{1/2}=\Omega(n^{1/2-52\delta-8\zeta-2\eta})\). Thus, the expected size of the solution returned by Algorithm 4 is at least<tbc>

\((\sum_{1\le i\le\sqrt{n}}\mathbb{E}(|q_i|))/2=\tilde{\Omega}(n^{2/3-221/3\delta-34/3\zeta-10/3\eta}).\)

<sup>3</sup>Here we need a slightly modified mod operator where \(\sqrt{n}\mathrm{mod}\sqrt{n}=\sqrt{n}\).

