## 1 Introduction

Matrix multiplication is arguably the most basic linear algebraic operation, with plentiful applications throughout computer science and beyond. Its algorithmic complexity has been studied for many decades. In 1969 a breakthrough result by Strassen \[Str69\] showed that \(n\times n\) matrices can be multiplied faster than the naive cubic time algorithm. Since then there has been an explosion of results obtaining lower and lower bounds on the exponent \(\omega\) defined as the smallest constant such that for all \(\varepsilon>0\), \(n\times n\) matrices can be multiplied using \(O(n^{\omega+\varepsilon})\) arithmetic operations (additions, subtractions, multiplications and divisions; this is called the arithmetic circuit model of computation). In recent years, the bound \(\omega<2.373\) has been obtained \[Vas12, DS13, LG14, AV21\]. A new paper by Duan, Wu and Zhou \[DWZ23\] shows that \(\omega<2.3719\).

The dream bound would be \(\omega=2\), implying a near-linear time algorithm for multiplying matrices. Unfortunately, a series of works \[AFLG15, AV18a, CVZ21, Alm21, AV18b, BCC<sup>+</sup>17a, ASU13, BCC<sup>+</sup>17b\] has shown that the known techniques for multiplying matrices cannot achieve \(\omega=2\).

All work on matrix multiplication since 1986 \[Str86, Vas12, DS13, LG14, AV21, DWZ23\] has used various variants of the so-called _laser method_. The strongest limitation result known for the laser method and its variants \[AFLG15\] is that such techniques cannot show that \(\omega<2.3078\).

The limitation results could mean that radically new methods need to be produced to make big strides. Yet, even if one stays within the laser method framework, it is still an intriguing question: _how close can we get to the_ 2.3078 _barrier bound?_

In many applications of matrix multiplication, one needs to multiply _rectangular_ matrices: \(n^a\times n^b\) by \(n^b\times n^c\), where _a,b,c_ are different. Here one defines \(\omega(a,b,c)\) to be the exponent for which matrix products of such dimensions can be multiplied in \(O(n^{\omega(a,b,c)+\varepsilon})\) time for all \(\varepsilon>0\), in the arithmetic circuit model of computation.

For instance, in the study of All-Pairs Shortest Paths (APSP) in unweighted directed graphs \[Zwi02\], the complexity of APSP depends on the value \(\mu\) which is defined as the real number satisfying the equation \(\omega(1,\mu,1)=1+2\mu\). The same value is needed for the best known algorithms for computing minimum witnesses of Boolean Matrix Multiplication \[CKL07\], for All-Pairs Bottleneck Paths in node-weighted graphs \[SYZ11\] and other problems.

In the work on _k_-clique detection, the value of \(\omega(1,2,1)\) is important, as it is known \[EG04\] that 4-cliques in _n_-node graphs can be detected in \(O(n^{\omega(1,2,1)+\varepsilon})\) time for any \(\varepsilon>0\). Moreover, if \(\omega(1,2,1)<3.16\), this would improve the known algorithms for _k_-clique detection for all \(k\ge 8\) \[NP85\].

A final value of interest is \(\alpha\), the largest constant so that \(\omega(1,\alpha,1)=2\), first studied by Coppersmith \[Cop82, Cop97\]. If \(\omega=2\), then \(\alpha=1\). So one can view the goal of increasing \(\alpha\) as another way to attempt to prove that \(\omega=2\).

The best bounds on rectangular matrix multiplication to date are given by Le Gall and Urrutia \[LGU18\], which improved upon \[Cop82, Cop97, HP98, KZHP08, LG12\]. For the values listed above, the bounds obtained by \[LGU18\] are as follows: \(\mu<0.5286\), \(\omega(1,2,1)<3.25164\) and \(\alpha<0.31389\).

The goal of this paper is to obtain better bounds on \(\omega,\alpha,\mu\) and rectangular matrix multiplication in general.

### 1.1 Our Results

The main result of this paper is a new improved variant of the laser method for designing matrix multiplication algorithms. Applying the new method, we obtain improved bounds for both square and rectangular matrix multiplication.

