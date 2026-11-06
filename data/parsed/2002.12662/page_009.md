<tbc>for each dataset, _k_ (i.e. number of subpatterns), and gap constraint by selecting from the set of 200 subpatterns. We emphasise that the generated patterns, while not specifically designed to be pathological, do represent relatively hard instances for SA-scan because of the high frequency of each subpattern.

#### Matching Performance for Different Gap Constraint Bands.

Our first experiment aims to elucidate the impact of gap constraint size on query time. We fix the subpattern length |_p<sub>i</sub>_|=_m<sub>i</sub>_=3.  1 shows the results from VLG patterns consisting of _k_=2<sup>1</sup>_,...,_2<sup>5</sup> subpatterns. Our method, marked Filter+TC, is always faster than WT, with the exception of the large-gap _C<sub>L</sub>_ pattern sets, where on some data sets it yields to WT (most likely due to the text-checking heuristic being less effective on _C<sub>L</sub>_).

#### Matching Performance for Different Subpattern Lengths.

In our second experiment, we examine the impact of subpattern lengths on query time, fixing the gap constraint to _C<sub>S</sub>_=100,110.  2 shows the results. Larger subpattern lengths tend to result in smaller SA ranges. Consequently, SA-scan outperforms WT by an even wider margin.

#### Overall Runtime Performance.

In a final experiment we explored the whole parameter space (i.e. \(k\in\{2^1,\dots,2^5\}\), \(m_i\in\{3,5,7\}\), \(C\in\{C_S,C_M,C_L\}\)). The results are summarized in Figure 6. Overall out SA-scan-based method is faster on average than the wavelet-tree-based one, usually by a wide margin.

### 6 Concluding Remarks

We have described a number of simple but highly effective improvements to the SA-scan VLG matching algorithm that, according to our experiments, elevate it

CC
Kernel
Para
Proteins
1M
Query time [us]
100k
10k
1k
100
F+TC Filter
Radix
F+TC Filter
Radix
F+TC Filter
Radix
F+TC Filter
Radix
F+TC Filter
Radix

Fig.5: Direct text checking improves search times further (_k_=4).

