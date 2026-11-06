<tbc>Hence<tbc>

\(\mathbb{E}Z_{(x,y)}\ge\left(\frac{n}{10}\right)^4p^5(1-p)^{20n}-O\left(\frac{1}{n^2}\right)=^{p=1/(4n)}\frac{1}{(4e)^510^4n}-O\left(\frac{1}{n^2}\right).\)

<tbc>Therefore:<tbc>

\(\mathbb{E}X_{(r,c)}\ge\sum_{(x,y)\in P}\mathbb{E}Z_{(x,y)}\ge\frac{|P|}{(4e)^510^4n}-O\left(\frac{|P|}{n^2}\right)\ge\frac{n}{5(4e)^510^4}-O(1)=2\beta n-O(1).\)

<tbc>Let \(\lambda:=\mathbb{E}X_{(r,c)}-\beta n\). Then \(\lambda\ge\beta n-O(1)=\Omega(n)\). By Theorem 4.11:

\(\mathbb{P}\left[X_{(r,c)}<\beta n\right]=\mathbb{P}\left[X_{(r,c)}<\mathbb{E}X_{(r,c)}-\lambda\right]\le 2\mathrm{exp}\left(-\frac{\lambda^2}{2n^2(1-p)p20^2+40\lambda/3}\right)\)<br>
\(\le\mathrm{exp}\left(-\Omega(n)\right).\)

This completes the proof of Claim 4.13, and hence also of Lemma 4.3. □

## 5. Proof of Theorem 1.1

In this section we use the results of Sections 3 and 4 to prove the enumeration in Theorem 1.1. The idea is to bound, from below, the number of successful outcomes of the random process. Then, we divide this by (an upper bound on) the number of ways in which each particular _n_-queens configuration can be constructed by the process. The result is a lower bound on Q(_n_).

We begin by counting the number of outcomes in the random greedy phase (Algorithm 2.1). We have shown that w.h.p. this algorithm succeeds in constructing a partial _n_-queens configuration with \(T=\left\lfloor(1-n^{-\alpha})n\right\rfloor\) queens. Furthermore, w.h.p. for every \(0\le t<T\), the number of available positions at time _t_ satisfies \(|\mathcal{A}(t)|=\left(1\pm n^{-0.4}\right)n^2(1-t/n)^4\). Thus, the number of outcomes of the random greedy phase is at least<tbc>

\(X:=\prod_{t=0}^{T-1}\left(1\pm n^{-0.4}\right)n^2(1-t/n)^4\ge\left(\left(1-n^{-\alpha}\right)n^2\right)^T\mathrm{exp}\left(4\sum_{t=0}^{T-1}\mathrm{log}\left(1-t/n\right)\right).\)

<tbc>Turning our attention to the sum, we have:<tbc>

\(\sum_{t=0}^{T-1}\mathrm{log}\left(1-t/n\right)=n\frac{1}{n}\sum_{t=0}^{T-1}\mathrm{log}\left(1-t/n\right)\ge n\int_0^{T/n}\mathrm{log}(1-x)dx\ge-n\left(1+\tilde{O}(n^{-\alpha})\right).\)

<tbc>Hence:

\(X\ge\left(\left(1-\tilde{O}(n^{-\alpha})\right)n^2\right)^T\mathrm{exp}\left(-4n-\tilde{O}(n^{1-\alpha})\right)\ge\left(\left(1-\tilde{O}(n^{-\alpha})\right)\frac{n^2}{e^4}\right)^n.\)

Furthermore, by Lemma 4.3 all but a vanishing fraction of these outcomes are 10(_n-T_)- absorbing, and therefore can be completed to a complete configuration by Algorithm 2.2.

We now wish to bound, from above, the number of ways in which a specific _n_-queens configuration can be constructed by the algorithm. Given such a configuration, 2(_n-T_) of its queens were placed by the absorbing stage. Given 2(_n-T_) queens, there are (2(_n-T_)-1)!!=(2(_n-T_))!/(2<sup>_n-T_</sup>(_n-T_)!) ways to partition them into _n-T_ pairs. For each pair, there are (at most) 2 ways it might have been obtained as an absorber.

