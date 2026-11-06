<tbc>Instead of raising the weights to a growing _p_, one can keep a benign base _p_<sub>0</sub> and iterate, multiplying each weight by a factor of the current solution,

\(w_e\leftarrow w_e^0\rho(x_u-x_v),a_i^1\leftarrow a_i^{1,0}\rho(x_i-1),a_i^0\leftarrow a_i^{0,0}\rho(x_i),\rho(d)=\frac{\varepsilon^2}{\varepsilon^2+d^2},\) (6)

and re-solving (3) until the pair (weights, solution) stops changing. This is the half-quadratic / majorise-minimise iteration of a nonconvex piecewise-constant energy with the Geman-McClure potential [19,29]; the unaries are reweighted too because they are edges of the augmented graph. The weights stay in (0,1] and the smallest factor is set by \(\varepsilon\), not by _p_ times the cost spread, and the tiny weights appear only on the edges across which the solution jumps. The fixed point is not the PW: it is a local minimiser that depends on the starting point, which for a finishing layer is the network’s own prediction. Inner solves are implicit and the outer loop is differentiated by automatic differentiation (checked against finite differences).

### B.6 Validation against the reference implementation

Our NumPy implementation of the plateau algorithm was checked against the authors’ reference code (PW\_1.0.1, `https://sourceforge.net/projects/ powerwatershed`) on the same 4-connected graphs, integer weights and seeds: on 80 random coarsely quantised images with two to five labels and on thirteen 512<sup>2</sup> cases (synthetic, camera, astronaut; two- and multi-label) the potentials agree to single precision (maximum difference \(6\cdot 10^{-8}\), the reference stores them as float) and the labels agree on every pixel once the same rule is applied to potentials exactly equal to 0.5. The reference realises the plateaus of the merged graph through a geodesic reconstruction of the weights from the seeds; without it, its result depends on the order in which equal weights are sorted. The harness and the records are in the code repository (`experiments/pwref/`, `results/pwref/`).

## C Architectures

Figures 3 and 4 draw the four pipelines compared in the main text. In every case the convolutional part is the same small U-Net (32-64-128-256 channels); the variants differ only in the number of output channels of its last \(1\times 1\) convolution and in what consumes them. Blue: the network; orange: the WS layer, which has no trainable parameters of its own except, in later runs, one scale on the edge costs; red, dashed: operations outside the training loop; green: the losses.

## D The instance pipelines in detail

This section describes, as precisely as we can, what the WS layer and its strongest baseline do in the instance experiments of Sect. 4.4, which parts they share, and where they differ. Figure 5 follows both on the same test patches.

