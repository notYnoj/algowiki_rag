## Subspace size and reconstruction.

11 shows that the full hardware samples contain 89 to 100% of the admissible modes. The small Galerkin errors therefore reflect a solve in nearly the whole admissible space, not a reduction of the subspace. Classical residual-greedy selection of the same size is as accurate or more accurate in every case, by up to eight orders of magnitude for the eight-qubit ellipse. Figure 4 compares the reconstructions at equal subspace size over the whole range of budgets. Except where both selections reach the whole sector, the hardware samples are less accurate than residual-greedy selection of the same size by factors from about 2 at the smallest budgets to about 10<sup>8</sup> for the eight-qubit ellipse. The ideal Krylov sampler, by contrast, stays within about one order of magnitude of the greedy and oracle selections for the six-qubit ellipse, although it reaches only small subspaces with these budgets. The loss of efficiency per basis state therefore comes from the hardware noise, which adds modes with negligible solution weight.

The same noise improves coverage per shot at these sizes, because it spreads shots over modes that the ideal law rarely visits. Sample-based methods aim to reduce the subspace, however, so the relevant measure is the error per basis state, and by that measure noise is harmful. A test of dimension reduction requires admissible spaces much larger than the number of distinct samples.

In summary, the experiments on two platforms confirm the measurement convention, the parity selection rule, and the replacement-noise picture of Corollary 6. The decay of the noiseless fraction per logical two-qubit gate is about 0.6% on both platforms, whereas the gate-independent loss differs. The<tbc>

(a) Ellipse 162, k = 0 (8 qubits)
(b) Replacement-noise fit
100
circuit law
IonQ Forte-1 (6 qubits)
0.5
ibm_cleveland
ibm_cleveland (6 qubits)
0.4
10-1
survival 1-p
0.3
probability
10-2
0.2
0.1
10-3
0.0
0
50
100
150
200
250
0
200
400
600
800
1000
1200
1400
mode index k1N + k2
logical two-qubit gates

(a) Ellipse 82, lonQ
(b) Ellipse 82, IBM
(c) Ellipse 162, IBM
(d) Lens 162, IBM
10-1
10-1
10-1
10-1
10-1
10-3
10-3
10-3
10-3
10-5
10-5
10-5
10-5
relative energy error
10-7
10-7
10-7
10-7
10-7
10-9
10-9
10-9
10-9
10-11
residual-greedy
10-11
10-11
10-11
10-13
oracle (largest [x2])
10-13
10-13
hardware samples
10-13
10-13
ideal Krylov sampler
10-15
10-15
10-15
0
20
40
60
0
20
40
60
0
50
100
150
200
250
0
20
40
60
subspace size [S]
subspace size [S]
subspace size [S]
subspace size [S]

**Figure 3:** IBM `ibm\_cleveland` results. (a) Circuit law (gray) and measured frequencies (red, 500 shots) for the eight-qubit ellipse at _k_=0. (b) Survival fraction 1-_p_ of the fitted replacement model versus the number of logical two-qubit gates on both platforms, with exponential fits (dashed). Points at the bottom are fully randomized circuits (_p\>_0.99).

**Figure 4:** Relative energy error of the Galerkin solution versus subspace size. Hardware samples (circles) are obtained by subsampling the measured counts at budgets of 15 to 480 shots, with the full sample as the last point; the parity filter is applied for the lens. Squares: ideal Krylov sampler with the same circuits and budgets. Solid line: classical residual-greedy selection. Dotted line: oracle selection of the largest \(|\hat{x}_\hat{z}|\). The vertical line marks the dimension of the admissible space.

