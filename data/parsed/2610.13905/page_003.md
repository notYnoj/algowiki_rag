<tbc>APA algorithms for arbitrary \(A\in\mathbb{C}^{m\times k}\) and \(B\in\mathbb{C}^{k\times n}\) of degree _dL_, where

\(L\le\left\{\mathrm{log}_{m_0}(m),\mathrm{log}_{n_0}(n),\mathrm{log}_{k_0}(k)\right\}\) (1.4)

is the number of recursive steps applied. Since the complexity of these algorithms depends primarily on the number of scalar multiplications in the base case routine - and this is potentially smaller than what can be achieved with a fast exact algorithm, as demonstrated in Figure 1 - APA matrix multiplication can be, asymptotically, faster than exact matrix multiplication. Despite this, APA algorithms are typically not used in practice. One reason is apparent from Figure 1: APA matrix multiplication requires dividing by \(\varepsilon\), which means we cannot hope to use it in the limit \(\varepsilon\rightarrow 0\) to obtain the exact product _C=AB_ (at least in the presence of floating-point roundoff).

Nevertheless, as outlined by Bini in \[9\], an APA algorithm _can_ be used to obtain an exact product of two matrices. Suppose that we evaluate a degree _d_ APA algorithm _d_+1 times with distinct evaluation parameters \(\varepsilon_1,\dots,\varepsilon_{d+1}\). If _C<sub>i</sub>_ is the output of the _i_-th evaluation, and moreover if \(\alpha_1,\dots,\alpha_{d+1}\) solve the<tbc>

\begin{tabular}{ccccc}
\(\left(\begin{array}{ c c }
a_{11} & a_{12} \\
a_{21} & a_{22} \\
a_{31} & a_{32}
\end{array}\right)\times\left(\begin{array}{ c c }
b_{11} & b_{12} \\
b_{21} & b_{22}
\end{array}\right)=\left(\begin{array}{ c c }
c_{11} & c_{12} \\
c_{21} & c_{22} \\
c_{31} & c_{32}
\end{array}\right)\) & & \\
(a) Classical & (b) Fast exact \[59\] & (c) APA \[10\] & \\
\end{tabular}

Figure 1: Three algorithms for \(\langle 3,2,2\rangle\) matrix multiplication using 12, 11, and 10 scalar multiplications, respectively. The fast exact algorithm is obtained by applying Strassen’s \(\langle 2,2,2;7\rangle\) routine to compute the upper \(2\times 2\) block of the output, while the APA algorithm is exact as \(\varepsilon\rightarrow 0\).

