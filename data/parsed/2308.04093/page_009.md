multiple instances with smaller _b_).

## 1.3 Further related works

In contrast to our 0-1 setting, the _unbounded_ setting (where each item has infinitely many copies available) has also been widely studied in the literature of Knapsack and Subset Sum algorithms, e.g., \[LPV20, JR19, JR22, AT19, CH22, Kle22, DMZ23\].

For the easier Subset Sum problem, an early result for Subset Sum in terms of _n_ and _w_<sub>max</sub> is Pisinger’s deterministic _O(nw_<sub>max</sub>)-time algorithm for Subset Sum \[Pis99\]. This is not completely subsumed by Bringmann’s \(\widetilde{O}(n+t)\le\widetilde{O}(nw_\mathrm{max})\) time algorithm \[Bri17\], due to the extra log factors and randomization in the latter result. More recently, Polak, Rohwedder, and Wegrzycki \[PRW21\] observed that an \(\widetilde{O}(n+w_\mathrm{max}^2)\) time algorithm directly follows from combining their proximity technique with Bringmann’s \(\widetilde{O}(n+t)\) Subset Sum algorithm \[Bri17\]. They improved it to \(\widetilde{O}(n+w_\mathrm{max}^{5/3})\) time, by further incorporating additive combinatorial techniques by \[BW21\]. Very recently, \[CLMZ24\] obtained \(\widetilde{O}(n+w_\mathrm{max}^{3/2})\)-time algorithm for Subset Sum, using their fine-grained proximity technique based on additive combinatorial results of \[BW21\].

Recently there has also been a lot of work on approximation algorithms for Knapsack and Subset Sum (and Partition) \[Cha18, Jin19, MWW19, BN21, DJM23, Mao23, CLMZ23\]. Prior to this work, the fastest known \((1-\varepsilon)\) approximation algorithm for 0-1 Knapsack had time complexity \(\widetilde{O}(n+1/\varepsilon^{2.2})\) \[DJM23\]. Notably, \[DJM23\] also used the additive combinatorial results of \[BW21\] to design knapsack approximation algorithms; this was the first application of additive combinatorial techniques to knapsack algorithms. In August 2023, Mao \[Mao23\] and Chen, Lian, Mao, and Zhang \[CLMZ23\] independently improved the time complexity to \(\widetilde{O}(n+1/\varepsilon^2)\), which is nearly tight under the (min,+)-convolution hypothesis \[CMWW19, KPS17\].

## 1.4 Open problems

There are several interesting open questions.

• In the regime where _n_ is much smaller than _w_<sub>max</sub>, can we get faster algorithms for 0-1 Knapsack? The independent work of He and Xu \[HX24\] achieved \(\widetilde{O}(n^{1.5}w_\mathrm{max})\) time. By combining with our result, one can also bound the running time as \(\widetilde{O}(n+\mathrm{min}\{n^{1.5}w_\mathrm{max},w_\mathrm{max}^2\})\le\widetilde{O}(nw_\mathrm{max}^{4/3})\). Can we achieve \(\widetilde{O}(nw_\mathrm{max})\) time (which would also match the \((n+w_\mathrm{max})^{2-o(1)}\) conditional lower bound based on (min,+)-convolution hypothesis \[CMWW19, KPS17\])?<tbc>

• Can we solve 0-1 Knapsack in \(O((n+w_\mathrm{max}+p_\mathrm{max})^{2-\delta})\) time for any constant \(\delta>0\)? Bringmann and Cassis \[BC22\] gave algorithms of such running time for the easier unbounded knapsack problem. They also showed that such algorithms require computing bounded-difference (min,+)-convolution \[CL15, CDXZ22\].<tbc>

• Can we solve 0-1 Knapsack in \(O(n+w_\mathrm{max}^2/2^{\Omega(\sqrt{\mathrm{log}w_\mathrm{max}})})\) time, matching the best known running time for (min,+)-convolution \[Wil18, BCD<sup>+</sup>14, CW21\]? Algorithms with such running time are known for the easier unbounded knapsack problem \[AT19, CH22, DMZ23\].<tbc>

• Can Subset Sum be solved in \(\widetilde{O}(n+w_\mathrm{max})\) time? This question has been repeatedly asked in the literature \[ABJ<sup>+</sup>19, ABHS22b, BW21, PRW21, BC22\]. Currently the best result is the very recent \(\widetilde{O}(n+w_\mathrm{max}^{3/2})\)-time randomized algorithm by Chen, Lian, Mao, and Zhang \[CLMZ24\].<tbc>

