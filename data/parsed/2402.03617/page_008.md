<tbc>The pMFC-based gait synthesis can be considered as an asymmetric traveling salesman problem, a famous NP-hard example in combinatorial optimization. Modern solutions include stochastic sampling solvers like simulated annealing, ant colony optimization, genetic algorithms, reinforcement learning (e.g., simple Q-learning or more complex deep learning approaches), and neural networks \[44\]-\[46\]. However, drawbacks to these approaches include unknown optimality and the black-box nature, which makes tuning of these solvers difficult to understand in physical terms. Therefore, a common approach is to linearize the cost function and use well-known methods like branch-and-bound which have guarantees on optimality \[46\]. Although this approach does not entirely eliminate the issue of combinatorial explosion, it provides a good balance of tractability and optimality, as discussed in further detail in Section V-C and Section VII-A5.

## B. Linearized Cost Functions

We propose modified cost functions _J<sub>t</sub>_ and \(J_\theta\), respectively, that linearly weight the locomotion, variance and gait length as

\(J_t(\mathbf{z})=\unknown_t^\mathsf{T}\underbrace{P_\mathbf{z}}_\text{translation}+\beta_t\underbrace{S_p^\mathsf{T}\mathbf{z}}_\text{variance}+\gamma_t\underbrace{1_{1\times m}\mathbf{z}}_\text{length},\)<br> \(J_\theta(\mathbf{z})=\alpha_\theta\underbrace{\Theta\mathbf{z}}_\text{rotation}+\beta_\theta\underbrace{S_\theta^\mathsf{T}\mathbf{z}}_\text{variance}+\gamma_\theta\underbrace{1_{1\times m}\mathbf{z}}_\text{length}\)

where \(P,\Theta,S_p,S_\theta\) are the graph’s translation, rotation and covariance trace matrices as summarized in Section IIIA; and \(\{\unknown_t,\beta_t,\gamma_t,\alpha_\theta,\beta_\theta,\gamma_\theta\}\) are the tunable hyperparameters. Consequently, gait synthesis is formulated as a <u>B</u>inary <u>Integer</u> Linear <u>Programming</u> (BILP) optimization problem with linear constraints that can be solved using optimization solvers, e.g., MATLAB® `intlinprog`. The optimization problem for the synthesis of a translation-dominant gait **z**_<sub>t</sub>_ is formulated as

\(min_\mathbf{z}J_t(\mathbf{z})=\left(\unknown_t^\mathsf{T}P+\beta_tS_p+\gamma_t1_{1\times m}\right)\mathbf{z}\text{s.t.}|\Theta\mathbf{z}|\le\varepsilon_\theta\mathbf{z}=0,B^i\mathbf{z}\le 1,z_i\in\{0,1\}\forall i,\#\mathbf{z}_1,\mathbf{z}_2\text{s.t.}\mathbf{z}=\mathbf{z}_1+\mathbf{z}_2,B\mathbf{z}_1=B\mathbf{z}_2=0\text{(13)}\)

where \(\varepsilon_\theta\) is a user-defined scalar that limits the total permitted rotation for a simple cycle to ensure translation-dominance. Similarly, a rotation-dominant gait \(\mathbf{z}_\theta\) can be synthesized via

\(min_\mathbf{z}J_\theta(\mathbf{z})=(\alpha_\theta\Theta+\beta_\theta S_\theta+\gamma_\theta 1_{1\times m})\mathbf{z}\text{s.t.}|P\mathbf{z}|\le\varepsilon_t\mathbf{z}=0,B^i\mathbf{z}\le 1,z_i\in\{0,1\}\forall i,\#\mathbf{z}_1,\mathbf{z}_2\text{s.t.}\mathbf{z}=\mathbf{z}_1+\mathbf{z}_2,B\mathbf{z}_1=B\mathbf{z}_2=0\text{(14)}\)

where \(\varepsilon_t\) is the user-defined maximum permitted translation. The exploration of gaits is performed by varying the hyperparameters (\(\alpha,\beta,\gamma\)), thereby varying the direction and magnitude of the translation/rotation, the variance (predictability) of the gait behavior, and the length (speed) of the gaits. Therefore,<tbc>

<tbc>an advantage of this method is the explainability of these hyperparameters, as they correspond to understandable values.

Randomized variation of the first hyperparameter \(\{\unknown_t,\alpha_\theta\}\) is achieved with <u>Latin</u> <u>Hypercube</u> <u>Sampling</u> (LHS), which produces a grid \(H\in\mathbb{R}^{N\times M}\) of sample points constrained to the interval \[0,1\]. _N_ is the user-defined number of variations, while _M_ corresponds to the length of \(\alpha\) (_M_=2 and _M_=1 for translation and rotation goals, respectively). The LHS grid can then be adapted to sweep \(\unknown_t\) and \(\alpha_\theta\) in the search spaces \(\left[-1-11-11\right]\) and \[-1,1\], respectively. This permits the exploration of omnidirectional translation and both clockwise and counterclockwise rotation. Fig. 3 details the proposed gait synthesis algorithm. Initially, the solution to the linearly constrained

BILP, (13) or (14), permits disjoint cycles. A detection step using <u>D</u>epth-<u>First</u> <u>S</u>earch (DFS) is included to check if the solution is a single simple cycle, and, if not, a cutting plane is added to the BILP that removes this solution from the feasible region.

## C. Complexity and Tractability

The gait synthesis problem remains NP-hard even in its linearized cost formulation and is complicated by the density of the directed graph and the existence of negative-weight

START Define goal TRANSLATION ROTATION BILP = Eq. 13 BILP = Eq. 14 M = 2 M = 1 Use LHS to define sampling grid Ha E R NxM = 2H 1
j = 0 Set BILP parameter(s) a = Ha[j.] = j + 1 i = 0 Call intlinprog to solve BILP Add cutting plane Run depth-first search on solution i = i + 1 YES Does solution consist of at most one cycle? NO i < L YES NO YES Store cycle j < N NO Return all cycles END

Fig. 3. Gait synthesis algorithm. Sampling grid _H_ is of size _N_ (number of variations) by _M_ (_M_=1,2 for rotation and translation gaits, respectively). _L_ is the user-defined maximum number of iterations to achieve simple cycle output.

