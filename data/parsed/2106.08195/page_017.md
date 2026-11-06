<tbc>by the assumption in the theorem statement. By Chernoff bound, we have<tbc>

\(Pr[|\mathcal{G}\cap\mathcal{R}|<p|\mathcal{G}|/2]\le exp(-p|\mathcal{G}|/8)=exp(-n^{\Omega(1)}),\)

<tbc>and thus w.h.p. we have \(|\mathcal{G}\cap\mathcal{R}|\ge p|\mathcal{G}|/2\). Plugging this into our lower bound for \(\widetilde{L}\) yields w.h.p.

\(\widetilde{L}\ge\frac{p|\mathcal{G}|\hat{L}}{8\sqrt{T}}=\Omega\big(min\big\{\frac{L^3}{n^2},\frac{L^3T}{\lambda n^2},\frac{L^4T}{\lambda\mu n^2}\big\}\big),\)

assuming that our guesses \(\hat{L},\hat{\lambda},\hat{\mu}\) are correct up to constant factors. This shows the claimed lower bound.

**Running Time:** The expected running time of Step 1 is \(\widetilde{O}(n+M/q)=\widetilde{O}(T)\) since \(q=\frac{M}{T}\). Step 2 runs in time \(\widetilde{O}(\sum_j|y_j|)=\widetilde{O}(n)\). Steps 3 and 5 take time _O_((_n/m_)<sup>2</sup>)=_O(T_). In the remainder we show that Step 4 also runs in expected time \(\widetilde{O}(T)\), assuming that our guesses \(\hat{L},\hat{\lambda},\hat{\mu}\) are correct up to constant factors. Recall that w.h.p. \(M_{ij}/8-q\le\widetilde{M}_{ij}\le 4M_{ij}\); we condition on this event in the following.<sup>6</sup> Then \(\widetilde{M}_{ij}=O(\frac{\mu n}{L\sqrt{T}})\) implies \(M_{ij}=O(q+\frac{\mu n}{L\sqrt{T}})\). Using inequality (3) we have \(q=\frac{M}{T}\le\frac{2\mu}{\sqrt{T}}\le\frac{2\mu n}{L\sqrt{T}}\), so \(M_{ij}=O(\frac{\mu n}{L\sqrt{T}})\). Since only blocks (_i,j_) with \(\widetilde{M}_{ij}=O(\frac{\mu n}{L\sqrt{T}})\) are tested, each invocation of the basic approximation algorithm in Step 4 runs in expected time \(\widetilde{O}((|x_i|+M_{ij})L_{ij}\sqrt{T}/L+|x_i|\sqrt{T}/L)=\widetilde{O}((m+\frac{\mu n}{L\sqrt{T}})L_{ij}\sqrt{T}/L+m\sqrt{T}/L)\). Since each block is tested with probability at most _p_, Step 4 has an expected running time of

\(O\big(\sum_{i,j}p\cdot\big(\big(m+\frac{\mu n}{L\sqrt{T}}\big)L_{ij}\frac{\sqrt{T}}{L}+\frac{m\sqrt{T}}{L}\big)\big)=O\big(\big(\frac{n}{\sqrt{T}}+\frac{\mu n}{L\sqrt{T}}\big)\frac{p\lambda\sqrt{T}}{L}+\frac{pnT}{L}\big)\)<br>
\(=\widetilde{O}\big(\frac{p\lambda n}{L}+\frac{p\lambda\mu n}{L^2}+\frac{pnT}{L}\big).\)

Note that our choice of \(p=\Theta(min\{\frac{L}{n},\frac{LT}{\lambda n},\frac{L^2T}{\lambda\mu n}\})\) ensures that this running time is \(\widetilde{O}(T)\).

## 5.6 Combining the Algorithms

Now we combine Algorithms 1-4. We show that w.h.p. at least one of these algorithms computes an estimate \(\widetilde{L}=\widetilde{\Omega}(LT^{0.4}/n^{0.8})\). In other words, the combined algorithm has approximation ratio \(\widetilde{O}(n^{0.8}/T^{0.4})\) with a running time budget of \(\widetilde{O}(T)\) and thus prove Theorem 9.

**Theorem 9** (Main Result, Relaxation)**.** _Given strings x,y of length n and a time budget_ \(T\in[n,n^2]\)_, in expected time_ \(\widetilde{O}(T)\) _we can compute a number_ \(\widetilde{L}\) _such that_ \(\widetilde{L}\le L:=L(x,y)\) _and w.h.p._ \(\widetilde{L}\ge\widetilde{\Omega}(LT^{0.4}/n^{0.8})\).

**Algorithm 1:** Recall from Theorem 10 that Algorithm 1 w.h.p. returns \(\widetilde{L}\ge min\{L,\sqrt{LT/n}\}\). If \(\widetilde{L}\ge L\) then we solved the problem exactly, so we only need to consider the case \(\widetilde{L}\ge\sqrt{LT/n}=L\sqrt{T/(Ln)}\). Assuming that \(L\le n^{0.6}T^{0.2}\), we obtain the claimed approximation guarantee \(\widetilde{L}\ge LT^{0.4}/n^{0.8}\). Hence, from now on we can assume

\(L>n^{0.6}T^{0.2}.\) (6)

**Algorithm 2:** Recall from Theorem 13 that Algorithm 2 w.h.p. returns \(\widetilde{L}=\Omega(\mu\sqrt{T}/n)\). Assuming that \(\mu\ge Ln^{0.2}/T^{0.1}\), we obtain the claimed approximation guarantee \(\widetilde{L}=\Omega(LT^{0.4}/n^{0.8})\). Hence, from now on we can assume

\(\mu<\frac{Ln^{0.2}}{T^{0.1}}.\) (7)

<sup>6</sup>In the error event we bound the running time of Step 4 by _O(n_<sup>2</sup>). This has a negligible contribution to the expected running time of Step 4.

