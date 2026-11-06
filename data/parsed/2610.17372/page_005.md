<tbc>explore all possible simple paths only (without containing any loops) between every pair of vertices. However, there may be more than one such possible paths with different values of _pred<sup>pq</sup>_. Further, it may also be possible that with the same _pred<sup>pq</sup>_, there may be different values of \(I_s^{pq}\) and/or \(I_f^{pq}\) defining a path from _p_ to _q_. We construct a path matrix _P_ whose (_p,q)<sup>th</sup>_ entry will contain information about all such possible contact periods and will be represented as \((\nu_{pq},(I_s^{pq}[1],I_f^{pq}[1],pred^{pq}[1])\), \((I_s^{pq}[2],I_f^{pq}[2],pred^{pq}[2])\), \(\cdots\) , \((I_s^{pq}[\nu_{pq}],I_f^{pq}[\nu_{pq}],pred^{pq}[\nu_{pq}])\)), where \(\nu_{pq}\) is the number of possible paths from _p_ to _q_, and the 3-tuple \((I_s^{pq}[i],I_f^{pq}[i],pred^{pq}[i])\) contains information about the starting interval, finishing interval and the corresponding predecessor vertex of _q_ in the _i<sup>th</sup>_ path, \(1\le i\le\nu_{pq}\). As special cases, the entries of \(P(p,p),p\in V\) will be set to (0,(0,0,0)) and also when there will be no path from _p_ to _q_, the entries of _P(p,q_) will be set to \((0,(0,0,\infty))\).

With the above idea, the path matrix _P_ is first initialized based on 1-adjacency of the vertices, following the algorithm _initialize\_path\_matrix_ as shown in Procedure 2. After that, to find the all-pairs shortest time paths, we would augment each entry of the path matrix with information about other possible contacts (as expressed through a 3- tuple \((I_s^{pq}[i],I_f^{pq}[i],pred^{pq}[i])\)), if any, through more than one edge. Thus, the (_p,q)<sup>th</sup>_ entry of _P_ will finally contain information about all possible paths from _p_ to _q_ indicated by the \(\nu_{pq}\) 3-tuples \((I_s^{pq}[i],I_f^{pq}[i],pred^{pq}[i])\), \(1\le i\le\nu_{pq}\). Finally, from all these \(\nu_{pq}\) tuples, the one with the minimum value of \((I_f^{pq}[i]-I_s^{pq}[i])\) will be chosen as the path with the shortest time from _p_ to _q_.

To achieve the above objective of computing the final path matrix, we proceed as follows. Assume that we have already computed the contact information for a path from _p_ to _q_ with the corresponding entry in the path matrix _P(p,q_) as \((I_s^{pq}[i],I_f^{pq}[i],pred^{pq}[i])\). Suppose, from the vertex _q_, we would now like to reach another vertex _r_ adjacent to _q_ where _A(q,r_)=(_CS<sub>qr</sub>,d<sub>qr</sub>,t<sub>qr</sub>_). It will be possible to reach the vertex _r_ from _q_ if we find some \(j>I_f^{pq}[i]\) such that there is a run of \(1's\) of length _t<sub>qr</sub>_ in _CS<sub>qr</sub>_ starting from the interval _j_, i.e., \(CS_{qr}[j]=CS_{qr}[j+1]=\cdots=CS_{qr}[j+t_{qr}-1]=1\), for some \(j>I_f^{pq}[i]\). Once such a run is found, the total time of traversal from _p_ to _r_ will be \(j+t_{qr}-I_s^{pq}[i]\). The start time and finish time from _p_ to _r_ through _q_ will also be accordingly evaluated as \(I_s^{pq}[i]\) and _j+t<sub>qr</sub>_-1, respectively and _pred<sup>pr</sup>_\[_i_\] will be set to _q_. The corresponding 3-tuple \((I_s^{pq}[i],j+t_{qr}-1,q)\) will then be inserted as a new 3-tuple in _P(p,r_) in the sorted order of \((I_s^{pr},I_f^{pr})\) values provided there is no other existing 3-tuple with the same values of \((I_s^{pr},I_f^{pr})\), to avoid duplicate entries which might be generated in the above process of finding the possible contacts.

The above operation will be repeated with all the \(\nu_{pq}\) tuples \((I_s^{pq}[i],I_f^{pq}[i],pred^{pq}[i])\), \(1\le i\le\nu_{pq}\). Collectively, we denote all these operations symbolically by \(P(p,q)\otimes A(q,r)\). The algorithm for computing \(P(p,q)\otimes A(q,r)\) is presented in the form of _update\_all\_possible\_contacts(A,P,p,r_) as given in Procedure 3.

With these preliminary ideas, we describe below an algorithm for computing all-pairs shortest time paths as described in the next section.

## 5 ALGORITHM FOR COMPUTING ALL-PAIRS SHORTEST TIME PATHS

All-pairs shortest paths in static graphs can be very conveniently computed in two steps of a modified matrix multiplication scheme as proposed by Hu \[29\]. Let _D_ be the \(n\times n\) distance matrix of the static graph in which the (_p,q)<sup>th</sup>_ element _d<sub>pq</sub>_ is set to the distance from the vertex _p_ to vertex _q_. The concept given in \[29\] is to compute the product (in some sense) of the matrix _D_ by itself (\(D\times D\)) through in-place computation following some well-defined rules - i) an entry of the product matrix once evaluated will immediately replace the corresponding entry of only the left _D_ matrix in the above multiplication process, ii) the entries of the product matrix are computed once through a forward multiplication process and then through a backward multi

\begin{tabular}{cc}
\multicolumn{2}{c}{**Procedure 1:** _find\_next\_run(A,P,q,r,start,finish,flag_)} \\
\multicolumn{2}{c}{**Input:** _A,P,q,r,start,finish,flag_} \\
\multicolumn{2}{c}{**Output:** Updated start,finish,flag} \\
\multicolumn{2}{c}{_count_=0;} \\
\multicolumn{2}{c}{_flag_=0;} \\
\multicolumn{2}{c}{_j=start;_} \\
\multicolumn{2}{c}{_// next run of length t<sub>qr</sub> or more_} \\
\multicolumn{2}{c}{**while** _j\<= M AND flag_==0 do} \\
\multicolumn{2}{c}{**if** _CS<sub>qr</sub>_\[_j_\]==1 then} \\
\multicolumn{2}{c}{_count_++;_} \\
\multicolumn{2}{c}{**if** _count==t<sub>qr</sub>// a run of length t<sub>qr</sub> just found_} \\
\multicolumn{2}{c}{**then**} \\
\multicolumn{2}{c}{_start=j-t<sub>qr</sub>_+1;} \\
\multicolumn{2}{c}{**else**} \\
\multicolumn{2}{c}{**if** \(count\ge t_{qr}//\) a run of length t<sub>qr</sub> or greater is found**} \\
\multicolumn{2}{c}{**then**} \\
\multicolumn{2}{c}{_flag_=1;} \\
\multicolumn{2}{c}{_finish=j_-1;} \\
\multicolumn{2}{c}{_break;_} \\
\multicolumn{2}{c}{_count_=0;} \\
\multicolumn{2}{c}{_j_++;_} \\
\end{tabular}

