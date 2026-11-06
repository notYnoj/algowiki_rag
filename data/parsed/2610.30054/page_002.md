**4 Upper bounds via spectral points 20**<tbc>

4.1 Spectral points, asymptotic spectrum duality, and basic properties ..... 21<tbc>

4.2 Superadditivity on partial direct sums ..... 22<tbc>

4.3 Concavity and tripling for each leg ..... 24<tbc>

4.4 Square matrix multiplication ..... 25<tbc>

4.5 Quadratic constraints on asymptotic spectrum of matrix multiplication ..... 27<tbc>

4.6 Rectangular matrix multiplication ..... 30<tbc>

**5 Operational barrier 31**<tbc>

5.1 Symmetric notation P<sub>_x,y,z_</sub> for permuted polynomial multiplication ..... 32<tbc>

5.2 Set F of formal combinations of tensors ..... 32<tbc>

5.3 Formal preorder relation \(\unknown\) on F and operational barrier statement ..... 33<tbc>

5.4 Definition of functions \(F_\theta^\star\) on F ..... 34<tbc>

5.5 Choice of \(\theta\) for the \(\omega(a,b,c)\) barrier ..... 35<tbc>

5.6 Basic properties of \(F_\theta^\star\) ..... 36<tbc>

5.7 Proof of monotonicity of \(F_\theta^\star\) and the operational barrier ..... 38<tbc>

5.8 Operational asymptotic spectrum \(\Delta_\unknown\) ..... 40

## 1 Introduction

The exponent \(\omega_\mathbb{F}\) of matrix multiplication over a field F is the infimum of all real numbers \(\tau\) such that the tensor rank of the matrix multiplication tensor \(\langle n,n,n\rangle\) over F is \(\mathcal{O}(n^\tau)\). OpenAI recently released a proof that \(\omega_\mathbb{C}\le 9/4\) \[Ope26a, Theorem 1.1\], significantly improving over the previous upper bounds and using new ideas. We give an exposition of their proof in the language of degeneration inequalities and Strassen’s asymptotic spectrum of tensors \[Str88, Section 3\] (see also the survey of Wigderson and Zuiddam \[WZ26\]). Our version of the proof works over every field.

**Theorem 1.1.** _For every field_ F, \(\omega_\mathbb{F}\le 9/4\).

The previous upper bound was \(\omega_\mathbb{F}<2.371339\) \[ADW<sup>+</sup>25\], from the laser method.

We also discuss rectangular matrix multiplication exponents. For integers \(n_1,n_2,n_3\ge 1\), the matrix multiplication tensor \(\langle n_1,n_2,n_3\rangle\) describes the multiplication of an \(n_1\times n_2\) matrix by an \(n_2\times n_3\) matrix. For real numbers \(a,b,c\ge 0\), let \(\omega_\mathbb{F}(a,b,c)\) be the infimum of the real numbers \(\gamma\) such that the tensor rank of \(\langle\lceil n^a\rceil,\lceil n^b\rceil,\lceil n^c\rceil\rangle\) over F is \(\mathcal{O}(n^\gamma)\). In particular, \(\omega_\mathbb{F}=\omega_\mathbb{F}(1,1,1)\). Following Uzna ́nski \[Uzn26\], the same methods give the following bounds.

**Theorem 1.2.** _For every field_ F _and all real numbers_ \(a\ge b\ge c\ge 0\),

\(\omega_\mathbb{F}(a,b,c)\le\left\{\begin{array}{ c c }
a+b & \text{\textit{if}}c(a+b)\le ab, \\
\frac{(ab+bc+ca)^2}{4abc} & \text{\textit{if}}c(a+b)>ab,
\end{array}\right.\)

_with equality if_ \(c(a+b)\le ab\).

In particular, \(\omega_\mathbb{F}(1,k,1)=2\) for \(0\le k\le 1/2\), so \(\alpha_\mathbb{F}:=sup\{k\ge 0:\omega_\mathbb{F}(1,k,1)=2\}\) is at least 1/2 (Corollary 4.17). This implies for instance that \(n^2\times n\) by \(n\times n^2\) matrices can be multiplied in \(\mathcal{O}(n^{4+\varepsilon})\) operations! This improves previous \(\alpha_\mathbb{C}>0.465\) \[Ope26b\] and \(\alpha_\mathbb{F}>0.321334\) from the laser method \[WXXZ24\]. Figure 1 shows Theorem 1.2.

We will prove that the bound of Theorem 1.2 is "the best that its proof can give": the ingredients that our proof use do not give a better upper bound on \(\omega_\mathbb{F}(a,b,c)\), and neither does any combination (in a precise way) of the ingredients (Theorem 5.4). To improve the bounds further requires going around this "operational barrier".

