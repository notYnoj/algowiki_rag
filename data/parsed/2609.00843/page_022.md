For all three input distributions, RT-CDF was the fastest method from _R_=2<sup>7</sup> through 2<sup>17</sup>, whereas CUB was fastest at _R_=2<sup>18</sup>. For \(R\le 2^{14}\), the RT-CDF execution times differed little across the input distributions, and all three distributions exhibited the same tendency of increasing execution time with the range size. Even at _R_=2<sup>17</sup>, RT-CDF was 1.15, 1.19, and 1.22 times faster than the fastest baseline for the uniform, normal, and all-equal inputs, respectively. At _R_=2<sup>18</sup>, its speedup ratios relative to the fastest baseline fell to 0.62, 0.62, and 0.64, respectively, and the advantage of RT-CDF disappeared independently of the input distribution. The largest ratios in these tables occurred at _R_=2<sup>10</sup> for the uniform and all-equal inputs and at _R_=2<sup>9</sup> for the normal input, and were approximately 2.65-2.67. The implementation based on Kolonias et al. required approximately 267-273ms for every range under the all-equal input, much longer than for the other two distributions. This is presumably because its threads are assigned by value and almost all output generation is concentrated in the single thread assigned to value zero. CUB was the fastest baseline in every one of these 36 conditions, and RT-CDF outperformed CUB and all other baselines in 33 of the 36. The only conditions in which RT-CDF was not the fastest were the three input distributions at _R_=2<sup>18</sup>. These results show that, for _n_=10<sup>8</sup>, RT-CDF performance depends primarily on the range size and only weakly on the input distribution.

We next fix the range and compare execution time as a function of the input size _n_. As a representative range for which RT-CDF performs well over a broad interval of input sizes, we first consider _R_=2<sup>10</sup>. Figures 2, 3, and 4 show the uniform, normal, and all-equal results, respectively.

\begin{tabular}{ccccccc}
_R_ & RT-CDF \[ms\] & CUB \[ms\] & RefHP \[ms\] & Kolonias et al. \[ms\] & Best baseline & Best baseline/RT-CDF \\
2<sup>7</sup> & **0.956** & 1.430 & 1.831 & 267.40 & CUB & 1.50 \\
2<sup>8</sup> & **0.961** & 1.430 & 1.852 & 267.41 & CUB & 1.49 \\
2<sup>9</sup> & **0.969** & 2.562 & 3.042 & 267.38 & CUB & 2.64 \\
2<sup>10</sup> & **0.974** & 2.576 & 3.042 & 267.38 & CUB & 2.65 \\
2<sup>11</sup> & **0.981** & 2.576 & 4.093 & 266.65 & CUB & 2.63 \\
2<sup>12</sup> & **0.994** & 2.507 & 4.450 & 267.36 & CUB & 2.52 \\
2<sup>13</sup> & **1.018** & 2.509 & 6.839 & 267.39 & CUB & 2.46 \\
2<sup>14</sup> & **1.029** & 2.509 & 7.056 & 267.89 & CUB & 2.44 \\
2<sup>15</sup> & **1.200** & 2.509 & 11.722 & 267.74 & CUB & 2.09 \\
2<sup>16</sup> & **1.688** & 2.506 & 11.656 & 267.91 & CUB & 1.48 \\
2<sup>17</sup> & **2.767** & 3.387 & 13.259 & 270.19 & CUB & 1.22 \\
2<sup>18</sup> & 5.333 & **3.404** & 15.744 & 273.06 & CUB & 0.64 \\
\end{tabular}

11: Execution times and speedups for _n_=10<sup>8</sup> (all-equal input)

