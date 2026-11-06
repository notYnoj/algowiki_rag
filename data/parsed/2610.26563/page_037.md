and hence

\(R_k=m\left(\frac{r}{m}\right)^k.\) (167)

In particular, one product of dimension _n<sup>k</sup>_ has rank at most _R<sub>k</sub>_. Taking _k_th roots and passing to the limit gives

\(n^\omega\le\frac{r}{m},\) (168)

or equivalently \(mn^\omega\le r\). If _m_ does not divide _r_, the same limit follows by applying the divisible case to the \(\ell\)th tensor power with rank bound \(m^\ell\lceil(r/m)^\ell\rceil\), taking \(\ell\)th roots, and letting \(\ell\rightarrow\infty\).

## B Prior matrix-multiplication algorithms

### B.1 Finite-base multiplication counts

4 lists the bases used in the comparison catalogue. Their padding-free recursive estimates are defined in (152).

LITA uses the rational construction at the cited revision \[22\]. The size-54 Smirnov base is the cyclic tensor product of three \(\langle 3,3,6\rangle\) rank-40 decompositions. The size-12 Bini base is the cyclic tensor product of three \(\langle 3,2,2\rangle\) rank-10 approximations. The size-1936 Schwartz–Zwecher count is the improved second-family bound, rather than the square of 36110.

For rectangular products, Pan’s aggregation identity generalizes to

\(R(\langle m,k,n\rangle\oplus\langle k,n,m\rangle)\le mkn+mk+kn+nm,\) (169)

\(\underline{R}(\langle m,k,n\rangle\oplus\langle k,n,m\rangle)\le mkn+mk+kn.\) (170)

The second bound follows by cyclically relabeling the dimensions in \[26, Eq. (3.1)\]. The earlier exact one- product family used below is

\(P_\mathrm{Pan}(q)=\frac{q^3-4q}{3}+6q^2(q\mathrm{even})\) (171)

\[25, 27\].

### B.2 Approximate steps with exact subproblems

The bilinear representations of Bini, Schönhage, and Smirnov supplied by Benson and Ballard \[6, 5\] have first- order approximation error in \(\lambda\). If \(A(\lambda)=\lambda^{-a}(A_0+O(\lambda))\) with \(A_0\neq 0\), then \(\|A(\lambda)\|_2=\lambda^{-a}(\|A_0\|_2+O(\lambda))\);<tbc>

\begin{tabular}{cccc}
Construction & base dimension _b_ & count _r<sub>b</sub>_ & type \\
Strassen \[36\] & 2 & 7 & exact \\
Laderman \[23\] & 3 & 23 & exact \\
Pan (1978) \[25\] & 70 & 143640 & exact \\
Pan (1982) \[26\] & 44 & 36133 & exact \\
Smirnov \[34\] & 54 & 64000 & exact \\
Sedoglavic–Smirnov \[32\] & 12 & 1040 & exact \\
Schwartz–Zwecher \[31\] & 44 & 36110 & exact \\
Schwartz–Zwecher \[31\] & 1936 & 1303676064 & exact \\
Dumas–Pernet–Sedoglavic \[18\] & 4 & 48 & exact \\
LITA \[22\] & 32 & 14197 & exact \\
Bini et al. \[7\] & 12 & 1000 & border rank \\
Smirnov \[34\] & 3 & 20 & border rank \\
Schönhage \[30\] & 3 & 21 & border rank \\
\end{tabular}

4: Prior square bases in the finite-size comparison.

