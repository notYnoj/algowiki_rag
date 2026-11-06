<tbc>interactions and are optimally learned using stochastic Hierholzer’s algorithm. The framework also affords mathematical definition of fixed gaits as binary column vectors. This facilitates definition of locomotion gaits as simple cycles that are transformation invariant, i.e., the translation and rotation of a simple cycle are preserved irrespective of the starting vertex.

Thereafter, gaits are synthesized by optimizing a linearized cost function formulated as a BILP with linear constraints. This formulation provides a quick and tractable solution despite the problem being NP-hard and balances exploration of gaits (through LHS) with exploitation through the exact and optimal solutions obtained using MATLAB<sup>®</sup> `intlinprog`. Multiple translation and rotation gaits are synthesized using the experimentally learned graph edge weights. The resulting synthesized gaits are experimentally validated to demonstrate that the pMFC approach can synthesize locomotion gaits on unknown surfaces through optimal learning. In summary, the<tbc>

<tbc>method focuses on synthesizing gaits and is effective for robots lacking biological analogues for biomimetic gait selection and/or robust dynamic models that facilitate simulation for use in traditional learning methods. Therefore, a great application for this method is in soft robot locomotion control due to the significant simulation-to-reality gaps that currently exist with model-based methods.

The advantages to this approach include its versatility (as it is not dependent on any model or actuator type), explainability of the tunable parameters, resilience (in the case of assumption violations and actuator failure), and the optimality and diversity of the synthesized gaits. Limiting assumptions of the model include quasi-static motion primitives, flat ground (a common condition for fixed gaits), static stability of robot states following all transitions, and binary actuation states. These assumptions also exclude dynamic and more complex gaits which could potentially provide faster speed and more<tbc>

Intuitive/ Other Gaits
Synthesized Gaits
5
2.5
L1
2 L02
L1
4
1 L01
2
1 L02
Rotational Speed (deg/s)
1.5
L01
Rotational Speed (deg/s)
3
2 L03
2 Lt2
L3
L1
Lt2
2
L1
L03
L2
L1
0.5
1 Lt1
L3
L2
2 Lt1
0
Lt3
0
Lt3
1 Lt1
-0.5
-1
0
1
2
3
4
5
6
7
0
2
4
6
8
10
Translational Speed (mm/s)
Translational Speed (mm/s)
(a) Three-limb substrate 1 (rubber mat)
(b) Three-limb substrate 2 (whiteboard)
4
1 L01
1 L02
3.5
10
3
3 L02
8
Rotational Speed (deg/s)
2.5
L03
Rotational Speed (deg/s)
2
L03
L05
L1
L1 L01
6
1.5
L1
L3 L04
L2
L3 Lt3
4
L2
L1 Lt5
0.5
L3
L1 Lt2
2
L1 Lt1
Lt3 Lt4
0
L1 Lt1
-0.5
0
0
1
2
3
4
5
6
7
0
2
4
6
8
Translational Speed (mm/s)
Translational Speed (mm/s)
(c) Three-limb substrate 3 (carpet)
(d) Four-limb substrate 1 (rubber mat)

Fig. 18. Gait characterization where the height and width of the ellipsoid bubbles represent \(\pm 1\) standard deviation of rotational speed and translation speed, respectively, of a gait cycle. Red bubbles correspond to gaits synthesized for the given robot-environment pair, and grey bubbles correspond to the remaining gaits.

