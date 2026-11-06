For our approximate flow, we still satisfy that property because

\(\sum_{i=1}^da_i\overline{x_i}=\sum_{i=1}^da_i(\mathrm{max}(1,f_i)-2)\cdot\frac{1}{1-r/d}\)<br>
\(=\sum_{i=1}^da_i\cdot(\mathrm{max}(1,f_i)-c_i+a_i)\cdot\frac{1}{1-r/d}\)<br>
\(=((\sum_{i=1}^da_i^2)+\sum_{i=1}^da_i\cdot(\mathrm{max}(1,f_i)-c_i))\cdot\frac{1}{1-r/d}\)<br>
\(=(d+(\sum_{i=1}^da_i\cdot(\mathrm{max}(1,f_i)-c_i)))\cdot\frac{1}{1-r/d}\)<br>
\(=(d-r)\cdot\frac{1}{1-r/d}\)<br>
\(=d\)

where the first step follows from Definition of <o>_x_</o><sub>i</sub> (see Eq. (17)), the second step follows from _c<sub>i</sub>=a<sub>i</sub>_+2, the third step follows from separating two summations, the forth step follows from \(\sum_{i=1}^da_i^2=1\), the fifth step follows from Definition of _r_ (see Eq. (16)), and the last step follows from simple algebra.

Lastly, this \(\overline{x}\in\mathbb{R}^d\) is also an approximation of<tbc>

\(\mathrm{min}_{a^\top x=d}\|x\|_\infty,\)

<tbc>because the optimal solution is _x=a_ which has \(\|x\|_\infty=1\) and for our <o>_x_</o> we have<tbc>

\(\|x\|_\infty\le\frac{1}{1-r/d}\)

<tbc>where for the true max-flow _f_<sup>∗</sup> of size \(F\le 4d\) (by \(c_i\le 4\) for all \(i\in[d]\)) we have

\(r=\sum_{i=1}^da_i(c_i-\mathrm{max}(1,f_i))\)<br>
\(=\sum_{i=1}^da_i(c_i-f^*)+\sum_{i=1}^da_i(f_i^*-\mathrm{max}(1,f_i))\)<br>
\(=\sum_{i=1}^da_i(f_i^*-\mathrm{max}(1,f_i))\)<br>
\(\le\sum_{i=1}^d(f_i^*-\mathrm{max}(1,f_i))\)<br>
\(\le\epsilon F\)<br>
\(\le 4\epsilon d\) (18)

where the first step follows from Eq. (16), the last step follows from \(F\le 4d\), the second step follows from simple algebra, the third step follows from \(c_i=f_i^*\) for all \(i\in[d]\), the forth step follows each summation term is positive and \(a_i\in\{\pm 1\}\), the fifth step follows from property of _f<sub>i</sub>_, and the last step follows from \(F\le 4d\).

Thus

\(\frac{1}{1-r/d}\le\frac{1}{1-4\epsilon}\le 1+1/8\)

where the first step follows from Eq. (16), the last step follows from \(\epsilon\in(0,1/36)\).

