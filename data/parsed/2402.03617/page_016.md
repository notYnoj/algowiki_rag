<tbc>and the ellipse axes represent \(\pm 1\) standard deviation. Finally, a line that originates at (0,0) and is proportionally scaled to the data is used to divide each plot into two regions: rotation- dominance (upper left) and translation-dominance (bottom right). Data points with the smallest bubbles (i.e., smallest variance) that lie furthest from these lines are considered optimal as they achieve the best separation between rotation and translation.

There are a few observations of interest.

1) The synthesized rotation-dominant and translation- dominant gaits are generally well-separated, as indicated by the dotted line.

2) The intuitive gaits tend to lie closer to line, suggesting a greater degree of translation/rotation coupling.

3) The four-limb robot achieves the greatest speeds (both translational and rotational) with the lowest percentage of variance, but struggles to achieve near-zero translation or rotation, most likely due to its stronger rotational inclination.

4) The three-limb robot and carpet experiments produce the lowest degree of separation with the highest degree of variance.

These plots provide a concise overview of the experiments, including the degree to which the robot-environment pairs conform to the model assumptions; the three-limb carpet experiments violated methodology assumptions (e.g., lack of repeatability of quasi-static states, inconsistent curling/uncurling, uneven and heterogeneous substrate), the effect of which is clearly reflected in the gait characterization plot. As can be

seen in  IX, the methodology achieves an average speed improvement over intuitive gaits of 82% and 97% for translation and rotation, respectively, achieving maximum translation speeds of 3.68 mm/s (0.017 BL/s) and 7.15 mm/s (0.033 BL/s) as well as maximum rotation speeds of 4.23\(^\circ\)/s and 10.61\(^\circ\)/s for the TerreSoRo-III and TerreSoRo-IV, respectively. Nevertheless, these data show that the proposed gait method strategy is successful and resilient, capable of learning gaits for soft robots with unintuitive behavior, unexpected asymmetrical motion, coupled translational/rotational movements, and complex interaction with the environment even when testing for different robot morphologies, different surfaces, assumption violations, and simulated actuator failure. These experiments also emphasize the importance of considering robot-environment interactions rather than just the robot in free space, as even varying the frictional interaction between the soft robot and flat substrate can significantly alter the robot behavior and optimal locomotion gaits.

## VIII. CONCLUSION

This research demonstrates that statistical graph theory has the ability to play an instrumental role in locomotion control of soft robots in unknown environments. The probabilistic Model-Free Control (pMFC) framework is an improved environment-centric data-driven approach that affords a graphical representation to locomotion control. The structure of the digraph is robot-specific where the vertices and edges correspond to the discretized robot states and motion primitives. The probabilistic edge weights describe the robot-environment

\begin{tabular}{ccc}
Gait & _V(L_) & Robot States \\
<sup>1</sup>_Lt_<sub>3</sub> & \[3,8,1\] & \\
<sup>1</sup>_Lt_<sub>4</sub> & \[5,3,8,1\] & \\
<sup>1</sup>_L_<sub>θ3</sub> & \[4,5,6,3,2\] & \\
<sup>1</sup>_L_<sub>θ4</sub> & \[11,13,3,1\] & \\
\end{tabular}

V1
V2
V16
V1
V2
V16
V3
V15
V3
V14
V4
V14
V4
V13
V5
V13
V5
V12
V6
V12
V6
V11
V7
V11
V7
V10
V8
V10
V8
V9
V9
(a)
(b)

1 Lt4
1 Lt5
30
400
300
20
Orientation (deg)
10
200
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
1 L04
1 L05
30
400
20
300
Orientation (deg)
10
200
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
(c)
(d)

Fig. 16. Single actuator failure (loss of limb) resulting in reformulating from (a) original digraph to (b) pruned digraph. All lines connecting nodes represent bidirectional edges (i.e., two distinct robot state transitions) for ease of visualization.

TABLE VIII

TERRESORO-IV LOSS-OF-LIMB SYNTHESIZED GAITS ON RUBBER MAT.

Fig. 17. TerreSoRo-IV gaits synthesized for the rubber mat (substrate 1) in the case of single-actuator failure (loss of limb). Experimental (a) trajectory and (b) orientation plots for the translation-dominant gaits (<sup>1</sup>_Lt_<sub>4</sub>,<sup>1</sup>_Lt_<sub>5</sub>) are shown in addition to the (c) trajectory and (d) orientation plots for the rotation- dominant gaits (\(^1L_{\theta 4},^1L_{\theta 5}\)).

