For all-equal inputs, the maximum speedup observed in the entire experiment, 4.39, occurred at _R_=2<sup>9</sup> and _n_=10<sup>6</sup>. For each representative two-pass range shown in the figure--_R_=2<sup>9</sup>,2<sup>12</sup>,2<sup>15</sup>,2<sup>16</sup>--the ratio exceeded 1 at every measured input size. This differs from the uniform and normal results for large ranges, in which the ratio fell below 1 for small inputs. At _R_=2<sup>17</sup>, a baseline was faster for \(n\le 10^7\), whereas RT-CDF was fastest for \(n\ge 2\times 10^7\). At _R_=2<sup>18</sup>, RT-CDF and CUB were nearly tied at _n_=10<sup>6</sup>, but the ratio was at most 1 for every measured input size.

For all three input distributions, the largest advantage of RT-CDF over the baselines was obtained at _R_=2<sup>9</sup>. The ratio generally decreased as the range grew, and a baseline was particularly likely to be superior for small inputs with a large range. At _R_=2<sup>17</sup>, all three distributions exhibited a boundary<tbc>

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
Figure 13: RT-CDF speedup over the fastest baseline for all-equal inputs

