<tbc>_a_ when the product of all _d_ signs is +1, and otherwise output a uniform label other than _a_. With

\(\phi_d(t)=\frac{\sum_{h=0}^d(-1)^{d-h}\genfrac(){pt}{2}{t-1}{h}\genfrac(){pt}{2}{n-t}{d-h}}{\genfrac(){pt}{2}{n-1}{d}},\bar{\phi}_d=\left\{\begin{array}{ c c }
1/(d+1), & d\text{even,} \\
0, & d\text{odd,}
\end{array}\right.\)

the rank law is \(w_t=n^{-1}+(\phi_d(t)-\bar{\phi}_d)/(2(n-1))\). For \(d\ge 1\) its coefficient of _t<sup>d</sup>_ is \(2^d/\big(2(n-1)d!\genfrac(){pt}{2}{n-1}{d}\big)>0\), and for _q_=0 the law is uniform, of degree zero. The algorithm uses \(\lceil d/2\rceil\le q\) calls.

At _n_=3 and _q_=1 the construction gives the rank law (1/2,0,1/2), which has degree two and so cannot come from one classical comparison. By Corollary 1 and Theorem 2, one quantum comparison permits rank laws of degree two, whereas one classical comparison permits degree one. The larger degree is necessary for a quantum gain at one comparison. A nonnegative rank law of degree at most one is affine in the rank and sums to one, so it is a mixture of the law (5) with _q_=1 and its reversal, and its top-_r_ mass is at most _C_<sub>1</sub>(_n,r_) for every _r_. For _r_=1 this reads \(nw_1\le 2=nC_1(n,1)\).

However, the degree bound does not determine the optimal alignment probability. One quantum comparison and two classical comparisons share the degree bound two and have different values (Section 6). Determining the alignment optimum therefore requires optimization over rank laws that admissible quantum algorithms can realize.

## 6 The exact optimum with one quantum comparison

To determine this optimum, we need an attaining algorithm and an upper bound that applies to every admissible one-comparison strategy. The following theorem supplies both and expresses their common value through an explicit cubic.

**Theorem 3.** _Q_<sub>1</sub>(2,1)=1_. For_ \(n\ge 3\) _and_ \(1\le r<n\)_, put m=n_-1_, k=n_-2 _and h=n_-2_r, and let_ \(\zeta\) _be the smallest positive root of_

\(F_{n,r}(z)=2nhz^3+3(nk-h^2)z^2-4(2n-3)hz-6mk.\) (9)

_Then_

\(Q_1(n,r)=\frac{r}{n}+\frac{r(n-r)}{n(n-1)}\zeta.\) (10)

_For r\<n/_2 _the positive root is unique and lies in_ (1,3)_. For r=n/_2 _it is_ \(\sqrt{2(n-1)/n}\)_. For n/_2_\<r\<n_-1 _it is the unique root in_ (1,(_n_-2)/(2_r-n_))_, and for r=n_-1 _it is_ 1_. An explicit initial state and output measurement attain this value for every unknown order._

**Corollary 2.** _For_ \(n\ge 2\),

\(Q_1(n,1)=\frac{3(n-1)+\sqrt{13n^2-18n+9}}{2n^2},\text{\textit{and}}Q_1(n,n/2)=\frac{1}{2}+\sqrt{\frac{n}{8(n-1)}}\)

_for even n. The equivalent blind-pick size nQ_<sub>1</sub>(_n,_1) _increases with n toward_ \((3+\sqrt{13})/2\approx 3.3028\)_, and for_ \(n\ge 3\)_, nQ_<sub>1</sub>(_n,_1)_\>_3=_nC_<sub>2</sub>(_n,_1) _exactly when n\>_9_, with equality at n_=9.

