<tbc>fixed, solving its system exactly at increasing _p_ ( 9). The Jacobi-PCG used in training is accurate only near the training _p_: on 256 patches it matches the exact solve to 0.015% of the pixels at \(p\le 20\), differs on 0.5% at _p_=35, and from _p_=100 reaches its iteration cap in single and double precision with 5-12% of the pixels wrong. Sparse LU also loses accuracy for \(p\ge 100\) by cancellation in the pivots. The sweep therefore uses an elimination free of subtractions (the GTH variant of Gaussian elimination, in the log domain), about 2s per patch at any _p_; its outputs sum to one within 10<sup>-13</sup>, and it agrees with sparse LU on 32 patches at \(p\le 100\) and with the training solver at \(p\le 20\).

Accuracy rises up to the training _p_ and then falls monotonically towards the limit, which the curve reaches by _p_≈500; most of the 0.07 F<sub>1</sub> and 0.06 PQ gap has opened by _p_=100. The quality of the matched nuclei (SQ) stays between 0.809 and 0.816 from _p_=20 on, so the loss is in detection. The fraction of pixels labelled unlike the limit decreases steadily; on three patches it is zero at _p_=3000, direct evidence that the finite-_p_ solve tends to our exact limit on the same costs.

The binary models behave differently (Fig. 10b). For the WS layer with learned costs of  2, trained up to _p_=50, IoU is flat up to the training _p_ (0.707-0.710) and then falls to the limit (0.660), while the instance scores of its connected components keep rising past the training _p_, to F<sub>1</sub> 0.653 and PQ 0.521 at _p_=200 against 0.602 and 0.480 at _p_=50, and stay within 0.01 F<sub>1</sub> of the limit (0.643): a higher _p_ removes the faint blobs that thresholding a soft output leaves. The same holds for a second binary model trained with an edge target on its costs (the run `edge\_bce` of the record; not the edge-target row of  2): F<sub>1</sub> 0.434 at the training _p_, 0.529 at _p_=200, 0.519 at the limit. Agreement with the limit converges more slowly than for the instance model (0.69% and 0.16% of the pixels still differ at _p_=500), since sigmoid edge costs lie in \[0,1\] and \(p\Delta c\) stays small. The layer’s PCG is accurate for the learned-cost model up to _p_=200 but not at _p_=500 (0.44% of the pixels wrong), and for the edge-target model it is wrong on 0.8-3% of the pixels from _p_=100 on; the rows of  2 are at the training _p_, where the exact solve reproduces them.

(a) instance layer (markers fixed)
(b) binary: rv_learned (solid), + edge target (dashed)
(c) pixels labelled unlike the exact limit (= 0 at =)
0.80
0.7
IoU
0.75
0.6
F1@0.5
0.70
F1@0.5
0.5
10-2
score on fold 2
score on fold 2
PQ
0.65
IoU
0.4
0.60
AjI
0.3
10-3
0.55
0.2
Instance layer (sec. 11.5)
0.50
PQ
training p (5-20)
training p (5-50)
binary rv_learned (sec. 6)
binary + edge target (sec. 10)
5
10
20
35
50
100
200
500
5
10
20
50
100
200
500
5
10
20
35
50
100
200
500
p (inverse temperature)
p (inverse temperature)
p (inverse temperature)

**Fig.10.** Accuracy on fold 2 against _p_, solved exactly with costs and markers fixed: (a) the instance WS layer, (b) two binary WS layers (learned costs, solid; with an edge target, dashed); the diamonds at \(\infty\) are the exact PW limit. (c) Fraction of pixels labelled unlike the limit; open markers at the training _p_.

