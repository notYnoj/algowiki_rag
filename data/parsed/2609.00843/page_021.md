## 4.3 Performance Evaluation

We first fix the input size at _n_=10<sup>8</sup>. s 9, 10, and 11 show execution times and speedup ratios for the uniform, normal, and all-equal inputs, respectively. Here, "Best baseline" denotes the fastest execution time among CUB, RefHP, and the implementation based on Kolonias et al. The speedup ratio is the execution time of the fastest baseline divided by the execution time of RT-CDF. Consequently, a ratio greater than 1 means that RT-CDF is faster than every baseline.

\begin{tabular}{ccccccc}
_R_ & RT-CDF \[ms\] & CUB \[ms\] & RefHP \[ms\] & Kolonias et al. \[ms\] & Best baseline & Best baseline/RT-CDF \\
2<sup>7</sup> & **0.956** & 1.446 & 2.833 & 73.34 & CUB & 1.51 \\
2<sup>8</sup> & **0.961** & 1.444 & 2.849 & 73.52 & CUB & 1.50 \\
2<sup>9</sup> & **0.968** & 2.561 & 4.088 & 37.00 & CUB & 2.65 \\
2<sup>10</sup> & **0.971** & 2.579 & 4.090 & 18.76 & CUB & 2.66 \\
2<sup>11</sup> & **0.982** & 2.584 & 4.091 & 9.651 & CUB & 2.63 \\
2<sup>12</sup> & **0.993** & 2.579 & 4.089 & 5.085 & CUB & 2.60 \\
2<sup>13</sup> & **1.008** & 2.565 & 4.089 & 3.135 & CUB & 2.54 \\
2<sup>14</sup> & **1.012** & 2.597 & 4.084 & 3.517 & CUB & 2.57 \\
2<sup>15</sup> & **1.187** & 2.610 & 4.078 & 3.982 & CUB & 2.20 \\
2<sup>16</sup> & **1.714** & 2.606 & 4.078 & 4.202 & CUB & 1.52 \\
2<sup>17</sup> & **2.975** & 3.414 & 3.953 & 5.798 & CUB & 1.15 \\
2<sup>18</sup> & 5.528 & **3.421** & 3.994 & 8.642 & CUB & 0.62 \\
\end{tabular}

\begin{tabular}{ccccccc}
_R_ & RT-CDF \[ms\] & CUB \[ms\] & RefHP \[ms\] & Kolonias et al. \[ms\] & Best baseline & Best baseline/RT-CDF \\
2<sup>7</sup> & **0.956** & 1.435 & 2.953 & 69.75 & CUB & 1.50 \\
2<sup>8</sup> & **0.961** & 1.442 & 2.850 & 73.03 & CUB & 1.50 \\
2<sup>9</sup> & **0.968** & 2.582 & 4.080 & 36.77 & CUB & 2.67 \\
2<sup>10</sup> & **0.973** & 2.585 & 4.078 & 35.31 & CUB & 2.66 \\
2<sup>11</sup> & **0.980** & 2.578 & 4.091 & 25.43 & CUB & 2.63 \\
2<sup>12</sup> & **0.992** & 2.578 & 4.094 & 14.48 & CUB & 2.60 \\
2<sup>13</sup> & **1.007** & 2.580 & 4.096 & 7.738 & CUB & 2.56 \\
2<sup>14</sup> & **1.012** & 2.587 & 4.089 & 4.803 & CUB & 2.56 \\
2<sup>15</sup> & **1.186** & 2.590 & 4.089 & 4.293 & CUB & 2.18 \\
2<sup>16</sup> & **1.707** & 2.607 & 4.078 & 4.274 & CUB & 1.53 \\
2<sup>17</sup> & **2.881** & 3.429 & 3.983 & 5.951 & CUB & 1.19 \\
2<sup>18</sup> & 5.520 & **3.419** & 3.990 & 8.690 & CUB & 0.62 \\
\end{tabular}

9: Execution times and speedups for _n_=10<sup>8</sup> (uniform distribution)

10: Execution times and speedups for _n_=10<sup>8</sup> (normal distribution)

