<tbc>Choose _D<sub>t</sub>_ distinct neighbors _u_<sub>1</sub>_,...,u<sub>D<sub>t</sub></sub>_ carrying color _i<sub>t</sub>_ in their palettes. At the end of the round, each such vertex has lost the label _i<sub>t</sub>_: it is either emptied by the cap or loses _i<sub>t</sub>_ in the neighbor update. Therefore

\(\lambda(Q^{t-1})-\lambda(Q^t)\ge D_t.\)

Summing over rounds and telescoping yields (7), since \(\lambda(Q^0)=kn\).

For the third assertion, let \(\varphi\) be a proper coloring of _G_\[_A_\]. We prove inductively that, after each round, \(\varphi(v)\) remains in the palette of every \(v\in A\); moreover, each selected pivot _f<sub>s</sub>_ has the singleton palette \(\{\varphi(f_s)\}\), and no neighbor of _f<sub>s</sub>_ carries \(\varphi(f_s)\) in its palette. These assertions hold initially, with the pivot assertions vacuous.

Suppose they hold before round _t_. Every vertex of _A_ is active. If \(|A|\ge T\) and \(t\le T\), then an unchosen vertex remains, so _f<sub>t</sub>_ is defined. Every unchosen \(v\in A\) is a candidate in the maximization defining _f<sub>t</sub>_, and consequently<tbc>

\(m_{Q^{t-1}}(v)\le m_{Q^{t-1}}(f_t)=D_t.\)

<tbc>Thus the cap does not empty its palette and preserves \(\varphi(v)\). For an earlier pivot _f<sub>s</sub>_, the inductive assertions give

\(d_{\varphi(f_s)}^{Q^{t-1}}(f_s)=0,\)

so its singleton palette is also preserved by the cap. In particular, \(\varphi(f_t)\in P^t(f_t)\), making the prescribed color choice legal.

The update deletes \(\varphi(f_t)\) only from neighbors of _f<sub>t</sub>_. Properness of \(\varphi\) ensures that no such neighbor in _A_ loses its prescribed color. The pivot _f<sub>t</sub>_ receives the singleton palette \(\{\varphi(f_t)\}\), and all its neighbors lose that color. The assertions for earlier pivots remain valid. This completes the induction and proves that the run completes _T_ rounds.

## 6.2 The missing-cap lemma

**Lemma 6.2.** _Suppose that G is_ \(\varepsilon\)_-far from being k-colorable. Let_<tbc>

\(T:=\left\lceil\frac{4k}{\varepsilon}\right\rceil\ge 1,\alpha:=\frac{\varepsilon}{4(k+1)}.\)

<tbc>_Every run completing T rounds has some_ \(1\le t\le T\) _with_

\(|U(P^t)|\le(1-\alpha t)n.\) (8)

_Consequently, if_ \(|A|\ge T\) _and G_\[_A_\] _is k-colorable, then the proper-coloring run contains all of A in the cap at that time._

_Proof._ By Lemma 3.2, whenever a relevant graph exists we have \(0<\varepsilon<1/(2k)\). Hence

\(\alpha T\le\frac{4k+\varepsilon}{4(k+1)}<1,\)

so all right-hand sides in (8) are positive.

Assume for contradiction that (8) fails for every _t_. Then<tbc>

\(B_t=n-|U(P^t)|<\alpha tn,\)

<tbc>so \(B_t\le\alpha tn\). Lemma 6.1 supplies all the other hypotheses of Lemma 4.1, including (7). Therefore some coloring _c_ satisfies

\(|M(c)|\le\left(\alpha(k+1)+\frac{k}{T}\right)n^2\le\frac{\varepsilon}{2}n^2<\varepsilon n^2,\)

contradicting Lemma 3.1. The final statement follows from the last part of Lemma 6.1.

