<tbc>The basic move set is **M**<sub>Q</sub>={(1,0),(0,1),(1,1),(1,-1)}. The known quasipolynomial formulas for up to four queens are:

(5.1) \(u_\mathbb{Q}(1;n)=n^2.\)<br>
\(u_\mathbb{Q}(2;n)=\frac{n^4}{2}-\frac{5n^3}{3}+\frac{3n^2}{2}-\frac{n}{3}=\frac{n(n-1)(3n^2-7n+2)}{6}\)<br>
\(u_\mathbb{Q}(3;n)=\left\{\frac{n^6}{6}-\frac{5n^5}{3}+\frac{79n^4}{12}-\frac{25n^3}{2}+11n^2-\frac{43n}{12}+\frac{1}{8}\right\}+(-1)^n\left\{\frac{n}{4}-\frac{1}{8}\right\}.\)<br>
\(u_\mathbb{Q}(4;n)=\left\{\frac{n^8}{24}-\frac{5n^7}{6}+\frac{65n^6}{9}-\frac{1051n^5}{30}+\frac{817n^4}{8}-\frac{19103n^3}{108}+\frac{3989n^2}{24}-\frac{18131n}{270}+\frac{253}{54}\right\}\)<br>
\(+(-1)^n\left\{\frac{n^3}{4}-\frac{21n^2}{8}+7n-\frac{7}{2}\right\}+\Re(\zeta_3^n)\frac{32(n-1)}{27}+\mathrm{Im}(\zeta_3^n)\frac{40\sqrt{3}}{81}.\)

The square and cube roots of unity in _u_<sub>Q</sub>(4;_n_) imply period 6.

The formula for two queens, originally due to Lucas, is given by our Theorem III.4.1. The formula for three queens, due to Landau, is implied by our Theorem III.4.2. Kotˇešovec gives formulas for up to six queens, calculated by him for _q_=4,5 and calculated for six queens by Artem M. Karaevev. (\[12\] has the citations.) These three have not been not rigorously proved.

Kotˇešovec conjectured formulas for \(\gamma_1\) and \(\gamma_2\) based on the known and heuristically derived formulas (mostly by him) for _u_<sub>Q</sub>(_q;n_) for small _q_. Theorem III.3.1 proves his conjectures and also a formula for \(\gamma_3\), and further proves that \(\gamma_4\) is constant as a function of _n_, but that the next two coefficients are not.

**Corollary 5.1** (of Theorem III.3.1)**.** _In u_<sub>Q</sub>(_q;n_) _the coefficients_ \(\gamma_i\) _for_ \(i\le 4\) _are constant as functions of n; but_ \(\gamma_5\) _has period_ 2 _if_ \(q\ge 3\)_. Exact formulas are_

\(\gamma_0=\frac{1}{q!},\gamma_1=-\frac{1}{(q-2)!}\left\{\frac{5}{3}\right\},\)<br>
\(\gamma_2=\frac{1}{2!(q-2)!}\left\{\frac{25}{9}(q-2)_2+\frac{61}{6}(q-2)+3\right\},\)<br>
\(\gamma_3=-\frac{1}{3!(q-2)!}\left\{\frac{125}{27}(q-2)_4+\frac{305}{6}(q-2)_3+\frac{681}{5}(q-2)_2+73(q-2)+2\right\}.\)

Unlike the case of bishops and semibishops, the period of _u_<sub>Q</sub>(_q;n_) is not simple, although Kotˇešovec \[12, 6th ed., p. 31\] makes the following remarkable conjecture.

**Conjecture 5.2** (Kotˇešovec)**.** The counting quasipolynomial for _q_ queens has period lcm\[_F<sub>q</sub>_\], the least common multiple of all positive integers up through the _q_-th Fibonacci number _F<sub>q</sub>_.

The observed periods up to _q_=7 (see \[12, 6th ed., pp. 19, 27-28\] for _q_=7) agree with this proposal, and the theory of Section IV.6 lends credence to its veracity.

Kotˇešovec conjectures, yet more strongly, the exact form of the denominator of the generating function \(\sum_{n\ge 0}u_\mathbb{Q}(q;n)x^n\): it is a product of specific cyclotomic polynomials raised to specific powers; see \[12, third ed., pp. 11, 14 _et seq._\], \[12, 6th ed., p. 22\]. The conjecture implies that, when written in standard Ehrhart form with denominator (1-_x<sup>p</sup>_)<sup>2_q_+1</sup>, the<tbc>

