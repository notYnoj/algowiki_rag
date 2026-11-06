<tbc> 4 compares this value with \(F_1(\varrho)\). At a good-enough fraction of 5 percent, the limiting quantum success probability is about 0.1543, close to the finite value 0.1544 for 1000 designs in  3.

With exact comparisons and one selected design, no adaptive choice of pairs improves on a blind pick of _q_+1 designs followed by a knockout. The budget needed for a target probability therefore follows from (3). If the exact comparison oracle can be queried coherently, the equivalent blind-pick size of one quantum comparison for selecting the best design approaches about 1.65 times the size of one classical comparison as _n_ grows. In the cases computed this ratio decreases when the good-enough set is a larger fraction of the designs. It is about 1.63 for the top 5 percent of 1000 designs and 1.38 for the top half. These ratios measure gains per comparison under the exact oracle model. Their computational significance depends on how the comparisons are implemented.

\begin{tabular}{cccccc}
 & blind & classical & quantum & classical & size \\
_r_ & pick & _q_=1 & _q_=1 & _q_=2 & \(s_\mathrm{eq}^Q(7,r)\) \\
1 & 0.1429 & 0.2857 & 0.4164 & 0.4286 & 2.9145 \\
2 & 0.2857 & 0.5238 & 0.6769 & 0.7143 & 2.7826 \\
3 & 0.4286 & 0.7143 & 0.8314 & 0.8857 & 2.6151 \\
4 & 0.5714 & 0.8571 & 0.9199 & 0.9714 & 2.4157 \\
5 & 0.7143 & 0.9524 & 0.9705 & 1 & 2.1953 \\
6 & 0.8571 & 1 & 1 & 1 & 2 \\
\end{tabular}

\begin{tabular}{cccccc}
 & good-enough & classical & quantum & classical & size \\
_r_ & fraction & _q_=1 & _q_=1 & _q_=2 & \(s_\mathrm{eq}^Q(1000,r)\) \\
1 & 0.1% & 0.0020 & 0.0033 & 0.0030 & 3.3000 \\
10 & 1% & 0.0199 & 0.0326 & 0.0297 & 3.2939 \\
50 & 5% & 0.0975 & 0.1544 & 0.1428 & 3.2655 \\
100 & 10% & 0.1901 & 0.2885 & 0.2712 & 3.2265 \\
200 & 20% & 0.3602 & 0.5038 & 0.4884 & 3.1364 \\
500 & 50% & 0.7503 & 0.8537 & 0.8754 & 2.7698 \\
\end{tabular}

\begin{tabular}{ccc}
Good-enough fraction & Classical & Quantum \\
1% & 0.019900 & 0.032583 \\
5% & 0.097500 & 0.154311 \\
10% & 0.190000 & 0.288343 \\
20% & 0.360000 & 0.503566 \\
50% & 0.750000 & 0.853553 \\
\end{tabular}

2: Selection performance for seven designs.

3: Selection performance for 1000 designs.

4: Fixed-fraction limits.

