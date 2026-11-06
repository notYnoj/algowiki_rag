Substituting these expressions gives

\(\sum_{i>j}(t_i-t_j)^2=2^{n-1}\cdot 2^{n-3}\left(\sum_{i=1}^{n-1}a_i^2+T^2\right)-2^{2n-4}T^2\)<br>
\(=2^{2n-4}\sum_{i=1}^{n-1}a_i^2\)<br>
\(=\frac{2^{2(n-1)}}{4}\sum_{i=1}^{n-1}a_i^2.\)

From Lemma 1, we have

\(t_i-t_j\ge 2a_n\left\lfloor\frac{i-j}{a_n}\right\rfloor.\)

Therefore,

\(\frac{2^{2(n-1)}}{4}\sum_{i=1}^{n-1}a_i^2\ge 4a_n^2\sum_{i>j}\left\lfloor\frac{i-j}{a_n}\right\rfloor^2\)<br>
\(\ge(1-o(1))4a_n^2\sum_{k=1}^{\lfloor 2^{n-1}/a_n\rfloor} k^2a_n(2^{n-1}-ka_n)\)<br>
\(=(1-o(1))4a_n^3\sum_{k=1}^{\lfloor 2^{n-1}/a_n\rfloor}\left(2^{n-1}k^2-a_nk^3\right)\)<br>
\(\ge(1-o(1))4a_n^3\left(\frac{2^{n-1}}{3}\frac{2^{3(n-1)}}{a_n^3}-\frac{a_n}{4}\frac{2^{4(n-1)}}{a_n^4}\right)\)<br>
\(=(1-o(1))\frac{2^{4(n-1)}}{3}.\)

Hence,

\(\sum_{i=1}^{n-1}a_i^2\ge(1-o(1))\frac{2^{2n}}{3}.\)

Since

\(\sum_{i=1}^{n-1}a_i^2\le(n-1)a_{n-1}^2,\)

we obtain

\((n-1)a_{n-1}^2\ge(1-o(1))\frac{2^{2n}}{3}.\)

Consequently,

\(a_{n-1}\ge\left(\frac{1}{\sqrt{3}}-o(1)\right)\frac{2^n}{\sqrt{n-1}}=\left(\frac{2}{\sqrt{3}}-o(1)\right)\frac{2^{n-1}}{\sqrt{n-1}},\)

which is better than the lower bound obtained directly, i.e., \(a_{n-1}\ge\left(\sqrt{\frac{2}{\pi}}-o(1)\right)\frac{2^{n-1}}{\sqrt{n-1}}\).

