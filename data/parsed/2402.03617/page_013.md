<tbc>(e.g., consistent curling and uncurling of the limbs) and flat and homogeneous substrates. It is therefore anticipated that the results will be poorer for this substrate. Despite this, the synthesized gaits are still fairly successful, resulting in multi- directional translation-dominant gaits and rotation-dominant gaits in both clockwise and counter-clockwise directions. One of the translation-dominant gaits <sup>3</sup>_L_<sub>_t_1</sub> has extremely limited translation, but very precise zero rotation. However, these gaits tend to be less precise (i.e., contain more variance) than those executed on the other substrates, particularly for the rotation-dominant gaits. For example, the rotation-dominant gait \(^3L_{\theta 2}\) has a large translation component and does not have a precise instantaneous center of rotation. It is also interesting that the synthesized rotation-dominant gaits have much longer sequences when compared to the other substrates.

## 5) Comparison Between BILP and Exhaustive Gait Search Results:

The gait synthesis methodology presented here attempts to overcome the computational challenges of nonlinearity and combinatorial explosion by introducing linearizations, relaxations, and simplifications that reduce the complexity and increase the tractability of the problem. To examine the degree to which these alterations affect the optimality of the solutions, we can exhaustively calculate the nonlinear cost functions _J<sub>t,nl</sub>_ and \(J_{\theta,nl}\), defined in (12), for all possible simple cycles. This is only tractable for robots of three or fewer limbs. The hyperparameter \(\lambda\) is set to 1 to equally scale the motion and variance. Fig. 12 plots one nonlinear cost function versus the inverse of the other. The Pareto front can then be seen along the upper right-hand side of the plots as the points at which<tbc>

\begin{tabular}{ccc}
Gait & _V(L_) & Robot States \\
<sup>2</sup>_L_<sub>_t_1</sub> & \[6,4,5,2\] & \\
<sup>2</sup>_L_<sub>_t_2</sub> & \[4,7,5,1\] & \\
<sup>2</sup>_L_<sub>_t_3</sub> & \[5,3\] & \\
<sup>2</sup>_L_<sub>_t_1</sub> & \[5,1\] & \\
<sup>2</sup>_L_<sub>_t_2</sub> & \[1,4,2,6\] & \\
<sup>2</sup>_L_<sub>_t_3</sub> & \[5,7,6,2\] & \\
\end{tabular}

\begin{tabular}{ccc}
Gait & _V(L_) & Robot States \\
<sup>3</sup>_L_<sub>_t_1</sub> & \[7,3\] & \\
<sup>3</sup>_L_<sub>_t_2</sub> & \[7,4,3\] & \\
<sup>3</sup>_L_<sub>_t_3</sub> & \[4,5,3,2\] & \\
<sup>3</sup>_L_<sub>_t_1</sub> & \[2,6,5,3,8,4\] & \\
<sup>3</sup>_L_<sub>_t_2</sub> & \[3,8,7,6,4,5,2\] & \\
<sup>3</sup>_L_<sub>_t_3</sub> & \[7,4,2,6,5,3,1\] & \\
\end{tabular}

2 Lt1
2 Lt2
2 Lt3
20
200
Orientation (deg)
0
0
-20
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
2 L01
2 L02
2 L03
20
Orientation (deg)
200
0
0
-20
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

3 Lt1
3 Lt2
3 Lt3
200
20
100
Orientation (deg)
0
0
-100
-20
-10
0
10
20
30
0
20
40
60
x (cm)
Time (s)
(a)
(b)
3 L01
3 L02
3 L03
200
20
Orientation (deg)
100
0
0
-100
-20
-200
0
20
40
60
x (cm)
Time (s)
(c)
(d)

TABLE IV

TERRESORO-III SYNTHESIZED GAITS ON SUBSTRATE 2 (WHITEBOARD).

Fig. 10. TerreSoRo-III gaits synthesized for the whiteboard (substrate 2). Experimental (a) trajectory and (b) rotation plots for the translation-dominant gaits (<sup>2</sup>_L_<sub>_t_1</sub>,<sup>2</sup>_L_<sub>_t_2</sub>,<sup>2</sup>_L_<sub>_t_3</sub>) are shown in addition to the (c) trajectory and (d) orientation plots for the rotation-dominant gaits (\(^2L_{\theta 1},^2L_{\theta 2},^2L_{\theta 3}\)).

TABLE V

TERRESORO-III SYNTHESIZED GAITS ON SUBSTRATE 3 (CARPET).

Fig. 11. TerreSoRo-III gaits synthesized for the carpet (substrate 3). Experimental (a) trajectory and (b) orientation plots for the translation-dominant gaits (<sup>3</sup>_L_<sub>_t_1</sub>,<sup>3</sup>_L_<sub>_t_2</sub>,<sup>3</sup>_L_<sub>_t_3</sub>) are shown in addition to the (c) trajectory and (d) orientation plots for the rotation-dominant gaits (\(^3L_{\theta 1},^3L_{\theta 2},^3L_{\theta 3}\)).

