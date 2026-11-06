<tbc>components, \(G'_1,\dots,G'_k\) as outlined in paragraph _Techniques for finding type-A connected cliques_. The minmax similarity of _G<sub>i</sub>_ and _G<sub>j</sub>_ is then computed as \(\kappa_{ij}:=max\left\{|V(G'_\ell)||\ell=1,\dots,k\right\}\). Using the minmax similarity measure with the greedy ordering as outlined above, we greedily minimize the size of the maximum sized graph in which we have to find cliques in each of the steps. The computational results in Section 4 demonstrate a strong relationship between the chosen similarity measures and the number of maximal connected common subgraphs, validating the choice of these measures.

## 4 Results

To understand the relationship between similarity values between graphs and the number of their maximal `type-A` connected common edge subgraphs, we conducted the following experiment. For 500 molecular graphs, M={_G_<sub>1</sub>_,...,G_<sub>500</sub>}, from the ZINC data set \[18\], each having _n_ vertices with \(20\le n\le 25\), we computed for each pair of graphs their number of maximal `type-A` connected common edge subgraphs, and also the similarities measures (the three graph kernels VH, WL, NSDP and the minmax similarity - see Section 3).

yt
yt
106
106
105
105
104
104
103
103
102
102
0.0
0.2
0.4
0.6
0.8
1.0
0.0
0.2
0.4
0.6
0.8
1.0
Minmax Similarity Value
VH Similarity Value
yt
yt
106
106
105
105
104
104
103
103
102
102
0.0
0.2
0.4
0.6
0.8
1.0
0.0
0.2
0.4
0.6
0.8
1.0
WL Similarity Value
NSPD Similarity Value

**Fig.1.** Plots showing the relationship between the four normalized similarity measures VH, WL, NSDP or minmax (x-axis) and the values \(y_\ell\) on the y-axis that reflect average number of `type-A` connected common subgraphs of two graphs, see text for further details.

