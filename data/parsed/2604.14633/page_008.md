**Lemma 13.** _If_ \(g/u>-1/(3\alpha)\)_, then_ \(\tilde{w}(\partial^+S)\ge\frac{1}{9}\tilde{w}(\partial S)\) _for all_ \(S\subseteq V\) .

_Proof._ By Lemma 6, we have \(w(\partial^+S)\ge\frac{1}{2}w(\partial^-S)\) for all \(S\subseteq V\) . Together with Lemma 12, we have \(2\tilde{w}(\partial^+S)\ge w(\partial^+S)\ge\frac{1}{2}w(\partial^-S)\ge\frac{1}{4}\tilde{w}(\partial^-S)\), so \(\tilde{w}(\partial^+S)\ge\frac{1}{8}\tilde{w}(\partial^-S)\), or equivalently \(\tilde{w}(\partial^+S)\ge\frac{1}{9}\tilde{w}(\partial S)\).

## 3.2 Energy Bounds

To bound the running time, we need to track the number of calls to ToggleCut. Let _M=n_<sup>_O_(1)</sup> be large enough, and define the _energy_ of arc (_u,v_) as<tbc>

\(\mathcal{E}(u,v)=\int_{\mathbf{y}(v)-\mathbf{y}(u)}^M\frac{1}{max\{x,0\}+1}dx.\)

<tbc>Observe that

\(\mathcal{E}(u,v)=\left\{\begin{array}{ c c }
ln(M+1)-ln(\mathbf{y}(v)-\mathbf{y}(u)+1) & \text{if}\mathbf{y}(v)\ge\mathbf{y}(u), \\
ln(M+1)+\mathbf{y}(u)-\mathbf{y}(v) & \text{if}\mathbf{y}(v)\le\mathbf{y}(u).
\end{array}\right.\)

The following lemma shows that each call to ToggleCut decreases the total energy by an additive 1_/n_<sup>_o_(1)</sup>.

**Lemma 14** (Energy decrease)**.** _On each call to_ ToggleCut_, the total energy decreases by at least_ \(\Omega(1/\alpha^3)\).

_Proof._ On each call to ToggleCut\((\eta)\), the implicit cut _C_ satisfies \(g/u\le-1/(3\alpha)\), where **g**(_C_)=_g\<_0 and \(\mathbf{u}(\partial C)\le u\). We also have \(\mathbf{u}(\partial C)\ge u/\alpha\) since otherwise, if \(\mathbf{u}(\partial C)<u/\alpha\), then the ratio \(\mathbf{g}(C)/\mathbf{u}(\partial C)\) would be less than \(\mathbf{g}(C)/(u/\alpha)=\alpha\cdot g/u\), contradicting the fact that _g/u_ is at most \(1/\alpha\) times the min-ratio cut.

We now analyze the contribution of ToggleCut\((\eta)\) to the total energy. Let _w_ and **y** be the weight and potential function immediately before ToggleCut\((\eta)\). For each arc \((u,v)\in\partial^+C\), the value of **y**(_u_) is increased by \(\eta\), so the energy E(_u,v_) increases by<tbc>

\(\int_{\mathbf{y}(v)-\mathbf{y}(u)-\eta}^{\mathbf{y}(v)-\mathbf{y}(u)}\frac{1}{max\{x,0\}+1}dx.\)

<tbc>Similarly, for each arc \((u,v)\in\partial^-C\), the value of **y**(_v_) is increased by \(\eta\), so the energy E(_u,v_) decreases by<tbc>

\(\int_{\mathbf{y}(v)-\mathbf{y}(u)}^{\mathbf{y}(v)-\mathbf{y}(u)+\eta}\frac{1}{max\{x,0\}+1}dx.\)

<tbc>By the approximation of weights (Lemma 12), we have \(w(u,v)\le 2\tilde{w}(u,v)\), so for any arc \((u,v)\in\partial C\), we have \(u\ge\mathbf{u}(\partial C)\ge\tilde{w}(u,v)\ge\frac{1}{2}w(u,v)\). Since \(\eta=\frac{1}{16\alpha u}\le\frac{1}{8\alpha\cdot w(u,v)}\), by the stability guarantee (Lemma 11) with \(\delta=\frac{1}{8\alpha}\), we have<tbc>

\(\frac{1}{1+1/(8\alpha)}w(u,v)\le\frac{1}{max\{x,0\}+1}\le\frac{1}{1-1/(8\alpha)}w(u,v)\text{for all}x\in[\mathbf{y}(v)-\mathbf{y}(u)-\eta,\mathbf{y}(v)-\mathbf{y}(u)+\eta].\)

