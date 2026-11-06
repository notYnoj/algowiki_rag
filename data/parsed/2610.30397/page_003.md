<tbc>must be checked. Group verification evaluates the correctness of the bank mask set as a whole, while Single function verification examines the correctness of each individual bank mask. For **Group verification**, 20,000 addresses from an allocated memory region are placed into an address pool. The bank ID of each address in the pool are computed and all the addresses are partitioned into 2#bank masks groups. In each group, an address _A_<sub>1</sub> is randomly selected. Another address _A_<sub>2</sub> from the same bank and an address _B_<sub>1</sub> from a different bank are then randomly chosen. The latency _t_<sub>1</sub> for accessing _A_<sub>1</sub> and _A_<sub>2</sub> is measured, and the latency _t_<sub>2</sub> for accessing _A_<sub>1</sub> and _B_<sub>1</sub> is also measured. If _t_<sub>1</sub>_\>_ threshold and _t_<sub>2</sub>_\<_ threshold, this iteration is counted as a pass; otherwise, it is counted as a failure. After repeating this process for many addresses and across all banks, the pass rate is computed to represent the reliability of the recovered bank masks. For **Single function verification**, the main purpose is to verify the correctness of each bank mask in the recovered bank mask set. If one correct bank mask is removed from the set, the pass rate is expected to be reduced to approximately half of that of **Group verification**. Each bank mask is removed in turn and the pass rate of the remaining bank masks will be measured.

## IV. RESULTS

### A. Recovered Bank Masks and Verification Results

I summarizes the final bank masks recovered on Jetson Orin Nano and Raspberry Pi 4B using the pipeline described in Section III. Our approach collects 10,000,000 latencies in **Latency measurement** and the latency represents CPU clock cycles. For **Bank mask computation**, the computation is conducted 200 times and each time, 100 different same-bank pairs are subsampled to form a difference matrix. Each row of the difference matrix is the XOR vectors of the two same-bank addresses.

Figure 1 report the **Group verification** pass rate for each threshold as a function of threshold for Jetson Orin Nano. For several bank mask sets, only a single threshold produces a result, so it appears a single point in Figure 1. The pass rate in the figure is the average value of the pass rates after executing **Group Verification** for 10 rounds. For Jetson Orin Nano, **Threshold sweep** produces five distinct recovered bank mask sets.

Among these candidates, bank mask set 5 consistently yields the highest group verification pass rate and reaches a region close to 1.0 over a broad threshold range. In contrast, the lower-dimensional candidate sets achieve substantially lower pass rates. This separation suggests that, on Jetson Orin Nano, bank mask set 5 is the candidate most consistent with the observed same-bank versus different-bank latency behavior.

A similar trend is observed on Raspberry Pi 4B. The **Threshold sweep** yields two candidate bank mask sets: bank mask set 1 contains `0x800000000, 0x2000, 0x1000`, bank mask set 2 contains `0x80000000, 0x4000, 0x2000, 0x1000`. Bank mask set 2, dominates the high<tbc>

<tbc>pass rate region and remains close to 1.0 across most of the selected threshold range, while bank mask set 1 yields negligible pass rate. Consequently, the **Group verification** results on both platforms show that the recovered bank masks produce bank partitions that agree with the measured latency behavior. Accordingly, the final bank masks reported in  I are the solutions most strongly supported by the verification data.

We further evaluate the bank masks of Jetson Orin Nano using **Single function verification**. The selected threshold is 550, where the pass rate of **Group verification** is 0.996907, the highest among the threshold range. The expected pass rate after removing one correct bank mask is 0.498454. For each of the bank masks, removing that mask yields a pass rate very close to the expectation. This behavior is consistent with the principle of **Single function verification**, which means each recovered addressing function contributes independently to the final bank partition, and removing any one of them causes a degradation in verification quality. This result provides additional evidence that the recovered bank masks on Jetson Orin Nano are stable and reliable.

### B. Threshold Sensitivity and Verification Analysis

A more detailed analysis on Jetson Orin Nano is performed to better understand threshold sensitivity. This analysis is<tbc>

Jetson Orin Nano: Pass Rate vs Threshold
1.0
0.8
Average pass rate over 10 rounds
0.6
Recovered bank-mask set
Bank mask set 1
Bank mask set 2
0.4
Bank mask set 3
Bank mask set 4
Bank mask set 5
0.2
0.0
500
520
540 Threshold
560
580

Latency histogram partitioned by predicted bank relation
106
Different bank Same bank
105
104
103
#Measurements
102
101
100
450
500
550
600
650
700
750
Time [CPU cycles]

Fig. 1. **Group verification** pass rate versus threshold on Jetson Orin Nano. Each curve corresponds to one recovered bank mask set, and different colors/markers denote different solutions.

Fig. 2. Latency histogram partitioned by predicted bank relation.

