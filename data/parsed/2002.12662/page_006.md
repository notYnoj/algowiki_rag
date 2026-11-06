<tbc>_p_<sub>2</sub> (the second subpattern) happens to be smaller (i.e. _p_<sub>2</sub> has less occurrences in T than _p_<sub>1</sub>) then we set bits \(F[(i-\delta)/b..(i-\Delta)/b]\) (rather than \(F[(i+\delta)/b..(i+\Delta)/b]\)) to 1. Assuming _p_<sub>1</sub> is in fact more frequent than _p_<sub>2</sub>, the second refinement is to perform a second round of filtering using the contents of _A_<sub>2</sub>. More precisely, having obtained _A_<sub>2</sub>, we clear _F_ (setting all bits to 0) and scan _A_<sub>2</sub> settings bits \(F[(i-\delta)/b..(i-\Delta)/b]\) to 1 for each \(i\in A_2\). We then scan _A_<sub>1</sub> and discard any element _i_ for which _F_\[_i/b_\] now equals 0. Obviously it only makes sense to employ this heuristic if the initial filtering reduced the number of candidates, |_A_<sub>2</sub>|, of the second subpattern significantly below _m_<sub>1</sub>. In practice we found _m_<sub>2</sub>_\<m_<sub>1</sub>/2 led to a consistent speedup.

Of course, these techniques generalize easily to _k\>_2 subpatterns. The idea is that the output of the intersection of the first two subpatterns then becomes an input interval to be intersected with the third subpattern, and so on.

As Figure 3 shows, employing _F_ can reduce runtime immensely, but the improvement varies greatly with _b_. A good choice for _b_ depends on a number of factors. For each occurrence of _p_<sub>1</sub>, we set \(\lceil\frac{\Delta-\delta}{b}\rceil\) bits in _F_. Accesses to _F_ while setting these bits are essentially random (determined by the order of the positions of _p_<sub>1</sub>, which are the lexicographic order of the corresponding suffixes of T), and so it helps greatly if _b_ is chosen so that _F_, which has size _n/b_ bits, fits in cache. This can be seen in Figure 3, particularly clearly for the CC, Kernel, and Protein data sets, where performance improves sharply with increasing _b_ until _F_ fits in cache (30MiB on our test machine) where it quickly stabilizes (at<tbc>

-107
CS
-107
CM
-107
CL
1
1
1
0.8
0.8
0.8
0.6
0.6
0.6
Total time [us]
0.4
0.4
0.4
0.2
0.2
0.2
0
0
0
0
2
4
6
8
10
12
14
16
0
2
4
6
8
10
12
14
16
0
2
4
6
8
10
12
14
16
log b
log b
log b
CC Filter
Kernel Filter
Para Filter
Proteins Filter
CC Radix
Kernel Radix
Para Radix
Proteins Radix

Fig.3: Effect of filter granularity on search time. Ordinate is runtime in microseconds and mantissa is the logarithm (base 2) of the filter block size. Dashed lines show the time required by SA-scan (using radix sort) without any filter. Each plot corresponds to a different set of 20 synthetically generated VLG patterns. All patterns contain 2 of the 200 most frequent subpatterns in each data set. We fixed the gap constraints \(C_i=\langle\delta_i,\Delta_i\rangle\) between subpatterns to small (\(C_S=\langle 100,110\rangle\)), medium (\(C_M=\langle 1000,1100\rangle\)), or large (\(C_L=\langle 10000,11000\rangle\)). Section 5 gives more details of data sets and pattern sets.

