Matrices are generated on the GPU. Times are wall-clock times from submission to completion of `gemm`, with the workspace allocated by a previous call; we report the best of 3-7 repetitions (medians differ by less than 1%). Emulated FP64 rates count 2_mnk_ flops for DGEMM and 8_mnk_ for ZGEMM. Energy is read from the board energy counter of the `xe` driver over runs of at least 2s.

We use the following test matrices: U\[-1,1) (as in \[20\]); \((\mathcal{U}(0,1)-\frac{1}{2})\mathrm{exp}(\phi\mathcal{N}(0,1))\) with \(\phi\in\{0.5,1,2,4\}\) (as in \[17\]); sin/cos matrices; and two adversarial families described in Section 8.3. Accuracy is measured against a double-double GEMM computed on the GPU (error ≈2<sup>-100</sup> relative to |_A_||_B_|) on \(512\times 512\) outputs. We report the maximum error in ulps of the exact result, the fraction of correctly rounded entries, the componentwise error \(\mathrm{max}|\tilde{c}_{ij}-c_{ij}|/(|A||B|)_{ij}\) and the normwise relative error. All experiments can be reproduced (see  and data availability).

## 8 Results

### 8.1 Correctness

The test program (108 tests) checks the bound of Eq. (7) element-wise against the double-double reference for all combinations of `N/T/C`, \(\alpha\) and \(\beta\), leading dimensions larger than the row count, _s_=2..24, _k_ from 1 to 300000, and tiling under a workspace limit of 4-8MB; tiled results are bitwise identical to untiled ones. Two unit tests follow \[20\]. The split kernel is compared with `\_int128` arithmetic on 2.2 million residues, including subnormals and signed zeros, and the CRT kernel reconstructs 8192 random exact integers with \(|\hat{c}|\le M/4\) (including \(|\hat{c}|=M/4\)) for every _s_=2..24. Both tests report zero mismatches. Integer inputs give bitwise exact results, and Inf/NaN inputs propagate NaN to the affected row or column.

### 8.2 Accuracy

Figure 2 and  6 show how the error depends on _s_. The componentwise error decreases by a factor of about 2<sup>4</sup> per modulus, as predicted by _t_≈(log<sub>2</sub>_M_-log<sub>2</sub>_k)/_2. The componentwise accuracy of native DGEMM is reached at _s_=14-15 for well-scaled data and at _s_=17 for \(\phi=2\) ( 7). Beyond this point the result becomes correctly rounded. For U\[-1,1), all entries are correctly rounded from _s_=15-16 on, whereas native DGEMM rounds only 1.7-3% (oneMKL on the GPU) and 2-13% (MKL on the CPU) of the entries correctly, with maximum errors of 10<sup>5</sup>-10<sup>7</sup> ulps caused by cancellation. For inputs with wide exponent ranges (\(\phi=0.5\)-2 and sin/cos), correct rounding requires _t\>_62 and thus the extended-width path with _s_=19-23.

### 8.3 Worst cases

8 collects inputs designed to stress the method.

_Boundary of the CRT range._ If all entries equal 1-2<sup>-53</sup>, they round to \(\hat{a}=2^t\) and give \(|\hat{c}|=k2^{2t}=M/4\), the limit of Eq. (4). The results are exact for all _s_.

_Spike._ One element per row of _A_ is 2<sup>40</sup> times larger than the others. The shared row exponent then leaves the remaining elements only _t_-40 bits, and at _s_=16 the componentwise error is 10<sup>-10</sup>, four orders of magnitude worse than DGEMM. Increasing _s_ to 20 restores DGEMM- level accuracy, and _s_=24 gives correct rounding. This is the fundamental limitation of all shared-exponent schemes.

_Cancellation._ With _A_=\[_XX_\] and _B_=\[_Y_;-_Y_+2<sup>-30</sup>_Z_\] we obtain |_C_|≈2<sup>-30</sup>|_A_||_B_|. Native DGEMM loses 30 bits (normwise relative error \(2\times 10^{-6}\) on the GPU and \(7\times 10^{-7}\) on the CPU). Ozaki scheme II with \(s\ge 20\), in contrast, represents the inputs exactly, computes \(\hat{c}\) exactly and rounds only once: the normwise error is \(9\times 10^{-16}\) at _s_=20, and the result is correctly rounded at _s_=24.

