• \(|\mathcal{W}_j|\le 4C\sqrt{w_\mathrm{max}\mathrm{log}w_\mathrm{max}}\cdot 2^j\)_, and_<tbc>

• \(W(A\cap I_{\mathcal{W}_{>j}})\le 4Cw_\mathrm{max}^{3/2}/2^j\) _and_ \(W(B\cap I_{\mathcal{W}_{>j}})\le 4Cw_\mathrm{max}^{3/2}/2^j\),

_where C is the universal constant from Lemma 3.1._

_Proof._ Assume the _n_ items are sorted in decreasing order of efficiency, and the greedy solution is _G_={1,2_,...,i_<sup>∗</sup>}. Following \[CLMZ24\], for each \(1\le j\le s\), we define \(\ell_j\) to be the smallest \(1\le\ell_j\le i^*\) such that \(|\mathrm{supp}(\{w_{\ell_j},w_{\ell_j+1},\dots,w_{i^*}\})|\le 2C\sqrt{w_\mathrm{max}\mathrm{log}w_\mathrm{max}}\cdot 2^j\). Similarly, define _r<sub>j</sub>_ to be the largest \(i^*<r_j\le n\) such that \(|\mathrm{supp}(\{w_{i^*+1},\dots,w_{r_j}\})|\le 2C\sqrt{w_\mathrm{max}\mathrm{log}w_\mathrm{max}}\cdot 2^j\). Note that \([\ell_j,r_j]\subseteq[\ell_{j+1},r_{j+1}]\). We define the number of layers _s_ to be the smallest _s_ such that \(2C\sqrt{w_\mathrm{max}\mathrm{log}w_\mathrm{max}}\cdot 2^s\ge w_\mathrm{max}\). Then, in the last layer _j=s_, we have \(\ell_s=1,r_s=n\) by definition. Note that \(s<\mathrm{log}_2(\sqrt{w_\mathrm{max}})\).

Then, the partition \(\mathcal{W}=\mathcal{W}_1\unknown\mathcal{W}_2\unknown\cdots\unknown\mathcal{W}_s\) is defined as follows:

• Let \(\mathcal{W}_{\le j}:=\mathrm{supp}(\{w_{\ell_j},w_{\ell_j+1},\dots,w_{r_j}\})\) for all \(1\le j\le s\).<tbc>

• Then, let \(\mathcal{W}_1:=\mathcal{W}_{\le 1}\), and \(\mathcal{W}_j:=\mathcal{W}_{\le j}\backslash\mathcal{W}_{\le j-1}\) for \(2\le j\le s\).

Since \([\ell_j,r_j]\subseteq[\ell_{j+1},r_{j+1}]\) and \([\ell_s,r_s]=[1,n]\), this construction defines a partition \(\mathcal{W}=\mathcal{W}_1\unknown\mathcal{W}_2\unknown\cdots\unknown\mathcal{W}_s\). By definition of \(\ell_j,r_j\), it automatically satisfies the first property \(|\mathcal{W}_j|\le|\mathcal{W}_{\le j}|\le 4C\sqrt{w_\mathrm{max}\mathrm{log}w_\mathrm{max}}\cdot 2^j\) from the lemma statement. It remains to verify the second claimed property \(W(A\cap I_{\mathcal{W}_{>j}})\le 4Cw_\mathrm{max}^{3/2}/2^j\) (the other property \(W(B\cap I_{\mathcal{W}_{>j}})\le 4Cw_\mathrm{max}^{3/2}/2^j\) can be proved similarly).

Suppose this property is violated by some optimal exchange solution (_A,B_) (where \(A\subseteq\overline{G}=\{i^*+1,\dots,n\},B\subseteq G=\{1,\dots,i^*\}\)) and some \(1\le j\le s\), i.e.,<tbc>

\(W(A\cap I_{\mathcal{W}_{>j}})>4Cw_\mathrm{max}^{3/2}/2^j.\) (24)

<tbc>In particular, \(A\cap I_{\mathcal{W}_{>j}}\neq\varnothing\) implies \(r_j\neq n\). By definition of _r<sub>j</sub>_, this means

\(|\mathrm{supp}(\{w_{i^*+1},\dots,w_{r_j}\})|>2C\sqrt{w_\mathrm{max}\mathrm{log}w_\mathrm{max}}\cdot 2^j-1.\) (25)

Now consider the following two cases. Recall weights\((I):=\unknown_{i\in I}\{w_i\}\) denotes the multiset of item weights in \(I\subseteq[n]\).

• Case \(|\mathrm{supp}(\text{weights}(A))|\ge C\sqrt{w_\mathrm{max}\mathrm{log}w_\mathrm{max}}\cdot 2^j\):<tbc>

<tbc>Recall from Eq. (5) that |_W(A_)-_W(B_)|_\<w_<sub>max</sub>, so by Eq. (24) we have<tbc>

<tbc>\(W(B)>W(A)-w_\mathrm{max}\ge 4Cw_\mathrm{max}^{3/2}/2^j-w_\mathrm{max}\ge 3Cw_\mathrm{max}^{3/2}/2^j,\)<tbc>

<tbc>where we used \(2^j\le 2^s<\sqrt{w_\mathrm{max}}\) and assumed _C_ is large enough. Hence, \(|\mathrm{supp}(\text{weights}(A))|\cdot W(B)>3C^2w_\mathrm{max}^2\sqrt{\mathrm{log}w_\mathrm{max}}\), and Lemma 3.1 (with _N_:=_w_<sub>max</sub>) applied to weights(_A_) and weights(_B_) implies the existence of two non-empty item subsets \(A'\subseteq A,B'\subseteq B\) with the same total weight \(W(A')=W(B')\). Then, \((A\backslash A',B\backslash B')\) achieves strictly higher profit than (_A,B_), contradicting the optimality of (_A,B_).<tbc>

• Case \(|\mathrm{supp}(\text{weights}(A))|<C\sqrt{w_\mathrm{max}\mathrm{log}w_\mathrm{max}}\cdot 2^j\):<tbc>

