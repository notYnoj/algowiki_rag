_Proof of Theorem 3.1._ If \(\tau/2\le T\), by combining Lemmas A.1, A.2, A.3, and A.4, then with probability at least \(1-2\delta-1/\mathrm{poly}(n)\), we have:

\((1-2\varepsilon)T\le(T_0-\varepsilon T)+(1-\varepsilon)(T_1+T_2+T_3-\varepsilon T)\le X\le(T_0+\varepsilon T)+(1+\varepsilon)(T_1+T_2+T_3)\le(1+2\varepsilon)T.\)

Note that if \(\tau\le T\) then the output is \((1\pm 2\varepsilon)T\) and in particular is at least \((1-2\varepsilon)T\ge(1-2\varepsilon)\tau\).

If \(\tau/2\ge T\), by combining Lemmas A.1, A.3, and A.4, then with probability at least \(1-2\delta-1/\mathrm{poly}(n)\)

\(X\le T_0+\varepsilon\tau/2+(1+\varepsilon)(T_1+T_2+T_3)\le(1+\varepsilon)T+\varepsilon\tau/2\le(1+\varepsilon)\tau/2+\varepsilon\tau/2<(1-2\varepsilon)\tau.\)

assuming \(\varepsilon\le 1/6\). Re-parameterizing \(\varepsilon\leftarrow\varepsilon/2\) and \(\delta\leftarrow\delta/2\) in the algorithm yields the required accuracy results. The space bound is proved in Theorem A.1.

