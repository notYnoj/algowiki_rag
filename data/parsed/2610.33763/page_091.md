_m_ grow proportionally. The described behaviour agrees with the negative results in \[97, 123\], where theoretical barriers to the optimality of preconditioned Krylov solvers are proven.

**Remark 6.6** _ 6.1 also reports the measured CPU timings, even if, in this setting, they do not compare the preconditioned and non-preconditioned cases in a totally meaningful way. In fact, since the algorithms are implemented in MATLAB, we are limited in our ability to optimize the code compared with what is possible in more sophisticated programming languages. Therefore, the measured CPU time also reflects implementation-specific overhead rather than the intrinsic efficiency of the algorithms, and may therefore be misleading._

\begin{tabular}{ccccccccccccc}
 & & \multicolumn{4}{c}{\(\xi=0.2\)} & \multicolumn{4}{c}{\(\xi=0.5\)} & \multicolumn{4}{c}{\(\xi=0.8\)} \\
 & & \multicolumn{4}{c}{\(\eta=0.8\)} & \multicolumn{4}{c}{\(\eta=0.5\)} & \multicolumn{4}{c}{\(\eta=0.2\)} \\
 & & \multicolumn{2}{c}{Iter} & \multicolumn{2}{c}{CPU} & \multicolumn{2}{c}{Iter} & \multicolumn{2}{c}{CPU} & \multicolumn{2}{c}{Iter} & \multicolumn{2}{c}{CPU} \\
_n_ & _m_ & - & _P<sub>N</sub>_ & - & _P<sub>N</sub>_ & - & _P<sub>N</sub>_ & - & _P<sub>N</sub>_ & - & _P<sub>N</sub>_ & - & _P<sub>N</sub>_ \\
2<sup>4</sup> & 2<sup>4</sup> & 66 & 15 & 0.11 & 0.03 & 53 & 17 & 0.02 & 0.01 & 45 & 16 & 0.03 & 0.01 \\
2<sup>4</sup> & 2<sup>5</sup> & 62 & 16 & 0.04 & 0.02 & 60 & 17 & 0.04 & 0.02 & 63 & 16 & 0.03 & 0.01 \\
2<sup>4</sup> & 2<sup>6</sup> & 64 & 17 & 0.06 & 0.03 & 67 & 17 & 0.07 & 0.03 & 86 & 17 & 0.08 & 0.03 \\
2<sup>4</sup> & 2<sup>7</sup> & 61 & 17 & 0.11 & 0.05 & 67 & 17 & 0.13 & 0.06 & 141 & 17 & 0.30 & 0.05 \\
2<sup>4</sup> & 2<sup>8</sup> & 61 & 17 & 0.37 & 0.15 & 79 & 17 & 0.49 & 0.15 & 230 & 16 & 2.02 & 0.14 \\
2<sup>5</sup> & 2<sup>4</sup> & 107 & 26 & 0.04 & 0.01 & 75 & 30 & 0.02 & 0.02 & 49 & 28 & 0.01 & 0.01 \\
2<sup>5</sup> & 2<sup>5</sup> & 110 & 27 & 0.08 & 0.04 & 79 & 29 & 0.05 & 0.03 & 68 & 27 & 0.04 & 0.03 \\
2<sup>5</sup> & 2<sup>6</sup> & 110 & 27 & 0.16 & 0.06 & 86 & 29 & 0.12 & 0.06 & 90 & 27 & 0.13 & 0.06 \\
2<sup>5</sup> & 2<sup>7</sup> & 103 & 27 & 0.50 & 0.15 & 89 & 29 & 0.41 & 0.16 & 142 & 27 & 0.77 & 0.15 \\
2<sup>5</sup> & 2<sup>8</sup> & 100 & 27 & 1.20 & 0.42 & 96 & 30 & 1.13 & 0.47 & 230 & 28 & 3.76 & 0.43 \\
2<sup>6</sup> & 2<sup>4</sup> & 213 & 36 & 0.17 & 0.03 & 101 & 49 & 0.06 & 0.04 & 51 & 40 & 0.02 & 0.03 \\
2<sup>6</sup> & 2<sup>5</sup> & 211 & 35 & 0.32 & 0.05 & 103 & 48 & 0.11 & 0.07 & 71 & 39 & 0.06 & 0.06 \\
2<sup>6</sup> & 2<sup>6</sup> & 207 & 36 & 1.34 & 0.14 & 110 & 47 & 0.43 & 0.20 & 94 & 39 & 0.31 & 0.15 \\
2<sup>6</sup> & 2<sup>7</sup> & 193 & 37 & 2.05 & 0.37 & 109 & 48 & 0.84 & 0.47 & 145 & 41 & 1.30 & 0.39 \\
2<sup>6</sup> & 2<sup>8</sup> & 194 & 36 & 4.48 & 1.13 & 117 & 49 & 2.27 & 1.54 & 231 & 40 & 5.65 & 1.26 \\
2<sup>7</sup> & 2<sup>4</sup> & 503 & 46 & 1.46 & 0.08 & 136 & 71 & 0.16 & 0.12 & 56 & 57 & 0.05 & 0.13 \\
2<sup>7</sup> & 2<sup>5</sup> & 493 & 46 & 6.68 & 0.18 & 136 & 71 & 0.66 & 0.32 & 76 & 56 & 0.25 & 0.24 \\
2<sup>7</sup> & 2<sup>6</sup> & 458 & 46 & 8.78 & 0.36 & 137 & 70 & 1.07 & 0.59 & 98 & 56 & 0.60 & 0.45 \\
2<sup>7</sup> & 2<sup>7</sup> & 440 & 46 & 11.96 & 0.88 & 136 & 72 & 1.80 & 1.64 & 146 & 56 & 2.42 & 1.44 \\
2<sup>7</sup> & 2<sup>8</sup> & 436 & 48 & 28.55 & 3.20 & 138 & 71 & 5.55 & 5.67 & 232 & 56 & 10.76 & 3.90 \\
2<sup>8</sup> & 2<sup>4</sup> & 1237 & 60 & 37.41 & 0.31 & 181 & 101 & 1.10 & 0.62 & 59 & 77 & 0.18 & 0.43 \\
2<sup>8</sup> & 2<sup>5</sup> & 1165 & 59 & 50.73 & 0.53 & 174 & 100 & 1.53 & 0.99 & 78 & 76 & 0.39 & 0.73 \\
2<sup>8</sup> & 2<sup>6</sup> & 1149 & 58 & 68.13 & 1.10 & 171 & 99 & 2.30 & 1.99 & 100 & 76 & 1.01 & 1.43 \\
2<sup>8</sup> & 2<sup>7</sup> & 1044 & 59 & 92.23 & 3.03 & 168 & 100 & 4.67 & 5.41 & 150 & 76 & 3.92 & 3.85 \\
2<sup>8</sup> & 2<sup>8</sup> & 985 & 60 & 151.27 & 8.66 & 166 & 101 & 11.27 & 15.08 & 234 & 76 & 17.51 & 10.48 \\
\end{tabular}

6.1: Iterations and CPU times required for solving the linear system with the GMRES method, without and with the preconditioner, for various choices of the fractional orders.

