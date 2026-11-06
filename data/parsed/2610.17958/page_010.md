<tbc>cerevisiae (I and II) and D. melanogaster -- the coverage of _S_Exact by _S_SEQ-SLIDER ranges from 45% to 100%. In particular, it was 100% only for S. cerevisiae I and D. melanogaster with parameter pair (\(\ell=8,d=3\)). Note that we used the more lenient version \(s_\ell\) of the similarity index to derive these results.

Moreover, for each \((\ell,d)\)-motif pair \(M\in S_\text{Exact}\), we also computed the highest similarity \(s_\ell(M,M')\), where \(M'\in S_\text{M-SLIDER}\) (resp. \(M'\in S_\text{SEQ-SLIDER}\)). Figure 5.3<tbc>

<tbc>shows the distribution of \((\ell,d)\)-motif pairs from _S_Exact for the parameter pair \((\ell=8,d=5)\) as a density plot. We observe that _S_Exact has a substantial amount of \((\ell,d)\)-motif pairs with similarity \(s_\ell\) below 50% to their closest counterparts in _S_M-SLIDER and _S_SEQ-SLIDER for the D. melanogaster, A. thaliana, and H. sapiens (I and II) datasets. On the other hand, for the E. coli and S. cerevisiae (I and II) datasets, most \((\ell,d)\)-motif pairs in _S_Exact have similarity above 70% to their closest counterparts in _S_M-SLIDER and _S_SEQ-SLIDER.

We arrive at the same conclusion for the parameter pair \((\ell=8,d=3)\), although SEQ-SLIDER had a better overall performance compared to \((\ell=8,d=5)\); see Figure 5.4. In particular, we note that every motif pair in _S_Exact has similarity \(s_\ell\ge 70\%\) with some motif pair in _S_M-SLIDER or _S_SEQ-SLIDER on the S. cerevisiae I and<tbc>

8.1 5.3 0
0 0.5 1
Similarity 0
0.5 1
Similarity (a) E. coli (b) S. cerevisiae I 4.2 4
Density 0
0 0.5 1
Similarity 0
0.5 1
Similarity (c) D. melanogaster (d) A. thaliana 5.7 9.1 0
0 0.5 1
Similarity 0
0.5 1
Similarity (e) H. sapiens I (f) S. cerevisiae II 5.1 0
0 0.5 1
Similarity (g) H. sapiens II (c) H. sapiens I (d) S. cerevisiae II 2.9 0
Density 0
0 0.5 1
Similarity (e) H. sapiens II 5.9 5.9 0
0 0.5 1
Similarity 0
0.5 1
Similarity (e) H. sapiens II

Figure 5.3: For every \(M\in S_\text{Exact}\), we show the highest \(s_\ell(M,M')\) such that \(M'\in S_\text{M-SLIDER}\) (resp. \(M'\in S_\text{SEQ-SLIDER}\)) for parameter pair \((\ell=8,d=5)\).

Figure 5.4: For every \(M\in S_\text{Exact}\), we show the highest \(s_\ell(M,M')\) such that \(M'\in S_\text{M-SLIDER}\) (resp. \(M'\in S_\text{SEQ-SLIDER}\)) for parameter pair \((\ell=8,d=3)\). We omitted the results for S. cerevisiae I and D. melanogaster because _S_Exact was fully covered by _S_SEQ-SLIDER.

