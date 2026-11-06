<tbc>Homogeneity and monotonicity give<tbc>

\(ag_{ij}(r,s)\le g_{ij}(r',s')\le bg_{ij}(r,s).\)

<tbc>Together with \(g_{ij}(r,s)\le r+s\), this implies

\(|g_{ij}(r',s')-g_{ij}(r,s)|\le\frac{r+s}{min\{r,s\}}max\{|r'-r|,|s'-s|\}.\) (F.2)

The coefficient is bounded on every closed bounded region that stays away from the coordinate axes. Approximating a positive real pair by rationals therefore gives a unique continuous extension. All the rational bounds, homogeneity, monotonicity, input interchange, and powered concavity extend by continuity. So does (20).

We finally check that this extension agrees with the limit in (18). For positive integers _A,B_, the scale _q_=1 in (F.1) gives \(f_{ij}(A,B)\le g_{ij}(A,B)\). Thus for arbitrary real _r,s\>_0,

\(\frac{f_{ij}(\lceil mr\rceil,\lceil ms\rceil)}{m}\le g_{ij}\left(\frac{\lceil mr\rceil}{m},\frac{\lceil ms\rceil}{m}\right)\longrightarrow g_{ij}(r,s),\)

using homogeneity and continuity.

For the reverse bound, fix positive rationals _r_<sub>0</sub>_\<r_, _s_<sub>0</sub>_\<s_ and an admissible scale _q_ with _qr_<sub>0</sub>_,qs_<sub>0</sub> positive integers. Put \(k=\lfloor m/q\rfloor\). For all sufficiently large _m_, \(k\ge 1\), and \(kqr_0\le\lceil mr\rceil\), \(kqs_0\le\lceil ms\rceil\). Monotonicity and replication give

\(\frac{f_{ij}(\lceil mr\rceil,\lceil ms\rceil)}{m}\ge\frac{k}{m}f_{ij}(qr_0,qs_0).\)

Since \(k/m\rightarrow 1/q\), taking the lower limit and then the supremum over _q_ gives a lower bound _g<sub>ij</sub>(r_<sub>0</sub>_,s_<sub>0</sub>). Let _r_<sub>0</sub>_,s_<sub>0</sub> approach _r,s_ from below and use continuity. This proves the limit formula (18), and completes the lemma.

## Appendix G. Common slopes and the angular constraint

Here we justify the common slopes and offsets, then derive the angular constraint using finite increments rather than derivatives.

_Proof of Lemma 5.1._ Write _P=P<sub>ij</sub>_ and _Q=P<sub>ik</sub>_. We will define<tbc>

\(c_{ij}=sup_{s>0}\left(\frac{P(s)}{L_i}-s\right),c_{ik}=sup_{s>0}\left(\frac{Q(s)}{L_i}-s\right)\)

<tbc>once the common positive slope _L<sub>i</sub>_ has been established. For _s\>_1, the nonnegative secant slope (_P(s_)-_P_(1))/(_s_-1) decreases as _s_ grows, by concavity. It therefore has a finite limit, which is also _L<sub>P</sub>_=lim_P(s)/s_. Likewise define _L<sub>Q</sub>_=lim_Q(s)/s_. Dividing the coupled inequalities

\(P(3s+1)\ge 2P(s)+Q(s),Q(3s+1)\ge 2Q(s)+P(s)\)

by _s_ and passing to infinity gives \(L_P\ge L_Q\) and \(L_Q\ge L_P\). Call their common value _L<sub>i</sub>_.

Their sum _R=P+Q_ satisfies \(R(3s+1)\ge 3R(s)\). Iterating at \(s_m=3^m(s+\frac{1}{2})-\frac{1}{2}\) gives

\(R(s)\le lim_{m\rightarrow\infty} 3^{-m}R(s_m)=L_i(2s+1).\) (G.1)

Since _R(s)\>_0, we have _L<sub>i</sub>\>_0. For _v\>u\>_0, concavity bounds the secant slope (_P(v_)-_P(u_))/(_v-u_) below by every later secant slope; sending its far endpoint to infinity gives<tbc>

\(P(v)-P(u)\ge L_i(v-u).\)

