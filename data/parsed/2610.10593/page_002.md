<tbc>framework. We combine parameter sharing with mass-dependent conditioning and explicit correction of the extraction bottlenecks. The resulting construction proves the following algorithmic guarantee.

**Theorem 1.** _There is an algorithm for multiplying two_ \(n\times n\) _matrices over_ Q _using O(n_<sup>2.37115924</sup>) _arithmetic operations. More precisely, the square matrix multiplication exponent satisfies_

\(\omega_\mathbb{Q}<2.37115924.\)

_The same algorithmic guarantee holds over every characteristic-zero extension of_ Q_, including_ R _and_ C.

Relative to the bound of Dupont et al., the reduction in the exponent is \(1.776\cdot 10^{-5}\). This is an improvement in the polynomial growth rate of the arithmetic complexity: the corresponding leading powers of _n_ differ by a factor _n_<sup>0.00001776</sup>. As with other algorithms obtained through this tensor framework, the guarantee is asymptotic; the exponent alone does not specify a practical crossover size. A contemporaneous public computational release \[4\] reports an upper-bound expression approximately equal to 2.371169352063661; the present certified expression is also smaller than that value.

1 places the result among selected major improvements in the matrix multiplication exponent.

## Contributions.

The paper contributes a new certified matrix multiplication construction and a concrete combination of techniques for finding and verifying it:

\begin{tabular}{ccc}
Year & Work and reference & Bound on \(\omega\) \\
1969 & Strassen \[15\] & \(\le log_27<2.807355\) \\
1978 & Pan \[11\] & _\<_2.796 \\
1979 & Bini, Capovani, Romani, and Lotti \[3\] & _\<_2.7799 \\
1981 & Schönhage \[13\] & _\<_2.522 \\
1982 & Romani \[12\] & _\<_2.517 \\
1982 & Coppersmith and Winograd \[6\] & _\<_2.495548 \\
1986 & Strassen \[16\] & _\<_2.479 \\
1990 & Coppersmith and Winograd \[7\] & _\<_2.375477 \\
2010 & Stothers \[14\] & _\<_2.37369 \\
2012 & Vassilevska Williams \[17\] & _\<_2.3729 \\
2014 & Le Gall \[10\] & _\<_2.3728639 \\
2021 & Alman and Vassilevska Williams \[1\] & _\<_2.3728596 \\
2023 & Duan, Wu, and Zhou \[8\] & _\<_2.371866 \\
2024 & Vassilevska Williams et al. \[18\] & \(\le 2.371552\) \\
2025 & Alman et al. \[2\] & _\<_2.371339 \\
2026 & Dupont et al. \[9\] & _\<_2.371177 \\
2026 & BSD (public certificate) \[4\] & _\<_2.371169353 \\
2026 & **This paper** (Theorem 1) & _\<_**2.37115924** \\
\end{tabular}

1: Selected improvements in upper bounds on the matrix multiplication exponent. Years refer to the cited publications; some results appeared earlier in proceedings or preprints. The Vassilevska Williams entry uses a bound from the corrected full version. The BSD row is a public computational certificate, rather than a paper, and its bound is rounded upward from the exact rational certificate.

