<tbc>one cost function is maximized and the other is minimized. Shading is also incorporated to indicate gait length, as shorter gaits tend to be preferable due to their simplicity. While it is assumed that some level of optimality will be compromised, the data indicate that the majority of the synthesized gaits do fall on the Pareto front, while the remaining ones fall slightly within. These plots are only shown for one dataset (the rubber mat substrate) but suggest that this gait synthesis methodology maintains a reasonable degree of optimality and experimentally produces useful gaits. Again, numerical optimality for these cost functions does not necessarily equate to experimental optimality as there is expected to be some level of variation between the predicted (i.e., expected) and experimental gait behaviors.

## B. Robot 2: TerreSoRo-IV

This section details the experimental results of both synthesized and intuitive gaits for the four-limb robot on a single substrate (rubber mat). Gaits are then re-synthesized without re-learning the graph with the added constraint that one limb is non-functioning.

### 1) Intuitive Gaits:

Intuitive gaits are first performed on the rubber mat substrate as detailed in  VI. Despite being adapted from three-limb robot intuitive gaits, the resulting behavior is different. All three gaits contain a much stronger rotational component than those seen in the three-limb robot, suggesting that this robot may be more inclined towards counter-clockwise rotation. The pronk-like gait _L_<sub>1</sub>, which would be expected to induce only rotation due to the rotational symmetry of the robot instead results in the largest translation with the smallest rotation of the three gaits; the opposite is true of the pronk-like gait for the three-limb robot. The rotary gallop-inspired gait _L_<sub>2</sub> produces relatively small translation with a rotation component, despite this pattern resulting in the largest translation for the three-limb robot. Finally, the push-pull gait, selected to produce translation, results in the<tbc>

<tbc>largest rotation and least translation of all the gaits. This contrasts with the translation-dominant nature of the three- limb push-pull gait. These experimental results underscore the difficulty of intuitively picking soft robot gaits and predicting the resulting behavior, particularly when they lack robotic or biological analogues.

### 2) Experimental Results on Substrate 1 (Rubber Mat):

Gaits for the four-limb robot are synthesized for the rubber mat substrate and presented in  VII and Fig. 14 (see multimedia video attachment for <sup>1</sup>_L_<sub>_t_1</sub>). Compared to the three-limb robot, the translation-dominant gaits have a larger rotational component and the rotation-dominant gaits achieve much larger rotation magnitudes (up to six-fold) with much smaller translation components. Additionally, no clockwise rotation-dominant gait is synthesized for the four-limb robot. These reasons suggest that this robot is more inclined towards counter-clockwise motion. Despite the strong coupling of translational and rotational motion inherent in the robot design, the synthesized gaits are successful and reasonably uncoupled. Another interesting observation is that all three translation- dominant gaits consist of the same limb being either fully curled or fully uncurled for the duration of the gait. This can essentially be interpreted as an alteration of the robot morphology to prevent rotation, similar to the way some animals drag their tails to stabilize their locomotion. The fact that this alteration occurred for every synthesized translation- dominant gait (and with the same limb) without any pre- defined knowledge of the robot highlights the versatility of this method to identify manufacturing / behavior inconsistencies and exploit them to enhance locomotion.

One of the major motivations for data-driven control of soft robots is the difficulty in eliminating or minimizing motion<tbc>

\begin{tabular}{cccc}
Gait & _V(L_) & Robot States & Inspiration \\
_L_<sub>1</sub> & \[16, 1\] & \(\rightarrow\) & pronk \\
_L_<sub>2</sub> & \[9, 5, 3, 2\] & \(\rightarrow\) & rotary gallop \\
_L_<sub>3</sub> & \[13, 16, 4, 1\] & \(\rightarrow\) & push-pull \\
\end{tabular}

Gait Length
2
3
4
5
6
7
8
0.8
Feasible Synthesized
Feasible Synthesized
0.6
0.4
1/Jt,nl
0.2
0
100
102
104
1/J0,nl
100
0
2
4
6
J0,nl
(a)
(b)

L1
L2
L3
30
400
300
20
Orientation (deg)
200
10
y (cm)
100
0
0
-10
0
10
20
0
20
40
x (cm)
Time (s)
(a)
(b)

Fig. 12. Exhaustive nonlinear cost function evaluations for all possible TerreSoRo-III gaits (simple cycles) on the rubber mat, calculated with data from Eulerian cycle experiments. Synthesized gaits (red) are plotted alongside feasible gaits of varying lengths (grey/black) to evaluate (a) translation dominance of gaits <sup>1</sup>_L_<sub>_t_1</sub>,<sup>1</sup>_L_<sub>_t_2</sub>, and <sup>1</sup>_L_<sub>_t_3</sub> and (b) rotation dominance of gaits \(^1L_{\theta 1},^1L_{\theta 2}\), and \(^1L_{\theta 3}\). Inverse cost functions 1_/J<sub>t,nl</sub>_ and \(1/J_{\theta,nl}\) are shown on the logarithmic scale.

TABLE VI

INTUITIVE GAITS FOR TERRESORO-IV (NOT SYNTHESIZED).

Fig. 13. TerreSoRo-IV intuitive gaits _L_<sub>1</sub>_,L_<sub>2</sub>, and _L_<sub>3</sub> tested on the rubber mat with experimental (a) trajectory and (b) orientation plots.

