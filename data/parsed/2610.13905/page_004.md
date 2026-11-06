<tbc>Vandermonde system

\(\left(\begin{array}{ c c c c c }
1 & 1 & \cdots & 1 \\
\varepsilon_1 & \varepsilon_2 & \cdots & \varepsilon_{d+1} \\
\vdots & \vdots &  & \vdots \\
\varepsilon_1^d & \varepsilon_2^d & \cdots & \varepsilon_{d+1}^d
\end{array}\right)\left(\begin{array}{ c }
\alpha_1 \\
\alpha_2 \\
\vdots \\
\alpha_{d+1}
\end{array}\right)=\left(\begin{array}{ c }
1 \\
0 \\
\vdots \\
0
\end{array}\right),\) (1.5)

then by construction

\(\alpha_1C_1+\cdots+\alpha_{d+1}C_{d+1}=\left(\sum_{i=1}^{d+1}\alpha_i\right)AB+\left(\sum_{i=1}^{d+1}\alpha_i\varepsilon_i\right)R_1+\cdots+\left(\sum_{i=1}^{d+1}\alpha_i\varepsilon_i^d\right)R_d=AB.\) (1.6)

In the recursive setting, (1.4) implies that the number of evaluations necessary to obtain the exact product of arbitrary \(A\in\mathbb{C}^{m\times k}\) and \(B\in\mathbb{C}^{k\times n}\) has logarithmic dependence on the size of the matrices.<sup>4</sup> That is, the complexity of an APA matrix multiplication algorithm is \(O(L\cdot(mkn)^{log_{m_0k_0n_0}(t)})\), where _L_ must satisfy (1.4) with equality to get the improved exponent.

The extra logarithmic factor here implies that, while the exponent \(\omega=log_{m_0k_0n_0}(t)\) may be lower than what can be achieved by fast exact \(\langle m_0,k_0,n_0\rangle\) matrix multiplication, APA algorithms, evaluated enough times to get an exact output, can only offer practical speedups on (possibly galactically) large matrices. For this reason, they have historically been considered mainly of theoretical interest, primarily as a source of upper bounds on the border rank of \(\mathcal{M}_{\langle m,k,n\rangle}\). This is no doubt compounded by the fact that techniques for deriving APA algorithms are poorly documented in the literature. The most popular search algorithm applies some version of (nonlinear or alternating) least squares to the tensor decomposition problem. While least squares is similarly used to find fast exact algorithms (see e.g., \[3, 56\]), this approach has a unique limitation in the APA setting: the need to convert numerical decompositions into ones with functional entries. There is no known algorithmic way to do this. Indeed, Smirnov uses "various choice heuristics" to obtain many of the current best-known APA algorithms in \[56\]. Other open questions concern the practical details of using APA matrix multiplication. For example, recalling that fast exact matrix multiplication is well-known to be (norm-wise) stable \[20\], can the same be said of the "exactification" procedure introduced by Bini \[9\]? Additionally, can we accelerate an APA algorithm using the same tools applied to fast exact matrix multiplication, specifically the alternative basis approach of Holtz et al. \[32\]?

The goal of this work is to address all three of these questions. Our first contribution is a new search algorithm for APA matrix multiplication routines that can be easily run on small values of _m_<sub>0</sub>, _k_<sub>0</sub>, and _n_<sub>0</sub>, requires minimal computing resources, and automatically generates decompositions with functional entries (e.g., of the form shown in Figure 2). Alongside this search algorithm, we also extend both the aforementioned numerical stability results and the alternative basis procedure to the APA setting. One strong motivation for this work is the rapidly changing (and varied) set of demands placed on matrix multiplication kernels by machine learning applications (see the discussion in \[23\]), which warrants revisiting every option in our algorithmic toolkit. Note in particular that an APA algorithm may only be slower than fast exact matrix multiplication in practice if we evaluate it enough times to get an exact product; in applications where only a low-precision approximate product is necessary - and hence evaluating an APA algorithm _O_(1) may be sufficient - APA matrix multiplication will be competitive. Indeed, Ballard et al. \[4\] have already obtained promising results in this direction in the context of neural network training.

## 1.1 Our Contributions

The main contributions of this paper can be summarized as follows:

1. In Section 2 we present a new algorithm for generating APA matrix multiplication routines. The key insight is the following: by applying a symbolic De-Groote transformation and deleting one rank-one term in the corresponding tensor decomposition, a fast exact algorithm yields an APA routine with one fewer scalar multiplication (assuming the product of the factors in the deleted term is nilpotent). Using the recently introduced flip graph \[39, 50\] to find exact algorithms where this condition is satisfied, we obtain new APA routines for a variety of matrix sizes, including one that improves the previously best-known rank.<tbc>

<sup>4</sup>Note that making the base case routine exact via (1.6) and using that recursively would lead to a slower algorithm.

