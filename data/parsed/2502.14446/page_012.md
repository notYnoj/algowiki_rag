moderate, with 3.5Gb being used for the largest dataset, LTMM. Datasets that benefit more from an increased number of repetitions are those whose relative contrast is higher (e.g. LTMM), because<tbc>

<tbc>motifs are more likely to share long hash prefix. It is important to note that the sublinear behavior in memory growth is due to our use of the tensoring implementation.

_Impact of the quantization parameter r._ In this experiment, we manually fix \(r\in\{4,8,12,16\}\) and compare it with the value automatically chosen by the algorithm using the procedure described in Section 6.1 in terms of the resulting number of distance computations, and hence running time. Figure 6 shows that the choice of _r_ has a dramatic impact on the number of distance computations. Remarkably, the value automatically picked by our algorithm in a data-dependent way (and used in the rest of the experiments we presented) attains the same performance as the best fixed parameter considered in this experiment.

## 7.5 Quality of the results

_Impact of probability threshold_ \(\delta\). We test the influence of \(\delta\) (that controls the algorithm’s failure rate) in the range from 0.05 to 0.4: larger values allow the algorithm to satisfy the stopping condition earlier, improving runtime at the cost of reduced recall. For each setting we measured the achieved recall, the relative runtime with respect to the stricter setting (\(\delta=0.05\)), and the mean absolute relative error (MARE) of distances of the returned motifs with respect to the ground truth. In Figure 7 we present the recall-efficiency trade-off. We observe that the target recall imposed with \(\delta\) is always satisfied, moreover, the fraction of time required with respect to our highest target is stable under similar contrast values (note the similar behavior of LTMM, Weather and Ruth, which share a relatively high contrast). About the quality of the discovered motifs at lower deltas, we found that the MARE never exceeds 3% for \(\delta ≤0.2\), indicating that the quality of the result is still preserved.

_Impact of noise._ In this last experiment we replicate the experimental design of [41], where the task is to reliably find motifs even when datasets are cluttered by noisy dimensions. To evaluate the robustness of our algorithm, we added from 4 to 256 additional dimensions, each being a random walk, to datasets Potentials, Evaporator, Ruth, Weather. Then we ran MOMENTI looking for the _d_-dimensional motif, with _d_ as per  2, repeating each experiment 12 times. In all settings, irrespective of the number of additional noisy dimensions, our algorithm attained recall values of 1, showing its robustness to the number of irrelevant dimensions.

## 8 CONCLUSIONS

We presented a LSH based algorithm for the motif discovery problem in multidimensional time series, with strong guarantees on the quality of the results. Experimental evidence supports the efficacy and efficiency of our approach, demonstrating that it is able to find motifs with only a fraction of all possible distance computations.

## ACKNOWLEDGMENTS

This work was supported in part by the Big-Mobility project by the University of Padova under the Uni-Impresa call, by the MUR PRIN 2022TS4Y3N EXPAND project, by MUR PNRR CN00000013 National Center for HPC, Big Data and Quantum Computing, and by Marsden Fund (MFP-UOA2226).

WEATHER
WHALES
70
0.05
0.3
10000
60
0.04
0.2
50
0.03
9000
40
0.02
0.1
30
0.01
8000
Time (s)
EL.LOAD
LTMM
57250
Memory (GB)
57000
40000
1.5
56750
56500
2
20000
1.0
56250
10
50
100
150
200
400
10
50
100
150
200
400
Repetitions L

x106
WEATHER
x106
WHALES
6
4
4
2
2
0
0
x106
EL.LOAD
x106
LTMM
Compared couples
1.5
Auto-tuned r
1.5
1.0
1.0
0.5
0.5
0.0
0.0
2
4
8
16
32
2
4
8
16
32
Discretization parameter r

1.0
EVAPORATOR
0.8
QUAKE
Fraction of Time
POTENTIALS
0.6
EL_LOAD
8
WEATHER
0.05
0.4
0.1
RUTH
0.2
0.4
LTMM
WHALES
0.5
0.6
0.7
0.8
0.9
1.0
Recall (2 1-8)

**Figure 5: Time and space requirements for motif discovery at different maximum allowed values of** _L_**.**

**Figure 6: Number of comparisons for different values of** _r_**. The red dot is the value found by the heuristic in Section 6.1.**

**Figure 7: Relation between** \(\delta\)**, represented by the markers, the measured recall and the fraction of time required with respect to the tighter bound.**

