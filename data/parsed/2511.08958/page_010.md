<tbc>score between the dense and sparse implementations and check the LCIS padding equality. All 15,641 test cases (14,641 exhaustive and 1,000 randomized) passed these checks. The validation log and test seeds are included. These finite tests check the implementation; the preceding proofs establish general correctness.

## 7.2. Measurement protocol

Inputs are independently uniform integer sequences over \(\{0,\dots,\sigma-1\}\), with _n=m=N_. Thus \(\mathbb{E}[M]=N^2/\sigma\). The density series fixes _N_=600 and varies the alphabet size; the scaling series sets \(\sigma=N\). Each configuration uses three independently seeded input pairs and three timed repetitions per pair and algorithm. Each algorithm is warmed up once before the series, and execution order alternates. Garbage collection runs before each timed call and remains enabled. Input generation and validation are outside the timed region. The clock is Python’s `perf\_counter\_ns`.

For each algorithm we first take the median of three repetitions on each input pair, then the median of those three medians.  1 reports these values, the median match count, and the ratio of aggregate dense time to aggregate sparse time. The ratio is calculated before rounding; it is not the median of individual speedups. All 180 raw timings, input-generation seeds, and the execution environment are included in the supplement. Each measured result was validated, and the two implementations agreed on optimum length for every benchmark input.

Measurements used CPython 3.12.14 on Windows 11 (build 26200), with an AMD Ryzen 7 5700X processor (8 cores, 16 logical processors) and approximately 32 GiB RAM. The algorithms execute sequentially in one Python process.

## 7.3. Observed tradeoff and limitations

Figure 2 plots the fixed-_N_ density measurements from  1 against their median match counts. The ordering of the measured runtimes switches between the tested configurations with _M_=1425 and

\begin{tabular}{ccccccc}
Series & _N_ & \(\sigma\) & _M_ & Dense (s) & Sparse (s) & Ratio \\
Density & 600 & 4 & 89895 & 0.1453 & 0.6788 & 0.21 \\
Density & 600 & 16 & 22410 & 0.0614 & 0.2016 & 0.30 \\
Density & 600 & 64 & 5597 & 0.0440 & 0.0586 & 0.75 \\
Density & 600 & 256 & 1425 & 0.0376 & 0.0178 & 2.11 \\
Density & 600 & 1024 & 340 & 0.0371 & 0.0042 & 8.84 \\
Density & 600 & 4096 & 86 & 0.0371 & 0.0014 & 26.32 \\
Scaling & 200 & 200 & 200 & 0.0040 & 0.0017 & 2.39 \\
Scaling & 400 & 400 & 429 & 0.0174 & 0.0052 & 3.37 \\
Scaling & 800 & 800 & 814 & 0.0685 & 0.0104 & 6.56 \\
Scaling & 1600 & 1600 & 1570 & 0.2688 & 0.0240 & 11.19 \\
\end{tabular}

1. Fresh end-to-end measurements. Ratio is dense time divided by sparse time; values below one favor the dense implementation.

