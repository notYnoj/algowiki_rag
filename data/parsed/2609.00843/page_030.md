For normal inputs, the largest advantage likewise occurred at _R_=2<sup>9</sup>, with a maximum speedup of 3.60 at \(n=9\times 10^6\). RT-CDF was fastest throughout the measured range for _R_=2<sup>9</sup> and 2<sup>12</sup>. The ratio fell below 1 at _n_=10<sup>6</sup> for _R_=2<sup>15</sup> and at \(n\le 5\times 10^6\) for _R_=2<sup>16</sup>, but RT-CDF was fastest for larger inputs. At _R_=2<sup>17</sup>, a baseline was faster for \(n\le 10^7\), whereas RT-CDF was fastest for \(n\ge 2\times 10^7\). As for the uniform distribution, the ratio was below 1 for every input size at _R_=2<sup>18</sup>.

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
Figure 12: RT-CDF speedup over the fastest baseline for normally distributed inputs

