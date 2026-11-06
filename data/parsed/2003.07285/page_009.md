Now, construct a graph _G_ in which we have a vertex for every \(1\le i\le\sqrt{n}\) and there is an edge between two vertices _i_ and _j_ if and only if \(|\text{lcs}(b_i,\bar{b}_j)|+|\text{lcs}(\bar{b}_i,b_j)|\ge\overline{\Omega}(n^{1/6})\). Using Lemma 8.6 we show that for any three vertices _i_, _j_, and _k_, at least there is an edge between one pair. Next, we apply the Turán’s theorem to show that _G_ is dense and thus the expected size of the LCS for two randomly selected blocks of \(s'\) and \(\overline{s'}\) is at least \(\overline{\Omega}(n^{1/6})\). This implies that the expected size of the solution returned by Algorithm 4 is \(\overline{\Omega}(n^{1/6+1/2})=\overline{\Omega}(n^{2/3})\) which is <o>_O_</o>(_n_<sup>1/3</sup>) approximation since the size of the optimal solution is bounded by _n_.

Indeed the proof for the case of complete permutation is much cleaner than the case of semi- permutation. However, we present a nice reduction in Section 8 that shows the argument carries over to the semi-permutation case. Roughly speaking, the idea is to create a _mask_ for both refined strings \(s'\) and \(\overline{s'}\) and prove some nice properties for the masks. Each mask is essentially a permutation of the symbols in \(\Sigma\) chosen in a way that the size of the LCS of the two masks is tentatively equal to the size of the LCS of two random blocks chosen from \(s'\) and \(\overline{s'}\). We then use the masks to turn each semi-permutation into a complete permutation by padding the characters that do not appear in the block to the end of it, according to their order in the corresponding mask. After this, each block is a complete permutation and the lemma holds for it. We then argue that the lemma also holds for the original refined blocks.

Let us be more precise about the proof. In Algorithm 4, after refining the blocks into semi- permutations, we know that in the nontrivial instances, the size of the solution is at least \(\overline{\Omega}(n)\). Now, for a symbol \(c\in\Sigma\), define _p<sub>c</sub>_ to be the probability that a random block (of any string) contains symbol _c_. If \(p_c=\overline{o}(1)\) for some character, then it is safe to assume that symbol _c_ does not contribute significantly to the solution. Thus, after removing all such symbols, the solution size is still \(\overline{\Omega}(n)\). Notice that we do not remove the characters in our algorithm and just for the case of simplicity, we ignore these characters in our analysis.

Now, for every symbol \(c\in\Sigma\) we have the property that \(p_c=\overline{\Omega}(1)\). Thus, if we take <o>_O_</o>(1) (but large enough) random blocks of the strings, each symbol appears in at least one block w.h.p. Based on this idea, we construct a mask for each string as follows: we start with an empty mask. Each time we randomly select a block of that string and append the characters that are not already in the mask but appear in the selected block to the end of the mask. The order of the newly added characters is the same as their order in the selected block. We repeat this procedure <o>_O_</o>(1) times to make sure the mask contains all of the symbols.

Again we emphasize that the construction of the masks is only part of the proof and does not play any role in Algorithm 4. Denote the constructed mask for string _s_ by mask(_s_) and the one for string <o>_s_</o> by mask(<o>_s_</o>). If \(\mathbb{E}[|\text{lcs}(\text{mask}(s),\text{mask}(\overline{s}))|]=\overline{\omega}(1)\) then we can imply that for two randomly selected blocks \(b'_i\) of _s_ and \(\overline{b'_j}\) of <o>_s_</o> we have \(\mathbb{E}[|\text{lcs}(b'_i,\overline{b'_j})|]=\overline{\omega}(1)\) and thus the expected solution size of Algorithm 4 is \(\overline{\omega}(\sqrt{n})\). This implies that Algorithm 4 is \(\overline{o}(\sqrt{n})\) approximation. Therefore, we<tbc>

acb
ebqa
edbfg
mask:
acb
acb eq
acbeq dfg

Figure 2: An example for the construction of the masks

