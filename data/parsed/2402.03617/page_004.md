<tbc>matrix _B=B(G_)=(_b<sub>ij</sub>_) of _G_ is a \(n\times m\) matrix that associates each edge to an ordered pair of vertices:

\(b_{ij}=\left\{\begin{array}{ c c }
1 & v_i\text{is initial vertex of}e_i \\
-1 & v_i\text{is terminal vertex of}e_i \\
0 & \text{otherwise.}
\end{array}\right.\) (1)

A complete digraph is a digraph in which every pair of vertices is connected by bidirectional edge with no loops. In addition, we also define initial and terminal matrices _B<sup>i</sup>,B<sup>t</sup>_ as

\(B=B^i-B^t,\begin{array}{ c c }
b_{ij}^i=\left\{\begin{array}{ c c }
1 & v_i\text{is initial vertex of}e_i \\
0 & \text{otherwise} \\
b_{ij}^t=\left\{\begin{array}{ c c }
1 & v_j\text{is terminal vertex of}e_i \\
0 & \text{otherwise.}
\end{array}\right.\) (2)

A closed walk consists of a sequence of vertices starting and ending at the same vertex, where consecutive vertices in the sequence are connected by a directed edge. A simple cycle is a closed walk where no vertices or directed edges are repeated, other than the start and the end vertex. Let _L_ be a simple cycle in _G_ with a given sequence of vertices \(V(L)=v_1v_2\cdots v_lv_{(l+1)}\) s.t. _v_<sub>1</sub>=_v_<sub>_l_+1</sub> This can also be represented as a sequence of edges \(E(L)=e_1e_2\cdots e_l\), where _e<sub>i</sub>=v<sub>i</sub>v_<sub>_i_+1</sub>. While both of these representations contain the notion of a starting vertex _v_<sub>1</sub> or edge _e_<sub>1</sub> (i.e., a starting point to the simple cycle), a cycle can also be identified without this by a \((m\times 1)\) vector **z**=(_z<sub>i</sub>_) where

\(z_i=\left\{\begin{array}{ c c }
1 & \text{if}z_i\in E(L) \\
0 & \text{otherwise.}
\end{array}\right.\) (3)

The vector **z** is a simple cycle only if it satisfies the constraints that (1) at each vertex, the number of incoming edges is equal to the outgoing edges, _B_**z**=0, (2) the out-degree of each vertex (i.e., the number of edges for which each vertex is an initial vertex) is at most one, \(B^i\mathbf{z}\le 1\), and (3) it does not contain a sum of unconnected simple cycles. Hence, the simple cycle subspace _C_<sub>1</sub>(_G_) with linear constraints is defined as

\(C_1(G)=\left\{\begin{array}{ c c }
\mathbf{z}\in\mathbb{Z}_2^{(m\times 1)}: & B\mathbf{z}=0,B^i\mathbf{z}\le 1 \\
\#\mathbf{z}_1,\mathbf{z}_2\text{s.t.}\mathbf{z}=\mathbf{z}_1+\mathbf{z}_2,B\mathbf{z}_1=B\mathbf{z}_2=0
\end{array}\right.\) (4)

The weights associated with each of its edges **_w_**_<sub>i</sub>=w(e<sub>i</sub>_) form _W(E_), the set of edge weights.

## A. Soft Robot and Environment-specific Weighted Digraph

For a terrestrial soft robot, locomotion occurs when an imbalance of forces acting on the robot results in a net planar motion of the center of mass. This locomotion can be generally divided into three categories: static, quasi-static, and dynamic. In static locomotion, the robot is statically stable during all locomotion stages and will remain in its position if the actuation is suspended or locked. Dynamic locomotion generally exploits different strategies, including static instability, to achieve greater changes in inertia and higher magnitudes of speed. Accordingly, quasi-static locomotion can be described as locomotion that includes some dynamic behavior but is statically stable at a certain stage of motion. In the context of this research, both static and quasi-static locomotion can be<tbc>

<tbc>modeled and explored using weighted digraphs; fully dynamic motion (e.g., rolling) is not currently explored in this work.

_Robot states_ are defined as discrete statically stable robot configurations. Every soft robot thus possesses a multitude of robot states, each with varying shapes and postures that can change the distribution and magnitude of forces on the system. _Motion primitives_ refer to the possible transitions between these robot states. As these transitions can lead to force imbalances that result in locomotion, motion primitives effectively discretize the factors dominating the robot-environment interaction. For this discussion, we focus on formulating a graphical framework that methodically associates knowledge of motion primitives with environment feedback. The identification and exploration of these robot states is outside the scope of this research.

To construct the digraph, robot states are modeled as vertices _V(G_), and motion primitives are modeled as directional edges _E(G_) that connect the vertices. The resulting translation \(\mathbf{p}_i\in\mathbb{R}^{2\times 1}\) and rotation \(\theta_i\) associated with each motion primitive is then encoded in the corresponding edge weight **_w_**(_e<sub>i</sub>_), recorded in the coordinate system of the initial vertex. These motions and edge weights are environment-specific and depend on the type of surface of interaction. Hence, _these digraph weights are fundamental to robot adaptation and learning in different environments_. To account for variances in actuation and robot-environment interactions in addition to measurement noise, each edge weight **_w_**_<sub>i</sub>_ is modeled as a normal distribution with mean \(\unknown_i\in\mathbb{R}^{3\times 1}\) and covariance matrix \(\Sigma_i\in\mathbb{R}^{3\times 3}\):

\(\mathbf{w}_i=\mathcal{N}\left(\unknown_i,\Sigma_i\right),\unknown_i=\left[\begin{array}{ c }
\mathbf{p}_i \\
\theta_i
\end{array}\right],\Sigma_i=\left[\begin{array}{ c c }
\Sigma_{pp} & \Sigma_{p\theta} \\
\Sigma_{\theta p} & \Sigma_{\theta\theta}
\end{array}\right].\) (5)

The pMFC framework is summarized as a weighted robot- environment specific digraph (_G,W_) with the following elements:

1) The structure of digraph _G_ is determined by the robot:<tbc>

\(\bullet\) _n_, number of robot states or graph vertices _V(G_)<tbc>

\(\bullet\) _m_, number of motion primitives or edges _E(G_)<tbc>

\(\bullet\) _B(E_), incidence matrix of dimension \(n\times m\)<tbc>

2) The probabilistic digraph edge weights, \(W(E)=\left\{P(E),\Theta(E),S(E)\right\}\), correspond to the resulting locomotion of motion primitives and are environment- specific:<tbc>

\(\bullet\) _P(E_), mean displacement matrix of dimension \(2\times m\)<tbc>

\(\bullet\) \(\Theta(E)\), mean rotation matrix of dimension \(1\times m\)<tbc>

\(\bullet\) _S(E_), noise covariance matrix of dimension \(3\times 3\times m\) where \(S(e_i)=\Sigma_i(e_i)\)<tbc>

\(\bullet\) _S<sub>p</sub>(E_), translation covariance trace matrix of dimension \(1\times m\) where \(S_p(e_i)=\mathrm{tr}\left(\Sigma_{pp}(e_i)\right)\)<tbc>

\(\bullet\) \(S_\theta(E)\), rotation covariance matrix of dimension \(1\times m\) where \(S_\theta(e_i)=\Sigma_{\theta\theta}(e_i)\).

While discretizing the robot’s states does not affect its physical deformability and adaptability, it is essential to select states that accurately capture the key factors governing its interaction with the environment to prevent oversimplification.

