**Proof.** Refer to Figure 12 for a visualization of the ranges of \(x,y,x',y'\).

Consider arbitrary \((x,x')\in(|l(r)\times[|r(q')\dots r(s')])\cup([|l(r)\dots l(q)]\times r(q'))\) and \((y,y')\in(|r(r)\times[|r(q')\dots r(s')])\cup([|r(q)\dots r(r)]\times r(s'))\). We perform a case distinction.

**(1)** If there exists a node \(t\in\mathbf{S}\) such that \(r\le t<q\) and \(\mathrm{sim}(\mathbf{F}[x\dots y),\mathbf{F}'[x'\dots y'))\) aligns sub(_t_) to a subtree \(\mathbf{F}'[x'\dots y')\), then we note \(\mathrm{sim}(\mathbf{F}[x\dots y),\mathbf{F}'[x'\dots y'))=\mathrm{sim}_q(\mathbf{F}[x\dots y),\mathbf{F}'[x'\dots y'))\), where \(\mathrm{sim}_q\) comes from Lemma 4.10 applied on sub(_r_), \(\mathbf{F}'[|r(q')\dots r(s'))\), **S** and _q_.

**(2)** Otherwise, by Proposition 3.12, \(\mathrm{sim}(\mathbf{F}[x\dots y),\mathbf{F}'[x'\dots y'))=\mathrm{sim}(\mathbf{F}[x\dots l(q))+\mathbf{F}[|l(q)\dots y),\mathbf{F}'[x'\dots y'))\). From Proposition 3.10(i), follows that \(|l(q)\times[|r(q')\dots r(s')]\) and \(|r(q)\times[|r(q')\dots r(s')]\) are paired anchor sets of \(\mathrm{sim}(\mathbf{F}[x\dots y),\mathbf{F}'[x'\dots y'))\). Thus, we can write

\(\mathrm{sim}(\mathbf{F}[x\dots y),\mathbf{F}'[x'\dots y'))=\mathrm{max}_{z^\prime,w^\prime\in[|r(q^\prime)\dots r(s^\prime)]:x^\prime\le z^\prime\le w^\prime\le y^\prime}\big\{\mathrm{sim}(\mathbf{F}[x\dots l(q)),\mathbf{F}'[x'\dots z'))\)<br>
\(+\mathrm{sim}(\mathrm{sub}(q),\mathbf{F}'[z'\dots w'))\)<br>
\(+\mathrm{sim}(\mathbf{F}[|r(q)\dots y),\mathbf{F}'[w'\dots y'))\big\}.\)

This concludes our case distinction. To compute \(\mathrm{sim}(\mathbf{F}[x\dots y),\mathbf{F}'[x'\dots y'))\) for the desired ranges of \(x,y,x',y'\), we break down the index set for \(x,y,x',y'\) as follows (see Figure 12):

\(\{(x,x',y,y'):(x,x')\in(|l(r)\times[|r(q')\dots r(s')])\cup([|l(r)\dots l(q)]\times r(q')),\)<br>
\((y,y')\in(|r(r)\times[|r(q')\dots r(s')])\cup([|r(q)\dots r(r)]\times r(s'))\}=\)<br>
\(\{(x,x',y,y'):(x,x')\in|l(r)\times[|r(q')\dots r(s')],(y,y')\in|r(r)\times[|r(q')\dots r(s')]\}\) (11)

\(\cup\{(x,x',y,y'):(x,x')\in|l(r)\times[|r(q')\dots r(s')],(y,y')\in[|r(q)\dots r(r)]\times r(s')\}\) (12)

\(\cup\{(x,x',y,y'):(x,x')\in[|l(r)\dots l(q)]\times r(q'),(y,y')\in|r(r)\times[|r(q')\dots r(s')]\}\) (13)

\(\cup\{(x,x',y,y'):(x,x')\in[|l(r)\dots l(q)]\times r(q'),(y,y')\in[|r(q)\dots r(r)]\times r(s')\}.\) (14)

We construct the matrices \(A^{(1)}=(a_{i,j}^{(1)})\), \(A^{(2)}=(a_{i,j}^2)\), \(B=(b_{i,j})\), \(C^{(1)}=(c_{i,j}^{(1)})\), \(C^{(2)}=(c_{i,j}^{(2)})\) of sizes \(\mathrm{rsz}'\times\mathrm{rsz}'\), \(\mathrm{lsz}\times\mathrm{rsz}'\), \(\mathrm{rsz}'\times\mathrm{rsz}'\), \(\mathrm{rsz}'\times\mathrm{rsz}'\), \(\mathrm{rsz}\times\mathrm{rsz}'\), where \(\mathrm{rsz}'=\mathrm{r}(s')-\mathrm{r}(q')+1\), \(\mathrm{lsz}=|l(q)-|l(r)+1\), rsz=_r(r_)-_r(q_)+1, and defined as (in the following definitions, we index matrix entries from zero, instead of one):

\(a_{i,j}^{(1)}=\left\{\begin{array}{ c c }
\mathrm{sim}(\mathbf{F}[|l(r)\dots l(q)),\mathbf{F}'[|(r(q')+i)\dots(|r(q')+j)))) & i\le j \\
-\infty & \text{otherwise}',
\end{array}\right.\)<br>
\(a_{i,j}^{(2)}=\mathrm{sim}(\mathbf{F}[|(l(r)+i)\dots l(q)),\mathbf{F}'[|r(q')\dots(|r(q')+j))))\)<br>
\(b_{i,j}=\left\{\begin{array}{ c c }
\mathrm{sim}(\mathrm{sub}(q),\mathbf{F}'[|r(q')+i\dots r(q')+j))) & i\le j \\
-\infty & \text{otherwise}',
\end{array}\right.\)<br>
\(c_{i,j}^{(1)}=\left\{\begin{array}{ c c }
\mathrm{sim}(\mathbf{F}[|r(q)\dots r(r)),\mathbf{F}'[|(r(q')+i)\dots(|r(q')+j))) & i\le j \\
-\infty & \text{otherwise}
\end{array}\right.\)<br>
\(c_{i,j}^{(2)}=\mathrm{sim}(\mathbf{F}[|(r(q)+j)\dots r(r)),\mathbf{F}'[|(r(q')+i)\dots r(q')))\)

Observe that all matrices _A_<sup>(1)</sup>_,A_<sup>(2)</sup>_,B,C_<sup>(1)</sup>, and _C_<sup>(2)</sup> have dimensions bounded by _m_. We now outline the process for retrieving the required information to construct these matrices. The entries of _A_<sup>(1)</sup> and _A_<sup>(2)</sup> are derived from whole-infix and suffix-prefix similarities as specified in Main Theorem 4 for \(\mathbf{F}[|l(r)\dots l(q))\) and \(\mathbf{F}'[|r(q')\dots r(s'))\), respectively. The entries for matrix _B_ are directly provided by Input (v) of the \((s,s',q,q')\)-DISED instance. Similarly, _C_<sup>(1)</sup> and _C_<sup>(2)</sup> are constructed from whole-infix and suffix-prefix

