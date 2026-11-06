## Appendix A. Splitting two polynomial products

We recap the two-sector construction used in \[9, Lemma 4.1\] as an explicit change of coordinates for pairs of polynomials.<sup>1</sup>

Fix \(r\ge 1\) and \(s\ge 2\). The tensor \(C_{XY}(r,s)\otimes B_X(2)\) computes

\((f,(a,b))\longmapsto(fa,fb),\mathrm{deg}f<r,\mathrm{deg}a,\mathrm{deg}b<s.\)

Thus tensoring with _B<sub>X</sub>_(2) means multiplying two polynomials by the same _f_. We will change coordinates to split the second input into lengths _s_+1 and _s_-1.

For \(e\ge 1\) and \(\mathrm{deg}a,\mathrm{deg}b\le e\), use<tbc>

\(p=a+tb,h=b-p_{e+1}t^e,p_d=[t^d]p.\)

<tbc>Here \[_t<sup>d</sup>_\]_p_ denotes the coefficient of _t<sup>d</sup>_. We have \(\mathrm{deg}p\le e+1\) and \(\mathrm{deg}h\le e-1\), and these coordinates are invertible: _b=h+p_<sub>_e_+1</sub>_t<sup>e</sup>_, _a=p-tb_. Use them on the input pair with _e=s_-1 and on the output pair with _e=r+s_-2. Multiplication by _f_ becomes<tbc>

\((p,h)\longmapsto(fp,fh+p_st^{s-1}(f-f_{r-1}t^{r-1})).\)

<tbc>Scale input _h_ by \(\varepsilon^{-1}\) and its output coordinate by \(\varepsilon\). The map is now

\((p,h)\longmapsto(fp,fh+\varepsilon p_st^{s-1}(f-f_{r-1}t^{r-1}))-\rightarrow^{\varepsilon\rightarrow 0}(fp,fh).\)

The independent polynomials _p,h_ have lengths _s_+1_,s_-1, respectively. This gives _C<sub>XY</sub>(r,s_+1) and _C<sub>XY</sub>(r,s_-1) sharing the first leg, with disjoint second and third legs. Permuting the legs gives the other orientations.

## Appendix B. The three-sector splitting

We recap the construction from \[9, Lemma 4.2\]. In _C<sub>XY</sub>(r,_3_s+r_-1), a term has \(0\le x<r\) and output index _z=x+y_. Partition the second-input and output indices into three intervals:

\(\begin{array}{ c c c }
 & \text{left} & \text{middle} & \text{right} \\
Y & [0,s-1] & [s,2s+r-2] & [2s+r-1,3s+r-2] \\
Z & [0,s+r-2] & [s+r-1,2s+r-2] & [2s+r-1,3s+2r-3].
\end{array}\)

Scale middle _Y_ variables by \(\varepsilon\) and middle _Z_ variables by \(\varepsilon^{-1}\), leaving the others unchanged. Since _z=y+x_ with \(0\le x<r\), left and right _Y_ indices stay in the corresponding _Z_ intervals. Cross-sector terms thus connect middle _Y_ to outer _Z_ and acquire a factor \(\varepsilon\); matched terms remain unchanged. As \(\varepsilon\rightarrow 0\), precisely three matched sectors sharing _X_ remain.

Translations identify the outer sectors with _C<sub>XY</sub>(r,s_). The middle is

\(\sum_{u=0}^{r-1}\sum_{v=0}^{s-1}x_{r-1-u}y_{s+u+v}z_{s+r-1+v},\)

which is _C<sub>XZ</sub>(r,s_) after reversing its first-leg basis. This identifies the individual sector. In the fixed-word construction of (13), the sectors acquire independent first-leg variables before their individual bases are changed.

<sup>1</sup>This is the degree-one case of the classical Clebsch–Gordan formula \[6, Theorem 2.6.3, pp. 56-57 of the author version\]. The coefficient calculation here does not require that formula.

