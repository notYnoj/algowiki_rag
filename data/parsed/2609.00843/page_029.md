For uniform inputs, the largest advantage over the baselines occurred at _R_=2<sup>9</sup>, where the maximum speedup was 3.70 at \(n=9\times 10^6\). For _R_=2<sup>9</sup> and 2<sup>12</sup>, the ratio exceeded 1 at every measured input size. As the range increased, however, the ratio for small inputs decreased: it fell below 1 at \(n=10^6,2\times 10^6\) for _R_=2<sup>15</sup> and at \(n\le 5\times 10^6\) for _R_=2<sup>16</sup>. This tendency became more pronounced at _R_=2<sup>17</sup>, where a baseline was faster for \(n\le 2\times 10^7\), whereas RT-CDF was fastest for \(n\ge 3\times 10^7\). At _R_=2<sup>18</sup>, the ratio was below 1 for every measured input size, with no indication that RT-CDF would overtake the baselines as the input size increased.

R = 27
R = 28
4
3
2
Speedup
1
0
106
107
108
109
Input size n
(a) Ranges requiring one CUB pass (R 28)
R = 29
R = 212
4
R = 215
R = 216
3
2
Speedup
1
0
106
107
108
109
Input size n
(b) Representative ranges requiring two CUB passes (29 1 R 216)
R = 217
R = 218
4
3
2
Speedup
1
0
106
107
108
109
Input size n
(c) Ranges requiring three CUB passes (217 1 R 218)
Figure 11: RT-CDF speedup over the fastest baseline for uniformly distributed inputs

Figure 11: RT-CDF speedup over the fastest baseline for uniformly distributed inputs

