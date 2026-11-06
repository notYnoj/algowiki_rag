<tbc>to be the state-of-the-art approach for the indexed version of problem. We believe better indexing methods for VLG matching can be found, but that our version of SA-scan, which makes judicious use of filters, text checking, and subpattern processing order, represents a strong baseline against which the performance of more exotic methods should be measured.

Numerous avenues for continued work on VLG matching exist, perhaps the most interesting of which is to reduce index size. Currently, SA-scan uses \(nlogn+nlog\sigma\) bits of space for a text of length _n_ on alphabet \(\sigma\) for the suffix array and text, respectively (the WT approach of Bader et al., uses slightly more). Because our methods consist (mostly) of simple scans of SA ranges or scans of the underlying text, they are easily translated to make use of recent results on Burrows-Wheeler-based compressed indexes \[10\] that allow fast access to elements of the suffix array from a compressed representation of it. Via this observation we derive the first compressed indexes for VLG matching. These indexes use _O(r_log_n_) bits of space, where _r_ is the number of runs in the Burrows- Wheeler transform, a quantity that decreases with text compressibility. On our 2 GiB Kernel data set, for example, the compressed index takes around 20 MiB in practice, and can still support VLG matching in times competitive with the indexes of Bader et al. We plan to explore this in more depth in future work.

## Acknowledgements.

Our thanks go to Tania Starikovskaya for suggesting the problem of indexing for regular-expression matching to us. We also thank Matthias Petri and Simon Gog for prompt answers to questions about their article and code and the anonymous reviewers for helpful comments. This work was funded by the Academy of Finland via grant 319454 and by EU’s Horizon 2020 research<tbc>

\begin{tabular}{ccccccccccccc}
\multirow{2}{*}{Method} & \multicolumn{3}{c}{CC} & \multicolumn{3}{c}{Kernel} & \multicolumn{3}{c}{Para} & \multicolumn{3}{c}{Proteins} \\
 & _C<sub>S</sub>_ & _C<sub>M</sub>_ & _C<sub>L</sub>_ & _C<sub>S</sub>_ & _C<sub>M</sub>_ & _C<sub>L</sub>_ & _C<sub>S</sub>_ & _C<sub>M</sub>_ & _C<sub>L</sub>_ & _C<sub>S</sub>_ & _C<sub>M</sub>_ & _C<sub>L</sub>_ \\
\multicolumn{13}{c}{k = 2} \\
Filter+TC & 1391 & 1783 & 3329 & 744 & 1303 & 2243 & 2243 & 4170 & 2184 & 388 & 485 & 976 \\
WT\_ALL & 17354 & 19736 & 21757 & 7393 & 10205 & 15891 & 12372 & 14683 & 3654 & 8549 & 10547 & 14470 \\
\multicolumn{13}{c}{k = 4} \\
Filter+TC & 1099 & 1739 & 3186 & 664 & 1158 & 1654 & 1214 & 8134 & 9036 & 370 & 580 & 1609 \\
WT\_ALL & 7452 & 7499 & 8770 & 2201 & 4810 & 2756 & 6554 & 9039 & 5230 & 8486 & 9319 & 12621 \\
\multicolumn{13}{c}{k = 8} \\
Filter+TC & 2185 & 1219 & 3057 & 328 & 733 & 3563 & 5 & 27 & 10300 & 354 & 581 & 2231 \\
WT\_ALL & 7919 & 6511 & 6054 & 1885 & 2260 & 1468 & 237 & 345 & 2518 & 11940 & 12867 & 13450 \\
\multicolumn{13}{c}{k = 16} \\
Filter+TC & 674 & 930 & 3267 & 312 & 667 & 984 & 5 & 15 & 631 & 350 & 534 & 2361 \\
WT\_ALL & 7483 & 5580 & 7827 & 948 & 1497 & 1540 & 279 & 260 & 249 & 20950 & 21811 & 23501 \\
\multicolumn{13}{c}{k = 32} \\
Filter+TC & 510 & 649 & 2193 & 369 & 327 & 634 & 5 & 14 & 541 & 342 & 528 & 2326 \\
WT\_ALL & 10358 & 13142 & 11564 & 1973 & 1696 & 1617 & 496 & 517 & 498 & 46232 & 47935 & 48784 \\
\end{tabular}

1: Total query time in milliseconds on all data sets for fixed _m<sub>i</sub>_=3 and gap constraints \(C_S=\langle 100,110\rangle\), \(C_M=\langle 1000,1100\rangle\), and \(C_L=\langle 10000,11000\rangle\).

