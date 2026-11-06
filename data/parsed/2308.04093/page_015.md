**Lemma 3.2** (Extension of \[CLMZ24, Lemma 4.1\])**.** _The set_ W _of input item weights can be partitioned in O(n+w_<sub>max</sub>log_w_<sub>max</sub>) _time into_ \(\mathcal{W}=\mathcal{W}_1\unknown\mathcal{W}_2\unknown\cdots\unknown\mathcal{W}_s\)_, where_ \(s<\mathrm{log}_2(\sqrt{w_\mathrm{max}})\)_, with the following property:_

_Denote_ \(\mathcal{W}_{\le j}=\mathcal{W}_1\cup\cdots\cup\mathcal{W}_j\) _and_ \(\mathcal{W}_{>j}=\mathcal{W}\backslash\mathcal{W}_{\le j}\)_. For every optimal exchange solution_ (_A,B_) _and every_ \(1\le j\le s\),

• \(|\mathcal{W}_j|\le 4C\sqrt{w_\mathrm{max}\mathrm{log}w_\mathrm{max}}\cdot 2^j\)_, and_<tbc>

• \(W(A\cap I_{\mathcal{W}_{>j}})\le 4Cw_\mathrm{max}^{3/2}/2^j\) _and_ \(W(B\cap I_{\mathcal{W}_{>j}})\le 4Cw_\mathrm{max}^{3/2}/2^j\),

_where C is the universal constant from Lemma 3.1._

The proof of Lemma 3.2 is similar to that of the original two-partition version \[CLMZ24, Lemma 4.1\], and is deferred to Appendix B.2.

Given this weight partitioning \(\mathcal{W}=\mathcal{W}_1\unknown\mathcal{W}_2\unknown\cdots\unknown\mathcal{W}_s\), our overall algorithm runs in two stages: in the first stage, we only consider items whose weights belong to W<sub>1</sub>, and efficiently compute an _I_<sub>W<sub>1</sub></sub>-optimal DP table (see Definition 2.6) by exploiting the small size of W<sub>1</sub>. Then, the second stage of the algorithm updates the DP table using the remaining items \(I_{\mathcal{W}_2}\unknown\cdots\unknown I_{\mathcal{W}_s}\). The second stage follows the same idea as \[CLMZ24\] of using Lemma 3.2 to trade off the size of the DP table and the number of linear-time scans needed to update the DP table. In contrast, the first stage is more technically challenging; we summarize it in the following lemma, and prove it in subsequent sections:

**Lemma 3.3** (The first stage)**.** _Let_ \(\mathcal{W}_1\subseteq[w_\mathrm{max}]\) _from Lemma 3.2 be given. Then we can compute an I_<sub>W<sub>1</sub></sub>_-optimal DP table in_ \(O(n+w_\mathrm{max}^2\mathrm{log}^4w_\mathrm{max})\) _time._

The overall \(O(n+w_\mathrm{max}^2\mathrm{log}^4w_\mathrm{max})\) algorithm for 0-1 Knapsack then follows from Lemma 3.3 and Lemma 3.2, using arguments similar to \[CLMZ24\].

_Proof of Theorem 1.1 assuming Lemma 3.3._ Use Lemma 3.2 to obtain the weight partition \(\mathcal{W}=\mathcal{W}_1\unknown\mathcal{W}_2\unknown\cdots\unknown\mathcal{W}_s\), where \(s<\mathrm{log}_2(\sqrt{w_\mathrm{max}})\). Define a size upper bound \(L_j:=4Cw_\mathrm{max}^{3/2}/2^j+w_\mathrm{max}\) for \(1\le j\le s\). Note that for every optimal exchange solution (_A,B_) and every \(1\le j\le s\) we have

\(|W(A\cap I_{\mathcal{W}_{\le j}})-W(B\cap I_{\mathcal{W}_{\le j}})|=\big|\big(W(A)-W(B)\big)-\big(W(A\cap I_{\mathcal{W}_{>j}})-W(B\cap I_{\mathcal{W}_{>j}})\big)\big|\)<br>
\(\le|W(A)-W(B)|+|W(A\cap I_{\mathcal{W}_{>j}})-W(B\cap I_{\mathcal{W}_{>j}})|\)<br>
\(<w_\mathrm{max}+4Cw_\mathrm{max}^{3/2}/2^j\)<br>
\(=L_j,\) (9)

where the last inequality follows from Eq. (5) and Lemma 3.2.

We run the first-stage algorithm of Lemma 3.3, and obtain an _I_<sub>W<sub>1</sub></sub>-optimal DP table. By Eq. (9), we can shrink the size of this DP table to _L_<sub>1</sub> without losing its _I_<sub>W<sub>1</sub></sub>-optimality. Then, we repeatedly apply the following claim:

**Claim 3.4.** _For_ \(2\le j\le s\)_, given an_ \(I_{\mathcal{W}_{\le j-1}}\)_-optimal DP table of size L_<sub>_j_-1</sub>_, we can compute an_ \(I_{\mathcal{W}_{\le j}}\)_-optimal DP table of size L<sub>j</sub> in_ \(O(|\mathcal{W}_j|(L_{j-1}+w_\mathrm{max}\mathrm{log}w_\mathrm{max})+|I_{\mathcal{W}_j}|)\) _time._

