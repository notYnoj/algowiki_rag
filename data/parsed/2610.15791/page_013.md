## 7 Comparison in ordinal-optimization terms

We use the equivalent blind-pick size to compare the exact values in OO terms. We first consider selection of the best design, then examine how the comparison changes when more designs are accepted as good enough.  1 reports the sizes _nC<sub>q</sub>(n,_1) and _nQ_<sub>1</sub>(_n,_1) for selecting the best of _n_ designs. The classical values are exact for every \(n\ge q+1\) (Theorem 1). The quantum values follow from Corollary 2 and are rounded to four decimals. The quantum entries at _n_=2 and _n_=9 are displayed exactly. The value at _n_=3 is \(1+\sqrt{2}\). For one classical comparison the size is 2 for every \(n\ge 2\) (Corollary 1). For one quantum comparison it increases from 2 toward about 3.30 as _n_ grows (Corollary 2). The values coincide at _n_=2, because one comparison orders two designs. One quantum comparison has a larger equivalent blind-pick size than two classical comparisons exactly when \(n\ge 10\). The classical entry with two comparisons is omitted at _n_=2, where one comparison already identifies the best design.

For a fixed pool of seven designs, we next vary the good-enough target.  2 reports alignment probabilities for the top _r_, for \(1\le r\le 6\). It also gives the equivalent blind-pick size \(s_\text{eq}^Q(7,r)\) of one quantum comparison. The blind pick selects one design. Classical values follow from Theorem 1 and quantum values from Theorem 3. Decimal values are rounded to four places. The equivalent blind-pick size of one classical comparison is 2 for every _r_ in the table (Corollary 1). For \(r\le 5\), the probability with one quantum comparison is strictly between those with one and two classical comparisons. An alignment probability of 0.8 for the best three of seven requires two classical comparisons, since _C_<sub>1</sub>(7,3)=5/7, whereas one quantum comparison suffices. The same holds for an alignment probability of 0.9 for the best four, since _C_<sub>1</sub>(7,4)=6/7.

In OO applications the good-enough set is usually a small fraction of many designs. To examine this regime,  3 reports alignment probabilities for the top _r_ of _n_=1000 designs and the equivalent blind-pick size \(s_\text{eq}^Q(1000,r)\) of one quantum comparison. Values are rounded to four decimals. The equivalent blind-pick size of one quantum comparison is about 3.27 for the top 5 percent, 3.23 for the top 10 percent and 3.14 for the top 20 percent. Each exceeds the size 3 of two classical comparisons. For the top half the quantum size is 2.77, below 3. In the cases computed, the equivalent size decreases as the good-enough set grows, so the quantum gain in these units is largest for selecting the best design.

For a fixed good-enough fraction, Corollary 3 gives a comparison that no longer depends on the number of designs. The classical limit is \(lim_{n\rightarrow\infty} C_1(n,\lfloor\varrho n\rfloor)=1-(1-\varrho)^2\), by Theorem 1.<tbc>

\begin{tabular}{cccc}
_n_ & classical, _q_=1 & classical, _q_=2 & quantum, _q_=1 \\
2 & 2 & & 2 \\
3 & 2 & 3 & 2.4142 \\
4 & 2 & 3 & 2.6302 \\
7 & 2 & 3 & 2.9145 \\
9 & 2 & 3 & 3 \\
10 & 2 & 3 & 3.0300 \\
20 & 2 & 3 & 3.1659 \\
100 & 2 & 3 & 3.2753 \\
\(\infty\) & 2 & 3 & 3.3028 \\
\end{tabular}

1: Equivalent blind-pick sizes for selecting the best design.

