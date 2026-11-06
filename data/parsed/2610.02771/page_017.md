## B Proofs for Section 2 (A 1-bit mean estimator)

Throughout all the proofs, we write \(a\wedge b:=\mathrm{min}\{a,b\}\).

### B.1 Proof of Lemma 2 (Tail-integral identity)

_Proof._ Fix \(w\in\mathbb{R}\) and _L\>_0.<br>
If \(w\ge 0\), then \(\mathbf{1}\{w\le-t\}=0\) for every \(t\ge 0\), and hence<tbc>

\(\int_0^L\big(\mathbf{1}\{w\ge t\}-\mathbf{1}\{w\le-t\}\big)dt=\int_0^L\mathbf{1}\{w\ge t\}dt=\int_0^{w\wedge L}1dt=w\wedge L=[w]_L.\)

<tbc>If _w\<_0, then \(\mathbf{1}\{w\ge t\}=0\) for every \(t\ge 0\), and therefore<tbc>

\(\int_0^L\big(\mathbf{1}\{w\ge t\}-\mathbf{1}\{w\le-t\}\big)dt=-\int_0^L\mathbf{1}\{w\le-t\}dt=-\int_0^{(-w)\wedge L}1dt=[w]_L.\)

<tbc>This proves the pointwise identity. Taking expectations gives

\(\mathbb{E}[[W]_L]=\int_0^L\big(\mathrm{Pr}(W\ge t)-\mathrm{Pr}(W\le-t)\big)dt,\)

since the integrand is bounded in absolute value by 1 on a finite interval.

### B.2 Proof of Lemma 3

We fix \(L\ge\sigma\) in the following proofs.

_Proof of (i)._ Condition on _W=w_. Since _S_ is uniform on {+1,-1}, independent of _T_, and<tbc>

\(Y=\mathbf{1}\{S(X-c)\ge T\}=\mathbf{1}\{SW\ge T\},\)

<tbc>we have

\(\mathbb{E}[Z|W=w]=\frac{1}{2}\int_0^L\frac{2}{g_L(t)}g_L(t)\mathbf{1}\{w\ge t\}dt-\frac{1}{2}\int_0^L\frac{2}{g_L(t)}g_L(t)\mathbf{1}\{w\le-t\}dt\)<br>
\(=\int_0^L\big(\mathbf{1}\{w\ge t\}-\mathbf{1}\{w\le-t\}\big)dt.\)

By Lemma 2, this equals \[_w_\]_<sub>L</sub>_. Therefore<tbc>

\(\mathbb{E}[Z|W]=[W]_L\text{almost surely.}\)

<tbc>and taking expectations yields

\(\mathbb{E}[Z]=\mathbb{E}[[W]_L].\)

<tbc>_Proof of (ii)._ Again condition on _W=w_, and set<tbc>

\(u:=|w|\wedge L.\)

<tbc>Since \(Z=\frac{2S}{g_L(T)}Y\) , we have \(Z^2=\frac{4}{g_L(T)^2}Y\) . Hence

\(\mathbb{E}[Z^2|W=w]=\frac{1}{2}\int_0^L\frac{4}{g_L(t)^2}g_L(t)\mathbf{1}\{w\ge t\}dt+\frac{1}{2}\int_0^L\frac{4}{g_L(t)^2}g_L(t)\mathbf{1}\{w\le-t\}dt\)<br>
\(=2\int_0^L\frac{1}{g_L(t)}\big(\mathbf{1}\{w\ge t\}+\mathbf{1}\{w\le-t\}\big)dt\)<br>
\(=2\int_0^u\frac{dt}{g_L(t)}.\)

