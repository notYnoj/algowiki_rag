For fixed nonnegative real _u,v,w_, let \(\omega(u,v,w)\) be the infimum of the exponents _e_ for which multiplying an \(\lceil n^u\rceil\times\lceil n^v\rceil\) matrix by a \(\lceil n^v\rceil\times\lceil n^w\rceil\) matrix uses _O(n<sup>e</sup>_) arithmetic operations, with the convention above. Write \(\omega(k)=\omega(1,k,1)\) and \(\alpha=sup\{k\ge 0:\omega(k)=2\}\).

We first state the bound for general matrix shapes, with the exponents sorted in decreasing order. We interpret the threshold \(\frac{ab}{a+b}\) as zero when _a=b_=0.

**Theorem 1.1.** _For every fixed_ \(a\ge b\ge c\ge 0\),

\(\omega(a,b,c)\le\left\{\begin{array}{ c c }
a+b, & c\le\frac{ab}{a+b}, \\
\frac{a+b+c}{2}+\frac{1}{4}\left(\frac{ab}{c}+\frac{ac}{b}+\frac{bc}{a}\right), & c>\frac{ab}{a+b}.
\end{array}\right.\) (1)

_When_ \(c\le\frac{ab}{a+b}\)_, equality holds by the size lower bound._

Applying this bound to the sorted dimensions of (1_,k,_1) gives the rectangular curve.

**Corollary 1.2.** _For every fixed real_ \(k\ge 0\),

\(\omega(k)\le\left\{\begin{array}{ c c }
2, & 0\le k\le\frac{1}{2}, \\
1+k+\frac{1}{4k}, & k\ge\frac{1}{2}.
\end{array}\right.\) (2)

_Consequently_ \(\omega(k)=2\) _for_ \(0\le k\le\frac{1}{2}\).

Corollary 1.2 gives exponent two for inner dimension up to _n_<sup>0.5</sup>, and an upper bound within \(\frac{1}{4k}\) of the input-size lower bound 1+_k_ for \(k\ge 1\).

The proof has two parts. First, we list explicit ways to split and combine polynomial products and apply a tensor character to them. A character assigns numerical sizes that add on direct sums, multiply on tensor products, and cannot increase under restriction. Multinomial counting gives concavity and growth inequalities for these sizes. Rescaling, common slopes, and affine bounds then give \(\sum_iarccos\sqrt{p_i}\ge\pi/2\) for the character’s three dot-product parameters.

Upper bound on w(k)
Lower bound max {2, 1+ k}
3
2.75
2.5
Exponent
2.25
2
0
1
2
1
2
2
k

Figure 1: The upper bound on \(\omega(k)\) from Corollary 1.2 for \(0\le k\le 2\), together with the size lower bound max{2,1+_k_}. The bounds coincide for \(0\le k\le\frac{1}{2}\).

