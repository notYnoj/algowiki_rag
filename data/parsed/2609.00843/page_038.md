<tbc>As s 15-17 show, when RT-CDF outperforms the baselines on large inputs, the absolute reduction in execution time is also substantial. For example, for a uniform input with _R_=2<sup>15</sup> and _n_=10<sup>9</sup>, RT- CDF runs in 11.88ms, reducing the execution time by approximately 13.12ms relative to the fastest baseline, CUB, at 25.00ms. For the same range and input size under the normal distribution, RT-CDF runs in 12.14ms and CUB in 24.87ms, a difference of approximately 12.73ms.

For small inputs, by contrast, even a large speedup ratio corresponds to a small absolute difference. For an all-equal input with _R_=2<sup>9</sup> and _n_=10<sup>6</sup>, the speedup is approximately 4.39, but RT-CDF runs in 0.02140ms and the fastest baseline, CUB, in 0.09403ms, a difference of approximately 0.073ms. Both the ratio and the absolute execution time should therefore be considered.

As the range approaches the performance boundary, the absolute advantage on large inputs also narrows. For a uniform input with _R_=2<sup>17</sup> and _n_=10<sup>9</sup>, RT-CDF runs in 28.55ms and the fastest baseline, RefHP, in 29.75ms, an advantage of approximately 1.20ms. At _R_=2<sup>18</sup> and _n_=10<sup>9</sup>, RT-CDF takes 53.14ms, whereas RefHP takes 29.75ms, making RT-CDF approximately 23.39ms slower. This again demonstrates that the performance boundary occurs between _R_=2<sup>17</sup> and _R_=2<sup>18</sup>.

## 4.4 Execution-Time Breakdown and Performance Limitations

To investigate why RT-CDF performance changes with the range and input distribution, we used the additional measurements described in Section 4.2 to break down the time spent in each processing stage. Figure 14 shows the results with the input size fixed at _n_=10<sup>8</sup>. The figure presents the execution times of two processing stages: histogram construction and output generation. We also measured local<tbc>

\begin{tabular}{ccccc}
\multicolumn{5}{c}{ 17 (continued)} \\
_R_ & RT-CDF \[ms\] & CUB \[ms\] & RefHP \[ms\] & Kolonias et al. \[ms\] \\
2<sup>14</sup> & **1.029** & 2.509 & 7.056 & 267.9 \\
2<sup>15</sup> & **1.200** & 2.509 & 11.72 & 267.7 \\
2<sup>16</sup> & **1.688** & 2.506 & 11.66 & 267.9 \\
2<sup>17</sup> & **2.767** & 3.387 & 13.26 & 270.2 \\
2<sup>18</sup> & 5.333 & **3.404** & 15.74 & 273.1 \\
\multicolumn{5}{c}{_n_=10<sup>9</sup>} \\
2<sup>7</sup> & **9.701** & 13.33 & 17.29 & - \\
2<sup>8</sup> & **9.731** & 13.33 & 17.29 & - \\
2<sup>9</sup> & **9.767** & 24.55 & 19.78 & - \\
2<sup>10</sup> & **9.830** & 24.55 & 21.87 & - \\
2<sup>11</sup> & **9.904** & 24.54 & 23.98 & - \\
2<sup>12</sup> & **9.969** & 24.54 & 21.88 & - \\
2<sup>13</sup> & **10.15** & 24.55 & 30.26 & - \\
2<sup>14</sup> & **10.22** & 23.87 & 46.93 & - \\
2<sup>15</sup> & **12.05** & 23.87 & 75.89 & - \\
2<sup>16</sup> & **17.06** & 23.87 & 79.74 & - \\
2<sup>17</sup> & **27.66** & 32.90 & 109.9 & - \\
2<sup>18</sup> & 51.75 & **32.90** & 109.6 & - \\
\end{tabular}

