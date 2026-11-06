## 2 Asteroidal Triples and Friends in (Likely Necessary) Matrix Multiplication Time

There are simple reductions from Boolean matrix multiplication to many of these problems, showing that \(n^{\omega-o(1)}\) time seems _necessary_ to solve them. This is true for instance for unweighted APSP and most "funny" matrix products. For even more problems, \(n^{\omega-o(1)}\) time lower bounds can be proven under stronger but still plausible assumptions such as that detecting a triangle in an _n_-node graph requires \(n^{\omega-o(1)}\) time. For problems with \(n^{\omega-o(1)}\) time conditional lower bounds and subcubic time upper bounds using matrix multiplication, a natural question is:

_Can these problems be solved in_ \(\tilde{\mathcal{O}}(n^\omega)\) _time or is there a higher conditional lower bound?_

The term "intermediate problem" has emerged to capture problems that are in truly subcubic time but whose running times are _strictly larger_ than \(n^\omega\). Several recent works study such problems within the context of fine-grained complexity \[BKPR19, LPV20, VX20a, CVX21, Fis26\], providing conditional lower bounds \(n^{c-o(1)}\) for \(c>\omega\) for some of these problems.

Most studied intermediate problems have running times that are \(\tilde{\mathcal{O}}(n^{2.5})\) if \(\omega=2\); a popular running time is \(\tilde{\mathcal{O}}(n^{(3+\omega)/2})\). This is the best known running time for the Dominance Product \[Mat91\], max- min matrix product and All-Pairs Bottleneck Paths \[VWY07, DP09\], All-Pairs Non-Decreasing Paths \[Vas10, DGZ18, DJW19\], Monotone Min-Plus Product \[BGSV19, VX20b, GPVX21, CDXZ22\], Language Edit Distance (also known as Scored Parsing \[AP72, Sah17, BGSV19\]), RNA Folding \[NJ80, Aku99, ZTZU11, VGF14, Sah17\], Dyck Edit Distance \[Sah14, BGSV19, DKS22, FGK<sup>+</sup>24\], Tree Edit Distance \[Mao21, Dür23, NPS<sup>+</sup>25\], Node-weighted APSP \[Cha10, Yus09, AFJ<sup>+</sup>25\], and Min-Equality Product \[VX20a\].

One of the very first papers to prove \(n^{\omega-o(1)}\) lower bounds under plausible conjectures for a variety of graph problems, while also providing subcubic time algorithms using matrix multiplication, is a seminal SODA 2003 paper by Kratsch and Spinrad \[KS06\]. Almost all of the problems studied by \[KS06\] were solved in O(_n_<sup>2.79</sup>) time. With a small change<sup>2</sup> the algorithms can be made to run in \(\tilde{\mathcal{O}}(n^{(3+\omega)/2})\) time. This motivates the following questions.

_Are these problems intermediate, or can they be solved in_ \(\tilde{\mathcal{O}}(n^\omega)\) _time?_

_How do these problems fit into the recently established fine-grained hierarchy?_

Even the name of Kratsch and Spinrad’s paper "Between O(_mn_) and \(\mathcal{O}(n^\alpha)\)" (here \(\alpha=\omega\)) suggests that the problems in the paper are intermediate. Despite much recent progress on the fine-grained complexity of intermediate problems, the problems studied in Kratsch and Spinrad’s paper have not seen improvements since the paper was written more than 20 years ago.

The main contribution of our work is to show that these problems are not intermediate. They, in fact, admit conditionally tight \(\tilde{\mathcal{O}}(n^\omega)\) time algorithms.

### 1.1 The problems studied by Kratsch and Spinrad

Kratsch and Spinrad \[KS06\] investigate the following algorithmic problems in structural graph theory that have very strong motivation, e.g., in the study of perfect graphs, AT-free graphs and triangulated graphs (see Appendix A for details). Given an (undirected) graph **G**=(_V,E_), the problems are:

\(\blacksquare\) Computing the _neighborhood-deleted components_ of **G**: Specifically, for each \(v\in V\) , compute the connected components of **G**\[_V_\\_N[v_\]\] (the graph obtained by removing _v_ and its neighborhood).

<sup>2</sup> The neighborhood connected components algorithm of \[KS06\] uses an inefficient way to list witnesses of Boolean matrix multiplication. Just by replacing Lemma 2.1 in \[KS06\] with the approach of \[AGMN92, GKL09\] to list up to _f_ witnesses per pair in \(\tilde{\mathcal{O}}(f\text{MM}(n,n/f,n))\) time, one obtains a running time \(\tilde{\mathcal{O}}(f\text{MM}(n,n/f,n)+\text{MM}(n,n^2/f,n))\) for neighborhood-deleted components which gives \(\tilde{\mathcal{O}}(n^{(3+\omega)/2})\) via blocking or O(_n_<sup>2.616</sup>) with rectangular matrix multiplication. For the rest of the problems, in \[KS06\] there is an additional \(\tilde{\mathcal{O}}(n^{(3+\omega)/2})\) cost after the neighborhood- deleted components are computed.

