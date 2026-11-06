<tbc>collection trial minimizes the biases that may be caused by transient effects and edge order.

### D. Framework Implementation

The implementation of the pMFC can be divided into the following steps.

#### 1) Digraph Construction:

The soft robot’s _n_ states and _m_ motion primitives are identified and used to build a robot- specific digraph with empty edge weights, as detailed in Section III-A.

#### 2) Edge Weight Learning Experiments:

Algorithm 1 is used to generate randomized sequences of robot states to fully traverse the complete digraph. This determines the control sequence for the soft robot to experimentally execute sequentially on a given substrate. The resulting translation and rotation of each motion primitive is recorded and used to calculate the corresponding edge weight according to (5) in Section III-A.

#### 3) Gait Synthesis:

Optimal translation and rotation gaits, represented by simple cycles in the graph, are then synthesized via the optimization algorithm presented in Section V-B.

#### 4) Gait Validation Experiments:

The synthesized gaits are then tested experimentally to validate the performance.

## IV. GAIT DEFINITION AND TRANSFORMATION INVARIANCE

Locomotion gaits are generally classified into two categories: fixed and free \[40\]. Fixed gaits follow the traditional definition of gaits, where an animal or robot employs a fixed periodic sequence of body movements to realize locomotion. For more versatile movement, roboticists later abstracted the idea of gaits to encompass free gaits, which comprise any sequence of motions, whether periodic or aperiodic, that move the robot between two specified locations, often considering obstacles or dynamically challenging environments. Free gaits therefore require much more computation, modeling, and sensing. We restrict our definition of gaits to the biological interpretation (i.e., fixed gaits), where gait synthesis is defined as the generation of periodic control sequences that correspond to a desired movement.

Terrestrial locomotion gaits in _SE_(2) are expected to be repeated sequentially to realize planar motion. However, the definition of locomotion gaits becomes complicated when both translation and rotation are involved. While the simple vector cycle notation defined in (3) affords simplicity in the gait definition and gait synthesis optimization problem, it does not encode a specific starting vertex _v_<sub>1</sub>. Here, we show that such ambiguity can lead to inconsistent resultant locomotion.

Let _L_ be a simple cycle with _l_ edges where each edge _e<sub>i</sub>_ has an associated initial vertex _v<sub>i</sub>_, terminal vertex _v_<sub>_i_+1</sub> and edge weight **_w_**_<sub>i</sub>_ represented in the coordinate system _i_ of the initial vertex<sup>2</sup>. Let the edge representation of _L_ be \(E(L)=e_1e_2\cdots e_l\). For kinematic analysis, the body coordinate system is fixed on the robot which translates and rotates by \(w_i=[p_i,\theta_i]^\mathsf{T}\) when executing a motion primitive, i.e., traversal along the edge _e<sub>i</sub>_ as visualized in Fig. 2 for a three-limb soft robot. The transformation matrix \(g_i\in SE(2)\) for this motion is

\(g_i=\left[\begin{array}{ c c } R(\theta_i) & p_i \\ 0 & 1
\end{array}\right],R(\theta)=\left[\begin{array}{ c c } cos\theta & -sin\theta \\ sin\theta & cos\theta \end{array}\right]\in SO(2)\)

The traversal of consecutive edges \(e_ie_{i+1}\cdots e_j,s.t.,i<j\) is captured in the transformation matrix _g<sub>i,j</sub>_

\(g_{i,j}(e_ie_{i+1}\cdots e_j)=\left[\begin{array}{ c c } R_{i,j} & p_{i,j} \\ 0 & 1
\end{array}\right]\)<br>
\(\text{s.t.}R_{i,j}=R\left(\sum_{k=i}^j\theta_k\right)\text{and}\) (9)

\(p_{i,j}=p_i+R_{i,i}p_{i+1}\cdots+R_{i,j-1}p_j=\sum_{k=i}^jR_{i,(k-1)}p_k\)<br>
\(\text{where}R_{i,i}=R(\theta_i)\text{and}R_{i,(i-1)}=I.\)

Here, the displacement **_p_**_<sub>i,j</sub>_ and rotation _R<sub>i,j</sub>_ are expressed in the coordinate system of the initial vertex of the edge _e<sub>i</sub>_. Consequently, the transformation matrix for simple cycle _L_

<sup>2</sup>The subscript _i_ in this section is meant to represent the relationship between vertices, edges, and coordinate systems to elucidate the subsequent proofs in Section IV and does not correlate to the vertex/edge numbering convention used in other sections of the paper.

**Algorithm 1:** Stochastic Hierholzer’s for complete digraphs. **Result:** Eulerian cycle (list of ordered vertices) states = \[0,1_,...,n_\] ; random.shuffle(states) ; cycle = empty list ; **for** _i_ = \[_n_-1_,...,_1,0\] **do** j = 0 ; **while** \(i\neq j\) **do** cycle.append(states\[j\]); cycle.append(states\[i\]); j = j+1 ; **end** **end** Return cycle

Fig. 2. Example planar locomotion of a three-limb soft robot where the translations and rotations are observed in the coordinate system of the initial vertex of each edge _e<sub>i</sub>_.

