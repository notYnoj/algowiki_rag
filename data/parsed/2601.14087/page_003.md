in  I, adopting column-major ordering reduces overall BT by 14.366% compared with the non-optimized baseline. Furthermore, when applying our ordering strategies based on the input ’1’-bit count, the input-side BT decreases further, leading to overall BT reductions of 20.177% and 19.305% for ACC ordering and APP ordering, respectively.

## B. Results of DNN Workload Experiment

Fig. 3 shows our evaluation platform, which consists of a data allocation unit and 16 processing elements (PEs) implementing the first convolution and pooling layers of LeNet-5. The allocation unit supplies each PE with inputs, weights, and bias. Inside the allocation unit, the sorting unit generates sorted indices, and the transmitting units permute the data according to these indices before forwarding them to PEs.

### 1) Waveform verification of APP-PSU:

We present the waveform of four representative input patterns to illustrate the behavior of the APP-PSU. As shown in Fig. 4, output indices from buckets with higher ‘1’-bit counts are placed after those from buckets with lower counts. For (1) all-ones and (2) all- zeros patterns, the output indices follow ascending order. In the case of (3) repeated pattern whose ’1’-bit count decreases from 8 to 0, the last eight indices shown in the figure clearly illustrate the behavior of the APP ordering algorithm. The same ordering effect is observed for (4) random input pattern.

### 2) Example of ordered flits:

Fig. 2 shows a 128-bit link transmission snapshot for a single packet processed by the APP-PSU. On the input side, the ‘1’-bit counts of the transmitted values exhibit a generally decreasing trend; for example,

data with a ’1’-bit count of 7 are placed ahead of those with counts of 5 or 6, whereas the weight side remains random. This ordering reduces abrupt large popcount variations and helps maintain a small BT gradient across the link.

### 3) Sorting unit area reduction:

We synthesized four popcount-sorting unit designs - one based on the Bitonic network [10], one based on CSN [11] [12], ACC-PSU, and APP-PSU - using commercial EDA tools targeting 500 MHz in a 22 nm technology node, with all designs implemented using the same pipeline depth. The evaluation covered two convolution kernel sizes, \(5\times 5\) and \(7\times 7\). As shown in Fig. 5, APP-PSU attains the lowest area of \(2193\mu m^2\) and \(6928\mu m^2\) for the two kernel sizes, outperforming all other architectures. The approximation yields 24.9% and 36.7% area reductions in the popcount unit and sorting unit, respectively, at a kernel size of 25, resulting in an overall reduction of 35.4%.

### 4) Power result:

We evaluate post-layout power consumption with back-annotated switching activity using commercial EDA tools. A set of 100 convolution kernels is applied as test vectors to three configurations: the non-optimized baseline, ACC ordering, and APP ordering. All reported percentages are averaged. At the PE level, ACC-PSU reduces power by 4.98%, while APP-PSU achieves a 4.58% reduction. The corresponding PE power breakdown for APP ordering versus baseline is shown in Fig. 6.

