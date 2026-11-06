<tbc>due to the redesigned tether, resulting in an acceptable level of repeatability.

Readers may refer to the attached multimedia for the experimental videos of selected synthesized gaits and a visual outline of the pMFC framework.

## A. Robot 1: TerreSoRo-III

This section details the results of both intuitive/ ad hoc gaits and synthesized gaits for the three-limb robot on three different substrates. The optimality of the BILP formulation approach is analyzed by comparing the results with those of an **exhaustive gait search** where the nonlinear cost functions (12) are evaluated for all possible locomotion gaits. This analysis is only performed for the three-limb robot as increasing the number of limbs (even to four limbs) leads to combinatorial explosion and the intractability of exhaustive gait search.

### 1) Intuitive Gaits:

First, manually chosen gaits are executed on all three substrates. These gaits, detailed in  II, are loosely inspired by the actuation sequences of pronk and rotary gallop gaits that are commonly executed in rotationally symmetric robots \[49\], \[50\], and push-pull gaits observed in biological starfish and starfish-inspired robots \[51\], respectively. The sequence of discrete robot states (vertices), _V(L_), for each gait is shown. Shaded (maroon) limbs represent limb actuation. As the actuation of each limb is designed to have a rotational component and is rotationally symmetric about the robot’s center hub, the intuitive belief is that the symmetric actuation sequences of both pronk and rotary gallop gaits would induce only rotation.

However, Fig. 7(a-b) shows that the pronk-like gait results in a small amount of translation on two of the substrates, indicating some unexpected asymmetrical distribution of forces. Similarly, the rotary gallop-like gait, Fig. 7(c-d), results in large net translation on two of the substrates. Finally, the push-pull gait, Fig. 7(e-f), which is expected to be translation- dominant, only achieves useful translation on carpet. These results suggest that unexpected asymmetries (which can result from several sources including manufacturing inaccuracies and surface defects of the substrate) can have substantial influence on gait behavior, hence, motivating a more data-driven approach. Further, these gaits have different performance on different substrates; the push-pull gait translates in almost the opposite direction on carpet as it does on the rubber mat and the whiteboard. This further justifies an environment-centric gait synthesis strategy.

### 2) Gait Synthesis for Substrate 1 (Rubber Mat):

III shows the synthesized gaits <sup>1</sup>_L_ for the rubber mat. The results are divided into translation-dominant gaits <sup>1</sup>_L<sub>ti</sub>_ and rotation- dominant gaits <sup>1</sup>\(L_{\theta i}\) where _i_=1,2,3. Experimental results suggest that the method is effective at finding both translation- dominant, Fig. 8(a-b), and rotation-dominant gaits, Fig. 8(c- d) (see multimedia video attachment). It should be noted that gait optimality depends on the application. For example, the translation-dominant gait <sup>1</sup>_L_<sub>_t_2</sub> has a large translation amplitude but suffers from a rotational component that may be undesirable. On the other hand, the translation-dominant gait <sup>1</sup>_L_<sub>_t_3</sub> has very stable straight-line motion but is not as fast as the other gaits. The rotation-dominant gait \(^1L_{\theta 1}\) has very minimal translation but has less precise rotational motion compared to the other rotation gaits. The proposed methodology allows the researcher to vary hyperparameters and constraints accordingly to tune these very aspects (e.g., speed, precision, and translation/rotation separation). Furthermore, it permits omnidirectional translation and is able to find both clockwise and counter-clockwise rotational gaits.

\begin{tabular}{cccc}
Gait & _V(L_) & Robot States & Inspiration \\
_L_<sub>1</sub> & \[1,8\] & \(\rightarrow\) & pronk \\
_L_<sub>2</sub> & \[2,3,5\] & \(\rightarrow\) & rotary gallop \\
_L_<sub>3</sub> & \[5,8,4,1\] & \(\rightarrow\) & push-pull \\
\end{tabular}

Rubber Mat
Whiteboard
Carpet
30
150
20
100
Orientation (deg)
50
10
0
0
-50
-10
0
10
20
0
20
40
60
x (cm)
Time (s)
(a)
(b)
30
150
20
100
Orientation (deg)
50
10
0
0
-50
-10
0
10
20
0
20
40
60
x (cm)
Time (s)
(c)
(d)
30
150
20
100
Orientation (deg)
50
10
0
0
-50
-10
0
10
20
0
20
40
60
x (cm)
Time (s)
(e)
(f)

TABLE II

TERRESORO-III INTUITIVE GAITS (NOT SYNTHESIZED).

Fig. 7. Experimental results for TerreSoRo-III performance of the intuitive gaits ( II) on three different substrates. (a,c,e) Robot trajectories and (b,d,f) global robot orientation over time are plotted for gaits _L_<sub>1</sub>, _L_<sub>2</sub>, and _L_<sub>3</sub>, respectively. Each plot contains experimental data for three different substrates: rubber mat (blue), whiteboard (orange), and carpet (yellow).

