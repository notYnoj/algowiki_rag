Now, it remains to specify the size of _A<sub>r</sub>_, which we can do as follows:

\(|A_r|=|A|-\left(|A_v|+|A_c|+|A_t|\right)\)<br>
\(=\left[\frac{8}{3}\left(1728n^2+43n+24\sqrt{6}\sqrt{864n^4+43n^3}\right)\right]\)<br>
\(-\left(\frac{56}{3}n+96n\left(\left[\sqrt{\left[\frac{8}{3}\left(1728n^2+43n+24\sqrt{6}\sqrt{864n^4+43n^3}\right)\right]}\right]\right]+1\right)\right).\)

Notice that all components in the equation except of \(-\frac{56}{3}n\) are integers and that, by the structure of (2,2)-e3-sat instances, it must be that \(\frac{2}{3}n\in\mathbb{N}\). Thus, because \(m=\frac{4}{3}n\) must also be a positive integer, we can assume that \(n\in 3\mathbb{N}\), in which case |_A<sub>r</sub>_| is an integer value. We need to verify that |_A<sub>r</sub>_| is non-negative.

**Claim 12.** _For any integer_ \(n\ge 1\), |_A<sub>r</sub>|\>_0.

_Proof of Claim 12._ First, we define

\(R(n)=24\sqrt{6}\sqrt{864n^4+43n^3},\)<br>
\(a(n)=1728n^2+43n,\text{and}\)<br>
\(C(n)=\left[\frac{8}{3}\left(a(n)+R(n)\right)\right].\)

Notice that

\(R(n)^2=2985984n^4+148608n^3,\text{and}\)<br>
\(a(n)^2=2985984n^4+148608n^3+1849n^2.\)

Therefore,

\(R(n)^2=a(n)^2-1849n^2,\)

and thus, by \(n\ge 1\),

\(\left(a(n)-1\right)^2=a(n)^2-2a(n)+1\)<br>
\(=2985984n^4+148608n^3-1607n^2-86n+1\)<br>
\(=R(n)^2-1607n^2-86n+1\)<br>
\(<R(n)^2\)<br>
\(<a(n)^2,\)

so

\(a(n)-1<R(n)<a(n).\)

Clearly, there must exist some \(0<\varepsilon<1\) such that

\(R(n)=a(n)-1+\varepsilon.\)

Thus, substituting this expression for _R(n_) in _C(n_), we get

\(C(n)=\left[\frac{8}{3}\left(2a(n)+\varepsilon-1\right)\right]\)<br>
\(=\left[9216n^2+229n+\frac{n}{3}+\frac{8}{3}\varepsilon-\frac{8}{3}\right].\)

