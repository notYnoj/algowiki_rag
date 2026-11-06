**Proof.** By definition, _P_ is only supported on the indices _i_ with \((A[i]\mathrm{mod}2^\ell)\in x2^{\ell-1}+[0,2^{\ell-1})\) and analogously, _Q_ is only supported on the indices _j_ with \((B[j]\mathrm{mod}2^\ell)\in y2^{\ell-1}+[0,2^{\ell-1})\). Let _i,j_ be two indices satisfying these requirements. Then:<tbc>

\(P[i]+Q[j]=\left\lfloor\frac{A[i]}{2^\ell}\right\rfloor+\left\lfloor\frac{B[j]}{2^\ell}\right\rfloor=\frac{A[i]+B[j]-(A[i]\mathrm{mod}2^\ell)-(B[j]\mathrm{mod}2^\ell)}{2^\ell}.\)

<tbc>This can be upper bounded by<tbc>

\(P[i]+Q[j]\le\frac{A[i]+B[j]-(x+y)2^{\ell-1}}{2^\ell},\)

<tbc>and correspondingly lower bounded by<tbc>

\(P[i]+Q[j]>\frac{A[i]+B[j]-(x+y)2^{\ell-1}-2^\ell}{2^\ell}=\frac{A[i]+B[j]-(x+y)2^{\ell-1}}{2^\ell}-1.\)

<tbc>But as this is an integer, we must have<tbc>

\(P[i]+Q[j]=\left\lfloor\frac{A[i]+B[j]-(x+y)2^{\ell-1}}{2^\ell}\right\rfloor.\)

<tbc>Hence, since \(x,y,\ell\) are fixed, it is minimized for any witness (_A∗B_)\[_i+j_\]. In particular, _i_<sup>∗</sup> is a witness of (_P∗Q_)\[_k_<sup>∗</sup>\], and

\(P[i^*]+Q[j^*]=\left\lfloor\frac{(A*B)[k^*]-(x+y)2^{\ell-1}}{2^\ell}\right\rfloor\le\left\lfloor\frac{(A*B)[k^*]}{2^\ell}\right\rfloor,\)

proving (i). Moreover, for any witness _i_ of (_P∗Q_)\[_k_<sup>∗</sup>\], _A_\[_i_\]+_B_\[_k_<sup>∗</sup>-_i_\] cannot differ from (_A∗B_)\[_k_<sup>∗</sup>\] by \(2^\ell\) or more, proving (ii).

**Claim 5.5.** _There is some_ \(z\in[-4,4]\) _such that, in any iteration corresponding to these choices of_ \(\ell,x,y,z\)_, with probability at least_ 0.9 _it holds that P_\[_i_<sup>∗</sup>\]+_Q_\[_j_<sup>∗</sup>\]=_R_\[_k_<sup>∗</sup>\].

**Proof.** We derive lower and upper bounds on<tbc>

\(\mathrm{min}_{i,j\in Xi+j=k^*}\left\lfloor\frac{A[i]}{2^\ell}\right\rfloor+\left\lfloor\frac{B[j]}{2^\ell}\right\rfloor.\)

<tbc>On the one hand, a simple lower bound is \(\lfloor(A*B)[k^*]/2^\ell\rfloor-2\). On the other hand, _X_ contains some \(2^{\ell+1}\)-pseudo-witness \(i'\) of (_A∗B_)\[_k_<sup>∗</sup>\] with probability at least \(1-(1-p^2)^t\ge 1-\mathrm{exp}(-p^2t)=1-\mathrm{exp}(-n^{-2\rho}\cdot 100\lceil n^{2\rho}\rceil)\ge 0.9\). Conditioned on this event, we have

\(\mathrm{min}_{i,j\in Xi+j=k^*}\left\lfloor\frac{A[i]}{2^\ell}\right\rfloor+\left\lfloor\frac{B[j]}{2^\ell}\right\rfloor\le\left\lfloor\frac{A[i']}{2^\ell}\right\rfloor+\left\lfloor\frac{B[k^*-i']}{2^\ell}\right\rfloor\)<br>
\(\le\frac{A[i']+B[k^*-i']}{2^\ell}\)<br>
\(<\frac{(A*B)[k^*]+2^{\ell+1}}{2^\ell}\)<br>
\(<\left\lfloor\frac{(A*B)[k^*]}{2^\ell}\right\rfloor+3.\)

