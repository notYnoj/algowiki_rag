<tbc>the baselines changes with the input size at _R_=2<sup>17</sup>. At _R_=2<sup>18</sup>, RT-CDF was not fastest for any of the four representative input sizes. For uniform and normal inputs, RefHP or CUB was fastest depending on the input size, and CUB was fastest in all four all-equal conditions. Thus, these winner maps show the same pattern as the execution-time and speedup results: RT-CDF retains an advantage for large inputs at _R_=2<sup>17</sup> but loses it at _R_=2<sup>18</sup>. Among all 144 combinations of representative input size and range, RT-CDF was fastest in 119, RefHP in 13, and CUB in 12; the implementation based on Kolonias et al. was never fastest.

Finally, we compare the absolute execution times of all methods at representative input sizes. For _n_=10<sup>6</sup>,10<sup>7</sup>,10<sup>8</sup>,10<sup>9</sup>, s 15, 16, and 17 show the execution times of RT-CDF, CUB, RefHP, and the implementation based on Kolonias et al. over every evaluated range for uniform, normal, and all- equal inputs, respectively. The smallest execution time in each condition is shown in bold. These tables make it possible to examine not only which method is fastest, but also the absolute magnitude of the performance differences.

\begin{tabular}{ccccc}
_R_ & RT-CDF \[ms\] & CUB \[ms\] & RefHP \[ms\] & Kolonias et al. \[ms\] \\
\multicolumn{5}{c}{_n_=10<sup>6</sup>} \\
2<sup>7</sup> & **0.01772** & 0.02296 & 0.04203 & 0.7402 \\
2<sup>8</sup> & **0.01998** & 0.02553 & 0.04174 & 0.7446 \\
2<sup>9</sup> & **0.02095** & 0.1034 & 0.04301 & 0.3795 \\
2<sup>10</sup> & **0.02190** & 0.1028 & 0.04327 & 0.1989 \\
2<sup>11</sup> & **0.02700** & 0.1027 & 0.04134 & 0.1128 \\
2<sup>12</sup> & **0.03053** & 0.1025 & 0.04337 & 0.07029 \\
2<sup>13</sup> & 0.04580 & 0.1042 & **0.04311** & 0.06548 \\
2<sup>14</sup> & 0.05649 & 0.1053 & **0.04325** & 0.09759 \\
2<sup>15</sup> & 0.06625 & 0.1056 & **0.04215** & 0.1665 \\
2<sup>16</sup> & 0.08320 & 0.1067 & **0.04139** & 0.2489 \\
2<sup>17</sup> & 0.1261 & 0.1217 & **0.04245** & 0.4601 \\
2<sup>18</sup> & 0.2464 & 0.1172 & **0.1004** & 0.9149 \\
\multicolumn{5}{c}{_n_=10<sup>7</sup>} \\
2<sup>7</sup> & **0.07101** & 0.1641 & 0.2198 & 7.327 \\
2<sup>8</sup> & **0.07424** & 0.1694 & 0.2218 & 7.345 \\
2<sup>9</sup> & **0.07891** & 0.2742 & 0.2263 & 3.694 \\
2<sup>10</sup> & **0.08275** & 0.2737 & 0.2254 & 1.871 \\
2<sup>11</sup> & **0.08786** & 0.2738 & 0.2278 & 0.9625 \\
2<sup>12</sup> & **0.09407** & 0.2735 & 0.2284 & 0.5096 \\
2<sup>13</sup> & **0.1105** & 0.2766 & 0.2278 & 0.3295 \\
2<sup>14</sup> & **0.1245** & 0.2784 & 0.2274 & 0.3526 \\
2<sup>15</sup> & **0.1571** & 0.2822 & 0.2289 & 0.4213 \\
2<sup>16</sup> & **0.2172** & 0.2776 & 0.7029 & 0.5276 \\
2<sup>17</sup> & 0.3335 & 0.3227 & **0.2309** & 0.7531 \\
\multicolumn{5}{c}{Continued on the next page} \\
\end{tabular}

15: Execution times of the methods at representative input sizes (uniform distribution)

