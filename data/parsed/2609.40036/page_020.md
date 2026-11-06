_For every fixed_ 0_\<p\<p_<sub>LP</sub><sup>cert</sup>(_D,c), there is a constant_ \(\kappa>0\) _such that_

\(sup_{G\in supp\mathcal{L}_{n,D,c}}P_\mathrm{W}^\mathrm{LP}(G,p)=O_{D,c,p}(n^{-\kappa})\rightarrow 0.\) (86)

_The same conclusion holds for a uniformly random support of exactly_ \(\lfloor pm\rfloor\) _nonzero errors, where m=Dn/_2_. Both conclusions also hold for the probability of failure on the error or any one- coordinate modification, uniformly over the nonzero error values._

_Proof._ Put \(R=2(D-1)\sqrt{p(1-p)}\). The strict inequality in the hypothesis is equivalent to _R\<(D_-1)<sup>-1_/c_</sup>. Every successful output has girth at least _g(n_) from (63). For sufficiently large _n_, set _h=g(n_)-1=_c_log<sub>_D_-1</sub>_n+O_(1) in (83). Uniformly over these graphs,

\(P_\mathrm{W}^\mathrm{LP}(G,p)\le\frac{nD}{D-1}R^h=O_{D,c,p}\big(n^{1+clog_{D-1}R}\big).\) (87)

Take \(\kappa=-1-clog_{D-1}R>0\). The fixed-weight statement follows from the same finite-graph bound, and the one-coordinate statement follows from (84).

The bound holds uniformly over every graph produced by the ensemble. The certified rate is independent of _q_, because the proof uses only the error locations and discards information about the nonzero error values. It can be smaller than the actual LP threshold and does not establish the factor-(_q_-1) improvement proved for ML decoding. The guarantee applies to random error locations; but it does not imply recovery from every error pattern of linear weight. The numerical experiments in the next subsection compare the noise rates tolerated by LP decoding with the ML decoding threshold at accessible block lengths.

## 3.3.3 Numerical experiments

We tested the LP decoder on the Linial-Simkin ensemble with _c_=0.9, \(D\in\{3,5,7\}\), and prime fields F_<sub>q</sub>_ with \(q\in\{2,3,5\}\). For each degree and vertex count _n_, we sampled eight independent graphs from the LS ensemble (Definition 4). Errors were drawn from the _q_SC (Definition 3); at each noise level we used between one and eight error vectors per graph, for a total of 60,048 error samples. We solved an equivalent split-check formulation of (81) using the dual-simplex solver in HiGHS 1.15.1. Integral outputs were checked against the syndrome using exact field arithmetic. Fractional optima were counted as decoding failures, as in the definition of \(P_\mathrm{W}^\mathrm{LP}\).

Figure 1 shows the resulting _waterfall curves_, which plot the word-error rate as a function of the input symbol-error probability. Each point averages equally over the eight graphs.<sup>1</sup> As expected, the transition sharpens with block length, most clearly for the cubic graphs. For _D_=3_,q_=2, the input error probabilities at 50% word error are 0.0991,0.0919,0.0849,0.0761 with increasing instance size. The corresponding 10%-90% transition widths decrease from 0.0476 to 0.0292, 0.0212, and 0.0162. These descriptive crossing estimates use monotone interpolation of the measured curves. Both the narrowing and the movement of the transition are appreciable, so the largest measured midpoint should not be identified with any asymptotic threshold.

<sup>1</sup>The numerical choice among degenerate optima can depend on the solver state. Filled symbols use a reused solver object with its solver state cleared between calls; open symbols use a fresh object for each call, with all original samples at that point rerun. The latter points allow up to eight hours per solve. The 38 remaining unresolved samples occur at seven high-noise quinary points and are represented by intervals, never omitted or assigned a decoding outcome.

