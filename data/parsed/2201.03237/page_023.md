\begin{tabular}{cccccc}
Dataset & Algorithm & Size & AOD & MOD & Time \\
\multirow{5}{*}{Sift} & HNSW & 220.4 & 30 & 50 & 295 \\
 & KGraph & 408 & 100 & 100 & 88 \\
 & DPG & 191.3 & 45 & 261 & 88+30 \\
 & NSSG & 160.7 & 39 & 50 & 115+75 \\
 & TBSG & 174.7 & 40 & 50 & 115+80 \\
\multirow{5}{*}{Gist} & HNSW & 296 & 25 & 70 & 3021 \\
 & KGraph & 1608 & 400 & 400 & 1202 \\
 & DPG & 308 & 75 & 7721 & 1202+74 \\
 & NSSG & 143.5 & 34 & 70 & 1202+341 \\
 & TBSG & 195 & 44 & 70 & 1202+313 \\
\multirow{5}{*}{Glove} & HNSW & 254 & 18 & 50 & 1670 \\
 & KGraph & 1903 & 400 & 400 & 905 \\
 & DPG & 956 & 200 & 200 & 905+1370 \\
 & NSSG & 107 & 21 & 50 & 905+156 \\
 & TBSG & 204 & 42 & 80 & 1198+119 \\
\multirow{5}{*}{Crawl} & HNSW & 352 & 13 & 40 & 1952 \\
 & KGraph & 3199 & 400 & 400 & 1190 \\
 & DPG & 812 & 100 & 100 & 1190+651 \\
 & NSSG & 187 & 22 & 40 & 1190+380 \\
 & TBSG & 221 & 26 & 50 & 1190+188 \\
\end{tabular}

3: We list some important information of graph-based indexes, including the average out-degree(AOD), maximum out-degree(MOD), index size(Size)(MB) and index time(Time)(sec). Index size refers to the size of the index stored on the disk.

