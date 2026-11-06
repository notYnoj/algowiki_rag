## 2.2 Bounds on \(\alpha'_k\)

For any \(n\in\mathbb{N}\) and, \(s,t\in\mathcal{A}^*\), we let

\(V_n(s,t)=\mathbb{E}\left[\mathrm{min}_{i+j=ni,j\ge 0}d_e(sX_1X_2\dots X_i,tY_1Y_2\dots Y_j)\right].\)

As _n_ goes to infinity, the impact of the fixed prefixes _s_ and _t_ is negligible and the following Lemma is immediate.

**Lemma 4.** _For any fixed_ \(s,t\in\mathcal{A}^*\)_, we have_

\(\alpha'_k=\mathrm{lim}_{n\rightarrow\infty}\frac{V_n(s,t)}{n}.\)

We are now ready to bound \(\alpha'_k\) using this second expression. We let \(\vec{V_n}\) be the vector whose components are the _V<sub>n</sub>(s,t_) where _s_ and _t_ range over all strings of length _h_ for a given _h_. Using the dynamic programming given earlier we provide upper bounds on the components of \(\vec{V_n}\) based on \(\vec{V_{n-1}}\) and \(\vec{V_{n-2}}\).

**Fact 5.** _Let_ \(a\in\mathcal{A}\) _and_ \(s,t\in\mathcal{A}^*\)_, then_

\(V_n(as,at)\le\frac{1}{|\mathcal{A}|^2}\sum_{c,c^\prime\in\mathcal{A}}V_{n-2}(sc,tc').\) (5)

_Proof._ We have

\(V_n(as,at)=\mathbb{E}\left[\mathrm{min}_{i+j=ni,j\ge 0}d_e(asx_1x_2\dots x_i,aty_1y_2\dots y_j)\right]\)<br>
\(=\mathbb{E}\left[\mathrm{min}_{i+j=ni,j\ge 0}d_e(sx_1x_2\dots x_i,ty_1y_2\dots y_j)\right]\)<br>
\(\le\mathbb{E}\left[\mathrm{min}_{i+j=ni,j\ge 1}d_e(sx_1x_2\dots x_i,ty_1y_2\dots y_j)\right]\)<br>
\(=\frac{1}{|\mathcal{A}|^2}\sum_{c,c^\prime\in\mathcal{A}}\mathbb{E}\left[\mathrm{min}_{i+j=ni,j\ge 1}d_e(scx_2\dots x_i,tc'y_2\dots y_j)\right]\)<br>
\(=\frac{1}{|\mathcal{A}|^2}\sum_{c,c^\prime\in\mathcal{A}}\mathbb{E}\left[\mathrm{min}_{i+j=n-2i,j\ge 0}d_e(scx_1\dots x_i,tc'y_1\dots y_j)\right]\)<br>
\(=\frac{1}{|\mathcal{A}|^2}\sum_{c,c^\prime\in\mathcal{A}}V_{n-2}(sc,tc'),\)

as desired.

