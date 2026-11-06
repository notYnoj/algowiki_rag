<tbc>Some recent results in the literature have focused on instances other than the challenging ones presented above. A summary of these results and a comparison with PMS8 is presented in table 1. These results have been obtained on various types of hardware: single core, multi-core, GPU, grid. In the comparison, we try to match the number of processors whenever possible. However, the speed difference is large enough that the hardware is unlikely to play an important part.

\begin{tabular}{cccccc}
**Instance** & **qPMS7** & **PMS8<sup>1</sup>** & **PMS8<sup>16</sup>** & **PMS8<sup>32</sup>** & **PMS8<sup>48</sup>** \\
(13,4) & 29s & 7s & 3s & 2s & 2s \\
(15,5) & 3m & 48s & 5s & 4s & 3s \\
(17,6) & 11m & 6m & 22s & 12s & 9s \\
(19,7) & 55m & 27m & 2m & 52s & 37s \\
(21,8) & 4.9h & 1.6h & 7m & 4m & 3m \\
(23,9) & 27.1h & 5.5h & 22m & 11m & 8m \\
(25,10) & - & 15.5h & 1.0h & 31m & 21m \\
(26,11) & - & - & - & - & 46.9h \\
\end{tabular}

\begin{tabular}{cccccc}
Previous algorithm & Instance & Time & Cores & PMS8

Time & PMS8

Cores \\
Yu et al. 2012 \[15\], PairMotif & (27, 9) & 10h & 1 & 4s & 1 \\
\multirow{2}{*}{Desaraju and Mukkamala 2011 \[5\]} & (24,6) & 347s & 1 & 1s & 1 \\
 & (48,12) & 188s & 1 & 1s & 1 \\
\multirow{2}{*}{Dasari et al. 2011 \[3\], mSPELLER /

gSPELLER} & (21,8) & 3.7h & 16 & 7m & 16 \\
 & (21,8) & 2.2h & 4 GPUs x

240 cores & 7m & 16 \\
Dasari et al. 2010 \[2\], BitBased & (21,8) & 1.1h & & 7m & 16 \\
Dasari and Desh 2010 \[1\], BitBased & (21,8) & 6.9h & 16 & 7m & 16 \\
Sahoo et al. 2011 \[12\] & (16,4) & 106s & 4 & 1s & 1 \\
Sun et al. 2011 \[14\], TreeMotif & (40,14) & 6h & 1 & 6s & 1 \\
He et al. 2010 \[13\], ListMotif & (40,14) & 28,087s & 1 & 6s & 1 \\
Faheem 2010 \[8\], skip-Brute Force & (15,4) & 2934s & 96 nodes & 1s & 1 \\
\multirow{3}{*}{Ho et al. 2009 \[9\], iTriplet} & (24,8) & 4h & 1 & 5s & 1 \\
 & (38,12) & 1h & 1 & 1s & 1 \\
 & (40,12) & 5m & 1 & 1s & 1 \\
\end{tabular}

5
4.5
4
3.5
3
Speedup
2.5
2
1.5
1
(13,4)
(15,5)
(17,6)
(19,7)
(21,8)
(23,9)
Instance

**Fig.6.** Comparison between qPMS7 and PMS8 on challenging instances. PMS8_<sup>P</sup>_ means PMS8 used _P_ CPU cores.

**Fig.7.** Speedup of PMS8 single core over qPMS7.

** 1.** Side by side comparison between previous results in the literature and PMS8. Time is reported in seconds (s), minutes (m) or hours (h).

