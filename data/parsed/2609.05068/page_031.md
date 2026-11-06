**Algorithm 1** Greedy Heuristic Algorithm

\(\forall k\in K\): \(Q^k\leftarrow P^k\)<br>
_H_=0, \(H^-=\text{OPT}(\text{DCMCF}_{\{Q^k\}_{k\in K}})\)<br>
while \(H^-\ge H\) do<br>
   \((k^-,p^-)=\text{argmin}\{x_p^k|x_p^k>0,\sum_{a\in p}\frac{1}{c_a-y_a}=d^k\}\)<br>
   \(Q^{k^-}=Q^{k^-}\backslash\{p^-\}\)<br>
   _H=H_<sup>-</sup>, \(H^-=\text{OPT}(\text{DCMCF}_{\{Q^k\}_{k\in K}})\)<br>
end while<br>
return _H_

\(S\ge 1\) then \(|Q_S^k|\ge 1\) for every commodity \(k\in K\), and the heuristic H_<sub>threshold</sub>_ provides a strictly positive lower-bound for the DCMCF problem.

Before analyzing the performance guarantees of H_<sub>threshold</sub>_ in Section 5.3, we will present a lower bound of the optimal objective value of DCMCF that can be easily expressed and polynomially encoded in the size of the problem instance. While this bound is generally rather loose, it will nonetheless be used in the analysis of H<sub>threshold</sub> in the next section.

**Lemma 5.2.** _There exists a feasible solution_ \(\gamma\) _of DCMCF such that:_

\(\gamma\ge\gamma_{low}=\mathrm{min}_{k\in K,p\in P^k}\frac{\frac{1}{\sum_{a\in p}\frac{1}{c_a}}-\frac{1}{d^k}}{\sum_{k^\prime\in K}b^{k^\prime}}.\) (35)

_Proof._ Let \(\gamma^{opt}\) be the optimal value of \(\gamma\) when DCMCF is solved exactly. Then, there is at least one commodity _k_, and one path \(p\in P^k\) such that \(\sum_{a\in p}\frac{1}{c_a-y_a}=d^k\). Moreover, for any \(a\in p\), starting from \(\frac{1}{c_a-y_a}\le d^k\), we get that \(\frac{y_a}{c_a-y_a}\le y_ad^k\) which can be written as \(\frac{c_a}{c_a-y_a}\le 1+y_ad^k\). Di viding by _c<sub>a</sub>_ leads to \(\frac{1}{c_a-y_a}\le\frac{1}{c_a}+y_a\frac{d^k}{c_a}\). Therefore, \(d^k=\sum_{a\in p}\frac{1}{c_a-y_a}\le\sum_{a\in p}\frac{1}{c_a}+y_a\frac{d^k}{c_a}\). By bounding _y<sub>a</sub>_ by \(\gamma^{opt}(\sum_{k^\prime\in K}b^{k^\prime})\), we get that \(d^k\le\sum_{a\in p}\frac{1}{c_a}+d^k\gamma^{opt}(\sum_{k^\prime\in K}b^{k^\prime})\sum_{a\in p}\frac{1}{c_a}\), leading to inequality (35).

## 5.3 Performance guarantees of H_<sub>threshold</sub>_

We show that H_<sub>threshold</sub>_, when applied with an appropriately chosen threshold, constitutes an approximation algorithm with provable performance<tbc>

