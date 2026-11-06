<tbc>our algorithm finds interactions that SLIDER misses altogether. Subsection 5.6 is designed to show that case (2) is a significant contributor to the observed difference in scores.

## 5.6 Results for RQ2.

We measured the fraction (coverage) of \((\ell,d)\)-motif pairs in _S_<sub>Exact</sub> that have similarity \(s_\ell\ge 70\%\) to at least one \((\ell,d)\)-motif pair in _S_<sub>M-SLIDER</sub> and _S_<sub>SEQ-SLIDER</sub>. Here, we summarize<tbc>

<tbc>the results for SEQ-SLIDER only since it outperformed M-SLIDER in all but one instance (H. sapiens I with \((\ell=8,d=3)\)); refer to  C.2 in the appendix. The coverage of _S_<sub>Exact</sub> by _S_<sub>SEQ-SLIDER</sub> ranges from 8% to 52% across both parameter pairs for the A. thaliana and H. sapiens (I and II) datasets, meaning that SEQ- SLIDER misses at least roughly half of the top-scoring motif pairs, and up to 92% of them (M-SLIDER fares similarly). For the remaining datasets -- E. coli, S.<tbc>

M-SLIDER Exact
M-SLIDER Exact
SEQ-SLIDER
1
1
1
1
1
Norm. fx2
Norm. fx2
Norm. fx2
Norm. fx2
0.5
0.5
0.5
0.5
0
0
0
0
1
1
2301
1
1
363
1
1
231
Score rank
Score rank
Score rank
Score rank
(a) E. coli
(b) S. cerevisiae I
(a) E. coli
(b) S. cerevisiae I
1
1
1
1
Norm. fx2
Norm. fx2
Norm. fx2
Norm. fx2
Norm. fx2
0.5
0.5
0.5
0.5
0
0
0
0
1
149
1
168
1
1
2384
1
1
Score rank
Score rank
Score rank
Score rank
(c) D. melanogaster
(d) A. thaliana
(c) D. melanogaster
(d) A. thaliana
1
1
1
Norm. fx2
Norm. fx2
Norm. fx2
Norm. fx2
Norm. fx2
Norm. fx2
Norm. fx2
0.5
0.5
0.5
0.5
0.5
0
0
0
0
0
1
187
1
1836
1
1836
1
5792
Score rank
Score rank
Score rank
Score rank
(e) H. sapiens I
(f) S. cerevisiae II
(e) H. sapiens I
(f) S. cerevisiae II
1
1
Norm. fx2
Norm. fx2
Norm. fx2
Norm. fx2
Norm. fx2
0.5
0.5
0
0
0
1
472
1
4558
1
Score rank
Score rank
Score rank
(g) H. sapiens II
(g) H. sapiens II

Figure 5.1: Distribution of (normalized) \(f_{\chi^2}\) scores of \(S'_{\mathrm{M}-\mathrm{SLIDER}}\) and \(S'_{\mathrm{SEQ}-\mathrm{SLIDER}}\) compared to \(S'_{\mathrm{Exact}}\) across datasets of  5.1 for parameter pair (\(\ell=8,d=5\)).

Figure 5.2: Distribution of (normalized) \(f_{\chi^2}\) scores of \(S'_{\mathrm{M}-\mathrm{SLIDER}}\) and \(S'_{\mathrm{SEQ}-\mathrm{SLIDER}}\) compared to \(S'_{\mathrm{Exact}}\) across datasets of  5.1 for parameter pair (\(\ell=8,d=3\)).

