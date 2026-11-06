In this introduction we will give a brief overview of the proof ideas and results, focussing on \(\omega_\mathbb{F}=\omega_\mathbb{F}(1,1,1)\), but the ideas work for the rectangular exponents \(\omega_\mathbb{F}(a,b,c)\) as well. Formal definitions and statements are from Section 2 onwards. Standard references for background are the survey of Bläser \[Blä13\] and the book of Bürgisser, Clausen and Shokrollahi \[BCS97\].

## 1.1 Degeneration ingredients and combination rules

The matrix multiplication tensor is \(\langle n_1,n_2,n_3\rangle=\sum_{i=1}^{n_1}\sum_{j=1}^{n_2}\sum_{k=1}^{n_3}E_{ij}\otimes E_{jk}\otimes E_{ki}\), where _E<sub>ij</sub>_ is the matrix with entry 1 at (_i,j_) and 0 elsewhere. The matrix multiplication exponent \(\omega_\mathbb{F}\) is defined in terms of tensor rank (or equivalently in terms of arithmetic circuit complexity). For a tensor _T_ the tensor rank R(_T_) is the smallest number _r_ such that \(T\le\langle r\rangle\) where \(\langle r\rangle=\sum_{i=1}^re_i\otimes e_i\otimes e_i\) is the unit tensor and where \(\le\) denotes restriction: the left hand side is obtained from the right hand side by applying linear maps to the three legs. It goes back to Strassen \[Str69\] that if \(\langle n,n,n\rangle\le\langle r\rangle\) for integers \(n\ge 2\) and \(r\ge 1\), then \(\omega_\mathbb{F}\le\mathrm{log}r/\mathrm{log}n\). Throughout, log denotes the logarithm to base 2.

It is known that \(\omega_\mathbb{F}\) does not change if we replace restriction by its approximative version, degeneration (i.e., we replace tensor rank by border rank): if \(\langle n,n,n\rangle\unknown\langle r\rangle\) for integers \(n\ge 2\) and \(r\ge 1\), then still \(\omega_\mathbb{F}\le\mathrm{log}r/\mathrm{log}n\). Degeneration \(\unknown\) is a restriction in which we allow to use matrices whose entries are polynomials in a formal variable \(\varepsilon\), which we think of as going to zero (also in positive characteristic one can define this correctly, symbolically). So to prove upper bounds on \(\omega_\mathbb{F}\) it suffices to prove degenerations of the form<tbc>

\(\langle n,n,n\rangle\unknown\langle r\rangle,\)

Upper bound on w(1,b,c)
Upper bound on w(1,k,1)
Theorem 1.2
lower bound 1 + b
2.4
Theorem 1.2
C = b/(1 + b)
laser method
C = 0.321b
lower bound
2.3
9/4
2.25
2.2
2.00
1.75
2.1
1.50
2.0
w(6,3,2) = 9
1.25
0.8
0.6
1.00
0.4
0.2
a > 0.321
a > 1/2
0.2
0.4
b
0.0
0.8
0.00
0.25
0.50
0.75
1.00
1.0
C
k

Figure 1: (Left) The upper bound of Theorem 1.2 on \(\omega_\mathbb{F}(1,b,c)\) for \(1\ge b\ge c\ge 0\) as a blue surface, above the grey plane of the lower bound 1+_b_. The black dotted curve _c=b/_(1+_b_) indicates until where upper bound and lower bound match and give \(\omega_\mathbb{F}(1,b,c)=1+b\). The orange dotted line _c_=0.321334_b_ shows until where this match was known by previous results from the laser method \[WXXZ24\]. (Right) The upper bound of Corollary 4.17 on \(\omega_\mathbb{F}(1,k,1)\) for \(0\le k\le 1\), compared with the previously known upper bound from the laser method, as the lower convex hull of the values tabulated in \[WXXZ24, ADW<sup>+</sup>25\].

