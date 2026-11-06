For _R_=2<sup>18</sup>, RT-CDF was not the fastest method at any of the 28 measured input sizes for any distribution. For uniform and normal inputs, the fastest method alternated between CUB and RefHP depending on the input size, but both outperformed RT-CDF throughout the measurement range. For all- equal inputs, RT-CDF and CUB were nearly tied at _n_=10<sup>6</sup>, but CUB was faster thereafter. Moreover, increasing the input size did not produce a trend in which RT-CDF caught up with and overtook the baselines; the large-input advantage observed at _R_=2<sup>17</sup> was lost at _R_=2<sup>18</sup>.

In summary, RT-CDF was superior independently of the input size and distribution at _R_=2<sup>10</sup>; its relative performance changed with the input size at _R_=2<sup>17</sup>; and the baselines were superior throughout the measurement range at _R_=2<sup>18</sup>. The performance boundary of RT-CDF therefore appears clearly between _R_=2<sup>17</sup> and _R_=2<sup>18</sup>.

We next present the speedup ratio defined as the execution time of the fastest baseline divided by that of RT-CDF for each condition. A ratio greater than 1 means that RT-CDF is fastest; a ratio below 1 means that at least one baseline is faster. In the version of CUB `DeviceRadixSort` used in this experimental environment, 32-bit keys are processed using Onesweep, with up to eight bits processed per pass. We refer to each such processing step as a pass. Because CUB was instructed to sort only the low- order log<sub>2</sub>_R_ bits required by the range, it requires one pass for \(R\le 2^8\), two passes for \(2^9\le R\le 2^{16}\), and three passes for \(2^{17}\le R\le 2^{18}\). To account for these differences, we divide the speedup results into these three ranges. For the two-pass range, we show representative results for _R_=2<sup>9</sup>,2<sup>12</sup>,2<sup>15</sup>,2<sup>16</sup>. Figures 11, 12, and 13 show the uniform, normal, and all-equal results, respectively. Because the numerator is the fastest baseline for each condition, changes in the curves reflect not only changes in the performance gap relative to RT-CDF but also changes in which baseline is fastest.

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

Figure 10: Execution time for all-equal inputs (_R_=2<sup>18</sup>)

