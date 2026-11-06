<tbc>LPIPS increases from 0.08 to 0.11, and rec.FID rises from 0.65 to 1.02. We set \(\lambda\) to 2.5 based on experimental experience.

• **Support Factor** _s_: As stated in Eq. 2 of the main paper, _s_ controls the effective rendering support of each Gaussian. Performance degrades significantly when _s_=1, but stabilizes for \(s\ge 3\). This aligns with the 3\(\sigma\) rule, _i.e._, 99.7% of the mass of a 2D Gaussian lies within three standard deviations from the mean. To ensure full coverage, we set _s_=5 in all experiments.<tbc>

• **Minimal Region Size** _s<sub>min</sub>_: We set _s<sub>min</sub>_ in the calibration algorithm to match its value in the initialization algorithm, where _s<sub>min</sub>_ determines the minimum width or height of each region. We observe that increasing _s<sub>min</sub>_ from 4 to 16 results in negligible performance degradation. This is expected because, with 128 tokens representing a 256\(\times\)256 image, the average spatial extent per token is approximately 22\(\times\)22 pixels. Consequently, most of the segmented regions naturally have a width or height greater than or equal to 16, making the choice of _s<sub>min</sub>_ within this range largely inconsequential for the final tokenization.

## F Training/Inference Efficiency of GPSToken Generators

We provide comprehensive computational benchmarks comparing the GPSToken generator with the SiT-XL/2 baseline in both training and inference, as shown in  8. At 1M iterations, GPSToken achieves a significantly lower FID score (7.61 vs. 14.50), with 42% less training time (256h vs. 439h), 73% higher training throughput (1.09 vs. 0.63 iters/s), and 35% lower VRAM consumption (41,498 MB vs. 63,684 MB). During inference, although VRAM usage increases slightly (9,636 MB vs. 9,126 MB), our method nearly doubles the throughput (0.129 vs. 0.067 samples/s), reducing latency by approximately half.

These efficiency gains stem from two key design choices: (i) GPSToken reduces the number of effective tokens, lowering computational and memory overhead; (ii) the two-stage generation framework simplifies the learning objective and stabilizes optimization, enabling faster convergence to higher- quality solutions. Overall, GPSToken not only improves generation quality but also substantially reduces training cost and inference latency.

\begin{tabular}{ccccccc}
\multicolumn{2}{c}{**Hyper-parameter**} & PSNR & SSIM & LPIPS & rec. FID & FID \\
\multirow{2}{*}{\(\lambda\)} & 0 & 23.52 & 0.638 & 0.110 & 1.02 & 2.59 \\
 & 5 & 24.06 & 0.652 & 0.083 & 0.68 & 2.23 \\
\multirow{2}{*}{_s_} & 1 & 17.55 & 0.439 & 0.344 & 160 & 165 \\
 & 3 & 24.07 & 0.657 & 0.080 & 0.66 & 2.18 \\
\multirow{2}{*}{_s_min} & 7 & 24.06 & 0.658 & 0.080 & 0.66 & 2.16 \\
 & 8 & 24.05 & 0.656 & 0.080 & 0.66 & 2.18 \\
\multirow{2}{*}{_s_min} & 16 & 24.03 & 0.657 & 0.081 & 0.66 & 2.19 \\
\multicolumn{2}{c}{**ours (**\(\lambda=2.5,s=5,s_\text{\textbf{min}}=4\)**)**} & 24.06 & 0.657 & 0.080 & 0.65 & 2.18 \\
\end{tabular}

\begin{tabular}{cccccccc}
**Method** & **Metric** & **500K** & **1000K** & **T-Mem** & **T-Thpt** & **I-Mem** & **I-Thpt** \\
\multirow{2}{*}{Baseline} & FID & 19.07 & 14.50 & \multirow{2}{*}{63684} & \multirow{2}{*}{0.63} & \multirow{2}{*}{9126} & \multirow{2}{*}{0.067} \\
 & Time (h) & 219 & 439 & & & & \\
\multirow{2}{*}{Ours} & FID & 9.57 & 7.61 & \multirow{2}{*}{41498} & \multirow{2}{*}{1.09} & \multirow{2}{*}{9636} & \multirow{2}{*}{0.129} \\
 & Time (h) & 128 & 256 & & & & \\
\end{tabular}

7: Hyper-parameter selection on \(\lambda\), _s_, and _s_min.

8: Training and Inference Efficiency Comparison between SiT-XL/2 Baseline and GPSToken generator on ImageNet 256\(\times\)256 with A100 GPU.

**Notes:** T-Mem: Training Memory (MB), T-Thpt: Training Throughput (iters/s),<br>
I-Mem: Inference Memory (MB), I-Thpt: Inference Throughput (samples/s)

