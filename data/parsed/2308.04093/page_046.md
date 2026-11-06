To prove Lemma 4.9, we use the celebrated deterministic algorithm for finding a coloring of a set system that achieves small discrepancy, using the method of conditional probabilities or pessimistic estimators.

**Theorem B.4** (Deterministic set balancing \[Spe87, Rag88\])**.** _Given sets_ \(S_1,S_2,\dots,S_m\subseteq[n]\) _where_ \(|S_i|\le b\) _for all i, there is an O(n+bm)-time deterministic algorithm that finds_ \(x\in\{+1,-1\}^n\)_, such that for every_ \(i\in[m]\),

\(\left|\sum_{j\in S_i}x_j\right|\le 2\sqrt{b\mathrm{ln}(2m)}.\)

Note that the algorithm from Theorem B.4 can run in input-sparsity time, because when coloring an element \(j\in[n]\) we only need to update the pessimistic estimators for the sets _S<sub>i</sub>_ that contain _j_. To make this algorithm work in the word-RAM model with \(\Theta(\mathrm{log}(n+m))\)-bit words, the discrepancy bound is worsened by a constant factor to allow arithmetic operations with relative error 1/poly(_nm_) when computing the pessimistic estimators.

Lemma 4.9 then follows from recursively applying Theorem B.4.

_Proof of Lemma 4.9._ Without loss of generality we assume \(r\ge 2\), and assume _r_ is a power of two, by decreasing _r_ and increasing the size upper bound to \(|S_i|\le b_0:=2r\mathrm{log}_2(2m)\).

We use the following recursive algorithm with log<sub>2</sub>(_r_) levels: given size-_b_<sub>0</sub> sets _S_<sub>1</sub>_,...,S<sub>m</sub>_ from universe \[_n_\], use Theorem B.4 to find a two-coloring \(C_0:[n]\rightarrow\{+1,-1\}\), and then recurse on two subproblems whose _m_ sets are restricted to the universe \(C_0^{-1}(+1)\) and the universe \(C_0^{-1}(-1)\) respectively. The discrepancy of _C_<sub>0</sub> achieved by Theorem B.4 ensures these two subproblems contain sets of size at most \(b_0/2+\sqrt{b_0\mathrm{ln}(2m)}\). We keep recursing in this manner, and the _k_-th level of the recursion tree gives a 2_<sup>k</sup>_-coloring of the universe \[_n_\]. Finally the log<sub>2</sub>(_r_)-th level gives the desired _r_-coloring of \[_n_\]. By induction, the maximum size of _S<sub>i</sub>_ intersecting any color class is at most _b_<sub>log<sub>2</sub>(_r_)</sub>, which is recursively defined as<tbc>

\(b_0=2r\mathrm{log}m,b_k=b_{k-1}/2+\sqrt{b_{k-1}\mathrm{ln}(2m)}(1\le k\le\mathrm{log}_2(r)).\)

<tbc>To solve this recurrence, first divide by _b_<sub>_k_-1</sub> on both sides and get

\(\frac{b_k}{b_{k-1}}\le\frac{1}{2}\mathrm{exp}\left(2\sqrt{\mathrm{ln}(2m)/b_{k-1}}\right)\text{(using}1+x\le e^x\text{)}\)<br>
\(\le\frac{1}{2}\mathrm{exp}\left(2\sqrt{2^{k-1}\mathrm{ln}(2m)/b_0}\right).\text{(using}b_j\ge b_{j-1}/2\text{inductively)}\)

By telescoping,

\(b_{\mathrm{log}_2(r)}\le b_0\prod_{k=1}^{\mathrm{log}_2(r)}\frac{1}{2}\mathrm{exp}\left(2\sqrt{2^{k-1}\mathrm{ln}(2m)/b_0}\right)\)<br>
\(=\frac{b_0}{2^{\mathrm{log}_2(r)}}\mathrm{exp}\left(2\sqrt{\mathrm{ln}(2m)/b_0}\sum_{k=1}^{\mathrm{log}_2(r)}\sqrt{2^{k-1}}\right)\)<br>
\(=\frac{2r\mathrm{log}_2(2m)}{r}\mathrm{exp}\left(2\sqrt{\frac{\mathrm{ln}(2m)}{2r\mathrm{log}_2(2m)}\frac{\sqrt{r-1}}{\sqrt{2-1}}}\right)\)<br>
\(=O(\mathrm{log}m),\)

