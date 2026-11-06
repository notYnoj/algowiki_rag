_Proof._ Let (_A,B_) be an optimal exchange solution such that \(A\cap I_{\mathcal{W}_1}=A'\) and \(B\cap I_{\mathcal{W}_1}=B'\). In the following we will only prove the claimed properties about \(A'\), and the properties about \(B'\) can be proved similarly.

For Item 1, note that \(J_{\le k}^+=\{i\in\overline{G}\cap I_{\mathcal{W}_1}:\text{rank}(i)\le 2^k-1\}\), and we have \(2^k-1\ge 2w_\mathrm{max}\) by the definition of _k_. By the prefix property (Lemma 2.4), we have \(\text{rank}(i)\le 2w_\mathrm{max}\) for all \(i\in A'\), and thus \(A'\subseteq J_{\le k}^+\).

For Item 2, we apply Lemma 3.6 with _N_:=_w_<sub>max</sub> to the multisets weights(_A_) and weights(_B_), which should not share any common non-zero subset sum (Eq. (6)). Since |_W(A_)-_W(B_)|_\<w_<sub>max</sub> (Eq. (5)), Lemma 3.6 implies for all \(r\ge 1\) that

\(|\mathrm{supp}_r(\text{weights}(A))|<C_0\sqrt{w_\mathrm{max}/r}\cdot\sqrt{\mathrm{log}(2w_\mathrm{max})}\) (14)

for some universal constant _C_<sub>0</sub>. Hence,

\(|A'\cap J_{\le j}^+|=|\{i\in A':1\le\text{rank}(i)\le 2^j-1\}|\)<br>
\(=\sum_{w\in\mathcal{W}_1}\mathrm{min}\{2^j-1,|A'\cap I_{\{w\}}|\}\)<br>
\(=\sum_{r=1}^{2^j-1}|\mathrm{supp}_r(\text{weights}(A'))|\)<br>
\(\le\sum_{r=1}^{2^j-1}|\mathrm{supp}_r(\text{weights}(A))|\)<br>
\(\le\sum_{r=1}^{2^j-1}C_0\sqrt{w_\mathrm{max}/r}\cdot\sqrt{\mathrm{log}(2w_\mathrm{max})}\) (by Eq. (14))<br>
\(<C_0\sqrt{w_\mathrm{max}}\cdot 2\sqrt{2^j-1}\cdot\sqrt{\mathrm{log}(2w_\mathrm{max})}\)<br>
\(<C2^{j/2}\sqrt{w_\mathrm{max}\mathrm{log}(2w_\mathrm{max})}\)

for some universal constant _C_.

For Item 3, the set under consideration is a subset of W<sub>1</sub>, and in the _j_=1 case we can simply bound its size using Lemma 3.2 as \(\le|\mathcal{W}_1|\le 8C_1\sqrt{w_\mathrm{max}\mathrm{log}w_\mathrm{max}}\le b_1\), provided the constant _C_ in the definition of _b_<sub>1</sub> (Eq. (13)) is large enough. Now it remains to consider \(2\le j\le k\), and we have to bound the number of \(w\in\mathcal{W}_1\) such that \(I_{\{w\}}\cap J_{j-1}^+\subseteq A'\) and \(I_{\{w\}}\cap J_j^+\neq\varnothing\). For any such _w_, by definition of our rank partitioning (Definition 3.5), \(I_{\{w\}}\cap J_j^+\neq\varnothing\) means that \(I_{\{w\}}\cap\overline{G}\) contains some item _i_ with \(\text{rank}(i)\ge 2^{j-1}\), and hence \(|I_{\{w\}}\cap J_{j-1}^+|=2^{j-2}\). Then from \(I_{\{w\}}\cap J_{j-1}^+\subseteq A'\) we get \(|I_{\{w\}}\cap A'|\ge 2^{j-2}\), or equivalently, \(w\in\mathrm{supp}_{2^{j-2}}(\text{weights}(A'))\). Thus, the number of such _w_ is at most

\(|\mathrm{supp}_{2^{j-2}}(\text{weights}(A'))|\le|\mathrm{supp}_{2^{j-2}}(\text{weights}(A))|\)<br>
\(<C_0\sqrt{w_\mathrm{max}/(2^{j-2})}\cdot\sqrt{\mathrm{log}(2w_\mathrm{max})}\) (by Eq. (14))<br>
\(\le C\sqrt{w_\mathrm{max}}\cdot 2^{-j/2}\sqrt{\mathrm{log}(2w_\mathrm{max})}\)<br>
\(=b_j\)

for some large enough constant _C_.

