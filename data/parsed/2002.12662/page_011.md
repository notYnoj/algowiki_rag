# Fast Indexes for Gapped Pattern Matching

<tbc>and innovation programme under Marie Sklodowska-Curie grant agreement No 690941 (BIRDS).

### References

\begin{tabular}{ccccccccccccc}
\multirow{2}{*}{Method} & \multicolumn{3}{c}{CC} & \multicolumn{3}{c}{Kernel} & \multicolumn{3}{c}{Para} & \multicolumn{3}{c}{Proteins} \\
 & 3 & 5 & 7 & 3 & 5 & 7 & 3 & 5 & 7 & 3 & 5 & 7 \\
\multicolumn{13}{c}{k = 2} \\
Filter+TC & 1391 & 478 & 321 & 744 & 304 & 84 & 2243 & 629 & 75 & 388 & 33 & 24 \\
WT\_ALL & 17354 & 4535 & 2995 & 7393 & 1725 & 94 & 12372 & 9911 & 2435 & 8549 & 427 & 172 \\
\multicolumn{13}{c}{k = 4} \\
Filter+TC & 1099 & 327 & 179 & 664 & 132 & 64 & 1214 & 742 & 67 & 370 & 32 & 21 \\
WT\_ALL & 7452 & 2030 & 512 & 2201 & 145 & 31 & 6554 & 10908 & 2414 & 8486 & 96 & 68 \\
\multicolumn{13}{c}{k = 8} \\
Filter+TC & 2185 & 227 & 100 & 328 & 133 & 116 & 5 & 628 & 66 & 354 & 28 & 25 \\
WT\_ALL & 7919 & 1395 & 466 & 1885 & 154 & 47 & 237 & 16475 & 3563 & 11940 & 48 & 33 \\
\multicolumn{13}{c}{k = 16} \\
Filter+TC & 674 & 228 & 140 & 312 & 90 & 50 & 5 & 675 & 65 & 350 & 28 & 33 \\
WT\_ALL & 7483 & 925 & 365 & 948 & 129 & 80 & 279 & 29231 & 6222 & 20950 & 83 & 61 \\
\multicolumn{13}{c}{k = 32} \\
Filter+TC & 510 & 192 & 109 & 369 & 117 & 85 & 5 & 563 & 65 & 342 & 32 & 28 \\
WT\_ALL & 10358 & 1464 & 548 & 1973 & 274 & 167 & 496 & 64780 & 13435 & 46232 & 181 & 131 \\
\end{tabular}

2: Total query time in milliseconds for fixed gap constraint \(C_S=\langle 100,110\rangle\) for different subpattern lengths \(m_i\in\{3,5,7\}\) and different data sets.

