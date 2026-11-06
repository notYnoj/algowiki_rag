most \(\kappa 2^{3682\sqrt{D}log^7(D)}\gamma(D)\nu^{\rho+\varepsilon}\) operations and let \(\lambda=2^{2000log^3(D)}\kappa\). We will show that

\(T[\nu,D,\phi]\le\left\{\begin{array}{ c c }
2\kappa 2^{3682\sqrt{D}log^7(D)}\gamma(D)\nu^{\rho+\varepsilon} & \text{if Line 1 is reached} \\
2^{2000log^3(D)}T[\nu,D,1/log^6(D)]+\lambda 2^{3682\sqrt{D}log^7(D)}\gamma(D)\nu^{\rho+\varepsilon} & \text{if Line 1 is reached} \\
2T[\frac{3}{4}\nu,D,\phi+\frac{1}{40log^7(D)}]+2^{99log^2(D)}T[\nu,\lfloor D-3\sqrt{D}\rfloor,1] & \text{else.}
\end{array}\right.\)

Finally, \(\xi(\nu,D,\phi)=\lambda 2^{4000log^7(D)(\sqrt{D}+\frac{21\phi}{40log^4(D)}))}\gamma(D)\nu^\delta\), where \(\delta=max(\rho+\varepsilon,2.49)\), will be an upper bound for _T_ in closed form.

Let us start by showing that _T_ is indeed an upper bound on the number of operations performed by all future recursive calls (including the current one) combined. The number of operations performed by the current recursive call was analyzed above. If Line 1 is reached, then only one further call to `base-case` is made. If Line 1 is reached, then `red-portals` is called and the proof of Lemma 10 yields that this leads to at most 2<sup>2000log<sup>3</sup>(_D_)</sup>-1 calls of `red-portals`, these calls combined call `solve-\(\pi\)-`r` at most 2<sup>2000log<sup>3</sup>(_D_)</sup> times, and in each of these calls, the value of _x_ is at most 44log(_D_) by Lemma 8. This implies that \(\phi\) is at most \(\frac{44}{40log^7(D)}\le\frac{1}{log^6(D)}\). Moreover, the num ber of operations performed by the current recursive call of `solve-\(\pi\)-`r` and the at most 2<sup>2000log<sup>3</sup>(_D_)</sup> recursive calls of `red-portals` perform at most

\(2^{2000log^3(D)}\kappa 2^{3682\sqrt{D}log^7(D)}\gamma(D)\nu^{\rho+\varepsilon}\le\lambda 2^{3682\sqrt{D}log^7(D)}\gamma(D)\nu^\delta.\)

This shows that _T_ is indeed an upper bound in the second case. If neither of Line 1 are reached, then we call `solve-\(\pi\)-`r` once each in Line 1 with the same value of _D_, the value of \(\nu\) shrunk by a factor of 3/4, and _x_ increased by one. Hence, the value of \(\phi\) increases by at most \(\frac{1}{40log^7(D)}\). Moreover, we call `solve-\(\pi\)-`r` in Line 1 once for each cycle in S. As analyzed above, there are at most 2<sup>99log<sup>2</sup>(_D_)</sup> cycles in S and in each of these recursive calls, the number \(\nu\) of vertices does not increase, the value of _D_ is decreased by \(\lceil 3\sqrt{D}\rceil\), and in the worst case the value of \(\phi\) increases to 1. The number of operation in the current recursive call is again at most \(\kappa 2^{3682\sqrt{D}log^7(D)}\gamma(D)\nu^{\rho+\varepsilon}\) and hence _T_ is an upper bound as claimed in all cases.

To conclude the proof, we show that \(T\le\xi\). We prove this by induction and therefore assume that \(T\le\xi\) in each recursive call. Note that if Line 1 is reached, then only one recursive call is made to `base-case` which does not incur any other recursive calls. Hence, it holds trivially that \(T[\nu,D,\phi]=2\kappa 2^{3682\sqrt{D}log^7(D)}\gamma(D)\nu^{\rho+\varepsilon}\le\lambda 2^{4000\sqrt{D}log^7(D)}\gamma(D)n^\delta\le\xi(\nu,D,\phi)\) (note that \(\frac{21\Phi}{40log^4(D)}\) might be very small but it is non-negative). If Line 1 is reached, then we have that \(T[\nu,D,\phi]=2^{2000log^3(D)}T[\nu,D,1/log^6(D)]\) and \(\phi=1\). The induction hypothesis then yields

\(T[\nu,D,\phi]=2^{2000log^3(D)}T[\nu,D,1/log^6(D)]+\lambda 2^{3682\sqrt{D}log^7(D)}\gamma(D)\nu^{\rho+\varepsilon}\)<br>
\(\le 2^{2000log^3(D)}\cdot\lambda 2^{4000log^7(D)(\sqrt{D}+\frac{1}{2log^{10(D)}})}\gamma(D)\nu^\delta+\lambda 2^{3682\sqrt{D}log^7(D)}\gamma(D)\nu^\delta\)<br>
\(\le\lambda\gamma(D)\nu^\delta(2^{4000log^7(D)(\sqrt{D}+\frac{21}{40log^{10(D)}}+\frac{2000log^3(D)}{4000log^7(D)})}+2^{3682\sqrt{D}log^7(D)})\)<br>
\(\le\lambda(2\cdot 2^{4000log^7(D)(\sqrt{D}+\frac{21}{40log^{10(D)}}+\frac{20}{40log^4(D)})})\gamma(D)\nu^\delta\)<br>
\(\le\lambda 2^{4000log^7(D)(\sqrt{D}+\frac{21}{log^6(D)}+20+\frac{1}{100log^3(D)})}\gamma(D)\nu^\delta\)<br>
\(\le\lambda 2^{4000log^7(D)(\sqrt{D}+\frac{21}{40log^4(D)})}\gamma(D)\nu^\delta=\xi(\nu,D,1)=\xi(\nu,D,\phi).\)

