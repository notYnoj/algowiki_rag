To interpret this MILP formulation, we give the following notes:

\(\bullet\) If a bidirected reconfigurable link \(\{i,j\}\in\mathcal{E}\) is included in _M_, then both directions \((i,j)\in\vec{\mathcal{E}}\) and \((j,i)\in\vec{\mathcal{E}}\) are implemented in \(\vec{M}\) simultaneously. Let each decision variable \(z_{i,j}\in\{0,1\}\) indicate whether to select the directed reconfigurable link \((i,j)\in\vec{\mathcal{E}}\) into \(\vec{M}\) for implementation. Thus, the constraint (7) ensures the simultaneous implementation of both directions for each bidirected reconfigurable link \(\{i,j\}\in\mathcal{E}\).<tbc>

\(\bullet\) The variable \(\lambda\in\mathbb{R}^+\) indicates the maximum load for all directed links in the reconfigured network \(\left(V,\vec{E}\cup\vec{M}\right)\). Our goal is to minimize \(\lambda\) by setting these decision variables _z<sub>i,j</sub>_.<tbc>

\(\bullet\) For every two nodes \(i,j\in V\) , let P_<sub>i,j</sub>_ denote the set of all simple directed paths from _i_ to _j_ in the static network \(\left(V,\vec{E}\right)\). For each (directed) static link \(e\in\vec{E}\), let _c(e_) denote its capacity. For each demand _d<sub>i,j</sub>_, the variable _f<sub>P</sub>_ shows the flow size along a directed path \(P\in\mathcal{P}_{i,j}\). Finally, let P be the collection of all directed paths P_<sub>i,j</sub>_ for every two \(i,j\in V\) , i.e., \(\mathcal{P}=\bigcup_{i,j\in V}\mathcal{P}_{i,j}\).<tbc>

\(\bullet\) The constraints (2) ensure that each demand \(d_{i,j}\in D\) being sent on the static network \((V,\vec{E})\) if _z<sub>i,j</sub>_=0, otherwise _d<sub>i,j</sub>_ being sent on a directed reconfigurable link \((i,j)\in\vec{M}\).<tbc>

\(\bullet\) The constraints of (3) and (4) bound the maximum load on directed links in \(\vec{E}\cup\vec{M}\) by \(\lambda\).<tbc>

\(\bullet\) For the above MILP formulation, we can relax it into an LP formation in an oblivious way, by changing the integrality constraint \(\forall i,j\in V:z_{i,j}\in\{0,1\}\) to \(\forall i,j\in V:0\le z_{i,j}\le 1\), which results in _an integrality gap_ \(\ge 2\).<tbc>

\(\bullet\) To ensure that all indicator variables _z<sub>i,j</sub>_ lie in the matching polytope after relaxing \(z_{i,j}\in\{0,1\}\) to \(0\le z_{i,j}\le 1\), blossom inequalities defined by (9) are usually required. However, blossom inequalities are unnecessary for our LP since our rounding procedures can always guarantee that the generated feasible solution is a matching.

_Blossom Inequalities:_

\(\sum_{i,j\in U}z_{i,j}\le\frac{|U|-1}{2}\forall U\subseteq V:|U|\text{is odd.}\) (9)

### a) Solving LP Relaxation.:

After relaxing the above MILP, the corresponding LP relaxation can be solved efficiently, although it contains an exponential number of variables \(\{f_P:P\in\mathcal{P}\}\) and constraints (6). There are different ways to do it, but we introduce an intuitive way, often employed in approximating the min-congestion multi-commodity flow problem \[22\], \[31\]. The original LP formulation can be transferred to an equivalent LP with _a compact formulation_, where the flow for each demand \(d_{i,j}\in D\) is presented on each link, i.e., \(\left\{f_e^{i,j}\in\mathbb{R}_{\ge 0}:e\in\vec{E}\cup\vec{\mathcal{E}}\right\}\), instead of along paths in P_<sub>i,j</sub>_, and also satisfies flow conservation for all nodes. This compact LP clearly has a polynomial number of variables and constraints, which can be efficiently solved, while a solution of<tbc>

<tbc>the compact LP can be transferred to a solution of its original LP with the same load on each link.

### b) Deterministic Rounding.:

