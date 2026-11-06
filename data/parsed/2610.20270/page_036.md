## Near-singular warm starts (Figure 1(c)).

The _i_-th run starts at \(Z_i^0=\bar{Z}_i+\varepsilon G_i\) with \(\varepsilon=10^{-3}\), where _G<sub>i</sub>_ has independent standard Gaussian entries in the svec coordinates. The perturbation has norm about \(\varepsilon\sqrt{N(N+1)/2}\approx 0.15\), below \(10^{-3}\|\bar{Z}_i\|_F\). So every start lies near a singular endpoint rather than at it. All 100 runs converge. The iteration counts lie in \[4,008, 5,124\] (median 4,922). Each limiting moment iterate has rank one, and each limiting certificate stays within 0.11 in Frobenius norm (about one percent of its size) of its sampled certificate _S<sub>i</sub>_. At the stated tolerance these limiting certificates have numerical rank 210, so the iteration stops at nonsingular endpoints close to the singular samples.

## A higher-degree objective.

Figure 2 repeats the full protocol of Figure 1 on PBO4-20. From the all-zeros start (panel (a)), the residual enters the same sharp linear phase after a long transient. The run converges in 50,014 iterations; on this instance the cold start happens to select a strictly complementary endpoint. Panels (b)-(c) report one hundred near-singular warm starts, generated exactly as for BQP-20q. The sampled certificates have numerical ranks 68 to 80 (median 72). The endpoints \(\bar{Z}_i\) have numerical ranks 69 to 71, with pairwise distances in \[8.6,10.0\] (the certificate norms are about 57). All 100 runs converge, in 5,420 to 5,497 iterations, and the limiting certificates again have numerical rank 210. The phenomenon, and our theory, are not special to quadratic objectives.

101
Zk1
10-4
10-9
0
25000
50000
iteration k

67
number of samples
50
25
8
0
69
70
71
rank(Zi)

10-2
Zk1
10-5
10-8
0
2000
4000
iteration k

(a) cold start, SC limit

(b) ranks of the endpoints \(\bar{Z}_i\)

(c) 100 near-singular warm starts

Figure 2: The protocol of Figure 1 on the certified dense quartic instance PBO4-20 (_N_=211, order-two quotient relaxation). (a) All-zeros start: 50,014 iterations; here the limiting pair is strictly complementary. (b) Numerical ranks of 100 sampled singular endpoints \(\bar{Z}_i\), far below _N_=211. (c) The 100 runs started near them all converge locally linearly.

