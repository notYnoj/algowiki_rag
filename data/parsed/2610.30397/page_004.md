<tbc>based on the latency data collected during **Latency measurement** and examines the recovered bank masks from three perspectives: the latency distribution induced by the recovered partition, the expected **Group verification** pass rate as a function of threshold, and the contamination behavior under subsampling.

Figure 2 shows the latency histogram partitioned by the bank relation predicted by the final recovered bank masks in  I. Using the recovered addressing functions, each measured address pair is classified as either _same bank_ or _different bank_. The figure shows a clear separation, that is, most different-bank measurements concentrate in the lower- latency region, while the same-bank measurements are in higher latencies. The observation is consistent with the **Group verification** results in Section IV-A, which shows that thresholds located in the gap between the two distributions are expected to better separate same-bank from different-bank pairs.

As 10,000,000 latency samples are collected and the sample size is large, the resulting empirical distributions are used as a practical approximation of the memory behavior on Jetson Orin Nano. Based on these latency samples and the recovered bank masks, the expected **Group verification** pass rate is estimated at each threshold. Let _L_<sub>same</sub> and _L_<sub>diff</sub> denote the latency random variables for pairs predicted to be in the same bank and in different banks, respectively. For a threshold \(\tau\), define

\(p_\mathrm{same}(\tau)=\mathrm{Pr}[L_\mathrm{same}>\tau],p_\mathrm{diff}(\tau)=\mathrm{Pr}[L_\mathrm{diff}<\tau].\)

Under the natural independence approximation between the two sampled events in one verification trial, the expected pass probability is \(p_\mathrm{pass}(\tau)=p_\mathrm{same}(\tau)p_\mathrm{diff}(\tau)\). These probabilities are estimated empirically from the latency dataset obtained during **Latency measurement**. The expected pass rate is close to zero at very low and very high thresholds, and reaches a region near 1.0 in an intermediate threshold range. This follows from the two histogram tails. If \(\tau\) is too small, many different-bank pairs also exceed the threshold. If \(\tau\) is too large, many same-bank pairs fail to exceed it. Only thresholds near the separation region, approx. 500-570 clock cycles, can yield higher verification pass rate. The high pass rate range is therefore consistent with the threshold region in which the final bank masks achieve the highest measured **Group verification** performance.

## V. CONCLUSION

This paper presented an end-to-end software-only pipeline for reverse engineering and verifying DRAM address mapping functions on embedded systems, with a particular focus on modern LPDDR5 platforms. Our workflow combines<tbc>

<tbc>latency measurement, threshold sweep, Knock-Knock-based bank mask recovery, and two verification stages, including group verification and single function verification. Unlike prior approaches that return only a single inferred solution, our method records the recovered bank masks and their verification metrics for each candidate threshold. Overall, our results show that combining reverse engineering with rigorous software- based verification provides a practical and robust methodology for DRAM analysis on embedded ARM platforms especially LPDDR5 systems, where DRAM hierarchy information is incomplete.

## REFERENCES

\begin{tabular}{ccc}
**Platform** & **# Masks** & **Recovered bank masks** \\
Jetson Orin Nano & 7 & 0x214ccde00, 0x110ad4400, 0x950ccc00, 0x50eeac00, 0x21708c00, 0xd331200, 0x235d600 \\
Raspberry Pi 4B & 4 & 0x80000000, 0x4000, 0x2000, 0x1000 \\
\end{tabular}

TABLE I

RECOVERED BANK MASKS ON JETSON ORIN NANO AND RASPBERRY PI 4B

