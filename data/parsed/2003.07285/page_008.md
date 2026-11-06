4 focuses on the rarus characters. Since either the crebris or rarus pieces of the optimal solution provide a 1/2 guarantee, any \(\overline{\sigma}(\sqrt{n})\) solution for each set of characters gives us an \(\overline{\sigma}(\sqrt{n})\) solution to LCS.

We argue in Section 8 that Algorithm 3 provides an \(\overline{\sigma}(\sqrt{n})\) approximation of the crebris characters. In other words, we show that the length of the solution that Algorithm 3 finds is at least \(\overline{\omega}(\sqrt{n})\), if the crebris characters dominate the solution. Let _c_ be a crebris character in a part of the solution which is associated to blocks _b<sub>i</sub>_ and <o>_b_</o><sub>j</sub>. Since _c_ is crebris, then \(\overline{\omega}(1)\) characters of these blocks have the same symbol as _c_ and therefore the expected value of _T_\[_i_\]\[_j_\] in Algorithm 3 is an \(\overline{\sigma}(\sqrt{n})\) approximation of \(|\mathsf{lcs}(b_i,\overline{b_j})|\). This observation enables us to prove that Algorithm 3 gives an \(\overline{\sigma}(\sqrt{n})\) approximation of the crebris characters of opt.

The analysis for Algorithm 4 is much more technically involved. Notice that after applying Algorithm 3, we know that in the nontrivial instances, for any optimal solution opt, the majority of the characters are rarus. The nice property of the rarus characters is that after modifying each block into a semi-permutation, the size of the rarus characters in any optimal solution remains relatively intact. Notice that some rarus characters may appear too many \((\overline{\omega}(1))\) times in both corresponding blocks of _s_ and <o>_s_</o>, however, the majority of the rarus characters appear only a few times (<o>_O_</o>(1)) in the corresponding blocks and therefore after turning blocks into semi-permutations, the size of the rarus portion of any optimal solution remains relatively unchanged.

Let us refer to the semi-permutations by refined blocks and denote them by \(b'_i\) and \(\overline{b'_i}\). We also denote the refined strings by \(s'\) and \(\overline{s'}\). We show in Section 8 that if \(m=\overline{O}(\sqrt{n})\) and \(|\mathsf{lcs}(s',\overline{s'})|=\overline{\Omega}(n)\) then we have

\(\mathbb{E}_{i,j\sim[\sqrt{n}]}[|\mathsf{lcs}(b'_i,\overline{b'_j})]=\overline{\omega}(1)\)

for two randomly selected refined blocks _b<sub>i</sub>_ and \(b'_j\). This indeed proves that Algorithm 4 obtains an \(\overline{\sigma}(\sqrt{n})\) approximation of the optimal solution, provided that all the previous algorithms have failed to do so.

Our analysis is based on two well-known combinatorial theorems: Dilworth’s theorem and Turán’s theorem.

Theorem (Turán 1941 \[30\]). _Let G be any graph with n vertices, such that G is K_<sub>_r_+1</sub>_-free. Then the number of edges in G is at most_ (1-1_/r)n_<sup>2</sup>/2.

Theorem (Dilworth-1950 \[17\]). _Let P be a poset. Then there exists an antichain X and a chain decomposition Y satisfying_ |_X_|=|_Y_|.

For a formal definition of poset, antichain, and chain decomposition, we refer the reader to Section 8.

To illustrate the idea, let us consider a simple case in which \(|\Sigma|=\sqrt{n}\) and each block is a complete permutation of \(\Sigma\). Also, we assume for simplicity that in the optimal solution, every block _b<sub>i</sub>_ of _s_ is matched with block \(b'_i\) of <o>_s_</o>, that is \(|\mathsf{lcs}(b_i,\overline{b_i})|=\overline{\Omega}(\sqrt{n})\) for each \(1\le i\le\sqrt{n}\). We show that in this case, the expected size of LCS for two randomly selected blocks of \(s'\) and \(\overline{s'}\) is \(\overline{\Omega}(n^{1/6})\). In this case, we first leverage Dilworth’s theorem to prove Lemma 8.6.

**Lemma** 8.6 (restated)**.** _Let_ \(\pi_1\), \(\pi_2\)_, and_ \(\pi_3\) _be three permutations of numbers_ \[1_...m_\]_. Then, we have_<tbc>

\(max\{|\mathsf{lcs}(\pi_1,\pi_2)|,|\mathsf{lcs}(\pi_1,\pi_3)|,|\mathsf{lcs}(\pi_2,\pi_3)|\}\ge m^{1/3}.\)

