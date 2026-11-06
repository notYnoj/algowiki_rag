\begin{tabular}{cccccccc}
 & & \multicolumn{3}{c}{\((\ell=8,d=3)\)} & \multicolumn{3}{c}{\((\ell=8,d=5)\)} \\
Dataset & Method & Reduced

solution size & Full

solution size & Coverage & Reduced

solution size & Full

solution size & Coverage \\
\multirow{3}{*}{E. coli} & Exact & 6200 & 10,000 & -- & 8521 & 10,000 & -- \\
 & M-SLIDER & 9916 & 10,000 & 75.01% & 2301 & 2302 & 45.33% \\
 & SEQ-SLIDER & 694 & 10,000 & **85.61**% & 9959 & 10,000 & **93.70**% \\
\multirow{3}{*}{S. cerevisiae I} & Exact & 231 & 10,000 & -- & 10,000 & 10,000 & -- \\
 & M-SLIDER & 9980 & 10,000 & 100.00% & 363 & 363 & 9.79% \\
 & SEQ-SLIDER & 1337 & 10,000 & **100.00**% & 10,000 & 10,000 & **77.20**% \\
\multirow{3}{*}{D. melanogaster} & Exact & 893 & 10,000 & -- & 10,000 & 10,000 & -- \\
 & M-SLIDER & 9890 & 10,000 & 85.55% & 149 & 149 & 3.19% \\
 & SEQ-SLIDER & 1311 & 10,000 & **100.00**% & 10,000 & 10,000 & **45.17**% \\
\multirow{3}{*}{A. thaliana} & Exact & 3460 & 10,000 & -- & 10,000 & 10,000 & -- \\
 & M-SLIDER & 10,000 & 10,000 & 4.65% & 168 & 168 & 5.76% \\
 & SEQ-SLIDER & 2384 & 10,000 & **8.12**% & 10,000 & 10,000 & **21.38**% \\
\multirow{3}{*}{H. sapiens I} & Exact & 1836 & 10,000 & -- & 9992 & 10,000 & -- \\
 & M-SLIDER & 9996 & 10,000 & **58.27**% & 187 & 187 & 3.71% \\
 & SEQ-SLIDER & 3057 & 10,000 & 52.34% & 10,000 & 10,000 & **11.67**% \\
\multirow{3}{*}{S. cerevisiae II} & Exact & 5989 & 10,000 & -- & 9996 & 10,000 & -- \\
 & M-SLIDER & 9909 & 10,000 & 28.63% & 9988 & 10,000 & 38.56% \\
 & SEQ-SLIDER & 5792 & 10,000 & **78.56**% & 9993 & 10,000 & **91.79**% \\
\multirow{3}{*}{H. sapiens II} & Exact & 6197 & 10,000 & -- & 10,000 & 10,000 & -- \\
 & M-SLIDER & 10,000 & 10,000 & 9.95% & 472 & 472 & 4.97% \\
 & SEQ-SLIDER & 4558 & 10,000 & **17.50**% & 10,000 & 10,000 & **28.97**% \\
\end{tabular}

C.2: Coverage of _S_<sub>Exact</sub> by _S_<sub>SEQ-SLIDER</sub> and _S_<sub>M-SLIDER</sub> for _h_=8 and threshold \(\tau=70\%\). Values for _S_<sub>Exact</sub> are omitted as they are (trivially) 100%.

