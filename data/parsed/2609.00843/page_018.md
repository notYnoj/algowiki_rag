As shown in Figure 1, the binary-search method was faster in 184 of the 240 conditions. Its advantage became more pronounced as the input size increased: for all 120 conditions with \(n\ge 5\times 10^7\), the binary-search method was faster regardless of the range size or input distribution. For small inputs and large ranges, by contrast, the prefix-maximum method was faster. This appears to be because a large range increases the number of tiles, making fixed overheads of the binary-search method-- including per-tile kernel launches and retrieval of tile populations before output generation--relatively large for small inputs. Our evaluation includes inputs of up to 10<sup>9</sup> elements and uses one common output-generation algorithm for all conditions. The binary-search method was consistently faster for large inputs, indicating that this design is suitable for RT-CDF evaluations that include large-scale inputs. Nevertheless, switching the output-generation method according to the input size and range could further improve RT-CDF under conditions in which binary search was slower. Such adaptive selection is a possible future improvement.

We next select the tile width _T_ for the binary-search method used in the main evaluation. Using the binary-search measurements from the preceding comparison of output-generation methods, we compared tile widths separately for each range size _R_. For each _R_, the comparison covered 20 conditions formed by 10 input sizes _n_ and two input distributions. For each condition, we define the normalized execution time of tile width _T_ as

\(r(T)=\frac{\text{execution time with}T}{\text{minimum execution time for that condition}}.\)

Thus, \(r(T)\ge 1\), and _r(T_)=1 means that _T_ is the fastest tile width under that condition. For each tile width, we computed the geometric mean of _r(T_) over the 20 conditions and compared tile widths using this value. A value closer to 1 means that the tile width performs closer to the fastest choice for each condition across the 20 combinations of input size and input distribution.  5 presents the results.

Based on  5, for each range size _R_ we selected the tile width _T_ with the smallest geometric mean of normalized execution time. The selected tile widths and corresponding numbers of tiles are shown in  6.

\begin{tabular}{ccccccccccccc}
 & \multicolumn{12}{c}{Tile width _T_} \\
Range size _R_ & 128 & 256 & 512 & 1,024 & 2,048 & 4,096 & 6,144 & 8,192 & 12,288 & 16,384 & 20,480 & 24,576 \\
2<sup>7</sup> & 1.000 & - & - & - & - & - & - & - & - & - & - & - \\
2<sup>8</sup> & 1.134 & 1.000 & - & - & - & - & - & - & - & - & - & - \\
2<sup>9</sup> & 1.306 & 1.102 & 1.000 & - & - & - & - & - & - & - & - & - \\
2<sup>10</sup> & 1.806 & 1.274 & 1.089 & 1.001 & - & - & - & - & - & - & - & - \\
2<sup>11</sup> & 2.758 & 1.759 & 1.268 & 1.078 & 1.001 & - & - & - & - & - & - & - \\
2<sup>12</sup> & - & 2.627 & 1.688 & 1.213 & 1.054 & 1.001 & - & - & - & - & - & - \\
2<sup>13</sup> & - & - & 2.420 & 1.555 & 1.129 & 1.013 & 1.030 & 1.017 & - & - & - & - \\
2<sup>14</sup> & - & - & - & 2.310 & 1.480 & 1.112 & 1.052 & 1.029 & 1.119 & 1.216 & - & - \\
2<sup>15</sup> & - & - & - & - & 1.951 & 1.278 & 1.127 & 1.010 & 1.057 & 1.297 & 1.323 & 1.376 \\
2<sup>16</sup> & - & - & - & - & - & 1.450 & 1.171 & 1.004 & 1.063 & 1.286 & 1.318 & 1.199 \\
2<sup>17</sup> & - & - & - & - & - & - & - & 1.013 & 1.012 & 1.285 & 1.219 & 1.136 \\
2<sup>18</sup> & - & - & - & - & - & - & - & - & - & 1.202 & 1.123 & 1.001 \\
\end{tabular}

5: Geometric mean of normalized execution time for each tile width

