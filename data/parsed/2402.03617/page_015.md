<tbc>artifacts due to small manufacturing inconsistencies. Many soft robots are designed to be symmetric but have significant biases in motion that are not captured in simulation. This further complicates motion planning, as symmetries are often exploited to simplify the control space. The presented four- limb robot is designed to be rotationally symmetric but is observed to exhibit biases in motion. To explore this, we tested symmetric permutations (i.e., 90 degree rotations of the actuation sequence) of the same translation-dominant gait <sup>1</sup>_L_<sub>_t_1</sub> and plotted the results in Fig. 15. Despite being expected to have identical translation and rotation at 90 degree rotations, the gaits, despite being individually fairly stable, possess vastly different magnitudes of translation, with one gait nearly doubling the rotation magnitude of the others. While simulation is a valuable tool for robotic control, these data emphasize a growing understanding in the soft robot community that data- driven methods (which can also augment existing simulation tools) are needed to address the unique challenges of soft robots, including that of manufacturing inconsistencies.

### 3) Loss-of-limb Scenario Experimental Results:

While the soft robotics field continues to mature, robustness remains a problem. Therefore, control algorithms should be designed to be resilient in the case of actuator failure (e.g., a tendon snapping). The proposed gait synthesis algorithm contains an input variable of functioning actuators; in the case of one or more failures, the gait synthesis can be easily and quickly recalculated by first pruning the unreachable states and edges of the digraph, as shown in Fig. 16.  VIII and Fig. 17 detail the results of the gait synthesis for loss-of-limb scenario. The "lost" limb was varied for gait synthesis and the translation-dominant and rotation-dominant gaits that exhibited the best function evaluations (i.e., best predicted trajectories and rotation values) were chosen. One limb was excluded from the limb variation in translation-dominant synthesis to avoid repeated gaits in  VII. We were able to successfully synthesize translation-dominant and rotation-dominant gaits in the case of actuator failure. One translation-dominant gait, <sup>1</sup>_L_<sub>_t_4</sub>, even exhibited higher translation magnitude with similar rotation, as compared to the previously synthesized gaits. This is expected to be due to variation between predicted and expected behavior.

## C. Gait Characterization

To summarize the experimental results and analyze the success and applicability of the proposed gait synthesis method, we can construct _gait characterization_ plots. It can be difficult to define optimality of the gaits as different factors (e.g., translation magnitude, rotation magnitude, and variance) can impact their usefulness in practice. To attempt to visualize these factors, Fig. 18 plots the experimental average translational speed versus the average rotational speed for every gait tested (both intuitive and synthesized). Bubbles (ellipses) are used to represent the data, where the centroid is the average of the data<tbc>

\begin{tabular}{ccc}
Gait & _V(L_) & Robot States \\
<sup>1</sup>_L_<sub>_t_1</sub> & \[3, 15, 1\] & \\
<sup>1</sup>_L_<sub>_t_2</sub> & \[5, 15, 1\] & \\
<sup>1</sup>_L_<sub>_t_3</sub> & \[6, 16, 2\] & \\
<sup>1</sup>\(L_{\theta 1}\) & \[13, 8, 10, 7, 11, 2\] & \\
<sup>1</sup>\(L_{\theta 2}\) & \[12, 13, 8, 10, 7\] & \\
<sup>1</sup>\(L_{\theta 3}\) & \[16, 8, 10, 7, 12, 6, 1\] & \\
\end{tabular}

1 Lt1
1 Lt2
1 Lt3
30
600
20
400
Orientation (deg)
10
200
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
1 L01
1 L02
1 L03
600
30
20
400
Orientation (deg)
10
200
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
(c)
(d)

15
150
10
Orientation (deg)
100
5
50
-5
-10
0
-5
0
5
10
0
20
40
x (cm)
Time (s)
(a)
(b)

TABLE VII

TERRESORO-IV SYNTHESIZED GAITS ON SUBSTRATE 1 (RUBBER MAT).

Fig. 14. TerreSoRo-IV gaits synthesized for the rubber mat (substrate 1). Experimental (a) trajectory and (b) rotation plots for the translation-dominant gaits (<sup>1</sup>_L_<sub>_t_1</sub>,<sup>1</sup>_L_<sub>_t_2</sub>,<sup>1</sup>_L_<sub>_t_3</sub>) are shown in addition to the (c) trajectory and (d) orientation plots for the rotation-dominant gaits (\(^1L_{\theta 1},^1L_{\theta 2},^1L_{\theta 3}\)).

Fig. 15. TerreSoRo-IV translation-dominant gait <sup>1</sup>_L_<sub>_t_1</sub> is compared with its three rotationally symmetric permutation gaits in terms of experimental (a) trajectory and (b) orientation.

