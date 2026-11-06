<tbc>One may wonder whether a gait that is synthesized to be optimal for one substrate will be optimal and/or effective on others. To investigate this, Fig. 9 visualizes the results of the translation-dominant gait <sup>1</sup>_L_<sub>_t_1</sub> and rotation-dominant gait \(^1L_{\theta 1}\) executed on all three substrates (see multimedia video attachment). Interestingly, <sup>1</sup>_L_<sub>_t_1</sub> performs comparably on the rubber mat and the whiteboard, but has a very large rotational component on the carpet. On the other hand, \(^1L_{\theta 1}\) performs similarly for the rubber mat and carpet, but has a larger rotational component on the whiteboard. These results re-affirm the need for environment-centric and data-driven gait synthesis.

## 3) Gait Synthesis for Substrate 2 (Whiteboard):

Synthesized gaits on the whiteboard are detailed in  IV and experimental plots are presented in Fig. 10 (see multimedia video attachment for <sup>2</sup>_L_<sub>_t_3</sub>). As can be seen, the gaits synthesized for this surface are different from the rubber mat ones, suggesting that gait motion and optimality are dependent on the environment (i.e., substrate). Nevertheless, the gait synthesis appears to be fairly successful, although one of the translation gaits <sup>2</sup>_L_<sub>_t_2</sub> has a large rotational component. While the hyperparameters can be tuned to avoid this, the variance in the robot motion means that expected (predicted) gait behavior may still vary from its experimental trajectory. The translation- dominant gaits are of similar speed and magnitude to those tested on the rubber mat, whereas the rotation-dominant gaits achieve much faster and precise rotation. This may suggest that it is easier for the robot to achieve rotational motion on this substrate as compared to the rubber mat.

## 4) Gait Synthesis for Substrate 3 (Carpet):

For the last substrate, the synthesized gaits for carpet are detailed in  V with the experimental results shown in Fig. 11 (see multimedia video attachment for <sup>3</sup>_L_<sub>_t_3</sub>). Carpet is assumed to be the most difficult surface tested in this experiment as (a) the loop pile texture leads to a rougher and less flat substrate that results in a much more complex robot-environment interaction, especially as silicone material can deform and interact with small hills and valleys in the material, (b) the material is much less homogeneous than the other substrates as it can wear over time, and (c) experiments show that unlike the other substrates, the robot is not able to fully uncurl the limbs at times, leading to higher variance in the motion. All three of these factors contribute to violations of the assumptions of the methodology, which dictate repeatable quasi-static motion<tbc>

\begin{tabular}{ccc}
Gait & _V(L_) & Robot States \\
<sup>1</sup>_L_<sub>_t_1</sub> & \[6,3\] & \\
<sup>1</sup>_L_<sub>_t_2</sub> & \[8,2,1\] & \\
<sup>1</sup>_L_<sub>_t_3</sub> & \[6,4,5,7,1\] & \\
<sup>1</sup>_L_<sub>\(\theta\)1</sub> & \[4,2,1\] & \\
<sup>1</sup>_L_<sub>\(\theta\)2</sub> & \[3,4,2,6,7,1\] & \\
<sup>1</sup>_L_<sub>\(\theta\)3</sub> & \[7,5,6,2,4,1\] & \\
\end{tabular}

1 Lt1
1 Lt2
1 Lt3
40
100
20
Orientation (deg)
50
y (cm)
0
-50
-20
0
20
0
20
40
60
x (cm)
Time (s)
(a)
(b)
1 L01
1 L02
1 L03
40
100
Orientation (deg)
50
20
0
-50
-20
0
20
0
20
40
60
x (cm)
Time (s)
(c)
(d)

Rubber Mat Whiteboard Carpet
40
200
Orientation (deg)
20
0
y (cm)
0
-200
-400
-40
-20
0
20
40
60
x (cm)
Time (s)
(a)
(b)
40
200
Orientation (deg)
20
0
y (cm)
0
-200
-400
-40
-20
0
20
40
60
x (cm)
Time (s)
(c)
(d)

TABLE III

TERRESORO-III SYNTHESIZED GAITS ON SUBSTRATE 1 (RUBBER MAT).

Fig. 8. Experimental results of TerreSoRo-III gaits synthesized for the rubber mat (substrate 1). The top figures plot the translation-dominant gaits (<sup>1</sup>_L_<sub>_t_1</sub>,<sup>1</sup>_L_<sub>_t_2</sub>,<sup>1</sup>_L_<sub>_t_3</sub>) with (a) the robot trajectory and (b) the global robot orientation over time, respectively. The bottom figures plot the rotation- dominant gaits (\(^1L_{\theta 1},^1L_{\theta 2},^1L_{\theta 3}\)) with (c) the robot trajectory and (d) the global robot orientation over time, respectively.

Fig. 9. TerreSoRo-III gaits synthesized for the rubber mat executed on all three substrates. Translation-dominant gait <sup>1</sup>_L_<sub>_t_1</sub> trajectory and orientation results are plotted in (a) and (b), respectively. Rotation-dominant gait \(^1L_{\theta 1}\) trajectory and orientation results are plotted in (c) and (d), respectively.

