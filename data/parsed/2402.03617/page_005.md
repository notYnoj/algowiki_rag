## B. Example Robot

A deformable two-limb soft robot, shown in Fig. 1, is presented to gain a better understanding of the framework. The robot comprises a soft deformable body and a flexible hub that houses the motors of the motor-tendon actuators. The embedded tendons connected to the motors allow for controlled curling or uncurling of each limb. The limb states correspond to the discrete configurations when the limb is curled or uncurled, given as

\(\mathrm{limbstate}=\left\{\begin{array}{ c c } 0 & \mathrm{forlimbuncurled} \\ 1 & \mathrm{forlimbcurled}.
\end{array}\right.\) (6)

For a _n<sub>l</sub>_=2-limb robot with _n<sub>s</sub>_=2 states per limb, the robot can exist in _n_=(_n<sub>s</sub>)<sup>n<sub>l</sub></sup>_=4 discrete states which are different permutations of the limb states - {00},{01},{10},{11}, or _V_={_v_<sub>1</sub>_,v_<sub>2</sub>_,v_<sub>3</sub>_,v_<sub>4</sub>}. These states correspond to the different robot shapes and represent vertices of the digraph in Fig. 1. For this complete digraph, where transitions between all vertices are allowed, the number of motion primitives is _m=n(n_-1)=12. The edges \(E=\{e_1,e_2,\cdots,e_{12}\}\) are defined using the incidence matrices _B,B<sup>i</sup>_ as

