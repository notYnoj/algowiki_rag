assume w.l.o.g. that \(\mathbb{E}[|\mathsf{lcs}(b'_i,\overline{b'_j})|]=\overline{O}(1)\).

Now, for every refined block \(b'_i\) of _s_ we construct a complete permutation by padding the characters that are not included in \(b'_i\) to the end of it. However, we maintain the property that the order of the newly added characters should be exactly the same as their order in mask(_s_). Let us refer to these (complete) permutations by cp_<sub>i</sub>_ for _s_. We similarly transform the semi-permutations of <o>_s_</o> into complete permutations using mask(<o>_s_</o>). We denote the complete permutations for <o>_s_</o> by <o>cp<sub>_i_</sub></o>. Notice that again, the construction of the complete permutations is only for the sake of analysis and we do not explicitly construct these permutations in our algorithm.

Now, we can use the previous analysis and prove that if the size of the solution is large (\(\overline{\Omega}(n)\)) then the LCS of two randomly selected complete permutations is large (\(\overline{\omega}(1)\)). However, this does not give us a bound for the refined blocks since complete permutations have extra characters and those characters may contribute to a large portion of the common subsequence. Here, we leverage the fact that E[|lcs(mask(_s),_mask(<o>_s_</o>))|]=<o>_O_</o>(1) or in other words, the expected size of the longest common subsequence for the masks is small. Using this bound, we can show that the contribution of the extra characters to the common subsequence is bounded by \(\overline{\omega}(1)\) and therefore the majority of the solution is due to the characters of the refined blocks. This proves that the LCS of two randomly selected refined blocks of _s_ and <o>_s_</o> is large (\(\overline{\omega}(1)\)) and thus Algorithm 4 is \(\overline{o}(\sqrt{n})\) approximate.

## 5 A Linear Time _O(n_<sup>0.497956</sup>) Approximation Algorithm for LCS

In this section we bring a formal proof to show that our algorithm is _O(n_<sup>0.497956</sup>) approximation. In Sections 6, 7, and 8 we analyze Algorithms 1, 2, 3, and 4 in details and prove Lemmas 6.1, 7.1, and 8.1 (a simple statement for each lemma is given in Figure 4). We consider two parameters \(\delta\) and \(\eta\) in our analysis to denote the value of |lcs(_s,<o>s</o>_)| by \(n^{1-\delta}\) and the number of symbols by \(n^{1/2+\eta}\). Therefore, we have \(0\le\delta\le 1\) and \(-0.5\le\eta\le 0.5\). As shown in Figure 4, the approximation factor of our algorithm is bounded by \(\tilde{O}(n^\nu)\) where:

\(\nu=min\left\{\begin{array}{ c }
1/2-\delta/2, \\
1/2-\eta, \\
1/2-1/37+(221/37)\delta+(10/37)\eta
\end{array}\right\}\)

Thus, we can optimize \(\nu\) by solving the following linear program:

acb
ebqa
edbfg
mask:
acbeqdfg
acb eqdfg
ebqa cdfg
edbfgacq

Figure 3: An example for the construction of the masks

