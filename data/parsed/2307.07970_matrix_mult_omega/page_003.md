In particular, we show that \(\alpha>0.321334\) (improving upon the previous bound 0.31389), \(\mu<0.527661\) (improving upon the previous bound 0.5286) and \(\omega(1,2,1)<3.250385\) (improving upon 3.25164).

As a consequence, Zwick’s algorithm for APSP in directed unweighted graphs (and several other algorithms, e.g., minimum witnesses for Boolean Matrix Multiplication \[CKL07\] and All-Pairs Bottleneck Paths in node-weighted graphs \[SYZ11\]) runs in _O(n_<sup>2.527661</sup>) time and 4-cliques can be found in _O(n_<sup>3.250385</sup>) time.

For many other bounds on rectangular matrix multiplication, see  1.

### Independent Work.

Independently, Le Gall \[LG24\] also obtained bounds on rectangular matrix multiplication, improving over \[LGU18\]. His method generalizes the approach of \[DWZ23\] to rectangular matrices. For technical reasons, the bound on \(\omega\) produced by his method does not match the bound in \[DWZ23\]. In comparison, our method is not only a generalization of \[DWZ23\] to rectangular matrices, but also an improvement. As a result, our bounds are better than the bounds in \[LG24\].

## 2 Technical Overview

### 2.1 Overview of Previous Work

For positive integers _a,b,c_, the \(a\times b\times c\) matrix multiplication tensor \(\langle a,b,c\rangle\) is a tensor over the variable sets \(\{x_{ij}\}_{i\in[a],j\in[b]}\), \(\{y_{jk}\}_{j\in[b],k\in[c]}\), \(\{z_{ki}\}_{k\in[c],i\in[a]}\) defined as the tensor computing the \(a\times c\) product matrix \(\{z_{ki}\}_{k\in[c],i\in[a]}\) of an \(a\times b\) matrix \(\{x_{ij}\}_{i\in[a],j\in[b]}\) and a \(b\times c\) matrix \(\{y_{jk}\}_{j\in[b],k\in[c]}\).<sup>1</sup> Specifically, \(\langle a,b,c\rangle\) can be written as the following trilinear form

\(\langle a,b,c\rangle=\sum_{i\in[a]}\sum_{j\in[b]}\sum_{k\in[c]}x_{ij}y_{jk}z_{ki}.\)

<sup>1</sup>For integer \(n\ge 0\), the notation \[_n_\] denotes {1_,...,n_}.

\begin{tabular}{ccc}
\(\kappa\) & upper bound on \(\omega(1,\kappa,1)\) & previous bound on \(\omega(1,\kappa,1)\) \\
**0.321334** & 2 & N/A \\
0.33 & 2.000100 & 2.000448 \\
0.34 & 2.000600 & 2.001118 \\
0.35 & 2.001363 & 2.001957 \\
0.40 & 2.009541 & 2.010314 \\
0.45 & 2.023788 & 2.024801 \\
0.50 & 2.042994 & 2.044183 \\
**0.527661** & 2.055322 & N/A \\
0.55 & 2.066134 & 2.067488 \\
0.60 & 2.092631 & 2.093981 \\
0.65 & 2.121734 & 2.123097 \\
0.70 & 2.153048 & 2.154399 \\
\end{tabular}

\begin{tabular}{ccc}
\(\kappa\) & upper bound on \(\omega(1,\kappa,1)\) & previous bound on \(\omega(1,\kappa,1)\) \\
0.75 & 2.186210 & 2.187543 \\
0.80 & 2.220929 & 2.222256 \\
0.85 & 2.256984 & 2.258317 \\
0.90 & 2.294209 & 2.295544 \\
0.95 & 2.332440 & 2.333789 \\
1.00 & **2.371552** & 2.371866 \\
1.10 & 2.452056 & 2.453481 \\
1.20 & 2.535063 & 2.536550 \\
1.50 & 2.794941 & 2.796537 \\
2.00 & 3.250385 & 3.251640 \\
2.50 & 3.720468 & 3.721503 \\
3.00 & 4.198809 & 4.199712 \\
\end{tabular}

1: Our bounds on \(\omega(1,\kappa,1)\) by analyzing the fourth power of the CW tensor compared to the best previous bounds. The previous bound for \(\kappa=1\) comes from \[DWZ23\]’s eighth-power analysis, while all other entries come from \[LGU18\].

