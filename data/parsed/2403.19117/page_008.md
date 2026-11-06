## 8 A Faster Algorithm for Pigeonhole Equal Sums

We think of each set \(S\in B_{r^*}\) as a ball of color _w(S_), and apply Lemma 10 to the _k_ integers (colors) \(t\in\mathbb{N}\) ensured by Lemma 9, each having at least _h_ sets (balls) \(S\in B_{r^*}\) with _w(S_)=_t_. We set the sample rate to be

\(\alpha:=\frac{1}{2h\sqrt{k}}\le\frac{1}{2h}.\) (13)

Then the failure probability of the subsampling step is at most

\(\mathrm{exp}(-kh(h-1)\alpha^2/4)=\mathrm{exp}(-\frac{h-1}{16h})\le\mathrm{exp}(-1/32),\)

Overall, the probability that the algorithm successfully finds a solution is at least \(\Omega(1/n)\cdot(1-\mathrm{exp}(-1/32))\ge\Omega(n^{-1})\).

## Time complexity

The mod-_p_ DP runs in \(O^*(p)\le O^*(P)\) time. Since the bins have total size \(\sum_{r\in\mathbb{Z}_p}|B_r|=2^n\), the chosen bin _B_<sub>_r_<sup>∗</sup></sub> has expected size \(\mathbf{E}_{r^*\in\mathbb{Z}_p}[|B_{r^*}|]=2^n/p\le 2^n/P\), and hence the subsample \(C\subseteq B_{r^*}\) has expected size \(\mathbf{E}[|C|]\le\alpha 2^n/P\). To detect a solution \(S,S'\in C\) with \(w(S)=w(S')\), we simply sort _C_ in near-linear time. Hence the total expected running time is \(O^*(P+\alpha 2^n/P)\). By Markov’s inequality, with probability at least 1-_n_<sup>-10</sup>, the algorithm terminates in \(O^*(P+\alpha 2^n/P)\) time. By a union bound, the algorithm successfully finds a solution in time \(O^*(P+\alpha 2^n/P)\) with probability at least \(\Omega(n^{-1})-n^{-10}\ge\Omega(n^{-1})\). This success probability can be boosted to 0.99 by repeating the algorithm _O(n_) times.

Recall from Equations (12) and (13) that \(\alpha=\frac{1}{2h\sqrt{k}}=\frac{1}{2h\sqrt{\lceil m/4P\rceil}}\le\frac{\sqrt{P}}{h\sqrt{m}}\), so the run time is (ignoring poly(_n_) factors)

\(P+\alpha 2^n/P\le P+\frac{2^n}{h\sqrt{mP}}.\)

Recall _h_=2_<sup>j</sup>_+1 (where \(0\le j\le n-1\)) and \(m=\lceil\frac{\Delta}{2^{j+1}n}\rceil\), and hence \(hm<h(1+\frac{\Delta}{2^{j+1}n})\le h+\frac{\Delta}{n}<(2^{n-1}+1)+\frac{2^n}{n}\le 2^n\) (assuming \(n\ge 3\)). Now we set

\(P:=2m\cdot\mathrm{min}\left\{1,\big(\frac{2^n}{hm^2}\big)^{2/3}\right\},\)

and we first need to verify the requirement \(2\le P\le 2m\) introduced earlier: The upper bound is obvious. To see the lower bound, note that \(2m\ge 2\) and \(2m\cdot\big(\frac{2^n}{hm^2}\big)^{2/3}=2\big(\frac{2^{2n}}{h^{2m}}\big)^{1/3}\ge 2\big(\frac{2^{2n}}{(hm)^2}\big)^{1/3}\ge 2\) (using the inequality \(hm\le 2^n\) we just showed).

Hence, the overall running time is at most (ignoring poly(_n_) factors)

\(P+\frac{2^n}{h\sqrt{mP}}\le 2m\big(\frac{2^n}{hm^2}\big)^{2/3}+\frac{2^n}{h\sqrt{m\cdot 2m}}\cdot\mathrm{max}\left\{1,\big(\frac{hm^2}{2^n}\big)^{1/3}\right\}\)<br>
\(=2\cdot\frac{2^{2n/3}}{h^{2/3}m^{1/3}}+\frac{1}{\sqrt{2}}\mathrm{max}\left\{\frac{2^n}{hm},\frac{2^{2n/3}}{h^{2/3}m^{1/3}}\right\}\)<br>
\(\le O\big(\frac{2^{2n/3}}{h^{2/3}m^{1/3}}+\frac{2^n}{hm}\big)\)<br>
\(\le O^*\big(\frac{2^{2n/3}}{h^{1/3}\Delta^{1/3}}+\frac{2^n}{\Delta}\big)\text{(by}hm>\frac{\Delta}{2n}\text{from Equation (10))}\)<br>
\(\le O^*\big(\frac{2^{2n/3}}{\Delta^{1/3}}\big).\text{(by}h>1\text{and the assumption that}\Delta\ge 2^{n/2}\text{)}\)

This finishes the proof of Lemma 5.

