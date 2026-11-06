The testing dataset is randomly generated according to the FM (fixed number of mutation) model \[16\]. We have used it in our experiment and showed the result in table 3.3 and table 3.4. Our algorithm shows a little better result than Algorithm TraverStringRef in some challenging states. Although it lags behind the qPMS9 in all cases. The comparisons are shown in table 3.3, table 3.4, fig. 3.4, fig. 3.5.

\begin{tabular}{cc}
Parameter & Setting \\
\(|\Sigma|\) & 4 (DNA) \\
_n_ & 20 \\
_m_ & 600 \\
_q_ & 10,20 \\
_l_ & 13, 15, 17,... \\
\end{tabular}

\begin{tabular}{ccccccc}
**Algorithm** & **(13,4)** & **(15,5)** & **(17,6)** & **(19,7)** & **(21,8)** & **(23,9)** \\
**qPMS-Sigma** & 12s & 50s & 165s & 755s & 2909s & 12153s \\
**TraverStringRef** & 11s & 47s & 179s & 745s & 3098s & 13027s \\
**qPMS7** & 14s & 133s & 1046s & 8465s & 71749s & \\
**PMS8** & 7s & 48s & 312s & 1596s & 5904s & 19728s \\
**qPMS9** & 6s & 34s & 162s & 804s & 2724s & 8136s \\
\end{tabular}

\begin{tabular}{ccccccc}
**Algorithm** & **(13,4)** & **(15,5)** & **(17,6)** & **(19,7)** & **(21,8)** & **(23,9)** \\
**TraverStringRef** & 7 & 36 & 160 & 760.6 & 3643.3 & 17232.4 \\
**TraverStringRef** & 5.5 & 32 & 166.1 & 779.9 & 3700.6 & 17922.2 \\
**qPMS7** & 31 & 152 & 850.7 & & 4865.0 & 29358 \\
**qPMSPrune** & 12.8 & 126.7 & 1116.5 & 10540.8 & & \\
**PMS9** & & & & & & \\
\end{tabular}

3.2: Parameter Setting for Testing Data Set

3.3: Computational Results for DNA Sequences for _q_=20

3.4: Computational Results for DNA Sequences for _q_=10

