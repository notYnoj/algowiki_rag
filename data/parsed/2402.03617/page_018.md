<tbc>diverse motions, including through actuation patterns of varying voltage/time constants and continuous input functions. Regarding the generalizability of this approach, the pMFC framework is particularly well suited for multi-limb crawling soft robots. These robots tend to use binary actuation control, have stable robot configurations throughout movement, and involve locomotion that can be modeled (or easily adapted to be modeled) as quasi-static. The framework is also applicable to a variety of different robot constructions, morphology, actuators, and number of limbs, provided that the robot locomotion adheres to the model assumptions.

Limitations of this methodology include the exponentially increasing complexity with added states and limbs; more complex solvers or non-exact solvers can be used to circumvent this complexity as more actuators are added, while patterns and probabilistic methods may need to be exploited to decrease learning time. For example, direct application of our method to robots with five or six actuators would result in graph edge learning times (i.e., continuous experimental robot operation) of 22.5 minutes and 47.3 minutes, respectively.

The experimental results performed on a planar surface are extremely promising. They validate the idea of a data-driven probabilistic model-free control framework to optimally learn about an unknown surface and synthesize the locomotion gaits in real time. The synthesized gaits have the potential to serve as starting points for other locomotion control techniques, including Reinforcement Learning (RL) and Central Pattern Generators (CPG). Furthermore, the proposed framework is sufficiently generic to be extended and applied to a diverse family of multi-limb soft robots without requiring significant modifications. In summary, it is particularly relevant for soft robots where prior knowledge of their behavior is limited. Both the assumption of planar uniform locomotion surface and temporally constant edge weights of the graph limit the applicability of this method to more challenging terrains. Subsequently, the evolution of the framework for complex and dynamic environments will involve combining this methodology with feedback control. Future work will focus on applying the synthesized gaits to soft robot locomotion control and path planning; utilizing learning methods to further tune and optimize actuation and gait parameters; developing modifications<tbc>

<tbc>to reduce learning time (e.g., through Gaussian Processes or reinforcement learning); evolving the methodology for application in more complex environments and dynamic systems; and investigating the factors contributing to increased variance in soft robot locomotion behavior, such as complex frictional interactions and the influence of the tether.

## ACKNOWLEDGMENT

The authors would like to thank Patricio Vela and Alexander Chang for invaluable discussions.

## REFERENCES

\begin{tabular}{ccccccccc}
\multirow{2}{*}{Robot} & \multirow{2}{*}{Substrate} & \multicolumn{3}{c}{Intuitive Gaits} & \multicolumn{3}{c}{Synthesized Gaits} & \multirow{2}{*}{% Improvement} \\
 & & \(\|\nu\|_\mathrm{max}\) (mm/s) & \(\|\nu\|_\mathrm{max}\) (BL/s) & \(\|\omega\|_\mathrm{max}\) (\(^\circ\)/s) & \(\|\nu\|_\mathrm{max}\) (mm/s) & \(\|\nu\|_\mathrm{max}\) (BL/s) & \(\|\omega\|_\mathrm{max}\) (\(^\circ\)/s) & \\
1 & 1 & 3.68 & 0.017 & - & 6.64 & 0.030 & - & 80.4 \\
1 & 2 & 2.89 & 0.013 & - & 7.15 & 0.033 & - & 148.0 \\
1 & 3 & 2.87 & 0.013 & - & 4.25 & 0.019 & - & 47.9 \\
2 & 1 & 3.08 & 0.009 & - & 4.73 & 0.013 & - & 53.4 \\
1 & 1 & - & - & 2.30 & - & - & 1.61 & -30.1 \\
1 & 2 & - & - & 1.48 & - & - & 4.51 & 204.8 \\
1 & 3 & - & - & 1.58 & - & - & 2.62 & 65.2 \\
2 & 1 & - & - & 4.23 & - & - & 10.61 & 150.6 \\
\multicolumn{9}{c}{Note: The maximum translation speed \(\|\nu\|_\mathrm{max}\) and maximum rotation speed \(\|\omega\|_\mathrm{max}\) for each table entry are chosen among the three intuitive gaits and the three synthesized gaits (translation-dominant and rotation-dominant gaits, respectively) for each robot-substrate pair without loss of limb. The body length (BL) is calculated as the maximum dimension of the robot in the flat (unactuated) state. BL = 220 mm for robot 1 and BL = 350 mm for robot 2.} \\
\end{tabular}

TABLE IX

SPEED AND PERFORMANCE OF GAITS.

