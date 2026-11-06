<tbc>occludes one or more markers, the marker positions(s) can be reconstructed from the estimated pose by finding the nearest neighbor from the previous frame.

### C. Experimental Procedure

Experiments for each robot-environment pair are performed using the following procedure.

#### 1) Digraph Construction:

Before beginning experiments, two generic unweighted digraphs are constructed as described in Section III that are specific to the TerreSoRo-III and TerreSoRo-IV, respectively. These digraphs are environment- agnostic and are used to abstractly model all robot states and motion primitives. The TerreSoRo-III has 8 robot states with 56 motion primitives while the TerreSoRo-IV has 16 robot states with 240 motion primitives. The objective of the experiments is for the robots to learn environment-specific digraph weights and validate the synthesized environments- specific gaits.

#### 2) Edge Weight Learning Experiments:

The robot executes five randomized Eulerian cycles (Algorithm 1) and the resulting motion is recorded, as detailed in Section III-C. The total experiment time for the five trials of a given robot-environment pair is determined by \(t_\mathrm{total}=5m\tau\) for _m_ motion primitives with \(\tau\) time constant and is \(5\times(56)\times(550\mathrm{ms})=2.6\) minutes for the TerreSoRo-III and \(5\times(240)\times(450\mathrm{ms})=9.0\) minutes for the TerreSoRo-IV. These data are then processed in MATLAB to extract and sort the digraph weights as measured in the initial vertex coordinate frame.

#### 3) Gait Synthesis:

Once the edge weights of the digraph have been calculated, the translation and rotation gaits are synthesized separately using the gait synthesis algorithm, Fig. 3. The intervals for the swept hyperparameters \(\alpha_t\) and \(\alpha_\theta\) are set to \[-1,1\] to permit translation in all directions and<tbc>

<tbc>both clockwise and counterclockwise rotation, respectively. Expected gait motion is then calculated for each gait and the remaining hyperparameters (\(\beta\) and \(\gamma\)) are manually adjusted as needed to achieve useful gait motion. Tolerances (\(\varepsilon_t\) and \(\varepsilon_\theta\)) are also chosen depending on the motion and size of the robot. Third, each gait is tested for a total of 120 motion primitives (66 seconds for the TerreSoRo-III and 54 seconds for the TerreSoRo-IV) to give sufficient time to investigate the motion and variance of the gaits.

#### 4) Gait Validation Experiments:

Finally, the gait experiment data (robot trajectories and rotation over time) are processed and aligned to start at the same initial global orientation of the robot at the origin of the coordinate grid. The optimality of the optimization is explored in Section VII-A5.

## VII. RESULTS AND DISCUSSION

I presents the matrix of planned experiments aimed at investigating and analyzing the extent to which robot- environment interactions affect locomotion, and the applicability and effectiveness of the proposed gait synthesis strategy. First, both robots execute intuitive gaits that are chosen manually. Both robots lack direct robotic analogues (due to the specific combined inching and rotating motion of the limbs) and direct biological analogues (due to being rotationally symmetric with three or four limbs). Therefore, three intuitive gaits for each robot are chosen based loosely on gaits that have successfully been performed on rotationally symmetric robots and starfish. Then, gait synthesis is performed for Robot 1 (TerreSoRo-III) on three different substrates: 1) a black rubber garage mat; 2) a whiteboard; and 3) a carpet. Three translation gaits and three rotation gaits are synthesized for each substrate, and the results are recorded. For Robot 2 (TerreSoRo-IV), gait synthesis is only performed on one substrate (rubber mat), but is also performed in the case of simulated actuator failure (loss of limb scenario).

Analysis of preliminary experiments indicated a significant influence of the tether placement and direction on robot behavior. This was attributed to the weight and relative stiffness of the tether, as well as swinging of the tether when connected to an overhead component or interference with the robot when allowed to drag on the floor. To address this, the tether was redesigned to be skinnier, lighter, and more flexible. The tether connector was changed to include a vertical offset to avoid interference with the robot, and a slip ring was added to the four-limb robot. Repeatability experiments were then conducted by executing the same locomotion gait with the tether placed in different orientations relative to the robot; the results showed a significant reduction in locomotion variation<tbc>

\begin{tabular}{ccccccc}
\multirow{2}{*}{Robot} & \multicolumn{3}{c}{Substrate} & \multirow{2}{*}{Intuitive

Gaits} & \multicolumn{2}{c}{Synthesized Gaits} \\
 & 1 & 2 & 3 & & Standard & Loss-of-Limb \\
1 & \(\times\) & \(\times\) & \(\times\) & \(\times\) & \(\times\) & \\
2 & \(\times\) & & & \(\times\) & \(\times\) & \(\times\) \\
\end{tabular}

Computer with live video
Overhead webcams
Microcontroller & Power supply
Substrate 2 (whiteboard)
Robot (TerreSoRo II)
Substrate 1 (rubber mat)
Substrate 3 (carpet)

(a)

(b)

Fig. 6. (a) Experimental setup with the soft robot placed on top of a removable flat substrate with (b) alternate substrates. A tether cable connects the robot to the microcontroller, which connects to the power supply.

TABLE I

EXPERIMENT MATRIX.

