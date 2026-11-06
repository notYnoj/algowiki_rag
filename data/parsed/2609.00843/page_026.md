At _R_=2<sup>17</sup>, unlike at _R_=2<sup>10</sup>, a baseline was faster for small inputs, whereas RT-CDF became the fastest method as the input size increased. For the uniform distribution, RefHP was fastest for \(n\le 10^7\), CUB was fastest at \(n=2\times 10^7\), and RT-CDF was fastest for \(n\ge 3\times 10^7\). For the normal distribution, RefHP was fastest at _n_=10<sup>6</sup>, CUB for \(2\times 10^6\le n\le 10^7\), and RT-CDF for \(n\ge 2\times 10^7\). For all-equal inputs, CUB was fastest for \(n\le 10^7\), whereas RT-CDF was fastest for \(n\ge 2\times 10^7\). Across the three distributions, RT-CDF was fastest in 53 of the 84 conditions. Thus, _R_=2<sup>17</sup> is a boundary regime in which fixed overheads favor the baselines for small inputs, but the advantage of RT-CDF emerges once the input is sufficiently large.

Finally, we examine the largest evaluated range, _R_=2<sup>18</sup>. Figures 8, 9, and 10 show execution time as a function of _n_ for the uniform, normal, and all-equal inputs, respectively.

103
RT-CDF
CUB
RefHP
Kolonias et al.
102
Execution time [ms]
101
100
10-1
106
107
108
109
Input size n

Figure 7: Execution time for all-equal inputs (_R_=2<sup>17</sup>)

