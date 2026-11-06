<tbc>the same parameters and wall data as Eq. (19), we test the advantages of reduced precision and multi-GPU model parallelism in Figure 11.

For the memory-bound sparse factorization of three-dimensional systems, precision is a significant lever, since many accelerators run Float64 precision at a small fraction of their Float32 precision rate. As seen in Figure 11a, the cost of the Float32 precision solve falls by an order of magnitude at scale, and it prevents the memory overflow of the Float64 precision factor at \(1.8\times 10^6\) degrees of freedom. At matched tolerance, its final state agrees with the Float64 precision solve to within \(4\times 10^{-6}\) in relative _L_<sup>2</sup> norm at every smaller size. Consequently, if the stiffness of the problem tolerates a Float32 precision factor, reduced precision is the most effective acceleration available, especially in three dimensions where the bottleneck is the factorization of the pencil matrix. In reverse mode, the Float32 precision gradient of the Brusselator closure problem on a \(32\times 32\) grid at rtol = 10<sup>-5</sup> agrees with the Float64 precision gradient to a relative _L_<sub>2</sub> error of 10<sup>-3</sup>. Distributing the factorization across devices is a weaker lever, as seen in Figure 11b, roughly halving the cost on two devices and improving only modestly on four.

(a)
Brusselator 3D, fp64 vs fp32
(b)
Brusselator 3D, placements
fp64 solve
1 GPU
103
fp32 solve
103
1 GPU + host spill
2 GPUs
4 GPUs
102
102
wall time (s)
101
101
100
100
105
106
105
106
degrees of freedom
degrees of freedom

Figure 11: Scaling diagrams for the three-dimensional Brusselator for `diff-soup JIDA` at rtol = atol = 10<sup>-6</sup> on L40S devices, with the line style denoting the precision or the device placement as described in the legend. Wall time is measured according to the procedure described in Section 7.1, with no cap line because these runs are bounded by the scheduler slice rather than by the wall cap. Notably, data points are omitted where the factorization did not fit in memory. (a) The single-device diagram shows Float32 precision outperforming Float64 precision by an order of magnitude at scale and reaching a larger grid. (b) The placement diagram shows two devices roughly halving the cost of one and four devices improving on two with diminishing returns, with host spill keeping the largest grid solvable on one device at a far higher cost.