Let \(Z_{opt}=\{z_{i,j}\}_{i,j\in V}\) be an optimal solution to the LP relaxation of the above MILP. Let \(\lambda_\text{opt}\) denote the optimal congestion for the fractional optimal solution _Z_opt. Let \(\lambda_\text{min}\) denote the minimized congestion of the original ILP, which has \(\lambda_\text{opt}\le\lambda_\text{min}\). Now, we introduce our idea to obtain a feasible integer solution \(\hat{Z}=\{\hat{z}_{ij}\}_{i,j\in V}\) based on rounding each fractional variable _z<sub>i,j</sub>_ in _Z_opt.

We first consider the following rounding-up function:<tbc>

\(\hat{z}_{i,j}=\left\{\begin{array}{ c c }
1 & \text{if}z_{i,j}>1/2; \\
0 & \text{if}z_{i,j}\le 1/2.
\end{array}\right.\)

<tbc>It is easy to see that \(\hat{z}_{i,j}=\hat{z}_{j,i}\) for all \(i,j\in V\) , since _z<sub>i,j</sub>=z<sub>j,i</sub>_ in _Z_opt. For each \(i,j\in V\) , we round up its flows _f<sub>P</sub>_ for all \(P\in\mathcal{P}_{i,j}\) by the following way:

\(\hat{f}_P=\left\{\begin{array}{ c c }
f_P/\left(1-z_{i,j}\right), & \text{if}\hat{z}_{i,j}=0; \\
0 & \text{if}\hat{z}_{i,j}=1.
\end{array}\right.\)

### 2) Approximation Results:

Next, we will show several approximation results based on the above rounding-up method.

**Theorem 1.** _When_ \(\tau=SS\)_, the min-congestion reconfigurable network problem has a polynomial-time_ 2_-approximation algorithm._

_Proof:_ Due to the degree bound of one, without violating (5), each node \(i\in V\) can have at most one indicator variable \(z_{i,j}\in Z_\text{opt}\) that has _z<sub>i,j</sub>\>_1/2, where \((i,j)\in\vec{\mathcal{E}}\). Thus, by rounding up the variable _z<sub>i,j</sub>\>_1/2 to one, each node \(i\in V\) can have at most one directed reconfigurable link \((i,j)\in\vec{M}\), which implies that (5) is still satisfied by \(\hat{Z}\). For each \(i,j\in V\) , if \(\hat{z}_{i,j}=1\) then the constraint (2) is clearly satisfied as 0=0; otherwise, by summing flows \(\hat{f}_P\) for all \(P\in\mathcal{P}_{ij}\), we can have the inequality (10), still satisfying (2).

\(\sum_{P\in\mathcal{P}_{i,j}}\hat{f}_P=\sum_{P\in\mathcal{P}_{i,j}}\frac{f_P}{(1-z_{i,j})}=\frac{1}{(1-z_{i,j})}\sum_{P\in\mathcal{P}_{i,j}}f_P\)<br>
\(\ge\frac{(1-z_{i,j})d_{i,j}}{(1-z_{i,j})}=d_{i,j}\) (10)

For each directed static link \(e\in\vec{E}\), we consider the constraint (3). Note that \(\hat{f}_P>0\) holds, where \(P\in\mathcal{P}_{i,j}\) and \(i,j\in V\) , only if \(z_{i,j}\le 1/2\), which implies \(\hat{f}_P=f_P/(1-z_{i,j})\le 2f_P\). Thus, we have the following inequation.

\(\sum_{P\in\mathcal{P}:e\in P}\hat{f}_P\le\sum_{P\in\mathcal{P}:e\in P}2\cdot f_P\le 2\cdot\lambda_\text{opt}\cdot c(e)\) (11)

Regarding the constraint (4), for each \((i,j)\in\vec{\mathcal{E}}\), it implies

\(\hat{z}_{i,j}\cdot d_{i,j}\le 2\cdot z_{i,j}\cdot d_{i,j}\le 2\cdot\lambda_\text{opt}\cdot c((i,j)).\)

Now, it is safe to conclude that \(\hat{Z}\) is a feasible integer solution, and \(f:=\left\{\hat{f}_P:P\in\mathcal{P}_{i,j}\text{and}i,j\in V\right\}\) defines a feasible flow serving all demands _D_. As \(\lambda_\text{opt}\le\lambda_\text{min}\), it implies<tbc>

