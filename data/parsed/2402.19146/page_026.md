right 1_<sup>t</sup>_ in \(N_2(\beta)\) to the characters in \(V_1(\alpha)\), or to the characters only in \(V_1(\alpha)\) and _V_**<sub>0</sub>**. Then, from similar discussion to the case (1), the length of the possible subsequence is less than _E_+1.<tbc>

2. Otherwise, we can align _V_**<sub>0</sub>** to \(V_2(\beta)\) and 1_<sup>t</sup>_ in \(N_1(\alpha)\) to the left 1_<sup>t</sup>_ in \(N_2(\beta)\). From a similar discussion to the above case and Lemma 10, \(\mathtt{ct}\text{\_}\mathtt{lcs}(N_1(\alpha),N_2(\beta))=E\).

Now we construct _S<sub>A</sub>_ of length 240_n<sub>A</sub>d_<sup>2</sup>+56_n<sub>A</sub>d_+100_d_<sup>2</sup>+16_n<sub>A</sub>_\(\in O(n_A\mathtt{poly}(d))\) and _T<sub>B</sub>_ of length 400_n<sub>A</sub>d_<sup>2</sup>+25_n<sub>B</sub>d_<sup>2</sup>+100_d_<sup>3</sup>+14_n<sub>B</sub>d_+100_d_<sup>2</sup>+4_n<sub>B</sub>_\(\in O((n_A+n_B)\mathtt{poly}(d))\) as follows:

\(S_A=\mathtt{0}^u\left(N_1(\alpha_1)\mathtt{0}^uN_1(\alpha_2)\mathtt{0}^u\cdots\mathtt{0}^uN_1(\alpha_{n_A})\mathtt{0}^u\right)^2\)<br>
\(T_B=\mathtt{0}^{u(2n_A+1)}N_2(\beta_1)\mathtt{0}^uN_2(\beta_2)\mathtt{0}^u\cdots\mathtt{0}^uN_2(\beta_{n_B})\mathtt{0}^{u(2n_A+1)},\)

where _u_=100_d_<sup>2</sup>.

We show the following lemmas:

**Lemma 12** _If there exist_ \(\alpha\in A\) _and_ \(\beta\in B\) _that are orthogonal, then_ \(\mathtt{ct}\text{\_}\mathtt{lcs}(S_A,T_B)\ge F+1\) _holds, where F=En<sub>B</sub>+u_(2_n<sub>A</sub>_+1).

_Proof_ In this proof, we give an alignment of _T<sub>B</sub>_ to _S<sub>A</sub>_ from which a common CT-subsequence of length _F_+1 can be constructed. Let \(\alpha_i\in A\) and \(\beta_j\in B\) be vectors which are orthogonal. If \(j\le i\), we align \(N_2(\beta_j)\) to the _first_ \(N_1(\alpha_i)\) in _S<sub>A</sub>_. By doing so, it is guaranteed that every normalized vector gadget \(N_2(\beta_x)\) in _T<sub>B</sub>_ (\(x\neq j\)) can be aligned to some normalized vector gadget in _S<sub>A</sub>_. Symmetrically, if _j\>i_, we align \(N_2(\beta_j)\) to the _second_ \(N_1(\alpha_i)\) in _T<sub>A</sub>_. Then, we align all the normalized vector gadgets in _T<sub>B</sub>_, except \(N_2(\beta_j)\), be aligned to normalized vector gadgets to the right and left of \(N_1(\alpha_i)\) in order from closest to \(N_1(\alpha_i)\), and _u_(2_n<sub>A</sub>_+1) 0’s in _T<sub>B</sub>_ are aligned to 0’s which interleave normalized vector gadgets in _S<sub>A</sub>_. The length of the common CT-subsequence constructed from such alignment is at least _E_+1+(_n<sub>B</sub>_-1)_E+u_(2_n<sub>A</sub>_+1)=_F_+1 by Lemma 11.

**Lemma 13** _If_ \(\alpha\) _and_ \(\beta\) _are not orthogonal for all pairs of_ \(\alpha\in A\) _and_ \(\beta\in B\)_, then_ \(\mathtt{ct}\text{\_}\mathtt{lcs}(S_A,T_B)\le F\) _holds._

_Proof_ Since \(\alpha\) and \(\beta\) are not orthogonal, any alignment between two normalized vector gadgets has length at most _E_ by Lemma 11. By a similar alignment of the proof of Lemma 12, we can construct a common CT-subsequence of length _En<sub>B</sub>+u_(2_n<sub>A</sub>_+1)=_F_ from the condition, such that we align all the normalized vector gadgets in _T<sub>B</sub>_ be aligned to normalized vector gadgets in _S<sub>A</sub>_ in order, and _u_(2_n<sub>A</sub>_+1) 0’s in _T<sub>B</sub>_ are aligned to 0’s which interleave normalized vector gadgets in _S<sub>A</sub>_. Here, we prove such alignment, which we denote by _M_, is optimal. Assume on the contrary that there exists a subsequence \(S'\) of _S<sub>A</sub>_ that CT-matches a common CT-subsequence of _T<sub>B</sub>_ with \(|S'|\ge F+1\). Since the total length of normalized vector gadgets in _S<sub>A</sub>_ is 40_n<sub>A</sub>d_<sup>2</sup>+56_n<sub>A</sub>d_+16_n<sub>A</sub>_, \(S'\) must include at least _F_-(40_n<sub>A</sub>d_<sup>2</sup>+56_n<sub>A</sub>d_+16_n<sub>A</sub>)\>_88_n<sub>A</sub>d_<sup>2</sup>+100_d_<sup>2</sup>_\>u_ 0’s. We consider the following two cases:

