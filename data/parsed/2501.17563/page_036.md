## B.1 About the

You may find the code on Arxiv, "hidden" as additional source file named "_STTLP-sage-python3- source.zip_" in the source-code of this paper (before it was compiled to the PDF file that you are reading). The archive contains a few scripts, and a few generated logs.

The code is written in Sage language \[3\], whose syntax is mostly that of Python 3. In fact, some functionality of the code can be run purely in python, such as analyzing topologies and enumerating their STTs. However, the "core" of solving LPs and manipulating polytopes does require Sage.

The code is divided to multiple scripts, based on a logical division that is explained in an opening comment within each file. The main script also has functions dedicated to reproducibility, to enable a relatively simple way to compute the various results discussed throughout the paper. While the code has been cleaned and made readable, this is by no means "production level" code.

In order to run the code, you need a standard installation of Sage (and, indirectly of Python 3), and to make sure that you have the ‘networkx’ python package installed (other imported packages such as ‘time’ and ‘math’ are standard in python). It is possible to install Sage locally, further details are on the web \[2\]. For running short code, you may also use an online server such as \[1\]. "Short" mostly refers to time, each run is terminated after about a minute or two. There is also a limit to the length of the script, which is not reached with "reasonable" code, but can be reached if the script contains long hard-coded values.<sup>14</sup>

<sup>14</sup>There are ≈2000 different primary directions which find non-integer vertices (not all unique), for each of the seven small topologies. Computing them is slow, so we pre-computed and hard-coded them and other demanding computations. This makes the code long, and as a side-effect we have these values documented.

\begin{tabular}{ccccccccc}
_U_<sub>(_n,i_)</sub> & _D_ & Edges & _U_<sub>(_n,i_)</sub> & _D_ & \multicolumn{4}{c}{Edges} \\
(3,0) & 2 & (1,2), (2,3) & (8,0) & 7 & (1,2), (2,3), (3,4), (4,5), (5,6), (6,7), (7,8) & & & \\
(4,0) & 3 & (1,2), (2,3), (3,4) & (8,1) & 6 & (1,2), (2,3), (2,8), (3,4), (4,5), (5,6), (6,7) & & & \\
(4,1) & 2 & (1,2), (2,3), (2,4) & (8,2) & 6 & (1,2), (2,3), (3,4), (3,8), (4,5), (5,6), (6,7) & & & \\
(5,0) & 4 & (1,2), (2,3), (3,4), (4,5) & (8,3) & 6 & (1,2), (2,3), (3,4), (4,5), (4,8), (5,6), (6,7) & & & \\
(5,1) & 3 & (1,2), (2,3), (2,5), (3,4) & (8,4) & 5 & (1,2), (2,3), (3,4), (3,7), (4,5), (5,6), (7,8) & & & \\
(5,2) & 2 & (1,2), (2,3), (2,4), (2,5) & (8,5) & 5 & (1,2), (2,3), (2,7), (3,4), (3,8), (4,5), (5,6) & & & \\
(6,0) & 5 & (1,2), (2,3), (3,4), (4,5), (5,6) & (8,6) & 5 & (1,2), (2,3), (2,7), (3,4), (4,5), (4,8), (5,6) & & & \\
(6,1) & 4 & (1,2), (2,3), (2,6), (3,4), (4,5) & (8,7) & 5 & (1,2), (2,3), (3,4), (3,7), (4,5), (4,8), (5,6) & & & \\
(6,2) & 4 & (1,2), (2,3), (3,4), (3,6), (4,5) & (8,8) & 5 & (1,2), (2,3), (2,7), (2,8), (3,4), (4,5), (5,6) & & & \\
(6,3) & 3 & (1,2), (2,3), (2,5), (3,4), (3,6) & (8,9) & 5 & (1,2), (2,3), (3,4), (3,7), (3,8), (4,5), (5,6) & & & \\
(6,4) & 3 & (1,2), (2,3), (2,5), (2,6), (3,4) & (8,10) & 5 & (1,2), (2,3), (2,7), (3,4), (4,5), (5,6), (5,8) & & & \\
(6,5) & 2 & (1,2), (2,3), (2,4), (2,5), (2,6) & (8,11) & 4 & (1,2), (2,3), (3,4), (3,6), (3,7), (4,5), (7,8) & & & \\
(7,0) & 6 & (1,2), (2,3), (3,4), (4,5), (5,6), (6,7) & (8,12) & 4 & (1,2), (2,3), (2,6), (3,4), (3,7), (4,5), (7,8) & & & \\
(7,1) & 5 & (1,2), (2,3), (2,7), (3,4), (4,5), (5,6) & (8,13) & 4 & (1,2), (2,3), (2,6), (3,4), (3,7), (4,5), (4,8) & & & \\
(7,2) & 5 & (1,2), (2,3), (3,4), (3,7), (4,5), (5,6) & (8,14) & 4 & (1,2), (2,3), (2,6), (2,7), (3,4), (3,8), (4,5) & & & \\
(7,3) & 4 & (1,2), (2,3), (3,4), (3,6), (4,5), (6,7) & (8,15) & 4 & (1,2), (2,3), (2,6), (3,4), (3,7), (3,8), (4,5) & & & \\
(7,4) & 4 & (1,2), (2,3), (3,4), (4,5), (4,6), (4,7) & (8,16) & 4 & (1,2), (2,3), (2,6), (3,4), (4,5), (4,7), (4,8) & & & \\
(7,5) & 4 & (1,2), (2,3), (3,4), (3,6), (4,5), (4,7) & (8,17) & 4 & (1,2), (2,3), (3,4), (3,6), (3,7), (3,8), (4,5) & & & \\
(7,6) & 4 & (1,2), (2,3), (3,4), (3,6), (3,7), (4,5) & (8,18) & 4 & (1,2), (2,3), (2,6), (2,7), (2,8), (3,4), (4,5) & & & \\
(7,7) & 4 & (1,2), (2,3), (2,6), (3,4), (4,5), (4,7) & (8,19) & 3 & (1,2), (2,3), (2,5), (2,6), (3,4), (3,7), (3,8) & & & \\
(7,8) & 3 & (1,2), (2,3), (2,5), (3,4), (3,6), (3,7) & (8,20) & 3 & (1,2), (2,3), (2,5), (2,6), (2,7), (3,4), (3,8) & & & \\
(7,9) & 3 & (1,2), (2,3), (3,4), (3,5), (3,6), (3,7) & (8,21) & 3 & (1,2), (2,3), (2,5), (2,6), (2,7), (2,8), (3,4) & & & \\
(7,10) & 2 & (1,2), (2,3), (2,4), (2,5), (2,6), (2,7) & (8,22) & 2 & (1,2), (2,3), (2,4), (2,5), (2,6), (2,7), (2,8) & & & \\
\end{tabular}

7: A correspondence between topology name _U_<sub>(_n,i_)</sub> (size _n_ and index _i_) to an explicit list of edges. _D_ is short for edge-diameter.

