The initial code to generate these bounds was written completely independently from the codebase linked<tbc>

<tbc>in \[20\]. We also developed a separate code base containing a C++ implementation of Lueker’s algorithm converted directly from his code (see Appendix B). The bounds from all three independently developed code bases match exactly for \(\ell\le 15\), indicating that the implementations are likely correct. Our results from the general case also exactly match Kiwi and Soto’s \[16\] for matching values of \(\sigma\), _d_, and \(\ell\) (see Appendix C).

\begin{tabular}{ccc}
\multirow{2}{*}{\(\ell\)} & **Lower bound on** \(\gamma\) & **Lower bound on** \(\gamma\) \\
 & **(Lueker \[20\])** & **(ours)** \\
1 & 0.666666 & 0.666666 \\
2 & 0.727272 & 0.727272 \\
3 & 0.747922 & 0.747922 \\
4 & 0.758576 & 0.758576 \\
5 & 0.765446 & 0.765446 \\
6 & 0.770273 & 0.770273 \\
7 & 0.773975 & 0.773975 \\
8 & 0.776860 & 0.776860 \\
9 & 0.779259 & 0.779259 \\
10 & 0.781281 & 0.781281 \\
11 & 0.783005 & 0.783005 \\
12 & 0.784515 & 0.784515 \\
13 & 0.785841 & 0.785841 \\
14 & 0.787017 & 0.787017 \\
15 & 0.788071 & 0.788071 \\
16 & - & **0.789021** \\
17 & - & **0.789882** \\
18 & - & **0.790668** \\
19 & - & **0.791389** \\
20 & - & **0.792052** \\
21 & - & **0.792665** \\
\end{tabular}

412
Binary Feasible Triplet Feasible Triplet
410
48
46
switch to external memory
Runtime (s)
44
42
40
4-2
4-4
2
4
6
8
10
12
14
16
18
20
String Length l

Figure 2: Runtime of the Feasible Triplet and Binary Feasible Triplet algorithms for \(\gamma_{2,2}\) as string length parameter \(\ell\) increases. Specialization to the binary case improves performance and the presented method of memory I/O reduces the overhead incurred by switching from RAM to disk memory to less than 18x.

2: Lower bounds on \(\gamma\) for values of \(\ell\), the string length parameter, from 1 to 21. Bold numbers represent new best lower bounds.

