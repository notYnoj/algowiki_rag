<tbc>Because of all this, it is conceivable that TED is similarly difficult and that (w.r.t. Question 1) only small polylogarithmic improvements are potentially attainable and (w.r.t. Question 2) it is truly harder than APSP.

A third question concerns the unweighted TED problem. Mao \[Mao22\] showed that a truly subcubic running time is possible for the problem. The current record for the running time is by Dürr \[Dür23\] and is \(\tilde{\mathcal{O}}(n^{(4\omega+12)/(\omega+5)}=\mathcal{O}(n^{2.9148})\).<sup>1</sup> Here, \(\omega\) is the \(n\times n\) matrix multiplication exponent, where one can multiply two \(n\times n\) matrices in \(\mathcal{O}(n^{\omega+\varepsilon})\) time for all \(\varepsilon>0\).<sup>2</sup> The current bound on \(\omega\), due to \[ADV<sup>+</sup>25\], is \(\omega\le 2.371339\).

There are many structured variants of problems related to APSP and for a very large number of them, shortly after a truly subcubic time algorithm was found, an \(\tilde{\mathcal{O}}(n^{(3+\omega)/2})\) time (or better) algorithm was also found. There are many such examples, we present a few:

The All Pairs Bottleneck Paths \[VWY09\] and All pairs nondecreasing paths \[Vas10\] problems were first shown to have truly subcubic time algorithms in the first decade of the century and are now both known to be solvable in \(\tilde{\mathcal{O}}(n^{(3+\omega)/2})\) time \[DJW19, DP09\].<tbc>

The Min-Plus product of \(n\times n\) matrices (given _A_, _B_, compute _C_ with C\[_i,j_\] = min_<sub>k</sub>(A_\[_i,k_\] + _B_\[_k,j_\]) is known to be equivalent to APSP in _n_-node graphs \[FM71\] so that under the APSP Hypothesis it requires _n_<sup>3-_o_(1)</sup> time. Various structured variants of the Min-Plus matrix product have been shown to have truly subcubic time algorithms, e.g. when the matrices have "bounded differences" \[BGSV19\] or whose entries are bounded by O(_n_) and are monotone (non-decreasing in the rows or columns) \[VX20, GPVX21\]. Later, \[CDXZ22\] showed that these variants can be solved in \(\tilde{\mathcal{O}}(n^{(3+\omega)/2})\) time. These structured Min-Plus products have many applications for a variety of fundamental problems, e.g. to many sequence similarity problems such as Language Edit Distance (aka Scored Parsing<tbc>

<sup>1</sup> \(\tilde{\mathcal{O}}\) hides poly-logarithmic factors. <sup>2</sup> Slightly abusing notation, we omit this \(\varepsilon\) from the rest of the paper, which is in line with the literature. The reader should be aware that in many running times in the literature that one states in terms of \(\omega\), a secret \(\varepsilon\) is always hiding. The running times with a numerical-valued exponent use a strict upper bound on \(\omega\) (such as the O(_n_<sup>2.9546</sup>) running time for unweighted TED of \[Mao22\]), so this \(\varepsilon\) does not appear.

\begin{tabular}{ccc}
**Work** & **Setting** & **Complexity** \\
Tai \[Tai79\] & weighted & O(_n_<sup>6</sup>) \\
Shasha, Zhang \[ZS89\] & weighted & O(_n_<sup>4</sup>) \\
Klein \[Kle98\] & weighted & O(_n_<sup>3</sup>log_n_) \\
Demaine, Mozes, Rossman, Weimann \[DMRW10\] & weighted & O(_n_<sup>3</sup>) \\
Bringmann, Gawrychowski, Mozes, Weinmann \[BGMW20\] & weighted & no \(\mathcal{O}(n^{3-\varepsilon})\) algorithm under APSP \\
Mao \[Mao22\] & unweighted & \(\tilde{\mathcal{O}}(n^{(4\omega+12)/(\omega+5)})=\mathcal{O}(n^{2.9148})\) \\
**This work** & **weighted** & \(n^3/2^{\Omega(\sqrt{\mathrm{log}n})}\) \\
**This work** & **unweighted** & \(\tilde{\mathcal{O}}(n^{(3+\omega)/2})=\mathcal{O}(n^{2.6857})\) \\
\end{tabular}

** 1** Computational bounds of TED across different works. In the unweighted setting, complexities are computed using the best known bound on the matrix multiplication exponent \(\omega\le 2.371339\) from \[ADV<sup>+</sup>25\]. The stated bound for \[Mao22\] additionally uses results on Rectangular Bounded Monotone Min-plus Product by Dürr \[Dür23\].

