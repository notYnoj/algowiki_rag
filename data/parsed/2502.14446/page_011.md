Note that the running times for Mstump are identical to the ones reported in  3, given that Mstump finds motifs for all dimensionalities natively. As for MOMENTI the indexing time is the same in this setting as the one reported in  3, therefore we omit it for clarity. We observe that even in this more challenging scenario our algorithm is able to discover the motifs for all dimensionalities faster than the Mstump baseline. Indeed, the running time of MOMENTI is always within a factor ≈1.6 of its running time on the one dimensional case.

To further investigate this behavior, in Figure 2 we report the relation between the discovery time of a motif (_x_ axis) and its distance (_y_ axis). Each color identifies a dataset, and each point represents a motif for some dimensionality: for instance the Weather dataset (orange) has 7 points in this figure because it has 8 dimensions, and we set the algorithms to find the 7 motifs spanning between 2 and 8 dimensions. The dashed horizontal lines mark the runtime performance of Mstump, which reports all the motifs at the same time at the end of its execution. For instance, the orange dashed horizontal line reports that Mstump takes ≈10<sup>3</sup> seconds on the Weather dataset. The times marked by dashed lines and by the rightmost points of each solid line are the same as in  6.

As can be observed in Figure 2, by virtue of how the algorithm runs, motifs at a shorter distance are found earlier. For instance, for Weather the motif of dimensionality 4 has a dist\(_4\simeq\) 49 while the motif of dimensionality 5 has dist\(_5\simeq\) 77, which requires more iterations (and thus more time) to meet the stopping condition of the algorithm. As we discussed earlier, this fact can be used in an _anytime_ fashion: the execution can be stopped at any point after the first motifs have been returned, knowing that motifs yet to be found are at larger distances and thus might be uninteresting.

## 7.3 Scalability

We now test the scalability of MOMENTI compared to Mstump. We omit EMD and RP from this comparison, as previous sections show that they do not scale beyond moderately sized time series. While the behavior of Mstump is data-independent, i.e. its running time depends only on the size of the data, for MOMENTI the running time is influenced by both the size of the time series and the contrast of the motifs. Therefore, to test the scalability in a robust way we employ our largest dataset and a synthetic one. We generate a random walk with _D_=5 of length between 10000 and 100

million, planting a sinusoidal motif of length _w_=300 across _d_=2 dimensions perturbed with Gaussian noise such that _c_<sub>2,1|_n_</sub> is 1.1. For LTMM we pick chunks of increasing size centered around the true motif, we underline that each chunk has a different contrast, so some could be harder than others for our algorithm. The results are reported in Figure 3, where both axes use a logarithmic scale. We observe that our algorithm scales better with the input size, with a sub-quadratic running time.

## 7.4 Influence of parameters on the running time

We now study the impact of the parameters _K_, _L_, and _r_ on the running time, that in the previous experiments were either fixed (_K_=8 and _L_=200) or estimated from the data (the quantization parameter _r_). Remember that our algorithm finds the correct answer with probability \(1-\delta\) for any setting of the parameters, that influence only the performance. Each experiment in the following has been repeated 10 times: the plots report the average as a colored line, additionally, a gray dashed line reports the sizes of the hash indices built under different settings. Dotted lines indicate that the result is estimated due to timeout.

_Impact of concatenations K_. We test \(K\in\{4,8,12,16\}\), reporting the results in Figure 4. We observe that a higher number of concatenations is related to longer computing times, both because more repetition of the outer loop of Algorithm 1 have to be executed and because the index construction takes longer. Conversely, using short hash values with _K_=4 incurs high execution times as well, mainly because fewer distance computations are pruned. In all tested cases the best tradeoff is achieved with _K_=8, which is the recommended value and the one we used in all previous experiments. We stress that for any value of _K_ considered in this section MOMENTI is faster than the baseline Mstump.

_Impact of repetitions L_. We test _L_ in the range from 10 to 400, setting _K_=8: a large _L_ will allow the stopping condition to be satisfied in earlier iteration of the outer loop of Algorithm 1, thus requiring fewer distance computations, at the expense of a higher index build time. Figure 5 explores this trade-off, with values of _L_ between 100 and 200 minimizing the search time. Adding more repetitions increases the memory usage, which however remains rather<tbc>

105 104 103 Time (s) 102 MSTUMP (SYNTH) 101 MOMENTI (SYNTH) MOMENTI (LTMM) 100 MSTUMP (LTMM) 104 105 106 107 108 Size

WEATHER WHALES 800 0.04 12000 600 11000 0.3 400 0.03 10000 200 9000 0.2 0
8000 0
EL.LOAD LTMM Time (s) 1.7 Memory (GB) 18000 80000 16000 1.6 14000 70000 4.0 1.5 3.5 12000 60000 3.0 10000 1.4 4
8 12 16 4
8 12 16 Concatenations K

**Figure 3: Scalability vs. input size (log scale).**

**Figure 4: Time and space requirements for motif discovery at different maximum allowed values of** _K_.

