None of the above algorithms match the \((n+w_\mathrm{max})^{2-\circ(1)}\) conditional lower bound. The following question has been asked by \[PRW21, BC22, CLMZ24\]:

_Main question: Can 0-1 Knapsack be solved in_ \(\widetilde{O}(n+w_\mathrm{max}^2)\) _time?_

We remark that this \(\widetilde{O}(n+w_\mathrm{max}^2)\) running time is known to be achievable for the easier _Unbounded Knapsack_ problem (where each item has infinitely many copies available) \[AT19, CH22, DMZ23\], matching the \((n+w_\mathrm{max})^{2-\delta}\) conditional lower bound for Unbounded Knapsack \[CMWW19, KPS17\]. As argued by \[PRW21\], the 0-1 setting appears to be much more difficult, and most of the techniques for Unbounded Knapsack do not appear to apply to the 0-1 setting.

## 1.1 Our contribution

In this paper, we affirmatively resolve this main question, closing the gap between the previous \(\widetilde{O}(n+w_\mathrm{max}^{12/5})\) upper bound \[CLMZ24\] and the quadratic conditional lower bound \[CMWW19, KPS17\].

**Theorem 1.1.** _The 0-1 Knapsack problem can be solved by a deterministic algorithm with time complexity_ \(O(n+w_\mathrm{max}^2\mathrm{log}^4w_\mathrm{max})\).

In our paper we only describe an algorithm that outputs the total profit of the optimal knapsack solution. It can be modified to output an actual solution using the standard technique of back pointers, without affecting the asymptotic time complexity.

By a reduction described in \[PRW21, Section 4\], we have the following corollary which parameterizes the running time by the largest item profit _p_<sub>max</sub> instead of _w_<sub>max</sub>.

**Corollary 1.2.** _The 0-1 Knapsack problem can be solved by a deterministic algorithm with time complexity_ \(O(n+p_\mathrm{max}^2\mathrm{log}^4p_\mathrm{max})\).

### Independent works.

Independently and concurrently to our work, Bringmann \[Bri23\] also obtained an \(\widetilde{O}(n+w_\mathrm{max}^2)\) time algorithm for 0-1 Knapsack (more generally, Bounded Knapsack).

### Chronological remarks.

The current paper is a substantially updated version of an earlier manuscript (posted to arXiv in July 2023). This earlier manuscript contained much weaker results, and is obsolete now. Our current paper incorporates part of the techniques from our earlier manuscript, and also builds on the very recent work by Chen, Lian, Mao, and Zhang \[CLMZ24\] (posted to arXiv in July 2023).

## 1.2 Technical overview

Our Knapsack algorithm combines and extends several recent structural results and algorithmic techniques from the literature on knapsack-type problems. In particular, we crucially build on the techniques from two previous papers by Chen, Lian, Mao, and Zhang \[CLMZ24\], and by Deng, Mao, and Zhong \[DMZ23\]. Now we review the techniques in prior works and describe the ideas behind our improvement.

first algorithm for 0-1 Knapsack with subcubic dependence on (_n+w_<sub>max</sub>+_p_<sub>max</sub>).

