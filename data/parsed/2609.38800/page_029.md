## References

\begin{tabular}{cccccc}
Depth & External method & Coverage & Baseline ratio \[IQR\] & Matched local & Local - baseline \\
5 & Fixed angle & 13/36 & 0.916 \[0.903, 0.940\] & 0.893 & -0.024 \\
 & Fixed angle + opt. & 14/36 & 0.935 \[0.927, 0.944\] & 0.893 & -0.038 \\
 & Fourier & 26/36 & 0.828 \[0.782, 0.878\] & 0.893 & +0.050 \\
 & Interpolation & 31/36 & 0.932 \[0.912, 0.949\] & 0.891 & -0.041 \\
 & Recursive transfer + angle opt. & 2/36<sup>†</sup> & 0.917 \[0.909, 0.924\] & 0.799 & -0.117 \\
 & Recursive transfer + opt. & 2/36<sup>†</sup> & 0.882 \[0.869, 0.895\] & 0.799 & -0.083 \\
 & TQA & 30/36 & 0.876 \[0.846, 0.893\] & 0.889 & +0.021 \\
 & TQA + opt. & 24/36 & 0.918 \[0.899, 0.929\] & 0.883 & -0.034 \\
 & Transfer strategy & 28/36 & 0.909 \[0.894, 0.932\] & 0.885 & -0.030 \\
7 & Fixed angle & 6/36 & 0.949 \[0.927, 0.960\] & 0.898 & -0.049 \\
 & Fixed angle + opt. & 6/36 & 0.963 \[0.958, 0.965\] & 0.898 & -0.065 \\
 & Fourier & 26/36 & 0.862 \[0.788, 0.908\] & 0.894 & +0.028 \\
 & Interpolation & 31/36 & 0.954 \[0.940, 0.966\] & 0.890 & -0.067 \\
 & Recursive transfer + angle opt. & 2/36<sup>†</sup> & 0.941 \[0.938, 0.945\] & 0.800 & -0.141 \\
 & Recursive transfer + opt. & 2/36<sup>†</sup> & 0.906 \[0.894, 0.917\] & 0.800 & -0.106 \\
 & TQA & 31/36 & 0.906 \[0.876, 0.920\] & 0.890 & -0.012 \\
 & TQA + opt. & 24/36 & 0.941 \[0.928, 0.946\] & 0.883 & -0.060 \\
 & Transfer strategy & 31/36 & 0.935 \[0.916, 0.954\] & 0.890 & -0.050 \\
\end{tabular}

9: External exact-statevector QAOA parameter-setting baselines on their available instance support (continued). Baseline entries report median \[interquartile range\]. For every row, the local median and paired difference are recomputed using only the instances available for that baseline; positive differences favor the best local finite-shot optimizer. Different rows have different support and do not constitute a common controlled ranking.

<sup>†</sup>Sparse support (_n\<_5); interpret the median descriptively only.

