<tbc>The main evaluation below fixes the tile width for each range size to the value in  6.

## 4.2 Baselines and Measurement Conditions for the Main Evaluation

This subsection describes the conditions of the main evaluation using the tile widths selected in Section 4.1. The experimental environment was the same as in the preliminary evaluation. We compared RT-CDF with CUB, RefHP, and an implementation based on the algorithm of Kolonias et al.  7 summarizes the methods. For CUB, we used the known range size _R_ to restrict the bit range processed by `DeviceRadixSort` to \([0,\lceil log_2R\rceil)\). Because this setting reduces the number of bits processed relative to sorting all 32 bits, it favors CUB and reflects the known-range problem setting of this study more appropriately than always processing a complete 32-bit integer. RefHP is a prior implementation that refines H-P sort for GPUs and is the closest baseline to RT-CDF. We also included an implementation based on Kolonias et al. because its output generation, which produces one interval per value, is closely related to RT-CDF.

\begin{tabular}{ccc}
Range size _R_ & Tile width _T_ & Number of tiles \(m=\lceil R/T\rceil\) \\
2<sup>7</sup> & 128 & 1 \\
2<sup>8</sup> & 256 & 1 \\
2<sup>9</sup> & 512 & 1 \\
2<sup>10</sup> & 1,024 & 1 \\
2<sup>11</sup> & 2,048 & 1 \\
2<sup>12</sup> & 4,096 & 1 \\
2<sup>13</sup> & 4,096 & 2 \\
2<sup>14</sup> & 8,192 & 2 \\
2<sup>15</sup> & 8,192 & 4 \\
2<sup>16</sup> & 8,192 & 8 \\
2<sup>17</sup> & 12,288 & 11 \\
2<sup>18</sup> & 24,576 & 11 \\
\end{tabular}

\begin{tabular}{ccc}
Method & Implementation & Role \\
CUB & `DeviceRadixSort` with `begin\_bit=0` and `end\_bit=`\(\lceil log_2R\rceil\) & Stable-sorting baseline using the known range \\
RefHP & Prior implementation refining H-P sort for GPUs & Unstable counting-sort-based baseline \\
Kolonias et al. & Comparison implementation developed in this study from the algorithm of Kolonias et al. & Baseline with a closely related output-generation method \\
RT-CDF & Implementation that partitions the range and generates output from each tile histogram and CDF & Proposed method \\
\end{tabular}

6: Tile widths and numbers of tiles used in the main evaluation

7: Baselines

