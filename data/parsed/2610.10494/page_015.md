There are at most (_N_+1)_<sup>s</sup>_ multiplicity tuples. Summing and using the multinomial theorem gives

\(\left(\sum_ha_h\right)^N\le(N+1)^s2^{1/p_i}\lambda(T)^{N/p_i}.\)

For fixed _s_, this extra factor is polynomial in _N_. Taking _N_-th roots and letting \(N\rightarrow\infty\) proves (14).

_Proof of Lemma 3.4._ The two-sector splitting and Lemma 3.3 give, for \(s\ge 2\),

\(2f_{ij}(r,s)^{1/p_i}=\lambda(C_{ij}(r,s)\otimes B_i(2))^{1/p_i}\ge f_{ij}(r,s+1)^{1/p_i}+f_{ij}(r,s-1)^{1/p_i}.\)

This is discrete concavity in _s_; input interchange gives the other coordinate. The three-sector splitting and the same lemma give (16).

_Proof of Lemma 4.1._ Initially let _r,s\>_0 be rational, and define

\(g_{ij}(r,s)=sup_{q\in\mathbb{Q}_{>0}qr,qs\in\mathbb{Z}_{>0}}\frac{f_{ij}(qr,qs)}{q}.\) (F.1)

Replication gives \(f_{ij}(m,m)\ge m\), and monotonicity therefore gives \(f_{ij}(r,s)\ge min\{r,s\}\) for integer lengths. The bounds and input interchange follow from (15) and the lower bound above. Replacing _q_ by _q/t_ proves homogeneity.

The crucial point is that finitely many supremum values can be approached at one common scale. Choose scales _q<sub>h</sub>_ approximating the desired values, and choose _Q_ so that every _Q/q<sub>h</sub>_ is a positive integer. By (17),

\(\frac{f_{ij}(Qr,Qs)}{Q}\ge\frac{f_{ij}(q_hr,q_hs)}{q_h}.\)

Replacing _Q_ by an integer multiple preserves all these approximations and can clear any additional rational denominators. Monotonicity now follows by comparing lengths at a common scale.

For concavity, take \(s=\tau s_1+(1-\tau)s_2\), with rational \(0\le\tau\le 1\). Approach _g<sub>ij</sub>(r,s_<sub>1</sub>) and _g<sub>ij</sub>(r,s_<sub>2</sub>) at one scale _Q_, with _Qr,Qs_<sub>1</sub>_,Qs_<sub>2</sub>_,Qs_ integers. Discrete concavity gives

\(\left(\frac{f_{ij}(Qr,Qs)}{Q}\right)^{1/p_i}\ge\tau\left(\frac{f_{ij}(Qr,Qs_1)}{Q}\right)^{1/p_i}+(1-\tau)\left(\frac{f_{ij}(Qr,Qs_2)}{Q}\right)^{1/p_i}.\)

Bound the left side by _g<sub>ij</sub>(r,s_)<sup>1_/p<sub>i</sub>_</sup> and let the approximation error tend to zero. Input interchange gives the other coordinate.

For tripling, monotonicity first enlarges the discrete source length 3_s+r_-1 to 3_s+r_. At a common scale _Q_,

\(\left(\frac{f_{ij}(Qr,Q(3s+r))}{Q}\right)^{1/p_i}\ge 2\left(\frac{f_{ij}(Qr,Qs)}{Q}\right)^{1/p_i}+\left(\frac{f_{ik}(Qr,Qs)}{Q}\right)^{1/p_i}.\)

Approach the two right-hand suprema simultaneously; the left side is bounded by _g<sub>ij</sub>(r,_3_s+r_)<sup>1_/p<sub>i</sub>_</sup>. This proves (20).

To extend the profiles to real lengths, we first compare two positive rational pairs (_r,s_) and \((r',s')\). Put<tbc>

\(a=min\left\{\frac{r'}{r},\frac{s'}{s}\right\},b=max\left\{\frac{r'}{r},\frac{s'}{s}\right\}.\)

