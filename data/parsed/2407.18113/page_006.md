**Fact 6.** _Let_ \(a,b\in\mathcal{A}\) _such that_ \(a\neq b\) _and_ \(s,t\in\mathcal{A}^*\)_, then_<tbc>

\(V_n(as,bt)\le 1+\left\{\begin{array}{ c }
\frac{1}{|\mathcal{A}|}\sum_{c\in\mathcal{A}}V_{n-1}(sc,bt) \\
\frac{1}{|\mathcal{A}|}\sum_{c\in\mathcal{A}}V_{n-1}(as,tc) \\
\frac{1}{|\mathcal{A}|^2}\sum_{c,c^\prime\in\mathcal{A}}V_{n-2}(sc,tc')
\end{array}\right..\)

<tbc>_Proof._ We have

\(V_n(as,bt)=\mathbb{E}\left[min_{i+j=ni,j\ge 0}d_e(asx_1x_2\dots x_i,bty_1y_2\dots y_j)\right]\)<br>
\(=\mathbb{E}\left[min_{i+j=ni,j\ge 0}\left(1+min\left\{\begin{array}{ c }
d_e(sx_1x_2\dots x_i,bty_1y_2\dots y_j) \\
d_e(asx_1x_2\dots x_i,ty_1y_2\dots y_j) \\
d_e(sx_1x_2\dots x_i,ty_1y_2\dots y_j)
\end{array}\right)\right]\)<br>
\(\le 1+min\left\{\begin{array}{ c }
\mathbb{E}\left[min_{i+j=ni,j\ge 0}d_e(sx_1x_2\dots x_i,bty_1y_2\dots y_j) \\
\mathbb{E}\left[min_{i+j=ni,j\ge 0}d_e(asx_1x_2\dots x_i,ty_1y_2\dots y_j)
\end{array}\right].\)

We upper bound the first term of this minimum as follows,

\(\mathbb{E}\left[min_{i+j=ni,j\ge 0}d_e(sx_1x_2\dots x_i,bty_1y_2\dots y_j)\right]\le\mathbb{E}\left[min_{i+j=ni\ge 1,j\ge 0}d_e(sx_1x_2\dots x_i,bty_1y_2\dots y_j)\right]\)<br>
\(=\frac{1}{|\mathcal{A}|}\sum_{c\in\mathcal{A}}\mathbb{E}\left[min_{i+j=ni\ge 1,j\ge 0}d_e(scx_2\dots x_i,bty_1y_2\dots y_j)\right]\)<br>
\(=\frac{1}{|\mathcal{A}|}\sum_{c\in\mathcal{A}}\mathbb{E}\left[min_{i+j=n-1i\ge 0,j\ge 0}d_e(scx_1\dots x_i,bty_1y_2\dots y_j)\right]\)<br>
\(=\frac{1}{|\mathcal{A}|}\sum_{c\in\mathcal{A}}V_{n-1}(sc,bt).\)

Similar computations for the two other terms of this minimum yields

\(V_n(as,bt)\le 1+\left\{\begin{array}{ c }
\frac{1}{|\mathcal{A}|}\sum_{c\in\mathcal{A}}V_{n-1}(sc,bt) \\
\frac{1}{|\mathcal{A}|}\sum_{c\in\mathcal{A}}V_{n-1}(as,tc) \\
\frac{1}{|\mathcal{A}|^2}\sum_{c,c^\prime\in\mathcal{A}}V_{n-2}(sc,tc')
\end{array}\right.,\)

as desired.

