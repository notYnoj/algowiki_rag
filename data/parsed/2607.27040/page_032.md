\begin{tabular}{cc}
**Notation** & **Definition** \\
_r<sub>#</sub>_ & Number of representatives. \\
_s<sub>#</sub>_ & Number of active representatives, equivalent to the definition in  E.2. \\
_R_ & Block of all _r<sub>#</sub>_ representatives. \\
_Ri<sub>i</sub>_ & The _i_th representatives. \\
\(R'_1\) & The _i_th active representative. \\
_L_ & Library zone, containing sorted sequence of all active representatives \(R'_1\dots R'_{s_\#}\) interlaced with buffer positions. \\
_L<sub>i</sub>_ & The _i_th gap in _L_; a contiguous block of 8 representatives \(\ell_1\dots\ell_8\). \\
\(s'_\#\) & Number of gaps in _L_. \\
\(L_1\dots L_{s_\#}^\prime\) & Gaps in the library, which are contiguous blocks of 8 representatives \(\ell_1\dots\ell_8\). \\
_D_ & Rebuild buffer. \\
\(n_1\dots n_{2s_\#^\prime-1}\) & Logical segment tree over gaps _L_<sub>1</sub>_...L<sub>s<sub>#</sub></sub>_. \\
size(_n<sub>i</sub>_) & Number of active representatives in gaps covered by node _n<sub>i</sub>_. \\
span(_n<sub>i</sub>_) & Number of gaps covered by node _n<sub>i</sub>_. \\
\(\psi(n_i)\) & Imbalance of node _n<sub>i</sub>_, used for amortized analysis. \\
\end{tabular}

\begin{tabular}{cc}
**Notation** & **Definition** \\
\(m'\) & size of small subsequence to be sorted. \\
_w_ & size of each word. \\
\(A'\) & Small subsequence of \(m'\) active elements. \\
\(B'\) & Merge buffer of \(m'\) buffer elements. \\
_k_ & size of runs sorted by table sort/number of runs in a group merged at once. \\
_k<sub>#</sub>_ & Number of merge passes to sort \(A'\). \\
_r<sub>i</sub>_ & size of runs after the _i_th merge pass (excluding the last run that is potentially short). \\
_A<sub>i</sub>_ & The _i_th sorted run from the previous merge pass. \\
_B<sub>i</sub>_ & The _i_th block of buffer elements reserved for merging the _i_th group of _k_ runs. \\
\(k'\) & Number of runs merged in the final merge pass. \\
\end{tabular}

\begin{tabular}{cc}
**Notation** & **Definition** \\
\multicolumn{2}{c}{Randomized Approach} \\
_g_ & Max capacity of a cache line. \\
_gi_ & The _i_th element in a cache line. \\
_d_ & The cache integer to store integers from 0 to _g_ made up of bits _d_<sub>0</sub>_...d_<sub>\(\lfloor lgg\rfloor\)</sub> where _d<sub>j</sub>_ has priority 2_<sup>j</sup>_. \\
\multicolumn{2}{c}{Deterministic Approach} \\
_t_ & Parameter for comparisons moves tradeoff, obeys \(2\le t\le lg^*n-1\). \\
\(t'\) & Number of levels in a cache line, follows \(t'\le t-1\) by definition. \\
_G<sub>i</sub>_ & The cache block at level _i_. \\
\end{tabular}

** E.3:** Section 2.2 and App. A Notation

** E.4:** Section 2.3 and App. B Notation

** E.5:** Section 2.6 and App. C Notation

